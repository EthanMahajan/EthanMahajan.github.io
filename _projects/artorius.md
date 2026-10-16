---
layout: page
back_to_top: true
title: "Artorius: FDM 3D Printer"
description: High-speed CoreXY printer designed, fabricated, tested, and revised from an older machine
og_image: /assets/img/social/artorius.png
img: assets/img/artoriusRevised.png
importance: 1
project_started: June 2024
documentation_updated: 2026-10-06
category: Engineering
github: https://github.com/EthanMahajan/Artorius
cad_model: /assets/models/artorius/artorius.3mf
card_label: Independent build
card_description: "Custom CoreXY printer: operational hardware, a revised frame, and integrated CAN-bus electronics."
hero:
  image: assets/img/artoriusRevised.png
  alt: Revised CAD assembly of the Artorius CoreXY printer
  caption: "Revised CAD assembly. The linked case study includes footage of the operational printer."
  video_lead: true
  video: ifcJKhLbfP0
  video_caption: "Custom toolhead, frame, and electronics, followed by Benchy printing footage."
portfolio: true
pdf_summary:
  design: "Recurring problems with an older BIQU B1 led me to redesign its architecture around reusable motors and a 24 V supply. I developed a CoreXY frame, motion system, and custom toolhead in CAD, fabricated fixtures, assembled the machine, and integrated CAN-bus electronics with a serviceable enclosure."
  evidence: "The printer is operational and the linked video shows Benchy printing. Motion tests explored approximately 1,000 mm/s; this is not a validated print-quality speed. Extra frame support did not fully resolve resonance. Alignment, packaging, vibration, and repeatable print quality remain refinement priorities."
portfolio_highlights:
  - Designed the frame, motion system, and custom toolhead together in CAD around reusable components.
  - Fabricated fixtures, assembled the machine, and integrated a CAN-bus toolboard and serviceable electronics.
  - Motion tests explored approximately 1,000 mm/s; consistent print quality and alignment remain refinement goals.
comparison:
  title: From the first layout to a revised assembly
  intro: "These CAD views document two stages of the design. The revision added frame support and improved electronics access, while leaving alignment and vibration as ongoing challenges."
  stages:
    - label: Before
      title: Early frame and motion layout
      image: assets/img/artoriusEarlyRender.png
      alt: Early CAD assembly of the Artorius frame and motion system
      caption: "The initial layout established the CoreXY architecture. Physical assembly later exposed rigidity and packaging issues that were less apparent in CAD."
    - label: After
      title: Revised frame and electronics
      image: assets/img/artoriusRevised.png
      alt: Revised Artorius CAD assembly with additional frame support and electronics enclosure
      caption: "Additional extrusion and a serviceable electronics enclosure addressed support and access. Extra extrusion alone did not fully resolve resonance."
  takeaway: "Plan packaging, wiring, and alignment early, then evaluate the assembly physically. A revised CAD model is a design change, not proof of a measured performance gain."
project_summary:
  role: "Independent design and build"
  tools: "CAD, FDM fabrication, CoreXY motion, CAN bus"
  status: "Operational; refinement ongoing"
  result: "Working custom printer and high-speed motion tests"
---

{% include project_summary.liquid %}

{% include project-highlights.liquid %}

Artorius is a CoreXY 3D printer I designed and built using suitable components from an older BIQU B1. It combines a custom toolhead, an extrusion frame, and serviceable electronics. The build gave me experience connecting mechanical design decisions to alignment, vibration, and actual printing behavior.

<section class="project-section project-section--portrait">
<div class="project-section__copy" markdown="1">

## Ideation

Repeated reliability and troubleshooting problems with the original printer prompted me to reconsider its architecture. I wanted a machine that could explore higher speeds while remaining practical to fabricate and service, rather than simply replacing individual components on the original frame.

Reusing the BIQU B1's suitable motors and 24 V supply helped define the project constraints. I focused the new design effort on the CoreXY motion system, frame, and toolhead, with rigidity, component access, and straightforward assembly as priorities alongside speed. The project became an opportunity to learn how these decisions interact once a CAD assembly becomes a working machine.

</div>
<div class="project-section__media">
{% include figure.liquid path="assets/img/artoriusSketch.jpg" alt="Early feasibility and material-cost sketch." title="Early feasibility and material-cost sketch." class="img-fluid rounded" zoomable=true caption="Early feasibility and material-cost sketch." %}
</div>
</section>

## Design

