<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-01-29 | Updated: 2026-01-29 -->

# ai_co_scientist_v2

## Purpose

**MIRROR (Meta-Learning Iterative Research Optimization & Reflection System)** - 메타러닝 기반 자기개선 무한루프 에이전트 시스템입니다.

이 시스템은 **이중 루프 학습 (Dual-Loop Learning)** 아키텍처를 통해:
1. **내부 루프**: 제출물 품질 개선
2. **외부 루프**: 에이전트 시스템 자체 개선

두 계층에서 동시에 학습하고 개선합니다.

## Key Files

| File | Description |
|------|-------------|
| `main.py` | MIRROR 시스템 메인 실행 스크립트 |
| `META_LEARNING_AGENT_SYSTEM.md` | 상세 설계 문서 - 이중 루프 학습 아키텍처 |
| `ARCHITECTURE_SUMMARY.md` | 시스템 아키텍처 요약 |
| `README.md` | 프로젝트 개요 및 사용 가이드 |
| `CLAUDE.md` | AI 에이전트를 위한 프로젝트 가이드 |
| `test_mirror.py` | MIRROR 시스템 테스트 스크립트 |

## Subdirectories

| Directory | Purpose |
|-----------|---------|
| `mirror/` | MIRROR 시스템 코어 - 이중 루프 학습 엔진 |
| `submissions/` | 제출물 (버전별 관리) |
| `versions/` | 버전 히스토리 및 변경 로그 |

## For AI Agents

### Working In This Directory

MIRROR 시스템의 핵심 혁신은 **메타러닝**을 통해 에이전트 시스템이 스스로를 개선한다는 점입니다.

### Dual-Loop Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    MIRROR 시스템 아키텍처                        │
└─────────────────────────────────────────────────────────────────┘

                    ┌─────────────────────────────────────┐
                    │     메타러닝 레이어 (Meta-Learning)   │
                    │  - Agent Architecture 개선           │
                    │  - Prompt Strategy 최적화            │
                    │  - Workflow 재구성                   │
                    └──────────────┬──────────────────────┘
                                   │
                    ┌──────────────▼──────────────────────┐
                    │     리플렉션 레이어 (Reflection)      │
                    │  - iteration별 성능 분석             │
                    │  - 실패 원인 진단                    │
                    │  - 개선 전략 생성                    │
                    └──────────────┬──────────────────────┘
                                   │
        ┌──────────────────────────┼──────────────────────────┐
        │                          │                          │
        ▼                          ▼                          ▼
┌───────────────┐      ┌──────────────────┐      ┌──────────────────┐
│  외부 루프     │      │     내부 루프      │      │   버전 컨트롤     │
│ (Outer Loop)  │      │   (Inner Loop)   │      │  (Version Ctrl)  │
│               │      │                  │      │                  │
│ • Agent 개선  │◀─────│ • 제출물 개선     │      │ • iteration      │
│ • Prompt 최적화│      │ • 품질 향상      │      │   commit        │
│ • Workflow    │      │ • 심사 기준      │      │ • diff 추적      │
│   재설계      │      │   충족          │      │ • rollback       │
└───────────────┘      └──────────────────┘      └──────────────────┘
```

### Running the System

```bash
# 기본 실행
python main.py

# 목표 점수 설정
python main.py --target-score 90

# 최대 반복 횟수 설정
python main.py --max-iterations 15

# 조합
python main.py --target-score 85 --max-iterations 20
```

### Testing

```bash
# MIRROR 시스템 테스트
python test_mirror.py

# 단위 테스트
python -m pytest tests/

# 통합 테스트
python -m pytest tests/integration/
```

### Common Patterns

#### MIRROR 엔진 사용

```python
from mirror.engine import MIRROREngine

# 엔진 초기화
engine = MIRROREngine(config={
    'target_score': 90,
    'max_iterations': 15
})

# 에이전트 등록
engine.register_agent('literature', LiteratureAgent())
engine.register_agent('writer', WritingAgent())

# 실행
result = engine.run()

# 결과 확인
print(f"Final Score: {result['best_score']}")
print(f"Total Iterations: {result['total_iterations']}")
```

#### Self-Improving Agent

```python
from mirror.agents.base import SelfImprovingAgent

class MyAgent(SelfImprovingAgent):
    def __init__(self):
        super().__init__('my_agent')
        self.version = "1.0.0"

    def execute(self, task):
        # 핵심 로직
        return result

# 피드백 기반 개선
feedback = {
    'score': 0.6,
    'weaknesses': ['reasoning_unclear'],
    'suggestions': ['add_examples']
}

agent.improve(feedback)
# → 전략 적응, 프롬프트 최적화, 버전 업데이트
```

#### 버전 관리

```python
from mirror.version_control import VersionController

vc = VersionController()

# iteration 완료 후 commit
vc.create_commit(
    iteration=5,
    submission=current_submission,
    score=87.5,
    improvements=[...]
)

