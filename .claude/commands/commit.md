# Auto Commit

Stage all changed files, generate a context-aware commit message, and commit.

## Workflow
1. Run `git status` to detect all changed files.
2. Run `git diff` and `git diff --cached` to read diffs.
3. Summarize changes (file names, key diffs) to draft a commit message.
4. Show the generated commit message for approval.
5. On approval, run `git add -A` and `git commit -m "<message>"`.

## Safety Rules
- Always prompt for confirmation before committing.
- Never push automatically.
- Never use `--no-verify`.

## Commit Message Style
- Use Conventional Commits format: `type(scope): description`
- Subject ≤ 50 chars
- Add body only when the "why" isn't obvious from the diff
