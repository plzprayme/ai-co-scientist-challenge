<!-- Generated: 2026-01-29 | Updated: 2026-01-29 -->

# ai-co-scientist-challenge

## Purpose

2026 AI Co-Scientist Challenge Korea - Track 1 참가를 위한 **AI 활용 과학기술 연구 수행 및 연구보고서 작성 자동화 시스템**입니다.

이 프로젝트는 AI 에이전트 시스템을 통해 과학기술 연구의 전 과정(문헌 조사, 가설 생성, 실험 설계, 데이터 분석, 논문 작성)을 자동화하고, 무한루프 메커니즘을 통해 제출물의 품질을 지속적으로 개선합니다.

## Key Files

| File | Description |
|------|-------------|
| `ai_co_scientist_agent_system.md` | 대회 정보 요약 및 무한루프 에이전트 시스템 설계 문서 (한글) |
| `claude_code_zai_env.sh` | Claude Code 실행 환경 설정 스크립트 |
| `.mcp.json` | Model Context Protocol 서버 설정 |

## Subdirectories

| Directory | Purpose |
|-----------|---------|
| `ai_co_scientist_agents/` | 기본 무한루프 에이전트 시스템 (8개 전문 에이전트) |
| `ai_co_scientist_v2/` | MIRROR 시스템 - 메타러닝 기반 자기개선 무한루프 에이전트 |
| `ai_co_scientist_glm4/` | GLM-4 모델 통합 및 RALP 래퍼 구현 |

## For AI Agents

### Working In This Directory

이 프로젝트는 **3개의 독립적인 시스템**으로 구성되어 있습니다:

