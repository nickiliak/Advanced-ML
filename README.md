# Advanced Machine Learning (02460)

DTU course **02460 — Advanced Machine Learning**. This repository contains my weekly programming exercises and the larger course projects, all managed with [`uv`](https://docs.astral.sh/uv/).

## Project Structure

```
Advanced-ML/
├── README.md
├── CLAUDE.md
├── pyproject.toml
├── uv.lock
├── main.py
├── data/                                  # Shared datasets / cached files
├── Projects/                              # Larger course projects (git submodules)
│   ├── Deep-Generative-Modeling/          # Project 1 — generative modelling
│   ├── VAE-Geometry/                      # Project 2 — VAE Riemannian geometry
│   └── MUTAG-Gen-GNN/                     # Project 3 — generative GNN on MUTAG
├── Week1/   # Deep Latent Variable Models — VAE
├── Week2/   # Normalizing Flows
├── Week3/   # Diffusion Models — DDPM
├── Week5/   # Manifold Learning & Latent Geometry
├── Week6/
├── Week7/
├── Week9/   # Graphs & Node Embeddings (shallow embedding)
├── Week10/  # Graph Neural Networks — Graph Classification
├── Week11/  # Graph Convolutions
└── .claude/                               # Claude Code skills, hooks, settings
    ├── commands/
    ├── scripts/
    └── settings.json
```

## Weekly Topics

| Week | Topic | Key files |
|------|-------|-----------|
| 1  | Deep Latent Variable Models — VAE | `vae.py`, `plot_posterior.py` |
| 2  | Normalizing Flows — Masked Coupling Layers | `flow.py`, `ToyData.py` |
| 3  | Diffusion Models — DDPM | `ddpm.py`, `unet.py` |
| 5  | Manifold Learning & Latent Geometry | `evaluate_vae_curve.ipynb`, `evaluate_len_curve.ipynb` |
| 9  | Graphs & Node Embeddings — shallow embedding, link prediction | `shallow_embedding.ipynb` |
| 10 | Graph Neural Networks — Graph Classification | `gnn_graph_classification.ipynb` |
| 11 | Graph Convolutions | `graph_convolution.ipynb` |

## Projects

The `Projects/` folder holds the larger course projects as **git submodules**.

### Project 1 — Deep Generative Modeling (`Projects/Deep-Generative-Modeling/`)

Implementation work around deep generative models (see the project's own `README.md` for details).

### Project 2 — VAE Geometry (`Projects/VAE-Geometry/`)

Mini-project estimating Riemannian geometries induced by Variational Autoencoders on a subset of MNIST (3 classes, 2,048 observations).

- **Part A** — Single-decoder VAE with pull-back geodesics: piecewise-linear curves minimising image-space energy via L-BFGS.
- **Part B** — Ensemble VAE (shared encoder + K independent decoders): Monte Carlo geodesic energy and coefficient of variation (CoV) across 10 reruns to measure geodesic reliability as a function of ensemble size K.

```bash
# Part A
uv run python src/part_a_pullback/main.py train
uv run python src/part_a_pullback/main.py geodesics

# Part B — train K=3 decoders across 10 reruns
for i in $(seq 0 9); do
    uv run python src/part_b_ensemble/ensemble_train.py --num-decoders 3 --rerun-index $i
done
```

### Project 3 — MUTAG-Gen-GNN (`Projects/MUTAG-Gen-GNN/`)

Generative Graph Neural Networks on the MUTAG molecular dataset. See [Projects/MUTAG-Gen-GNN/README.md](Projects/MUTAG-Gen-GNN/README.md) for project-specific instructions; the project follows the standard `src/`, `configs/`, `models/`, `reports/`, `notebooks/` layout.

## Setup

This repo uses **`uv`** (do not use `pip` or `python -m venv` directly).

1. Initialize submodules:
   ```bash
   git submodule update --init --recursive
   ```
2. Install dependencies:
   ```bash
   uv sync
   ```
3. Run a script:
   ```bash
   uv run python main.py
   ```
4. Per-week exercises:
   ```bash
   uv run python WeekN/<script>.py
   # or open the notebook
   uv run jupyter lab WeekN/<notebook>.ipynb
   ```

## Claude Code Skills

This repository ships project-local Claude Code slash commands under `.claude/commands/` to streamline the weekly exercise workflow:

| Command | Purpose |
|---------|---------|
| `/week-readme-setup` | Create or update `WeekN/answers/README.md` with questions extracted from the exercise PDF. |
| `/week-commands-generator` | Generate / update `WeekN/commands.md` with run instructions for that week. |
| `/answer-check` | Evaluate whether a candidate answer is correct for a given week/question — **no spoilers**. Auto-invokes `/week-answer-fill` on a `Correct` verdict. |
| `/week-answer-fill` | Insert an answer under the matching heading in `WeekN/answers/README.md`. |
| `/teach` | Guided learning through hints and scaffolded problem-solving (no direct answers). |
| `/commit` | Stage all changes and write a Conventional Commit message. |

### Week Folder Convention

```text
WeekN/
├── <exercise>.pdf            # Original exercise sheet
├── exercise.md               # Extracted question text (created by /week-readme-setup)
├── commands.md               # How to run that week's code
├── <code>.py / .ipynb        # Solution code / notebook
└── answers/
    ├── README.md             # Per-question answers (filled by /week-answer-fill)
    └── *.png                 # Figures referenced by the answers
```

### Persistent Memory

Auto-memory for this project lives at:

```
.claude/projects/c--Users-nick-Desktop-DTU-Courses-02460-Advanced-Machine-Learning-Advanced-ML/memory/
```

with `MEMORY.md` as the index of feedback / project / reference notes that persist across Claude Code conversations.
