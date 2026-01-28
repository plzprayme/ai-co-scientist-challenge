# MIRROR System 9999 Iteration Run - Setup Guide

**Status:** ⚠️ **BLOCKED - Environment Limitations**

---

## 🚫 Current Blockers

### 1. No pip3 / No Package Manager
```
❌ pip3 command not found
❌ python3 -m pip not available  
❌ No sudo access (uid=1000, not root)
```

**Impact:** Cannot install numpy, pandas, anthropic, openai, gitpython, arxiv

### 2. Missing Python Dependencies
```
Required: numpy>=1.24.0, pandas>=2.0.0, gitpython>=3.1.40, anthropic, openai, arxiv
Installed: NONE
```

**Impact:** MIRROR system cannot start

### 3. Resource Concerns for 9999 Iterations
```
Estimated Git Commits: ~3333 (every 3 iterations)
Estimated Log Size: ~100MB+
Estimated Runtime: Days to weeks
Estimated API Calls: ~30,000 (if using real APIs)
```

**Impact:** System may exhaust resources, hit rate limits

---

## ✅ Solution: Manual Setup Required

### Step 1: Install System Dependencies

**Run these commands in your WSL terminal:**

```bash
# Update package list
sudo apt-get update

# Install pip and virtualenv
sudo apt-get install -y python3-pip python3-venv python3-dev

# Verify installation
python3 -m pip --version
```

### Step 2: Install Python Dependencies

```bash
cd ai_co_scientist_v2

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install requirements
pip install --upgrade pip
pip install -r requirements.txt

# Verify installation
python -c "import numpy, pandas, git; print('All OK')"
```

### Step 3: Configure API Keys (Optional)

If using real Anthropic/OpenAI APIs:

```bash
# Set environment variables
export ANTHROPIC_API_KEY="your_key_here"
export OPENAI_API_KEY="your_key_here"

# Or create .env file
cat > .env << ENVEOF
ANTHROPIC_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here
ENVEOF
```

### Step 4: Run MIRROR System

```bash
# Activate virtual environment
source venv/bin/activate

# Run with safety limits
python main.py --max-iterations 100 --target-score 90

# Or run full 9999 (after testing)
python main.py --max-iterations 9999 --target-score 100
```

---

## 🎯 Recommended Approach

### Phase 1: Test Run (10 iterations)
```bash
source venv/bin/activate
python main.py --max-iterations 10
```

**Verify:**
- System starts without errors
- Iterations complete successfully
- Git commits are created
- Logs are written

### Phase 2: Medium Run (100 iterations)
```bash
python main.py --max-iterations 100
```

**Monitor:**
- Memory usage: `htop` or `top`
- Disk usage: `df -h`
- Git log: `git log --oneline | wc -l`

### Phase 3: Full Run (9999 iterations)
```bash
# Run in background with logging
nohup python main.py --max-iterations 9999 > mirror_run.log 2>&1 &

# Monitor progress
tail -f mirror_run.log

# Check git commits
git log --oneline | tail -10
```

---

## ⚠️ Important Warnings

### Resource Management

**Disk Space:**
- 9999 iterations × ~3 iterations/commit = ~3333 commits
- Estimated repository growth: 500MB - 2GB
- **Monitor**: `df -h` before and during run

**Memory:**
- Monitor for leaks: `watch -n 10 'ps aux | grep python'`
- Set ulimit: `ulimit -v 8388608` (8GB limit)

**Git Performance:**
- 3333 commits may slow down git operations
- Consider periodic squashing or shallow clones

### API Rate Limits

If using real Anthropic/OpenAI APIs:
- 9999 iterations × 3 judges = ~30,000 API calls
- **Likely to hit rate limits**
- **Solution**: Implement caching, use mock agents, or get increased limits

### Run Duration

**Estimates:**
- Fast iteration (30s): 9999 × 30s = ~83 hours
- Medium iteration (2min): 9999 × 2min = ~333 hours (14 days)
- Slow iteration (5min): 9999 × 5min = ~833 hours (35 days)

**Recommendation:** Start with test runs to gauge actual iteration speed

---

## 🔧 Alternative Approaches

### Option 1: Use Mock Agents (Fastest)
- Edit `main.py` to use mock agents with fixed outputs
- Completes iterations in seconds
- Good for testing git commit logic

### Option 2: Reduce Commit Frequency
- Modify `shared/git_auto_commit.py`
- Change from every 3 iterations to every 100
- Reduces git commits from 3333 to ~100

### Option 3: Use Checkpoint Branch
- Create branch: `long-run-$(date +%Y-%m-%d)`
- Squash commits periodically
- Keep master clean

### Option 4: Cloud Environment
- Use Google Colab Pro (has GPUs, pre-installed libraries)
- Use AWS/Azure/GCP with proper resource allocation
- Better for long-running compute tasks

---

## 📋 Pre-Flight Checklist

Before running 9999 iterations:

- [ ] Install python3-pip and python3-venv
- [ ] Create and activate virtual environment
- [ ] Install all requirements.txt dependencies
- [ ] Configure API keys (if using real APIs)
- [ ] Verify git auto-commit is working (test with 3 iterations)
- [ ] Check disk space (recommend 20GB+ free)
- [ ] Set up log rotation (prevent disk exhaustion)
- [ ] Monitor system resources (htop, iotop)
- [ ] Test run with 10 iterations first
- [ ] Test run with 100 iterations
- [ ] Verify checkpoint/resume functionality
- [ ] Set up process monitoring (systemd, supervisor, or tmux)

---

## 🎯 Current Status

```
✅ Code: Implemented and ready
✅ Git auto-commit: Integrated  
✅ Documentation: Complete
❌ Environment: NOT READY
❌ Dependencies: MISSING
❌ Execution: CANNOT START
```

---

## 📞 Next Steps

**User Action Required:**

1. Open WSL terminal
2. Run: `sudo apt-get install python3-pip python3-venv`
3. Run: `cd ai_co_scientist_v2 && python3 -m venv venv`
4. Run: `source venv/bin/activate && pip install -r requirements.txt`
5. Run: `python main.py --max-iterations 10` (test)
6. If test succeeds: `python main.py --max-iterations 9999`

---

## 📊 Success Metrics

After setup, successful run will show:
- Iterations completing without errors
- Scores improving or stabilizing
- Git commits appearing in log
- Reasonable memory usage (<2GB)
- Disk usage growing slowly

**Monitor Command:**
```bash
# Watch git commits
watch -n 10 "git log --oneline | wc -l"

# Watch disk usage
watch -n 60 "df -h ."

# Watch process
watch -n 5 "ps aux | grep 'python main.py'"
```

---

**Generated:** 2026-01-29  
**Status:** Ready for user to execute setup
