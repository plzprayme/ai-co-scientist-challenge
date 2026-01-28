<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-01-29 | Updated: 2026-01-29 -->

# agents

## Purpose

8개의 전문화된 AI 에이전트 구현 - 각 에이전트는 연구 워크플로우의 특정 단계를 담당합니다.

각 에이전트는 독립적으로 실행 가능하며, 파이프라인을 통해 연결됩니다.

## Key Files

| File | Description |
|------|-------------|
| `__init__.py` | 에이전트 패키지 초기화 및 에이전트 팩토리 |
| `director.py` | ResearchDirectorAgent - 연구 총괄 및 워크플로우 조율 |
| `literature.py` | LiteratureReviewAgent - 문헌 조사 및 Research Gap 식별 |
| `hypothesis.py` | HypothesisAgent - 가설 생성 및 실험 설계 |
| `data_analysis.py` | DataAnalysisAgent - 데이터 수집 및 통계 분석 |
| `paper_writing.py` | PaperWritingAgent - 영문 연구보고서 작성 |
| `ai_logging.py` | AILoggingAgent - AI 활용 로깅 및 기여도 평가 |
| `validation.py` | ValidationAgent - 재현성 및 통계적 검증 |
| `quality.py` | QualityAssuranceAgent - 심사 기준 기반 자가 평가 |

## Subdirectories

이 디렉토리에는 하위 디렉토리가 없습니다.

## For AI Agents

### Agent Pipeline Flow

```
1. ResearchDirectorAgent (연구 총괄)
   ├─ 프로젝트 관리
   ├─ 진행 상황 추적
   └─ 에이전트 간 조율
   ↓
2. LiteratureReviewAgent (문헌 조사)
   ├─ arXiv, Google Scholar 검색
   ├─ 논문 요약 및 분류
   └─ Research Gap 식별
   ↓
3. HypothesisAgent (가설 생성)
   ├─ 가설 생성
   ├─ 실험 설계
   └─ 방법론 수립
   ↓
4. DataAnalysisAgent (데이터 분석)
   ├─ 데이터 수집
   ├─ 통계 분석
   ├─ 시각화
   └─ 결과 해석
   ↓
5. PaperWritingAgent (논문 작성)
   ├─ Abstract 작성
   ├─ Introduction 작성
   ├─ Methodology 작성
   ├─ Results 작성
   ├─ Discussion 작성
   └─ Conclusion 작성
   ↓
6. AILoggingAgent (AI 활용 로깅)
   ├─ 모든 AI 상호작용 기록
   ├─ 프롬프트와 응답 저장
   └─ AI 기여도 평가
   ↓
7. ValidationAgent (검증)
   ├─ 재현성 확인
   ├─ 통계적 검증
   └─ 코드 검증
   ↓
8. QualityAssuranceAgent (품질 보증)
   ├─ 심사 기준 기반 평가
   ├─ 3개 AI Judge 평가
   └─ 피드백 생성
   ↓
   [품질 기준 충족?] → NO: 무한루프 반복
                      → YES:  완료
```

### Common Patterns

#### Agent Basic Structure

```python
from abc import ABC, abstractmethod

class BaseAgent(ABC):
    def __init__(self, name: str):
        self.name = name
        self.llm_client = self._init_llm_client()

    @abstractmethod
    def execute(self, task: dict) -> dict:
        """에이전트 핵심 로직"""
        pass

    def _init_llm_client(self):
        """LLM 클라이언트 초기화"""
        # Claude, GPT-4, Gemini 중 선택
        pass
```

#### Using Individual Agents

```python
from agents.literature import LiteratureReviewAgent
from agents.hypothesis import HypothesisAgent

# 문헌 조사
lit_agent = LiteratureReviewAgent()
result = lit_agent.conduct_review(
    topic="Machine Learning for Materials Discovery"
)
print(result['papers'])

# 가설 생성
hyp_agent = HypothesisAgent()
hypothesis = hyp_agent.generate_hypothesis(
    literature=result['papers'],
    research_gap=result['gaps']
)
print(hypothesis['statement'])
```

