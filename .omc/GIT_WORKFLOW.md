# Git Workflow for Automated Iterations

**Generated:** 2026-01-29

---

## Configuration Status

✅ **Git Configured for Automated Pushes**

- **Remote:** `https://github.com/plzprayme/ai-co-scientist-challenge.git`
- **Credential Helper:** Enabled (`git config credential.helper store`)
- **PAT Location:** `~/.git-credentials` (mode 600)
- **User:** pratme <pratme@users.noreply.github.com>

---

## Automated Commit & Push Pattern

### Every Iteration Workflow

```bash
# 1. Check status
git status

# 2. Stage changes (exclude caches, logs, workspace)
git add AGENTS.md .omc/
git add ai_co_scientist_agents/AGENTS.md
git add ai_co_scientist_v2/AGENTS.md
git add ai_co_scientist_glm4/AGENTS.md
# ... other relevant files

# 3. Create commit
git commit -m "$(cat <<'EOF'
[Iteration N] Brief description

- Change 1
- Change 2

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
EOF
)"

# 4. Push to remote
git push origin master
```

---

## Excluded Patterns

**Always exclude from commits:**

```bash
# Python cache
__pycache__/
*.pyc
*.pyo

# Runtime data
logs/
workspace/
*.log

# Serena state (if not needed)
.serena/

# OMC internal state (usually)
.omc/state/subagent-tracking.json
```

**Recommended .gitignore:**

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/

# Logs
logs/
*.log

# Workspace
workspace/
*.workspace

# Serena
.serena/

# IDE
.vscode/
.idea/
*.swp
*.swo
```

---

## Verification Commands

```bash
# Verify credentials work
git push origin master --dry-run

# Verify remote
git remote -v

# Verify credential storage
git config --list | grep credential

# Check recent commits
git log --oneline -5
```

---

## Integration with Workflows

### After AGENTS.md Generation

```bash
# Commit documentation
git add AGENTS.md ai_co_scientist_agents/AGENTS.md
git commit -m "docs: update AGENTS.md for system X"
git push origin master
```

### After RALPLAN Completion

```bash
# Commit plan
git add .omc/plans/feature.md
git add .omc/ralplan-state.json
git commit -m "plan: complete RALPLAN for feature"
git push origin master
```

### After Implementation Work

```bash
# Commit code changes
git add src/
git commit -m "feat: implement feature X"
git push origin master
```

---

## Troubleshooting

### Push Fails with Authentication Error

```bash
# Re-configure credentials (use your own PAT from .mcp.json)
echo "https://YOUR_PAT@github.com" > ~/.git-credentials
chmod 600 ~/.git-credentials
git config credential.helper store
```

### Push Fails with "Non-fast-forward"

```bash
# Pull first, then push
git pull origin master --rebase
git push origin master
```

### Need to Change PAT

1. Update MCP config: `.mcp.json`
2. Update credentials file: `~/.git-credentials`
3. Test: `git push origin master --dry-run`

---

## Best Practices

1. **Commit Often**: Every iteration, every meaningful change
2. **Push Immediately**: Don't let commits pile up locally
3. **Clear Messages**: Describe what changed and why
4. **Co-Authorship**: Always include Co-Authored-By for AI contributions
5. **Verify Status**: Check `git status` before committing

---

## Quick Reference

```bash
# Full workflow (one iteration)
git status
git add .omc/ AGENTS.md ai_co_scientist_*/AGENTS.md
git commit -m "[Iter N] description"
git push origin master

# Verify push worked
git log --oneline -1
git diff origin/master
```

---

**Last Updated:** 2026-01-29
**Git Repository:** https://github.com/plzprayme/ai-co-scientist-challenge
