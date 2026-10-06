---
layout: page
title: Phone Mount
description: Adjustable, low-cost iPhone filming mount built from aluminum extrusion and 3D-printed fixtures
img: assets/img/phone-mount/thumbnail.jpg
importance: 4
category: Engineering
---

I designed and built an adjustable phone mount to film my engineering projects with an iPhone. Aluminum extrusion provides the structure, while custom 3D-printed fixtures connect the frame, position the arm, and hold the phone. The first printed prototype was usable for the finished setup.

## Ideation

I wanted a low-cost way to capture footage of my builds without buying a dedicated camera or an expensive filming rig. Reusable aluminum extrusion and a small set of printed parts offered a practical way to make a mount that I could adjust for different camera angles.

The build cost approximately $18 including aluminum extrusion, or about $4 excluding the extrusion, as estimated in the project video.

<div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/phone-mount/concept-sketch.jpg" title="Phone Mount concept sketch" alt="Phone Mount concept sketch" class="img-fluid rounded z-depth-1" caption="Early sketch identifying vertical adjustment, arm rotation, and phone orientation." %}
    </div>
</div>

## Design

I modeled the fixtures in Fusion 360 around three adjustments: vertical positioning, arm rotation, and phone orientation. Screw-tightened joints let me reposition the mount and lock it for recording.

The design balances adjustability with stiffness. A printed base supports the extrusion, while the connecting fixtures need to resist sagging under the arm and phone. M5 screws attach the fixtures to the extrusion; M4 screws and heat-set inserts secure the phone-retaining pieces.

I also designed the printed geometry around FDM manufacturing. Chamfers, clearance holes, and inclined internal surfaces help the parts print and assemble without relying on difficult unsupported geometry.

<div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/phone-mount/assembly-cad.jpg" title="Adjustable Phone Mount CAD assembly" alt="Adjustable Phone Mount CAD assembly" class="img-fluid rounded z-depth-1" caption="Fusion 360 assembly showing the extrusion frame and adjustable printed joints." %}
    </div>
</div>

<div class="row">
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/phone-mount/phone-holder-cad.jpg" title="Phone holder CAD" alt="Printed phone holder surrounding a pink phone model" class="img-fluid rounded z-depth-1" caption="Phone-retaining fixtures and the rotating connection to the arm." %}
    </div>
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/phone-mount/base-cad.jpg" title="Base CAD" alt="Printed base supporting the vertical aluminum extrusion" class="img-fluid rounded z-depth-1" caption="Braced printed base supporting the upright extrusion." %}
    </div>
</div>

## Prototype

I exported the parts from Fusion 360, prepared them in OrcaSlicer, and printed the fixtures in ABS. I arranged the parts for individual printing and used a Hilbert-curve infill pattern based on my previous experience with ABS warping.

<div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/phone-mount/slicer-layout.jpg" title="Phone Mount parts in OrcaSlicer" alt="Phone Mount parts in OrcaSlicer" class="img-fluid rounded z-depth-1" caption="Printed fixtures arranged across separate build plates in OrcaSlicer." %}
    </div>
</div>

All of the parts printed successfully on the first attempt. I assembled the fixtures with the aluminum extrusion and fasteners, producing a working mount with the intended height and angular adjustments.

<div class="row justify-content-sm-center">
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/phone-mount/assembled-prototype.jpg" title="Assembled Phone Mount" alt="Completed extrusion phone mount with a printed base and adjustable arm" class="img-fluid rounded z-depth-1" caption="The assembled first prototype, ready for use filming engineering projects." %}
    </div>
</div>

## Testing & Revision

The prototype was good enough for final use filming with my iPhone. Assembly revealed one small design oversight: a missing access hole made an extrusion-mounting screw harder to reach. I worked around it during assembly and identified the access opening as a straightforward improvement.

The finished mount provided useful footage, although the phone holder had some play and touching the base introduced visible shake. Improving holder stiffness and base stability would be the next refinements; the first prototype already met my practical recording needs.

## Project Video

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
