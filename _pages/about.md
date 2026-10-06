---
layout: about
title: About
permalink: /
subtitle: Mechanical Engineering student focused on CAD, manufacturing, and prototyping

profile:
  align: right
  image: prof_pic.jpg
  image_circular: false # crops the image to make it circular

selected_papers: true # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page
---

I am Ethan Mahajan, a mechanical engineering student at the Georgia Institute of Technology.

I enjoy turning engineering concepts into reliable physical products through CAD design, additive manufacturing, machining, and iterative testing.

My experience includes designing and revising a high-speed FDM 3D printer, completing freelance CAD and manufacturing work, and researching microplastic contamination from 3D-printed cups. I am currently building experience across digital design, materials, fabrication, and engineering communication.

I am seeking internship, co-op, and project opportunities where I can contribute to hands-on mechanical design and manufacturing work.

<div class="d-flex flex-wrap" style="gap: .75rem; margin: 1.5rem 0;">
  <a class="btn btn-primary" href="{{ '/projects/' | relative_url }}">View Projects</a>
  <a class="btn btn-outline-primary" href="{{ site.data.socials.cv_pdf | relative_url }}">Download Resume (PDF)</a>
  <a class="btn btn-outline-primary" href="mailto:{{ site.data.socials.email }}">Contact Me</a>
</div>

## Featured build: Artorius

{% include figure.liquid path="assets/img/artoriusRevised.png" alt="Revised CAD assembly of the Artorius CoreXY printer" class="img-fluid rounded" caption="The revised Artorius assembly: custom toolhead, extrusion frame, and serviceable electronics." %}

I designed, fabricated, and revised this operational CoreXY printer around components from an older machine. The project brought together mechanical packaging, printed fixtures, motion control, and CAN-bus electronics, with further work focused on alignment, vibration, and print reliability.

{% assign featured_artorius = site.projects | where: 'path', '_projects/artorius.md' | first %}
[Explore the design decisions and see it printing →]({{ featured_artorius.url | relative_url }})
