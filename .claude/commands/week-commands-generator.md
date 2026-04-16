# Week Commands Generator

Generate and update commands for a specific week in `WeekN/commands.md`.

**Input:** $ARGUMENTS  
Expected format: `week <N>`  
Example: `/week-commands-generator week 1`

## Inputs
- `week`: e.g. `week 1`, `Week1`, or `1` → normalize to `Week<N>`

If week is not provided, ask the user to specify which week.

## Week Normalization
Extract first integer from week input → `Week<N>`.

## Repository Convention
- Week folder: `WeekN/`
- Main Python script: `WeekN/<script_name>.py`
- Commands file: `WeekN/commands.md` (not root `commands.md`)
- Output directories: `WeekN/ckpts/`, `WeekN/samples/`, `WeekN/outputs/`
- All commands assume execution from project root using relative paths

## Procedure
1. Normalize week input.
2. Locate `WeekN/` and identify the main Python script.
3. Inspect the script's argument parser to extract:
   - Available modes (e.g., `train`, `sample`)
   - Default parameters and their descriptions
4. Create or update `WeekN/commands.md` with:
   - Concise command examples (1–2 per mode)
   - Commands formatted as: `uv run WeekN/script.py [mode] [parameters]`
   - Paths using `WeekN/ckpts/`, `WeekN/samples/`, `WeekN/outputs/`
   - An "Outputs" section documenting where files are saved
   - A lean parameters table

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
- Missing week folder → report and ask user to create it.
- No Python script found → list available files and ask which to use.
- Script defaults don't use `WeekN/` subdirectory paths → suggest updating the script arguments.

## Script Best Practices
When a script needs to be updated for output organization:
1. Default argument values should use `WeekN/ckpts/`, `WeekN/samples/`, `WeekN/outputs/` paths
2. Directory creation: `os.makedirs('WeekN/subfolder', exist_ok=True)`

## Output Contract
- State which week was updated/created.
- Confirm `WeekN/commands.md` was created or updated.
- All model/sample/output paths must be inside `WeekN/` subfolders.
- Never modify root `commands.md`.
- Keep output concise.
