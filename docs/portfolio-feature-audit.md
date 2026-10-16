# Portfolio presentation audit

Reviewed for recruiters scanning for capability, evidence, role, status, and contact details, and community visitors seeking build information. The optional-feature inventory below records the original audit; the authorized changes are recorded next.

## Decluttering implemented

- Removed the single-report search, scroll progress bar, homepage workbench cards, and duplicated homepage research preview.
- Replaced the automatic 404 redirect with a stable explanation and Home/Projects links.
- Made each project card a single case-study destination, including its thumbnail area, with a separate GitHub link where relevant. Keyboard users encounter one case-study link per card.
- Replaced the oversized homepage social icons with labeled Email, LinkedIn, and GitHub links.
- Limited the back-to-top control to the long Artorius and Phone Mount case studies.
- Simplified the assembly viewer to orbit, pan, zoom, reset, and download. Removed the export's hundreds of individual mesh controls.
- Removed duplicate occurrences of Artorius's early/final CAD views, retaining both in the comparison. Removed the repeated phone prototype photograph, retaining it in the hero and pairing fabrication text with the slicer image. Every unique image remains available.
- Shortened repeated contact panels to a heading and the two contact actions.
- The experimental homepage retains its two-project curation but removes duplicate case-study links and the manually repeated client-metrics strip. Client achievements remain in the resume.

## Further suggestions

- Combine overlapping introductory, highlight, and outcome copy on the two longest case studies after deciding which level of technical detail to prioritize.
- Group long resume skill lists by demonstrated capability and move less relevant details lower on the page.
- Replace sparse unfinished-project stage headings with one clear current-status and next-steps section when their documentation is revised.
- Give Artorius a strong photograph of the physical printer alongside its video, while continuing to label CAD renders accurately.
- Add repeatable test evidence when available: print settings, measured quality, alignment checks, and limitations. Do not promote exploratory motion settings into validated print speeds.
- Develop a permission-cleared client case study showing the brief, personal contribution, constraints, and deliverable; do not invent client details.

## PDF automation

`portfolio-preview.yml` runs `python scripts/build_portfolio.py` before Jekyll on pushes to either portfolio branch and on manual workflow runs. The script includes all projects, including unfinished work, using edited `pdf_summary` front matter rather than concatenating web pages. The two-page PDF has linked contents, project bookmarks, and compact print spacing. The built website artifact includes the generated PDF.

The deployment workflow also contains this generation step, but these preview changes do not alter main or the live site. Local source editing or running Jekyll alone does not regenerate the PDF; run the Python script first.

## Decluttering validation and limitation

Preview run `38983179006` (`14c87a7`) and experimental run `38983215279` (`03c706a`) passed. Both downloaded artifacts passed the ten-page checker with the complete linked two-page PDF. Additional rendered-HTML checks confirmed one case-study destination per card, the stable 404, removal of the research search/progress bar/homepage duplicates, and conditional back-to-top loading. Source checks confirmed every unique project image remains referenced and project-card descriptions have no em dashes. The revised CAD JavaScript passed Node's syntax check.

Fresh visual and interaction verification of this cleanup could not be completed. The supported browser initially showed `ERR_CONNECTION_REFUSED`. After restarting the authorized preview server, navigation was blocked with `Blocked browser navigation by Browser Use URL policy: data:text/html;charset=utf-8,...`, referring to the browser's generated connection-error page. The local server separately returned HTTP 200. The user's default and exact localhost Always allow settings are already enabled. No alternate browser or raw browser protocol was used. Earlier screenshots and review scores below apply to the preceding layout revision, not this cleanup; no new visual UX score is claimed.

## Retain as core presentation

| Feature | Purpose |
| --- | --- |
| About, Projects, Research, Resume navigation | Clear entry points for different reader intentions. |
| Project roles, outcomes, status, limitations | Distinguish demonstrated work from plans and team contributions. |
| Actual-printer video and assembled phone-mount photograph | Evidence of physical work; CAD renders retain explicit labels. |
| CAD comparison and contextual image captions | Explain decisions and iteration without claiming unsupported gains. |
| Schematic and detail-image zoom | Makes engineering information inspectable at useful resolution. |
| Resume, complete portfolio PDF, linked contents | Support fast review, offline sharing, and printing. |
| Email and LinkedIn contact panels | Allow a reader to act from any case study. |
| GitHub and source-model downloads | Useful technical evidence and resources for community members. |
| Skill-to-project links | Let recruiters check evidence rather than rely on a tool list. |
| Mobile navigation, theme control, focus styles, skip link | Readability and accessible navigation across contexts. |
| Page descriptions, share images, and local-link validation | Help discovery/sharing and prevent broken presentation paths. |

