# Notebook and presentation refinement

This revision is shared by the preview and experimental branches. Main and the live deployment remain unchanged.

- The homepage has two prominent actions: View Projects and Contact Me. Resume and complete-portfolio downloads are secondary text links.
- Artorius and Phone Mount use their at-a-glance panels for the short summary; duplicate highlight lists, opening summaries, and closing outcome copy are consolidated. Shape Machine's contribution descriptions are shortened without expanding the claimed role.
- Air Purifier and Chess Board combine their unfinished prototype/final-product sections into Current status and next steps. The resume's chess-fabrication evidence link targets the new heading.
- An Engineering notebook collection, index, entry layout, per-project note lists, and authoring template are ready. No entries are fabricated. The index is linked quietly from Projects; empty per-project sections are hidden.
- The browser uses a generated display export of Artorius, while the original assembly remains the full download. Generation preserves mesh identities, material groups, and assembly transforms, welds coincident vertices at 0.0001 mm precision, and reduces display triangles with a bounds check and adaptive fallback. Fine details are explicitly described as simplified.
- Both portfolio workflows already run `scripts/build_portfolio.py`; that entry point now generates the display model as well as the PDF and share cards. Generated model files are ignored by Git and included in the compiled site.

Physical-printer photographs, new repeatable test data, and concrete contribution comparisons are deferred at Ethan's request. See `portfolio-content-to-gather.md` for proposed source files and `engineering-notebook.md` for the publishing workflow.

Validation includes local source/image preservation checks, Python/JavaScript syntax checks, the rendered site checker, and supported-browser testing where available. The model checker verifies source and preview hashes, finite vertices, valid triangle indices, all generated meshes, and a preview size below 30% of the full export. Earlier three-cycle UX scores are historical; no new score is assigned to this refinement.
