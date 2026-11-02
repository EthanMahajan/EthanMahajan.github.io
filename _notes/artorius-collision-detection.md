---
layout: notebook-note
title: Detecting collisions on Artorius with StallGuard and an accelerometer
date: 2026-11-01
project: artorius
published: true
math: true
back_to_top: true
description: "Using the accelerometer already on Artorius to check StallGuard homing and investigate collision detection."
og_image: /assets/img/notebook/artorius-collision-detection/artorius-impact-x.png
notebook_intro: |
  **Printer:** Artorius, my custom CoreXY FDM printer  
  **Status as of November 1, 2026:** Physical impacts have triggered the synchronized stop system with the printer stationary. I have not yet verified stopping distance or behavior with the motors moving.
sections:
  - { title: Motivation, id: why-i-started-this-project }
  - { title: Alternatives, id: choosing-an-approach }
  - { title: Sensors, id: what-the-two-sensors-measure }
  - { title: Signal path, id: getting-a-signal-from-the-toolhead-to-both-motors }
  - { title: Commissioning, id: building-and-commissioning-the-system }
  - { title: Detector, id: how-the-detector-processes-acceleration }
  - { title: Software, id: the-software-behind-the-stop }
  - { title: Calibration, id: using-the-accelerometer-to-calibrate-stallguard }
  - { title: Future work, id: other-uses-i-want-to-investigate }
  - { title: Results and limits, id: what-i-have-measured-and-what-i-still-need-to-measure }
  - { title: References, id: references-and-test-records }
---

## Why I started this project

Artorius uses sensorless homing. When the carriage reaches the end of its travel, the stepper driver senses increased motor load and tells the printer to stop. There is no mechanical limit switch. The feature works, although getting the sensitivity right has involved trial and error.

If the setting is too sensitive, the printer may stop before the carriage reaches the frame. If it is not sensitive enough, the motors can keep pushing after contact. The right setting also depends on motor current, travel speed, mechanical friction, and the rest of the machine. I wanted a way to evaluate those settings using a second measurement instead of relying entirely on how the homing move looked or sounded.

I also want to catch problems that happen after homing. A printer normally assumes that every commanded motor step produces the expected movement. If the nozzle hits a curled print or the carriage catches on something, that assumption can become wrong. The machine may continue printing with a position error, even though it has no direct way to tell what happened.

Artorius already had two useful pieces of hardware: TMC5160 stepper drivers, which can estimate motor load, and an LIS2DW12 accelerometer on the toolhead, which I had used for input shaping. I wanted to use the accelerometer as a second measurement when tuning StallGuard, then see whether the same approach could help recognize collisions.

I want other printer owners to be able to try this without rebuilding their machines. A software package could reuse the accelerometer and motor drivers they already have, instead of requiring another sensor, wiring, and brackets. The current prototype still requires compatible electronics and custom toolhead firmware, so it is not ready to install on arbitrary printers.

## Choosing an approach

I considered several ways to recognize contact before changing any firmware.

<div class="table-scroll resonance-table" tabindex="0" role="region" aria-label="Detection approaches" markdown="1">

| Approach                                                   | Advantage                                                 | Limitation                                                                                               |
| :--------------------------------------------------------- | :-------------------------------------------------------- | :------------------------------------------------------------------------------------------------------- |
| Tune StallGuard manually                                   | Already supported by the drivers and Klipper              | A motor load reading alone cannot establish when contact occurred                                        |
| Install mechanical switches or contact sensors             | Gives a physical reference at a known location            | Requires mounts, wiring, and installation on each printer                                                |
| Use only the accelerometer for homing                      | Reuses an existing sensor and responds to a physical jolt | Normal movement and vibrations can resemble an impact. A detected jolt does not establish a precise home |
| Analyze sensor readings in a Python script or G-code macro | Easy to modify, record, and visualize                     | Waiting for ordinary host software adds delay to a stop decision                                         |
| Combine StallGuard and the toolhead accelerometer          | Gives two different observations using existing hardware  | Requires firmware changes and coordination between controllers                                           |

