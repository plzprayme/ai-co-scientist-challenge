# OMC Integration Plan for AI Co-Scientist Challenge System

**Plan ID:** omc-integration
**Generated:** 2026-01-29
**Status:** READY

---

## Context

### Original Request
The user wants to know how to use the AI Co-Scientist Challenge system with oh-my-claudecode (OMC) and wants a command to do so.

### Available Systems

The project contains **three independent AI co-scientist systems**:

| System | Directory | Description | Entry Point |
|--------|-----------|-------------|-------------|
| **Infinite Loop Agents** | `ai_co_scientist_agents/` | 8 specialized agents with infinite loop quality improvement | `main.py` |
| **MIRROR System** | `ai_co_scientist_v2/` | Meta-learning self-improving agent system with version control | `main.py` |
| **RALP + GLM-4** | `ai_co_scientist_glm4/` | GLM-4 model with RALP (Reflection-Agent Loop Pattern) | `main_ralp.py` |

### Existing Work (Acknowledged)

**ALREADY COMPLETE:**
1. `.omc/skills/ai-co-scientist.md` - OMC skill definition with triggers
2. `AGENTS.md` - Contains "OMC Integration Commands" section with all commands

**NOT NEEDED (per Architect analysis):**
- Wrapper scripts (OMC uses direct Python execution)
- State management integration (systems manage their own state)
- Custom command syntax (OMC loads skills via keyword matching)

---

## Work Objectives

### Core Objective
Ensure the user has a clear, working command to execute the AI Co-Scientist systems via OMC.

### Deliverables
1. Verified correct commands in skill file (if any corrections needed)
2. Clear summary for user

### Definition of Done
- User can execute AI Co-Scientist systems with documented commands
- All commands use correct syntax (python3, not python)
- All verification steps are testable

---

## Must Have / Must NOT Have

### Must Have
- Correct command syntax (python3 for execution)
- Testable verification steps
- Clear documentation of available options

### Must NOT Have
- Wrapper scripts (unnecessary per Architect)
- Custom state management (systems handle their own)
- Invalid command syntax (/ralph:cd ... is not valid OMC syntax)
- Non-existent command options (--phase option exists; --target-score needs verification)

---

## Task Flow and Dependencies

```
NO IMPLEMENTATION NEEDED

The skill file and AGENTS.md documentation already exist.
This plan focuses on VERIFICATION and CLARIFICATION only.

┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   User       │────▶│  AGENTS.md   │────▶│  Python      │
│  Question    │     │  Commands    │     │  Execution   │
└──────────────┘     └──────────────┘     └──────────────┘
```

---

## Detailed TODOs

### Task 1: Verify and Correct Skill File Commands

**File:** `.omc/skills/ai-co-scientist.md`

**Issues Found:**
1. Uses `python` instead of `python3`
2. OMC mode syntax `/ralph:cd ...` is NOT valid
3. Commands should be direct bash commands

**Acceptance Criteria:**
- All commands use `python3`
- Remove invalid OMC mode prefix syntax
- Commands are testable

**Required Changes:**
```markdown
# BEFORE (incorrect):
/ralph:cd ai_co_scientist_agents && python main.py --target-score 85
/ultrawork:cd ai_co_scientist_agents && python main.py

# AFTER (correct):
cd ai_co_scientist_agents && python3 main.py --target-score 85
cd ai_co_scientist_agents && python3 main.py
```

---

### Task 2: Verify AGENTS.md Commands

**File:** `AGENTS.md`

**Issues Found:**
1. Uses `python` instead of `python3`
2. OMC mode syntax `/ralph:cd ...` is NOT valid

**Acceptance Criteria:**
- All commands use `python3`
- Note: OMC modes are activated via keywords, not command prefixes

**Required Changes:**
```markdown
# BEFORE (incorrect):
/ralph:cd ai_co_scientist_agents && python main.py --target-score 85

# AFTER (correct):
# To use with OMC ralph mode, say: "ralph run ai co-scientist"
# Direct command:
cd ai_co_scientist_agents && python3 main.py --target-score 85
```

