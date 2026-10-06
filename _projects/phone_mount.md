---
layout: page
title: Phone Mount
description: Adjustable, low-cost iPhone filming mount built from aluminum extrusion and 3D-printed fixtures
img: assets/img/phone-mount/thumbnail.jpg
importance: 2
category: Engineering
---

| Role                               | Tools / methods                      | Status                            | Main result                                                            |
| ---------------------------------- | ------------------------------------ | --------------------------------- | ---------------------------------------------------------------------- |
| Independent design and fabrication | Fusion 360, OrcaSlicer, ABS printing | Completed; usable first prototype | Adjustable iPhone filming mount; approximately $18 including extrusion |

I built a low-cost adjustable phone mount to film my engineering projects with an iPhone. Extrusion supplies the structure; printed fixtures provide the connections and camera positioning.

## Ideation

I wanted a low-cost way to capture footage of my builds without buying a dedicated camera or an expensive filming rig. Reusable aluminum extrusion and a small set of printed parts offered a practical way to make a mount that I could adjust for different camera angles.

The build cost approximately $18 including aluminum extrusion, or about $4 excluding the extrusion, as estimated in the project video.

<div class="project-gallery">
    {% include figure.liquid path="assets/img/phone-mount/concept-sketch.jpg" alt="Concept sketch identifying the required adjustments." title="Concept sketch identifying the required adjustments." class="img-fluid rounded" zoomable=true caption="Concept sketch identifying the required adjustments." %}
</div>

## Design

I modeled the fixtures in Fusion 360 around three adjustments: vertical positioning, arm rotation, and phone orientation. Screw-tightened joints let me reposition the mount and lock it for recording.

The design balances adjustability with stiffness. A printed base supports the extrusion, while the connecting fixtures need to resist sagging under the arm and phone. M5 screws attach the fixtures to the extrusion; M4 screws and heat-set inserts secure the phone-retaining pieces.

I also designed the printed geometry around FDM manufacturing. Chamfers, clearance holes, and inclined internal surfaces help the parts print and assemble without relying on difficult unsupported geometry.

<div class="project-gallery">
    {% include figure.liquid path="assets/img/phone-mount/assembly-cad.jpg" alt="Overall extrusion and fixture assembly." title="Overall extrusion and fixture assembly." class="img-fluid rounded" zoomable=true caption="Overall extrusion and fixture assembly." %}
    {% include figure.liquid path="assets/img/phone-mount/phone-holder-cad.jpg" alt="Phone retention and angular adjustment." title="Phone retention and angular adjustment." class="img-fluid rounded" zoomable=true caption="Phone retention and angular adjustment." %}
    {% include figure.liquid path="assets/img/phone-mount/base-cad.jpg" alt="Braced base supporting the upright." title="Braced base supporting the upright." class="img-fluid rounded" zoomable=true caption="Braced base supporting the upright." %}
</div>

## Prototype

I exported the parts from Fusion 360, prepared them in OrcaSlicer, and printed the fixtures in ABS. I arranged the parts for individual printing and used a Hilbert-curve infill pattern based on my previous experience with ABS warping.

All of the parts printed successfully on the first attempt. I assembled the fixtures with the aluminum extrusion and fasteners, producing a working mount with the intended height and angular adjustments.

<div class="project-gallery">
    {% include figure.liquid path="assets/img/phone-mount/slicer-layout.jpg" alt="Fixtures prepared on separate OrcaSlicer plates." title="Fixtures prepared on separate OrcaSlicer plates." class="img-fluid rounded" zoomable=true caption="Fixtures prepared on separate OrcaSlicer plates." %}
    {% include figure.liquid path="assets/img/phone-mount/assembled-prototype.jpg" alt="Assembled first prototype with adjustable arm." title="Assembled first prototype with adjustable arm." class="img-fluid rounded" zoomable=true caption="Assembled first prototype with adjustable arm." %}
</div>

## Testing & Revisions

The prototype was good enough for final use filming with my iPhone. Assembly revealed one small design oversight: a missing access hole made an extrusion-mounting screw harder to reach. I worked around it during assembly and identified the access opening as a straightforward improvement.

The finished mount provided useful footage, although the phone holder had some play and touching the base introduced visible shake. Improving holder stiffness and base stability would be the next refinements; the first prototype already met my practical recording needs.

## Final Product

The first prototype became the mount I use to capture project footage. Its value is a practical filming setup built from reusable stock and a small set of custom parts, with the adjustment range needed for my recordings. Further stiffness improvements are possible, but a second build was not necessary for the intended use.

The video documents the design, CAD, slicing, assembled prototype, and sample footage.

<div class="embed-responsive embed-responsive-16by9 rounded z-depth-1">
    <iframe
        class="embed-responsive-item"
        src="https://www.youtube-nocookie.com/embed/NBOV5k6CR7c"
        title="Phone Mount — design, fabrication, and demonstration"
        loading="lazy"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen
    ></iframe>
</div>

<div class="caption">
    Design overview at 0:36, CAD at 1:31, slicing at 4:25, and the assembled prototype at 5:43.
</div>

[Watch the Phone Mount project on YouTube](https://www.youtube.com/watch?v=NBOV5k6CR7c){:target="\_blank"}
