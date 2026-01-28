# AI Co-Scientist Challenge - Quick Command Reference

**Generated:** 2026-01-29

## The One Command You Need

```bash
# Run the infinite loop agent system (recommended for most users)
cd ai_co_scientist_agents && python main.py
```

---

## All Three Systems

| System | Command | Best For |
|--------|---------|----------|
| **8-Agent Infinite Loop** | `cd ai_co_scientist_agents && python main.py` | General research, comprehensive workflow |
| **MIRROR (Meta-Learning)** | `cd ai_co_scientist_v2 && python main.py` | Self-improving research with version tracking |
| **RALP + GLM-4** | `cd ai_co_scientist_glm4 && python main_ralp.py` | GLM-4 model with reflection loop |

---

## With OMC Modes

```bash
# Ralph mode - don't stop until quality target achieved
/ralph:cd ai_co_scientist_agents && python main.py --target-score 85

# Ultrawork mode - parallel agent execution
/ultrawork:cd ai_co_scientist_agents && python main.py

# Autopilot mode - fully autonomous
/autopilot:cd ai_co_scientist_agents && python main.py
```

---

## Single Phase Execution

```bash
# Run only specific phases
cd ai_co_scientist_agents && python main.py --phase literature
cd ai_co_scientist_agents && python main.py --phase hypothesis
cd ai_co_scientist_agents && python main.py --phase data_analysis
cd ai_co_scientist_agents && python main.py --phase writing
cd ai_co_scientist_agents && python main.py --phase validation
cd ai_co_scientist_agents && python main.py --phase quality
```

---

## Options

```bash
# Set target quality score
python main.py --target-score 90

# Set maximum iterations
python main.py --max-iterations 15

# Start from specific phase
python main.py --start-from hypothesis
```

---

## Output Files

After execution, submission files are in:
- `outputs/final_submission/research_paper.md`
- `outputs/final_submission/ai_usage_report.md`
- `outputs/final_submission/data_usage_list.md`
- `outputs/submission_<timestamp>.zip`

---

## Requirements

```bash
# Install dependencies
cd ai_co_scientist_agents && pip install -r requirements.txt

# Set environment variables (create .env file)
ANTHROPIC_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here
```
