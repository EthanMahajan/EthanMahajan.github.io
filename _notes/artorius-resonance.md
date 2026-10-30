---
layout: notebook-note
title: How resonances affected the design of Artorius
date: 2026-10-29
project: artorius
published: true
math: true
damping_demo: true
back_to_top: true
description: "Frame decisions, belt tension, and software input shaping in the design of Artorius."
og_image: /assets/img/notebook/artorius-resonance/y-20261018.png
sections:
  - title: Frame decisions
    id: frame-decisions
  - title: Belt tension
    id: belt-tension
  - title: Accelerations & speeds
    id: finding-accelerations--speeds-from-graphs
  - title: Input shaping & damping demo
    id: software-input-shaping--how-it-works
---

<div class="takeaway" markdown="1">

**Issue:** vibration and alignment limited confidence in repeatable print quality on Artorius.

**Changes tried:** frame support revisions, belt tuning, and software input shaping.

**Evidence:** earlier and later accelerometer plots show different responses. They help choose what to investigate next, but differing analysis methods prevent a controlled performance comparison; printed quality and reliability still need separate validation.

</div>

## Frame decisions

I used aluminum extrusion to build a frame around components reused from my BIQU B1. The choice balanced available material, assembly access, and the need to support a CoreXY gantry. Most of my available extrusion was 2020, so that became a practical constraint rather than a claim that one section is ideal for every printer.

For an ideal single-degree-of-freedom spring–mass model, the undamped natural frequency is

$$
f_n = \frac{1}{2\pi}\sqrt{\frac{k}{m}}
$$

Here $$k$$ is effective stiffness and $$m$$ is effective participating mass. This simple model helps explain the relationship; the real printer has multiple modes, joints, belts, and moving components. Toolhead mass and stationary frame mass are not interchangeable quantities in this model.

{% include figure.liquid path="assets/img/notebook/artorius-resonance/biqu-b1.png" alt="Original BIQU B1 printer before the CoreXY redesign" class="img-fluid rounded resonance-printer" zoomable=true original_link=true caption="Original BIQU B1. Reusing suitable hardware and available 2020 extrusion helped set the redesign's constraints." %}

I added extrusion after the first build, but resonance remained. Larger sections or different damping treatments would be additional design options to evaluate, not demonstrated fixes. I did not fill the frame with sand or add fluid or viscoelastic damping treatments.

## Belt tension

The two CoreXY belts coordinate toolhead motion. My tuning question was whether their measured responses were similar, alongside whether the mechanism moved freely. Belt tension should suit the mechanism; simply maximizing it or seeking the tallest peak is not a validation method.

**Reading the plots:** an accelerometer records the response while the machine is excited through a range of frequencies. The frequency axis is in Hz; power spectral density (PSD) describes how the measured signal's power is distributed across frequency. Peaks identify responses to investigate. Their height alone does not measure belt tension or establish print quality.

<div class="project-gallery resonance-comparison">
{% include figure.liquid path="assets/img/notebook/artorius-resonance/belts-20260503.png" alt="Earlier A/B belt response plot with separated peaks" class="img-fluid rounded" zoomable=true original_link=true caption="Earlier belt response — May 3, 2026. Frequency versus PSD; the belt responses show separated peaks. Peak height alone does not establish undertension." %}
{% include figure.liquid path="assets/img/notebook/artorius-resonance/belts-20261018.png" alt="Later A/B belt response plot with more closely aligned peaks" class="img-fluid rounded" zoomable=true original_link=true caption="Later belt response — October 18, 2026. The prominent peaks are more closely aligned. This documents a changed response, not an independent measurement of correct tension." %}
</div>

The later traces appear more similar than the earlier traces. Multiple peaks do not, by themselves, confirm binding, a locked bearing, or rubbing. Those remain possible inspection questions; no isolating inspection or controlled test identifying a single cause is documented here.

## Finding Accelerations & Speeds from Graphs

The Y-axis plots show the overall axis response and analysis output. They provide a starting point for firmware tuning, not a complete operating envelope.

