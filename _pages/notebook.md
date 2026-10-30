---
layout: page
title: Design Notes
permalink: /notebook/
description: Short project notes about design decisions, fabrication problems, tests, and lessons learned.
og_image: /assets/img/notebook/artorius-resonance/belts-20261018.png
nav: true
nav_order: 3
---

{% assign notebook_entries = site.notes | sort: 'date' | reverse %}
{% if notebook_entries.size > 0 %}

<ol class="notebook-list">
{% for note in notebook_entries %}
  {% assign project_path = note.project | prepend: '_projects/' | append: '.md' %}
  {% assign linked_project = site.projects | where: 'path', project_path | first %}
  <li>
    <h2><a href="{{ note.url | relative_url }}">{{ note.title | escape }}</a></h2>
    <p>{{ note.description | escape }}</p>
    <p class="caption"><time datetime="{{ note.date | date_to_xmlschema }}">{{ note.date | date: '%B %-d, %Y' }}</time>{% if linked_project %} / {{ linked_project.title | escape }}{% endif %}</p>
  </li>
{% endfor %}
</ol>
{% else %}
No design notes have been published yet. The [project case studies]({{ '/projects/' | relative_url }}) contain the current build documentation.
{% endif %}
