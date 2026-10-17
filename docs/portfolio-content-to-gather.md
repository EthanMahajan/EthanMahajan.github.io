# Source files that would directly strengthen the portfolio

Photographs, repeatable measurements, and concrete contribution comparisons are deferred at Ethan's request. These are proposed files to gather or create from real work; they are not claims that the evidence currently exists. The paths below are suggestions, not broken links or public placeholders.

## 1. Physical Artorius photographs

- `assets/img/artorius/assembled-printer.jpg`: a clear three-quarter view showing the whole physical printer.
- `assets/img/artorius/toolhead-photo.jpg`: a close-up showing the actual toolhead, wiring, and motion interface.
- `assets/img/artorius/print-sample.jpg`: a clearly lit print sample associated with a recorded test, when available.
- A short caption record identifying the pictured revision, approximate capture date, and what each photograph demonstrates. Keep CAD renders labeled separately.

Use original-resolution files. Photograph visible hardware honestly, with a simple background and enough light to inspect the build.

## 2. Repeatable test evidence

- `assets/data/artorius/print-tests.csv`: one row per trial, with test ID/date, hardware revision, material, nozzle and layer settings, actual print-speed and acceleration settings, test object, elapsed time, measured result, and outcome.
- `assets/data/artorius/test-method.md`: procedure, measurement tools, conditions, repetitions, acceptance criteria, and limitations. Include failed trials and distinguish commanded motion from validated printing performance.
- Matching photographs or short clips identified by test ID. Existing exploratory motion settings alone do not establish repeatable print quality.

A comparable small test record for phone-holder play or base stability would strengthen the phone-mount case study if those refinements are pursued. Record measured observations rather than estimating improvements after the fact.

## 3. A specific Shape Machine contribution

- Permission-cleared before/after screenshots of the same content or template at comparable viewport sizes.
- A short source note with the original issue, exact personal contribution, date or revision references, and the resulting observable change. A permitted commit or diff link is useful.
- If the change affected a shared template, identify the pages it actually affected. Do not infer audience or conversion gains without data.

Suggested image location: `assets/img/shape-machine/`. Include only material permitted for public presentation.

## 4. The first engineering notebook entry

Copy `docs/notebook-entry-template.md` into `_notes/` and fill it with one actual problem and what was tried. A fabrication photo, sketch, failed part, or small measured comparison can support it. A documented failure is useful evidence even when the next revision is unfinished.

These files can be added incrementally. The website already has the notebook structure, project associations, compact project PDF, and generated browser-model pipeline.
