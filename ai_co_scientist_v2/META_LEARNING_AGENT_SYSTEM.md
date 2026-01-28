# 2026 AI Co-Scientist Challenge Korea - Track 1
# 메타러닝 기반 자기개선 무한루프 에이전트 시스템 (Meta-Learning Self-Improving Infinite Loop Agent System)

## 1. 기존 시스템 비판적 평가 (Critical Analysis of Previous System)

### 1.1 주요 문제점

| 문제점 | 심각도 | 설명 |
|--------|--------|------|
| **정적 에이전트 구조** | 🔴 높음 | 에이전트가 고정된 로직으로 동작하며, iteration을 거치며 스스로 개선되지 않음 |
| **단일 피드백 루프** | 🔴 높음 | 제출물만 개선되고, 에이전트 시스템 자체는 개선되지 않음 |
| **No Version Control** | 🟡 중간 | iteration마다 commit이 없어 추적 및 롤백 불가 |
| **제한된 AI 활용** | 🟡 중간 | Claude만 사용하는 구조로 3개 이상 모델 활용 요구사항 미흡 |
| **No Meta-Learning** | 🔴 높음 | 이전 iteration의 학습이 시스템 아키텍처에 반영되지 않음 |
| **단순 시뮬레이션** | 🔴 높음 | 실제 데이터 분석이 아닌 mock 데이터 사용 |

### 1.2 대회 요구사항과의 괴리

```
대회 요구사항                    기존 시스템
─────────────────────────────────────────────────
3개 이상 AI 모델 활용     →      단일 모델 중심
실제 연구 수행            →      Mock 데이터 기반
AI 활용보고서 (상세 로그)  →      템플릿 기반 생성
연구 전 과정 AI 기여      →      일부 단계만 AI 활용
제출물 품질 개선           →      고정된 평가 기준
```

---

## 2. 개선된 시스템 아키텍처: MIRROR (Meta-Learning Iterative Research Optimization & Reflection System)

### 2.1 핵심 개념: 이중 루프 학습 (Dual-Loop Learning)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         MIRROR 시스템 아키텍처                               │
└─────────────────────────────────────────────────────────────────────────────┘

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
│  외부 루프     │      │     낸부 루프      │      │   버전 컨트롤     │
│ (Outer Loop)  │      │   (Inner Loop)   │      │  (Version Ctrl)  │
│               │      │                  │      │                  │
│ • Agent 개선  │◀─────│ • 제출물 개선     │      │ • iteration      │
│ • Prompt 최적화│      │ • 품질 향상      │      │   commit        │
│ • Workflow    │      │ • 심사 기준      │      │ • diff 추적      │
│   재설계      │      │   충족          │      │ • rollback       │
└───────────────┘      └──────────────────┘      └──────────────────┘
```

### 2.2 시스템 구성 요소

```python
# 시스템 구조
MIRROR/
├── core/
│   ├── meta_learner.py          # 메타러닝 엔진
│   ├── reflection_engine.py     # 리플렉션 엔진
│   ├── version_controller.py    # 버전 컨트롤러
│   └── feedback_loop.py         # 피드백 루프 관리
├── agents/
│   ├── base_agent.py            # 기본 에이전트 (self-improving)
│   ├── research_agents/         # 연구 수행 에이전트들
│   └── system_agents/           # 시스템 관리 에이전트들
├── memory/
│   ├── episodic_memory.py       # 에피소딕 메모리 (iteration별)
│   ├── semantic_memory.py       # 시맨틱 메모리 (누적 학습)
│   └── procedural_memory.py     # 프로시저럴 메모리 (workflow)
├── evaluation/
│   ├── rubric_evaluator.py      # 심사 기준 평가기
│   ├── ai_judges.py             # 다중 AI 심사위원
│   └── gap_analyzer.py          # Gap 분석기
└── outputs/
    ├── submissions/             # 제출물 (버전별)
    ├── agent_versions/          # 에이전트 버전
    └── learning_logs/           # 학습 로그
```

---

## 3. 이중 루프 학습 메커니즘 (Dual-Loop Learning Mechanism)

### 3.1 낸부 루프: 제출물 개선 (Inner Loop)

```python
class InnerLoop:
    """제출물 품질 개선 루프"""
    
    def iterate(self, current_submission, evaluation_result):
        """
        1. 심사 결과 분석
        2. 약점 식별
        3. 개선 전략 수립
        4. 제출물 수정
        5. 품질 검증
        """
        weaknesses = self.identify_weaknesses(evaluation_result)
        strategy = self.generate_improvement_strategy(weaknesses)
        improved = self.apply_improvements(current_submission, strategy)
        return improved
