<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-01-29 | Updated: 2026-01-29 -->

# mirror

## Purpose

MIRROR 시스템의 코어 엔진 - 이중 루프 학습 (Dual-Loop Learning) 아키텍처를 통해 제출물과 에이전트 시스템을 동시에 개선합니다.

## Key Files

| File | Description |
|------|-------------|
| `__init__.py` | MIRROR 패키지 초기화 |
| `engine.py` | MIRROREngine - 이중 루프 학습 메인 엔진 |
| `meta_learning.py` | MetaLearningEngine - 외부 루프 (에이전트 시스템 개선) |
| `reflection.py` | ReflectionEngine - 리플렉션 및 개선사항 생성 |
| `version_control.py` | VersionController - 버전 관리 및 commit 시스템 |

## Subdirectories

| Directory | Purpose |
|-----------|---------|
| `agents/` | SelfImprovingAgent 기본 클래스 및 에이전트 구현 |

## For AI Agents

### Working In This Directory

MIRROR 시스템의 핵심 컴포넌트들을 이해하고 활용합니다.

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

### Common Patterns

#### MIRROREngine 사용

```python
from mirror.engine import MIRROREngine

# 엔진 초기화
engine = MIRROREngine(config={
    'target_score': 90,
    'max_iterations': 15,
    'meta_learning_interval': 3  # 3 iteration마다 메타러닝
})

# 에이전트 등록
engine.register_agent('literature', LiteratureAgent())
engine.register_agent('hypothesis', HypothesisAgent())
engine.register_agent('writer', WritingAgent())

# 실행
result = engine.run()

# 결과 확인
print(f"Best Score: {result['best_score']}")
print(f"Total Iterations: {result['total_iterations']}")
print(f"Agent Improvements: {result['agent_improvements']}")
```

#### Meta-Learning 사용

```python
from mirror.meta_learning import MetaLearningEngine

# 메타러닝 엔진 초기화
meta_engine = MetaLearningEngine()

# 성능 데이터 수집
performance_data = {
    'iteration': 5,
    'score_history': [75, 78, 82, 85, 87],
    'weaknesses': ['methodology', 'clarity'],
    'agent_performances': {
        'literature': 0.9,
        'hypothesis': 0.7,
        'writer': 0.8
    }
}

# 메타러닝 실행
improvements = meta_engine.generate_improvements(performance_data)

# 에이전트 개선
for improvement in improvements:
    target_agent = improvement.target
    action = improvement.action
    # 에이전트에 개선사항 적용
    target_agent.improve(action)
```

#### Reflection 사용

```python
from mirror.reflection import ReflectionEngine

# 리플렉션 엔진 초기화
reflection_engine = ReflectionEngine()

# iteration 결과 분석
iteration_result = {
    'score': 82.5,
    'scores_by_criteria': {
        'practicality': 17,
        'methodology': 15,  # 약점!
        'data': 20,
        'conclusion': 9,
        'clarity': 4,
        'creativity': 17
    }
}

# 약점 식별
weaknesses = reflection_engine.identify_weaknesses(iteration_result)

# 개선사항 생성
improvements = reflection_engine.generate_improvements(weaknesses)

# 우선순위 결정
improvements = reflection_engine.prioritize_improvements(improvements)
```

#### Version Control 사용

```python
from mirror.version_control import VersionController

# 버전 컨트롤러 초기화
vc = VersionController()

# iteration 완료 후 commit
vc.create_commit(
    iteration=5,
    submission=current_submission,
    score=87.5,
    improvements=[
        'methodology: enhanced statistical validation',
        'writing: improved abstract clarity'
    ]
)

# 히스토리 조회
history = vc.get_history()
for commit in history:
    print(f"Iteration {commit['iteration']}: {commit['score']}")

# diff 확인
diff = vc.get_diff(iteration=4, iteration=5)
print(diff)

# rollback (필요시)
vc.rollback_to_iteration(iteration=4)
```

### Core Components

#### 1. MIRROREngine (`engine.py`)

**역할**: 이중 루프 학습 조율

```python
class MIRROREngine:
    def __init__(self, config):
        self.meta_engine = MetaLearningEngine()
        self.reflection_engine = ReflectionEngine()
        self.version_controller = VersionController()
        self.agents = {}

    def register_agent(self, name, agent):
        """에이전트 등록"""
        self.agents[name] = agent

    def run(self):
        """이중 루프 실행"""
        for iteration in range(self.max_iterations):
            # 내부 루프: 제출물 개선
            submission = self._run_inner_loop()

            # 버전 컨트롤: commit
            self.version_controller.create_commit(iteration, submission)

            # 외부 루프: 메타러닝 (주기적)
            if iteration % self.meta_learning_interval == 0:
                self._run_outer_loop()

        return self._get_final_result()
```

