---
layout: notebook-note
title: How resonances affected the design of Artorius
date: 2026-10-29
project: artorius
published: true
math: true
damping_demo: true
back_to_top: true
description: What frame revisions, belt tuning, and input shaping changed on my CoreXY printer.
og_image: /assets/img/notebook/artorius-resonance/y-20261018.png
sections:
  - { title: Frame, id: frame-decisions }
  - { title: Belts, id: belt-tension }
  - { title: Speeds & acceleration, id: finding-accelerations--speeds-from-graphs }
  - { title: Input shaping, id: software-input-shaping--how-it-works }
---

Moving Artorius quickly was only part of the problem. I wanted it to print good parts at speed, and vibration could leave ringing on their surfaces. I worked on the frame, belt path, and belt tension, then used accelerometer measurements to guide input shaping.

I have the earlier and later plots, but not the raw accelerometer data needed to rerun the analysis. They show how the response changed; they do not isolate the effect of each modification.

## Frame decisions

I built the frame from aluminum extrusion, including pieces reused from my BIQU B1. Most of what I had was 2020 extrusion. It was available, inexpensive, and straightforward to assemble around the CoreXY gantry.

A simple spring–mass model explains why stiffness and moving mass matter:

$$
f_n = \frac{1}{2\pi}\sqrt{\frac{k}{m}}
$$

Here, $$k$$ is effective stiffness and $$m$$ is the mass participating in that vibration mode. Increasing stiffness or reducing that mass raises the model's natural frequency. The printer has several vibration modes, so removing stationary frame mass is not equivalent to lightening the toolhead.

{% include figure.liquid path="assets/img/notebook/artorius-resonance/biqu-b1.png" alt="Original BIQU B1 printer before the CoreXY rebuild" class="img-fluid rounded resonance-printer" zoomable=true original_link=true caption="The BIQU B1 supplied motors, aluminum extrusion, and the 24 V supply for Artorius." %}

I added extrusion after the first build, though that alone did not eliminate resonance. Larger sections and added damping are other options; I did not fill the frame with sand or use fluid or viscoelastic damping.

A Fusion modal-analysis file is available for examining predicted vibration shapes. I have not included its results here, so the discussion below uses the measured response plots.

## Belt tension

CoreXY uses two belts, usually called A and B, that work together to move the toolhead. I wanted their responses to be similar while keeping the mechanism moving freely. Tightening both as far as possible was not the goal.

For these plots, the printer moves through a range of excitation frequencies while an accelerometer records the response. The horizontal axis is frequency in Hz; power spectral density (PSD) shows how the signal's power is distributed across those frequencies.

<div class="project-gallery resonance-comparison">
{% include figure.liquid path="assets/img/notebook/artorius-resonance/belts-20260503.png" alt="Earlier A and B belt response plot with separated peaks" class="img-fluid rounded" zoomable=true original_link=true caption="May 3, 2026: the two belt responses have separated peaks." %}
{% include figure.liquid path="assets/img/notebook/artorius-resonance/belts-20261018.png" alt="Later A and B belt response plot with more closely aligned peaks" class="img-fluid rounded" zoomable=true original_link=true caption="October 18, 2026: the prominent peaks are more closely aligned." %}
</div>

The later traces look more alike after work on the belt system. Peak height alone does not tell me whether a belt is correctly tensioned. Likewise, multiple peaks can prompt a check for binding or rubbing, but they do not identify a failed bearing or a single cause.

<h2 id="finding-accelerations--speeds-from-graphs">Choosing speeds and acceleration</h2>

The Y-axis plots show how the machine's response changed between the early build and the revised hardware. Between February and October, I revised the frame support, improved belt routing, and tuned belt tension. The later measurement follows that work; the change in analysis software was secondary.

{% include figure.liquid path="assets/img/notebook/artorius-resonance/y-20260212.png" alt="Earlier Y-axis response with several separated resonance peaks" class="img-fluid rounded" zoomable=true original_link=true caption="February 12, 2026: the early hardware's Y-axis response, with strong peaks spread across a wide frequency range." %}

The early response is spread across several strong peaks, roughly from 30 to 135 Hz. That makes it difficult to suppress the vibration with a shaper tuned around one narrow frequency band. The suggested 3HUMP_EI shaper covers a broader response, but its smoothing limits the suggested acceleration to about **1,500 mm/s²**. The problem is the spread of the response, not simply the height of one peak.

