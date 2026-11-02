# Artorius collision notebook review

Initial integration reviewed November 1, 2026. The November 2 follow-up below supersedes the original verbatim-preservation assessment and records the subsequent technical clarifications. Permalink: `/notebook/artorius-collision-detection/`.

## Scope and editorial integrity

The authoritative Markdown is integrated in full. A canonical comparison against the supplied source passes after removing only metadata and presentation markup: every paragraph, heading, code identifier, equation, table cell, signal label, alt text and caption is preserved. The title and subtitle move into standard front matter; the printer/status block moves into optional `notebook_intro` metadata so it appears ahead of the contents links. Both 1500 × 900 PNGs are byte-for-byte copies of the supplied X and Y records. No technical or substantive editorial changes were made.

The existing collection automatically adds the note to Design Notes and Artorius’s Related Design Notes. Existing header/footer project links and the resonance reference are retained. Tables reuse accessible scrolling regions; a semantic ordered list replaces the ASCII flow without changing its eight labels. The sole shared navigation correction gives the existing Menu/theme buttons their intended theme text color, fixing the dark-mode contrast defect found in mobile review. No framework or new JavaScript was added.

## Editing resources and evaluation

Searched available skills, repository files, supplied attachments, Downloads and local plugin/skill directories. The complete `unsloppify` v1.4 and `no-ai-slop` skill instructions and a separate original `No AI slop eval` resource were unavailable. **No claim is made that those inaccessible skills were executed.** The supplied `Artorius_No_AI_Slop_Evaluation.md` was read in full; every check below was reviewed against the integrated source using that evaluation and the task’s explicit editing criteria. This is editorial judgment, not authorship detection. All applicable checks pass; the legacy Word-delivery clause is outside this website task.

## Editing principles

| Check                                                                                                           | Result | Review evidence                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------- |
| Editing principles 1: The edit keeps the original technical claims, figures, examples, and uncertainty.         | PASS   | Canonical source comparison passes, including every paragraph, table, equation and signal label.                                  |
| Editing principles 2: First-person decisions and the author's direct account of the printer remain intact.      | PASS   | All first-person prose is unchanged.                                                                                              |
| Editing principles 3: Clear passages remain intact, including the original descriptions of the threshold tests. | PASS   | No sentence was rewritten.                                                                                                        |
| Editing principles 4: The draft changes selectively and keeps nearly all of its original length and detail.     | PASS   | Only presentation markup and metadata changed; no content was abbreviated.                                                        |
| Editing principles 5: The opening explains the existing homing problem and why this printer is involved.        | PASS   | The existing motivation remains first; the supplied stationary status appears before navigation.                                  |
| Editing principles 6: The decision section presents the choice before describing the transport details.         | PASS   | Alternatives and the chosen approach still precede the controller explanation.                                                    |
| Editing principles 7: Technical claims are tied to concrete hardware, code behavior, or recorded tests.         | PASS   | Original hardware, identifiers, settings and record IDs remain intact.                                                            |
| Editing principles 8: General sentences were tightened around Artorius and its implementation.                  | PASS   | No generic introductory material was added.                                                                                       |
| Editing principles 9: The author remains the subject of design, testing, and implementation decisions.          | PASS   | The author’s requirements, deployment, recovery and physical testing contributions remain explicit; Codex assistance is retained. |
| Editing principles 10: The alternatives table, mechanism diagram, analysis, and future work remain.             | PASS   | All three tables, eight signal steps, analysis and future-work sections are present.                                              |
| Editing principles 11: Tangled sentences were split without forcing all paragraphs into identical length.       | PASS   | Existing sentence and paragraph boundaries are retained.                                                                          |

## Words to cut

| Check                                                                                                                                 | Result | Review evidence                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------ | ---------------------------------------------------------------------------------------------- |
| Words to cut 1: Banned prestige words and empty rhetorical fillers are absent from article prose. Established technical terms remain. | PASS   | Manual review found no added prestige language or filler; all original technical terms remain. |

## Patterns to cut