</div>

I went with StallGuard plus the accelerometer. StallGuard measures changes in motor load. The accelerometer measures a jolt at the toolhead. Comparing those signals could tell me more about a homing attempt than either reading on its own.

I had to choose how that impact would reach the motors, too. I considered detecting it in a host Python script, adding a stop wire between the boards, and writing a dedicated controller-to-controller message. I used Klipper and Kalico's existing trigger synchronization instead. The toolhead controller could recognize the impact locally, and the main controller could use its existing motor stop callbacks. No additional wiring was needed.

I put the configuration, experiments, and reports in a separate Kalico plugin. The EBB42 firmware reads the sensor and decides when to trigger. The Python plugin manages the tests and records the results, without having to inspect each accelerometer sample before issuing a stop.

I also considered letting the program sweep through StallGuard settings and retry automatically. I left that for later. Right now, each collision trial is short and requires an operator to check the result before trying another setting.

## What the two sensors measure

### StallGuard estimates motor load

Artorius uses TMC5160 drivers for both CoreXY motors. These drivers include StallGuard2, which estimates how much load the motor is experiencing from its electrical behavior. During sensorless homing, a sufficiently strong stall indication can appear on the driver's DIAG output. Klipper treats that signal as a virtual endstop.

StallGuard has a sensitivity setting called `SGT`. On the TMC5160 it ranges from **−64 to +63**. Lower settings generally make it more sensitive. A setting that triggers reliably at one speed or current may behave differently after either changes, which is why I do not want to treat a single successful home as a universal calibration.

Motor load does not directly tell me when the carriage touches its stop. Increased friction, acceleration, or other resistance can affect the estimate. A StallGuard trigger needs to be interpreted alongside the conditions under which it occurred.

### The accelerometer measures the impact

An accelerometer measures acceleration along three axes. Artorius already had an LIS2DW12 on its BTT EBB42 toolhead controller for resonance testing. A sharp impact often produces a short spike in that measurement.

I still have to distinguish an impact from normal printer motion. A printer accelerates and decelerates thousands of times during a print. It also vibrates as belts, rails, and the toolhead respond to each move. A detector that stopped whenever acceleration was high would produce false alarms.

For the first version, I used two detection methods supported by the existing sensor. One checks the measured acceleration against a learned baseline. The other uses the LIS2DW's own single tap recognition. The current `combined` mode accepts either method as a reason to trigger. They do not have to fire together. The motor driver's StallGuard signal remains a separate input during the supervised homing trial.

During supervised homing tests, I want to compare which signal fired and under what conditions. If StallGuard stops a move before there is evidence of contact, the setting may be too sensitive. If the accelerometer detects an impact while StallGuard has not triggered, it may be too insensitive. The stationary tests do not yet establish either interpretation.

{% include figure.liquid path="assets/img/notebook/artorius-collision-detection/artorius-impact-x.png" alt="A recorded printer X impact. The sensor Z channel responds strongly at the right side of the trace." class="img-fluid rounded" zoomable=true original_link=true caption="One stationary X test. The large peak comes from a real tap on the toolhead. The graph shows the acceleration recorded around the trigger, not the distance a moving carriage would travel before stopping." %}

## Getting a signal from the toolhead to both motors

The accelerometer is connected to the EBB42, while the X and Y stepper drivers are on the Manta M8P. Those boards communicate over CAN, so an impact detected at the toolhead needs a way to stop motors controlled by another board.

Both CoreXY motors contribute to X and Y movement. Stopping one while the other continues could send the carriage in an unintended direction. I needed the stop request to reach both motor channels as one coordinated event.

The system follows this path:

