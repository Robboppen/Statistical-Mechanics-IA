# AGENTS.md — Statistical Mechanics IA

## What this repo is

Academic writing repository for the Statistical Mechanics course (IFA, Universidad de Valparaíso). No application code, no build pipeline, no tests.

## Key files

- **`Readme.md`** — Main deliverable document (Boltzmann Machines, physics ↔ ML bridge). Not a typical README; it *is* the product.
- **`resumen_papers.tex`** — Structured summaries of 11 papers in LaTeX. Compile with `pdflatex resumen_papers.tex`.
- PDFs in root are reference papers (not code/config).

## Language

All content is in **Spanish** (academic register). Write in Spanish when editing docs.

## LaTeX

- Packages: `amsmath, amssymb, hyperref, geometry, booktabs`
- No Makefile or build script exists. Compile manually: `pdflatex resumen_papers.tex`
- The `.pdf` in root is the compiled output of this `.tex` file.

## Conventions

- Markdown math uses `$$...$$` blocks and inline `$...$`.
- Commit messages in this repo are minimal (often just `.`). Match the style.
- No linting, formatting, or typecheck tools configured.