| Check                                                                                                                                          | Result | Review evidence                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ---------------------------------------------------------------------------------------- |
| Patterns to cut 1: No staged 'not X, but Y' openings or throat-clearing setups; technical qualifications remain where they prevent misreading. | PASS   | No staged rhetorical opening was added; genuine engineering qualifications are retained. |
| Patterns to cut 2: No faux-insight reveal, fake-strong verb sequences, or repeated mic-drop fragments.                                         | PASS   | No reveal or punchline structure was added.                                              |
| Patterns to cut 3: Claims about testing and system design cite mechanisms, settings, and local records rather than anonymous authority.        | PASS   | Claims still refer to concrete mechanisms and documented stationary tests.               |
| Patterns to cut 4: Phrases announcing that a point is 'important' or 'straightforward' were replaced by the underlying explanation.            | PASS   | No unsupported importance claims were added.                                             |
| Patterns to cut 5: No fake-profound ending; the article closes on specific measurements still needed.                                          | PASS   | The final engineering paragraph specifies the next measurements.                         |
| Patterns to cut 6: The final paragraphs identify concrete future measurements, without an extra recap conclusion.                              | PASS   | No additional recap conclusion was added.                                                |
| Patterns to cut 7: Headings organize substantive sections, charts serve a technical purpose, and tables compare actual options.                | PASS   | Headings cover substantive stages; figures and tables retain technical functions.        |
| Patterns to cut 8: Headings and prose use sentence case after colons where applicable; code identifiers are unchanged.                         | PASS   | Original sentence-case headings and exact code identifiers remain.                       |
| Patterns to cut 9: The article uses no em dashes.                                                                                              | PASS   | The article source contains no em dash.                                                  |

## Final read

| Check                                                                                                                                                                       | Result | Review evidence                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Final read 1: Paragraphs vary in length and form without repetitive punchlines.                                                                                             | PASS   | Original paragraph lengths and forms are retained.                                                                                                                                          |
| Final read 2: Editorial judgment: the piece retains the author's first-person mechanical engineering project voice. Final approval of personal voice belongs to the author. | PASS   | First-person voice is preserved verbatim; final judgment of personal voice belongs to the author.                                                                                           |
| Final read 3: Engineering statements remain readable without staged persuasion or unnecessary jargon in the opening.                                                        | PASS   | The opening explains sensorless homing in ordinary language before the deeper firmware sections.                                                                                            |
| Final read 4: Complete edited draft supplied in Markdown and Word, followed by a brief `What changed` summary in the delivery message.                                      | PASS   | The full Markdown article is integrated in the website and a change summary accompanies the PR. The supplied evaluation’s Word-delivery clause does not apply to this website-only request. |
| Final read 5: Not a detect-only request; the edit was made and is supplied.                                                                                                 | PASS   | An integrated page and presentation edits are supplied; this is not a detection-only assessment.                                                                                            |

## Protected engineering content

PASS: 271 historical firmware/plugin tests; eight successful stationary attempts and three inconclusive deadlines; 1,600 Hz, 0.625 ms, ±16 g, 0.488 mg/count, 128 samples and 80 ms; 3,000/2,000 mg commissioning thresholds; two consecutive samples; tap register 3, approximately 1.5 g and 5 ms; SGT −64 to +63; 10 mm/s, 0.6 A, 200 mm/s², 5 mm and 2 seconds; exact hardware, software and record identifiers. These are preserved author-reported results, not tests rerun against the printer during website integration. Stationary synchronization remains distinct from unmeasured moving-stop latency/distance and recovery.

## Audience reviews

- Recruiter: PASS. The opening gives the purpose and verified status; Alternatives, Commissioning and Results and limits provide direct scanning routes. Personal requirements, hardware mapping, deployment, recovery preparation and physical tests are explicit, alongside Codex’s assistance. Preliminary results remain qualified.
- Hobbyist: PASS. The StallGuard and LIS2DW explanations precede synchronization and implementation. Hardware compatibility, custom firmware, supervised trials and the absence of ordinary-print collision protection remain explicit. No general installation/release claim was added.
- General reader: PASS with a remaining density limitation. Sensorless homing, impact detection and coordinated CoreXY stopping are explained in ordinary language before implementation details. CAN and controller names are still specialist vocabulary, but the signal-path section explains their roles. The full technical explanation is retained rather than shortened. The numbered flow provides an additional route through it.

## Functional verification