<ol class="collision-signal-flow" aria-label="Collision signal path">
  <li>Toolhead hits an obstruction</li>
  <li>LIS2DW12 measures the acceleration</li>
  <li>EBB42 firmware recognizes an impact</li>
  <li>EBB42 signals its synchronized trigger</li>
  <li>Klipper's host C dispatcher relays the event</li>
  <li>Manta receives the trigger</li>
  <li>Both CoreXY motor stop callbacks run</li>
  <li>Plugin records the cause and clears XY homing</li>
</ol>

Klipper calls this mechanism `trsync`, short for trigger synchronization. Klipper uses it to coordinate endstop and probe events across multiple microcontrollers. I reused that mechanism rather than polling the accelerometer in a Python loop and sending a normal G-code stop command.

The EBB42 decides whether an accelerometer event satisfies the threshold. Its C firmware then triggers the EBB42's `trsync` participant. The host's C serial dispatcher relays the trigger to the Manta's participant, which has both XY steppers registered for stopping. This is separate from the ordinary Python event loop used for configuration and reporting.

There is still a host computer in the relay path. The EBB42 does not directly stop the Manta through a dedicated wire, and the setup is not independent of the Linux host. I have also not measured how long a physical collision takes to produce a motor stop under load. The architecture was chosen to reduce the work on the host's Python side, but its speed needs to be measured on the moving printer.

## Building and commissioning the system

I tested the sensor, synchronization, and actual impact detection separately. That made failures easier to trace.

### Saving the original firmware

Before flashing experimental firmware, I checked the hardware and software running on Artorius. The system uses a **Manta M8P v2.0**, a **BTT EBB42 Gen 2**, TMC5160 XY drivers, and the LIS2DW12 toolhead sensor. The printer runs a customized Kalico installation.

I verified the installed EBB42 bootloader and read back the existing application firmware. I kept that verified image, its build information, and its checksums so I could restore the board if the new code failed. The new firmware was flashed to the EBB42 only. The Manta and Eddy probe firmware were left alone.

Codex helped write and test the C firmware and Python plugin. My work included setting the requirements, mapping the system to Artorius's hardware and firmware versions, deploying the changes, checking recovery options, and running the physical tests. I also kept the experimental commands separate from ordinary printing and `G28` homing, so enabling the plugin would not silently change how the printer normally moves.

### Testing the sensor first

I began by recording accelerometer data while the printer was stationary. The initial raw acceleration threshold was **3,000 mg** (3 g). A gentle tap produced a visible spike but did not always cross that threshold. I reduced it to **2,000 mg** for commissioning and repeated the experiment. The sensor then recognized real impacts on both X and Y.

The first recording command kept the motor stop function disabled. It proved the accelerometer could recognize a tap, but did not exercise motor stopping.

### Checking the synchronization path

I next used an injected trigger to test how the Manta and EBB42 coordinated a stop. Both controllers reported the expected synchronization result, and the stationary motor step counts remained unchanged. That checked synchronization while bypassing the accelerometer, so I still needed a test triggered by a real tap.

I therefore had Codex add `ACCEL_SG_SELF_TEST STOP_TEST=2`. This command arms the actual LIS2DW detector and synchronized stop group while leaving all motors stationary. It waits for a real impact or for a bounded timeout. There is no homing move, automatic retract, or artificial trigger.

The new code was tested offline for raw acceleration, hardware tap detection, simultaneous events, timeouts, controller communication problems, failed sensor restoration, and cleanup behavior. After installing the updated source on Artorius and resolving differences in the local Python test environment, I ran the full suite with **271 tests passing**.

### Trying it on the printer

I ran stationary impact tests in both directions and deliberately allowed some runs to time out without a tap. In the recorded batch, **eight attempts passed** and **three ended as inconclusive deadlines**. No test faults were reported in that batch.

The successful X and Y records show the same sequence. The EBB42 identified a physical acceleration event. Both the EBB42 and Manta reported the synchronized trigger before the cleanup process sent stop queries. The existing X and Y motors were registered, their MCU step counts were unchanged, the accelerometer settings were restored, and the plugin cleared the XY homing state.