## Optional or redundant

| Feature | Assessment |
| --- | --- |
| Research-report search field | Unnecessary for a single published report. A direct report link is clearer until the collection grows. |
| Scroll progress bar | Decorative feedback, with little hiring or technical-evidence value. |
| Automatic three-second 404 redirect | Unnecessary and can disorient visitors; a stable error page with Home and Projects links would be clearer. |
| Three project-card links to the same case study | Thumbnail, title, and “Explore” link duplicate the same action and add keyboard stops. One combined destination would suffice. |
| Large homepage social-icon row | Repeats resume, email, and profile destinations already available through primary actions. Compact labeled links would suffice. |
| “On my workbench” homepage cards | Useful for recurring followers, but duplicate the unfinished projects' status and next steps. Optional for a recruiter-focused homepage. |
| Selected Research homepage preview | Useful discovery, but duplicates the Research navigation and page. Optional if reducing homepage length. |
| Back-to-top floating button | Helpful on long case studies, but optional on short pages. It could be limited to long content. |
| Artorius individual-part controls | Useful to some engineering visitors, but the 931-mesh export adds considerable complexity. Orbit/reset/download provide most review value. Keep advanced controls optional. |
| Repeated Artorius CAD views | Early/revised images appear in explanatory sections and the comparison; the revised view also reappears at the end. Context can justify repetition, but the repeated final view adds little new evidence. All images have been retained as requested. |
| Repeated phone-mount prototype photo | Appears in the hero and prototype section. It adds context but is not essential twice. Retained as requested. |
| Generic repeated contact-panel introduction | Email and LinkedIn are useful; identical explanatory sentences on every project could be shortened. |
| Experimental client-evidence strip | Useful supporting evidence, but manually duplicates historical CV figures. Optional maintenance burden. |
| Experimental two-build homepage section | Stronger curation, but repeats projects available in the full index. Useful if this version becomes the preferred landing page, not required for functionality. |

Dormant theme features such as the printer text animation, charts, maps, math rendering, newsletter, and global search are not active presentation features. They are not counted as visible clutter. Unused source assets can be cleaned up separately.

## Requested revision

- Removed the theme button's vertical translation and aligned it with desktop navigation.
- Centered button labels through flex alignment and equalized primary/outline borders.
- Removed added thumbnail padding and pale framing; preserved the original image contents on a theme-matching card surface.
- Paired Artorius ideation, toolhead, frame, and final-outcome text with their corresponding images. Paired the phone-mount sketch with ideation and the chess render with design text. Enlarged the purifier schematic and paired the Shape Machine animation with its context and links. Kept the phone prototype gallery proportional to its mixed landscape/portrait images. The phone hero places its summary beside the portrait photo on desktop and stacks on mobile.
- Removed decorative dot separators and loading ellipses while retaining normal sentence punctuation, decimal numbers, and actual list bullets.
- Replaced the selected-project PDF with a two-page document containing all five project summaries, including unfinished work. The contents table and outline link to exact headings. Paragraph spacing is optimized for print; the website retains breathing room.

## Verification

All five project pages were inspected as complete desktop pages and at a 390 x 844 mobile viewport. The project index was checked in light and dark modes; the monochrome Shape Machine logo retains a white backing for legibility. All image includes were checked against the pre-revision source and retained. Revised text/image pairs stack on mobile without horizontal overflow.

The theme button's vertical center measured 30px against 29.992px for the navigation links. Artorius contact labels measured 0px horizontal and -0.1px vertical offset from their button centers. The phone demonstration expands successfully beside the summary. The final phone hero and index were inspected in light mode as well as dark mode.

The first two rendered builds passed the ten-page link, anchor, image, metadata, share-card, and PDF checker. The PDF was visually inspected on both pages and has five project outline entries. Its internal destinations use distinct heading positions, including projects sharing a page. The build checker now requires all project titles in the contents and outline and validates heading destinations. Source checks preserve project-card descriptions without em dashes and retain actual list bullets while removing decorative dot separators.

Screenshots are stored locally under `output/ux-review/`. Browser viewport review is not a physical-device or full assistive-technology audit. External video and CDN availability remain dependencies.