- `bundle check`: PASS using the existing ignored Ruby 3.3.5 runtime and installed gems.
- `python scripts/build_portfolio.py`: PASS; model current, PDF/share cards and image dimensions generated. Generated outputs remain ignored and uncommitted.
- `JEKYLL_ENV=production bundle exec jekyll build --destination tmp/collision-site`: PASS, actual production Jekyll output including Sass, Liquid, minification and responsive WebP variants. Final recorded run: 5.718 seconds. Existing Ruby `fiddle` future-version warning only.
- `python scripts/check_portfolio.py tmp/collision-site`: PASS, 13 pages, local links/fragments, metadata, assets, notebook association, current model and linked two-page PDF.
- `node scripts/check_damping.cjs tmp/collision-site/assets/js/damping-demo.js`: PASS, initial conditions, ODE residuals, decay and critical-damping continuity.
- Canonical source/image comparison: PASS as described above (local review script in ignored `tmp/check_collision_source.py`).
- Changed-source Prettier: PASS for the note, layout, Sass and review report. `git diff --check`: PASS. Full CI command `npx prettier . --check`: FAIL on 81 existing files, all outside the changed source files. Unrelated formatting was left intact.
- HTTP checks: resonance reference and both Klipper documentation URLs returned 200. Analog Devices and ST requests timed out at 20 seconds; retained authoritative supplied URLs and recorded them as unverified, not broken.

## Browser verification

Served the actual build using `python scripts/serve_preview.py tmp/collision-site --port 8771` and inspected screenshots in the in-app browser at 1440 × 1000, 768 × 1024, 390 × 844 and 375 × 812 in light and dark themes. No page-wide horizontal overflow appeared at those widths. Tables keep their 640 px readable layout inside keyboard-focusable local scroll regions (335 px wide at the 390 px viewport). ArrowRight changed the table’s scroll position to 40 px with a visible solid focus outline.

The residual equation rendered in MathJax without an error and fitted the mobile article. All 11 contents links resolve to existing headings. Sample Signal path and Detector jumps put their headings below the 65 px fixed navigation (observed top about 162 px). Back to top returned focus to `main-content`. The mobile Menu opened and closed and the theme cycle worked. Browser error/warning logs were empty when checked.

Both figure URLs and responsive variants pass the structural checker. The X original was also opened directly in the browser and loaded at its unchanged 1500 × 900 resolution. An image click registered the existing medium-zoom open state; detailed touch/pinch zoom was not tested. Inline graph labels are necessarily small on phones, with the existing original-image links available for closer inspection. X and Y axes, gravity offset, residual magnitude and buffer duration remain explained in the article.

The existing resonance page was visually compared at desktop and mobile sizes; it retains its typography, contents list, figures, equations and demo. The new intro hook is absent from notes that do not opt in. Its source content is untouched. The only intentional shared visual difference is corrected dark Menu contrast. Artorius’s related-note link and the Design Notes index entry were verified in browser DOM as well as by the structural checker.

Screenshots are stored beside this report: desktop/tablet/mobile/small-mobile light and dark openings, plus mobile table, equation and signal-path views. Early captures precede the final one-line Menu color fix; the final mobile and small-mobile dark captures show the correction.

## Limits

The inaccessible editing skills cannot be certified as executed. Two external vendor links remain unverified due to timeouts. No physical printer experiments, firmware test suite, screen reader, real touch device or exhaustive accessibility audit was run as part of this content task. The repository’s optional axe workflow is not a substitute for those checks; remote PR CI results are reported separately. The broken-links workflow is restricted to the upstream al-folio repository and does not run for this fork. Nothing is merged or directly deployed.

## Added directional tap video

The author subsequently supplied `IMG_2219.MOV` (30.912 seconds, 1920 × 1080) and described the X/Y finger taps and predominantly axis-selective response. Added the full clip in Trying it on the printer, with native keyboard-accessible controls, inline playback, a still poster, an accessible label, explanatory caption and direct MP4 link. There is no autoplay, and `preload="none"` avoids downloading the 22.4 MB video until requested.

The web copy retains the full duration, 1080p frame dimensions and original AAC audio, transcoded to H.264/AAC MP4 with fast-start layout. Extra Apple spatial-audio and data streams and source metadata were omitted. A still/contact-sheet inspection confirms the stationary printer, finger taps and laptop interface. The author’s axis-selectivity description is qualified as a demonstration, not a measured false-trigger rate or moving-collision result. No speech transcript or independent quantitative directional analysis is claimed. The source article remains intact; the new video figure/caption is excluded from the preservation comparison as a separately authorized addition.

