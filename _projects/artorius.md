---
layout: page
title: "Artorius: FDM 3D Printer"
description: High-speed CoreXY printer designed, fabricated, tested, and revised from an older machine
img: assets/img/artoriusRevised.png
importance: 1
project_started: June 2024
documentation_updated: 2026-10-06
category: Engineering
github: https://github.com/EthanMahajan/Artorius
---

| Role                         | Tools / methods                              | Status                          | Main result                                        |
| ---------------------------- | -------------------------------------------- | ------------------------------- | -------------------------------------------------- |
| Independent design and build | CAD, FDM fabrication, CoreXY motion, CAN bus | Operational; refinement ongoing | Working custom printer and high-speed motion tests |

Artorius is a CoreXY 3D printer I designed and built using suitable components from an older BIQU B1. It combines a custom toolhead, an extrusion frame, and serviceable electronics. The build gave me experience connecting mechanical design decisions to alignment, vibration, and actual printing behavior.

## Ideation

Repeated reliability and troubleshooting problems with the original printer prompted me to reconsider its architecture. I wanted a machine that could explore higher speeds while remaining practical to fabricate and service, rather than simply replacing individual components on the original frame.

Reusing the BIQU B1's suitable motors and 24 V supply helped define the project constraints. I focused the new design effort on the CoreXY motion system, frame, and toolhead, with rigidity, component access, and straightforward assembly as priorities alongside speed. The project became an opportunity to learn how these decisions interact once a CAD assembly becomes a working machine.

<div class="project-gallery">
    {% include figure.liquid path="assets/img/artoriusSketch.jpg" alt="Early feasibility and material-cost sketch." title="Early feasibility and material-cost sketch." class="img-fluid rounded" zoomable=true caption="Early feasibility and material-cost sketch." %}
</div>

## Design

I developed the frame, motion system, and toolhead together in CAD, checking component placement and fabrication requirements. The key tradeoffs were stiffness versus packaging, toolhead mass distribution, and using printed fixtures where custom metal parts would be harder to manufacture.

### Toolhead

I designed the toolhead from scratch around a BIQU H2 extruder and a generic four-screw hotend mounting pattern. A 5015 fan provides part cooling, while a 2510 fan cools the cold side of the hotend to help prevent heat-related clogs.

I placed the extruder motor above the aluminum extrusion and arranged the other components to keep the toolhead's center of mass close to the gantry carriage. The toolboard sits on the side nearest the electronics enclosure to shorten wire paths and simplify cable routing.

### Frame

The frame uses standard 2020 aluminum extrusion, corner connectors, and printed joining parts. I revised the initially less rigid structure with additional extrusion to reduce resonance, although the improvement was limited.

Some components extend outside the frame because the layout was already well developed before I recognized the packaging issue. That constraint led to awkward motor-mount placement and highlighted the value of planning the entire assembly early.

### Motors & Mounts

RobotDigg NEMA17 2504 motors drive the XY gantry. Their mounts use double-shear support to support higher belt tension and include cooling-fan mounts. I configured the XY drivers for approximately 2 A motor current with a 48 V supply.

The Z axis reuses less demanding motors from the BIQU B1 and runs from the 24 V system supply. Rigid front mounts and an adjustable rear mount make assembly and heated-bed attachment easier.

<div class="project-gallery">
    {% include figure.liquid path="assets/img/artoriusEarlyRender.png" alt="Early frame and motion-system CAD." title="Early frame and motion-system CAD." class="img-fluid rounded" zoomable=true caption="Early frame and motion-system CAD." %}
    {% include figure.liquid path="assets/img/toolheadMockup.jpg" alt="Early custom toolhead concept." title="Early custom toolhead concept." class="img-fluid rounded" zoomable=true caption="Early custom toolhead concept." %}
</div>

## Prototype

I fabricated the printed fixtures and assembled them with extrusion, motion components, and electronics. The first build allowed me to evaluate the gantry arrangement physically and exposed weaknesses that were less apparent in CAD. I then revised the frame and wiring while retaining usable components.

### Wiring & Electronics

Wiring was initially an afterthought, so I redesigned its routing and enclosure to improve serviceability. The side-mounted electronics enclosure has a magnetically attached service panel and fans that cool the Manta M8P motherboard and TMC5160 motor drivers.

A reused 24 V power supply powers the main system, while an added 48 V supply powers the XY motor drivers. The toolboard connects through CAN bus, reducing the wiring carried to the toolhead. Integrating the BigTreeTech Eddy probe involved substantial setup and documentation troubleshooting; the connection now works.

<div class="project-gallery">
    {% include figure.liquid path="assets/img/artoriusBelts.png" alt="First-iteration CoreXY gantry and belt routing." title="First-iteration CoreXY gantry and belt routing." class="img-fluid rounded" zoomable=true caption="First-iteration CoreXY gantry and belt routing." %}
    {% include figure.liquid path="assets/img/artoriusProgress.png" alt="Intermediate build before the additional frame extrusion." title="Intermediate build before the additional frame extrusion." class="img-fluid rounded" zoomable=true caption="Intermediate build before the additional frame extrusion." %}
</div>

## Testing & Revisions

Motion testing reached speeds of approximately 1,000 mm/s and acceleration settings in the 50,000–100,000 mm/s² range. These describe the motion limits I explored, rather than a validated operating envelope for consistently high-quality printing.

Testing also exposed limitations that extra frame extrusion did not fully resolve. Keeping the machine square and free of skew remains difficult; a front crossbar would make alignment easier in a future revision. Better component packaging, greater frame rigidity, and cleaner motor-mount placement are other priorities.

The printer is operational, but I am continuing to work toward a better balance of speed, print quality, and reliability. The preview below shows the machine printing a Benchy from several angles, filmed using my custom phone mount.

## Final Product

The current machine is operational and can print a Benchy, as shown in the preview below. The project demonstrates a complete path from custom CAD and fabrication through electronics integration and motion testing. Quality, alignment, and reliability remain active refinement goals rather than finished performance claims.

<div class="project-gallery">
    {% include figure.liquid path="assets/img/artoriusRevised.png" alt="CAD rendering of the revised Artorius assembly." title="CAD rendering of the revised Artorius assembly." class="img-fluid rounded" zoomable=true caption="CAD rendering of the revised Artorius assembly." %}
</div>

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
