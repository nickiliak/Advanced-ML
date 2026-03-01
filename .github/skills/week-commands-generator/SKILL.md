---
name: week-commands-generator
description: "Generate and update commands for a specific week in its corresponding WeekN/commands.md file. Use when user asks to generate/update week commands (for example 'week 1 commands' or 'update Week2 commands'). Inspects the Python script's argument parser and creates command examples for all available modes."
---

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
- Output directories: `WeekN/ckpts/` (models), `WeekN/samples/` (samples), `WeekN/outputs/` (logs/data)
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
   - Use `WeekN/ckpts/`, `WeekN/samples/`, `WeekN/outputs/` in all file paths
   - Include an "Outputs" section documenting where files are saved
   - Minimal parameters table reflecting WeekN/ subdirectory paths
5. Keep formatting lean and practical—no extra prose.

## Output Format
```markdown
# Week N Commands

## [Mode Name]
\`\`\`bash
uv run WeekN/script.py [mode] [parameters]
\`\`\`

## Outputs
- Models: `WeekN/ckpts/`
- Samples: `WeekN/samples/`
- Logs/Data: `WeekN/outputs/`

## Parameters
- `param1`: description (default: value)
- `param2`: description (default: value)
```

## Fallback Rules
- If week folder is missing: report missing `WeekN/` and ask user to create it.
- If no Python script found in `WeekN/`: list available files and ask which to use.
- If script defaults don't use `WeekN/` subdirectory paths: suggest updating the script arguments to use paths like `WeekN/ckpts/model.pt`, `WeekN/samples/`, `WeekN/outputs/`

## Script Modification Best Practice
When updating a script for output organization, ensure:
1. Default argument values use `WeekN/ckpts/`, `WeekN/samples/`, and `WeekN/outputs/` paths
2. Directory creation logic uses `os.makedirs('WeekN/subfolder', exist_ok=True)`
3. All file operations respect these defaults


## Output Contract
- State which week was updated/created
- Confirm `WeekN/commands.md` was created or updated with proper subdirectory paths
- All model, sample, and output paths must be inside `WeekN/` subfolders (ckpts/, samples/, outputs/)
- Do not modify root commands.md or files outside WeekN/
- When updating scripts: ensure directories are created inside `WeekN/` (e.g., `os.makedirs('WeekN/ckpts', exist_ok=True)`)
- Keep output concise
