# Normalization and Reply Contract

## Week/Question Normalization
- Week input: extract first integer and map to `WeekN`.
- Question input: preserve the most specific token provided by user (`1.4`, `x`, etc.).

## Confidence Guidance
Use `Correct` only when both are true:
1. The answer satisfies all explicit requirements in the question statement.
2. No contradiction with definitions/assumptions in the PDF context.

Use `Wrong` when either is true:
1. Required component is missing or incorrect.
2. Core reasoning conflicts with the task constraints.

Use `Unclear` when context in PDF is insufficient to validate decisively.

## No-Spoiler Hint Style
Allowed:
- "Re-check the sign convention in your ELBO term."
- "Verify that your normalization condition holds for all classes."

Not allowed:
- Full corrected equation.
- Final numeric answer.
- Step-by-step solution.
