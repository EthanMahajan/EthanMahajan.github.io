---
layout: page
title: Projects
permalink: /projects/
description: Built hardware, design decisions, and the evidence behind each stage of development.
nav: true
nav_order: 2
og_image: /assets/img/artorius-working.jpg
---

<nav class="portfolio-secondary-links project-index-links" aria-label="Project resources"><a href="{{ site.portfolio_pdf | relative_url }}">Portfolio (PDF)</a></nav>
<div class="projects project-index">
{% assign categories = 'Engineering,Design' | split: ',' %}
{% for category in categories %}
  <h2 class="category" id="{{ category }}">{{ category }}</h2>
  <div class="row row-cols-1 row-cols-md-3">
  {% assign sorted_projects = site.projects | where: 'category', category | sort: 'importance' %}
  {% for project in sorted_projects %}
    {% include project-grid-card.liquid %}
  {% endfor %}
  </div>
{% endfor %}
</div>