<figure class="project-video--local collision-tap-video">
  <video controls playsinline preload="none" width="1920" height="1080"
    poster="{{ '/assets/video/artorius-collision-detection/directional-tap-test.jpg' | relative_url }}"
    aria-label="Stationary X and Y finger-tap demonstration on Artorius"
    aria-describedby="directional-tap-caption">
    <source src="{{ '/assets/video/artorius-collision-detection/directional-tap-test.mp4' | relative_url }}" type="video/mp4">
    <a href="{{ '/assets/video/artorius-collision-detection/directional-tap-test.mp4' | relative_url }}">Watch the stationary finger-tap demonstration</a>.
  </video>
  <figcaption class="caption" id="directional-tap-caption">
    I tap the toolhead in X and Y and compare the detector’s response with the selected axis. In this demonstration, it mostly responds to disturbances along the selected axis and ignores taps in the other direction. This is a stationary demonstration, not a measurement of directional false-trigger rates or stopping behavior during motion.
    <a href="{{ '/assets/video/artorius-collision-detection/directional-tap-test.mp4' | relative_url }}">Open the video</a>.
  </figcaption>
</figure>

<div class="table-scroll resonance-table" tabindex="0" role="region" aria-label="Commissioning tests and their limits" markdown="1">

| Test                               | Result                                                         | What remains unknown                                     |
| :--------------------------------- | :------------------------------------------------------------- | :------------------------------------------------------- |
| Stationary accelerometer recording | Real impacts appear in the sensor readings                     | Whether the event can reach the motor stop system        |
| Injected synchronized stop         | Both controllers participate in the stop group                 | Whether a real sensor event can initiate it              |
| Real impact with motors stationary | The sensor event propagates through the synchronized stop path | Whether moving, queued steps stop quickly enough         |
| No impact during the test window   | A timeout is reported as inconclusive                          | How the threshold behaves amid normal printing vibration |

</div>

{% include figure.liquid path="assets/img/notebook/artorius-collision-detection/artorius-impact-y.png" alt="A recorded printer Y impact. The sensor X channel has the largest change." class="img-fluid rounded" zoomable=true original_link=true caption="The Y impact uses a different sensor channel because of how the accelerometer is mounted. The nearly constant sensor Y reading around −2,000 counts is gravity. The spike near the end marks the impact." %}

### Making sure a timeout does not count as success

One detail of the firmware affected how I judged the results. When the sensor's test window expires, it can send the same synchronized reason code as an impact. Cleanup commands can also trigger stop responses. If I had checked only whether both controllers reported reason `2`, I could have counted a run with no impact as a pass.

The new test checks the detector's recorded cause and requires spontaneous synchronization reports from both controllers before cleanup begins. Sensor causes `1`, `2`, and `3` mean raw acceleration, hardware tap, and both. Cause `4` means the deadline expired. A deadline is recorded as **inconclusive**, even if both controllers returned the expected stop reason. A communication failure or incomplete restoration is recorded as a failure.

A future calibration routine would have to distinguish a real impact from a deadline before recommending any motor sensitivity.

## How the detector processes acceleration

The LIS2DW is configured to sample at **1,600 Hz**, producing a reading every **0.625 ms**. At its selected **±16 g** range, one raw count corresponds to about **0.488 mg**. The accelerometer also measures gravity while sitting still, so a channel aligned opposite gravity reads around **−2,000 counts**, close to −1 g.

The raw collision detector looks for a sudden change rather than total acceleration. It establishes a baseline for each sensor axis and updates that baseline as new readings arrive. The basic calculation is the largest difference between a sample and its baseline on the selected axes:

$$
A_{\mathrm{residual}}=\max_{i\in\mathrm{selected\ axes}}|a_i-b_i|
$$

Here, `a` is the latest raw reading and `b` is the running baseline. In the plots, raw sensor Y stays near −2,000 counts at rest, while the red `magnitude` trace stays near zero. The red line shows the acceleration remaining after subtracting the baseline, rather than the length of the XYZ acceleration vector.