Video follow-up validation: production Jekyll rebuild PASS (3.705 s), the 13-page structural checker PASS, source-preservation comparison PASS, changed-source Prettier PASS and patch whitespace PASS. `ffprobe` confirms H.264/AAC, 1920 × 1080 and a 30.931 s web duration (the slight container/audio padding differs from the 30.912 s source). Keyboard Space started playback in the browser; ready state reached 4, playback advanced past 14 seconds, and Space paused it without a media error. Inspected the native player at 390 px (335 × 188 px) and 1440 px (820 × 460 px), with no page-wide overflow. `mobile-video.png` and `desktop-video.png` show those views. Re-reviewed the added caption against the supplied editorial criteria: PASS; the word “mostly” and experimental limits are retained. Remote CI for the video commit is reported in the PR.

## Independent follow-up: November 2, 2026

Reviewed PR #13 at `2c25309` against both supplied Markdown files and the two original PNGs before editing. The canonical comparison passed at that commit, including image byte identity. The original integration did not omit technical substance. The existing video is retained as a previously documented addition, not treated as evidence supplied in this review.

### Findings and corrections

No critical or major defect found. Targeted changes in `_notes/artorius-collision-detection.md`:

- **Moderate, detector scale:** “raw count” did not identify the representation. A reader using the datasheet's 14-bit digits could apply the wrong scale by a factor of four. Explained unshifted 16-bit register units (0.488 mg/count) versus right-shifted 14-bit digits (1.952 mg/digit at ±16 g). Retained the original conversion and gravity interpretation. This is a representation clarification, not a recalibration of the supplied traces.
- **Moderate, recording duration:** 128 sample periods at the nominal rate are 80 ms, while the first-to-last interval covers 127 periods (79.375 ms). Both supplied plots extend to roughly 82 ms. Clarified nominal duration, distinguished the firmware history from the sensor's 32-sample FIFO, and explicitly left the plot timing discrepancy unresolved pending CSV timestamps. No explanation for the discrepancy was invented.
- **Minor, tap timing:** defined “shock time” as the maximum over-threshold duration accepted by the tap logic. It is not measured motor-stop latency.
- **Minor, first-use vocabulary:** expanded CAN and identified Kalico as the Klipper fork used here.
- **Minor, references:** added direct ST datasheet and AN5038 links so readers can check representation and tap settings. No layout, dependency, or unrelated-page changes were needed.

The source diff contains only these clarifications and the added reference. All original sections, comparisons, equation, test outcomes, identifiers, commissioning limits, contribution statement, uncertainty and future work remain. The supplied plots are unchanged.

### Technical evidence and limits

