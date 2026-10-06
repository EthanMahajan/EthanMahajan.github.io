# Agent guidelines

This repository is Ethan Mahajan's Jekyll engineering portfolio, based on al-folio. See `README.md` for the content structure and development commands.

- Preserve personal content, project media, publication data, resume files, and the original theme license.
- Keep `url: https://ethanmahajan.github.io` and an empty `baseurl` together in `_config.yml`.
- Format changes with `npm ci` and `npx prettier . --write`.
- Validate with `docker compose up --build` or `bundle exec jekyll build`; check navigation, images, resume links, and dark mode when changing rendered pages.
- Keep build outputs and installed dependencies out of commits.
- Follow `.github/GIT_WORKFLOW.md` for commit conventions.
