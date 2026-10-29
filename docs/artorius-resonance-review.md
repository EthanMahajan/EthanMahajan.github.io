# Artorius resonance integration and portfolio review

**Superseded editorial approach:** The author requested restoration of the original article after this review. The current article uses the PDF's prose, with equation formatting and an interactive damping demonstration added. The editorial descriptions below document the earlier version and do not describe the current article.

Restoration verification: the complete article prose matches the PDF after excluding equation and presentation markup. The original BIQU B1 image and left/right plot comparisons are restored. The damping demo uses the analytical free response with fixed mass and stiffness, initial displacement 1 and velocity 0. Initial conditions, numerical ODE residuals for underdamped/critical/overdamped cases, and continuity near critical damping pass. Browser checks exercise the slider at 0, 0.12, 0.99, 1, 1.01, and 1.25, confirming classification and frequency output, plus mobile integration. The targeted Liquid/Kramdown preview and structural checker passed at that time. The later [continuous-improvement session](continuous-improvement-2026-10-29.md) resolved the local build limitation and verified actual production Jekyll output; the build limitations described below are historical.

Reviewed October 29, 2026. Changes are local; nothing was pushed or deployed.

## New story and evidence

`_notes/artorius-resonance.md` uses the existing notebook collection and layout. Artorius links to it in Testing & Revisions and through the automatic associated-note list. The homepage and Projects index also link directly to the story. The compact downloadable portfolio is unchanged; notebook entries supplement it.

The five-page source draft, **How resonances affected the design of Artorius.pdf**, supplied the first-person explanation. Its planning notes and demonstration placeholders were not treated as implementation instructions or published as content. Edits retain the author's explanations while correcting the distinction between natural and damped frequency, free and forced response, PSD amplitude and belt tension, and diagnostic estimates and demonstrated printing performance.

The supplied configuration folder was recursively inventoried: 31 PNG plots, 13 CFG files, four CONF files, two extensionless files, and one ZIP. The ZIP contains a configuration snapshot, not raw measurement data. No raw CSV/STDATA recordings or Fusion modal-analysis model were found. Repeated KAMP directory paths contain configuration material, not additional engineering results. Original inputs were left unchanged. Printer configuration and service files were not copied into public assets.

Selected assets are byte-for-byte copies, renamed for readable public URLs under `assets/img/notebook/artorius-resonance/`:

| Public asset       | Supplied source relative to the configuration folder                  |
| ------------------ | --------------------------------------------------------------------- |
| belts-20260503.png | ShakeTune_results/belts/beltscomparison_20260503_194931.png           |
| belts-20261018.png | ShakeTune_results/belts/beltscomparison_20261018_133400.png           |
| y-20260212.png     | shaper_calibrate_Y.png                                                |
| y-20261018.png     | ShakeTune_results/input_shaper/inputshaper_20261018_133953_axis_Y.png |
| x-20261018.png     | ShakeTune_results/input_shaper/inputshaper_20261018_133953_axis_X.png |
| speed-20261018.png | ShakeTune_results/vibrations/vibrationsprofile_20261018_152849.png    |

The source draft's embedded graphs were inspected against these files. Other saved belt-tuning iterations, X/Y calibrations, the axis-map check, static-frequency test, and vibration profiles were inspected for context. Only figures supporting the published explanation were selected. Dates come from plot labels, not file modification times. No graph was assigned to a numbered hardware revision without a configuration/change log.

The 1,500 mm/s² estimate is the February 12 3HUMP_EI row. The 10,460 mm/s² estimate is the October 18 SMOOTH_MZV row. They use different algorithms and cannot establish a controlled mechanical improvement. October's SMOOTH_EI alternative is 5,190 mm/s² with predicted residual vibration of 0.3%, compared with 2.6% for SMOOTH_MZV. The article states these limitations beside the comparison.

Technical background was checked against Klipper's official resonance measurement and compensation guides, linked in the story. No external benchmark was substituted for the author's measurements.

## Review cycle 1: evidence and integration

