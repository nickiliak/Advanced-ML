---
description: Compute and auto-fill the answer to a week/question when the user has grasped the concept and the remaining work is rote calculation. Post-/learn escape hatch.
---

# Crunch (Auto-Solve Rote Calc)

Compute the full answer to a week/question end-to-end and auto-fill it into `WeekN/answers/README.md`. Use only when the user has already done the conceptual work (typically via `/learn`) and the remainder is mechanical algebra/arithmetic.

**Input:** $ARGUMENTS
**Expected formats:**
- `/crunch week <N> question <X.Y>` — compute and fill the named question
- `/crunch week <N> question <X.Y> note "<setup>"` — same, with explicit conceptual context the user already established

## Inputs
- `week`: e.g. `week 5`, `Week5`, `5` → normalize to `Week<N>`
- `question`: e.g. `5.1`, `Q5.1` → canonical token `Q<X.Y>`
- `note` (optional): the conceptual setup the user already confirmed in `/learn` chat or elsewhere — used to anchor the derivation so it matches the user's framing

If `week` or `question` is missing, ask.

## When to invoke

- After a `/learn` session where the user has established the approach but stopped before grinding the calculation.
- When the user says any of: "I get it, just fill it", "skip the arithmetic", "crunch the numbers", "the rest is mechanical".
- **Never** as a substitute for `/learn` when the user has not engaged with the concept. This is the post-conceptual escape hatch, not a shortcut around learning.

## Repository Convention
- Week folder: `WeekN/`
- Exercise description (preferred): `WeekN/exercise.md`
- Exercise PDF (fallback): exactly one `*.pdf` in `WeekN/`
- Answers README: `WeekN/answers/README.md`
- Per-week prep notes: `ExamPrep/prep/WeekN/{lecture,exercises,stuck}.md`

## Procedure

1. Normalize week and question.
2. Resolve question text:
   - If `WeekN/exercise.md` exists → extract the question from it.
   - Else locate the single PDF in `WeekN/` and run:
     ```
     uv run .claude/scripts/pdf_reader.py <pdf_path> <question_number>
     ```
   - On parse failure → ask the user to paste the question text.
3. **Guard — slot already filled.** Read the matching question slot in `WeekN/answers/README.md`. If the slot holds anything other than the `<!-- Add your answer here -->` placeholder (or empty content), report `Already filled → skipping` in one line and exit. Never overwrite an existing answer.
4. **Anchor on the user's framing.** Read `ExamPrep/prep/WeekN/stuck.md` (if present) and the `note` argument (if provided). The derivation should match the approach the user already locked in during `/learn` — do not invent a different framing.
5. **Compute the answer.** Work through the full derivation/calculation. Show the chain of steps that gets from setup to result. Include intermediate identities so the answer is self-contained for revision.
   - Chat output: use Unicode math symbols (‖·‖, ², ₁, √, π, Σ, ∂, ∇, …) — the chat renderer does not render LaTeX.
   - File output (the answer written to README): normal LaTeX is fine.
6. **Auto-fire** `/week-answer-fill week <N> question <X.Y> "<answer>"` to insert it under the matching question heading. Do not ask for confirmation — invocation of `/crunch` is itself the standing approval.
7. Confirm the write in one short line, e.g. `Crunched → Week5/answers/README.md Q5.1`.

## Output Contract

In order, each on its own block:
1. One short summary line of the conceptual frame (one sentence, the strategy — not the full derivation).
2. The derivation as it will be written to the README (the file payload, verbatim).
3. Confirmation line of the file write.

Do not modify files outside the selected week folder.

## Fallback Rules

- Missing week folder → state what is missing, ask for the exact reference.
- Missing `WeekN/exercise.md` AND missing PDF → ask the user to run `/week-readme-setup week N` first, or paste the question text directly.
- Ambiguous question mapping → ask the user to confirm the exact question label.
- Slot already filled → skip with the one-line report from step 3; do not propose a diff or overwrite.
- User invokes without prior `/learn` engagement and the question is conceptual (not just arithmetic) → respond once:
  > `/crunch` is the post-conceptual escape hatch. Run `/learn week N question X.Y` first, or use `/teach` for a single-turn walkthrough.
  
  Then exit without writing.
- Exercise file/PDF parse failure → ask the user to paste the question text directly.

## Differentiation from Existing Skills

| Skill | Purpose | Reveals answer? | Writes to README? |
|---|---|---|---|
| `/learn` | Socratic scaffold | Never | Only on `Chain complete.` via internal auto-fill |
| `/teach` | Tiered hints in chat | At Tier 5 if user insists | No |
| `/answer-check` | Grade a candidate answer | Never | On `Correct` via auto-fill |
| `/week-answer-fill` | Insert a user-supplied answer string | N/A (user supplies) | Yes |
| `/crunch` (this) | Compute the answer end-to-end and fill | Yes — fully | Yes |

The distinguishing trait: `/crunch` is the only skill that **both computes the full answer and writes it to the README**. It exists because rote calculation past a settled conceptual frame has zero study value.