# 히스토리 조회
history = vc.get_history()
```

### Code Style

- **PEP 8** 준수
- **Type hints** 필수
- **Docstring** Google style
- **Semantic Versioning** (v{MAJOR}.{MINOR}.{PATCH}-iter{N})

### Meta-Learning System

#### 3-Layer Memory

```python
# Episodic Memory - 단기 기억
self.episodic_memory.append({
    'iteration': 5,
    'score': 87.0,
    'weaknesses': [...],
    'success': True
})

# Semantic Memory - 장기 기억 (패턴)
self.semantic_memory['pattern_key'] = {
    'type': 'recurring_weakness',
    'confidence': 0.85,
    'frequency': 3
}

# Procedural Memory - 절차적 지식
self.procedural_memory['action'] = {
    'success_count': 5,
    'failure_count': 1
}
```

#### Improvement Generation

```python
# 병목 분석 → 개선사항 생성
improvements = [
    SystemImprovement(
        target='agent:methodology_agent',
        action='enhance_capabilities',
        reason='methodology is a bottleneck',
        priority='high'
    )
]
```

### Version Control

#### Semantic Versioning

```
v{MAJOR}.{MINOR}.{PATCH}-iter{N}

MAJOR: 아키텍처 변경 (5회 이상 개선)
MINOR: 전략 변경
PATCH: 프롬프트 조정
```

#### Commit Message Format

```
[Iteration 5] Submission Improvement

Score: 82.0 → 87.5 (+5.5)

## Improvements
- [HIGH] methodology: enhance_statistical_validation
- [MED] writing: improve_abstract_clarity

## Reflection
- Total improvements: 2
- High priority: 1
- Weaknesses addressed: ['methodology', 'writing']
```

### Multi-AI Judging System

```python
# 3개 모델 활용 (대회 요구사항)
judges = {
    'claude': ClaudeJudge(),
    'gpt4': GPT4Judge(),
    'gemini': GeminiJudge()
}

# 각각 평가
results = {
    'claude': {'practicality': 17, 'methodology': 16, ...},
    'gpt4': {'practicality': 16, 'methodology': 17, ...},
    'gemini': {'practicality': 18, 'methodology': 17, ...}
}

# 중앙값 집계
aggregated = {
    'practicality': median([17, 16, 18]),  # = 17
    'methodology': median([16, 17, 17])    # = 17
}
```

### Reflection System

#### Weakness Identification

```python
# 80% 미만이면 약점
if score < max_score * 0.8:
    weakness = Weakness(
        category='methodology',
        score=15,
        max_score=20,
        gap=5,
        possible_causes=[...],
        suggested_fixes=[...]
    )
```

#### Improvement Priority

```python
gap > 50% → high priority
gap > 30% → medium priority
else → low priority
```

### Workflow

```
Iteration N 시작
    │
    ├───▶ [내부 루프] 제출물 개선
    │         │
    │         ├──▶ 3개 AI Judge 평가 (Claude, GPT-4, Gemini)
    │         ├──▶ Gap 분석
    │         ├──▶ 개선 전략 생성
    │         └──▶ 제출물 수정
    │
    ├───▶ [버전 컨트롤] commit 생성
    │         │
    │         ├──▶ submission 저장
    │         ├──▶ CHANGELOG 업데이트
    │         └──▶ diff 추적
    │
    └───▶ [외부 루프] 메타러닝 (3 iteration마다)
              │
              ├──▶ 성능 분석
              ├──▶ 패턴 식별
              ├──▶ 에이전트 개선
              └──▶ 시스템 재구성
```

## Dependencies

### Internal

- `mirror/` - MIRROR 시스템 코어

### External

- **anthropic** - Claude API
- **openai** - GPT-4 API
- **google-generativeai** - Gemini API
- **pydantic** - 데이터 검증
- **gitpython** - Git 버전 관리

## Output Structure

```
submissions/
├── v1.0.0-iter1/              # 버전별 제출물
│   ├── research_paper.md
│   ├── ai_usage_report.md
│   └── data_usage_list.md
├── v1.0.1-iter2/
│   └── ...

versions/
├── commit_log.txt             # 커밋 로그
├── CHANGELOG.md               # 변경 이력
└── agent_versions/            # 에이전트 버전 히스토리
    ├── literature_agent.json
    └── writer_agent.json
```

## Key Differences from v1

| 특징 | v1 (ai_co_scientist_agents) | v2 (MIRROR) |
|------|---------------------------|-------------|
| 루프 구조 | 단일 루프 | 이중 루프 (내부 + 외부) |
| 개선 대상 | 제출물만 | 제출물 + 에이전트 시스템 |
| 메타러닝 | 없음 | 3계층 메모리 기반 |
| 버전 관리 | 없음 | Git-style commit 시스템 |
| 자기 개선 | 수동 | 자동 |
| 리플렉션 | 기본 | 고급 (패턴 인식) |

## Submission Checklist

- [ ] 연구보고서 (논문 형태, 영문)
- [ ] AI 활용보고서 (3개 모델 활용 증거)
- [ ] 데이터 목록
- [ ] iteration마다 commit
- [ ] CHANGELOG 작성
- [ ] 버전 태그 관리

<!-- MANUAL: -->
