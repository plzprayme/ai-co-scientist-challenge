<!-- Parent: ../../AGENTS.md -->
<!-- Generated: 2026-01-29 | Updated: 2026-01-29 -->

# agents

## Purpose

SelfImprovingAgent 기본 클래스 - MIRROR 시스템의 모든 에이전트가 상속받는 추상 클래스로, 피드백 기반 자기 개선 기능을 제공합니다.

## Key Files

| File | Description |
|------|-------------|
| `__init__.py` | 에이전트 패키지 초기화 |
| `base.py` | SelfImprovingAgent 추상 클래스 - 피드백 기반 자기 개선 |

## Subdirectories

이 디렉토리에는 하위 디렉토리가 없습니다.

## For AI Agents

### Working In This Directory

이 디렉토리는 **추상 클래스**만 포함합니다. 실제 에이전트 구현은 상위 레벨에서 이 클래스를 상속받아 구현합니다.

### SelfImprovingAgent Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                   SelfImprovingAgent                            │
└─────────────────────────────────────────────────────────────────┘

    ┌─────────────────────────────────────────────────────────────┐
    │                     Core Methods                            │
    ├─────────────────────────────────────────────────────────────┤
    │ • execute(task)           - 핵심 로직 실행                 │
    │ • improve(feedback)       - 피드백 기반 자기 개선           │
    │ • get_version()           - 현재 버전 조회                 │
    │ • get_performance()       - 성능 통계 조회                 │
    └─────────────────────────────────────────────────────────────┘

    ┌─────────────────────────────────────────────────────────────┐
    │                     3-Layer Memory                         │
    ├─────────────────────────────────────────────────────────────┤
    │ • episodic_memory    - 단기 기억 (iteration 데이터)        │
    │ • semantic_memory    - 장기 기억 (패턴)                    │
    │ • procedural_memory  - 절차적 지식 (성공/실패 횟수)        │
    └─────────────────────────────────────────────────────────────┘

    ┌─────────────────────────────────────────────────────────────┐
    │                     Self-Improvement                       │
    ├─────────────────────────────────────────────────────────────┤
    │ 1. Analyze Feedback    - 피드백 분석                       │
    │ 2. Identify Weakness  - 약점 식별                         │
    │ 3. Adapt Strategy     - 전략 적응                         │
    │ 4. Optimize Prompt    - 프롬프트 최적화                   │
    │ 5. Update Version     - 버전 업데이트                     │
    └─────────────────────────────────────────────────────────────┘
```

### Common Patterns

#### SelfImprovingAgent 상속

```python
from mirror.agents.base import SelfImprovingAgent

class LiteratureAgent(SelfImprovingAgent):
    def __init__(self):
        super().__init__('literature')
        # 초기화

    def execute(self, task):
        """핵심 로직 구현"""
        # 문헌 조사 수행
        papers = self.search_papers(task['topic'])
        gaps = self.identify_gaps(papers)
        return {'papers': papers, 'gaps': gaps}

    def _adapt_strategy(self, feedback):
        """전략 적응 로직"""
        if 'search_query' in feedback.weaknesses:
            self.search_strategy = 'broader'
```

#### 피드백 기반 개선

```python
# 에이전트 실행
agent = LiteratureAgent()
result = agent.execute({'topic': 'Battery Materials'})

# 피드백 생성
feedback = {
    'score': 0.6,  # 60% 성능
    'weaknesses': ['search_query_too_narrow', 'missing_recent_papers'],
    'suggestions': ['broaden_search', 'include_2024_papers']
}

# 자기 개선
agent.improve(feedback)

# 결과
# - 전략 적응: search_strategy = 'broader'
# - 프롬프트 최적화: "Include papers from 2024"
# - 버전 업데이트: 1.0.0 → 1.0.1
```

#### 버전 관리

```python
# 버전 조회
print(agent.get_version())  # "1.0.0"

# 개선 후 버전 업데이트
agent.improve(feedback)
print(agent.get_version())  # "1.0.1" (PATCH)

# 여러 개선 후
agent.improve(feedback2)
agent.improve(feedback3)
print(agent.get_version())  # "1.1.0" (MINOR)

# 아키텍처 변경 (5회 이상 개선)
for _ in range(5):
    agent.improve(feedback)
print(agent.get_version())  # "2.0.0" (MAJOR)
```

#### 성능 추적

```python
# 성능 통계 조회
stats = agent.get_performance()
print(stats)