The original Artorius page described resonance as an unresolved problem without showing the diagnostic work. The new article makes the engineering reasoning inspectable: constraints, alternatives, physical model, observations, suspected causes, and next tests. It makes a stronger case for troubleshooting ability, while leaving performance claims bounded by the evidence.

Implemented: six original diagnostic plots, the existing frame CAD image, corrected equations, an accessible scrolling comparison table, explicit uncertainty, and local section navigation. The existing MathJax setup file was missing; restored it and allowed page-level opt-in so unrelated pages do not load math scripts. Removed an unnecessary legacy polyfill request from that optional block.

## Review cycle 2: access and remaining weaknesses

The five most consequential remaining weaknesses, in priority order:

1. **Print quality is not quantitatively validated.** The printer video and motion tests establish operation, while the shaper outputs predict behavior. A fixed-geometry print comparison with measured dimensions and surface photographs would close this gap. The article makes the distinction explicit instead of promoting estimates to results.
2. **Changes cannot be causally attributed.** Saved plots span months and processing changes. A dated revision log with one intervention per sweep would be stronger than inferred revision labels. Published captions use measurement dates and disclose this limitation.
3. **Dense plots are difficult to read on phones.** Retained full-width figures and image zoom, and added keyboard-accessible original-image links using an optional parameter on the existing figure include. The comparison table has keyboard focus, an accessible region name, and a horizontal-scroll hint.
4. **The strongest new evidence was buried.** Added direct links from the homepage and Projects index, plus an Artorius testing summary. These are small additions within existing components rather than a new card system.
5. **Other projects have uneven evidence and closure.** The phone mount documents a usable outcome and limitations. Air Purifier documents schematic work only; Shape Machine still lacks concrete before/after contribution examples; the chess set has an engraved board but no completed metal pieces. Their current status labels are appropriately candid. Source material here does not justify upgrading those claims.

The broader page review found no page-wide overflow at 390 px across the homepage, project index, five projects, research, and resume. This is a geometry check, not proof of full accessibility or complete interaction coverage. No numerical aesthetic rating was assigned. Existing source text for the other projects was preserved; speculative redesigns would add risk without addressing their missing evidence.

## Verification and limits

- `bundle check` and `bundle install` were attempted with the local Ruby 3.3.5 runtime. Installation fails when native extensions require the unavailable MSYS2 build toolchain. **A full fresh Jekyll production build did not run.** Production CI must still run before publishing.
- A targeted review harness used actual Liquid 4.0.4 and Kramdown 2.5.2 to render the modified content and includes into a previously built local site shell. New responsive image variants were generated locally for that preview. This checks content integration but is not equivalent to compiling every Jekyll plugin, stylesheet, and production asset.
- The existing portfolio checker passed on that 12-page review overlay: local links and fragments, image descriptions, metadata presence, notebook metadata, browser-model structure, and the existing linked two-page PDF. Unchanged pages and PDF assets came from the previous build.
- Chrome inspected the story at desktop and mobile widths, including dark mode, equations, the comparison table, and original figures. Eleven MathJax containers rendered without math errors; images loaded and the story had no page-wide overflow at the inspected sizes. The table scrolls within its region on mobile.
- Prettier was run on the changed source files. `node --check` validates the MathJax setup syntax. `git diff --check` verifies patch whitespace. Original project figures and technical sections remain present.
- This session did not exhaustively check external links, actual printer performance, screen-reader output, physical touch devices, or every external video/CAD interaction. Those are not represented as passed checks.

## Highest-impact new material to produce

1. Matched print specimens at documented settings, with surface photographs, dimensions, repeats, and explicit acceptance criteria.
2. Raw accelerometer files and an experiment log recording firmware, shaper version, sensor mounting, belt settings, and each mechanical intervention.
3. Fusion modal-analysis exports with boundary conditions, joint assumptions, mass model, mode shapes, and comparison to measured peaks.
4. Clear photographs of the operational printer and revised belt path, labeled by revision and date.
5. A permitted before/after example showing the personal Shape Computation Lab website contribution, or a finished second fabrication stage for another project.