Checked the [ST datasheet](https://www.st.com/resource/en/datasheet/lis2dw12.pdf), table 3, and [AN5038](https://www.st.com/resource/en/application_note/dm00401877-lis2dw12-alwayson-3d-accelerometer-stmicroelectronics.pdf), register map and tap configuration. AN5038 gives FS/32 for the tap threshold: register 3 at ±16 g corresponds to 1.5 g. The datasheet's timing definition supports the shock-time clarification. The 16-bit representation explanation is consistent with the stated scale and visible gravity offset; custom logger code was not supplied for independent inspection.

[Analog Devices AN-002](https://www.analog.com/en/resources/app-notes/AN-002.html) supports the electrical load-estimation explanation. [Klipper TMC documentation](https://www.klipper3d.org/TMC_Drivers.html) supports the signed sensitivity direction and operating-condition limits. [Multi-MCU homing documentation](https://www.klipper3d.org/Multi_MCU_Homing.html) supports the distinction between triggering and motor overshoot. These sources do not independently verify Artorius's custom `CombinedDispatch` code, cause codes, register restoration or recorded outcomes. Those remain author-reported. No firmware source, raw JSON/CSV records or printer connection was available in this review. The historical 271 tests were not rerun.

### Audience and writing evaluation

Recruiter **PASS**: purpose/status are visible at the opening; alternatives, personal contribution and Codex assistance remain concrete. Hobbyist **PASS**: register units and timing are now explicit, and hardware/firmware compatibility and supervised-use limits remain. General engineering reader **PASS**: CAN and Kalico now have first-use explanations; the narrative still proceeds from motivation and alternatives to implementation and evidence.

Re-read every supplied evaluation check after editing. These are editorial judgments; the complete named writing skills are not available in the catalog or located files, so they are not claimed as executed. The table below uses the supplied evaluation's check numbers, not an invented replacement rubric.

| Group and check       | Result                        | Evidence                                                                                                            |
| --------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Editing principles 1  | PASS                          | Measurements and uncertainty preserved; timing discrepancy explicitly qualified.                                    |
| Editing principles 2  | PASS                          | First-person account retained.                                                                                      |
| Editing principles 3  | PASS                          | Commissioning threshold-test descriptions unchanged.                                                                |
| Editing principles 4  | PASS                          | Five localized prose clarifications; no section removed or condensed.                                               |
| Editing principles 5  | PASS                          | Original homing motivation retained.                                                                                |
| Editing principles 6  | PASS                          | Alternatives still precede transport details.                                                                       |
| Editing principles 7  | PASS                          | Added primary documentation; author-reported evidence distinguished above.                                          |
| Editing principles 8  | PASS                          | Definitions explain the actual installed system.                                                                    |
| Editing principles 9  | PASS                          | Author's contribution and Codex assistance unchanged.                                                               |
| Editing principles 10 | PASS                          | Tables, signal sequence, analysis and future work retained.                                                         |
| Editing principles 11 | PASS                          | Gravity explanation separated from register representation.                                                         |
| Words to cut 1        | PASS                          | No prestige language or rhetorical filler added.                                                                    |
| Patterns to cut 1     | PASS                          | Contrasts distinguish technical representations and measured versus unmeasured quantities.                          |
| Patterns to cut 2     | PASS                          | No staged reveal or punchline fragments.                                                                            |
| Patterns to cut 3     | PASS                          | Specific hardware documentation and recorded test identifiers.                                                      |
| Patterns to cut 4     | PASS                          | Mechanisms explained without importance inflation.                                                                  |
| Patterns to cut 5     | PASS                          | Ending still identifies measurements needed.                                                                        |
| Patterns to cut 6     | PASS                          | No extra recap conclusion added to article.                                                                         |
| Patterns to cut 7     | PASS                          | Existing substantive headings and technical visuals retained.                                                       |
| Patterns to cut 8     | PASS                          | Sentence-case headings retained.                                                                                    |
| Patterns to cut 9     | PASS                          | Article contains no em dash.                                                                                        |
| Final read 1          | PASS                          | Paragraph forms vary; no repetitive punchlines.                                                                     |
| Final read 2          | PASS                          | First-person voice retained; author has final voice judgment.                                                       |
| Final read 3          | PASS                          | First-use definitions reduce unexplained jargon.                                                                    |
| Final read 4          | FAIL literally; outside scope | Website Markdown delivered; no Word file requested or produced. This is not a writing defect to fix in the website. |
| Final read 5          | PASS                          | Actual targeted edits supplied.                                                                                     |

### Follow-up verification

- `bundle check`: PASS with existing local Ruby 3.3.5 runtime prepended to PATH.
- `$env:JEKYLL_ENV='production'; bundle exec jekyll build --destination tmp/collision-site`: PASS, final run 3.383 seconds; existing Ruby fiddle warning only.
- `python scripts/check_portfolio.py tmp/collision-site`: PASS, all 13 pages, links, anchors, assets, metadata and project association.
- `node scripts/check_damping.cjs tmp/collision-site/assets/js/damping-demo.js`: PASS.
- `npx prettier _notes/artorius-collision-detection.md docs/artorius-collision-review.md --check` and `git diff --check`: PASS after formatting.
- Initial `python tmp/check_collision_source.py`: PASS before edits. Exact identity is intentionally no longer claimed after the documented clarifications; reviewed the complete final diff for preserved content. Both image files remain untouched.
- Browser: new opening captures at 1440, 768, 390 and 375 px, each 900 px high, in light and dark modes. No page-wide horizontal overflow. Inspected revised detector at 390 px and references at desktop; MathJax had zero error nodes and browser warning/error logs were empty. Menu and theme controls operated successfully. Compared the resonance notebook at 375 px. Earlier wider resonance and table/player interaction checks above are historical, not claimed as repeated here.
- Screenshots: `revised-responsive.jpg` and `revised-detector-mobile.jpg` in the adjacent screenshot directory. No redesign warranted by these checks.
- Previous head `2c25309` CI is now complete: production build PASS, formatter FAIL, upstream-only broken-links job skipped. This supersedes the earlier “still running” status. Repository-wide formatting problems remain outside this targeted change; fresh changed-file formatting passes. GitHub CLI check retrieval returned HTTP 401, so remote status was obtained through the connected GitHub tool.

Remaining uncertainty is the source-record timing discrepancy and independent verification of the custom firmware and historical experiments. No moving collision performance claim was added. PR remains open and unmerged.