# {
#     'total_executions': 10,
#     'total_improvements': 5,
#     'average_score': 0.75,
#     'best_score': 0.85,
#     'recent_trend': 'improving'
# }
```

### Base Class Structure

```python
class SelfImprovingAgent(ABC):
    """피드백 기반 자기 개선 에이전트"""

    def __init__(self, name: str):
        self.name = name
        self.version = "1.0.0"

        # 3계층 메모리
        self.episodic_memory = []
        self.semantic_memory = {}
        self.procedural_memory = {}

        # 성능 추적
        self.performance_history = []

        # 전략
        self.strategy = {}

    @abstractmethod
    def execute(self, task: dict) -> dict:
        """핵심 로직 (하위 클래스에서 구현)"""
        pass

    def improve(self, feedback: dict):
        """피드백 기반 자기 개선"""
        # 1. 피드백 분석
        analysis = self._analyze_feedback(feedback)

        # 2. 약점 식별
        weaknesses = self._identify_weaknesses(analysis)

        # 3. 전략 적응
        self._adapt_strategy(weaknesses)

        # 4. 프롬프트 최적화
        self._optimize_prompts(weaknesses)

        # 5. 버전 업데이트
        self._update_version()

        # 6. episodic memory에 저장
        self.episodic_memory.append({
            'feedback': feedback,
            'improvements': weaknesses
        })

    def _analyze_feedback(self, feedback):
        """피드백 분석"""
        return {
            'score': feedback['score'],
            'weaknesses': feedback['weaknesses'],
            'suggestions': feedback['suggestions']
        }

    def _identify_weaknesses(self, analysis):
        """약점 식별"""
        weaknesses = []
        for weakness in analysis['weaknesses']:
            weaknesses.append(weakness)
        return weaknesses

    def _adapt_strategy(self, weaknesses):
        """전략 적응"""
        for weakness in weaknesses:
            # 전략 수정
            if weakness == 'search_query_too_narrow':
                self.strategy['search_breadth'] = 'broad'
            elif weakness == 'missing_recent_papers':
                self.strategy['year_filter'] = '>=2023'

    def _optimize_prompts(self, weaknesses):
        """프롬프트 최적화"""
        # 프롬프트 템플릿 수정
        pass

    def _update_version(self):
        """버전 업데이트 (Semantic Versioning)"""
        major, minor, patch = self.version.split('.')
        patch = int(patch) + 1

        if patch >= 5:
            patch = 0
            minor = int(minor) + 1

        if minor >= 5:
            minor = 0
            major = int(major) + 1

        self.version = f"{major}.{minor}.{patch}"

    def get_version(self):
        """현재 버전 조회"""
        return self.version

    def get_performance(self):
        """성능 통계 조회"""
        if not self.performance_history:
            return {}

        return {
            'total_executions': len(self.performance_history),
            'average_score': sum(self.performance_history) / len(self.performance_history),
            'best_score': max(self.performance_history),
            'recent_trend': self._calculate_trend()
        }

    def _calculate_trend(self):
        """최근 트렌드 계산"""
        recent = self.performance_history[-5:]
        if len(recent) < 2:
            return 'unknown'

        if recent[-1] > recent[0]:
            return 'improving'
        elif recent[-1] < recent[0]:
            return 'declining'
        else:
            return 'stable'
```

### 3-Layer Memory System

#### Episodic Memory (단기 기억)

```python
# iteration 데이터 저장
self.episodic_memory.append({
    'iteration': 5,
    'task': task,
    'result': result,
    'score': 0.75,
    'feedback': feedback,
    'timestamp': datetime.now()
})
```

#### Semantic Memory (장르 기억)

```python
# 패턴 저장
self.semantic_memory['search_pattern'] = {
    'type': 'recurring_weakness',
    'confidence': 0.85,
    'frequency': 3,
    'last_seen': iteration
}

# 패턴 조회
if 'search_pattern' in self.semantic_memory:
    pattern = self.semantic_memory['search_pattern']
    if pattern['confidence'] > 0.8:
        # 높은 확신도의 패턴 발견
        # 미리 조치
```

#### Procedural Memory (절차적 지식)

```python
# 성공/실패 횟수 저장
self.procedural_memory['search_broad'] = {
    'success_count': 5,
    'failure_count': 1,
    'success_rate': 0.83
}

# 최적 전략 선택
def choose_best_strategy(self):
    best_strategy = None
    best_rate = 0

    for strategy, stats in self.procedural_memory.items():
        if stats['success_rate'] > best_rate:
            best_rate = stats['success_rate']
            best_strategy = strategy

    return best_strategy
```

### Code Style

- **추상 클래스**: ABC 상속
- **Type hints** 필수
- **Docstring** Google style
- **불변성** 선호

### Implementation Example

```python
from mirror.agents.base import SelfImprovingAgent

class HypothesisAgent(SelfImprovingAgent):
    def __init__(self):
        super().__init__('hypothesis')
        self.creativity_level = 0.7

    def execute(self, task):
        """가설 생성"""
        literature = task['literature']
        gaps = task['gaps']

        # 프롬프트 생성
        prompt = self._generate_prompt(literature, gaps)

        # LLM 호출
        hypothesis = self._call_llm(prompt)

        # 성능 기록
        self.performance_history.append(task.get('score', 0.0))

        return {'hypothesis': hypothesis}

    def _generate_prompt(self, literature, gaps):
        """프롬프트 생성 (전략 반영)"""
        prompt = f"Generate a hypothesis based on:\n"
        prompt += f"- Literature: {literature}\n"
        prompt += f"- Gaps: {gaps}\n"

        # 전략 반영
        if self.strategy.get('creativity') == 'high':
            prompt += "\nBe creative and innovative."
        else:
            prompt += "\nBe conservative and rigorous."

        return prompt

    def _adapt_strategy(self, weaknesses):
        """전략 적응"""
        if 'not_creative' in weaknesses:
            self.strategy['creativity'] = 'high'
            self.creativity_level = 0.9
        elif 'not_rigorous' in weaknesses:
            self.strategy['creativity'] = 'low'
            self.creativity_level = 0.5

    def _optimize_prompts(self, weaknesses):
        """프롬프트 최적화"""
        if 'not_creative' in weaknesses:
            self.prompt_template = self.prompt_template.replace(
                "Generate a hypothesis",
                "Generate a CREATIVE and NOVEL hypothesis"
            )
```

## Dependencies

### Internal

- 없음 (최상위 에이전트 기본 클래스)

### External

- **anthropic** - Claude API
- **openai** - GPT-4 API
- **pydantic** - 데이터 검증

<!-- MANUAL: -->
