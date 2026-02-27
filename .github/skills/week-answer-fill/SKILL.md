---
name: week-answer-fill
description: "Fill answers in WeekN README files from exercise instructions. Use when user asks for a specific week and question (for example 'week 1 question 1.4'). Resolves week folder, reads the week exercise PDF, and appends the answer under the matched question heading in README without changing unrelated content."
---

# Week Answer Fill

## Purpose
Use this skill when the user asks to fill in an answer for a specific week and question in the weekly README.

## Inputs
- `week`: user phrasing like `week 1`, `Week1`, or `1`
- `question`: user phrasing like `1.4`, `question 1.4`, `q1.4`, or `question x`
- `answer_text`: the answer content to insert in the README

If `answer_text` is not provided, ask the user to provide it.

## Required Repository Convention
- Week folder: `WeekN/`
- Exactly one exercise PDF in `WeekN/` (for example `02460_week1_exercises.pdf`)
- Answers folder: `WeekN/answers/` (create if missing)
- Week README file: `WeekN/answers/README.md` (create if missing)

## Procedure
1. Normalize week input using [week mapping](./references/week-and-question-normalization.md).
2. Open `WeekN/` and locate:
   - the week PDF (`*.pdf`)
   - the answers folder (`WeekN/answers/`), create if missing
   - the week README (`WeekN/answers/README.md`), create if missing
3. Read the week PDF exercise text and identify the exact target question using the normalized question token.
4. In week README, find a heading that matches the target question pattern from [heading matching rules](./references/week-and-question-normalization.md).
5. Append the answer directly below the matched heading using this block:

   ```markdown
   **Answer:**
   <answer_text>
   ```

6. If the answer references images from `WeekN/outputs/`, copy those images to `WeekN/answers/` and update image paths in the README to use relative paths (e.g., `![description](image.png)`).
7. Preserve existing content and formatting. Do not reorder sections.

## Fallback Rules
- If week folder is missing: report missing `WeekN/` and ask user to add it.
- If answers folder is missing: create `WeekN/answers/`.
- If README is missing in answers folder: create `WeekN/answers/README.md` with basic structure.
- If PDF is missing or multiple PDFs exist: report ambiguity and ask user to choose file.
- If no matching heading exists in README: append a new section at end:

  ```markdown
  ## Question <normalized-question>

  **Answer:**
  <answer_text>
  ```

- If PDF cannot be parsed, ask the user to provide the exercise text snippet for the target question.

## Output Contract
- State which files were used.
- State whether answer was inserted under existing heading or new section.
- List any images copied to the answers folder.
- Do not modify files outside the selected week folder.
