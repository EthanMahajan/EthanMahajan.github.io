---
layout: page
title: Artorius
description: High-Speed, Reliable coreXY 3D Printer
img: assets/img/artoriusRevised.png
importance: 3
category: fun
---

I recycled my old cartesian style 3D printer into a new-generation machine to perform as well as current day consumer-grade printers, if not better.

Initially, this project started out as a grievance with my old BIQU B1 3D printer because it would struggle to print when I needed it to leading to multiple-day troubleshooting sessions, so something had to change. I realized that I could redesign the printer from the ground up to not only fix the existing issues but also add new features. Thus, I got to work thinking about how it would work; designing how the parts would mesh together; and checking for existing parts that fit my design goals.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/artoriusSketch.jpg" title="Early Sketch" class="img-fluid rounded z-depth-1" style="height: 250px; object-fit: cover;" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/artoriusEarlyRender.png" title="Early CAD Renderings" class="img-fluid rounded z-depth-1" style="height: 250px; object-fit: cover;" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/toolheadMockup.jpg" title="Early Toolhead Design" class="img-fluid rounded z-depth-1" style="height: 250px; object-fit: cover;" %}
    </div>
</div>
<div class="caption">
    On the left, an early brainstorm session for the feasibility and material cost of the machine. In the middle, an early mockup of the printer without including most of the necessary components. On the right, an illustration of the toolhead I had originally designed.
</div>

Once I had the design firmly finished, I started ordering the parts and building the printer. After every part had arrived, I got to work assembling and testing this first iteration for performance. This led to me recognizing my design had flaws that were fundamental to the frame as well as other components, so I got back to designing as shown in the photos below.

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/artoriusBelts.png" title="First Revision Gantry" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/artoriusProgress.png" title="Rendering Between Revisions" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    You can also have artistically styled 2/3 + 1/3 images, like these.
</div>

You can also put regular text between your rows of images.
Say you wanted to write a little bit about your project before you posted the rest of the images.
You describe how you toiled, sweated, _bled_ for your project, and then... you reveal its glory in the next row of images.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/artoriusRevised.png" title="2nd Iteration" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Rendering of the second iteration of Artorius.
</div>

The code is simple.
Just wrap your images with `<div class="col-sm">` and place them inside `<div class="row">` (read more about the <a href="https://getbootstrap.com/docs/4.4/layout/grid/">Bootstrap Grid</a> system).
To make images responsive, add `img-fluid` class to each; for rounded corners and shadows use `rounded` and `z-depth-1` classes.
Here's the code for the last row of images above:

{% raw %}

```html
<div class="row justify-content-sm-center">
  <div class="col-sm-8 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/6.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/11.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
```

{% endraw %}