```

### 3.2 외부 루프: 에이전트 개선 (Outer Loop)

```python
class OuterLoop:
    """에이전트 시스템 자체 개선 루프"""
    
    def meta_learn(self, iteration_history):
        """
        1. iteration 패턴 분석
        2. 에이전트 성능 분석
        3. 아키텍처 개선점 식별
        4. 프롬프트 전략 최적화
        5. workflow 재구성
        """
        patterns = self.analyze_patterns(iteration_history)
        agent_performance = self.evaluate_agents(patterns)
        improvements = self.identify_improvements(agent_performance)
        return self.apply_meta_improvements(improvements)
```

### 3.3 통합 플로우

```
Iteration N 시작
    │
    ├───▶ [낸부 루프] 제출물 개선
    │         │
    │         ├──▶ AI Judge 평가 (3개 모델)
    │         ├──▶ Gap 분석
    │         ├──▶ 개선 전략 생성
    │         └──▶ 제출물 수정
    │
    ├───▶ [버전 컨트롤] commit 생성
    │         │
    │         ├──▶ diff 생성
    │         ├──▶ 태그 부여 (vN.M)
    │         └──▶ 롤백 포인트 저장
    │
    └───▶ [외부 루프] 메타러닝
              │
              ├──▶ iteration 패턴 분석
              ├──▶ 에이전트 성능 평가
              ├──▶ 개선 전략 생성
              └──▶ 에이전트 아키텍처 업데이트

Iteration N+1 시작 (개선된 에이전트로)
```

---

## 4. 핵심 컴포넌트 상세 설계

### 4.1 메타러닝 엔진 (Meta-Learning Engine)

```python
class MetaLearningEngine:
    """
    iteration을 거치며 시스템 자체를 개선하는 메타러닝 엔진
    """
    
    def __init__(self):
        self.episodic_memory = EpisodicMemory()      # 단기 기억
        self.semantic_memory = SemanticMemory()      # 장기 기억
        self.procedural_memory = ProceduralMemory()  # 절차 기억
        
    def learn_from_iteration(self, iteration_data: IterationData):
        """
        iteration으로부터 학습
        """
        # 1. 에피소딕 메모리 저장
        self.episodic_memory.store(iteration_data)
        
        # 2. 패턴 추출 및 시맨틱 메모리 업데이트
        patterns = self.extract_patterns(iteration_data)
        self.semantic_memory.consolidate(patterns)
        
        # 3. 프로시저럴 메모리 업데이트
        if iteration_data.success:
            self.procedural_memory.reinforce(iteration_data.workflow)
        else:
            self.procedural_memory.adjust(iteration_data.workflow, iteration_data.failure_reason)
    
    def generate_improvements(self) -> List[SystemImprovement]:
        """
        개선사항 생성
        """
        improvements = []
        
        # 에이전트 아키텍처 개선
        agent_improvements = self.suggest_agent_improvements()
        improvements.extend(agent_improvements)
        
        # 프롬프트 전략 개선
        prompt_improvements = self.suggest_prompt_improvements()
        improvements.extend(prompt_improvements)
        
        # workflow 개선
        workflow_improvements = self.suggest_workflow_improvements()
        improvements.extend(workflow_improvements)
        
        return improvements
    
    def suggest_agent_improvements(self) -> List[SystemImprovement]:
        """
        에이전트 아키텍처 개선 제안
        """
        # 실패 패턴 분석
        failure_patterns = self.episodic_memory.get_failure_patterns()
        
        improvements = []
        
        # 특정 에이전트의 반복적인 실패
        for agent_name, failures in failure_patterns.by_agent.items():
            if len(failures) > 3:  # 3회 이상 실패
                improvements.append(SystemImprovement(
                    target=f"agent:{agent_name}",
                    action="decompose",
                    reason=f"{agent_name} has failed {len(failures)} times, needs decomposition"
                ))
        
        # 병목 현상 분석
        bottlenecks = self.analyze_bottlenecks()
        for bottleneck in bottlenecks:
            improvements.append(SystemImprovement(
                target=f"workflow:{bottleneck.stage}",
                action="parallelize",
                reason=f"{bottleneck.stage} is causing delays"
            ))
        
        return improvements
