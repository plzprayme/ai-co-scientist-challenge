# MIRROR 시스템 아키텍처 요약

## 1. 시스템 개요

**MIRROR** (Meta-Learning Iterative Research Optimization & Reflection)  
2026 AI Co-Scientist Challenge Korea - Track 1을 위한 메타러닝 기반 자기개선 무한루프 에이전트 시스템

### 핵심 혁신: 이중 루프 학습 (Dual-Loop Learning)

```
┌─────────────────────────────────────────────────────────────────┐
│                        이중 루프 학습                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌──────────────────┐         ┌──────────────────┐            │
│   │   낸부 루프       │         │   외부 루프       │            │
│   │ (Inner Loop)     │         │ (Outer Loop)     │            │
│   │                  │         │                  │            │
│   │ • 제출물 개선    │◀───────│ • Agent 개선     │            │
│   │ • 품질 향상      │         │ • Prompt 최적화  │            │
│   │ • 심사 기준 충족 │         │ • Workflow 재설계│            │
│   └──────────────────┘         └──────────────────┘            │
│           │                              │                     │
│           └──────────────┬───────────────┘                     │
│                          │                                     │
│                    ┌─────▼─────┐                               │
│                    │  Commit   │                               │
│                    │  (버전관리) │                               │
│                    └───────────┘                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. 핵심 컴포넌트

### 2.1 MIRROREngine (`mirror/engine.py`)

메인 실행 엔진으로, 이중 루프 학습을 조율

```python
class MIRROREngine:
    def run(self):
        for iteration in range(1, max_iterations + 1):
            # 1. 연구 수행
            submission = self._execute_research()
            
            # 2. 다중 AI 심사 (3개 모델)
            evaluation = self._multi_judge_evaluation(submission)
            
            # 3. 리플렉션
            reflection = self._reflect(submission, evaluation)
            
            # 4. 낸부 루프: 제출물 개선
            improved = self._improve_submission(submission, evaluation, reflection)
            
            # 5. 버전 컨트롤: commit
            self._commit_iteration(iteration, improved, evaluation, reflection)
            
            # 6. 외부 루프: 메타러닝 (3 iteration마다)
            if iteration % 3 == 0:
                improvements = self._meta_learn()
                self._apply_system_improvements(improvements)
```

### 2.2 MetaLearningEngine (`mirror/meta_learning.py`)

외부 루프 - 시스템 자체를 개선

**3계층 메모리 시스템:**

| 메모리 계층 | 설명 | 용도 |
|------------|------|------|
| **Episodic** | 개별 iteration의 구체적 경험 | 단기 기억 |
| **Semantic** | 추상화된 지식과 패턴 | 장기 기억 |
| **Procedural** | workflow와 절차적 지식 | 행동 학습 |

**주요 기능:**
- 패턴 추출 (반복 약점, 성공/실패 패턴)
- 병목 지점 식별
- 시스템 개선사항 생성

### 2.3 ReflectionEngine (`mirror/reflection.py`)

iteration 결과 분석 및 개선사항 생성

**심사 기준별 약점 식별:**
- 80% 미만 점수 → 약점으로 간주
- 원인 분석 + 개선 방안 제안
- 우선순위 부여 (high/medium/low)

### 2.4 VersionController (`mirror/version_control.py`)

Git-style 버전 관리

**기능:**
- iteration마다 commit 생성
- Semantic versioning (`v1.0.0-iter1`)
- diff 추적
- rollback 지원
- CHANGELOG 자동 생성

### 2.5 SelfImprovingAgent (`mirror/agents/base.py`)

스스로 개선하는 에이전트 기본 클래스

**기능:**
- Semantic versioning (Major/Minor/Patch)
- 성능 기록 및 분석
- 프롬프트 전략 최적화
- 피드백 기반 개선

---

## 3. 데이터 흐름

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Literature │────▶│ Hypothesis  │────▶│    Data     │
│    Agent    │     │    Agent    │     │    Agent    │
└─────────────┘     └─────────────┘     └─────────────┘
                                               │
                       ┌───────────────────────┘
                       ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  AI Usage   │◀────│   Writer    │◀────│   Results   │
│    Agent    │     │    Agent    │     │             │
└─────────────┘     └─────────────┘     └─────────────┘
       │
       ▼
┌─────────────────────────────────────────────────────┐
│              Multi-AI Judge Evaluation               │
│  (Claude + GPT-4 + Gemini → Median Aggregation)     │
└─────────────────────────────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────────────────────┐
│              Reflection & Improvement                │
│  - Weakness Identification                           │
│  - Improvement Generation                            │
│  - Next Steps Suggestion                             │
└─────────────────────────────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────────────────────┐
│              Version Control (Commit)                │
│  - Tag: v{MAJOR}.{MINOR}.{PATCH}-iter{N}            │
│  - Changelog Update                                  │
└─────────────────────────────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────────────────────┐
│              Meta-Learning (every 3 iters)           │
│  - Pattern Analysis                                  │
│  - Agent Architecture Update                         │
│  - Prompt Strategy Optimization                      │
└─────────────────────────────────────────────────────┘
```

---

## 4. 파일 구조

```
ai_co_scientist_v2/
├── mirror/                          # MIRROR 시스템 코어
│   ├── __init__.py                  # 패키지 초기화
│   ├── engine.py                    # 메인 엔진 (이중 루프)
│   ├── meta_learning.py             # 메타러닝 엔진 (외부 루프)
│   ├── reflection.py                # 리플렉션 엔진
│   ├── version_control.py           # 버전 컨트롤러
│   └── agents/
│       ├── __init__.py
│       └── base.py                  # Self-Improving Agent 기본 클래스
│
├── submissions/                     # 제출물 (버전별, 자동 생성)
│   ├── iter_001/
│   ├── iter_002/
│   └── ...
│
├── versions/                        # 버전 히스토리 (자동 생성)
│   ├── v1.0.0-iter1.json
│   ├── commit_log.txt
│   └── CHANGELOG.md
│
├── main.py                          # 실행 스크립트
├── test_mirror.py                   # 테스트 스위트
├── META_LEARNING_AGENT_SYSTEM.md    # 상세 설계 문서
├── ARCHITECTURE_SUMMARY.md          # 이 파일
├── README.md                        # 사용자 가이드
└── CLAUDE.md                        # CLAUDE CODE 설정
```

