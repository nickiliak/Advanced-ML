# Project Environment: `uv`

This project uses **`uv`** for Python environment and package management.

## When generating code
- Use `uv pip install` instead of `pip install`
- Use `uv run` instead of `python`
- Use `uv sync` to install dependencies
- Do NOT use `pip` or `python -m venv`
- Keep code and explanations simple and concise
- Avoid over-engineering solutions

---

# Exam Prep Context

This repo is the user's study lab for the **02460 final exam**. The exam is written and **paper notes are allowed** — the end goal is a dense, hand-carryable cheatsheet covering every weekly topic.

- Cheatsheet drafts live under [ExamPrep/prep/](ExamPrep/prep/) (one section per topic, formula-first, minimal prose).
- Source material for the cheatsheet: weekly lecture PDFs, `WeekN/answers/README.md`, project READMEs in [Projects/](Projects/).

## Old Exams Policy — validation set

[ExamPrep/old_exams/](ExamPrep/old_exams/) holds past papers (2024 final, 2024 mock, 2025 final). The user will sit these **timed** after studying as a held-out validation set.

**Access rules (meta-only):**
- ✅ May inspect topic coverage, question format, length, weighting, recurring patterns to guide what the cheatsheet must cover.
- ❌ Never quote or paraphrase question content into study materials, cheatsheets, or weekly answers.
- ❌ Never solve old-exam questions unless the user explicitly asks (e.g. after a timed run, for review).
- ❌ Never let old-exam phrasing leak into hints or examples — the user must see those questions cold.

If unsure whether something counts as leakage, ask before producing.

## Weekly Folder Status

| Week | Topic | Status |
|------|-------|--------|
| 1  | VAE / Deep Latent Variable Models | partial — needs polish |
| 2  | Normalizing Flows | partial — needs polish |
| 3  | Diffusion / DDPM | partial — needs polish |
| 5  | Manifold Learning & Latent Geometry | partial — needs polish |
| 6  | (metrics) | **empty — run `/week-readme-setup` first** |
| 7  | (geometry) | **empty — run `/week-readme-setup` first** |
| 9  | Graph Node Embeddings | partial — needs polish |
| 10 | GNNs — Graph Classification | partial — needs polish |
| 11 | Graph Convolutions | partial — needs polish |

[Projects/](Projects/) — three completed course projects (Deep-Generative-Modeling, VAE-Geometry, MUTAG-Gen-GNN). Treat as applied reference / worked examples when building cheatsheet sections.

## Solving Mode

The user solves exercises on their own merit. A dedicated study agent will be set up later to handle hint-vs-answer logic. **Until then**: when the user asks about an *unsolved* exercise, ask whether they want hints (`/teach` style) or a full solution before answering. `/answer-check` is always safe — it grades without spoilers.

## Slash Commands — quick reference

| Command | Purpose |
|---------|---------|
| `/week-readme-setup` | Extract exercise questions from a `WeekN/*.pdf` into `WeekN/answers/README.md`. |
| `/week-commands-generator` | Generate `WeekN/commands.md` with run instructions. |
| `/answer-check` | Grade a candidate answer; no spoilers. Auto-fires `/week-answer-fill` on `Correct`. |
| `/week-answer-fill` | Insert a confirmed answer under the matching question heading. |
| `/teach` | Hints and scaffolded problems — never the direct solution. |
| `/commit` | Stage all changes and write a Conventional Commit message. |
