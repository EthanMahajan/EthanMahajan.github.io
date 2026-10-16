# Portfolio experiment

Branch: `codex/portfolio-experimental`, created from the completed preview at `329967f`.

## Differences from the preview

- A larger, direct homepage headline: “I turn CAD into working hardware.” The name remains above it and Georgia Tech context stays directly below it. The shorter introduction retains the existing opportunity statement.
- Client-work achievements remain in the resume. The initial experiment included a historical evidence strip, but the authorized decluttering pass removed that duplicate homepage presentation and its manual-maintenance burden.
- Two curated build spotlights use the existing `portfolio: true` flag and project front matter. Artorius uses footage of the working printer; the phone mount uses the assembled-prototype photograph. Each shows its documented outcome and current status, with a direct case-study link. Desktop places the builds side by side; mobile stacks them.

The project index, case studies, resume, PDF generator, forest-green colors, and preview UX fixes are inherited. No filtering was added for a five-project collection. The preview remains independently reviewable. This branch does not merge or deploy to main.

## Validation

The first experimental GitHub Actions build (`38969940101`, commit `dc80d3a`) passed. Its artifact also passed the ten-page local link, anchor, image-description, metadata, share-card, and three-page PDF checker. A source check confirmed the three client metrics match the existing CV and all project-card descriptions remain free of em dashes.

Inspected desktop and 390 x 844 mobile rendering in the supported browser. No horizontal overflow was found (390px viewport, body, and document width). The initial layout delayed the project media behind the evidence strip, so the final order puts the builds first and reduces the desktop portrait to 22% of the content width. The historical evidence strip follows the builds, with its date aligned to the section title. Final rendered checks are recorded below.

The preview's three-cycle UX review remains in `docs/portfolio-preview.md`; experimental validation is separate and does not add preview review cycles.

Final implementation validation: GitHub Actions run `38970178389` for `3d3b633` passed, and its downloaded artifact passed the local ten-page checker. Inspected the revised desktop and 390 x 844 mobile homepage in light and dark themes, confirming stacked builds on mobile and no horizontal overflow. Activated the evidence link and verified it opens the resume's documented freelance experience. Screenshots are retained locally in `output/ux-review/`, including `experimental-desktop.png`. The viewport override was reset after testing.

Limitations: the two spotlights add homepage length, and YouTube/CDN loading still depends on external services. Browser viewport testing does not replace physical-device, screen-reader, or performance testing. No additional numerical UX score is claimed for this experiment. The evidence-strip observations above document the initial version; that strip has since been removed.

## Shared presentation refinement

The subsequent preview refinement is carried into this branch: aligned theme control, centered button labels, original thumbnails without added pale framing, contextual project-image layouts, and the complete two-page PDF with linked contents for all five projects. The two curated homepage builds remain independent of PDF inclusion. Decorative dot separators were also removed from the experimental subtitle and client-work date. See `docs/portfolio-feature-audit.md` for optional features and the review evidence.

The shared decluttering pass removes duplicate navigation, homepage workbench/research previews, decorative progress feedback, repeated image placements, and individual CAD mesh controls. Featured builds now have one case-study link each. The stronger headline and two-build curation remain the deliberate differences from preview.

The rendered cleanup build (`38983215279`, `03c706a`) passed CI and the downloaded artifact passed the ten-page/PDF checker plus structural checks for the removed duplicates. Fresh browser review was blocked by the browser's URL policy on its generated connection-error page, despite the restarted preview server returning HTTP 200. See the feature audit for the exact limitation; no fresh visual score or interaction validation is claimed.
