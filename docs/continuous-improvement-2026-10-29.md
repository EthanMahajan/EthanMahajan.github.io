# Continuous portfolio improvement — October 29, 2026

## Scope and safeguards

This log covers the improvement session requested after restoring the author's resonance article. Preserve that article's prose and technical meaning. Improve presentation and behavior using the existing Jekyll components. Do not invent evidence, change project completion status, push, or deploy.

The working tree already contains the resonance article, damping demo, figure links, and associated site edits from this conversation. They are the starting point, not unrelated work to discard. A copy of the starting article is retained in ignored `tmp/article-before-continuous-improvement.md`. Its SHA-256 is `E71103EC10BFF850980145EB82EAAC49231AF7E3EFFEB78D1CCAFD89DCED4A0F`.

## Cycle 1 — reliable rendering and readable navigation

Ranked findings before implementation:

| Priority | Finding and evidence                                                                                                                      | Why it matters                                                                                     | Intended correction                                                                            |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| 1        | Full local Jekyll build has not run; earlier previews combine new content with an older shell. Native Ruby gems require MSYS2.            | A successful overlay can conceal integration and deployment failures.                              | Install the missing tools under ignored workspace runtime folders and build the actual site.   |
| 2        | The figure include's error handler removes every `.responsive-img-srcset` on the page and depends on jQuery.                              | One failed image can alter unrelated figures, and early loading failures can hit an undefined `$`. | Restrict recovery to the failed image's own picture element with native DOM methods.           |
| 3        | The restored long article has four major sections but no contents navigation near its beginning.                                          | Readers must scroll extensively to reach input shaping and the demo.                               | Add optional section navigation through the notebook layout without changing the article body. |
| 4        | `.navbar` has `opacity: 0.95`; text behind it was visible in the actual dark preview.                                                     | Overlapping text reduces navigation clarity on long pages.                                         | Use the existing opaque theme background.                                                      |
| 5        | Shared figures emit invalid `width="100%"` and `height="auto"` attributes when dimensions are absent. Alt/title attributes are unescaped. | Invalid dimensions weaken layout predictability; quotes in descriptions can break markup.          | Omit unspecified numeric dimensions and escape descriptive attributes.                         |

Changes, validation results, and subsequent review cycles will be recorded below as they complete.

Cycle 1 results:

- The actual production Jekyll build succeeds, including Sass, JavaScript minification, bibliography, layouts, and 102 responsive image variants. The only build warning concerns Ruby's future `fiddle` dependency behavior; no source error is being hidden.
- The local build tools are installed under ignored `tmp/runtime/`. Ruby 3.3.5 needed a current pthread DLL to match newly compiled extensions; the original DLL is backed up alongside it. Native compile options are confined to ignored `.bundle/config`. The lockfile adds Windows platform packages/checksums without changing existing dependency versions.
- The strengthened checker now follows local script URLs and responsive `srcset` URLs and rejects invalid image dimension attributes.
- A 30-page/viewport browser pass at 390, 768, and 1280 px found a regression from removing the old percentage-width attribute: the research photograph expanded to its intrinsic 4032 px width. Added a shared `max-width: 100%` constraint, and scheduled a fresh build/recheck. The other nine page types had one h1, no loaded-image failures, and no page-wide overflow in that pass.
- The actual notebook page has working section links, an opaque navbar, rendered equations, a visible damping curve, and no console errors during the initial inspection. Article body text remained byte-for-byte unchanged in Cycle 1.

## Cycle 2 — evidence access and regressions

