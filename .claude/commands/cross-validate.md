---
description: Cross-validate a week's answers in WeekN/answers/README.md against the official WeekN/solutions.pdf, with optional auto-rewrite of incorrect answers
---

# Cross-Validate Week Answers

Cross-validate every answered question in `WeekN/answers/README.md` against the official `WeekN/solutions.pdf`. Produce per-question verdicts with page references, then offer to overwrite any `Wrong` or `Partial` answers with the official solution (one confirmation per question).

**Input:** $ARGUMENTS
Expected format: `week <N>`
Example: `/cross-validate week 1`

## Inputs
- `week`: e.g. `week 1`, `Week1`, or `1` → normalize to `Week<N>`.

## Week Normalization
- Extract first integer from week input → `Week<N>`.

## Repository Convention
- Week folder: `WeekN/`
- Answers file: `WeekN/answers/README.md`
- Solutions PDF (required): `WeekN/solutions.pdf`
- Exercise text (preferred): `WeekN/exercise.md`
- Exercise PDF (fallback): `WeekN/02460_week<N>_exercises.pdf`

## Procedure
1. Normalize `week` input.
2. Verify both `WeekN/answers/README.md` and `WeekN/solutions.pdf` exist. If `solutions.pdf` is missing, abort with:
   ```
   solutions.pdf not found at WeekN/solutions.pdf — drop the official solutions PDF there and re-run.
   ```
3. Extract solutions text once:
   ```
   uv run .claude/scripts/pdf_reader.py WeekN/solutions.pdf
   ```
4. Parse `WeekN/answers/README.md`: collect every `## Question X.Y` (or `## QX.Y`) heading and the text between its `**Answer:**` marker and the next `## ` heading.
5. For each question `X.Y`:
   - If the answer body is empty or contains only `<!-- Add your answer here -->` → verdict = `Missing`. Skip the rewrite step.
   - Otherwise extract the official solution for `X.Y` from `solutions.pdf`:
     ```
     uv run .claude/scripts/pdf_reader.py WeekN/solutions.pdf X.Y
     ```
   - Compare the user answer against the official solution and assign one of:
     - `Correct`: all required components present, no contradiction with the official solution.
     - `Partial`: some required components present but at least one is missing or incorrect.
     - `Wrong`: core claim contradicts the official solution, or the central required step is incorrect.
     - `Unclear`: the question cannot be located in `solutions.pdf` (record the pages searched).
6. Emit one result block per question (see Response Format below).
7. After all results are listed, iterate over `Wrong` and `Partial` verdicts in order. For each, ask:
   ```
   Q<X.Y> [<verdict>]: rewrite with official solution? (y/n)
   ```
   - On `y`: locate the heading in the README using this priority and replace only the body between `**Answer:**` and the next `## ` heading with the official solution text.
     1. Heading contains exact numeric token (`1.4`, `Q1.4`, `Question 1.4`).
     2. Heading starts with `Question` + token.
     3. Heading contains the question's title text (case-insensitive).
   - On `n`: leave the answer untouched.

## Grading Notes
- The user's answer wording can differ from the solution; only the substance matters.
- Treat numerical answers as `Correct` only if they match within obvious rounding tolerance.
- For multi-part questions, downgrade to `Partial` if any sub-part is missing or wrong.
- Cite a page number from `solutions.pdf` whenever possible; use `n/a` when the official solution spans the whole document or no page can be pinned down.

## Response Format

Per question, exactly:
```
Q<X.Y> — <Correct|Wrong|Partial|Missing|Unclear>
  Reason: <one short sentence>
  Solutions ref: p.<page or "n/a">
```

Footer after all questions:
```
Summary: <c> Correct · <p> Partial · <w> Wrong · <m> Missing · <u> Unclear  (total <n>)
```

## Auto-Rewrite Rules
- Never rewrite without an explicit `y` for that question.
- Never modify questions verdicted `Correct`, `Missing`, or `Unclear`.
- Preserve the `## Question X.Y: <title>` heading exactly.
- Preserve the `**Answer:**` line. Replace only the body between it and the next `## ` heading.
- Preserve embedded image references (`![...](*.png)`) when they belong to the question being rewritten only if they remain accurate; otherwise drop them and note this in the response.
- Do not touch any file other than `WeekN/answers/README.md`.

## Fallback Rules
- Missing `WeekN/` → report and abort.
- Missing `WeekN/answers/README.md` → suggest `/week-readme-setup week N` and abort.
- Missing `WeekN/solutions.pdf` → abort with the exact message from step 2.
- Question heading in README but not findable in `solutions.pdf` → verdict `Unclear`, list pages searched, skip the rewrite step for that question.
- PDF parse failure → ask the user to confirm `solutions.pdf` is text-based (not a scan); abort.

## Output Contract
- State which week and files were used.
- Print every per-question block, then the summary footer.
- For each rewrite, state whether the README was modified and which heading matched.
- Do not modify files outside the selected week folder.
