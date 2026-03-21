---
layout: page
title: Artorius
description: High-Speed, Reliable coreXY 3D Printer
img: assets/img/artoriusRevised.png
importance: 3
category: fun
---

I recycled my old cartesian style 3D printer into a new-generation machine to perform as well as current day consumer-grade printers, if not better.

Initially, this project started out as a grievance with my old BIQU B1 3D printer because it would struggle to print when I needed it to leading to multiple-day troubleshooting sessions, so something had to change. I realized that I could redesign the printer from the ground up to not only fix the existing issues but also add new features. Thus, I got to work thinking about how it would work; designing how the parts would mesh together; and checking for existing parts that fit my design goals.

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

Once I had the design firmly finished, I started ordering the parts and building the printer. After every part had arrived, I got to work assembling and testing this first iteration for performance. This led to me recognizing my design had flaws that were fundamental to the frame as well as other components, so I got back to designing as shown in the photos below.


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

Now, equipped with the fixes to my previous iteration, I can reconstruct the printer to full form as pictured below. I am yet to test this revision as I am still readying the printed parts, aluminum extrusion, and electronics, but having run modal and structural analysis on this frame, I am expecting significant performance improvements in regards to resonances which directly correlate to the maximum speeds and accelerations.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/artoriusRevised.png" title="2nd Iteration" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Rendering of the second iteration of Artorius.
</div>
