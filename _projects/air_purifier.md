---
layout: page
title: Air Purifier
description: Engineering project in development
importance: 1
category: Engineering
github: https://github.com/EthanMahajan/Air-Purifier
---

I am developing a smart DIY air purifier that reuses a 120 mm computer case fan inside a custom 3D-printed housing. The design is intended to improve room air quality while also serving as a white-noise generator for a dorm room. The project repository contains the current design files and documentation.

## Ideation

The project began as a way to build a practical purifier from readily available computer hardware while adding useful automation. In addition to filtering room air, the purifier is intended to provide consistent background noise in a dorm-room environment.

## Design

The purifier is designed around a 120 mm computer case fan and a particulate-matter sensor. The control system will adjust fan speed based on measured room PM levels and detect when the filter needs to be replaced. The electrical schematics are complete in KiCad; PCB component placement has not started yet.

## Prototype

The project is still in development. The next prototype work will include placing the PCB, fabricating the housing, assembling the electronics, and integrating the fan, filter, and sensor system.

## Project Media

Prototype photographs, CAD views, and KiCad screenshots will be added as fabrication progresses.

{% comment %}Add project images here when available, following the Artorius gallery pattern.{% endcomment %}
{% comment %}
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/airPurifierCad.png" title="Air Purifier CAD" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/airPurifierPcb.png" title="KiCad PCB Layout" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
{% endcomment %}

## Testing & Revision

Testing and revisions are coming soon. Once the first assembled prototype is available, I will evaluate particulate-matter response, fan-speed control, filter replacement detection, noise output, and overall usability.

[View the Air Purifier repository on GitHub](https://github.com/EthanMahajan/Air-Purifier){:target="_blank"}
