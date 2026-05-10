# Project Environment: `uv`

This project uses **`uv`** for Python environment and package management.

## When generating code
- Use `uv pip install` instead of `pip install`
- Use `uv run` instead of `python`
- Use `uv sync` to install dependencies
- Do NOT use `pip` or `python -m venv`
- Keep code and explanations simple and concise
- Avoid over-engineering solutions

## Math notation in chat (not in code)
The user's chat renderer does NOT render LaTeX (`$...$` and `$$...$$` show as raw markup). Use **Unicode mathematical symbols** instead — they render universally:
- Norms: ‖v‖, ‖v‖_Gₓ
- Greek: α β γ δ ε θ λ μ π σ φ ψ ω, Σ Δ ∇
- Operators: × · ∘ ⊗ ⊕ ⟨·,·⟩
- Superscripts: x² x³ xⁿ xᵀ x⁻¹
- Subscripts: x₁ x₂ xₙ xᵢ
- Calculus: ∂ ∫ ∮ ∑ ∏ ∞ √ ≈ ≠ ≤ ≥ → ⇒ ↦
- Sets: ℝ ℕ ℤ ℚ ℂ ∈ ∉ ⊂ ⊆ ∪ ∩
- Logic: ∀ ∃ ¬ ∧ ∨

For complex multi-line derivations use code blocks with these Unicode symbols. Inside actual `.py` / `.md` files (not chat), normal LaTeX is fine.

---

# Exam Prep Context

This repo is the user's study lab for the **02460 final exam**. The exam is written and **paper notes are allowed** — the end goal is a dense, hand-carryable cheatsheet covering every weekly topic.

The pipeline has two stages with **different length budgets**:

1. **Per-week study notes** — length-unconstrained. Live under [ExamPrep/prep/](ExamPrep/prep/), one folder per week, three files each:

   ```
   ExamPrep/prep/WeekN/
   ├── lecture.md     # lecture highlights, key formulas, derivations from slides
   ├── exercises.md   # worked exercise theory, patterns, cross-week links
   └── stuck.md       # confusions, mistakes, repeated wrong turns — drilling targets
   ```

   Folders are created lazily — only when notes work begins for that week. The `/learn` skill auto-proposes lines for `stuck.md` (user approves before write); `lecture.md` and `exercises.md` grow only through user-led editing.

2. **Final cheatsheet** — **hard limit: 3 pages max.** This is what the user will physically bring to the timed (2h) exam. Built from the per-week notes by condensing aggressively. Formula-first, minimal prose, no redundancy across sections. Cheatsheet generator design is deferred until enough weekly notes exist to know what's needed.

Source material for both stages: weekly lecture PDFs, `WeekN/answers/README.md`, project READMEs in [Projects/](Projects/).

## Old Exams Policy — validation set

[ExamPrep/old_exams/](ExamPrep/old_exams/) holds past papers (2024 final, 2024 mock, 2025 final). The user will sit these **timed** after studying as a held-out validation set.

**Access rules (meta-only):**
- ✅ May inspect topic coverage, question format, length, weighting, recurring patterns to guide what the cheatsheet must cover.
- ❌ Never quote or paraphrase question content into study materials, cheatsheets, or weekly answers.
- ❌ Never solve old-exam questions unless the user explicitly asks (e.g. after a timed run, for review).
- ❌ Never let old-exam phrasing leak into hints or examples — the user must see those questions cold.

If unsure whether something counts as leakage, ask before producing.

## Weekly Topics

All weeks have `WeekN/exercise.md` and a scaffolded `WeekN/answers/README.md`.

| Week | Topic |
|------|-------|
| 1  | VAE / Deep Latent Variable Models |
| 2  | Normalizing Flows |
| 3  | Diffusion / DDPM |
| 5  | Manifold Learning & Latent Geometry |
| 6  | Metrics |
| 7  | Geometry |
| 9  | Graph Node Embeddings |
| 10 | GNNs — Graph Classification |
| 11 | Graph Convolutions |

**Progress is computed on demand, not tracked here** (avoids drift). To see current per-week answered counts, run:

```bash
bash .claude/scripts/week_status.sh
```

…or ask Claude to scan `Week*/answers/README.md` for `Add your answer here` placeholders.

[Projects/](Projects/) — three completed course projects (Deep-Generative-Modeling, VAE-Geometry, MUTAG-Gen-GNN). Treat as applied reference / worked examples when building cheatsheet sections.

## Solving Mode

The user solves exercises on their own merit. Three modes available, pick by user intent:

- `/learn week N question X.Y` — **Socratic loop**. Multi-turn scaffolding with per-step verdicts. Never reveals the answer, even if asked. Auto-proposes `stuck.md` entries on `Wrong` verdicts (user approves). Use this for **unsolved** exercises by default.
- `/teach <free text>` — free-form tiered hints, single-turn. Will escalate to a full answer at Tier 5 if the user insists. Use for quick conceptual unblocking outside the exercise loop.
- `/answer-check week N question X.Y "<attempt>"` — grades a written attempt with `Correct/Wrong/Unclear`. No spoilers. Auto-fires `/week-answer-fill` on `Correct`.

When the user asks about an unsolved exercise without specifying the mode, default to suggesting `/learn`.

## Slash Commands — quick reference

| Command | Purpose |
|---------|---------|
| `/week-readme-setup` | Extract exercise questions from a `WeekN/*.pdf` into `WeekN/answers/README.md`. |
| `/week-commands-generator` | Generate `WeekN/commands.md` with run instructions. |
| `/learn` | Socratic teacher. Multi-turn scaffold with per-step verdict, no answers ever. Proposes `stuck.md` entries on `Wrong`. |
| `/answer-check` | Grade a candidate answer; no spoilers. Auto-fires `/week-answer-fill` on `Correct`. |
| `/week-answer-fill` | Insert a confirmed answer under the matching question heading. |
| `/teach` | Free-form tiered hints — escalates to a full answer at Tier 5 if user insists. |
| `/commit` | Stage all changes and write a Conventional Commit message. |
