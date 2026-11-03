# Website feedback review — November 3, 2026

Implemented the 32 browser comments in the local Jekyll site. The updated preview is served at http://127.0.0.1:8773/. These changes are not published.

## Changes by comment

| Comments | What changed                                                                                                                                                                                                                                                                               |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1–4      | Homepage and project/research card titles use the theme green without underlines, including hover. Applied the same treatment to linked headings and related-note titles.                                                                                                                  |
| 5        | Renamed the homepage section “Contact Information.” Its heading, email, LinkedIn, and resume links share a row on desktop; links use smaller type without underlines. They wrap on narrow screens.                                                                                         |
| 6        | Removed the border and special padding from the navbar Resume link.                                                                                                                                                                                                                        |
| 7        | Moved Portfolio (PDF) into the Projects header at the upper right.                                                                                                                                                                                                                         |
| 8–9      | Renamed repository links to “GitHub,” including their accessible labels and project resource links.                                                                                                                                                                                        |
| 10–11    | Restored the purifier electrical schematic thumbnail and removed the generated system diagram from the case study.                                                                                                                                                                         |
| 12–13    | Purifier status now says the schematic is finished while PCB layout and mechanical design are undecided. Added planned laser cutting alongside FDM printing; the housing is described as likely laser-cut panels with printed fixtures.                                                    |
| 14, 23   | Vertically centered the project summary beside the overview image/video. This lowers the purifier and phone-mount summaries while preserving the mobile stack.                                                                                                                             |
| 15       | Added the motivation to understand room air quality, including during 3D printing, alongside filtration and background noise. Kept fume hazard assessment as a question, not a capability of the particulate sensor.                                                                       |
| 16       | Removed the purifier's planned-validation table and repetitive status checklist. The short design section states the next decisions.                                                                                                                                                       |
| 17–18    | Added reused aluminum extrusion alongside the Z motors and 24 V supply. Omitted minor screws/cables from the summary and removed “practically.”                                                                                                                                            |
| 19, 24   | Centered figure captions throughout the site. Centered the research image and its caption as a unit.                                                                                                                                                                                       |
| 20       | Renamed the viewer “Interactive 3D assembly.” It loads when it approaches the viewport, with a manual button for fallback/retry, static image, and download link retained.                                                                                                                 |
| 21       | Updated Artorius to confirmed motion at 1,000 mm/s and 250,000 mm/s². Added the expected 50 mm³/s flow limit and the 50 ÷ (0.25 × 0.5) = 400 mm/s estimate for the 0.5 mm nozzle. Motion results, expected flow, and print-quality limits remain distinct.                                 |
| 22       | Replaced the closing list of old issues with better high-speed cooling, print-quality tuning, and a full printer enclosure. Historical build observations remain in their original chronological context.                                                                                  |
| 25       | Research is now a thumbnail catalog. Its study opens at /publications/printed-cups/, with the original methods, observations, limitations, report links, and citation preserved. Homepage study links go directly to the detail page; old index anchors still resolve.                     |
| 26       | Replaced the resume contents disclosure with an always-visible navigation list matching the notebook contents style.                                                                                                                                                                       |
| 27       | Condensed the collision article around motivation, signal path, stationary tests, and next steps. Retained the demonstration video, one inline plot, a link to the Y plot, test counts, operator supervision, Codex attribution, and motion-test limitations.                              |
| 28       | Rewrote the resonance article using the supplied five-page PDF: frame decisions, belt response, interpreting acceleration/speed plots, and input shaping. Kept the diagrams, numerical comparisons, and uncertainty; moved the longer mathematical derivation into an optional disclosure. |
| 29       | Centered the “In this article” label and navigation links; applied the shared layout to the resume navigation too.                                                                                                                                                                         |
| 30–31    | Removed forced MathJax overflow that created equation scrollbars. Preserved equations rather than clipping their contents.                                                                                                                                                                 |
| 32       | Removed “Choose preset.” The current damping classification is now a bordered, clickable control with a dropdown indicator.                                                                                                                                                                |

## Writing and evidence decisions

The anti-slop review removes repetitive cautions and abstract process language without upgrading a planned feature or analysis estimate into a measured result.

The collision article is substantially shorter. The full prior technical record is preserved in [artorius-collision-technical-record.md](artorius-collision-technical-record.md), outside the published site. It retains register settings, timing/scale details, recovery behavior, calibration logic, and record IDs that would overwhelm the main article. The published note retains its November 1 stationary-test status; the newer Artorius motion-speed result does not establish collision stopping performance.

The resonance PDF was read in full and visually inspected. Its opening editorial prompts were treated as draft material, not instructions. The rewrite does not repeat its claims that PSD peak height proves belt tension, that multiple peaks identify binding, or that differing shaper estimates prove a print-quality improvement. The original formulas and their underdamped/free-response conditions are retained. The PDF mentions an available Fusion modal-analysis file, but that file and raw accelerometer records were not supplied; no simulation results or new analysis were invented.

The November 3 motion figures come from the owner's update. The 400 mm/s figure is an approximate flow calculation, not a measured printing result. Supporting technical references remain linked in the article: [Klipper resonance measurement](https://www.klipper3d.org/Measuring_Resonances.html#selecting-max_accel) and [resonance compensation](https://www.klipper3d.org/Resonance_Compensation.html).

Updated the purifier's resume/skill evidence wording and regenerated the two-page portfolio PDF so the project summaries agree with the website.

