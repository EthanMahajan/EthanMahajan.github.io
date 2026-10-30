---
layout: page
back_to_top: true
title: Adjustable Phone Filming Mount
project_intro: "I designed and built this adjustable iPhone mount to film my engineering projects. Aluminum extrusion provides the structure, while custom ABS fixtures allow height, arm rotation, and phone orientation to be adjusted."
description: Adjustable, low-cost iPhone filming mount built from aluminum extrusion and 3D-printed fixtures
og_image: /assets/img/social/phone_mount.png
img: assets/img/phone-mount/assembled-prototype.jpg
importance: 2
documentation_updated: 2026-10-20
category: Engineering
thumbnail_alt: Physical adjustable phone mount with extrusion upright and ABS fixtures
card_label: Functional prototype
card_description: "Adjustable iPhone filming mount built from extrusion and custom ABS fixtures. I designed the joints, printed and assembled the parts, and use the functional prototype to film projects; the video estimates about $18 including extrusion."
hero:
  summary_beside: true
  image: assets/img/phone-mount/assembled-prototype.jpg
  alt: Assembled phone filming mount with extrusion upright and adjustable arm
  caption: "The usable first prototype: adjustable height, arm rotation, and phone orientation."
  video: NBOV5k6CR7c
  video_caption: "Design at 0:36, CAD at 1:31, slicing at 4:25, and the assembled prototype at 5:43."
portfolio: true
pdf_summary:
  design: "I needed an inexpensive, adjustable way to film engineering builds with an iPhone. I modeled Fusion 360 fixtures for height, arm rotation, and phone orientation, printed them in ABS, and assembled the mount with aluminum extrusion, heat-set inserts, and fasteners. Chamfers and clearances supported FDM fabrication and assembly."
  evidence: "The usable first prototype cost approximately $18 including extrusion, or $4 excluding it, as estimated in the project video. It became my project filming mount. Assembly exposed a missing screw-access hole; holder play and base shake suggest future stiffness improvements. A second build was unnecessary for the intended use."
project_summary:
  role: "Independent design and fabrication"
  tools: "Fusion 360, OrcaSlicer, ABS printing"
  status: "Completed; usable first prototype"
  result: "Adjustable iPhone filming mount; approximately $18 including extrusion"
---

<section class="project-section project-section--balanced">
<div class="project-section__copy" markdown="1">

<h2 id="ideation">An adjustable mount for project filming</h2>

I wanted a low-cost way to capture footage of my builds without buying a dedicated camera or an expensive filming rig. Reusable aluminum extrusion and a small set of printed parts offered a practical way to make a mount that I could adjust for different camera angles.

The project video estimates approximately $18 including aluminum extrusion, or about $4 excluding extrusion. This is a build estimate, not a complete costed bill of materials.

</div>
<div class="project-section__media">
{% include figure.liquid path="assets/img/phone-mount/concept-sketch.jpg" alt="Concept sketch identifying the required adjustments." title="Concept sketch identifying the required adjustments." class="img-fluid rounded" zoomable=true caption="Concept sketch identifying the required adjustments." %}
</div>
</section>

<h2 id="design">Joints, retention, and access</h2>

I modeled the fixtures in Fusion 360 around three adjustments: vertical positioning, arm rotation, and phone orientation. Screw-tightened joints let me reposition the mount and lock it for recording.

The design balances adjustability with stiffness. A printed base supports the extrusion, while the connecting fixtures need to resist sagging under the arm and phone. M5 screws attach the fixtures to the extrusion; M4 screws and heat-set inserts secure the phone-retaining pieces.

I also designed the printed geometry around FDM manufacturing. Chamfers, clearance holes, and inclined internal surfaces help the parts print and assemble without relying on difficult unsupported geometry.

<div class="project-gallery phone-details">
    <div class="annotated-assembly">
    <span class="figure-marker" style="left:48%;top:55%" aria-hidden="true">1</span><span class="figure-marker" style="left:91%;top:18%" aria-hidden="true">2</span>
    {% include figure.liquid path="assets/img/phone-mount/assembly-cad.jpg" alt="Overall extrusion and fixture assembly." title="Overall extrusion and fixture assembly." class="img-fluid rounded" zoomable=true caption="CAD assembly: (1) the sliding joint sets height and arm rotation; (2) the holder sets phone orientation. Loads pass through the printed joints into the braced base. See the base detail for tool-access findings." %}
    </div>
    {% include figure.liquid path="assets/img/phone-mount/phone-holder-cad.jpg" alt="Phone retention and angular adjustment." title="Phone retention and angular adjustment." class="img-fluid rounded" zoomable=true caption="CAD detail: screw-tightened retention pieces set phone orientation; M4 screws and heat-set inserts secure the holder." %}
    {% include figure.liquid path="assets/img/phone-mount/base-cad.jpg" alt="Braced base supporting the upright." title="Braced base supporting the upright." class="img-fluid rounded" zoomable=true caption="CAD base detail: bracing supports the upright. Assembly later exposed a missing screw-access hole; the workaround was used in the first prototype." %}
</div>

<section class="project-section project-section--balanced project-section--media-left">
<div class="project-section__copy" markdown="1">

## Prototype

I exported the parts from Fusion 360, prepared them in OrcaSlicer, and printed the fixtures in ABS. I arranged the parts for individual printing and used a Hilbert-curve infill pattern based on my previous experience with ABS warping.

All of the parts printed successfully on the first attempt. I assembled the fixtures with the aluminum extrusion and fasteners, producing a working mount with the intended height and angular adjustments.

</div>
<div class="project-section__media">
{% include figure.liquid path="assets/img/phone-mount/slicer-layout.jpg" alt="Fixtures prepared on separate OrcaSlicer plates." title="Fixtures prepared on separate OrcaSlicer plates." class="img-fluid rounded" zoomable=true caption="Fixtures prepared on separate OrcaSlicer plates." %}
</div>
</section>

<h2 id="testing--revisions">Findings from use</h2>

The first prototype became the mount I use to film project footage. A second build was unnecessary for my recording needs.

| Observed finding                                                                    | Proposed change (not built)    |
| ----------------------------------------------------------------------------------- | ------------------------------ |
| Missing access hole for an extrusion-mounting screw; assembly required a workaround | Add tool access to the fixture |
| Play in the phone holder                                                            | Improve retention stiffness    |
| Visible shake when touching the base                                                | Improve base stability         |

{: .requirements}

The expandable demonstration at the top documents the design, CAD, slicing, assembled mount, and sample footage.
