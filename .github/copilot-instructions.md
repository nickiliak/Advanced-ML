# GitHub Copilot Instructions

## Project Environment: `uv`

This project uses **`uv`** for Python environment and package management.

### When generating code:
- Suggest `uv pip install` instead of `pip install`
- Suggest `uv run` instead of `python`
- Suggest `uv sync` to install dependencies
- Do NOT suggest `pip` or `python -m venv`
- Keep code and explanations simple and concise
- Avoid over-engineering solutions
