# Portfolio experiment

Branch: `codex/portfolio-experimental`, created from the completed preview at `329967f`.

## Differences from the preview

- A larger, direct homepage headline: “I turn CAD into working hardware.” The name remains above it and Georgia Tech context stays directly below it. The shorter introduction retains the existing opportunity statement.
- A client-work evidence strip links to the resume's experience section. Its 20+ contracts, 30 tablet holders, and 4.6/5 rating come from the Fiverr entry in `_data/cv.yml`, dated February 2024 through October 2025. These are existing documented achievements; no client identities, results, or current availability are added. The small presentation data file `_data/home_evidence.yml` identifies that source and should be updated alongside it.
- Two curated build spotlights use the existing `portfolio: true` flag and project front matter. Artorius uses footage of the working printer; the phone mount uses the assembled-prototype photograph. Each shows its documented outcome and current status, with a direct case-study link. Desktop places the builds side by side; mobile stacks them.

The project index, case studies, resume, PDF generator, forest-green colors, and preview UX fixes are inherited. No filtering was added for a five-project collection. The preview remains independently reviewable. This branch does not merge or deploy to main.

## Validation

Build and rendered checks will be recorded after implementation. The preview's three-cycle UX review remains in `docs/portfolio-preview.md`; experimental validation is separate and does not add preview review cycles.
