# MIRROR System v2.0.0 비판적 분석 및 개선안

## 1. 기존 시스템의 치명적 문제점

### 1.1 구현 불가능한 구조

| 문제점 | 심각도 | 설명 |
|--------|--------|------|
| **Mock 데이터 의존** | 🔴 치명적 | 모든 에이전트가 mock 데이터 반환, 실제로는 작동하지 않음 |
| **다중 모델 가정** | 🔴 치명적 | Claude/GPT-4/Gemini를 가정했지만 glm 4.7만 사용 가능 |
| **복잡한 상속 구조** | 🟡 중간 | SelfImprovingAgent 추상 클래스가 실제 구현을 방해 |
| **파일 I/O 의존성** | 🟡 중간 | 디렉토리 구조 없으면 오류 발생 |
| **메타러닝 불명확** | 🔴 치명적 | "패턴 분석"이 구체적으로 어떻게 되는지 코드에 없음 |

### 1.2 ULTRAWORK RALP와의 괴리

```
ULTRAWORK RALP 특성:
- 무한 루프 실행
- 파일 기반 상태 관리
- 단일 모델 (glm 4.7) 사용
- 간단한 구조 선호

기존 MIRROR:
- 복잡한 클래스 구조
- 다중 모델 가정
- 메모리 기반 상태
- 추상화 과다
```

### 1.3 glm 4.7 특성 미고려

- glm 4.7는 한국어/영어 모두 가능
- 단일 모델로 모든 작업 수행
- 토큰 제한 고려 필요
- 함수 호출 (function calling) 지원

---

## 2. 개선된 시스템: RALP-MIRROR

### 2.1 설계 원칙

1. **단일 모델**: glm 4.7만 사용
2. **파일 기반 상태**: 모든 상태는 파일에 저장
3. **단순 구조**: 클래스 상속 최소화
4. **실제 실행 가능**: mock 없이 실제 동작
5. **RALP 통합**: 무한 루프에 적합한 구조

### 2.2 시스템 아키텍처

```
┌─────────────────────────────────────────────────────────────────┐
│                     RALP-MIRROR System                           │
│              (glm 4.7 + ULTRAWORK RALP 최적화)                   │
└─────────────────────────────────────────────────────────────────┘

┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   STATE      │────▶│   GLM 4.7    │────▶│   OUTPUT     │
│   FILE       │     │   MODEL      │     │   FILE       │
└──────────────┘     └──────────────┘     └──────────────┘
       ▲                                          │
       │                                          ▼
┌──────────────┐                         ┌──────────────┐
│   EVALUATE   │◀────────────────────────│   GENERATE   │
│   & LEARN    │                         │   SUBMISSION │
└──────────────┘                         └──────────────┘

Loop: 무한 반복 (ULTRAWORK RALP에 의해 관리)
```

### 2.3 파일 기반 상태 관리

```
workspace/
├── state.json              # 현재 상태 (iteration, score, 등)
├── rubric.json             # 심사 기준
├── submission/             # 제출물
│   ├── paper.md           # 연구보고서
│   ├── ai_usage.md        # AI 활용보고서
│   └── data_list.md       # 데이터 목록
├── history/               # 히스토리
│   ├── iter_001.json
│   ├── iter_002.json
│   └── ...
├── prompts/               # 프롬프트 템플릿
│   ├── paper_writer.txt
│   ├── evaluator.txt
│   └── improver.txt
└── learnings/             # 학습된 내용
    ├── weaknesses.json
    ├── strategies.json
    └── improvements.json
```

---

## 3. 핵심 개선사항

### 3.1 단일 모델 (glm 4.7) 최적화

```python
# BEFORE: 다중 모델 가정
judges = {
    'claude': ClaudeJudge(),
    'gpt4': GPT4Judge(),
    'gemini': GeminiJudge()
}

# AFTER: glm 4.7 하나로 3번 평가 (self-consistency)
evaluations = [
    glm4_evaluate(submission, temperature=0.3),  # 보수적
    glm4_evaluate(submission, temperature=0.7),  # 중립적
    glm4_evaluate(submission, temperature=1.0)   # 창의적
]
final_score = median(evaluations)
```

### 3.2 파일 기반 상태 관리

```python
# BEFORE: 메모리 기반
self.iteration_history = []

# AFTER: 파일 기반
def save_state(state):
    with open('workspace/state.json', 'w') as f:
        json.dump(state, f)

def load_state():
    with open('workspace/state.json', 'r') as f:
        return json.load(f)
```

### 3.3 단순화된 구조

```python
# BEFORE: 복잡한 클래스 상속
class SelfImprovingAgent(ABC):
    def improve(self, feedback): ...
    def _adapt_strategy(self, feedback): ...
    def _optimize_prompt(self, feedback): ...

# AFTER: 함수 기반
def improve_paper(paper, feedback):
    prompt = f"""
    이전 논문: {paper}
    피드백: {feedback}
    
    개선된 논문을 작성하세요.
    """
    return glm4_generate(prompt)
```

### 3.4 실제 실행 가능한 코드