```

### 4.2 리플렉션 엔진 (Reflection Engine)

```python
class ReflectionEngine:
    """
    iteration 결과를 분석하고 insight를 추출
    """
    
    def reflect(self, iteration_result: IterationResult) -> ReflectionReport:
        """
        iteration에 대한 리플렉션 수행
        """
        report = ReflectionReport()
        
        # 1. 성공/실패 분석
        report.outcome_analysis = self.analyze_outcome(iteration_result)
        
        # 2. 의사결정 분석
        report.decision_analysis = self.analyze_decisions(iteration_result)
        
        # 3. 대안 경로 탐색
        report.alternatives = self.explore_alternatives(iteration_result)
        
        # 4. 학습 포인트 추출
        report.learning_points = self.extract_learning_points(iteration_result)
        
        return report
    
    def analyze_outcome(self, result: IterationResult) -> OutcomeAnalysis:
        """
        결과 분석
        """
        expected = result.expected_score
        actual = result.actual_score
        
        gap = expected - actual
        
        if gap > 10:
            severity = "critical"
        elif gap > 5:
            severity = "major"
        else:
            severity = "minor"
        
        return OutcomeAnalysis(
            expected=expected,
            actual=actual,
            gap=gap,
            severity=severity,
            root_causes=self.identify_root_causes(result, gap)
        )
    
    def identify_root_causes(self, result: IterationResult, gap: float) -> List[RootCause]:
        """
        근본 원인 분석
        """
        causes = []
        
        # 심사 기준별 분석
        for criterion, score in result.scores.items():
            max_score = RUBRIC[criterion]['max']
            if score < max_score * 0.8:  # 80% 미만
                causes.append(RootCause(
                    category=criterion,
                    score=score,
                    max=max_score,
                    possible_causes=self.investigate_cause(criterion, result)
                ))
        
        return causes
```

### 4.3 버전 컨트롤러 (Version Controller)

```python
class VersionController:
    """
    iteration마다 commit을 생성하고 버전 관리
    """
    
    def __init__(self, repo_path: str):
        self.repo = git.Repo(repo_path)
        self.version_tags = []
        
    def commit_iteration(self, iteration_num: int, changes: Changes) -> Commit:
        """
        iteration 결과를 commit
        """
        # 변경사항 스테이징
        self.stage_changes(changes)
        
        # 커밋 메시지 생성
        commit_message = self.generate_commit_message(iteration_num, changes)
        
        # 커밋 생성
        commit = self.repo.commit(commit_message)
        
        # 태그 생성
        tag = f"v{iteration_num}.0"
        self.repo.create_tag(tag, commit)
        self.version_tags.append(tag)
        
        # 변경 로그 생성
        self.generate_changelog(iteration_num, changes)
        
        return commit
    
    def generate_commit_message(self, iteration: int, changes: Changes) -> str:
        """
        커밋 메시지 생성
        """
        lines = [
            f"[Iteration {iteration}] Submission Improvement",
            "",
            f"Score Change: {changes.score_change:+.1f}",
            f"AI Contribution: {changes.ai_contribution}%",
            "",
            "Improvements:",
        ]
        
        for improvement in changes.improvements:
            lines.append(f"  - {improvement.category}: {improvement.description}")
        
        lines.extend([
            "",
            "Agent Updates:",
        ])
        
        for update in changes.agent_updates:
            lines.append(f"  - {update.agent}: {update.change_type}")
        
        return "\n".join(lines)
    
    def rollback_to(self, tag: str) -> None:
        """
        특정 버전으로 롤백
        """
        self.repo.git.checkout(tag)
        
    def get_diff(self, tag1: str, tag2: str) -> Diff:
        """
        두 버전 간 diff 생성
        """
        return self.repo.git.diff(tag1, tag2)
