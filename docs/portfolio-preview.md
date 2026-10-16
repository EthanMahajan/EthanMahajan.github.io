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

Browser access to the local preview was denied. Desktop/mobile screenshots, interaction testing, and a final visual UX score are pending permission. Static verification is not a substitute for a rendered-page UX review.

## UX review rubric

Each review cycle scores five dimensions out of two: clarity and relevance; navigation and contact; visual hierarchy and spacing; responsive and accessible interaction; presentation of project evidence. Record specific issues and changes, review no more than three cycles, and stop early only if the score is solidly above 9.5. No visual score is assigned without browser inspection.
