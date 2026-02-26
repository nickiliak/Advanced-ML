# Week and Question Normalization

## Week Normalization
Accept these forms:
- `week 1`
- `Week1`
- `1`

Normalize to folder token: `Week1`.

General rule:
- Extract first integer from user week input.
- Construct `Week<integer>`.

## Question Normalization
Accept these forms:
- `1.4`
- `q1.4`
- `question 1.4`
- `question x` (if exactly one `question x` appears in PDF/README)

Normalize to canonical token:
- Numeric form: `Q1.4`
- Text form: `Question X`

## README Heading Matching Rules
Try in this order:
1. Heading contains exact numeric question token (`1.4`, `Q1.4`, `Question 1.4`)
2. Heading starts with `Question` + token
3. Heading contains same normalized text token (case-insensitive)

If multiple headings match:
- Prefer exact numeric match.
- Otherwise choose the first heading in document order and report ambiguity to user.
