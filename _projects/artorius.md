---
layout: page
back_to_top: true
title: "Artorius: FDM 3D Printer"
project_intro: "Artorius is a CoreXY 3D printer I designed and built around suitable components from an older BIQU B1. The project connects a custom frame and toolhead with fabrication, CAN-bus electronics, and physical motion testing."
description: A working CoreXY printer connecting custom mechanical design, fabrication, and electronics integration.
og_image: /assets/img/social/artorius.png
img: assets/img/artorius-working.jpg
importance: 1
project_started: June 2024
documentation_updated: 2026-10-29
category: Engineering
github: https://github.com/EthanMahajan/Artorius
cad_model: /assets/models/artorius/artorius.3mf
cad_preview: /assets/models/artorius/artorius-preview.3mf
card_label: Operational prototype
card_description: "Custom CoreXY printer: operational hardware, a revised frame, and integrated CAN-bus electronics."
hero:
  image: assets/img/artorius-working.jpg
  alt: Built Artorius printer with custom toolhead and gantry
  caption: "Physical printer, shown in the project video."
  video_lead: true
  video: ifcJKhLbfP0
  video_caption: "Custom toolhead, frame, and electronics, followed by Benchy printing footage."
portfolio: true
pdf_summary:
  design: "Recurring problems with an older BIQU B1 led me to redesign its architecture around reusable motors and a 24 V supply. I developed a CoreXY frame, motion system, and custom toolhead in CAD, fabricated fixtures, assembled the machine, and integrated CAN-bus electronics with a serviceable enclosure."
  evidence: "The printer is operational and the linked video shows Benchy printing. Motion tests explored approximately 1,000 mm/s; this is not a validated print-quality speed. Extra frame support did not fully resolve resonance. Alignment, packaging, vibration, and repeatable print quality remain refinement priorities."
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
sections:
  - { title: Overview, id: overview }
  - { title: Decisions, id: design }
  - { title: Build, id: prototype }
  - { title: Testing, id: testing--revisions }
  - { title: Resources, id: resources }
project_summary:
  role: "Independent design and build"
  tools: "CAD, FDM fabrication, CoreXY motion, CAN bus"
  status: "Operational; refinement ongoing"
  result: "Operational printer with Benchy footage; repeatable print quality remains under refinement"
---

<section class="project-section project-section--portrait">
<div class="project-section__copy" markdown="1">

<h2 id="ideation">Why I rebuilt the printer</h2>

- **Mechanical design:** developed the CoreXY frame, motion layout, and custom toolhead.
- **Fabrication and assembly:** printed fixtures, assembled the machine, and revised the frame.
- **Electronics and motion:** integrated CAN-bus toolhead electronics, supplies, motor drivers, and probing.

Repeated reliability and troubleshooting problems with the original printer prompted me to reconsider its architecture. I wanted a machine that could explore higher speeds while remaining practical to fabricate and service, rather than simply replacing individual components on the original frame.

Reusing the BIQU B1's suitable motors and 24 V supply helped define the project constraints. I focused the new design effort on the CoreXY motion system, frame, and toolhead, with rigidity, component access, and straightforward assembly as priorities alongside speed. The project became an opportunity to learn how these decisions interact once a CAD assembly becomes a working machine.

</div>
<div class="project-section__media">
{% include figure.liquid path="assets/img/artoriusSketch.jpg" alt="Early feasibility and material-cost sketch." title="Early feasibility and material-cost sketch." class="img-fluid rounded" zoomable=true caption="Early feasibility and material-cost sketch." %}
</div>
</section>

<h2 id="design">Frame and toolhead decisions</h2>

I developed the frame, motion system, and toolhead together in CAD, checking component placement and fabrication requirements. The key tradeoffs were stiffness versus packaging, toolhead mass distribution, and using printed fixtures where custom metal parts would be harder to manufacture.

