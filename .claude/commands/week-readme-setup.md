---
description: Create or update a WeekN README with theoretical and programming exercise questions extracted from the PDF
---

# Week README Setup

Create or update a WeekN README with both theoretical and programming exercise questions extracted from the PDF.

**Input:** $ARGUMENTS  
Expected format: `week <N>`  
Example: `/week-readme-setup week 1`

## Inputs
- `week`: e.g. `week 1`, `Week1`, `setup week 1`, or `1` → normalize to `Week<N>`

## Week Normalization
Extract first integer from week input → `Week<N>`.

## Repository Convention
- Week folder: `WeekN/`
- Exercise PDF: exactly one `*.pdf` in `WeekN/`
- Exercise Description: `WeekN/exercise.md` (created by this script)
- Answers folder: `WeekN/answers/` (create if missing)
- Week README: `WeekN/answers/README.md` (create if missing)

## Procedure
1. Normalize week input.
2. Locate `WeekN/` and the PDF.
3. Extract **both theoretical and programming questions** using `.claude/scripts/pdf_reader.py`:
   ```
   uv run .claude/scripts/pdf_reader.py <pdf_path>
   ```
   Use `extract_theoretical_vs_programming()` and keep both returned dicts.
4. Create `WeekN/exercise.md` with the extracted exercise description and questions from the PDF:
   - Include a header identifying the week
   - Group questions under `## Theoretical Exercises` and `## Programming Exercises` sections
   - List all questions with their full text under their respective section
   - This file becomes the source of truth for all question references
5. Create or update `WeekN/answers/README.md`:
   - Group questions under `## Theoretical Exercises` and `## Programming Exercises` headings
   - For each question (theoretical and programming) found in `exercise.md`:
     - If README exists: check for existing questions and preserve them; append new questions not yet in the file under the correct section
     - If README doesn't exist: create with a week header and the two section headings

## Question Structure
Add each question using this format:
```markdown
## Question X.Y: <question-text>

**Answer:**

<!-- Add your answer here -->

```

## Heading Format Rules
- Use `## Question X.Y: <question text>` format
- Include question title/description after the colon
- Questions appear in numerical order

## Fallback Rules
- Missing week folder → report and ask user to add it.
- Missing/ambiguous PDF → ask user to specify file.
- PDF parse failure → ask user to provide the list of questions manually.
- Existing README → merge new questions, preserving any answers already entered.

## Output Contract
- State the week folder used.
- State the PDF file used.
- Confirm `WeekN/exercise.md` was created (contains exercise description and all questions).
- List all questions added/found.
- State whether `WeekN/answers/README.md` was created or updated.
- Do not modify files outside the selected week folder.
- Do not overwrite existing answers in README.
