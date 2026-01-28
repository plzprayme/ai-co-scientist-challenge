# AI Co-Scientist Challenge Skill

## Metadata
- **name**: ai-co-scientist
- **description**: Execute AI Co-Scientist Challenge systems for automated scientific research
- **version**: 1.0.0
- **category**: research

## Trigger Patterns
- "run ai co-scientist"
- "execute research system"
- "start ai research"
- "ai scientist"
- "co-scientist"

## Systems

### 1. infinite-loop (Default)
- **Directory**: `ai_co_scientist_agents/`
- **Entry Point**: `main.py`
- **Description**: 8 specialized agents with infinite loop quality improvement
- **Best OMC Mode**: `ultrawork` (parallel agent execution)
- **Agents**: ResearchDirector, LiteratureReview, Hypothesis, DataAnalysis, PaperWriting, AILogging, Validation, QualityAssurance

### 2. mirror
- **Directory**: `ai_co_scientist_v2/`
- **Entry Point**: `main.py`
- **Description**: Meta-learning self-improving agent system with version control
- **Best OMC Mode**: `ralph` (infinite loop until quality target)
- **Features**: Double-loop learning, version tracking, diff analysis

### 3. ralp
- **Directory**: `ai_co_scientist_glm4/`
- **Entry Point**: `main_ralp.py`
- **Description**: GLM-4 model with Reflection-Agent Loop Pattern
- **Best OMC Mode**: `autopilot` (full autonomous execution)
- **Features**: GLM-4 integration, reflection loop, state persistence

## Usage Patterns

### Basic Execution
```bash
# Run default system (infinite-loop)
cd ai_co_scientist_agents && python3 main.py
```

### With OMC Modes (activated by keyword)
```bash
# Say: "ralph run ai co-scientist" (persistent until quality achieved)
cd ai_co_scientist_agents && python3 main.py --target-score 85

# Say: "ultrawork run ai co-scientist" (maximum parallelism)
cd ai_co_scientist_agents && python3 main.py

# Say: "autopilot run ai co-scientist" (fully autonomous)
cd ai_co_scientist_agents && python3 main.py
```

### Single Phase
```bash
# Run specific phase only
cd ai_co_scientist_agents && python3 main.py --phase literature
cd ai_co_scientist_agents && python3 main.py --phase hypothesis
cd ai_co_scientist_agents && python3 main.py --phase data_analysis
cd ai_co_scientist_agents && python3 main.py --phase writing
```

### With Options
```bash
# Set target score
cd ai_co_scientist_agents && python3 main.py --target-score 90

# Set max iterations
cd ai_co_scientist_agents && python3 main.py --max-iterations 15

# Start from specific phase
cd ai_co_scientist_agents && python3 main.py --start-from hypothesis
```

## Configuration

### Environment Variables (.env)
```
ANTHROPIC_API_KEY=sk-ant-xxxxx
OPENAI_API_KEY=sk-xxxxx
GOOGLE_API_KEY=xxxxx
ZHIPUAI_API_KEY=xxxxx
```

### Settings (config/settings.py)
```python
RESEARCH_TOPIC = "AI-driven methodology for enhancing scientific research"
RESEARCH_FIELD = "Bio"  # Bio, Materials, Chemistry, Earth Science, etc.
TARGET_DATE = "2026-01-31"
TARGET_SCORE = 85
```

## Output Files

### Directory Structure
```
outputs/
├── final_submission/
│   ├── research_paper.md      # Main research paper (English)
│   ├── ai_usage_report.md     # AI usage documentation
│   └── data_usage_list.md     # Data sources and licenses
├── literature_review/
├── hypothesis/
├── analysis_results/
├── paper/
├── ai_usage/
├── validation/
└── quality/
```

### Submission ZIP
- `outputs/submission_<timestamp>.zip`

## Workflow Phases

1. **init** - Initialize project, set research topic
2. **literature** - Search and analyze related papers
3. **hypothesis** - Generate hypotheses and experimental design
4. **data_analysis** - Collect and analyze data
5. **writing** - Write research paper in English
6. **ai_logging** - Compile AI usage report
7. **validation** - Validate results for reproducibility
8. **quality** - Assess against competition rubric (100 points)

## Quality Rubric

| Criterion | Points | Description |
|-----------|--------|-------------|
| Practicality | 20 | Research significance and value |
| Methodology | 20 | Clarity and scientific rigor |
| Data Quality | 25 | Logical, reliable, appropriate data |
| Conclusion | 10 | Scientific accuracy and evidence |
| Readability | 5 | Clear English communication |
| Creativity | 20 | Novel and differentiated approach |
| AI Contribution | P/F | Sufficient AI participation (3+ models) |

## Verification

### Health Check
```bash
# Check system can import
cd ai_co_scientist_agents && python3 -c "from agents.director import ResearchDirectorAgent; print('OK')"
```

### Dry Run
```bash
# Test single phase
cd ai_co_scientist_agents && python3 main.py --phase init
```

### Full Test
```bash
# Run with low target
cd ai_co_scientist_agents && python3 main.py --target-score 60 --max-iterations 2
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| API key errors | Check `.env` file exists and has valid keys |
| Import errors | Run `pip install -r requirements.txt` |
| State corruption | Delete `workspace/state.json` and restart |
| Token limits | Reduce `max_tokens` in config |
| Model unavailable | Fallback to alternative model |

## Integration Notes

This skill integrates with OMC through:
- Direct Python execution using `python3`
- OMC mode activation via keyword matching (say "ralph", "ultrawork", or "autopilot" with "run ai co-scientist")
- State persistence via system-specific state files
- Progress tracking through log files

## Quick Command

**The simplest way to run:**
```bash
cd ai_co_scientist_agents && python3 main.py
```

## Related Skills

- `research` - For parallel scientific research
- `tdd` - For test-driven development
- `writer` - For documentation generation
