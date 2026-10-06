# Ethan Mahajan — Engineering Portfolio

Personal portfolio for Ethan Mahajan, a mechanical engineering student at Georgia Tech.

Website: https://ethanmahajan.github.io

## Editing the site

- `_pages/`: about, projects, publications, and resume pages.
- `_projects/`: engineering project descriptions.
- `_data/cv.yml`: resume data; `_data/socials.yml`: contact links.
- `_bibliography/papers.bib`: publications.
- `assets/`: project images, 3D model, and downloadable PDFs.
- `_config.yml`: site settings; `_sass/`, `_layouts/`, and `_includes/`: theme styling and templates.

## Local development

```bash
docker compose up --build
```

Open http://localhost:8080. Alternatively, with Ruby and the dependencies installed:

```bash
bundle install
bundle exec jekyll serve
```

Format files with `npm ci` and `npx prettier . --write`.

## Deployment and resume generation

Pull requests run the Jekyll build through `.github/workflows/deploy.yml`. Merging into `main` deploys the built site to `gh-pages`.

The RenderCV workflow regenerates the resume PDF when `_data/cv.yml` or its RenderCV settings change. The resume page and social links use `assets/rendercv/rendercv_output/Ethan_Mahajan_CV.pdf`.

## Theme attribution

Built with Jekyll and the [al-folio theme](https://github.com/alshedivat/al-folio). The original theme's MIT license is retained in `LICENSE`.
