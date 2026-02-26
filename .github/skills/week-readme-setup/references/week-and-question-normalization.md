# Week and Question Normalization

## Week Normalization
Accept these forms:
- `week 1`
- `Week1`
- `1`
- `setup week 1`
- `create week 2 readme`

Normalize to folder token: `Week1`, `Week2`, etc.

General rule:
- Extract first integer from user week input.
- Construct `Week<integer>`.
