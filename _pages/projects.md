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
<div class="projects">
<span id="Engineering"></span><h2 id="selected-projects">Selected projects</h2>
{% assign featured = site.projects | where: 'importance', 1 | first %}{% include featured-project.liquid project=featured %}
<div class="evidence-grid">{% assign project = site.projects | where: 'importance', 2 | first %}{% include projects.liquid %}</div>
<span id="Design"></span><h2 id="additional-work">Additional work</h2>
<div class="evidence-grid">
{% assign sorted_projects = site.projects | sort: 'importance' %}
{% for project in sorted_projects %}{% if project.importance > 2 %}{% include projects.liquid %}{% endif %}{% endfor %}
</div></div>
