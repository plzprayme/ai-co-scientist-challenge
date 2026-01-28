# Auto-Commit Requirements Specification

## Decisions Based on Context

### Priority 0: Blocking Questions (Resolved)

**1. What specifically should be committed?**
- **Decision:** Iteration outputs only
  - `submissions/` directory (versioned submission artifacts)
  - `versions/` directory (commit logs, CHANGELOG)
  - `.omc/plans/` (RALP plans if generated)
  - Excluded: `workspace/`, `.omc/state/`, cache, logs

**2. Should commits happen before or after validation?**
- **Decision:** AFTER scoring improvement
  - Only commit if score improves OR iteration % 3 == 0 (meta-learning checkpoint)
  - Failed iterations don't pollute git history
  - Commit message includes score delta

**3. Target branch and push behavior?**
- **Decision:** `master` branch, immediate push
  - Every commit pushes immediately
  - No batching (history should be linear)
  - If remote ahead: `git pull --rebase` before push

**4. Handle merge conflicts?**
- **Decision:** Fail-fast with clear error
  - Single-instance assumption (no parallel runs)
  - If conflict detected: halt and notify user
  - Automatic retry: `git pull --rebase` (max 1 attempt)

**5. Commit message format?**
- **Decision:** Match existing VersionController style
  ```
  [Iteration 5] Score: 82.0 → 87.5 (+5.5)
  
  Improvements:
  - [HIGH] methodology: enhance_statistical_validation
  - [MED] writing: improve_abstract_clarity
  
  Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
  ```

## Functional Requirements

### FR1: Auto-Commit on Iteration
- Git adds modified files from allowed list
- Creates commit with standard message format
- Pushes to remote immediately
- Logs commit hash for verification

### FR2: Error Recovery
- Retries with backoff (network errors)
- Fails fast with clear message (auth errors)
- Attempts rebase (conflicts)

### FR3: State Validation
- Verifies git repo is clean on startup
- Checks not in detached HEAD state
- Validates PAT write permissions

### FR4: Selective Commits
- Only includes allowed patterns
- Excludes cache, logs, workspace
- Skips if no actual changes

## Acceptance Criteria

1. ✅ Each iteration creates git commit with correct files
2. ✅ Commit message includes iteration number and score delta
3. ✅ Push succeeds to remote (verified via git log)
4. ✅ Error handling works (retry, fail-fast)
5. ✅ Pre-flight checks prevent bad states
6. ✅ Git operations add < 5 seconds per iteration
