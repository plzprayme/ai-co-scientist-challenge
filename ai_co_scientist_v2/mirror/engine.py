#!/usr/bin/env python3
"""
MIRROR Engine - 메인 실행 엔진
"""

import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field

from .meta_learning import MetaLearningEngine
from .reflection import ReflectionEngine
from .version_control import VersionController

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class IterationData:
    """iteration 데이터"""
    iteration: int
    submission: Dict[str, Any]
    evaluation: Dict[str, Any]
    reflection: Dict[str, Any]
    timestamp: datetime = field(default_factory=datetime.now)


@dataclass
class SystemImprovement:
    """시스템 개선사항"""
    target: str
    action: str
    reason: str
    priority: str = "medium"


class MIRROREngine:
    """
    MIRROR 시스템 메인 엔진
    
    이중 루프 학습:
    - 낸부 루프: 제출물 품질 개선
    - 외부 루프: 에이전트 시스템 자체 개선
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.iteration = 0
        self.max_iterations = self.config.get('max_iterations', 20)
        self.target_score = self.config.get('target_score', 85)
        
        # 핵심 컴포넌트
        self.meta_learner = MetaLearningEngine()
        self.reflection = ReflectionEngine()
        self.version_ctrl = VersionController()
        
        # 에이전트 레지스트리
        self.agents: Dict[str, Any] = {}
        
        # 히스토리
        self.iteration_history: List[IterationData] = []
        self.best_score = 0
        self.best_submission = None
        
        logger.info("MIRROR Engine initialized")
        logger.info(f"Target score: {self.target_score}, Max iterations: {self.max_iterations}")
    
    def register_agent(self, name: str, agent: Any) -> None:
        """에이전트 등록"""
        self.agents[name] = agent
        logger.info(f"Agent '{name}' registered (v{getattr(agent, 'version', '1.0.0')})")
    
    def run(self) -> Dict[str, Any]:
        """
        메인 실행 루프
        
        Returns:
            최종 제출물
        """
        logger.info("=" * 60)
        logger.info("MIRROR Engine Starting")
        logger.info("=" * 60)
        
        for iteration in range(1, self.max_iterations + 1):
            self.iteration = iteration
            
            logger.info("")
            logger.info(f"{'='*60}")
            logger.info(f"ITERATION {iteration}/{self.max_iterations}")
            logger.info(f"{'='*60}")
            
            # 1. 연구 수행
            submission = self._execute_research()
            
            # 2. 다중 AI 심사 (3개 모델)
            evaluation = self._multi_judge_evaluation(submission)
            
            current_score = evaluation.get('total_score', 0)
            logger.info(f"Current score: {current_score}/{self.target_score}")
            
            # 3. 목표 달성 확인
            if current_score >= self.target_score:
                logger.info(f"✅ TARGET ACHIEVED at iteration {iteration}!")
                return self._finalize(submission, evaluation)
            
            # 4. 리플렉션
            reflection = self._reflect(submission, evaluation)
            
            # 5. 낸부 루프: 제출물 개선
            improved_submission = self._improve_submission(
                submission, evaluation, reflection
            )
            
            # 6. 버전 컨트롤: commit
            self._commit_iteration(iteration, improved_submission, evaluation, reflection)
            
            # 7. 히스토리 저장
            self.iteration_history.append(IterationData(
                iteration=iteration,
                submission=improved_submission,
                evaluation=evaluation,
                reflection=reflection
            ))
            
            # 8. 외부 루프: 메타러닝 (3 iteration마다)
            if iteration % 3 == 0:
                logger.info("Running meta-learning...")
                improvements = self._meta_learn()
                self._apply_system_improvements(improvements)
            
            # 9. 메타러닝: 개별 iteration 학습
            self.meta_learner.learn_from_iteration(self.iteration_history[-1])
            
            # 최고 점수 업데이트
            if current_score > self.best_score:
                self.best_score = current_score
                self.best_submission = submission
                logger.info(f"New best score: {self.best_score}")
        
        # 최대 iteration 도달
        logger.warning(f"Max iterations ({self.max_iterations}) reached")
        logger.info(f"Best score achieved: {self.best_score}")
        return self._finalize(self.best_submission, {})
    
    def _execute_research(self) -> Dict[str, Any]:
        """연구 수행"""
        logger.info("Executing research...")
        
        # 각 에이전트가 self-improving 하게 동작
        results = {}
        
        if 'literature' in self.agents:
            results['literature'] = self.agents['literature'].review()
        
        if 'hypothesis' in self.agents:
            results['hypothesis'] = self.agents['hypothesis'].generate(
                results.get('literature', {})
            )
        
        if 'data' in self.agents:
            results['data'] = self.agents['data'].analyze(
                results.get('hypothesis', {})
            )
        
        if 'writer' in self.agents:
            results['paper'] = self.agents['writer'].write(
                results.get('data', {})
            )
        
        if 'logger' in self.agents:
            results['ai_usage'] = self.agents['logger'].compile()
        
        return results
    
    def _multi_judge_evaluation(self, submission: Dict[str, Any]) -> Dict[str, Any]:
        """
        다중 AI 심사 (3개 모델 이상)
        
        대회 요구사항: "다중 AI 패널 심사(3개 모델 이상 활용)"
        """
        logger.info("Multi-AI judge evaluation...")
        
        # 3개 AI 모델로 평가
        judges = ['claude', 'gpt4', 'gemini']
        results = {}
        
        for judge in judges:
            if judge in self.agents:
                results[judge] = self.agents[judge].evaluate(submission)
            else:
                # Mock evaluation for testing
                results[judge] = self._mock_evaluation(submission, judge)
        
        # 결과 집계
        aggregated = self._aggregate_judge_results(results)
        
        return {
            'individual': results,
            'aggregated': aggregated,
            'total_score': aggregated.get('total', 0)
        }
    
    def _mock_evaluation(self, submission: Dict[str, Any], judge: str) -> Dict[str, float]:
        """Mock evaluation for testing"""
        import random
        base_score = 60 + random.random() * 25
        return {
            'practicality': min(20, base_score * 0.2),
            'methodology': min(20, base_score * 0.2),
            'data_quality': min(25, base_score * 0.25),
            'conclusion': min(10, base_score * 0.1),
            'readability': min(5, base_score * 0.05),
            'creativity': min(20, base_score * 0.2),
            'ai_contribution': 'PASS' if random.random() > 0.3 else 'FAIL',
            'total': base_score
        }
    
    def _aggregate_judge_results(self, results: Dict[str, Dict]) -> Dict[str, float]:
        """심사 결과 집계 (중앙값 사용)"""
        import numpy as np
        
        aggregated = {}
        criteria = ['practicality', 'methodology', 'data_quality', 'conclusion', 'readability', 'creativity']
        
        for criterion in criteria:
            scores = [r.get(criterion, 0) for r in results.values()]
            aggregated[criterion] = round(np.median(scores), 1)
        
        # AI 기여도는 모두 PASS여야 PASS
        ai_contributions = [r.get('ai_contribution', 'FAIL') for r in results.values()]
        aggregated['ai_contribution'] = 'PASS' if all(a == 'PASS' for a in ai_contributions) else 'FAIL'
        
        aggregated['total'] = sum(aggregated[c] for c in criteria)
        
        return aggregated
    
    def _reflect(self, submission: Dict[str, Any], evaluation: Dict[str, Any]) -> Dict[str, Any]:
        """리플렉션 수행"""
        logger.info("Reflecting on iteration...")
        return self.reflection.reflect(submission, evaluation)
    
    def _improve_submission(self, submission: Dict[str, Any], 
                           evaluation: Dict[str, Any],
                           reflection: Dict[str, Any]) -> Dict[str, Any]:
        """제출물 개선 (낸부 루프)"""
        logger.info("Improving submission...")
        
        # 개선 전략 생성
        improvements = reflection.get('improvements', [])
        
        # 각 개선사항 적용
        improved = submission.copy()
        
        for improvement in improvements:
            target = improvement.get('target')
            action = improvement.get('action')
            
            logger.info(f"  Applying: {action} to {target}")
            
            # 해당 에이전트에게 개선 요청
            if target in self.agents:
                improved[target] = self.agents[target].improve(
                    improved.get(target, {}),
                    improvement
                )
        
        return improved
    
    def _commit_iteration(self, iteration: int, submission: Dict[str, Any],
                         evaluation: Dict[str, Any], reflection: Dict[str, Any]) -> None:
        """iteration commit"""
        logger.info(f"Committing iteration {iteration}...")
        
        commit_info = {
            'iteration': iteration,
            'score': evaluation.get('total_score', 0),
            'improvements': reflection.get('improvements', []),
            'timestamp': datetime.now().isoformat()
        }
        
        self.version_ctrl.commit(commit_info)
    
    def _meta_learn(self) -> List[SystemImprovement]:
        """메타러닝 수행 (외부 루프)"""
        logger.info("Meta-learning from iteration history...")
        
        # 패턴 분석
        patterns = self.meta_learner.analyze_patterns(self.iteration_history)
        
        # 개선사항 생성
        improvements = self.meta_learner.generate_improvements(patterns)
        
        logger.info(f"Generated {len(improvements)} system improvements")
        
        return improvements
    
    def _apply_system_improvements(self, improvements: List[SystemImprovement]) -> None:
        """시스템 개선사항 적용"""
        logger.info("Applying system improvements...")
        
        for improvement in improvements:
            logger.info(f"  [{improvement.priority.upper()}] {improvement.target}: {improvement.action}")
            
            target = improvement.target
            
            if target.startswith('agent:'):
                agent_name = target.split(':')[1]
                if agent_name in self.agents:
                    self.agents[agent_name].apply_improvement(improvement)
            
            elif target == 'workflow':
                self._reconfigure_workflow(improvement)
            
            elif target == 'prompt':
                self._update_prompt_strategy(improvement)
    
    def _reconfigure_workflow(self, improvement: SystemImprovement) -> None:
        """Workflow 재구성"""
        logger.info(f"Reconfiguring workflow: {improvement.action}")
    
    def _update_prompt_strategy(self, improvement: SystemImprovement) -> None:
        """프롬프트 전략 업데이트"""
        logger.info(f"Updating prompt strategy: {improvement.action}")
    
    def _finalize(self, submission: Dict[str, Any], evaluation: Dict[str, Any]) -> Dict[str, Any]:
        """최종 제출물 준비"""
        logger.info("Finalizing submission...")
        
        # 제출물 패키징
        final = {
            'research_paper': submission.get('paper', {}),
            'ai_usage_report': submission.get('ai_usage', {}),
            'data_list': submission.get('data', {}).get('metadata', {}),
            'evaluation': evaluation,
            'iteration_count': self.iteration,
            'final_score': evaluation.get('total_score', 0),
            'timestamp': datetime.now().isoformat()
        }
        
        # 저장
        self._save_final_submission(final)
        
        return final
    
    def _save_final_submission(self, final: Dict[str, Any]) -> None:
        """최종 제출물 저장"""
        output_dir = Path('submissions')
        output_dir.mkdir(exist_ok=True)
        
        import json
        with open(output_dir / 'final_submission.json', 'w', encoding='utf-8') as f:
            json.dump(final, f, ensure_ascii=False, indent=2)
        
        logger.info(f"Final submission saved to {output_dir / 'final_submission.json'}")
    
    def get_stats(self) -> Dict[str, Any]:
        """실행 통계"""
        return {
            'total_iterations': self.iteration,
            'best_score': self.best_score,
            'improvement_count': len(self.iteration_history),
            'agent_versions': {name: getattr(agent, 'version', '1.0.0') 
                             for name, agent in self.agents.items()}
        }
