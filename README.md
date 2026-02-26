# Advanced Machine Learning (02460)

DTU Course: Advanced Machine Learning

## Project Structure

```
Advanced-ML/
├── main.py
├── pyproject.toml
├── README.md
├── Projects/
│   └── Deep-Generative-Modeling/   # Submodule
├── Week1/
├── Week2/
└── Week3/
```

## Setup

1. Initialize submodules:
```bash
git submodule update --init --recursive
```

2. Install dependencies with `uv`:
```bash
uv sync
```

3. Run the project:
```bash
uv run python main.py
```

## Copilot Skills

This repository includes two project-local Copilot skills under `.github/skills/`:

- `week-answer-fill`
	- Purpose: fill an answer into the selected week README for a specific question.
	- Expected input style: `week 1 question 1.4` (plus the answer text to insert).
	- Behavior: resolves `WeekN/`, reads the week exercise PDF, and appends under the matching question heading in `README.md`.

- `answer-check-no-spoiler`
	- Purpose: check whether a user's answer is correct/wrong for a selected week question.
	- Expected input style: `week 1 question 1.4` + candidate answer.
	- Behavior: evaluates against the exercise statement and replies with a verdict without revealing the full solution.

### Week Folder Convention (Required)

For each week, keep this structure so both skills work reliably:

```text
WeekN/
├── <exercise>.pdf
└── README.md
```

Notes:
- Keep exactly one exercise PDF in each `WeekN/` folder.
- Use question headings in `README.md` that include the question token (for example `Question 1.4`).
