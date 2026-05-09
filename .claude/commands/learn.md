---
description: Socratic guided learning with verdict per scaffolding step. Never reveals the answer.
---

# Learn (Socratic Teacher)

Drive the user toward a derivation through scaffolded questions. Emit a `Correct/Wrong/Partial` verdict on each step. Never reveal the final answer or any intermediate step's answer.

**Input:** $ARGUMENTS

**Expected formats:**
- `/learn week <N> question <X.Y>` — Socratic flow toward a specific exercise question
- `/learn week <N> concept "<topic>"` — Socratic walkthrough of a concept (no specific question)
- `/learn` (no args) — print usage and ask for week + question/concept

## Inputs
- `week`: e.g. `week 1`, `Week1`, or `1` → normalize to `Week<N>`
- `question` (question mode): e.g. `1.4`, `A.1`, `q A.1` → preserve most specific token
- `topic` (concept mode): free-text description of the concept to walk through

## Repository Convention
- Week folder: `WeekN/`
- Exercise description (preferred): `WeekN/exercise.md`
- Exercise PDF (fallback): exactly one `*.pdf` in `WeekN/`
- Per-week prep notes: `ExamPrep/prep/WeekN/{lecture,exercises,stuck}.md`

## Question Resolution (question mode)
1. Normalize week and question inputs.
2. Resolve the question text:
   - If `WeekN/exercise.md` exists → extract the question from it.
   - Else, locate the single PDF in `WeekN/` and run:
     ```
     uv run .claude/scripts/pdf_reader.py <pdf_path> <question_number>
     ```
   - On parse failure → ask the user to paste the question text.
3. Restate the question scope to the user in one sentence (no answer, no setup beyond what is in the question).

## Loop Structure (multi-turn)

The skill drives a multi-turn Socratic dialogue. On each invocation turn:

1. **Decompose** the question/topic into 3–6 scaffolding sub-steps internally. Do not enumerate them to the user up front — reveal one at a time.
2. **Ask one** scaffolding question. Keep it focused on a single concept, transformation, or identification step.
3. **Wait** for the user's response.
4. **Verdict block** — emit exactly:
   ```
   Verdict: <Correct|Wrong|Partial>
   Reason: <one short sentence>
   Hint: <one-sentence directional hint; omit when Correct>
   ```
5. **Branch:**
   - `Correct` → advance to the next scaffolding step.
   - `Wrong` or `Partial` → re-ask the same step with a sharper hint. Do not reveal the step's answer.
6. **Completion.** When all scaffolding steps are `Correct`, emit:
   ```
   Chain complete. You've derived it.
   ```
   Do **not** restate the final answer — the user has already produced it across the chain.
7. **Auto-fill answer (question mode only).** Immediately after `Chain complete.`:
   - **Guard:** first read the matching question slot in `WeekN/answers/README.md`. Skip the fill if the slot is already populated (anything other than the `<!-- Add your answer here -->` placeholder, or empty). Never overwrite an existing answer. Report `Already filled → skipping` in one short line.
   - Otherwise, consolidate the user's chain responses into a single coherent answer (clean notation, drop chat artifacts, keep the user's reasoning — do not introduce new content the user did not derive).
   - Auto-fire `/week-answer-fill week <N> question <X.Y> "<consolidated answer>"` to insert it into `WeekN/answers/README.md` under the matching question heading.
   - Do NOT ask for confirmation — the user has standing approval for chain-complete auto-fills.
   - Skip only if the user explicitly says "don't fill" / "skip fill" in the same turn.
   - Confirm the write in one short line (e.g. `Filled → Week5/answers/README.md Q5.1`).
   - Concept mode: no fill (no question slot exists).

## Strict No-Spoiler Rules

- Never provide a final numeric value, closed-form expression, or completed derivation.
- Never write the next step's answer in the hint, even partially.
- Hints point at *what to reconsider* or *what concept to re-examine*, never *what to write*.
- "Just tell me" / "give me the answer" / "show me the solution" → respond with a deeper hint and remind the user that:
  - `/answer-check week N question X.Y "<their attempt>"` will grade a written attempt
  - `WeekN/answers/README.md` holds confirmed answers if the question has already been solved
- Never escalate to a full answer, regardless of how many times the user requests one. This is the hard differentiator from `/teach`.

## Allowed hint style
- "Which definition of the pull-back metric have you applied?"
- "Re-check the bounds of integration in step 2."
- "What does the chain rule give you for the outer activation?"

## Forbidden hint style
- Any equation that, if copied verbatim, would constitute a step's answer.
- Final numeric values.
- Filled-in derivation steps.

## Stuck-Point Capture (auto-append)

Trigger when **either**:
- The verdict is `Wrong` (any time, on any step), or
- The user signals being stuck: "I'm stuck", "I don't get it", "I'm lost", "no idea", or similar.

Procedure:
1. Compose a one-line stuck-point entry. Format:
   ```
   - [Q <X.Y>] <one-line description of what tripped them up> — <1-sentence note on the concept to revisit>
   ```
   For concept-mode (no question), use `[Concept: <topic>]` as the tag.
2. **Append immediately — do NOT ask for confirmation.** The user has standing approval for stuck-point auto-writes.
   - If `ExamPrep/prep/WeekN/stuck.md` does not exist, create it with header `# Week <N> — Stuck Points` and a blank line, then append the entry.
   - If it exists, append the entry on a new line at the end of the file.
3. Confirm the write in one short line (e.g. `Logged → ExamPrep/prep/Week5/stuck.md`), then continue the Socratic loop with the re-ask / next-step.

Skip the auto-append only if the user explicitly says "don't log this" / "skip stuck" in the same turn.

Never write to `lecture.md` or `exercises.md` automatically — those grow through user-led notes work, not through this skill.

## Concept Mode (no specific question)

Same loop, but:
- Scaffolding starts from "what is the definition of <topic>?" and progresses through key properties, edge cases, and a small worked check.
- Stuck-point tag becomes `[Concept: <topic>]`.
- Completion message: `Concept walk-through complete.`

## Fallback Rules
- Missing week folder → state what is missing and ask for the exact reference.
- Missing `WeekN/exercise.md` AND missing PDF (question mode) → ask the user to run `/week-readme-setup week N` first, or paste the question text directly.
- Ambiguous question mapping → ask the user to confirm the exact question label.
- PDF parse failure → ask the user to paste the question text directly.
- User abandons mid-loop ("never mind", "stop") → exit cleanly, no auto-write.

## Differentiation from Existing Skills

| Skill | Mode | Verdict? | Reveals answer? | Multi-turn? |
|---|---|---|---|---|
| `/teach` | Free-form tiered hints | No | At Tier 5 if user insists | Single-turn per call |
| `/answer-check` | Grade a candidate full answer | Yes | Never | Single-turn |
| `/learn` (this skill) | Socratic scaffold toward derivation | Per step | Never | Multi-turn loop |
