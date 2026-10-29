---
layout: about
title: About
permalink: /
subtitle: Mechanical Engineering student focused on CAD, manufacturing, and prototyping

profile:
  align: right
  image: prof_pic.jpg
  image_alt: Ethan Mahajan
  image_circular: false # crops the image to make it circular

social: true # compact contact and profile links
---

I am Ethan Mahajan, a mechanical engineering student at the Georgia Institute of Technology. My work connects CAD, manufacturing, and testing through a custom FDM printer, freelance design and manufacturing work, and research into particles observed in water held in 3D-printed cups.

I am seeking internship, co-op, and project opportunities where I can contribute to hands-on mechanical design and manufacturing work.

<div class="portfolio-actions">
  <a class="btn btn-primary" href="{{ '/projects/' | relative_url }}">View Projects</a>
  <a class="btn btn-outline-primary" href="mailto:{{ site.data.socials.email }}">Contact Me</a>
</div>
<nav class="portfolio-secondary-links" aria-label="Downloads">
  <a href="{{ site.data.socials.cv_pdf | relative_url }}">Download Resume (PDF)</a>
  <a href="{{ site.portfolio_pdf | relative_url }}" download>Download Portfolio (PDF)</a>
</nav>

## Featured build: Artorius

{% assign featured_artorius = site.projects | where: 'path', '_projects/artorius.md' | first %}
{% include project-video.liquid project=featured_artorius %}

I designed, fabricated, and revised this operational CoreXY printer around components from an older machine. The project brought together mechanical packaging, printed fixtures, motion control, and CAN-bus electronics, with further work focused on alignment, vibration, and print reliability.

[Explore the design decisions and see it printing →]({{ featured_artorius.url | relative_url }})

[Design story: using resonance measurements to tune Artorius →]({{ '/notebook/artorius-resonance/' | relative_url }})
