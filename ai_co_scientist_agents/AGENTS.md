<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-01-29 | Updated: 2026-01-29 -->

# ai_co_scientist_agents

## Purpose

**무한루프 에이전트 시스템 (Infinite Loop Agent System)** - AI 활용 과학기술 연구 수행 및 연구보고서 작성을 위한 자동화 시스템입니다.

8개의 전문 에이전트가 연구 전 과정을 담당하며, 무한루프 워크플로우를 통해 품질 기준 충족까지 자동 반복합니다.

## Key Files

| File | Description |
|------|-------------|
| `main.py` | 메인 실행 스크립트 - 전체 워크플로우 조율 |
| `requirements.txt` | Python 의존성 목록 |
| `README.md` | 프로젝트 개요 및 사용 가이드 |
| `CLAUDE.md` | AI 에이전트를 위한 프로젝트 가이드 |
| `test_workflow.py` | 워크플로우 통합 테스트 |

## Subdirectories

| Directory | Purpose |
|-----------|---------|
| `agents/` | 8개 전문 에이전트 구현 (연구 총괄, 문헌, 가설, 데이터, 작성, 로깅, 검증, 품질) |
| `config/` | 설정 파일 (settings.py) |
| `outputs/` | 산출물 저장소 (논문, 데이터, AI 활용 로그 등) |
| `logs/` | 실행 로그 및 AI 상호작용 기록 |

## For AI Agents

### Working In This Directory

이 시스템은 **8개의 전문화된 에이전트**가 협력하여 연구를 수행합니다:

#### Agent Pipeline

```
1. ResearchDirectorAgent (연구 총괄)
   ↓
2. LiteratureReviewAgent (문헌 조사)
   ↓
3. HypothesisAgent (가설 생성)
   ↓
4. DataAnalysisAgent (데이터 분석)
   ↓
5. PaperWritingAgent (논문 작성)
   ↓
6. AILoggingAgent (AI 활용 로깅)
   ↓
7. ValidationAgent (검증)
   ↓
8. QualityAssuranceAgent (품질 보증)
   ↓
   [품질 기준 충족?] → NO: 무한루프 반복
                      → YES:  완료
```

### Running the System

```bash
# 전체 워크플로우 실행
python main.py

# 특정 Phase만 실행
python main.py --phase literature
python main.py --phase hypothesis
python main.py --phase data_analysis
python main.py --phase writing

# 특정 Phase부터 실행
python main.py --start-from hypothesis

# 품질 기준 설정 (기본값: 85점)
python main.py --target-score 90

# 최대 반복 횟수 설정
python main.py --max-iterations 15
```

### Testing

```bash
# 워크플로우 테스트
python test_workflow.py

# 단위 테스트
python -m pytest tests/

# 특정 에이전트 테스트
python -m pytest tests/test_agents.py
```

### Common Patterns

#### 에이전트 실행 패턴

```python
from agents.director import ResearchDirectorAgent
from agents.literature import LiteratureReviewAgent

# 에이전트 초기화
director = ResearchDirectorAgent()
literature_agent = LiteratureReviewAgent()

# 작업 실행
result = literature_agent.conduct_review()

# 결과 확인
print(result['papers_found'])
print(result['research_gaps'])
```

#### 설정 패턴

```python
from config.settings import RESEARCH_TOPIC, TARGET_SCORE

# 설정 사용
print(f"Research Topic: {RESEARCH_TOPIC}")
print(f"Target Score: {TARGET_SCORE}")
```

#### 로깅 패턴

```python
import logging

logger = logging.getLogger(__name__)
logger.info("Starting literature review")
logger.debug(f"Found {len(papers)} papers")
```

### Code Style

- **PEP 8** 준수
- **Type hints** 사용 (PEP 484)
- **Docstring** Google style
- **의존성 주입** 패턴 사용

### Configuration

`config/settings.py`에서 연구 설정을 관리합니다:

```python
# 연구 주제 설정
RESEARCH_TOPIC = "Your Research Topic"
RESEARCH_FIELD = "materials_chemistry"  # 7대 분야 중 선택

# 품질 기준
TARGET_SCORE = 85  # 목표 점수 (0-100)
MAX_ITERATIONS = 15  # 최대 반복 횟수

# API 설정 (환경 변수에서 로드)
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
```

## Dependencies

### Internal

- `agents/` - 각 에이전트 모듈
- `config/` - 설정 관리

### External

- **anthropic** (>=0.18.0) - Claude API
- **openai** (>=1.0.0) - GPT-4 API
- **pydantic** (>=2.0.0) - 데이터 검증
- **python-dotenv** (>=1.0.0) - 환경 변수
- **requests** (>=2.31.0) - HTTP 요청
- **arxiv** (>=2.0.0) - arXiv 논문 검색
- **scholarly** (>=1.0.0) - Google Scholar 검색

## Output Structure

```
outputs/
├── literature_review/       # 문헌 조사 결과
│   ├── papers.json
│   └── research_gaps.md
├── hypothesis/              # 가설 및 실험 설계
│   ├── hypothesis.md
│   └── experimental_design.md
├── analysis_results/        # 데이터 분석 결과
│   ├── data.csv
│   ├── analysis.py
│   └── figures/
├── paper/                   # 연구보고서
│   └── research_paper.md
├── ai_usage/                # AI 활용보고서
│   ├── ai_usage_report.md
│   └── interaction_logs/
├── validation/              # 검증 결과
│   └── validation_report.md
└── quality/                 # 품질 평가
    └── quality_report.md
```

## Quality Criteria System

심사 기준 기반 자가 평가 시스템:

| 항목 | 배점 | 평가 기준 |
|------|------|-----------|
| 주제의 실용성 | 20점 | 연구의 유의미성, 사회적·학문적 가치 |
| 방법론의 적절성 | 20점 | 방법론 명확성, 과학적 기준 부합 |
| 데이터의 적절성 | 25점 | 논리적 결과, 신뢰성, 명확한 결론 |
| 결론의 합리성 | 10점 | 과학적 사실 부합, 입증 여부 |
| 전달력 및 가독성 | 5점 | 명확한 전달, 이해 가능한 구성 |
| 연구의 창의성 및 참신성 | 20점 | 차별화된 접근, AI 활용 참신성 |
| **합계** | **100점** | **목표: 85점 이상** |

## AI Usage Logging

모든 AI 상호작용은 자동으로 기록됩니다:

```markdown
## Interaction Log

### Timestamp: 2026-01-29 10:30:00
### Model: claude-3-5-sonnet-20241022
### Task: Literature Review - Search Query Generation

#### Prompt:
[프롬프트 내용]

#### Response:
[응답 내용]

#### Usage:
- Tokens Used: 150/280
- Research Phase: Literature Review
- Contribution Level: High
```

## Infinite Loop Mechanism

```python
while True:
    # 1. 연구 수행
    research_result = conduct_research()

    # 2. 품질 평가
    quality_score = evaluate_quality(research_result)

    # 3. 기준 충족 확인
    if quality_score >= TARGET_SCORE:
        print("Quality criteria met!")
        break

    # 4. 반복 횟수 확인
    if iteration >= MAX_ITERATIONS:
        print("Max iterations reached")
        break

    # 5. 피드백 기반 개선
    improve_submission(research_result, quality_score)

    iteration += 1
```

<!-- MANUAL: -->