I developed the frame, motion system, and toolhead together in CAD, checking component placement and fabrication requirements. The key tradeoffs were stiffness versus packaging, toolhead mass distribution, and using printed fixtures where custom metal parts would be harder to manufacture.

{% include cad_viewer.liquid %}

<section class="project-section project-section--balanced">
<div class="project-section__copy" markdown="1">

### Toolhead

I designed the toolhead from scratch around a BIQU H2 extruder and a generic four-screw hotend mounting pattern. A 5015 fan provides part cooling, while a 2510 fan cools the cold side of the hotend to help prevent heat-related clogs.

I placed the extruder motor above the aluminum extrusion and arranged the other components to keep the toolhead's center of mass close to the gantry carriage. The toolboard sits on the side nearest the electronics enclosure to shorten wire paths and simplify cable routing.

</div>
<div class="project-section__media">
{% include figure.liquid path="assets/img/toolheadMockup.jpg" alt="CAD render of the early custom toolhead concept." title="CAD render of the early custom toolhead concept." class="img-fluid rounded" zoomable=true caption="CAD render of the early custom toolhead concept." %}
</div>
</section>

### Frame

The frame uses standard 2020 aluminum extrusion, corner connectors, and printed joining parts. I revised the initially less rigid structure with additional extrusion to reduce resonance, although the improvement was limited.

Some components extend outside the frame because the layout was already well developed before I recognized the packaging issue. That constraint led to awkward motor-mount placement and highlighted the value of planning the entire assembly early.

### Motors & Mounts

RobotDigg NEMA17 2504 motors drive the XY gantry. Their mounts use double-shear support to support higher belt tension and include cooling-fan mounts. I configured the XY drivers for approximately 2 A motor current with a 48 V supply.

The Z axis reuses less demanding motors from the BIQU B1 and runs from the 24 V system supply. Rigid front mounts and an adjustable rear mount make assembly and heated-bed attachment easier.



## Prototype

I fabricated the printed fixtures and assembled them with extrusion, motion components, and electronics. The first build allowed me to evaluate the gantry arrangement physically and exposed weaknesses that were less apparent in CAD. I then revised the frame and wiring while retaining usable components.

### Wiring & Electronics

Wiring was initially an afterthought, so I redesigned its routing and enclosure to improve serviceability. The side-mounted electronics enclosure has a magnetically attached service panel and fans that cool the Manta M8P motherboard and TMC5160 motor drivers.

A reused 24 V power supply powers the main system, while an added 48 V supply powers the XY motor drivers. The toolboard connects through CAN bus, reducing the wiring carried to the toolhead. Integrating the BigTreeTech Eddy probe involved substantial setup and documentation troubleshooting; the connection now works.

<div class="project-gallery">
    {% include figure.liquid path="assets/img/artoriusBelts.png" alt="CAD render of the first-iteration CoreXY gantry and belt routing." title="CAD render of the first-iteration CoreXY gantry and belt routing." class="img-fluid rounded" zoomable=true caption="CAD render of the first-iteration CoreXY gantry and belt routing." %}
    {% include figure.liquid path="assets/img/artoriusProgress.png" alt="Intermediate CAD assembly before the additional frame extrusion." title="Intermediate CAD assembly before the additional frame extrusion." class="img-fluid rounded" zoomable=true caption="Intermediate CAD assembly before the additional frame extrusion." %}
</div>

## Testing & Revisions

{% include project-comparison.liquid %}

Motion testing reached speeds of approximately 1,000 mm/s and acceleration settings in the 50,000–100,000 mm/s² range. These describe the motion limits I explored, rather than a validated operating envelope for consistently high-quality printing.

Testing also exposed limitations that extra frame extrusion did not fully resolve. Keeping the machine square and free of skew remains difficult; a front crossbar would make alignment easier in a future revision. Better component packaging, greater frame rigidity, and cleaner motor-mount placement are other priorities.

The printer is operational, but I am continuing to work toward a better balance of speed, print quality, and reliability. The demonstration at the top of this page shows Benchy printing from several angles, filmed using my custom phone mount.

## Current outcome

The current machine is operational and can print a Benchy, as shown in the demonstration at the top of this page. The project demonstrates a complete path from custom CAD and fabrication through electronics integration and motion testing. Quality, alignment, and reliability remain active refinement goals rather than finished performance claims.

[Watch the Artorius preview on YouTube](https://www.youtube.com/watch?v=ifcJKhLbfP0){:target="\_blank"}

[View the Artorius repository on GitHub](https://github.com/EthanMahajan/Artorius){:target="\_blank"}
