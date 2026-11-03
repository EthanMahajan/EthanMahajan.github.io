---
layout: notebook-note
title: Detecting collisions on Artorius with StallGuard and an accelerometer
date: 2026-11-01
project: artorius
published: true
back_to_top: true
description: Using the toolhead accelerometer to check sensorless homing and investigate collisions.
og_image: /assets/img/notebook/artorius-collision-detection/artorius-impact-x.png
notebook_intro: |
  **Status as of November 1, 2026:** Real taps trigger the synchronized stop system while the printer is stationary. Stopping distance and behavior during motion are still untested.
sections:
  - { title: Why, id: why-i-started-this-project }
  - { title: How it works, id: getting-a-signal-from-the-toolhead-to-both-motors }
  - { title: Tests, id: building-and-commissioning-the-system }
  - { title: Next steps, id: using-the-accelerometer-to-calibrate-stallguard }
  - { title: References, id: references-and-test-records }
---

## Why I started this project

Artorius uses sensorless homing: its TMC5160 drivers estimate motor load and stop the carriage when it reaches the end of travel. Tuning StallGuard sensitivity takes trial and error. Too sensitive, and the carriage stops early; too insensitive, and the motors keep pushing after contact.

I wanted a second measurement to check what actually happened. The printer already has an LIS2DW12 accelerometer on its EBB42 toolhead board for resonance testing. Could that sensor recognize contact and help me tune homing? Eventually, I also want to investigate collisions during printing.

## Getting a signal from the toolhead to both motors

StallGuard estimates motor load; the accelerometer detects a jolt. Comparing them could help distinguish contact from an early motor-load trigger.

The accelerometer is on the toolhead, but both CoreXY motors are controlled by the Manta M8P. They need to stop together. Artorius runs Kalico, a Klipper fork. I reused its trigger synchronization instead of adding wiring or waiting for a Python script to inspect every sample.

<ol class="collision-signal-flow" aria-label="Collision signal path">
  <li>The LIS2DW12 detects a sudden acceleration change.</li>
  <li>Custom EBB42 firmware triggers the synchronization system.</li>
  <li>The host's C dispatcher relays the event to the Manta.</li>
  <li>Both CoreXY motor stop callbacks run; the plugin records the result and clears XY homing.</li>
</ol>

The host computer is still part of this path. Clearing XY homing prevents later moves from trusting coordinates that a collision may have changed.

<span id="choosing-an-approach"></span>
<span id="what-the-two-sensors-measure"></span>
<span id="how-the-detector-processes-acceleration"></span>
<span id="the-software-behind-the-stop"></span>

The detector accepts either a change from the accelerometer's running baseline or the sensor's hardware tap signal. For the stationary tests, the raw method requires two consecutive samples above **2,000 mg** at **1,600 Hz**. Normal motion can also produce acceleration spikes, so these settings still need testing on a moving printer.

## Building and commissioning the system

Codex helped write and test the C firmware and Python plugin. I set the requirements, matched the implementation to Artorius's hardware, backed up and flashed the EBB42 firmware, and ran the physical tests. The experiment stays separate from ordinary printing and `G28` homing.

I tested sensor recording first, then synchronization with an injected trigger, then real taps using `ACCEL_SG_SELF_TEST STOP_TEST=2`. This command arms the detector and stop group without moving the motors.

**The software suite passed 271 tests. In the recorded hardware batch, eight stationary attempts passed and three timed out as inconclusive, with no reported faults.** Real X and Y impacts reached both controllers before cleanup. Motor step counts stayed unchanged, sensor settings were restored, and XY homing was cleared.

A timeout can return the same synchronization reason code as an impact. The test therefore checks the detector's recorded cause as well as both controllers' reports; a timeout cannot count as a successful impact.

