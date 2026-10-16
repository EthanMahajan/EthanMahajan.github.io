# Portfolio experiment

Branch: `codex/portfolio-experimental`, created from the completed preview at `329967f`.

## Differences from the preview

- A larger, direct homepage headline: “I turn CAD into working hardware.” The name remains above it and Georgia Tech context stays directly below it. The shorter introduction retains the existing opportunity statement.
- A client-work evidence strip links to the resume's experience section. Its 20+ contracts, 30 tablet holders, and 4.6/5 rating come from the Fiverr entry in `_data/cv.yml`, dated February 2024 through October 2025. These are existing documented achievements; no client identities, results, or current availability are added. The small presentation data file `_data/home_evidence.yml` identifies that source and should be updated alongside it.
- Two curated build spotlights use the existing `portfolio: true` flag and project front matter. Artorius uses footage of the working printer; the phone mount uses the assembled-prototype photograph. Each shows its documented outcome and current status, with a direct case-study link. Desktop places the builds side by side; mobile stacks them.

The project index, case studies, resume, PDF generator, forest-green colors, and preview UX fixes are inherited. No filtering was added for a five-project collection. The preview remains independently reviewable. This branch does not merge or deploy to main.

## Validation

The first experimental GitHub Actions build (`38969940101`, commit `dc80d3a`) passed. Its artifact also passed the ten-page local link, anchor, image-description, metadata, share-card, and three-page PDF checker. A source check confirmed the three client metrics match the existing CV and all project-card descriptions remain free of em dashes.

Inspected desktop and 390 x 844 mobile rendering in the supported browser. No horizontal overflow was found (390px viewport, body, and document width). The initial layout delayed the project media behind the evidence strip, so the final order puts the builds first and reduces the desktop portrait to 22% of the content width. The historical evidence strip follows the builds, with its date aligned to the section title. Final rendered checks are recorded below.

The preview's three-cycle UX review remains in `docs/portfolio-preview.md`; experimental validation is separate and does not add preview review cycles.

Final implementation validation: GitHub Actions run `38970178389` for `3d3b633` passed, and its downloaded artifact passed the local ten-page checker. Inspected the revised desktop and 390 x 844 mobile homepage in light and dark themes, confirming stacked builds on mobile and no horizontal overflow. Activated the evidence link and verified it opens the resume's documented freelance experience. Screenshots are retained locally in `output/ux-review/`, including `experimental-desktop.png`. The viewport override was reset after testing.

Limitations: the two spotlights add homepage length; the evidence strip repeats manually maintained historical CV figures; and YouTube/CDN loading still depends on external services. Browser viewport testing does not replace physical-device, screen-reader, or performance testing. No additional numerical UX score is claimed for this experiment.
