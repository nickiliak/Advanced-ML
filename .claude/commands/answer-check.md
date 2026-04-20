---
description: Evaluate whether a user's answer for a specific week and question is correct, without revealing the solution
---

# Answer Check (No Spoiler)

Evaluate whether a user's answer for a specific week and question is correct, without revealing the solution.

**Input:** $ARGUMENTS  
Expected format: `week <N> question <X.Y> <user_answer>`  
Example: `/answer-check week 1 question 1.4 "the answer is X because Y"`

## Inputs
- `week`: e.g. `week 1`, `Week1`, or `1` → normalize to `Week<N>`
- `question`: e.g. `1.4`, `q1.4`, `question 1.4` → normalize to canonical token `Q1.4`
- `user_answer`: the candidate answer to evaluate

If `user_answer` is missing, ask the user to provide it.

## Week/Question Normalization
- Extract first integer from week input → `Week<N>`
- Preserve most specific question token provided (`1.4`, `x`, etc.)

## Repository Convention
- Week folder: `WeekN/`
- Exercise Description (preferred): `WeekN/exercise.md` (created by week-readme-setup)
- Exercise PDF (fallback): exactly one `*.pdf` in `WeekN/`
- Week README: `WeekN/answers/README.md`

## Procedure
1. Normalize week and question inputs.
2. Check for the question in `WeekN/exercise.md` **first** (preferred source):
   - If `exercise.md` exists, extract the question text from it
   - If `exercise.md` does not exist, locate the PDF in `WeekN/` and run `.claude/scripts/pdf_reader.py`:
     ```
     uv run .claude/scripts/pdf_reader.py <pdf_path> <question_number>
     ```
3. Compare `user_answer` against the question requirements and constraints from the exercise source.
4. Apply conservative grading:
   - `Correct`: answer satisfies all explicit requirements and no contradictions
   - `Wrong`: required component is missing, incorrect, or contradicts constraints
   - `Unclear`: PDF context is insufficient to validate decisively

## Strict No-Spoiler Rules
- Never provide the full correct answer.
- Never provide a completed derivation or final numeric value when wrong.
- Allow only one brief directional hint pointing to what to reconsider.
- Do not rewrite the user's answer into the correct form.

## Allowed hint style
- "Re-check the sign convention in your ELBO term."
- "Verify that your normalization condition holds for all classes."

## Forbidden hint style
- Full corrected equation
- Final numeric answer
- Step-by-step solution

## Response Format
Return exactly this structure:
```
Verdict: <Correct|Wrong|Unclear>
Reason: <one short sentence about why>
Hint: <optional one-sentence directional hint; omit if Correct>
```

## Auto-Fill on Correct
If the verdict is `Correct`, immediately invoke the `/week-answer-fill` skill with the same week, question, and user answer — do not wait for the user to ask.

## Fallback Rules
- Missing week folder → state what is missing and ask for exact reference.
- Missing `WeekN/exercise.md` AND missing PDF → ask user to run `/week-readme-setup week N` first, or provide the question text directly.
- Ambiguous question mapping → ask user to confirm exact question label.
- Exercise file/PDF parse failure → ask user to provide the question text directly.