<div class="table-scroll" tabindex="0" role="region" aria-label="Artorius constraints and evidence" markdown="1">

| Constraint                                          | Design response                            | Evidence / verification status                                  |
| --------------------------------------------------- | ------------------------------------------ | --------------------------------------------------------------- |
| Reuse suitable BIQU B1 components                   | Retained motors for Z and the 24 V supply  | Integrated into the operational build                           |
| Fabricate custom fixtures practically               | FDM joining parts and toolhead fixtures    | Parts fabricated and assembled                                  |
| Improve access to electronics                       | Side enclosure with magnetic service panel | Incorporated in the revised assembly                            |
| Explore faster motion while retaining print quality | Frame revisions and resonance analysis     | Exploratory motion tested; repeatable quality limits unverified |

{: .requirements}

</div>

{% include cad_viewer.liquid %}

<section class="project-section project-section--balanced project-section--media-left">
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

<section class="project-section project-section--balanced">
<div class="project-section__copy" markdown="1">

<h2 id="prototype">Assembly and integration</h2>

I fabricated the printed fixtures and assembled them with extrusion, motion components, and electronics. The first build allowed me to evaluate the gantry arrangement physically and exposed weaknesses that were less apparent in CAD. I then revised the frame and wiring while retaining usable components.

</div>
<div class="project-section__media">
{% include figure.liquid path="assets/img/artoriusBelts.png" alt="CAD render of the first-iteration CoreXY gantry and belt routing." title="CAD render of the first-iteration CoreXY gantry and belt routing." class="img-fluid rounded" zoomable=true caption="CAD render of the first-iteration CoreXY gantry and belt routing." %}
</div>
</section>

<section class="project-section project-section--balanced project-section--media-left">
<div class="project-section__copy" markdown="1">

### Wiring & Electronics

Wiring was initially an afterthought, so I redesigned its routing and enclosure to improve serviceability. The side-mounted electronics enclosure has a magnetically attached service panel and fans that cool the Manta M8P motherboard and TMC5160 motor drivers.

A reused 24 V power supply powers the main system, while an added 48 V supply powers the XY motor drivers. The toolboard connects through CAN bus, reducing the wiring carried to the toolhead. Integrating the BigTreeTech Eddy probe involved substantial setup and documentation troubleshooting; the connection now works.

</div>
<div class="project-section__media">
{% include figure.liquid path="assets/img/artoriusProgress.png" alt="Intermediate CAD assembly before the additional frame extrusion." title="Intermediate CAD assembly before the additional frame extrusion." class="img-fluid rounded" zoomable=true caption="Intermediate CAD assembly before the additional frame extrusion." %}
</div>
</section>

<h2 id="testing--revisions">Testing and remaining limits</h2>

### Tests performed

Exploratory motion tests reached approximately **1,000 mm/s**, with acceleration settings of **50,000–100,000 mm/s²**. These are reported motion tests/settings, not a validated envelope for sustained printing or print quality. The project video separately documents Benchy printing; it does not establish print quality at those motion settings.

### What changed

I added extrusion to the frame and revised the wiring and electronics enclosure. The CAD comparison shows these design changes, not a controlled performance comparison; the views have different orientations and do not establish improved stiffness by themselves.

{% include project-comparison.liquid %}

<span id="resonance-guided-the-next-design-decisions"></span>

The resonance measurements helped identify questions for further tuning. [Read the design note]({{ '/notebook/artorius-resonance/' | relative_url }}) for earlier and later belt/axis plots, their differing analysis conditions, and why analysis estimates still need printed validation.

### Remaining limits

Extra extrusion did not fully resolve resonance. Keeping the machine square and free of skew remains difficult; a front crossbar is a proposed future change. Better packaging, frame rigidity, and motor-mount placement remain priorities alongside repeatable print quality and reliability.

## Resources

[View source files in the Artorius repository](https://github.com/EthanMahajan/Artorius)