For the current X/Y stationary tests, the raw method requires **two consecutive samples** above the configured **2,000 mg** threshold. The second method uses the accelerometer's hardware tap logic. Its current tap threshold register setting is `3`, equivalent to approximately **1.5 g** at ±16 g, with a shock time of about **5 ms**. Sharp impacts and slow pressure on the toolhead do not necessarily produce the same result. Both methods need more validation during movement.

The physical orientation of the sensor also matters. Artorius uses `axes_map: z,-x,-y`. Printer X is detected mainly through sensor Z, while printer Y corresponds to negative sensor X. The dominant channels in my X and Y recordings are consistent with those mappings.

Each recording stores the latest **128 samples**. At 1,600 Hz, that amounts to **80 ms**, regardless of whether the sensor was armed for two seconds. The peak falls near the right edge because recording ends around the trigger. The buffer shows what happened before the impact, but does not show moving motor stopping distance.

## The software behind the stop

The custom EBB42 firmware saves its impact cause, recognition time, a short buffer of acceleration samples, and sensor status. On the host, a Kalico plugin controls the tests and records the results.

For synchronization, the plugin uses `CombinedDispatch`, which builds on Klipper's `TriggerDispatch` and `trsync` machinery. The Manta's participant has both CoreXY motor callbacks. The EBB42 joins as a sensor participant with no motor of its own. That avoids registering a motor twice or trying to stop the two CoreXY drivers independently.

When a trial ends, the plugin checks what caused the trigger, gathers the controller results, and disarms the accelerometer. The firmware restores the sensor registers used by the normal LIS2DW functions, and the plugin verifies that restoration. The supervised motion code is written to restore temporary motor current and acceleration settings, including after errors. I have not yet verified that recovery during a moving collision.

The software then clears the XY homing state. Even if the printer thinks it knows the carriage's coordinates before a collision, missed motor steps could make those coordinates wrong. The next movement should not rely on a position that has not been reestablished.

## Using the accelerometer to calibrate StallGuard

The immediate application I want is guided StallGuard calibration. Rather than guessing an `SGT` value, I want to make a short approach toward a known stop, record which signal fired, and use that result to decide what setting to test next. The same experiment would be repeated under controlled speed and current settings.

<div class="table-scroll resonance-table" tabindex="0" role="region" aria-label="Guided StallGuard calibration observations" markdown="1">

| Observation during an approach                                            | Possible interpretation                                                    | Next action                                                              |
| :------------------------------------------------------------------------ | :------------------------------------------------------------------------- | :----------------------------------------------------------------------- |
| StallGuard fires before observed contact                                  | Sensitivity may be too high or the motor may have encountered another load | Record a premature candidate and consider a higher, less sensitive `SGT` |
| StallGuard fires at independently confirmed contact                       | That setting may be suitable for those test conditions                     | Repeat before accepting it as a candidate setting                        |
| Accelerometer sees an impact without a StallGuard trigger                 | StallGuard may be insufficiently sensitive                                 | Abort, inspect the result, and consider a lower `SGT`                    |
| Neither detector provides a useful result before the travel or time limit | There is not enough evidence for a setting                                 | Stop at the limit and review the setup                                   |
| Both trigger almost together                                              | The event may be genuine, but its timing or source is ambiguous            | Preserve both records and avoid guessing which was first                 |

</div>

The prototype contains an optimizer that can propose `SGT` settings within the TMC5160's **−64 to +63** range. It also records independently labeled results, so a suspected motor stall does not automatically become a successful home. The proposal process is bounded and can narrow its suggested settings as evidence accumulates.

It is not unattended calibration. The current software requires an operator to authorize each motion trial, confirm the starting position, and provide independent labels. It does not automatically repeat collisions or write a recommended threshold into `printer.cfg`. Those restrictions will stay until I have measurements from moving tests and enough repetitions to judge consistency.