| Priority | Finding and evidence                                                                                                                    | Why it matters                                                                                         | Action                                                                                                                                                                                 |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1        | The fresh build exposed a stale generated CAD preview: source checksum differed from the old manifest.                                  | Visitors would inspect an older assembly while downloading a newer one.                                | Regenerated with the existing script: current source is 57,564,191 bytes; preview is 12,867,806 bytes, retaining all 933 meshes and nine material groups. Original assembly unchanged. |
| 2        | Research overflow appeared during the Cycle 1 browser pass.                                                                             | Horizontal scrolling makes the research report difficult to use.                                       | Constrain shared figure images; recheck across the same viewport matrix.                                                                                                               |
| 3        | Resonance comparisons inherit a fixed 220 px image height from generic galleries.                                                       | Tall diagnostic plots shrink unnecessarily within their columns.                                       | Preserve their aspect ratios; use two columns on desktop and a deliberate stacked layout below 768 px.                                                                                 |
| 4        | The standalone printer image occupies close to an entire desktop viewport, and the long article lacks the existing back-to-top control. | Supporting context displaces the more valuable diagnostic evidence and makes return navigation slower. | Limit this illustration to 420 px wide and opt the note into the existing back-to-top behavior.                                                                                        |
| 5        | Comparison captions only say earlier/later, while the prose refers to left/right.                                                       | Once figures stack on phones, readers lose the original comparison reference.                          | Add left/right labels and measurement dates from the saved figures to captions, without changing the author's explanations.                                                            |

Presentation markup and front matter may change in Cycle 2; compare prose after excluding Liquid figure includes and HTML wrappers rather than comparing raw file bytes.

Cycle 2 results:

- Production rebuild passed in 2.714 seconds, reusing the responsive-image cache. The expanded checker passed on all 12 generated pages, including current source/preview model hashes, geometry structure, script references, responsive images, and linked two-page portfolio PDF.
- A browser fixture used the actual generated figure error handler with a deliberately missing WebP and two independent pictures, without loading jQuery. The failed picture recovered to its original PNG and the unrelated picture retained its source. The fixture reported PASS.
- Research at 390 px now has no page-wide overflow; its photograph renders at 345 px rather than 4032 px. The prior overflow was a regression caught and corrected during the loop.
- Article prose and equations still match the session's starting article after excluding presentation-only Liquid includes. Measurement dates added to captions came from the saved plot labels.
- The maintained `scripts/serve_preview.py` serves the actual build on localhost with `Cache-Control: no-store` and ignores conditional cache requests. This replaces reliance on an ad hoc preview overlay for verification.

## Cycle 3 — keyboard access, themes, and regression protection

| Priority | Remaining weakness                                                                                                | Evidence / implication                                                                                              | Action                                                                                                                                                                                                                       |
| -------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1        | The damping response had no maintained automatic mathematical check.                                              | A future equation edit or minification regression could draw a plausible but incorrect curve.                       | Add a dependency-free Node check of initial conditions, ODE residuals, undamped response, monotone non-oscillatory decay, and continuity around critical damping; run it against the minified asset in both build workflows. |
| 2        | Runtime asset references were under-checked before this session.                                                  | A page could pass despite missing local JavaScript or responsive variants.                                          | The expanded structural checker from Cycle 1 now runs on the actual build; verify the final minified damping asset as well.                                                                                                  |
| 3        | Mobile menu, section jumps, zoom/reset, and theme transitions still need interactive review after shared changes. | Geometry checks alone do not establish working controls.                                                            | Exercise these with the actual built pages and record outcomes rather than assuming them.                                                                                                                                    |
| 4        | The public site and previous preview remain separate from the new verified output.                                | Reviewing an old shell can hide newer integration defects.                                                          | Keep a clearly identified, no-cache localhost preview of the production build; document commands and avoid deploying.                                                                                                        |
| 5        | The biggest credibility gaps still require new project evidence.                                                  | Reformatting cannot establish measured print quality, an isolated intervention, or undocumented team contributions. | Keep these in Content Opportunities; do not manufacture public claims or rewrite the author's article.                                                                                                                       |

## Cycle 4 — first-screen usefulness and image stability

