# Portfolio preview

Branch: `codex/portfolio-preview`. The live site remains on `main`.

## What changed

- Artorius starts with its working-printer video. The phone mount starts with its assembled-prototype photograph and an expandable demonstration.
- Artorius includes a responsive, side-by-side comparison of early and revised CAD assemblies. Captions explain the changes and the remaining limitations.
- Project cards use outcome descriptions with colons, consistent image frames, status labels, and aligned links.
- Resume skill groups link to relevant project sections with a sentence explaining the demonstrated work. These links do not imply that every tool in a group was used in every project.
- A forest-green palette, consistent spacing, readable captions, dark-mode text colors, focus indicators, and a skip link carry through the site. Dark-mode links use a lighter green for readability; primary buttons retain a deep forest-green fill in both themes.
- Every project ends with an email and LinkedIn contact panel. Email subjects include the project title.
- A generated PDF is available from the homepage and Projects page. Branded share images are generated for the homepage and every project.

## Generate the portfolio

```sh
python -m pip install -r requirements-portfolio.txt
python scripts/build_portfolio.py
bundle exec jekyll build
python scripts/check_portfolio.py
```

The generator reads `_config.yml`, `_data/socials.yml`, and `_projects/*.md`. Projects with `portfolio: true` appear in the PDF, ordered by `importance`. Each selected project uses its existing `description`, `hero`, `project_summary`, and `portfolio_highlights`. The website renders those same highlights.

Edit project content once, then rebuild. No separately maintained PDF copy or website scraping is required. To include another project, give it a hero image and concise portfolio highlights, then set `portfolio: true`. The generator fails clearly if a page's text would overflow.

Generated PDF and share-image files are excluded from Git and created before Jekyll builds on both preview and production workflows. The preview workflow uploads the complete `_site` as `portfolio-preview-site`; it does not deploy the production website.

## Verification

The initial GitHub Actions build passed. Its rendered output passed the portfolio checker across ten pages, including local links, fragment targets, image descriptions, unique IDs, metadata, 1200 x 630 share images, and PDF text and links. All three PDF pages were rendered and inspected locally.

Browser access succeeded in the fresh session on October 16, 2026. The previous permission blocker no longer reproduces.

### Visual review: cycle 1

Score: **7.8/10** (clarity 1.7, navigation 1.4, hierarchy 1.5, responsive interaction 1.3, evidence 1.9). Inspected desktop light/dark homepage, desktop project grid and full Artorius page, and 390 x 844 mobile homepage, Artorius viewer, phone mount, and resume. The mobile menu and prototype expansion worked; the Artorius viewer loaded 931 mesh parts.

Observed and fixed: nearly invisible category headings in light mode; full-width mobile portrait delaying the introduction; mobile resume contents overlapping its title and contact card; fixed footer covering mobile content; thin body text; inconsistent resume heading sizing; internal project links using an external-link arrow. Clarified that Artorius's toolhead, belt-routing, and intermediate assembly stills are CAD renders. Added anchor clearance below the fixed header.

One YouTube embed failed after changing theme, while subsequent page navigation loaded embeds normally. The direct YouTube links remain available. Playback is an external dependency and needs a separate interaction check in the next cycle.

### Visual review: cycle 2

Score: **9.0/10** (clarity 1.8, navigation 1.8, hierarchy 1.8, responsive interaction 1.7, evidence 1.9). Reviewed the rebuilt output from commit `97c75d7` on desktop and 390 x 844 mobile, including dark resume, mobile homepage, and stacked Artorius CAD comparison. The resume overlap and fixed-footer obstruction are resolved. The printer video played successfully with advancing time and captions. All three forest-green PDF pages were rendered and inspected without clipping or overlap. The rebuilt ten-page link/metadata/PDF checker passed locally.

The research page still had a low-contrast year heading and undersized PDF button. Restored heading contrast and enlarged the report button to a 44px touch target; gave the report filter an accessible name. Retained the direct video fallback because third-party player loading can fail transiently. The homepage is still fairly text-heavy and Artorius is a long case study; these remain honest presentation limitations rather than reasons to claim a score above 9.5.

A further contrast check in this cycle found that the base theme overrode project-card descriptions with gray even in dark mode. An explicit card-body selector now uses the portfolio text color in both themes.

### Visual review: cycle 3 (final)

Score: **9.3/10** (clarity 1.8, navigation 1.8, hierarchy 1.9, responsive interaction 1.9, evidence 1.9). Reviewed final rendered output from `86a37db` at desktop and 390 x 844 mobile in light/dark themes. Verified readable dark card descriptions (computed RGB 230, 236, 239), research year contrast, the enlarged report button, the filter's accessible name, mobile resume without overlap, compact mobile portrait, navigation, and keyboard skip-link activation. The prior cycles exercised the expandable phone demonstration, actual printer-video playback, and on-demand CAD viewer. No further source changes were needed in this cycle. The build and ten-page structural checker passed; all three PDF pages were visually inspected during cycle 2.

Stopped at the requested maximum of three cycles, without claiming a score above 9.5. Remaining limitations: the homepage introduction is text-heavy, Artorius requires substantial scrolling, project cards repeat links to the same destination, and external video/CDN availability can affect media and viewer loading. Mobile review used a browser viewport, not a physical touch device. This was a visual and interaction review, not a full screen-reader or performance audit. Preview screenshots are retained locally under `output/ux-review/` (ignored by Git).

The experimental branch starts only after this preview is complete. It will be separately reviewable and will retain the forest-green direction and the distinction between CAD renders and working hardware.

## UX review rubric

Each review cycle scores five dimensions out of two: clarity and relevance; navigation and contact; visual hierarchy and spacing; responsive and accessible interaction; presentation of project evidence. Record specific issues and changes, review no more than three cycles, and stop early only if the score is solidly above 9.5. No visual score is assigned without browser inspection.