<figure class="project-video--local collision-tap-video">
  <video controls playsinline preload="none" width="1920" height="1080"
    poster="{{ '/assets/video/artorius-collision-detection/directional-tap-test.jpg' | relative_url }}"
    aria-label="Stationary X and Y finger-tap demonstration on Artorius"
    aria-describedby="directional-tap-caption">
    <source src="{{ '/assets/video/artorius-collision-detection/directional-tap-test.mp4' | relative_url }}" type="video/mp4">
    <a href="{{ '/assets/video/artorius-collision-detection/directional-tap-test.mp4' | relative_url }}">Watch the stationary finger-tap demonstration</a>.
  </video>
  <figcaption class="caption" id="directional-tap-caption">
    Stationary X/Y tap test. The detector mostly responds along the selected axis; this does not measure stopping distance or false-trigger rates during motion.
    <a href="{{ '/assets/video/artorius-collision-detection/directional-tap-test.mp4' | relative_url }}">Open the video</a>.
  </figcaption>
</figure>

<div class="impact-recordings">
{% include figure.liquid path="assets/img/notebook/artorius-collision-detection/artorius-impact-x.png" alt="Stationary printer X impact recorded mainly on the sensor Z channel." class="img-fluid rounded" zoomable=true original_link=true caption="X impact: the largest change is on sensor Z." %}
{% include figure.liquid path="assets/img/notebook/artorius-collision-detection/artorius-impact-y.png" alt="Stationary printer Y impact recorded mainly on the sensor X channel." class="img-fluid rounded" zoomable=true original_link=true caption="Y impact: the largest change is on sensor X." %}
</div>

Each buffer contains 128 samples, about 80 ms at the configured rate. The peaks record stationary taps, not the stopping distance of a moving carriage.

The plot labels use the sensor's axes. Its mounting orientation differs from the printer's, so Artorius uses `axes_map: z,-x,-y`: **printer X = sensor Z, printer Y = −sensor X, and printer Z = −sensor Y**. The negative Z spike in the X test therefore represents acceleration along negative printer X; it is recognized as an X-axis impact because the detector checks the mapped axis.

## Using the accelerometer to calibrate StallGuard

Next, I want to approach a known stop under supervision and compare the signals. StallGuard firing before confirmed contact may mean sensitivity is too high. An impact without a StallGuard trigger may mean it is too low. Both interpretations need repeated tests at controlled speeds and motor currents.

The prototype can propose `SGT` settings within **−64 to +63**, but an operator must approve each motion trial and label the result. It does not automatically repeat collisions or write a threshold into `printer.cfg`.

<span id="what-i-have-measured-and-what-i-still-need-to-measure"></span>
<span id="other-uses-i-want-to-investigate"></span>

Before using this during printing, I need to measure contact-to-stop time, stopping distance, and false triggers during normal moves. The initial supervised limits are **10 mm/s**, **0.6 A per XY motor**, **200 mm/s²**, at most **5 mm** of travel, and a **2 second** detector window. These are starting settings, not a demonstrated safe stopping distance.

Detecting skipped steps or external disturbances, and packaging this for other printers, are later possibilities. An accelerometer cannot recover absolute position like an encoder. For now, the implementation is specific to Artorius and provides no collision protection during ordinary printing.

## References and test records

- [Artorius resonance notebook](https://ethanmahajan.github.io/notebook/artorius-resonance/). The accelerometer's original use for measuring vibration and tuning input shaping.
- [Kalico TMC driver documentation](https://docs.kalico.gg/TMC_Drivers.html). StallGuard and sensorless homing behavior.
- [Kalico multi-MCU homing documentation](https://docs.kalico.gg/Multi_MCU_Homing.html). The existing controller synchronization mechanism.
- [Analog Devices StallGuard2 application note](https://www.analog.com/en/resources/app-notes/AN-002.html). Stepper motor load detection and tuning.
- [ST LIS2DW12 product information](https://www.st.com/en/mems-and-sensors/lis2dw12.html). Accelerometer and tap detection.
- [ST LIS2DW12 datasheet](https://www.st.com/resource/en/datasheet/lis2dw12.pdf) and [application note AN5038](https://www.st.com/resource/en/application_note/dm00401877-lis2dw12-alwayson-3d-accelerometer-stmicroelectronics.pdf). Output representation, FIFO depth, and hardware tap thresholds and timing.
- Project source and local test data: `accelerometer-stallguard/` and `printer_data/logs/accel_sg/`. The records reflect tests on Artorius, not independent benchmarks.