```

### 4.4 다중 AI 심사위원 (Multi-AI Judges)

```python
class MultiAIJudges:
    """
    3개 이상 AI 모델을 활용한 다중 심사 시스템
    """
    
    def __init__(self):
        self.judges = {
            'claude': ClaudeJudge(model="claude-3-5-sonnet-20241022"),
            'gpt4': GPT4Judge(model="gpt-4"),
            'gemini': GeminiJudge(model="gemini-pro"),
        }
        
    def evaluate(self, submission: Submission) -> MultiJudgeResult:
        """
        다중 심사 수행
        """
        results = {}
        
        # 각 심사위원 평가
        for name, judge in self.judges.items():
            logger.info(f"Judge {name} evaluating...")
            results[name] = judge.evaluate(submission)
        
        # 결과 집계
        aggregated = self.aggregate_results(results)
        
        # 불일치 분석
        discrepancies = self.analyze_discrepancies(results)
        
        return MultiJudgeResult(
            individual_results=results,
            aggregated=aggregated,
            discrepancies=discrepancies,
            confidence=self.calculate_confidence(results)
        )
    
    def aggregate_results(self, results: Dict[str, JudgeResult]) -> AggregatedScore:
        """
        심사 결과 집계 (앙상블)
        """
        aggregated = {}
        
        for criterion in RUBRIC.keys():
            scores = [r.scores[criterion] for r in results.values()]
            
            # 중앙값 사용 (이상치에 강건)
            aggregated[criterion] = {
                'median': np.median(scores),
                'mean': np.mean(scores),
                'std': np.std(scores),
                'min': min(scores),
                'max': max(scores),
                'consensus': self.check_consensus(scores)
            }
        
        return aggregated
    
    def analyze_discrepancies(self, results: Dict[str, JudgeResult]) -> List[Discrepancy]:
        """
        심사위원 간 불일치 분석
        """
        discrepancies = []
        
        for criterion in RUBRIC.keys():
            scores = {name: r.scores[criterion] for name, r in results.items()}
            
            max_diff = max(scores.values()) - min(scores.values())
            
            if max_diff > 5:  # 5점 이상 차이
                discrepancies.append(Discrepancy(
                    criterion=criterion,
                    scores=scores,
                    max_difference=max_diff,
                    possible_reasons=self.investigate_discrepancy(criterion, scores)
                ))
        
        return discrepancies
```

---

## 5. Self-Improving Agent 설계

### 5.1 기본 Self-Improving Agent

```python
class SelfImprovingAgent(ABC):
    """
    스스로 개선하는 에이전트 기본 클래스
    """
    
    def __init__(self, name: str):
        self.name = name
        self.version = "1.0.0"
        self.performance_history = []
        self.prompt_strategies = []
        self.current_strategy = None
        
    @abstractmethod
    def execute(self, task: Task) -> Result:
        pass
    
    def improve(self, feedback: Feedback) -> None:
        """
        피드백을 받아 스스로 개선
        """
        # 성능 기록
        self.performance_history.append({
            'timestamp': datetime.now(),
            'feedback': feedback,
            'strategy': self.current_strategy
        })
        
        # 개선 전략 선택
        if feedback.score < 0.7:  # 70% 미만
            self.adapt_strategy(feedback)
        
        # 프롬프트 최적화
        self.optimize_prompt(feedback)
        
        # 버전 업데이트
        self.update_version()
    
    def adapt_strategy(self, feedback: Feedback) -> None:
        """
        전략 적응
        """
        # 실패 패턴 분석
        patterns = self.analyze_failure_patterns()
        
        # 새로운 전략 생성
        new_strategy = self.generate_new_strategy(patterns)
        
        # 전략 테스트
        if self.test_strategy(new_strategy):
            self.current_strategy = new_strategy
            self.prompt_strategies.append(new_strategy)
    
    def optimize_prompt(self, feedback: Feedback) -> None:
        """
        프롬프트 최적화
        """
        # Few-shot 예제 업데이트
        if feedback.type == 'fewshot_insufficient':
            self.add_fewshot_examples(feedback.examples)
        
        # Chain-of-Thought 개선
        if feedback.type == 'reasoning_unclear':
            self.enhance_cot_prompt()
        
        # 컨텍스트 길이 조정
        if feedback.type == 'context_overflow':
            self.adjust_context_window()
    
    def update_version(self) -> None:
        """
        Semantic versioning
        """
        parts = self.version.split('.')
        major, minor, patch = int(parts[0]), int(parts[1]), int(parts[2])
        
        # Major: 아키텍처 변경
        # Minor: 전략 변경
        # Patch: 프롬프트 조정
        
        if self.architecture_changed():
            major += 1
            minor = 0
            patch = 0
        elif self.strategy_changed():
            minor += 1
            patch = 0
        else:
            patch += 1
        
        self.version = f"{major}.{minor}.{patch}"