<div class="project-gallery resonance-comparison">
{% include figure.liquid path="assets/img/notebook/artorius-resonance/y-20260212.png" alt="Earlier Y-axis response and input-shaper analysis" class="img-fluid rounded" zoomable=true original_link=true caption="Earlier Y-axis analysis — February 12, 2026. The response has several features rather than one dominant isolated peak; a cause cannot be identified from this plot alone." %}
{% include figure.liquid path="assets/img/notebook/artorius-resonance/y-20261018.png" alt="Later Y-axis response and input-shaper analysis" class="img-fluid rounded" zoomable=true original_link=true caption="Later Y-axis analysis — October 18, 2026. A more distinct peak and subpeak are visible. The subpeak's cause remains unconfirmed, and the analysis method differs from the earlier result." %}
</div>

The reported acceleration estimates were approximately **1,500 mm/s²** and **10,460 mm/s²**, **under different software/shaper analysis conditions**: one analysis used an add-on supporting smooth as well as regular resonance compensation. These values do not demonstrate a measured improvement factor in usable print acceleration.

Klipper describes its shaper acceleration estimate as a theoretical limit associated with smoothing. It is not proof of motor capability, sustainable acceleration, reliability, or print quality. See [Klipper: selecting max_accel](https://www.klipper3d.org/Measuring_Resonances.html#selecting-max_accel). Printed validation remains a separate step; the [resonance-compensation guide](https://www.klipper3d.org/Resonance_Compensation.html#selecting-max_accel) explains checking both ringing and smoothing in a test print.

{% include figure.liquid path="assets/img/notebook/artorius-resonance/speed-20261018.png" alt="Speed-dependent vibration profile with several peaks and lower-response bands" class="img-fluid rounded" zoomable=true original_link=true caption="Speed-dependent vibration analysis — October 18, 2026. Lower-response bands suggest candidate speeds to test; the plot is not a print-quality test." %}

I identified candidate bands around 56.3–71.5, 125–165, and 180–320 mm/s from this profile. These are operating choices to investigate under the recorded test conditions, not guaranteed quality ranges. Neither a lower vibration response nor the absence of another large peak establishes extrusion capacity, dimensional accuracy, or reliable printing at that speed.

## Software Input Shaping & How It Works

Input shaping changes the timing of motion commands to reduce the vibration they excite. It does not physically stiffen the frame. Mechanical changes and firmware tuning therefore belong to separate parts of the design process. [Klipper's resonance-compensation documentation](https://www.klipper3d.org/Resonance_Compensation.html) describes input shaping and the mechanical checks that precede tuning.

An illustrative linear model uses displacement $$x$$, damping coefficient $$c$$, mass $$m$$, stiffness $$k$$, and external force $$F(t)$$:

$$
m\ddot{x} + c\dot{x} + kx = F(t)
$$

Define $$\omega_n=\sqrt{k/m}$$ and damping ratio $$\zeta=c/(2\sqrt{km})$$. For the **underdamped free response**, with $$F(t)=0$$ and $$0\leq\zeta<1$$,

$$
\omega_d = \sqrt{\frac{k}{m} - \frac{c^2}{4m^2}}=\omega_n\sqrt{1-\zeta^2}
$$

$$
x(t)=e^{-\frac{c}{2m}t}\left(C_1\cos(\omega_dt)+C_2\sin(\omega_dt)\right)
$$

The constants depend on initial conditions. This decaying sinusoid is not the general solution for arbitrary forcing or for critically/overdamped cases. In the light-damping regime, damping changes frequency only slightly while changing how quickly oscillations decay; that approximation does not hold near critical damping. At critical damping and above, the free response is nonoscillatory.

{% include damping-demo.liquid %}

The demo isolates that teaching model. Artorius is a multi-mode mechanical system, and these parameters have not been fitted to its measurements. Input shaping coordinates commanded motions to reduce residual vibration; adding physical damping would be a different intervention, requiring its own design and tests.