1. **ai_co_scientist_agents/** - 기본 시스템
   - 8개의 전문화된 에이전트가 연구 워크플로우를 수행
   - 무한루프로 품질 기준 충족까지 자동 반복
   - 심사 기준 기반 자가 평가 시스템

2. **ai_co_scientist_v2/** - 고급 시스템 (MIRROR)
   - 메타러닝 기반 이중 루프 학습
   - 에이전트 시스템 자체를 자동 개선
   - 버전 관리 및 diff 추적

3. **ai_co_scientist_glm4/** - GLM-4 통합
   - 중국어 GLM-4 모델 활용
   - RALP (Reflection-Agent Loop Pattern) 구현

### System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AI Co-Scientist 무한루프 에이전트 시스템                    │
└─────────────────────────────────────────────────────────────────────────────┘

    ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
    │   Research   │────▶│   Planning   │────▶│  Execution   │
    │   Agent      │     │   Agent      │     │   Agent      │
    └──────────────┘     └──────────────┘     └──────────────┘
           ▲                                          │
           │                                          ▼
    ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
    │   Review     │◀────│   Analysis   │◀────│  Validation  │
    │   Agent      │     │   Agent      │     │   Agent      │
    └──────────────┘     └──────────────┘     └──────────────┘
```

### Testing Requirements

각 시스템은 독립적으로 실행 가능합니다:

```bash
# 시스템 1: 기본 에이전트 시스템
cd ai_co_scientist_agents
python main.py

# 시스템 2: MIRROR 시스템
cd ai_co_scientist_v2
python main.py

# 시스템 3: GLM-4 통합
cd ai_co_scientist_glm4
python main_ralp.py
```

### Common Patterns

- **Python 3.8+** 사용
- **Type hints** 필수 (PEP 484)
- **Docstring** Google style
- **의존성 관리**: requirements.txt 사용
- **설정 관리**: config/settings.py 또는 config.yaml

## Competition Context

### Track 1: AI 활용 과학기술 연구 수행 및 연구보고서 작성

**제출 마감**: 2026년 1월 31일(토) 18:00

**심사 기준 (100점)**:
- 주제의 실용성 (20점)
- 방법론의 적절성 (20점)
- 데이터의 적절성 (25점)
- 결론의 합리성 (10점)
- 전달력 및 가독성 (5점)
- 연구의 창의성 및 참신성 (20점)
- AI 연구기여도 (Pass/Fail) - **3개 이상 AI 모델 활용 필수**

**7대 지정주제 분야**:
1. 바이오 (Bio)
2. 재료·화학 (Materials & Chemistry)
3. 지구과학 (Earth Science)
4. 반도체·디스플레이 (Semiconductor & Display)
5. 이차전지 (Secondary Battery)
6. 에너지 (Energy)
7. 수학 (Mathematics)

## Dependencies

### External (Python)

- **anthropic** - Claude API 클라이언트
- **openai** - GPT-4 API 클라이언트
- **zhipuai** - GLM-4 API 클라이언트
- **pydantic** - 데이터 검증
- **python-dotenv** - 환경 변수 관리
- **requests** - HTTP 요청

### External (AI Models)

- **Claude 3.5 Sonnet** (Anthropic)
- **GPT-4** (OpenAI)
- **Gemini Pro** (Google)
- **GLM-4** (Zhipu AI)

## Research Workflow

### 1. Literature Review
- 논문 검색 (arXiv, Google Scholar)
- Research Gap 식별
- 관련 연구 정리

### 2. Hypothesis Generation
- 가설 생성
- 실험 설계
- 방법론 수립

### 3. Data Analysis
- 데이터 수집
- 통계 분석
- 시각화

### 4. Paper Writing
- 영문 연구보고서 작성
- 논문 형식 준수
- 참고문헌 정리

### 5. Quality Assurance
- 심사 기준 기반 자가 평가
- 3개 AI Judge 평가
- 피드백 기반 개선

### 6. AI Usage Logging
- 모든 AI 상호작용 기록
- 프롬프트와 응답 저장
- AI 기여도 평가

## Submission Deliverables

1. **연구보고서** (research_paper.md)
   - 논문 형태, 영문 작성
   - Abstract: 250-300 words
   - Keywords: 3-5개

2. **AI 활용보고서** (ai_usage_report.md)
   - URL 목록
   - AI 상호작용 로그
   - 체크리스트
   - AI 기여도 자체 평가 (50%+)

3. **활용 데이터 목록** (data_usage_list.md)
   - 공개 데이터 정보
   - 생성/수집 데이터 정보
   - 라이선스 정보

<!-- MANUAL: -->

## OMC Integration Commands

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

### With OMC Modes (Keyword Activation)

**Note:** OMC modes are activated by KEYWORD, not command prefix. Say these phrases to activate modes:

```bash
# Ralph mode - say: "ralph run ai co-scientist"
# (Don't stop until quality target achieved)
cd ai_co_scientist_agents && python3 main.py --target-score 85

# Ultrawork mode - say: "ultrawork run ai co-scientist"
# (Parallel agent execution)
cd ai_co_scientist_agents && python3 main.py

# Autopilot mode - say: "autopilot run ai co-scientist"
# (Fully autonomous from idea to completion)
cd ai_co_scientist_agents && python3 main.py
```

### Single Phase Execution

```bash
cd ai_co_scientist_agents && python3 main.py --phase literature
cd ai_co_scientist_agents && python3 main.py --phase hypothesis
cd ai_co_scientist_agents && python3 main.py --phase data_analysis
cd ai_co_scientist_agents && python3 main.py --phase writing
```

### Options

```bash
# Set target quality score
cd ai_co_scientist_agents && python3 main.py --target-score 90

# Set maximum iterations
cd ai_co_scientist_agents && python3 main.py --max-iterations 15

# Start from specific phase
cd ai_co_scientist_agents && python3 main.py --start-from hypothesis
```

### Output

After execution, find submission files in:
- `outputs/final_submission/research_paper.md`
- `outputs/final_submission/ai_usage_report.md`
- `outputs/final_submission/data_usage_list.md`
- `outputs/submission_<timestamp>.zip`
