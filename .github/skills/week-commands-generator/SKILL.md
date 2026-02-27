# Week Commands Generator

## Purpose
Use this skill to generate and update commands for a specific week in its corresponding WeekN/commands.md file.

## Inputs
- `week`: user phrasing like `week 1`, `Week1`, or `1`

If `week` is not provided, ask the user to specify which week.

## Required Repository Convention
- Week folder: `WeekN/`
- Main Python script: `WeekN/<script_name>.py` (e.g., `Week1/vae_bernoulli.py`)
- Commands file: `WeekN/commands.md` (not in root)
- All commands assume execution from root directory using relative paths

## Procedure
1. Normalize week input using standard week mapping (e.g., "week 1" → "Week1").
2. Locate the `WeekN/` folder and identify the main Python script.
3. Inspect the script's argument parser to extract:
   - Available modes (e.g., `train`, `sample`)
   - Default parameters and their descriptions
4. Create or update `WeekN/commands.md` with:
   - Concise command examples (1-2 per mode, showing typical usage)
   - Commands formatted as: `uv run WeekN/script.py [mode] [parameters]`
   - Minimal parameters table
5. Keep formatting lean and practical—no extra prose.

## Output Format
```markdown
# Week N Commands

## [Mode Name]
\`\`\`bash
uv run WeekN/script.py [mode] [parameters]
\`\`\`

## Parameters
- `param1`: description (default: value)
- `param2`: description (default: value)
```

## Fallback Rules
- If week folder is missing: report missing `WeekN/` and ask user to create it.
- If no Python script found in `WeekN/`: list available files and ask which to use.

## Output Contract
- State which week was updated/created
- Confirm `WeekN/commands.md` was created or updated
- Do not modify root commands.md or files outside WeekN/
- Keep output concise

