---
layout: page
title: "Artorius: FDM 3D Printer"
description: High-speed CoreXY printer designed, fabricated, tested, and revised from an older machine
img: assets/img/artoriusRevised.png
importance: 3
category: Engineering
github: https://github.com/EthanMahajan/Artorius
---

I redesigned an older BIQU B1 printer into a high-speed CoreXY machine intended to approach the performance of current consumer-grade printers.

## Ideation

The project began after repeated reliability and troubleshooting problems with the original printer. I defined a new set of design goals around speed, rigidity, serviceability, and reuse of suitable existing components.

## Design

I developed the frame, motion system, and toolhead layout in CAD, checking how components would fit together and evaluating material and fabrication requirements.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/artoriusSketch.jpg" title="Early Sketch" class="img-fluid rounded z-depth-1" style="height: 250px; object-fit: cover;" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/artoriusEarlyRender.png" title="Early CAD Renderings" class="img-fluid rounded z-depth-1" style="height: 250px; object-fit: cover;" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/toolheadMockup.jpg" title="Early Toolhead Design" class="img-fluid rounded z-depth-1" style="height: 250px; object-fit: cover;" %}
    </div>
</div>
<div class="caption">
    On the left, an early brainstorm session for the feasibility and material cost of the machine. In the middle, an early mockup of the printer without including most of the necessary components. On the right, an illustration of the toolhead I had originally designed.
</div>

## Prototype

I fabricated and assembled the first iteration from printed parts, aluminum extrusion, and electronic components. The initial build provided a physical test of the frame, gantry, and toolhead arrangement.


<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/artoriusBelts.png" title="First Revision Gantry" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/artoriusProgress.png" title="Rendering Between Revisions" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    On the left is the gantry where the toolhead will move using belts configured in a coreXY movement configuration. On the right, a photo of the stage of the printer for which I was testing where it had not yet gained the improved structural aluminum extrusion towards the top of the frame.
</div>

## Testing & Revision

Testing exposed fundamental frame and component weaknesses, which led to a second iteration. I used structural and modal analysis to guide revisions intended to reduce resonance and improve the speed and acceleration envelope. The revised build is currently being prepared for testing.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/artoriusRevised.png" title="2nd Iteration" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
Rendering of the second iteration of Artorius.
</div>

[View the Artorius repository on GitHub](https://github.com/EthanMahajan/Artorius){:target="_blank"}