#### Agent Composition

```python
from agents.director import ResearchDirectorAgent

# 연구 총괄 에이전트가 전체 워크플로우 조율
director = ResearchDirectorAgent()

# 모든 에이전트 등록
director.register_agent('literature', LiteratureReviewAgent())
director.register_agent('hypothesis', HypothesisAgent())
director.register_agent('data_analysis', DataAnalysisAgent())
# ... etc

# 전체 워크플로우 실행
result = director.run_full_workflow()
```

### Code Style

- **BaseAgent** 추상 클래스 상속
- **execute()** 메서드 구현 (핵심 로직)
- **Type hints** 필수
- **Error handling** 명시적
- **Logging** 일관된 형식

### Agent Responsibilities

#### 1. ResearchDirectorAgent

```python
class ResearchDirectorAgent(BaseAgent):
    """연구 총괄 및 워크플로우 조율"""

    def execute(self, project_config):
        # 1. 프로젝트 설정 로드
        # 2. 에이전트 순서 결정
        # 3. 중간 결과 전달
        # 4. 진행 상황 추적
        # 5. 최종 결과 집계
        pass
```

**담당**:
- 프로젝트 관리
- 에이전트 간 데이터 전달
- 진행 상황 추적
- 최종 결과 집계

#### 2. LiteratureReviewAgent

```python
class LiteratureReviewAgent(BaseAgent):
    """문헌 조사 및 Research Gap 식별"""

    def conduct_review(self, topic, field):
        # 1. 검색 쿼리 생성
        # 2. arXiv, Google Scholar 검색
        # 3. 논문 요약
        # 4. 연구 동향 파악
        # 5. Research Gap 식별
        pass
```

**담당**:
- arXiv 논문 검색
- Google Scholar 검색
- 논문 요약 및 분류
- Research Gap 식별

**사용 도구**:
- `arxiv` library
- `scholarly` library
- Web search

#### 3. HypothesisAgent

```python
class HypothesisAgent(BaseAgent):
    """가설 생성 및 실험 설계"""

    def generate_hypothesis(self, literature, gaps):
        # 1. Research Gap 분석
        # 2. 가설 생성
        # 3. 실험 설계
        # 4. 방법론 수립
        pass
```

**담당**:
- 가설 생성
- 실험 설계
- 방법론 수립
- 연구 질문 정의

#### 4. DataAnalysisAgent

```python
class DataAnalysisAgent(BaseAgent):
    """데이터 수집 및 통계 분석"""

    def analyze_data(self, hypothesis, experimental_design):
        # 1. 데이터 수집
        # 2. 데이터 전처리
        # 3. 통계 분석
        # 4. 시각화
        # 5. 결과 해석
        pass
```

**담당**:
- 데이터 수집
- 통계 분석 (t-test, ANOVA, 회귀분석 등)
- 시각화 (matplotlib, seaborn)
- 결과 해석

**사용 도구**:
- `pandas` - 데이터 처리
- `numpy` - 수치 계산
- `scipy` - 통계 분석
- `matplotlib`, `seaborn` - 시각화

#### 5. PaperWritingAgent

```python
class PaperWritingAgent(BaseAgent):
    """영문 연구보고서 작성"""

    def write_paper(self, research_results):
        # 1. Abstract 작성 (250-300 words)
        # 2. Introduction 작성
        # 3. Methodology 작성
        # 4. Results 작성
        # 5. Discussion 작성
        # 6. Conclusion 작성
        # 7. References 정리
        pass
```

**담당**:
- 영문 연구보고서 작성
- 논문 형식 준수
- 참고문헌 정리 (APA/IEEE style)

**출력 형식**:
- Markdown
- 논문 구조 (Abstract ~ References)

#### 6. AILoggingAgent

