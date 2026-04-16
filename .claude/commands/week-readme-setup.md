---
description: Create or update a WeekN README with programming exercise questions extracted from the PDF
---

# Week README Setup

Create or update a WeekN README with programming exercise questions extracted from the PDF.

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
- Answers folder: `WeekN/answers/` (create if missing)
- Week README: `WeekN/answers/README.md` (create if missing)

## Procedure
1. Normalize week input.
2. Locate `WeekN/`, the PDF, and `WeekN/answers/README.md`.
3. Extract **only programming/practical questions** (skip theoretical exercises) using `.claude/scripts/pdf_reader.py`:
   ```
   uv run .claude/scripts/pdf_reader.py <pdf_path>
   ```
   Use `extract_theoretical_vs_programming()` to filter programming questions.
4. For each programming question found:
   - If README exists: check for existing questions and preserve them; append new questions not yet in the file
   - If README doesn't exist: create with a header

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
- List all questions added/found.
- State whether `WeekN/answers/README.md` was created or updated.
- Do not modify files outside the selected week folder.
- Do not overwrite existing answers in README.
