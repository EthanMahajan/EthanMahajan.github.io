---
layout: page
title: Air Purifier
project_intro: "I am developing a smart air purifier that reuses a 120 mm computer fan in a printed housing. The current deliverable is the KiCad schematic; fabrication, sensing, and control integration are still pending."
overview_detail: "I completed the electrical schematics in KiCad. PCB component placement has not started, so the current work establishes the electrical design rather than a tested controller. The next design stage will address the board layout and integration with the housing, sensor, and fan."
description: Engineering project in development
card_label: Design in progress
card_description: "Smart air purifier controller: KiCad schematics complete, with PCB layout and physical testing next."
importance: 3
project_started: July 2026
documentation_updated: 2026-10-20
category: Engineering
github: https://github.com/EthanMahajan/Air-Purifier
og_image: /assets/img/social/air_purifier.png
img: assets/img/PurifierPCB.png
pdf_summary:
  caption: "Completed KiCad schematic; board layout and physical validation are pending."
  design: "A dorm-room need for filtration and background noise motivated a compact purifier concept using a repurposed 120 mm fan. The planned assembly combines a printed housing, filter, particulate-matter sensor, and custom controller. I completed the electrical schematics in KiCad; PCB placement has not started."
  evidence: "The demonstrated deliverable is schematic work, not a functioning purifier. Next steps are board layout, housing and board fabrication, and system integration. Airflow, fan control, sensor response, noise, and proposed filter-replacement detection still require physical testing."
project_summary:
  role: "Independent mechanical and electronics design"
  tools: "KiCad, CAD, planned FDM fabrication"
  status: "Design in progress"
  result: "Electrical schematics complete; physical integration pending"
---

## Ideation

The project began with a practical dorm-room need: filtration and background noise in a compact device. Reusing readily available fan hardware offered a starting point for the airflow system while leaving room to learn electronics design through a useful application.

I wanted the project to go beyond a fan in a box. Automatic response to particulate-matter levels and an indication of filter replacement needs became design goals, although neither has been implemented or tested yet.

## Design

The concept combines a 120 mm fan, filter, custom housing, and particulate-matter sensor. The planned controller will adjust fan speed from sensor readings. Filter-replacement detection remains a feature to develop and validate.

<div class="project-gallery project-gallery--detail">
    {% include figure.liquid path="assets/img/PurifierPCB.png" alt="Current electronics-design documentation for the purifier." title="Current electronics-design documentation for the purifier." class="img-fluid rounded" zoomable=true caption="Current electronics-design documentation for the purifier." %}
</div>

## Current status and next steps

The electrical schematics are complete; PCB placement and a physical prototype are pending. Next I need to lay out the board, fabricate the housing and board, and integrate the fan, filter, and sensor.

The assembled system will need testing for airflow, particulate response, fan control, noise, and filter-replacement behavior before those functions can be presented as demonstrated results.

[View the Air Purifier repository](https://github.com/EthanMahajan/Air-Purifier)
