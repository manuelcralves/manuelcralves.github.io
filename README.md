# Portfolio

The source code of my personal site, with a home page and one page for each of my selected projects.

It is a static site built with [Astro](https://astro.build), and the built pages load no JavaScript. Each project is a Markdown file in `src/content/projects/`, checked against the schema in `src/content.config.ts`. The fonts are downloaded at build time and served with the site.

## Run it

You need Node 22.12 or newer (I use Node 24).

```bash
npm install
npm run dev
```

The dev server runs at http://localhost:4321. `npm run build` writes the site to `dist/`, and `npm run astro check` runs the type checker.