My suspicion was that several mechanical problems were contributing at once: frame flex, uneven belt behavior, and friction in the belt path. Improving frame support and belt routing gave me concrete places to start. Binding, a bearing that does not turn freely, or a belt rubbing a nearby part would also be worth checking. The graph alone cannot tell me which of those caused a particular peak.

{% include figure.liquid path="assets/img/notebook/artorius-resonance/y-20261018.png" alt="Later Y-axis response after frame and belt revisions, with a dominant peak near 63 Hz" class="img-fluid rounded" zoomable=true original_link=true caption="October 18, 2026: after frame-support revisions, belt-path improvements, and tension tuning. The response is concentrated around a dominant peak and a smaller neighboring peak." %}

After those hardware changes, most of the response is concentrated near **63 Hz**, with a smaller neighboring peak, rather than spread across several widely separated peaks. That is a more manageable response for input shaping: the shaper can target a narrower frequency range. I see the cleaner shape as the main improvement from the mechanical work. A lower peak height is not the goal by itself.

The remaining subpeak still needs investigation. I suspect unnecessary belt friction, possibly from a bearing or rubbing at some positions, and would check that the full belt path moves freely before making further changes. That is a working hypothesis, not a confirmed diagnosis.

The later analysis suggests approximately **10,460 mm/s²**. It also uses different software with smooth as well as regular shapers, so the two acceleration recommendations are not directly comparable. That software difference affects the fit and recommendation; it does not by itself explain the cleaner measured response after the hardware revisions. Printed parts are still needed to establish usable printing acceleration.

[Klipper's acceleration estimate](https://www.klipper3d.org/Measuring_Resonances.html#selecting-max_accel) concerns input-shaper smoothing. I still need printed parts to judge ringing, detail, and quality at a chosen setting.

{% include figure.liquid path="assets/img/notebook/artorius-resonance/speed-20261018.png" alt="Vibration response at different travel speeds" class="img-fluid rounded" zoomable=true original_link=true caption="October 18, 2026: lower-response bands suggest speeds to try in a print profile." %}

This profile suggests candidate bands around **56.3–71.5**, **125–165**, and **180–320 mm/s**. They avoid some of the larger vibration peaks under these test conditions. Extrusion capacity and cooling impose separate limits.

**November 3 update:** I have now confirmed motion at **1,000 mm/s and 250,000 mm/s²**. With flow expected to max out around **50 mm³/s**, a **0.25 mm layer height** and **0.5 mm line width** give an estimated **400 mm/s** extrusion limit for the **0.5 mm nozzle**. These motion and flow figures answer different questions from the shaper estimates above. Better cooling, print-quality tuning, and a full enclosure are next.

<h2 id="software-input-shaping--how-it-works">How input shaping helps</h2>

[Input shaping](https://www.klipper3d.org/Resonance_Compensation.html) changes the timing of motion commands so the vibrations they excite partly cancel. It reduces residual vibration without physically stiffening the frame.

Damping is different: it dissipates energy so oscillation decays. The demo below shows that effect in a simple spring–mass model. Under light damping, changing damping affects decay much more than frequency; near critical damping that approximation no longer holds. At critical damping and above, the free response no longer oscillates.

<details class="model-details" markdown="1">
<summary>The spring–mass equations</summary>

For displacement $$x$$, mass $$m$$, damping coefficient $$c$$, stiffness $$k$$, and applied force $$F(t)$$:

$$
m\ddot{x} + c\dot{x} + kx = F(t)
$$

Define $$\omega_n=\sqrt{k/m}$$ and $$\zeta=c/(2\sqrt{km})$$. For the underdamped free response, $$F(t)=0$$ and $$0\leq\zeta<1$$:

$$
\omega_d = \sqrt{\frac{k}{m} - \frac{c^2}{4m^2}}=\omega_n\sqrt{1-\zeta^2}
$$

$$
x(t)=e^{-\frac{c}{2m}t}\left(C_1\cos(\omega_dt)+C_2\sin(\omega_dt)\right)
$$

The constants depend on initial conditions. This solution does not cover arbitrary forcing or critically/overdamped cases.

</details>

{% include damping-demo.liquid %}

The demo's parameters are not fitted to Artorius. I used frame and belt changes plus input shaping on the printer; adding physical damping would be a separate experiment.
