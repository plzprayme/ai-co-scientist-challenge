<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-01-29 | Updated: 2026-01-29 -->

# ai_co_scientist_glm4

## Purpose

**GLM-4 모델 통합 및 RALP (Reflection-Agent Loop Pattern) 구현** - 중국어 Zhipu AI의 GLM-4 모델을 활용한 연구 수행 시스템입니다.

이 시스템은 **RALP 래퍼**를 통해 GLM-4 모델을 연구 워크플로우에 통합하고, 반사적 사고(Reflection) 패턴을 구현합니다.

## Key Files

| File | Description |
|------|-------------|
| `main_ralp.py` | RALP 패턴 메인 실행 스크립트 |
| `ralp_wrapper.py` | RALP 래퍼 구현 - GLM-4 반사적 사고 패턴 |
| `glm4_client.py` | GLM-4 API 클라이언트 |
| `config.yaml` | GLM-4 설정 파일 |
| `requirements.txt` | Python 의존성 |
| `README.md` | 프로젝트 개요 |
| `CLAUDE.md` | AI 에이전트 가이드 |
| `CRITICAL_ANALYSIS.md` | 비판적 분석 문서 |
| `SYSTEM_SUMMARY.md` | 시스템 요약 |

## Subdirectories

이 디렉토리에는 하위 디렉토리가 없습니다.

## For AI Agents

### Working In This Directory

이 시스템은 **GLM-4** (중국어 최신 LLM)를 활용하여 연구를 수행합니다.

### RALP Pattern (Reflection-Agent Loop Pattern)

```
┌─────────────────────────────────────────────────────────────────┐
│                    RALP 패턴 아키텍처                            │
└─────────────────────────────────────────────────────────────────┘

    ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
    │    Agent     │────▶│   Action     │────▶│   Result     │
    │   (GLM-4)    │     │   Execution  │     │  Generation  │
    └──────────────┘     └──────────────┘     └──────────────┘
           ▲                                          │
           │                                          ▼
    ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
    │  Reflection  │◀────│   Critique   │◀────│  Evaluation  │
    │   (Self)     │     │   (Meta)     │     │   (Check)    │
    └──────────────┘     └──────────────┘     └──────────────┘
```

### Running the System

```bash
# 기본 실행
python main_ralp.py

# 설정 파일 사용
python main_ralp.py --config config.yaml

# 특정 작업 실행
python main_ralp.py --task literature_review
python main_ralp.py --task hypothesis_generation
python main_ralp.py --task paper_writing
```

### Configuration

`config.yaml`에서 GLM-4 설정을 관리합니다:

```yaml
# GLM-4 API 설정
api_key: "${GLM4_API_KEY}"
model: "glm-4-plus"
temperature: 0.7
max_tokens: 4096

# RALP 설정
reflection_cycles: 3
critique_threshold: 0.8
improvement_strategy: "iterative"

# 연구 설정
research_topic: "Your Research Topic"
target_field: "materials_chemistry"
target_score: 85
```

### Common Patterns

#### GLM-4 클라이언트 사용

```python
from glm4_client import GLM4Client

# 클라이언트 초기화
client = GLM4Client(api_key="your_api_key")

# 기본 호출
response = client.generate(
    prompt="Conduct a literature review on...",
    temperature=0.7
)

print(response['text'])
```

#### RALP 래퍼 사용

```python
from ralp_wrapper import RALPWrapper

# RALP 초기화
ralp = RALPWrapper(
    agent_client=glm4_client,
    reflection_cycles=3
)

# 작업 실행
result = ralp.execute_with_reflection(
    task="Conduct literature review",
    context=research_context
)

# 결과 확인
print(f"Initial: {result['initial_output']}")
print(f"Refined: {result['refined_output']}")
print(f"Reflections: {result['reflections']}")
```

#### 반사적 사고 패턴

```python
# 1. 초기 생성
initial = agent.generate(task)

# 2. 비판 (Critique)
critique = meta_agent.critique(initial)

# 3. 반사 (Reflection)
reflection = agent.reflect(critique)

# 4. 개선 (Improvement)
improved = agent.improve(initial, reflection)

# 5. 반복
for _ in range(cycles):
    critique = meta_agent.critique(improved)
    reflection = agent.reflect(critique)
    improved = agent.improve(improved, reflection)
```