I will begin those tests at low speed, low motor current, and short travel. The initial commissioning configuration specifies **10 mm/s**, **0.6 A per XY motor**, **200 mm/s²**, at most **5 mm** of approach, and a **2 second** detector window. These are starting limits for a supervised experiment. They are not proof of a safe stopping distance.

## Other uses I want to investigate

### Collision detection during a print

A printer could use the same sensor to recognize the nozzle hitting a curled print, the toolhead running into an obstruction, or a carriage reaching a hard limit unexpectedly. This would be useful only if the detector could distinguish collisions from normal acceleration and vibration.

I still need data from actual prints, including acceleration changes caused by input shaping, travel moves, mechanical resonance, and deliberate speed changes. I also need to measure the motion stop itself: how quickly the motors stop after a known contact and how far the carriage moves during that interval. Until then, this code is restricted to supervised experiments. It does not provide collision protection during ordinary printing.

### Suspected skipped steps

A missed step may cause a small acceleration transient, or it may show up as a difference between the commanded motion and the measured response. Combining those signals with motor load estimates might make it possible to flag some step loss events.

An accelerometer cannot measure absolute toolhead position the way an encoder can. Integrating acceleration to estimate position accumulates error, particularly with vibration and bias. I would treat this as a possible diagnostic for skipped steps, not a way to count missed steps or recover coordinates without another reference.

### Outside forces on the printer

A toolhead being pushed by hand or knocked by another object should produce an acceleration pattern. The same data might eventually be useful for detecting external disturbances, loose mechanical components, or unwanted contact while the printer is idle. I would need to collect examples and separate those events from motor vibration and ordinary handling before turning them into alerts or controls.

### A package other printers could install

For other printers, I want installation to be mostly software: check the accelerometer and motor driver, set the sensor's axis mapping, and run guided tests. I would rather adapt the plugin than ask someone to wire another switch into a printer that already has useful sensors.

The present implementation has only been commissioned on Artorius's EBB42, LIS2DW, TMC5160, Manta, and specific firmware versions. A general release would need to recognize other hardware layouts, manage firmware compatibility, automate installation and rollback, and make the limitations of each detection mode clear to the user.

## What I have measured, and what I still need to measure

In the stationary tests, real impacts on X and Y reached the synchronized stop mechanism. Both controllers reported the trigger before cleanup. The detector returned its sensor configuration to its normal state, both motor positions were unchanged in the stationary tests, and XY homing was cleared afterward. I also confirmed that no impact produces an inconclusive deadline rather than a false pass.

The software test suite passed **271 tests** before these hardware experiments. The saved JSON and CSV records show the detector causes, synchronization results, and the accelerometer data used in the plots. The representative X and Y tests are `1793569752217076067-3` and `1793569772135084468-7`.

My next measurements are the time from contact to a stop during a commanded move, the distance traveled after contact, and false triggers during normal motion. I also need to test StallGuard settings across different speeds, motor currents, and temperatures before treating any setting as reliable.

## References and test records

- [Artorius resonance notebook](https://ethanmahajan.github.io/notebook/artorius-resonance/). The accelerometer's original use for measuring vibration and tuning input shaping.
- [Klipper TMC driver documentation](https://www.klipper3d.org/TMC_Drivers.html). StallGuard and sensorless homing behavior.
- [Klipper multi MCU homing documentation](https://www.klipper3d.org/Multi_MCU_Homing.html). The existing controller synchronization mechanism.
- [Analog Devices StallGuard2 application note](https://www.analog.com/en/resources/app-notes/AN-002.html). Stepper motor load detection and tuning.
- [ST LIS2DW12 product information](https://www.st.com/en/mems-and-sensors/lis2dw12.html). Accelerometer and tap detection.
- Project source and local test data: `accelerometer-stallguard/` and `printer_data/logs/accel_sg/`. The records reflect tests on Artorius, not independent benchmarks.
