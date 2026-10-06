---
layout: page
title: Air Purifier
description: Engineering project in development
importance: 3
project_started: July 2026
documentation_updated: 2026-10-06
category: Engineering
github: https://github.com/EthanMahajan/Air-Purifier
img: assets/img/PurifierPCB
project_summary:
  role: "Independent mechanical and electronics design"
  tools: "KiCad, CAD, planned FDM fabrication"
  status: "Design in progress"
  result: "Electrical schematics complete; physical integration pending"
---

{% include project_summary.liquid %}

I am developing a smart air purifier that reuses a 120 mm computer case fan in a custom printed housing. The intended functions are room-air filtration and consistent background noise, with sensing and control added through a custom electronics design.

## Ideation

The project began with a practical dorm-room need: filtration and background noise in a compact device. Reusing readily available fan hardware offered a starting point for the airflow system while leaving room to learn electronics design through a useful application.

I wanted the project to go beyond a fan in a box. Automatic response to particulate-matter levels and an indication of filter replacement needs became design goals, although neither has been implemented or tested yet.

## Design

The concept combines a 120 mm fan, filter, custom housing, and particulate-matter sensor. The planned controller will adjust fan speed from sensor readings. Filter-replacement detection remains a feature to develop and validate.

I completed the electrical schematics in KiCad. PCB component placement has not started, so the current work establishes the electrical design rather than a tested controller. The next design stage will address the board layout and integration with the housing, sensor, and fan.

<div class="project-gallery">
    {% include figure.liquid path="assets/img/PurifierPCB" alt="Current electronics-design documentation for the purifier." title="Current electronics-design documentation for the purifier." class="img-fluid rounded" zoomable=true caption="Current electronics-design documentation for the purifier." %}
</div>

## Prototype

A complete physical prototype has not yet been assembled. The next steps are PCB placement, fabrication of the housing and board, and integration of the fan, filter, and sensor. This stage will test whether the electrical and mechanical designs work together as intended.

## Final Product

The final purifier is pending. The current deliverable is the completed schematic work and developing system design. A finished build will need evaluation of airflow, particulate response, fan control, noise, and filter-replacement behavior before those features can be presented as demonstrated results.

[View the Air Purifier repository](https://github.com/EthanMahajan/Air-Purifier)