### Code Style

- **PEP 8** 준수
- **Type hints** 사용
- **Docstring** Google style
- **YAML** 설정 파일 사용

### GLM-4 Model Characteristics

**Zhipu AI GLM-4**:
- 중국어 최신 LLM
- 강력한 추론 능력
- 다국어 지원 (중국어, 영어)
- 128K context window
- Function calling 지원

**장점**:
- 중국어 과학 논문 이해에 우수
- 복잡한 추론 작업에 강점
- 긴 context 처리 가능

### RALP Reflection Process

```python
# 반사적 사고 단계
def reflect(self, output, critique):
    reflections = []

    # 1. Self-Correction
    if 'errors' in critique:
        reflections.append("Correct identified errors")

    # 2. Enhancement
    if 'weaknesses' in critique:
        reflections.append("Enhance weak areas")

    # 3. Refinement
    if 'suggestions' in critique:
        reflections.append("Apply suggestions")

    return reflections
```

### Multi-Language Support

```python
# 중국어 논문 처리
chinese_response = client.generate(
    prompt="总结这篇论文的核心贡献...",
    language="zh"
)

# 영어 논문 처리
english_response = client.generate(
    prompt="Summarize the core contributions...",
    language="en"
)
```

## Dependencies

### External

- **zhipuai** (>=1.0.0) - GLM-4 API 클라이언트
- **pydantic** (>=2.0.0) - 데이터 검증
- **pyyaml** (>=6.0) - 설정 파일 파싱
- **python-dotenv** (>=1.0.0) - 환경 변수
- **requests** (>=2.31.0) - HTTP 요청

### API Keys

```bash
# .env 파일
GLM4_API_KEY=your_glm4_api_key_here
```

## Key Features

### 1. Reflection-Agent Loop Pattern

```python
class RALPWrapper:
    def execute_with_reflection(self, task, context):
        # 1. 초기 생성
        output = self.agent.generate(task, context)

        # 2. 반사적 사고循环
        for i in range(self.reflection_cycles):
            # 비판
            critique = self.meta_agent.critique(output)

            # 반사
            reflection = self.agent.reflect(critique)

            # 개선
            output = self.agent.improve(output, reflection)

        return output
```

### 2. Multi-Stage Critique

```python
# 3단계 비판
critique = {
    'factual_accuracy': check_facts(output),
    'logical_consistency': check_logic(output),
    'clarity_quality': check_clarity(output)
}
```

### 3. Iterative Improvement

```python
# 반복적 개선
for iteration in range(max_iterations):
    # 생성 → 비판 → 반사 → 개선
    output = generate(output, critique, reflection)

    # 수렴 확인
    if is_converged(output):
        break
```

## Comparison with Other Models

| 특징 | Claude | GPT-4 | GLM-4 |
|------|--------|-------|-------|
| 언어 | 영어 중심 | 영어 중심 | 중국어/영어 |
| Context | 200K | 128K | 128K |
| 추론 | 우수 | 우수 | 우수 |
| 중국어 | 보통 | 보통 | **최고** |
| 과학 논문 | 우수 | 우수 | 우수 |

## Use Cases

### 1. Chinese Literature Review

```python
# 중국어 논문 검토
chinese_papers = search_chinese_papers(topic)
review = ralp.execute_with_reflection(
    task="Review Chinese literature",
    context={"papers": chinese_papers}
)
```

### 2. Cross-Lingual Research

```python
# 다국어 연구
multilingual_review = {
    'english': review_english_papers(),
    'chinese': review_chinese_papers(),
    'korean': review_korean_papers()
}
```

### 3. Meta-Analysis

```python
# 메타 분석
meta_analysis = ralp.execute_with_reflection(
    task="Conduct meta-analysis",
    context={"studies": all_studies}
)
```

## Testing

```bash
# GLM-4 연결 테스트
python -m pytest tests/test_glm4_client.py

# RALP 패턴 테스트
python -m pytest tests/test_ralp_wrapper.py

# 통합 테스트
python -m pytest tests/integration/
```

## Critical Analysis

`CRITICAL_ANALYSIS.md` 참조:
- GLM-4 모델의 장단점 분석
- RALP 패턴의 효율성 평가
- 다른 모델과의 비교 분석
- 개선 제언

<!-- MANUAL: -->
