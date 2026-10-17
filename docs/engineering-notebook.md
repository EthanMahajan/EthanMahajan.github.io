# Engineering notebook

The notebook is a small Jekyll collection for occasional build notes. No entries or results have been invented. Its index is linked quietly from Projects; each case study automatically lists its associated published notes once they exist. The main navigation stays focused on About, Projects, Research, and Resume.

To add an entry:

1. Copy `docs/notebook-entry-template.md` to `_notes/descriptive-slug.md`.
2. Supply an actual date, specific title, one-sentence description, and project file stem (`artorius`, `phone_mount`, `air_purifier`, `laser_engraved_chess_board`, or `shape_machine`).
3. Replace the prompts with documented work. Put supporting images in `assets/img/notebook/` and use the existing `figure.liquid` include with descriptive alt text and captions.
4. Set `published: true` when ready. Drafts remain unpublished. The public address is `/notebook/descriptive-slug/`.
5. Run `python scripts/build_portfolio.py`, build Jekyll, and run `python scripts/check_portfolio.py`. Pushing either portfolio branch also runs these steps automatically.

Keep entries narrow: one problem, change, observation, and next step. Test evidence should include configuration, conditions, units, repetitions, raw data, and limitations. Contribution examples should identify the personal change and use permitted before/after material. Physical-printer photographs, new repeatable test results, and contribution comparisons are deferred until Ethan supplies them.

Notebook entries supplement the case studies; they are not automatically appended to the compact project-summary PDF. All five project summaries remain included in that PDF.