#### 2. MetaLearningEngine (`meta_learning.py`)

**역할**: 외부 루프 - 에이전트 시스템 개선

```python
class MetaLearningEngine:
    def __init__(self):
        # 3계층 메모리
        self.episodic_memory = []      # 단기 기억
        self.semantic_memory = {}       # 장르 기억 (패턴)
        self.procedural_memory = {}     # 절차적 지식

    def generate_improvements(self, performance_data):
        """메타러닝 기반 개선사항 생성"""
        # 1. 패턴 식별 (semantic memory)
        patterns = self._identify_patterns(performance_data)

        # 2. 병목 분석
        bottlenecks = self._analyze_bottlenecks(performance_data)

        # 3. 개선사항 생성
        improvements = self._generate_improvements(patterns, bottlenecks)

        # 4. episodic memory에 저장
        self.episodic_memory.append({
            'iteration': performance_data['iteration'],
            'patterns': patterns,
            'improvements': improvements
        })

        return improvements
```

**3계층 메모리 시스템**:
```python
# Episodic Memory - 단기 기억
self.episodic_memory.append({
    'iteration': 5,
    'score': 87.0,
    'weaknesses': ['methodology'],
    'success': True
})

# Semantic Memory - 장르 기억 (패턴)
self.semantic_memory['methodology_bottleneck'] = {
    'type': 'recurring_weakness',
    'confidence': 0.85,
    'frequency': 3
}

# Procedural Memory - 절차적 지식
self.procedural_memory['enhance_methodology'] = {
    'success_count': 5,
    'failure_count': 1
}
```

#### 3. ReflectionEngine (`reflection.py`)

**역할**: 리플렉션 및 개선사항 생성

```python
class ReflectionEngine:
    def identify_weaknesses(self, iteration_result):
        """약점 식별"""
        weaknesses = []

        for criteria, score in iteration_result['scores_by_criteria'].items():
            max_score = QUALITY_CRITERIA[criteria]['max_score']

            # 80% 미만이면 약점
            if score < max_score * 0.8:
                gap = max_score - score
                weakness = Weakness(
                    category=criteria,
                    score=score,
                    max_score=max_score,
                    gap=gap
                )
                weaknesses.append(weakness)

        return weaknesses

    def generate_improvements(self, weaknesses):
        """개선사항 생성"""
        improvements = []

        for weakness in weaknesses:
            # 우선순위 결정
            if weakness.gap > 50:
                priority = 'high'
            elif weakness.gap > 30:
                priority = 'medium'
            else:
                priority = 'low'

            improvement = SystemImprovement(
                target=f'agent:{weakness.category}_agent',
                action='enhance_capabilities',
                reason=f'{weakness.category} is a bottleneck',
                priority=priority
            )
            improvements.append(improvement)

        return improvements
```

#### 4. VersionController (`version_control.py`)

**역할**: 버전 관리 및 diff 추적

```python
class VersionController:
    def __init__(self):
        self.commits = []
        self.current_version = "1.0.0"

    def create_commit(self, iteration, submission, score, improvements):
        """commit 생성"""
        commit = {
            'iteration': iteration,
            'version': self._get_next_version(iteration, improvements),
            'timestamp': datetime.now(),
            'submission': submission,
            'score': score,
            'improvements': improvements,
            'diff': self._calculate_diff(iteration - 1, iteration)
        }

        self.commits.append(commit)
        self._write_commit_log(commit)
        self._update_changelog(commit)

    def get_history(self):
        """히스토리 조회"""
        return self.commits

    def get_diff(self, iter1, iter2):
        """diff 계산"""
        commit1 = self.commits[iter1]
        commit2 = self.commits[iter2]
        return {
            'score_change': commit2['score'] - commit1['score'],
            'improvements': commit2['improvements']
        }
```

**Semantic Versioning**:
```
v{MAJOR}.{MINOR}.{PATCH}-iter{N}

MAJOR: 아키텍처 변경 (5회 이상 개선)
MINOR: 전략 변경
PATCH: 프롬프트 조정
```

### Code Style

- **PEP 8** 준수
- **Type hints** 필수
- **Docstring** Google style
- **불변성** 선호

### Workflow

```
Iteration N 시작
    │
    ├───▶ [내부 루프] 제출물 개선
    │         │
    │         ├──▶ 3개 AI Judge 평가
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

- `agents/` - SelfImprovingAgent 기본 클래스

### External

- **anthropic** - Claude API
- **openai** - GPT-4 API
- **google-generativeai** - Gemini API
- **pydantic** - 데이터 검증
- **gitpython** - Git 버전 관리

<!-- MANUAL: -->
