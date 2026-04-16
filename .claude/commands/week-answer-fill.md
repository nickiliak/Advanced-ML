# Week Answer Fill

Fill in an answer for a specific week and question in the weekly README.

**Input:** $ARGUMENTS  
Expected format: `week <N> question <X.Y> <answer_text>`  
Example: `/week-answer-fill week 1 question 1.4 "The ELBO decomposes into reconstruction + KL terms"`

## Inputs
- `week`: e.g. `week 1`, `Week1`, or `1` → normalize to `Week<N>`
- `question`: e.g. `1.4`, `q1.4`, `question 1.4` → normalize to canonical token `Q1.4`
- `answer_text`: the answer content to insert

If `answer_text` is not provided, ask the user to provide it.

## Week/Question Normalization
- Extract first integer from week input → `Week<N>`
- Preserve most specific question token (`1.4`, `x`, etc.)
- Canonical form: `Q1.4`

## Repository Convention
- Week folder: `WeekN/`
- Exercise PDF: exactly one `*.pdf` in `WeekN/`
- Answers folder: `WeekN/answers/` (create if missing)
- Week README: `WeekN/answers/README.md` (create if missing)

## Procedure
1. Normalize week and question inputs.
2. Locate `WeekN/`, the PDF, and `WeekN/answers/README.md`.
3. Read the PDF using `.claude/scripts/pdf_reader.py` to confirm the target question:
   ```
   uv run .claude/scripts/pdf_reader.py <pdf_path> <question_number>
   ```
4. In the README, find the heading matching the target question using this priority:
   1. Heading contains exact numeric token (`1.4`, `Q1.4`, `Question 1.4`)
   2. Heading starts with `Question` + token
   3. Heading contains normalized text token (case-insensitive)
5. Append below the matched heading:
   ```markdown
   **Answer:**
   <answer_text>
   ```
6. If the answer references images in `WeekN/outputs/`, copy them to `WeekN/answers/` and update image paths to relative (e.g., `![description](image.png)`).
7. Preserve all existing content and formatting. Do not reorder sections.

## Fallback Rules
- Missing week folder → report and ask user to add it.
- Missing answers folder → create `WeekN/answers/`.
- Missing README → create `WeekN/answers/README.md` with basic structure.
- Missing/ambiguous PDF → ask user to specify file.
- No matching heading → append new section at end:
  ```markdown
  ## Question <normalized-question>
  **Answer:**
  <answer_text>
  ```
- PDF parse failure → ask user to provide exercise text for the target question.

## Output Contract
- State which files were used.
- State whether answer was inserted under existing heading or new section.
- List any images copied to answers folder.
- Do not modify files outside the selected week folder.