---

### Task 3: Verification Steps

**Acceptance Criteria:**
- Each verification command is testable
- Commands use correct Python interpreter

**Verification Commands:**
```bash
# Health check - verify imports
cd ai_co_scientist_agents && python3 -c "from agents.director import ResearchDirectorAgent; print('OK')"

# Dry run - test single phase
cd ai_co_scientist_agents && python3 main.py --phase init

# Full test with low target
cd ai_co_scientist_agents && python3 main.py --target-score 60 --max-iterations 1
```

---

## Command Reference (Corrected)

### Quick Start - The Command You Need

```bash
# Run the 8-agent infinite loop system (recommended)
cd ai_co_scientist_agents && python3 main.py
```

### All Three Systems

| System | Command | Description |
|--------|---------|-------------|
| **8-Agent System** | `cd ai_co_scientist_agents && python3 main.py` | 8 specialized agents, comprehensive workflow |
| **MIRROR** | `cd ai_co_scientist_v2 && python3 main.py` | Meta-learning with self-improvement |
| **RALP + GLM-4** | `cd ai_co_scientist_glm4 && python3 main_ralp.py` | GLM-4 with reflection loop |

### With Options

```bash
# Set target quality score (8-agent system)
cd ai_co_scientist_agents && python3 main.py --target-score 90

# Set maximum iterations
cd ai_co_scientist_agents && python3 main.py --max-iterations 15

# Start from specific phase
cd ai_co_scientist_agents && python3 main.py --start-from hypothesis

# Run single phase only
cd ai_co_scientist_agents && python3 main.py --phase literature
cd ai_co_scientist_agents && python3 main.py --phase hypothesis
cd ai_co_scientist_agents && python3 main.py --phase data_analysis
cd ai_co_scientist_agents && python3 main.py --phase writing
```

### Using OMC Modes

**Note:** OMC modes are activated by KEYWORD, not command prefix.

```bash
# Ralph mode - say: "ralph run ai co-scientist"
# Ultrawork mode - say: "ultrawork run ai co-scientist"
# Autopilot mode - say: "autopilot run ai co-scientist"
```

The skill file `.omc/skills/ai-co-scientist.md` contains trigger patterns that activate on these keywords.

---

## Output Locations

After execution, find submission files in:
- `ai_co_scientist_agents/outputs/final_submission/research_paper.md`
- `ai_co_scientist_agents/outputs/final_submission/ai_usage_report.md`
- `ai_co_scientist_agents/outputs/final_submission/data_usage_list.md`
- `ai_co_scientist_agents/outputs/submission_<timestamp>.zip`

---

## Success Criteria

| Criterion | Test | Success Threshold |
|-----------|------|-------------------|
| Import Check | `python3 -c "from agents.director import ResearchDirectorAgent"` | No ImportError |
| Dry Run | `python3 main.py --phase init` | Exit code 0 |
| Full Execution | `python3 main.py --target-score 60 --max-iterations 1` | Creates outputs |

---

## Summary

### What This Plan Does

1. **Corrects** command syntax in documentation (python -> python3)
2. **Removes** invalid OMC mode prefix syntax
3. **Provides** clear, testable commands

### What This Plan Does NOT Do

1. **Does NOT create wrapper scripts** - Not needed (Architect finding)
2. **Does NOT implement state management** - Systems handle their own state
3. **Does NOT add complex integration** - Direct execution is sufficient

### For the User

**The simplest command to run the AI Co-Scientist system:**

```bash
cd ai_co_scientist_agents && python3 main.py
```

**To use with OMC's persistent execution mode:**

Say: "ralph run ai co-scientist"

This triggers the skill via keyword matching in `.omc/skills/ai-co-scientist.md`.

---

**Plan Status:** READY FOR IMPLEMENTATION

**Next Action:** Execute the plan to correct documentation files