---

## 5. 실행 방법

```bash
# 기본 실행
python main.py

# 목표 점수 설정
python main.py --target-score 90

# 최대 반복 횟수 설정
python main.py --max-iterations 15

# 테스트
python test_mirror.py
```

---

## 6. 대회 요구사항 충족

| 요구사항 | MIRROR 구현 | 파일 |
|----------|-------------|------|
| 3개 이상 AI 모델 활용 | ✅ Claude, GPT-4, Gemini Judge | `main.py` |
| 연구 전 과정 AI 기여 | ✅ Self-Improving Agents | `mirror/agents/base.py` |
| AI 활용보고서 | ✅ 상세 로그 + 기여도 평가 | `LoggingAgent` |
| 제출물 품질 개선 | ✅ 낸부 루프 | `engine.py::_improve_submission` |
| 시스템 자체 개선 | ✅ 외부 루프 | `meta_learning.py` |
| 버전 관리 | ✅ iteration마다 commit | `version_control.py` |

---

## 7. 심사 기준 매핑

| 심사 기준 (100점) | MIRROR 대응 | 개선 메커니즘 |
|-------------------|-------------|---------------|
| 주제의 실용성 (20점) | `practicality` 분석 | 리플렉션 → 개선 |
| 방법론의 적절성 (20점) | `methodology` 분석 | 리플렉션 → 개선 |
| 데이터의 적절성 (25점) | `data_quality` 분석 | 리플렉션 → 개선 |
| 결론의 합리성 (10점) | `conclusion` 분석 | 리플렉션 → 개선 |
| 전달력 및 가독성 (5점) | `readability` 분석 | 리플렉션 → 개선 |
| 연구의 창의성 (20점) | `creativity` 분석 | 리플렉션 → 개선 |
| AI 연구기여도 (P/F) | 3모델 활용 + 로깅 | `MultiAIJudges` |

---

## 8. 핵심 클래스 다이어그램

```
┌─────────────────────────────────────────────────────────────────┐
│                        MIRROREngine                              │
├─────────────────────────────────────────────────────────────────┤
│ - iteration: int                                                │
│ - max_iterations: int                                           │
│ - target_score: float                                           │
│ - agents: Dict[str, SelfImprovingAgent]                         │
│ - iteration_history: List[IterationData]                        │
├─────────────────────────────────────────────────────────────────┤
│ + run(): Submission                                             │
│ + register_agent(name, agent)                                   │
│ - _execute_research(): Submission                               │
│ - _multi_judge_evaluation(): Evaluation                         │
│ - _reflect(): ReflectionReport                                  │
│ - _improve_submission(): Submission                             │
│ - _commit_iteration()                                           │
│ - _meta_learn(): List[SystemImprovement]                        │
│ - _apply_system_improvements()                                  │
└─────────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
┌───────────────┐   ┌─────────────────┐   ┌─────────────────┐
│MetaLearningEngine│   │ ReflectionEngine │   │VersionController│
├───────────────┤   ├─────────────────┤   ├─────────────────┤
│- episodic_memory │   │- reflection_history│   │- commits: List  │
│- semantic_memory │   ├─────────────────┤   │- current_version│
│- procedural_mem │   │+ reflect()      │   ├─────────────────┤
├───────────────┤   │- _identify_weaknesses│   │+ commit()       │
│+ learn_from_iteration()│   │- _generate_improvements│   │+ get_diff()     │
│+ analyze_patterns()│   │- _extract_insights()│   │+ rollback()     │
│+ generate_improvements()│   │- _suggest_next_steps()│   │+ generate_changelog()│
└───────────────┘   └─────────────────┘   └─────────────────┘
        │
        ▼
┌─────────────────────────────────────────────────────────────────┐
│                    SelfImprovingAgent (ABC)                      │
├─────────────────────────────────────────────────────────────────┤
│ - name: str                                                     │
│ - version: str                                                  │
│ - performance_history: List[Dict]                               │
│ - prompt_strategies: List[Dict]                                 │
├─────────────────────────────────────────────────────────────────┤
│ + execute(task): Result                                         │
│ + improve(feedback)                                             │
│ + apply_improvement(improvement)                                │
│ - _adapt_strategy(feedback)                                     │
│ - _optimize_prompt(feedback)                                    │
│ - _update_version()                                             │
└─────────────────────────────────────────────────────────────────┘
```

---

## 9. Commit 메시지 예시

```
[Iteration 5] Submission Improvement

Score: 82.0 → 87.0 (+5.0)

## Improvements
- [HIGH] practicality: add_real_world_examples
- [HIGH] creativity: explore_novel_ai_usage
- [MED] methodology: enhance_experimental_design

## Reflection
- Total improvements: 3
- High priority: 2

## Agent Updates
- literature_agent: version 1.0.1 → 1.0.2
- writing_agent: enhanced_cot_prompt
```

---

## 10. 확장 포인트

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
# meta_learning.py
def _generate_new_approach(self, patterns):
    if 'my_pattern' in patterns:
        return 'my_strategy'
```

---

**MIRROR System v2.0.0**  
*"시스템이 스스로를 개선하며 연구를 수행한다"*
