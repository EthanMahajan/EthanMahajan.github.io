---
layout: page
title: Projects
permalink: /projects/
description: Selected engineering, design, and fabrication projects.
nav: true
nav_order: 2
display_categories: [Engineering, Design]
horizontal: false
---

<nav class="portfolio-secondary-links project-index-links" aria-label="Project resources">
  <a href="{{ site.portfolio_pdf | relative_url }}" download aria-label="Download complete portfolio PDF">Portfolio (PDF)</a>
  <a href="{{ '/notebook/' | relative_url }}">Engineering notebook</a>
  <a href="{{ '/notebook/artorius-resonance/' | relative_url }}">Artorius resonance story</a>
</nav>

<div class="projects">
{% if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {% for category in page.display_categories %}
  <h2 class="category" id="{{ category }}">{{ category }}</h2>
  {% assign categorized_projects = site.projects | where: "category", category %}
  {% assign sorted_projects = categorized_projects | sort: "importance" %}
  <!-- Generate cards for each project -->
  {% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endif %}
  {% endfor %}

{% else %}

<!-- Display projects without categories -->

{% assign sorted_projects = site.projects | sort: "importance" %}

  <!-- Generate cards for each project -->

{% if page.horizontal %}

  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endif %}
{% endif %}
</div>

<p class="caption">The portfolio PDF includes every project, including work in progress, with linked contents. The engineering notebook contains shorter build notes and lessons learned.</p>
