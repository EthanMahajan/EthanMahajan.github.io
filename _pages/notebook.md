---
layout: page
title: Engineering notebook
permalink: /notebook/
description: Short project notes about design decisions, fabrication problems, tests, and lessons learned.
nav: true
nav_order: 4
---

Short notes from the work behind the case studies: a problem encountered, a change tried, and the evidence behind the next decision.

{% assign notebook_entries = site.notes | sort: 'date' | reverse %}
{% if notebook_entries.size > 0 %}

<ol class="notebook-list">
{% for note in notebook_entries %}
  {% assign project_path = note.project | prepend: '_projects/' | append: '.md' %}
  {% assign linked_project = site.projects | where: 'path', project_path | first %}
  <li>
    <p class="caption"><time datetime="{{ note.date | date_to_xmlschema }}">{{ note.date | date: '%B %-d, %Y' }}</time>{% if linked_project %} / {{ linked_project.title | escape }}{% endif %}</p>
    <h2><a href="{{ note.url | relative_url }}">{{ note.title | escape }}</a></h2>
    <p>{{ note.description | escape }}</p>
  </li>
{% endfor %}
</ol>
{% else %}
No notebook entries have been published yet. The [project case studies]({{ '/projects/' | relative_url }}) contain the current build documentation.
{% endif %}