```python
class AILoggingAgent(BaseAgent):
    """AI 활용 로깅 및 기여도 평가"""

    def log_interaction(self, model, prompt, response, context):
        # 1. 타임스탬프 기록
        # 2. 모델 정보 저장
        # 3. 프롬프트 저장
        # 4. 응답 저장
        # 5. 토큰 사용량 기록
        # 6. 기여도 평가
        pass

    def evaluate_ai_contribution(self, research_paper):
        # 1. AI 활용 패턴 분석
        # 2. 기여도 계산 (50%+ 목표)
        # 3. AI 활용보고서 생성
        pass
```

**담당**:
- 모든 AI 상호작용 기록
- AI 기여도 평가
- AI 활용보고서 작성

**로그 형식**:
```markdown
## Interaction Log

### Timestamp: 2026-01-29 10:30:00
### Model: claude-3-5-sonnet-20241022
### Task: Literature Review

#### Prompt:
[...]
#### Response:
[...]
#### Usage:
- Tokens: 150/280
- Contribution: High
```

#### 7. ValidationAgent

```python
class ValidationAgent(BaseAgent):
    """재현성 및 통계적 검증"""

    def validate_research(self, research_results):
        # 1. 재현성 확인
        # 2. 통계적 검증
        # 3. 코드 검증
        # 4. 데이터 검증
        pass
```

**담당**:
- 재현성 확인
- 통계적 검증 (p-value, effect size)
- 코드 검증
- 데이터 검증

#### 8. QualityAssuranceAgent

```python
class QualityAssuranceAgent(BaseAgent):
    """심사 기준 기반 자가 평가"""

    def evaluate_quality(self, submission):
        # 1. 3개 AI Judge 평가 (Claude, GPT-4, Gemini)
        # 2. 심사 기준별 점수 부여
        # 3. Gap 분석
        # 4. 피드백 생성
        # 5. 개선 제언
        pass
```

**담당**:
- 3개 AI Judge 평가
- 심사 기준별 점수 부여
- Gap 분석
- 피드백 생성

**심사 기준**:
- 주제의 실용성 (20점)
- 방법론의 적절성 (20점)
- 데이터의 적절성 (25점)
- 결론의 합리성 (10점)
- 전달력 및 가독성 (5점)
- 연구의 창의성 (20점)

### Testing Individual Agents

```python
# 에이전트 단위 테스트
from agents.literature import LiteratureReviewAgent

agent = LiteratureReviewAgent()
result = agent.conduct_review(
    topic="Battery Materials",
    field="secondary_battery"
)

# 결과 확인
assert result['papers_found'] > 0
assert result['gaps'] is not None
```

### Agent Communication

```python
# 에이전트 간 데이터 전달
lit_result = literature_agent.execute({'topic': topic})
hyp_result = hypothesis_agent.execute({
    'literature': lit_result['papers'],
    'gaps': lit_result['gaps']
})
data_result = data_analysis_agent.execute({
    'hypothesis': hyp_result['hypothesis'],
    'experimental_design': hyp_result['design']
})
```

## Dependencies

### Internal

- `../config/settings.py` - 설정 관리

### External

- **anthropic** - Claude API
- **openai** - GPT-4 API
- **google-generativeai** - Gemini API
- **arxiv** - arXiv 검색
- **scholarly** - Google Scholar 검색
- **pandas, numpy, scipy** - 데이터 분석
- **matplotlib, seaborn** - 시각화

## Agent Factory

```python
# __init__.py
class AgentFactory:
    """에이전트 생성 팩토리"""

    @staticmethod
    def create_agent(agent_type: str) -> BaseAgent:
        agents = {
            'director': ResearchDirectorAgent,
            'literature': LiteratureReviewAgent,
            'hypothesis': HypothesisAgent,
            'data_analysis': DataAnalysisAgent,
            'paper_writing': PaperWritingAgent,
            'ai_logging': AILoggingAgent,
            'validation': ValidationAgent,
            'quality': QualityAssuranceAgent
        }
        return agents[agent_type]()
```

<!-- MANUAL: -->