## Verification

- Production Jekyll build completed using the existing local Ruby runtime.
- Site checker passed across 14 pages: local links and anchors, image descriptions, metadata, browser-model assets, and the linked two-page portfolio.
- Damping checks passed: initial conditions, differential-equation residuals, nonoscillatory decay, and continuity at critical damping.
- Browser inspection confirmed green, non-underlined headings and a single-row desktop contact area.
- Verified the Projects header link and restored schematic thumbnail.
- Verified summary placement on the purifier and phone-mount pages, plus the stacked mobile layout.
- Clicked the research catalog card and verified the centered image/caption on the detail page.
- Verified that the resume navigation is visible without opening a disclosure.
- Verified automatic 3D model loading, zoom, and reset in the browser.
- Opened the mathematical details and checked all four display equations. No internal equation scrollbars or page overflow at mobile width.
- Selected Overdamped from the classification dropdown and confirmed the graph, classification, and nonoscillatory frequency label updated.
- Inspected desktop and 390 px mobile layouts. This is browser viewport testing, not a physical-device or screen-reader audit.
- Rendered and visually checked both portfolio PDF pages for clipping and overlap.

## Delivery

The source edits and this review remain local. The local preview includes the updated portfolio PDF. The resume PDF uses the repository's existing RenderCV workflow and has not been regenerated in this pass. The original research report and the supplied resonance reference PDF were not edited.

## Follow-up annotations: 16 additional changes

- **1:** Moved Related Design Notes directly below Project at a glance. Both Artorius titles remain complete, with their dates on separate lines.
- **2–4:** Centered the phone-mount CAD assembly at a smaller width. Rebuilt the holder and base details as two bordered text/image pairs in one desktop row, stacking the pairs on mobile. Centered the findings table and removed “assembly required a workaround” from its first row.
- **5:** Renamed the project to Air Purifier, including its generated card labels and portfolio PDF bookmark.
- **6:** Made the chess-board engraving video visible without expanding a disclosure. It sits below the planned-pieces section, with Board fabrication text to its right on desktop.
- **7–9:** Centered the collision video and placed smaller X/Y impact plots side by side. Explained the recorded `axes_map: z,-x,-y` mapping for all three printer axes and why the negative sensor-Z spike belongs to the printer-X test. The mapping comes from the preserved technical record.
- **10:** Replaced the two upstream Klipper references with the corresponding official Kalico TMC-driver and multi-MCU-homing documentation; both destinations were checked.
- **11–12:** Restored detail around the early and later Y-response plots. The text explains the broad early peaks, likely mechanical checks, the later dominant peak, and remaining friction/bearing speculation. Frame support, belt routing, and tension work lead the comparison; the changed analysis software remains a qualification on numerical acceleration recommendations. No individual mechanical cause is presented as proven.
- **13–15:** Removed the duplicate divider before Education; added visible Georgia Tech dual enrollment for Fall 2025–Spring 2026, covering Linear Algebra and Multivariable Calculus; indented the project examples under each skill.
- **16:** Ordered additional experience newest first: Mercor & Handshake AI, Wyzant, then Mathnasium. Applied the same chronology convention within engineering experience, projects, and involvement.

Writing was reviewed with anti-slop for fidelity, continuity, and useful detail. Dates, test counts, equations, and measured-versus-estimated distinctions were retained. The dual-enrollment entry uses the supplied semesters without inventing months. The website and shared resume data are updated; the downloadable resume PDF still uses the repository's separate RenderCV publishing workflow.

Follow-up verification: production Jekyll build and the 14-page portfolio checker passed. Desktop browser checks covered Artorius note placement, phone-mount pairs, the visible engraving video, centered collision media, and resume education/order. At 390 px, phone-mount pairs stack and the resume has no horizontal overflow. The regenerated two-page portfolio PDF was rendered and inspected; its Air Purifier title and bookmark agree with the site.

## Third annotation pass: eight changes

- **1:** The Artorius viewer now loads automatically after the page load event, all page images (including those below the viewer), and fonts have settled. It starts during browser idle time, with a timer fallback. Failed images do not block it indefinitely. The manual load button remains available.
- **2–4:** Removed the requested extrusion-estimate sentence, began the remaining sentence with “However,” specified tuning slicer and Klipper settings, and renamed the resource link “Artorius GitHub.”
- **5:** Expanded Board fabrication using the supplied process: 5 × 5 ft, 3/4-inch birch plywood; 16 rough-cut blanks; table-saw squaring and sanding at Georgia Tech’s Invention Studio; laser engraving; and a ripped, miter-cut, glued walnut border with rank/file labels. The copy identifies what the video shows.
- **6:** Moved the reverse-board photo to the right and vertically centered the adjacent status text.
- **7:** Centered standalone resonance figures and their images, including both Y-axis plots.
- **8:** Replaced the Languages and Interests disclosure with an always-visible resume section.

Verification: production build and 14-page portfolio checks passed. A focused loading-order check passed for pending images, image errors, font readiness, cached pages, idle scheduling, and the timer fallback. Browser inspection confirmed automatic model display, the chess layout, centered resonance images, and the absence of a Languages/Interests disclosure. Anti-slop review preserved the supplied fabrication sequence and dimensions without adding measurements or fabrication claims.

Final resume adjustment: moved Interests before Languages and indented both entry groups by 1.5rem beneath their headings. Added spacing before Languages.
