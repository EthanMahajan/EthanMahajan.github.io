---
layout: page
title: "Artorius: FDM 3D Printer"
description: High-speed CoreXY printer designed, fabricated, tested, and revised from an older machine
img: assets/img/artoriusRevised.png
importance: 3
category: Engineering
github: https://github.com/EthanMahajan/Artorius
---

Artorius is a working CoreXY 3D printer that I designed and built using parts from an older BIQU B1. The project combines a custom toolhead, an extrusion frame, high-speed XY motion, and serviceable electronics. Building and testing it taught me how frame rigidity, alignment, component placement, and wiring affect real printing performance.

## Ideation

The project began after repeated reliability and troubleshooting problems with the original printer. I defined a new set of design goals around speed, rigidity, serviceability, and reuse of suitable existing components.

## Design

I developed the frame, motion system, and toolhead in CAD around speed, practical fabrication, and reuse of suitable components.

### Toolhead

I designed the toolhead from scratch around a BIQU H2 extruder and a generic four-screw hotend mounting pattern. A 5015 fan provides part cooling, while a 2510 fan cools the cold side of the hotend to help prevent heat-related clogs.

I placed the extruder motor above the aluminum extrusion and arranged the other components to keep the toolhead's center of mass close to the gantry carriage. The toolboard sits on the side nearest the electronics enclosure to shorten wire paths and simplify cable routing.

### Frame

The frame uses standard 2020 aluminum extrusion, corner connectors, and printed joining parts. I revised the initially less rigid structure with additional extrusion to reduce resonance, although the improvement was limited.

Some components extend outside the frame because the layout was already well developed before I recognized the packaging issue. That constraint led to awkward motor-mount placement and highlighted the value of planning the entire assembly early.

### Motors & Mounts

RobotDigg NEMA17 2504 motors drive the XY gantry. Their mounts use double-shear support to support higher belt tension and include cooling-fan mounts. I configured the XY drivers for approximately 2 A motor current with a 48 V supply.

The Z axis reuses less demanding motors from the BIQU B1 and runs from the 24 V system supply. Rigid front mounts and an adjustable rear mount make assembly and heated-bed attachment easier.

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

I fabricated and assembled the printer from aluminum extrusion, custom printed parts, and electronic components. The initial build gave me a physical test of the frame, gantry, and toolhead arrangement, and the revised machine now prints successfully.

### Wiring & Electronics

Wiring was initially an afterthought, so I redesigned its routing and enclosure to improve serviceability. The side-mounted electronics enclosure has a magnetically attached service panel and fans that cool the Manta M8P motherboard and TMC5160 motor drivers.

A reused 24 V power supply powers the main system, while an added 48 V supply powers the XY motor drivers. The toolboard connects through CAN bus, reducing the wiring carried to the toolhead. Integrating the BigTreeTech Eddy probe involved substantial setup and documentation troubleshooting; the connection now works.

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

Motion testing reached speeds of approximately 1,000 mm/s and acceleration settings in the 50,000–100,000 mm/s² range. These describe the motion limits I explored, rather than a validated operating envelope for consistently high-quality printing.

Testing also exposed limitations that extra frame extrusion did not fully resolve. Keeping the machine square and free of skew remains difficult; a front crossbar would make alignment easier in a future revision. Better component packaging, greater frame rigidity, and cleaner motor-mount placement are other priorities.

The printer is operational, but I am continuing to work toward a better balance of speed, print quality, and reliability. The preview below shows the machine printing a Benchy from several angles, filmed using my custom phone mount.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/artoriusRevised.png" title="2nd Iteration" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
Rendering of the second iteration of Artorius.
</div>

## Project Video

<div class="embed-responsive embed-responsive-16by9 rounded z-depth-1">
    <iframe
        class="embed-responsive-item"
        src="https://www.youtube-nocookie.com/embed/ifcJKhLbfP0"
        title="Artorius CoreXY 3D Printer — features and Benchy printing preview"
        loading="lazy"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen
    ></iframe>
</div>

<div class="caption">
    Artorius printing a Benchy, with an overview of the custom toolhead, frame, motor mounts, and electronics.
</div>

[Watch the Artorius preview on YouTube](https://www.youtube.com/watch?v=ifcJKhLbfP0){:target="\_blank"}

[View the Artorius repository on GitHub](https://github.com/EthanMahajan/Artorius){:target="\_blank"}
