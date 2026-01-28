# CLAUDE.md - MIRROR System

## 프로젝트 개요

**MIRROR (Meta-Learning Iterative Research Optimization & Reflection System)**  
2026 AI Co-Scientist Challenge Korea Track 1 참가를 위한 메타러닝 기반 자기개선 무한루프 에이전트 시스템

---

## 핵심 원칙: 이중 루프 학습

```
낸부 루프 (Inner Loop): 제출물 품질 개선
외부 루프 (Outer Loop): 에이전트 시스템 자체 개선
```

---

## 빌드/테스트/배포 명령어

### 실행 명령어

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

### 테스트

```bash
# 단위 테스트
python -m pytest tests/

# 통합 테스트
python test_workflow.py
```

---

## 프로젝트 구조

```
ai_co_scientist_v2/
├── mirror/                    # MIRROR 시스템 코어
│   ├── engine.py             # 메인 엔진 (이중 루프)
│   ├── meta_learning.py      # 메타러닝 엔진 (외부 루프)
│   ├── reflection.py         # 리플렉션 엔진
│   ├── version_control.py    # 버전 컨트롤러
│   └── agents/
│       └── base.py           # Self-Improving Agent
├── submissions/              # 제출물 (버전별)
├── versions/                 # 버전 히스토리
│   ├── commit_log.txt
│   └── CHANGELOG.md
├── main.py                   # 실행 스크립트
└── README.md
```

---

## 코드 스타일

### Python

- PEP 8 준수
- Type hints 필수
- Docstring (Google style)

```python
def example(param: str) -> dict:
    """
    Example function.
    
    Args:
        param: Parameter description
        
    Returns:
        Result dictionary
    """
    return {"result": param}
```

---

## Self-Improving Agent 개발 가이드

### 기본 구조

```python
from mirror.agents.base import SelfImprovingAgent

class MyAgent(SelfImprovingAgent):
    def __init__(self):
        super().__init__('my_agent')
        # 초기화
    
    def execute(self, task):
        # 핵심 로직
        return result
```

### 피드백 기반 개선

```python
# 피드백 받기
feedback = {
    'score': 0.6,  # 60% 성능
    'weaknesses': ['reasoning_unclear'],
    'suggestions': ['add_examples']
}

agent.improve(feedback)

# 결과
# - 전략 적응
# - 프롬프트 최적화
# - 버전 업데이트 (1.0.0 → 1.0.1)
```

---

## 버전 관리 규약

### Semantic Versioning

```
v{MAJOR}.{MINOR}.{PATCH}-iter{N}

MAJOR: 아키텍처 변경 (5회 이상 개선)
MINOR: 전략 변경
PATCH: 프롬프트 조정
```

### Commit 메시지

```
[Iteration {N}] Submission Improvement

Score: {prev} → {curr} ({change:+.1f})

## Improvements
- [HIGH] {target}: {action}
- [MED] {target}: {action}

## Reflection
- Total improvements: {N}
- High priority: {N}
```

---

## 메타러닝 시스템

### 3계층 메모리

```python
# Episodic Memory - 단기 기억
self.episodic_memory.append({
    'iteration': N,
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

### 개선사항 생성

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

---

## 다중 AI 심사

### 3개 모델 활용

```python
judges = {
    'claude': ClaudeJudge(),
    'gpt4': GPT4Judge(),
    'gemini': GeminiJudge()
}

# 각각 평가
results = {
    'claude': {'practicality': 17, ...},
    'gpt4': {'practicality': 16, ...},
    'gemini': {'practicality': 18, ...}
}

# 중앙값 집계
aggregated = {
    'practicality': median([17, 16, 18])  # = 17
}
```

---

## 리플렉션 시스템

### 약점 식별

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

### 개선사항 생성

```python
# 우선순위 결정
gap > 50% → high
gap > 30% → medium
else → low
```

---

## 실행 흐름

```python
# 1. 엔진 생성
engine = MIRROREngine(config)

# 2. 에이전트 등록
engine.register_agent('literature', LiteratureAgent())
engine.register_agent('writer', WritingAgent())
...

# 3. 실행
result = engine.run()

# 낸부:
#   - 연구 수행
#   - 3개 AI Judge 평가
#   - 리플렉션
#   - 제출물 개선
#   - commit

# 외부 (3 iteration마다):
#   - 메타러닝
#   - 에이전트 개선
```

---

## 디버깅

### 로그 레벨 조정

```python
logging.basicConfig(level=logging.DEBUG)
```

### 중간 결과 확인

```python
# 특정 iteration에서 멈추고 확인
if iteration == 3:
    import pdb; pdb.set_trace()
```

### 히스토리 분석

```python
stats = engine.get_stats()
print(stats)

# {
#     'total_iterations': 5,
#     'best_score': 91.0,
#     'improvement_count': 5
# }
```

---

## 확장 포인트

### 새로운 Judge 추가

```python
class MyJudge(SelfImprovingAgent):
    def evaluate(self, submission):
        return {
            'practicality': 18,
            'methodology': 19,
            ...
        }

engine.register_agent('my_judge', MyJudge())
```

### 새로운 개선 전략

```python
def _generate_new_approach(self, patterns):
    if 'new_pattern' in patterns:
        return 'my_new_strategy'
```

---

## 제출 체크리스트

### 연구보고서

- [ ] 논문 형태 (영문)
- [ ] Abstract 250-300 words
- [ ] Keywords 3-5개
- [ ] 모든 섹션 포함

### AI 활용보고서

- [ ] URL 목록
- [ ] AI 상호작용 로그
- [ ] 체크리스트
- [ ] 기여도 평가 (50%+)
- [ ] 3개 모델 활용 증거

### 데이터 목록

- [ ] 공개 데이터 정보
- [ ] 생성 데이터 정보
- [ ] 처리 방법

### 버전 관리

- [ ] iteration마다 commit
- [ ] CHANGELOG 생성
- [ ] 태그 관리

---

## 참고 자료

- `META_LEARNING_AGENT_SYSTEM.md` - 상세 설계
- `mirror/engine.py` - 메인 구현
- `mirror/meta_learning.py` - 메타러닝
- `mirror/reflection.py` - 리플렉션
- `mirror/version_control.py` - 버전 관리

---

**MIRROR System v2.0.0**  
*"시스템이 스스로를 개선하며 연구를 수행한다"*
