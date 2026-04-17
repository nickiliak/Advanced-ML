# Advanced Machine Learning (02460)

DTU Course: Advanced Machine Learning

## Project Structure

```
Advanced-ML/
├── main.py
├── pyproject.toml
├── README.md
├── data/
├── Projects/
│   └── Deep-Generative-Modeling/   # Submodule
├── Week1/   # Deep Latent Variable Models (VAE)
├── Week2/   # Normalizing Flows
├── Week3/   # Diffusion Models (DDPM)
├── Week5/   # Manifold Learning & Latent Geometry
├── Week6/
├── Week7/
├── Week9/
└── Week10/  # Graph Neural Networks (GNN)
```

## Weekly Topics

| Week | Topic |
|------|-------|
| 1 | Deep Latent Variable Models — VAE implementation |
| 2 | Normalizing Flows — Masked Coupling Layers |
| 3 | Diffusion Models — DDPM implementation |
| 5 | Manifold Learning & Latent Geometry |
| 10 | Graph Neural Networks — Graph Classification |

## Setup

1. Initialize submodules:
```bash
git submodule update --init --recursive
```

2. Install dependencies with `uv`:
```bash
uv sync
```

3. Run the project:
```bash
uv run python main.py
```

## Claude Code Skills

This repository includes project-local Claude Code skills under `.claude/commands/`:

- `week-answer-fill` — Fill an answer into the selected week README for a specific question.
- `answer-check` — Check whether a user's answer is correct for a selected week question (no spoilers).
- `week-readme-setup` — Create or update a WeekN README with questions from the exercise PDF.
- `week-commands-generator` — Generate and update commands for a specific week.
- `teach` — Guided learning through hints without revealing answers.

### Week Folder Convention

```text
WeekN/
├── <exercise>.pdf
├── commands.md
└── answers/
    └── README.md
```