| Priority | Finding                                                                                              | Evidence / consequence                                                                                                                        | Action                                                                                                                                                                                                                      |
| -------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1        | Projects resources compete with the work above the first card.                                       | The 390 px screenshot shows three explanatory blocks before the Engineering heading; Artorius's title is near the bottom of the first screen. | Replace those blocks with a compact resource nav, retaining all three destinations and moving the explanatory PDF/notebook sentence below the cards. Keep a descriptive download accessible name.                           |
| 2        | Images have no reliable intrinsic aspect-ratio hints after invalid dimension attributes are removed. | Without numeric width/height, the browser cannot reserve their correct ratio before loading.                                                  | Generate dimensions from the actual source images with Pillow, use them in the existing figure include, and run generation as part of the existing asset-build command. Explicit supplied dimensions still take precedence. |
| 3        | The local preview's regenerated assembly must be exercised, not only checksum-checked.               | The first status read timed out while the browser parsed the model.                                                                           | A later read confirmed “Assembly loaded”; the mobile canvas rendered the current printer, and zoom/reset controls responded. Record the transient parsing delay rather than claiming instantaneous loading.                 |
| 4        | Source tests do not establish behavior of minified production JavaScript.                            | Jekyll runs Terser on the asset.                                                                                                              | Run the damping check against both source and generated scripts.                                                                                                                                                            |
| 5        | Repeated aesthetic edits now offer less value than missing engineering evidence.                     | The working pages have clear statuses and preserved explanations; new validation data is outside the provided material.                       | Finish verification and keep further evidence work in the backlog instead of producing cosmetic churn.                                                                                                                      |

## Cycle 5 — final keyboard defect

The final browser inspection found that the old third-party back-to-top control is a bare `<div>` containing an SVG, without an accessible name or keyboard operation. This is a concrete defect in the existing component, newly relevant to the long article.

Replaced its initialization with a small local native-button implementation. The button has an accessible name, a 44 px touch target, ordinary browser Enter/Space behavior, and is hidden outside the useful scroll range. It respects reduced-motion preferences and returns focus to the main content. The existing skip-link target now also has `tabindex="-1"` so it can receive focus explicitly. The article body is unchanged.

## Final verification and assessment

- **Actual production build:** passed after all changes (`tmp/jekyll-final.log`, final run 2.905 seconds with responsive images cached). This is fresh Jekyll output, not the earlier overlay. The asset preparation work in this session regenerated the model and image metadata; the existing portfolio PDF was checked but not rewritten.
- **Structural checker:** passed on all 12 pages, including local links/anchors, local scripts and responsive variants, image descriptions/dimensions, metadata presence, current model checksums/geometry, and the existing linked two-page PDF.
- **Responsive matrix:** 30 checks across ten page types at 390, 768, and 1280 px passed after the layout fixes: one h1 per page, no page-wide overflow, and no failed images among those already loaded. This does not claim every lazy image was forced to load in each matrix visit.
- **Browser interactions:** section navigation lands below the fixed header; the mobile menu expands and navigates to Projects; the regenerated CAD assembly loads and zoom/reset respond. The first CAD status read exceeded the inspector's three-second deadline during parsing; a subsequent read and screenshot confirmed success.
- **Damping:** source and minified-production mathematical checks pass. Browser keyboard input reaches critical damping at ζ = 1 and overdamping at ζ = 1.25, with “No oscillation” displayed. Light/dark screenshots show a teal curve and readable labels; dark axes are white. The slider was restored to 0.12.
- **Keyboard return navigation:** the replacement is a native `BUTTON`, named “Back to top,” measuring 44 × 44 px. Enter and Space both returned to scroll position 0 with focus on `main-content`. Theme setting was restored to its starting value, `system`; the viewport override was reset.
- **Content integrity:** author's prose and equations match the starting article after excluding figure-include presentation markup. Captions, layout/front matter, and navigation changed; engineering results and project statuses did not.
- **Build wiring:** both workflows run the damping check against the generated asset. Image-dimension generation is integrated into the existing portfolio asset builder; it records 34 images and adds no new package dependency. Formatting and patch-whitespace checks pass.

