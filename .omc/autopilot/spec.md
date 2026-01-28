# Auto-Commit Implementation - Complete Specification

## Executive Summary

Implement automatic git commit and push for all three AI co-scientist systems on every iteration.

## Requirements Summary

**Functional:**
- Auto-commit on iteration completion (checkpoint every 3 or score improvement)
- Push immediately to remote
- Only commit allowed files (submissions/, versions/, .omc/plans/)
- Generate structured commit messages with iteration # and score delta

**Non-Functional:**
- Git operations < 5 seconds per iteration
- Handle network errors with retry (3x, exponential backoff)
- Fail-fast on auth errors
- Pre-flight validation (clean repo, correct branch)

**Out of Scope:**
- Multi-repo support
- Parallel execution
- Advanced git features (branching, PRs)

## Architecture

**Shared Module Pattern:**
```
shared/git_auto_commit.py (GitAutoCommit class)
    ↓
├── ai_co_scientist_agents/main.py (direct import)
├── ai_co_scientist_v2/mirror/version_control.py (extension)
└── ai_co_scientist_glm4/main_ralp.py (direct import)
```

## Tech Stack

- **Python**: gitpython>=3.1.40
- **Git**: Native git command-line
- **Integration**: Subprocess-based (GitPython wrapper)

## File Changes

**New Files:**
- `shared/__init__.py`
- `shared/git_auto_commit.py` (400+ lines)
- `.gitattributes`

**Modified Files:**
- `ai_co_scientist_agents/main.py` (+30 lines)
- `ai_co_scientist_v2/mirror/version_control.py` (+20 lines)
- `ai_co_scientist_v2/mirror/engine.py` (+15 lines)
- `ai_co_scientist_glm4/main_ralp.py` (+25 lines)
- `.gitignore` (add workspace/, logs/, exclusions)

## API Design

```python
# Core class
class GitAutoCommit:
    pre_flight_check() -> Dict[str, Any]
    commit_iteration(iteration, score, prev_score, improvements) -> CommitResult
    _generate_commit_message(iteration, score, delta, improvements) -> str
    _stage_allowed_files() -> bool
    _push_with_retry() -> bool
```

## Integration Points

1. **ai_co_scientist_agents**: After quality assessment (line ~228)
2. **ai_co_scientist_v2**: In `_commit_iteration()` (line ~271)
3. **ai_co_scientist_glm4**: After `phase_evaluate()` (line ~424)

## Testing Strategy

1. **Unit**: Mock git operations, test logic
2. **Integration**: Real git commands in temp repo
3. **Manual**: Run 3 iterations, verify git log

## Acceptance Criteria

✅ Each iteration creates git commit with correct files
✅ Commit message includes iteration # and score delta
✅ Push succeeds to remote (verified via git log)
✅ Error handling works (retry, fail-fast)
✅ Pre-flight checks prevent bad states
✅ Git operations add < 5 seconds per iteration

---

**Status**: Ready for implementation
**Estimated Effort**: 9-11 hours
