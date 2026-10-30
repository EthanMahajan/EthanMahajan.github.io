---
layout: page
title: Smart Air Purifier — Controller Design
project_intro: "I am developing a smart air purifier that reuses a 120 mm computer fan in a printed housing. The current deliverable is the KiCad schematic; fabrication, sensing, and control integration are still pending."
description: KiCad schematic for a proposed fan, sensor, and filter controller; layout and physical validation are next.
thumbnail_alt: Planned sensor and fan control; the KiCad schematic is the current deliverable
card_label: Design in progress
card_description: "Controller concept for a compact purifier using a reused fan and particulate sensor. I completed the KiCad schematic; board layout, housing fabrication, and physical validation are the next stages. The design has not yet been demonstrated as a functioning purifier."
importance: 3
project_started: July 2026
documentation_updated: 2026-10-20
category: Engineering
github: https://github.com/EthanMahajan/Air-Purifier
og_image: /assets/img/social/air_purifier.png
img: assets/img/PurifierPCB.png
thumbnail_image: assets/img/purifier-system.svg
thumbnail_width: 800
thumbnail_height: 600
pdf_summary:
  caption: "Completed KiCad schematic; board layout and physical validation are pending."
  design: "A dorm-room need for filtration and background noise motivated a compact purifier concept using a repurposed 120 mm fan. The planned assembly combines a printed housing, filter, particulate-matter sensor, and custom controller. I completed the electrical schematics in KiCad; PCB placement has not started."
  evidence: "The demonstrated deliverable is schematic work, not a functioning purifier. Next steps are board layout, housing and board fabrication, and system integration. Airflow, fan control, sensor response, noise, and proposed filter-replacement detection still require physical testing."
overview_media:
  image: assets/img/PurifierPCB.png
  alt: KiCad schematic of the proposed purifier controller
  caption: "Completed schematic; use the full-resolution view to inspect labels. Board layout and physical validation are pending."
project_summary:
  role: "Independent mechanical and electronics design"
  tools: "KiCad, CAD, planned FDM fabrication"
  status: "Design in progress"
  result: "Electrical schematics complete; physical integration pending"
---

## Ideation

The project began with a practical dorm-room need: filtration and background noise in a compact device. Reusing readily available fan hardware offered a starting point for the airflow system while leaving room to learn electronics design through a useful application.

I wanted the project to go beyond a fan in a box. Automatic response to particulate-matter levels and filter-replacement indication became design goals.

## Design

The concept combines a 120 mm fan, filter, custom housing, and particulate-matter sensor. The planned controller will adjust fan speed from sensor readings. Filter-replacement detection remains a feature to develop and validate.

{% include figure.liquid path="assets/img/purifier-system.svg" alt="Planned sensor-to-controller-to-fan system; housing and filter integration are pending" width="800" height="600" class="system-overview" caption="Concept overview based on the current project description. Only the schematic is complete; arrows describe intended control relationships, not verified wiring." %}

## Current status and next steps

- **Complete:** electrical schematic.
- **Next:** PCB component placement and board layout.
- **Pending:** housing/board fabrication and system integration.
- **Pending:** physical validation.

### Planned validation

| Category                    | Question to test after assembly                                                  |
| --------------------------- | -------------------------------------------------------------------------------- |
| Airflow and fan suitability | Does the reused fan move useful airflow through the selected filter?             |
| Sensor response             | How does the sensor respond to changing conditions?                              |
| Fan control and power       | Does control operate as intended, and what power does the assembled system draw? |
| Noise                       | Is the sound suitable for the intended dorm-room use?                            |
| Filter indication           | Can filter-replacement behavior be validated?                                    |

{: .requirements}

These are planned checks; no numerical targets or performance results have been established here.

[View source files](https://github.com/EthanMahajan/Air-Purifier)
