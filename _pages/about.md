---
layout: about
title: About
permalink: /
headline: I turn CAD into working hardware.
subtitle: Mechanical engineering at Georgia Tech · Design, fabrication, and iteration

profile:
  align: right
  image: prof_pic.jpg
  image_alt: Ethan Mahajan
  image_circular: false # crops the image to make it circular

selected_papers: true # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page
---

I'm Ethan Mahajan, a mechanical engineering student at Georgia Tech. I design, fabricate, and revise physical prototypes, from a custom CoreXY printer to an adjustable filming mount.

I am seeking internship, co-op, and project opportunities where I can contribute to hands-on mechanical design and manufacturing work.

<div class="portfolio-actions">
  <a class="btn btn-primary" href="{{ '/projects/' | relative_url }}">View Projects</a>
  <a class="btn btn-outline-primary" href="{{ site.data.socials.cv_pdf | relative_url }}">Download Resume (PDF)</a>
  <a class="btn btn-outline-primary" href="{{ site.portfolio_pdf | relative_url }}" download>Portfolio (PDF)</a>
  <a class="btn btn-outline-primary" href="mailto:{{ site.data.socials.email }}">Contact Me</a>
</div>

{% include home-evidence.liquid %}

{% include home-builds.liquid %}