```python
# BEFORE: mock
papers = [{'title': 'Mock', 'year': 2024}]

# AFTER: 실제 arxiv 검색
papers = search_arxiv(query, max_results=10)
```

---

## 4. RALP 통합 구조

### 4.1 ULTRAWORK RALP용 메인 루프

```python
# main_ralp.py - RALP가 무한으로 실행
import json
import os

def main_loop():
    """RALP가 무한으로 호출"""
    state = load_state()
    
    if state['phase'] == 'research':
        do_research(state)
    elif state['phase'] == 'evaluate':
        do_evaluate(state)
    elif state['phase'] == 'improve':
        do_improve(state)
    elif state['phase'] == 'commit':
        do_commit(state)
    
    save_state(state)

# RALP가 실행: while True: main_loop()
```

### 4.2 상태 머신

```
[research] → [evaluate] → [improve] → [commit] → [research] → ...
                ↓
         [target met?]
              ↓ YES
         [finalize]
```

---

## 5. glm 4.7 특화 프롬프트 전략

### 5.1 함수 호출 (Function Calling) 활용

```python
def evaluate_with_glm4(submission):
    prompt = f"""
    다음 연구보고서를 심사 기준에 따라 평가하세요.
    
    연구보고서: {submission['paper']}
    
    다음 JSON 형식으로 응답하세요:
    {{
        "practicality": {{"score": 0-20, "reason": "..."}},
        "methodology": {{"score": 0-20, "reason": "..."}},
        "data_quality": {{"score": 0-25, "reason": "..."}},
        "conclusion": {{"score": 0-10, "reason": "..."}},
        "readability": {{"score": 0-5, "reason": "..."}},
        "creativity": {{"score": 0-20, "reason": "..."}},
        "ai_contribution": {{"pass": true/false, "reason": "..."}},
        "improvements": [
            {{"target": "...", "action": "...", "priority": "high/medium/low"}}
        ]
    }}
    """
    return glm4_generate(prompt, response_format='json')
```

### 5.2 Self-Consistency 평가

```python
def evaluate_ensemble(submission, n=3):
    """glm 4.7로 n번 평가 후 중앙값 선택"""
    scores = []
    for temp in [0.3, 0.7, 1.0]:
        result = glm4_evaluate(submission, temperature=temp)
        scores.append(result)
    
    # 중앙값 선택
    return {
        'practicality': median([s['practicality']['score'] for s in scores]),
        'methodology': median([s['methodology']['score'] for s in scores]),
        ...
    }
```

---

## 6. 구현 계획

### 6.1 Phase 1: 기본 구조 (파일 기반)
- [ ] state.json 관리
- [ ] submission 파일 생성
- [ ] 기본 glm 4.7 연동

### 6.2 Phase 2: 연구 수행
- [ ] 문헌 검색 (arxiv)
- [ ] 논문 작성
- [ ] AI 활용 로깅

### 6.3 Phase 3: 평가 및 개선
- [ ] glm 4.7 자가 평가
- [ ] 개선 전략 생성
- [ ] iteration 반복

### 6.4 Phase 4: RALP 통합
- [ ] 무한 루프 구조
- [ ] 상태 머신
- [ ] 자동 복구

---

## 7. 파일 구조 (최종)

```
ai_co_scientist_glm4/
├── main_ralp.py           # RALP용 메인 루프
├── glm4_client.py         # glm 4.7 API 클라이언트
├── state_manager.py       # 상태 관리 (파일 기반)
├── research_engine.py     # 연구 수행 엔진
├── evaluator.py           # 평가 엔진 (glm 4.7)
├── improver.py            # 개선 엔진
├── paper_writer.py        # 논문 작성기
├── ai_logger.py           # AI 활용 로거
├── arxiv_search.py        # 문헌 검색
├── utils.py               # 유틸리티
│
├── workspace/             # 작업 공간 (RALP가 관리)
│   ├── state.json
│   ├── rubric.json
│   ├── submission/
│   ├── history/
│   ├── prompts/
│   └── learnings/
│
├── config.yaml            # 설정 파일
└── README.md              # 문서
```

---

## 8. 기존 vs 개선 비교

| 항목 | 기존 MIRROR | 개선 RALP-MIRROR |
|------|-------------|------------------|
| 모델 | Claude/GPT-4/Gemini | **glm 4.7 하나** |
| 상태 | 메모리 기반 | **파일 기반** |
| 구조 | 복잡한 클래스 | **단순 함수** |
| 실행 | Mock 데이터 | **실제 API 호출** |
| RALP | 미고려 | **최적화** |
| 메타러닝 | 불명확 | **구체적 구현** |

---

## 9. 결론

기존 MIRROR 시스템은 아이디어는 좋았지만:
1. **실행 불가능한 mock 구조**
2. **다중 모델 가정**
3. **복잡한 클래스 상속**
4. **메타러닝의 불명확성**

개선된 RALP-MIRROR:
1. **glm 4.7 단일 모델**
2. **파일 기반 상태 관리**
3. **단순 함수 기반 구조**
4. **실제 API 연동**
5. **RALP 무한 루프 최적화**
