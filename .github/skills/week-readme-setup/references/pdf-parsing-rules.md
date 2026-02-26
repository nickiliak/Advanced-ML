# PDF Parsing Rules

## Question Extraction
The PDF parser should identify and extract all exercise questions. Look for patterns like:
- Question numbers: `1.1`, `1.2`, `2.1`, etc.
- Headers with "Question" or "Exercise" labels
- Numbered lists or subsections containing questions
- Questions typically appear after a problem statement or problem description

## Question Normalization
Questions should be normalized to the format:
- `Q1.1`, `Q1.2`, `Q2.1` (canonical form)
- Include the question text/title when available
- Preserve the hierarchical structure (main question vs. subquestions)

## Extraction Strategy
1. Use PDF text extraction to read the entire document
2. Identify patterns that indicate question beginnings
3. Extract question number and associated text
4. Group related subquestions together
5. Preserve any descriptive text or context provided with the question

## Fallback Options
If automated parsing fails:
- Ask the user to manually provide the list of questions
- Ask for specific exercise PDF file if multiple PDFs exist
- Offer to extract questions from a text version if available
