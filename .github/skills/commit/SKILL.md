---
name: commit
description: Skill to stage, auto-generate commit message, and commit changes when /commit is typed. Summarizes changes using file diffs and context.
---

# Auto Commit Skill

## Usage
- Type `/commit` in chat.
- The skill will:
  1. Detect all changed files and their diffs.
  2. Summarize the changes to generate a commit message.
  3. Stage all changes.
  4. Show you the generated commit message for approval.
  5. Commit if you confirm.

## Workflow
1. Detect unstaged and staged changes (git status).
2. Read diffs (git diff, git diff --cached).
3. Summarize changes (file names, key diffs, context window).
4. Propose a commit message (AI-generated summary).
5. On approval, run `git add -A` and `git commit -m "<message>"`.

## Safety
- Always prompt for confirmation before committing.
- Never push automatically.

## Extensibility
- Can be extended to support push, amend, or custom commit templates.

---

This skill enables fast, context-aware commits with minimal manual effort. See implementation for details.