(() => {
  "use strict";

  // Analytical free response: m x'' + c x' + k x = 0, x(0) = 1, x'(0) = 0.
  // Fixed m = 1 kg and k = 1 N/m give omega_n = 1 rad/s; c = 2 zeta.
  function displacement(time, zeta) {
    if (Math.abs(zeta - 1) < 1e-10) return Math.exp(-time) * (1 + time);
    if (zeta < 1) {
      const ratio = Math.sqrt(1 - zeta * zeta);
      return Math.exp(-zeta * time) * (Math.cos(ratio * time) + (zeta / ratio) * Math.sin(ratio * time));
    }
    const root = Math.sqrt(zeta * zeta - 1);
    const slow = -zeta + root;
    const fast = -zeta - root;
    return (fast * Math.exp(slow * time) - slow * Math.exp(fast * time)) / (fast - slow);
  }

  // Keep the analytical response independently checkable without a browser.
  if (typeof module !== "undefined" && module.exports) module.exports = { displacement };
  if (typeof document === "undefined") return;

  document.querySelectorAll("[data-damping-demo]").forEach((demo) => {
    const slider = demo.querySelector("input");
    const picker = demo.querySelector("[data-damping-picker]");
    const summary = picker.querySelector("summary");
    const options = [...picker.querySelectorAll("[data-damping-option]")];
    const presets = { none: 0, underdamped: 0.12, critical: 1, overdamped: 1.25 };
    const svg = demo.querySelector("svg");
    const grid = demo.querySelector("[data-damping-grid]");
    const curve = demo.querySelector("[data-damping-curve]");
    const value = demo.querySelector("[data-damping-value]");
    const classification = demo.querySelector("[data-damping-class]");
    const frequency = demo.querySelector("[data-damping-frequency]");
    const ns = "http://www.w3.org/2000/svg";

    function element(tag, attributes, text) {
      const node = document.createElementNS(ns, tag);
      if (tag === "text") node.setAttribute("fill", "currentColor");
      Object.entries(attributes).forEach(([key, val]) => node.setAttribute(key, val));
      if (text !== undefined) node.textContent = text;
      grid.append(node);
    }

    function draw() {
      const zeta = Number(slider.value);
      const width = Math.max(240, demo.clientWidth);
      const height = width < 500 ? 290 : 340;
      const left = 52;
      const right = width - 14;
      const top = 16;
      const bottom = height - 48;
      const x = (t) => left + (t / 20) * (right - left);
      const y = (v) => top + ((1.1 - v) / 2.2) * (bottom - top);
      svg.setAttribute("viewBox", `0 0 ${width} ${height}`);
      svg.style.height = `${height}px`;
      grid.replaceChildren();

      for (let t = 0; t <= 20; t += 5) {
        element("line", { x1: x(t), x2: x(t), y1: top, y2: bottom, class: "damping-demo__grid" });
        element("text", { x: x(t), y: bottom + 21, "text-anchor": "middle" }, String(t));
      }
      for (const v of [-1, -0.5, 0, 0.5, 1]) {
        element("line", { x1: left, x2: right, y1: y(v), y2: y(v), class: v === 0 ? "damping-demo__zero" : "damping-demo__grid" });
        element("text", { x: left - 10, y: y(v) + 4, "text-anchor": "end" }, String(v));
      }
      element("text", { x: (left + right) / 2, y: height - 5, "text-anchor": "middle" }, "Time (s)");
      element("text", { transform: `translate(14 ${(top + bottom) / 2}) rotate(-90)`, "text-anchor": "middle" }, "Normalized displacement");

      const points = [];
      for (let i = 0; i <= 1000; i++) {
        const t = (20 * i) / 1000;
        points.push(`${i ? "L" : "M"}${x(t).toFixed(3)},${y(displacement(t, zeta)).toFixed(3)}`);
      }
      curve.setAttribute("d", points.join(" "));
      value.textContent = zeta.toFixed(2);
      const mode = zeta === 0 ? "none" : zeta < 1 ? "underdamped" : zeta === 1 ? "critical" : "overdamped";
      classification.textContent = options.find((option) => option.dataset.dampingOption === mode).textContent;
      options.forEach((option) => option.setAttribute("aria-pressed", String(option.dataset.dampingOption === mode)));
      frequency.textContent = zeta < 1 ? `${(Math.sqrt(1 - zeta * zeta) * 100).toFixed(1)}%` : "Not applicable (nonoscillatory)";
      slider.setAttribute("aria-valuetext", `${zeta.toFixed(2)}, ${classification.textContent}`);
    }

    let frame;
    function scheduleDraw() {
      cancelAnimationFrame(frame);
      frame = requestAnimationFrame(draw);
    }
    slider.addEventListener("input", scheduleDraw);
    options.forEach((option) => {
      option.addEventListener("click", () => {
        slider.value = presets[option.dataset.dampingOption];
        picker.open = false;
        summary.focus({ preventScroll: true });
        scheduleDraw();
      });
    });
    picker.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        picker.open = false;
        summary.focus({ preventScroll: true });
        event.preventDefault();
      }
    });
    document.addEventListener("click", (event) => {
      if (!picker.contains(event.target)) picker.open = false;
    });
    new ResizeObserver(scheduleDraw).observe(demo);
    draw();
  });
})();