```

---

## 6. 메모리 시스템 (Memory System)

### 6.1 3계층 메모리 구조

```python
class MemorySystem:
    """
    인지 아키텍처 기반 3계층 메모리 시스템
    """
    
    def __init__(self):
        # 에피소딕 메모리: 개별 iteration의 구체적 경험
        self.episodic = EpisodicMemory(
            storage=VectorStore(),
            retention_policy='last_10_iterations'
        )
        
        # 시맨틱 메모리: 추상화된 지식과 패턴
        self.semantic = SemanticMemory(
            storage=KnowledgeGraph(),
            consolidation_interval='every_5_iterations'
        )
        
        # 프로시저럴 메모리: workflow와 절차적 지식
        self.procedural = ProceduralMemory(
            storage=RuleEngine(),
            adaptation_rate=0.1
        )
    
    def store_experience(self, iteration: IterationData) -> None:
        """
        경험 저장
        """
        # 에피소딕 메모리에 저장
        self.episodic.store(iteration)
        
        # 일정 주기로 시맨틱 메모리에 통합
        if self.should_consolidate():
            self.consolidate_to_semantic()
    
    def consolidate_to_semantic(self) -> None:
        """
        에피소딕 → 시맨틱 통합
        """
        recent_episodes = self.episodic.get_recent(k=5)
        
        # 패턴 추출
        patterns = self.extract_patterns(recent_episodes)
        
        # 지식 그래프 업데이트
        for pattern in patterns:
            self.semantic.add_knowledge(
                subject=pattern.subject,
                predicate=pattern.predicate,
                object=pattern.object,
                confidence=pattern.confidence
            )
    
    def retrieve_relevant(self, query: Query, context: Context) -> RetrievedInfo:
        """
        상황에 맞는 정보 검색
        """
        # 모든 메모리 계층에서 검색
        episodic_results = self.episodic.search(query, top_k=3)
        semantic_results = self.semantic.query(query)
        procedural_results = self.procedural.match(context)
        
        # 결과 융합
        return self.fuse_results(
            episodic=episodic_results,
            semantic=semantic_results,
            procedural=procedural_results
        )
```

---

## 7. 실행 워크플로우

### 7.1 메인 루프

```python
class MIRROREngine:
    """
    MIRROR 시스템 메인 엔진
    """
    
    def __init__(self):
        self.meta_learner = MetaLearningEngine()
        self.reflection = ReflectionEngine()
        self.version_ctrl = VersionController()
        self.judges = MultiAIJudges()
        self.agents = self.initialize_agents()
        
    def run(self, max_iterations: int = 20, target_score: float = 85) -> Submission:
        """
        메인 실행 루프
        """
        for iteration in range(1, max_iterations + 1):
            logger.info(f"=== Iteration {iteration} ===")
            
            # 1. 연구 수행
            submission = self.execute_research()
            
            # 2. 다중 AI 심사
            evaluation = self.judges.evaluate(submission)
            
            # 3. 목표 달성 확인
            if evaluation.aggregated['total'] >= target_score:
                logger.info(f"Target achieved at iteration {iteration}!")
                self.finalize(submission, evaluation)
                return submission
            
            # 4. 리플렉션
            reflection = self.reflection.reflect(
                IterationResult(
                    submission=submission,
                    evaluation=evaluation,
                    iteration=iteration
                )
            )
            
            # 5. 낸부 루프: 제출물 개선
            improved_submission = self.improve_submission(
                submission, evaluation, reflection
            )
            
            # 6. 버전 컨트롤: commit
            self.version_ctrl.commit_iteration(iteration, Changes(
                submission=improved_submission,
                evaluation=evaluation,
                reflection=reflection
            ))
            
            # 7. 메타러닝: 시스템 개선
            if iteration % 3 == 0:  # 3 iteration마다
                improvements = self.meta_learner.generate_improvements()
                self.apply_system_improvements(improvements)
            
            # 8. 학습
            self.meta_learner.learn_from_iteration(IterationData(
                iteration=iteration,
                submission=improved_submission,
                evaluation=evaluation,
                reflection=reflection
            ))
        
        # 최대 iteration 도달
        logger.warning("Max iterations reached")
        return self.get_best_submission()
    
    def execute_research(self) -> Submission:
        """
        연구 수행
        """
        # 각 에이전트가 self-improving 하게 동작
        literature = self.agents['literature'].review()
        hypothesis = self.agents['hypothesis'].generate(literature)
        data = self.agents['data'].analyze(hypothesis)
        paper = self.agents['writer'].write(data)
        ai_log = self.agents['logger'].compile()
        
        return Submission(
            paper=paper,
            ai_usage=ai_log,
            data_list=data.metadata
        )
    
    def apply_system_improvements(self, improvements: List[SystemImprovement]) -> None:
        """
        시스템 개선사항 적용
        """
        for improvement in improvements:
            logger.info(f"Applying improvement: {improvement}")
            
            if improvement.target.startswith('agent:'):
                agent_name = improvement.target.split(':')[1]
                self.agents[agent_name].apply_improvement(improvement)
            
            elif improvement.target.startswith('workflow:'):
                self.reconfigure_workflow(improvement)
            
            elif improvement.target.startswith('prompt:'):
                self.update_prompt_strategy(improvement)
