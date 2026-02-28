---
name: answer-check-no-spoiler
description: "Check whether a user's answer for a specific WeekN question is likely correct using the exercise statement context, and reply only with correct/wrong style feedback without revealing the solution. Use when user asks to validate an answer (for example 'week 1 question 1.4 is this right?')."
---

# Answer Check (No Spoiler)

## Purpose
Use this skill to evaluate a user's submitted answer for a specific week and question while avoiding answer leakage.

## Inputs
- `week`: `week 1`, `Week1`, or `1`
- `question`: `1.4`, `question 1.4`, `q1.4`, or similar
- `user_answer`: the user-provided candidate answer

If `user_answer` is missing, ask the user to provide it.

## Required Repository Convention
- Week folder: `WeekN/`
- Exactly one exercise PDF in `WeekN/`
- Week README file: `README.md` (or `README.MD` fallback)

## Evaluation Policy
Because there is no authoritative answer key, evaluate against:
1. Explicit constraints and definitions in the week exercise PDF.
2. Internal consistency with the question wording.
3. Mathematical/logical soundness of the user's claim.

Use conservative grading:
- If confidence is high and all constraints are satisfied -> `Correct`.
- If any required constraint is violated or reasoning is inconsistent -> `Wrong`.
- If evidence is insufficient from the PDF/question text alone -> return `Unclear` and request one clarifying detail from the user.

## Procedure
1. Normalize week/question with [normalization rules](./references/reply-contract.md).
2. Load the corresponding week PDF using the [`pdf_reader.py`](../scripts/pdf_reader.py) script and locate the target question statement.
   - Use `read_pdf_text(pdf_path)` to extract PDF text
   - Use `extract_question_text(pdf_text, question_number)` to get the specific question
3. Compare `user_answer` only against the question requirements and constraints.
4. Produce no-spoiler response using the fixed response contract below.

## Strict No-Spoiler Rules
- Never provide the full correct answer.
- Never provide a completed derivation or final numeric value if the user's answer is wrong.
- Allow only brief directional hints (max 1 sentence) that point to what to reconsider.
- Do not rewrite the user's answer into the correct form.

## Response Contract
Return exactly this structure:

```text
Verdict: <Correct|Wrong|Unclear>
Reason: <one short sentence about why>
Hint: <optional one-sentence directional hint; omit if Correct>
```

## Fallback Rules
- Missing week folder/PDF/question -> state what is missing and ask user for exact reference.
- Ambiguous question mapping -> ask user to confirm the exact question label.
- If PDF cannot be parsed: Use the [`pdf_reader.py`](../scripts/pdf_reader.py) script to extract and search the text. If still unable to find the question, ask the user to provide the question text.
