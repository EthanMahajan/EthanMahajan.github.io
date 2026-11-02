# Artorius collision notebook review

Reviewed November 1, 2026. Permalink: `/notebook/artorius-collision-detection/`.

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