```

---

## 8. 디렉토리 구조

```
ai_co_scientist_v2/
├── mirror/                          # MIRROR 시스템 코어
│   ├── __init__.py
│   ├── engine.py                    # 메인 엔진
│   ├── meta_learning.py             # 메타러닝 엔진
│   ├── reflection.py                # 리플렉션 엔진
│   ├── version_control.py           # 버전 컨트롤러
│   └── feedback_loop.py             # 피드백 루프
├── agents/                          # Self-Improving Agents
│   ├── base.py                      # 기본 클래스
│   ├── literature_agent.py          # 문헌 조사
│   ├── hypothesis_agent.py          # 가설 생성
│   ├── data_agent.py                # 데이터 분석
│   ├── writing_agent.py             # 논문 작성
│   ├── logging_agent.py             # AI 활용 로깅
│   └── judge_agents/                # AI 심사위원
│       ├── claude_judge.py
│       ├── gpt4_judge.py
│       └── gemini_judge.py
├── memory/                          # 메모리 시스템
│   ├── episodic.py                  # 에피소딕 메모리
│   ├── semantic.py                  # 시맨틱 메모리
│   └── procedural.py                # 프로시저럴 메모리
├── evaluation/                      # 평가 시스템
│   ├── rubric.py                    # 심사 기준
│   ├── multi_judge.py               # 다중 심사
│   └── gap_analyzer.py              # Gap 분석
├── prompts/                         # 프롬프트 템플릿
│   ├── templates/                   # 기본 템플릿
│   ├── strategies/                  # 전략별 프롬프트
│   └── evolved/                     # 진화된 프롬프트
├── submissions/                     # 제출물 (버전별)
│   ├── v1.0.0/                      # iteration 1
│   ├── v1.1.0/                      # iteration 2
│   └── ...
├── learning_logs/                   # 학습 로그
│   ├── episodic/                    # 에피소딕 기록
│   ├── semantic/                    # 시맨틱 지식
│   └── reflections/                 # 리플렉션 기록
├── config/                          # 설정
│   ├── agents.yaml                  # 에이전트 설정
│   ├── rubric.yaml                  # 심사 기준
│   └── models.yaml                  # 모델 설정
├── main.py                          # 실행 스크립트
├── requirements.txt
└── README.md
```

---

## 9. Commit 메시지 규약

```
[Iteration {N}] {제목}

Score: {이전} → {현재} ({변화량:+.1f})
AI Contribution: {百分比}%

## Improvements
- {개선사항 1}
- {개선사항 2}

## Agent Updates
- {에이전트명}: {변경내용}

## Reflection
{리플렉션 요약}

## Next Steps
{다음 iteration 계획}
```

---

## 10. 핵심 혁신점 요약

| 기존 시스템 | MIRROR 시스템 |
|-------------|---------------|
| 정적 에이전트 | **Self-Improving Agents** |
| 단일 피드백 루프 | **이중 루프 학습** (제출물 + 시스템) |
| No 버전 관리 | **iteration마다 commit** |
| 단일 AI 모델 | **3개 이상 다중 AI 심사** |
| Mock 데이터 | **실제 데이터 분석** |
| 고정된 프롬프트 | **진화하는 프롬프트 전략** |
| No 메타러닝 | **3계층 메모리 시스템** |

---

*이 시스템은 2026 AI Co-Scientist Challenge Korea의 Track 1 참가를 위해 설계되었습니다.*
*설계 원칙: "시스템이 연구를 수행하는 것이 아니라, 시스템이 스스로를 개선하며 연구를 수행한다"*
