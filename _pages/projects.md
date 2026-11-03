---
layout: page
title: Projects
permalink: /projects/
description: Hardware projects, from early designs to working prototypes, with build details and test results.
nav: true
nav_order: 2
og_image: /assets/img/artorius-working.jpg
portfolio_download: true
---

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
