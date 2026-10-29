"use strict";

// Check the analytical model through independent initial-condition and ODE tests.
// Accept the generated/minified script too, to validate the published code path.
const assert = require("node:assert/strict");
const path = require("node:path");
const { displacement } = require(path.resolve(process.argv[2] || "assets/js/damping-demo.js"));

const near = (actual, expected, tolerance, message) => {
  assert.ok(Number.isFinite(actual) && Math.abs(actual - expected) <= tolerance, `${message}: got ${actual}, expected ${expected}`);
};

for (const zeta of [0, 0.12, 0.5, 0.99, 1, 1.01, 1.25]) {
  const h = 0.0001;
  near(displacement(0, zeta), 1, 1e-12, `Initial displacement at ζ=${zeta}`);
  near((displacement(h, zeta) - displacement(-h, zeta)) / (2 * h), 0, 1e-7, `Initial velocity at ζ=${zeta}`);
  for (const t of [0.5, 1, 3, 10]) {
    const x = displacement(t, zeta);
    const velocity = (displacement(t + h, zeta) - displacement(t - h, zeta)) / (2 * h);
    const acceleration = (displacement(t + h, zeta) - 2 * x + displacement(t - h, zeta)) / (h * h);
    near(acceleration + 2 * zeta * velocity + x, 0, 1e-6, `ODE residual at ζ=${zeta}, t=${t}`);
  }
  if (zeta >= 1) {
    let previous = 1;
    for (let t = 0.1; t <= 20; t += 0.1) {
      const value = displacement(t, zeta);
      assert.ok(value >= 0 && value <= previous, `Non-oscillatory decay at ζ=${zeta}, t=${t}`);
      previous = value;
    }
  }
}

for (const t of [0, 1, 5, 20]) {
  near(displacement(t, 0), Math.cos(t), 1e-12, "Undamped response");
  for (const zeta of [0.999999, 1.000001]) {
    near(displacement(t, zeta), displacement(t, 1), 1e-5, "Continuity at critical damping");
  }
}

console.log("PASS: damping initial conditions, ODE residuals, non-oscillatory decay, and continuity at critical damping");
