# Auto-Commit Implementation Plan
## Git Auto-Commit for AI Co-Scientist Systems

**Status:** Ready for Review  
**Created:** 2026-01-29  
**Estimated Effort:** 9-11 hours  
**Complexity:** MEDIUM

---

## Executive Summary

Implement automatic git commit and push functionality for all three AI co-scientist systems (`ai_co_scientist_agents`, `ai_co_scientist_v2`, `ai_co_scientist_glm4`). The system will create commits on each iteration completion with structured commit messages including iteration number and score delta.

**Repository:** `https://github.com/plzprayme/ai-co-scientist-challenge.git`  
**Branch:** `master`  
**Current Status:** Git repo initialized, remote configured

---

## Table of Contents

1. [Context](#1-context)
2. [Architecture](#2-architecture)
3. [File Changes Summary](#3-file-changes-summary)
4. [Task Breakdown](#4-task-breakdown)
5. [Dependencies](#5-dependencies)
6. [Acceptance Criteria](#6-acceptance-criteria)
7. [Testing Strategy](#7-testing-strategy)
8. [Rollback Plan](#8-rollback-plan)

---

## 1. Context

### 1.1 Original Request

From `.omc/autopilot/spec.md`:

> Implement automatic git commit and push for all three AI co-scientist systems on every iteration.

### 1.2 Key Decisions (from requirements.md)

| Decision | Value |
|----------|-------|
| **Commit Timing** | AFTER scoring improvement OR every 3rd iteration |
| **Files to Commit** | `submissions/`, `versions/`, `.omc/plans/` only |
| **Target Branch** | `master` |
| **Push Behavior** | Immediate push after each commit |
| **Conflict Handling** | Fail-fast with `git pull --rebase` (1 attempt) |
| **Commit Message Format** | Structured with iteration #, score delta, improvements |

### 1.3 Existing Codebase Analysis

| System | Main Entry | Current Version Control | Integration Point |
|--------|-----------|------------------------|-------------------|
| **ai_co_scientist_agents** | `main.py:228` | None | After quality assessment |
| **ai_co_scientist_v2** | `mirror/engine.py:271` | `VersionController` class | In `_commit_iteration()` |
| **ai_co_scientist_glm4** | `main_ralp.py:424` | File-based state | After `phase_evaluate()` |

---

## 2. Architecture

### 2.1 Shared Module Pattern

```
shared/
├── __init__.py                  # Module marker
└── git_auto_commit.py           # GitAutoCommit class (400+ lines)
    ├── pre_flight_check()       # Validate repo state
    ├── commit_iteration()       # Main commit operation
    ├── _generate_commit_message()  # Structured messages
    ├── _stage_allowed_files()   # Selective staging
    └── _push_with_retry()       # Network error recovery
```

### 2.2 Integration Pattern

```
GitAutoCommit class
    ↓
    ├─→ ai_co_scientist_agents/main.py (direct import)
    ├─→ ai_co_scientist_v2/mirror/version_control.py (extension)
    └─→ ai_co_scientist_glm4/main_ralp.py (direct import)
```

### 2.3 Commit Decision Logic

```python
def should_commit(iteration, score, prev_score) -> bool:
    """Determine if commit should be created"""
    # Condition 1: Score improved
    if score > prev_score:
        return True
    
    # Condition 2: Every 3rd iteration (meta-learning checkpoint)
    if iteration % 3 == 0:
        return True
    
    return False
```

---

## 3. File Changes Summary

### 3.1 New Files (3)

| File | Lines | Purpose |
|------|-------|---------|
| `shared/__init__.py` | ~10 | Module marker, exports |
| `shared/git_auto_commit.py` | ~400 | Core GitAutoCommit class |
| `.gitattributes` | ~5 | Git LFS/config if needed |

### 3.2 Modified Files (5)

| File | Lines Changed | Purpose |
|------|---------------|---------|
| `ai_co_scientist_agents/main.py` | +30 | Import and call GitAutoCommit |
| `ai_co_scientist_v2/mirror/version_control.py` | +20 | Extend with git operations |
| `ai_co_scientist_v2/mirror/engine.py` | +15 | Pass commit info |
| `ai_co_scientist_glm4/main_ralp.py` | +25 | Import and call GitAutoCommit |
| `.gitignore` | +5 | Exclude workspace/, logs/, cache |

### 3.3 Dependency Updates (2)

| File | Change |
|------|--------|
| `ai_co_scientist_agents/requirements.txt` | Add `gitpython>=3.1.40` |
| `ai_co_scientist_glm4/requirements.txt` | Add `gitpython>=3.1.40` |

---

## 4. Task Breakdown

### Phase 1: Foundation (1 hour)

#### Task 1.1: Create Shared Module Structure

**File:** `shared/__init__.py`

```python
"""
Shared utilities for AI Co-Scientist systems.
"""

from .git_auto_commit import GitAutoCommit

__all__ = ['GitAutoCommit']
```

**Acceptance:** Module can be imported from any system directory

**Verification:**
```bash
python -c "from shared import GitAutoCommit; print('OK')"
```

---

### Phase 2: Core GitAutoCommit Implementation (4 hours)

#### Task 2.1: Implement GitAutoCommit Class Skeleton

**File:** `shared/git_auto_commit.py` (lines 1-100)

**Requirements:**
- Class constructor with `repo_path`, `branch`, `allowed_paths`
- Logger configuration
- Instance variables: `repo`, `branch`, `allowed_patterns`

**Acceptance:** Class instantiates without errors

#### Task 2.2: Implement Pre-Flight Checks

**File:** `shared/git_auto_commit.py` (lines 101-180)

**Method:** `pre_flight_check() -> Dict[str, Any]`

**Checks:**
1. Git repo exists and is valid
2. Not in detached HEAD state
3. On correct branch (`master`)
4. Working directory is clean (no uncommitted changes)
5. Remote is configured
6. PAT has write permissions (test push to dummy branch)

**Returns:**
```python
{
    'valid': bool,
    'branch': str,
    'remote': str,
    'clean': bool,
    'errors': List[str]
}
```

**Acceptance:** All checks pass on clean repo

**Verification:**
```bash
python -c "
from shared import GitAutoCommit
gac = GitAutoCommit('.')
result = gac.pre_flight_check()
assert result['valid'] == True
print('Pre-flight check passed')
"
```

#### Task 2.3: Implement Commit Message Generation

**File:** `shared/git_auto_commit.py` (lines 181-250)

**Method:** `_generate_commit_message(iteration, score, prev_score, improvements) -> str`

**Format:**
```
[Iteration 5] Score: 82.0 → 87.5 (+5.5)

Improvements:
- [HIGH] methodology: enhance_statistical_validation
- [MED] writing: improve_abstract_clarity

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

**Acceptance:** Message matches specification format

#### Task 2.4: Implement Selective File Staging

**File:** `shared/git_auto_commit.py` (lines 251-320)

**Method:** `_stage_allowed_files() -> bool`

**Allowed Patterns:**
- `submissions/**`
- `versions/**`
- `.omc/plans/**`

**Excluded:**
- `workspace/**`
- `logs/**`
- `.omc/state/**`
- `__pycache__/**`
- `*.pyc`

**Acceptance:** Only allowed files are staged

**Verification:**
```bash
# Create test files
touch submissions/test.txt
touch workspace/test.txt
python -c "
from shared import GitAutoCommit
gac = GitAutoCommit('.')
gac._stage_allowed_files()
import subprocess
result = subprocess.run(['git', 'diff', '--cached', '--name-only'], capture_output=True, text=True)
assert 'submissions/test.txt' in result.stdout
assert 'workspace/test.txt' not in result.stdout
print('Selective staging works')
"
```

#### Task 2.5: Implement Push with Retry

**File:** `shared/git_auto_commit.py` (lines 321-380)

**Method:** `_push_with_retry(max_retries=3, backoff_base=2) -> bool`

**Behavior:**
- Attempt push
- On network error: retry with exponential backoff
- On auth error: fail-fast (no retry)
- On conflict: attempt `git pull --rebase` once

**Acceptance:** Retries work, auth errors fail-fast

#### Task 2.6: Implement Main Commit Method

**File:** `shared/git_auto_commit.py` (lines 381-450)

**Method:** `commit_iteration(iteration, score, prev_score, improvements) -> CommitResult`

**Signature:**
```python
@dataclass
class CommitResult:
    success: bool
    commit_hash: str
    message: str
    pushed: bool
    error: Optional[str]
```

**Flow:**
1. Check if should commit (score improved or iteration % 3 == 0)
2. Stage allowed files
3. Generate commit message
4. Create commit
5. Push with retry
6. Return result

**Acceptance:** End-to-end commit succeeds

---

### Phase 3: Integration - ai_co_scientist_agents (1 hour)

#### Task 3.1: Add Import and Initialization

**File:** `ai_co_scientist_agents/main.py`

**Changes:**
1. Add import at top (after line 17):
```python
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from shared import GitAutoCommit
```

2. Initialize in `InfiniteLoopWorkflow.__init__()` (after line 87):
```python
# Git auto-commit
self.git_commit = GitAutoCommit(
    repo_path=str(Path(__file__).parent.parent),
    branch='master'
)
```

**Acceptance:** No import errors

#### Task 3.2: Add Pre-Flight Check

**File:** `ai_co_scientist_agents/main.py`

**Location:** In `run_infinite_loop()` before loop (after line 167)

**Code:**
```python
# Pre-flight git check
pre_flight = self.git_commit.pre_flight_check()
if not pre_flight['valid']:
    logger.error(f"Git pre-flight check failed: {pre_flight['errors']}")
    # Continue without git (non-blocking)
```

**Acceptance:** Check runs on startup

#### Task 3.3: Add Commit Call After Quality Assessment

**File:** `ai_co_scientist_agents/main.py`

**Location:** After score update (after line 211)

**Code:**
```python
# Auto-commit if score improved
prev_score = best_score - total_score  # Approximate
commit_result = self.git_commit.commit_iteration(
    iteration=iteration,
    score=total_score,
    prev_score=best_score if iteration > 1 else 0,
    improvements=improvement_areas
)
if commit_result.success:
    logger.info(f"Committed iteration {iteration}: {commit_result.commit_hash[:8]}")
```

**Acceptance:** Commit created after iteration

**Verification:**
```bash
cd ai_co_scientist_agents
python main.py --max-iterations 1
git log --oneline -1  # Should show new commit
```

---

### Phase 4: Integration - ai_co_scientist_v2 (1.5 hours)

#### Task 4.1: Extend VersionController with Git

**File:** `ai_co_scientist_v2/mirror/version_control.py`

**Changes:**
1. Add import (after line 12):
```python
import sys
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from shared import GitAutoCommit
```

2. Add to `__init__()` (after line 53):
```python
# Git integration
self.git_commit = GitAutoCommit(
    repo_path=str(self.repo_path.parent),
    branch='master'
)
```

**Acceptance:** VersionController instantiates with git

#### Task 4.2: Add Git Commit to Existing Commit Method

**File:** `ai_co_scientist_v2/mirror/version_control.py`

**Location:** In `commit()` method, after saving (after line 100)

**Code:**
```python
# Also commit to git
try:
    git_result = self.git_commit.commit_iteration(
        iteration=iteration,
    score=score,
    prev_score=self.commits[-1].score if self.commits else 0,
    improvements=improvements
)
    if git_result.success:
        logger.info(f"Git commit: {git_result.commit_hash[:8]}")
except Exception as e:
    logger.warning(f"Git commit failed: {e}")
```

**Acceptance:** Git commit happens alongside version commit

#### Task 4.3: Update Engine to Pass Score Info

**File:** `ai_co_scientist_v2/mirror/engine.py`

**Location:** In `_commit_iteration()` (modify line 271-283)

**Change:** Pass previous score from history

**Acceptance:** Previous score tracked correctly

---

### Phase 5: Integration - ai_co_scientist_glm4 (1 hour)

#### Task 5.1: Add Import and Initialization

**File:** `ai_co_scientist_glm4/main_ralp.py`

**Changes:**
1. Add import (after line 17):
```python
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from shared import GitAutoCommit
```

2. Initialize in `init_workspace()` (after line 65):
```python
# Git auto-commit
git_commit = GitAutoCommit(repo_path='.', branch='master')
```

**Acceptance:** No import errors

#### Task 5.2: Add Commit After Evaluation

**File:** `ai_co_scientist_glm4/main_ralp.py`

**Location:** In `phase_evaluate()`, after state update (after line 423)

**Code:**
```python
# Auto-commit
prev_score = state['best_score'] if state['iteration'] > 1 else 0
git_result = git_commit.commit_iteration(
    iteration=state['iteration'],
    score=total,
    prev_score=prev_score,
    improvements=[{'target': w['criterion'], 'action': w.get('improvement', 'improve'), 'priority': 'high'} for w in weaknesses]
)
if git_result.success:
    print(f"  Git committed: {git_result.commit_hash[:8]}")
```

**Acceptance:** Commit created after evaluation

---

### Phase 6: Configuration (0.5 hour)

#### Task 6.1: Update .gitignore

**File:** `.gitignore` (create if not exists)

**Content:**
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# Workspace
workspace/
logs/
*.log

# State
.omc/state/
.serena/cache/

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db
```

**Acceptance:** Git status shows clean for ignored files

#### Task 6.2: Create .gitattributes

**File:** `.gitattributes`

**Content:**
```
# Auto detect text files
* text=auto

# Linguist overrides
*.md linguist-language=Python
*.py linguist-detectable=true
```

**Acceptance:** File created

#### Task 6.3: Update Requirements Files

**Files:**
- `ai_co_scientist_agents/requirements.txt`
- `ai_co_scientist_glm4/requirements.txt`

**Add:**
```
# Git operations
gitpython>=3.1.40
```

**Acceptance:** Package installs successfully

---

## 5. Dependencies

### 5.1 Task Dependency Graph

```
Phase 1 (Foundation)
    ↓
Phase 2.1-2.6 (Core Implementation)
    ↓
    ├──→ Phase 3 (ai_co_scientist_agents)
    ├──→ Phase 4 (ai_co_scientist_v2)
    └──→ Phase 5 (ai_co_scientist_glm4)
    ↓
Phase 6 (Configuration)
```

### 5.2 Critical Path

```
Task 1.1 → Task 2.1 → Task 2.6 → Task 3.3 → VERIFICATION
```

**Minimum Viable Product:** Tasks 1.1, 2.1-2.6, 3.1-3.3 (single system integration)

---

## 6. Acceptance Criteria

### 6.1 Functional Requirements

| ID | Criterion | Verification |
|----|-----------|--------------|
| FR1 | Each iteration creates git commit with correct files | `git log --name-only` shows only allowed files |
| FR2 | Commit message includes iteration # and score delta | `git log -1` shows formatted message |
| FR3 | Push succeeds to remote | `git log origin/master --oneline` shows commit |
| FR4 | Error handling works (retry, fail-fast) | Simulate network/auth errors |
| FR5 | Pre-flight checks prevent bad states | Start in detached HEAD → error |
| FR6 | Git operations add < 5 seconds per iteration | Time measurement |

### 6.2 Non-Functional Requirements

| ID | Criterion | Target | Verification |
|----|-----------|--------|--------------|
| NFR1 | Network error retry | 3 attempts, exponential backoff | Code review + log check |
| NFR2 | Auth error handling | Fail-fast (no retry) | Code review |
| NFR3 | Conflict handling | Auto-rebase (1 attempt) | Simulate conflict |
| NFR4 | File exclusions | workspace/, logs/ never committed | Check git diff |

---

## 7. Testing Strategy

### 7.1 Unit Tests (Task 2.x)

**File:** `tests/test_git_auto_commit.py`

```python
import pytest
from shared import GitAutoCommit
from unittest.mock import patch, MagicMock

def test_pre_flight_check_clean_repo():
    """Pre-flight passes on clean repo"""
    gac = GitAutoCommit('.')
    result = gac.pre_flight_check()
    assert result['valid'] == True

def test_pre_flight_check_dirty_repo():
    """Pre-flight fails on dirty repo"""
    # Create uncommitted file
    Path('test.txt').write_text('test')
    gac = GitAutoCommit('.')
    result = gac.pre_flight_check()
    assert result['clean'] == False

@patch('subprocess.run')
def test_push_with_retry_network_error(mock_run):
    """Retry on network error"""
    mock_run.side_effect = [ConnectionError(), MagicMock(returncode=0)]
    gac = GitAutoCommit('.')
    result = gac._push_with_retry()
    assert result == True
    assert mock_run.call_count == 2

def test_commit_message_format():
    """Commit message follows specification"""
    gac = GitAutoCommit('.')
    msg = gac._generate_commit_message(
        iteration=5, score=87.5, prev_score=82.0,
        improvements=[{'priority': 'high', 'target': 'methodology', 'action': 'enhance'}]
    )
    assert '[Iteration 5]' in msg
    assert '82.0 → 87.5 (+5.5)' in msg
    assert '[HIGH]' in msg
```

**Run:** `pytest tests/test_git_auto_commit.py -v`

### 7.2 Integration Tests (Task 3.x-5.x)

**File:** `tests/test_integration.py`

```python
def test_agents_integration():
    """ai_co_scientist_agents creates commits"""
    os.chdir('ai_co_scientist_agents')
    # Run 1 iteration
    subprocess.run(['python', 'main.py', '--max-iterations', '1'])
    # Check git
    result = subprocess.run(['git', 'log', '--oneline', '-1'], capture_output=True)
    assert b'[Iteration 1]' in result.stdout

def test_v2_integration():
    """ai_co_scientist_v2 creates commits"""
    os.chdir('ai_co_scientist_v2')
    subprocess.run(['python', 'main.py', '--max-iterations', '1'])
    result = subprocess.run(['git', 'log', '--oneline', '-1'], capture_output=True)
    assert b'Submission Improvement' in result.stdout

def test_glm4_integration():
    """ai_co_scientist_glm4 creates commits"""
    os.chdir('ai_co_scientist_glm4')
    subprocess.run(['python', 'main_ralp.py'])
    result = subprocess.run(['git', 'log', '--oneline', '-1'], capture_output=True)
    assert b'Iteration' in result.stdout or b'Submission' in result.stdout
```

### 7.3 Manual Testing Checklist

- [ ] Run `ai_co_scientist_agents/main.py` for 3 iterations, verify 3 commits
- [ ] Check commit messages have correct format
- [ ] Verify only allowed files are in commits
- [ ] Test network recovery (disable internet, re-enable during run)
- [ ] Test conflict handling (create diverged history)
- [ ] Verify timing (git ops < 5 seconds)
- [ ] Check remote origin has all commits

---

## 8. Rollback Plan

### 8.1 Immediate Rollback (< 1 hour)

**If unit tests fail:**
```bash
# 1. Discard shared module changes
git checkout shared/

# 2. Revert integration changes
git checkout ai_co_scientist_agents/main.py
git checkout ai_co_scientist_v2/mirror/version_control.py
git checkout ai_co_scientist_glm4/main_ralp.py
```

### 8.2 Partial Rollback

**If one system integration fails:**
```bash
# Keep working systems, revert failing one
git checkout ai_co_scientist_agents/main.py  # Example
```

### 8.3 Complete Rollback

**If entire feature is broken:**
```bash
# Create rollback branch
git checkout -b rollback-auto-commit

# Revert to before implementation
git reset --hard HEAD~N  # N = number of implementation commits

# Notify team
```

### 8.4 Data Recovery

**Committed data is safe:**
- All commits are in git history
- Submissions/versions are tracked
- `.omc/plans/` is preserved

**To recover lost commits:**
```bash
git reflog
git checkout <commit-hash>
```

---

## 9. Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Commit success rate | 95%+ | (successful commits / total iterations) |
| Push success rate | 90%+ | (successful pushes / total commits) |
| Git operation time | < 5 sec | Time measurement in logs |
| Test coverage | 80%+ | pytest --cov |
| All systems integrated | 3/3 | Checklist |

---

## 10. Open Questions / Risks

| Question | Risk Level | Mitigation |
|----------|------------|------------|
| GitHub PAT expiration | MEDIUM | Document PAT refresh process |
| Network instability during contest | LOW | Local commits persist, push can retry |
| Conflicting parallel runs | LOW | Pre-flight check detects dirty state |
| Large file size in submissions | LOW | `.gitignore` excludes workspace/ |

---

## 11. Post-Implementation

### 11.1 Documentation Updates

- Update each system's README.md with git behavior
- Add `.omc/plans/auto-commit-implementation.md` completion notes
- Update CLAUDE.md files with git commands

### 11.2 Monitoring

After deployment:
```bash
# Monitor commits
git log --oneline --graph -10

# Check sync status
git status
git log origin/master..master
```

---

## 12. Sign-Off

**Implementation:** [ ] Pending  
**Code Review:** [ ] Pending  
**Testing:** [ ] Pending  
**Deployment:** [ ] Pending

---

**End of Implementation Plan**