The site now exposes the strongest work sooner on mobile, makes the long article easier to navigate, and has a verified current assembly rather than an older display export. It is more dependable and easier to inspect, without a change in the underlying engineering claims.

Stopped after five substantive cycles because the remaining highest-value improvements require new engineering evidence or larger, less certain changes. No numerical aesthetic rating, Lighthouse score, measured layout-shift improvement, full screen-reader audit, physical-device test, exhaustive external-link check, or CI run is claimed. External video/CDN availability and the initial CAD parsing delay remain limitations. Nothing was committed, pushed, or deployed.

### Reproduce the checks

With the repository's Ruby/Bundler environment and Python requirements available:

```powershell
$env:JEKYLL_ENV = 'production'
python scripts/build_image_metadata.py
python scripts/build_browser_model.py
bundle exec jekyll build --destination tmp/verified-site
python scripts/check_portfolio.py tmp/verified-site
node scripts/check_damping.cjs
node scripts/check_damping.cjs tmp/verified-site/assets/js/damping-demo.js
python scripts/serve_preview.py tmp/verified-site --port 8767
```

The normal CI asset step remains `python scripts/build_portfolio.py`, which generates the PDF, share cards, model preview, and image metadata before Jekyll. On this Windows checkout the portable Ruby/MSYS2 tools live under ignored `tmp/runtime/`; their paths must be activated when running Bundler locally. The preserved local native-extension options are in ignored `.bundle/config`. Official MSYS2 setup information: [Using MSYS2 in CI](https://www.msys2.org/docs/ci/).

## Follow-up: notebook navigation tab

Added Engineering notebook to the main navigation between Research and Resume, including active navigation on individual notebook entries. The menu now collapses below 768 px so the extra tab has room on smaller screens. The notebook retains its existing URL and article list.

Verified the production build and 12-page structural check, active navigation on the index and article, and layouts at 390, 576, 768, and 1024 px. No page-wide overflow; navbar height remains 61 px. The new link is available through the expanded mobile menu.

## Follow-up: damping behavior presets

Added a native dropdown for underdamped (ζ = 0.12), critically damped (ζ = 1), overdamped (ζ = 1.25), and no damping (ζ = 0). These retain the existing slider range; the underdamped preset shows several decaying oscillations, and the overdamped preset uses the upper end of that range. The slider remains available and keeps the dropdown synchronized with its current regime. No damping is now explicitly labeled rather than grouped under underdamped.

Verified all four dropdown selections, their ratios/classifications/frequency labels, synchronization after moving the slider to 0.75, and a mobile layout without overflow. Production build and analytical model checks pass.

## Follow-up: classification disclosure

Moved the damping choices into the classification descriptor below the graph. Clicking the current value opens the choices immediately underneath it, ordered by increasing damping coefficient: No damping (0), Underdamped (0.12), Critically damped (1), Overdamped (1.25). The separate selector above the plot is removed. Choosing a preset closes the disclosure and restores focus to its summary; Escape and outside clicks also close it. Slider synchronization is retained.

Verified all four presets, option ordering, keyboard opening/Escape, closing after selection, and mobile rendering without horizontal overflow. Production build, structural checks, and analytical damping checks pass.

Removed the classification descriptor's dotted underline at the author's request. The disclosure arrow and dropdown behavior are unchanged; production rebuild and CSS formatting checks pass.

## Content opportunities

These require new material from the author, not invented website content:

- Matched print specimens with documented settings, dimensional measurements, repeat counts, and surface photographs.
- A dated mechanical-change log and raw accelerometer recordings tying each sweep to a specific configuration.
- Fusion modal-analysis outputs with constraints, joints, masses, and mode shapes.
- Photographs identifying the operational printer's revisions and belt routing.
- A permitted before/after example of the personal Shape Computation Lab contribution, or documented completion of a pending fabrication stage in another project.
