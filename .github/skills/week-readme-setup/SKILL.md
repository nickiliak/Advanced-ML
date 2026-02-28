---
name: week-readme-setup
description: "Create or update a WeekN README with programming exercise questions extracted from the PDF. Use when user asks to set up a week (for example 'setup week 1' or 'create week 2 readme'). Reads the exercise PDF, extracts only the practical/programming questions (excluding theoretical exercises), and populates the README with questions and answer spaces."
---

# Week README Setup

## Purpose
Use this skill when the user asks to create or populate a week README with programming exercise questions extracted from the PDF. Only include practical/programming exercises, not theoretical exercises.

## Inputs
- `week`: user phrasing like `week 1`, `Week1`, `setup week 1`, or `1`

## Required Repository Convention
- Week folder: `WeekN/`
- Exactly one exercise PDF in `WeekN/` (for example `02460_week1_exercises.pdf`)
- Answers folder: `WeekN/answers/` (create if missing)
- Week README file: `WeekN/answers/README.md` (create if missing)

## Procedure
1. Normalize week input using [week mapping](./references/week-and-question-normalization.md).
2. Open `WeekN/` and locate:
   - the week PDF (`*.pdf`)
   - the answers folder (`WeekN/answers/` - create if missing)
   - the week README (`WeekN/answers/README.md` if exists, otherwise will be created)
3. Read the week PDF using the [`pdf_reader.py`](../scripts/pdf_reader.py) script and extract **only programming/practical questions** (skip theoretical exercises) using the [PDF parsing rules](./references/pdf-parsing-rules.md).
   - Use `read_pdf_text(pdf_path)` to extract PDF text
   - Use `extract_all_questions(pdf_text)` to get all questions
   - Use `extract_theoretical_vs_programming(pdf_text)` to filter only programming questions
4. Structure the README as follows:
   - If README exists: check for existing questions and preserve them; append any new questions not yet in the file
   - If README doesn't exist: create a new one with a header
   - For each programming question found, add a heading with the question text
   - Underneath each heading, add blank space (3-4 blank lines or a placeholder) for the user to fill in an answer

5. Use this structure for each question:

   ```markdown
   ## Question <normalized-question>: <question-text>

   **Answer:**

   <!-- Add your answer here -->

   ```

## Heading Format Rules
- Use `## Question X.Y: <question text>` format
- If question has a title or description, include it after the colon
- Questions should appear in numerical order in README

## Fallback Rules
- If week folder is missing: report missing `WeekN/` and ask user to add it
- If PDF is missing or multiple PDFs exist: report ambiguity and ask user to specify file
- If PDF cannot be parsed: Use the [`pdf_reader.py`](../scripts/pdf_reader.py) script with debug output to help diagnose. If still unable to parse, ask the user to provide the list of questions manually or the exercise text
- If README exists: merge new questions with existing content, preserving any answers already entered

## Output Contract
- State the week folder used
- State the PDF file used
- List all questions added/found
- State whether `WeekN/answers/README.md` was created or updated
- Do not modify files outside the selected week folder
- Do not overwrite existing answers in README

