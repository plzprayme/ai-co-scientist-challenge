#!/usr/bin/env python3
"""
Self-Improving Agent Base Class

스스로 개선하는 에이전트의 기본 클래스
"""

import logging
from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional
from datetime import datetime

logger = logging.getLogger(__name__)


class SelfImprovingAgent(ABC):
    """
    스스로 개선하는 에이전트 기본 클래스
    
    Features:
    - 버전 관리 (Semantic Versioning)
    - 성능 기록
    - 프롬프트 전략 최적화
    - 피드백 기반 개선
    """
    
    def __init__(self, name: str):
        self.name = name
        self.version = "1.0.0"
        self.performance_history: List[Dict] = []
        self.prompt_strategies: List[Dict] = []
        self.current_strategy: Optional[Dict] = None
        self.improvement_count = 0
        
        logger.info(f"Agent '{name}' initialized (v{self.version})")
    
    @abstractmethod
    def execute(self, task: Any) -> Any:
        """
        에이전트의 핵심 실행 로직
        
        Args:
            task: 수행할 작업
            
        Returns:
            실행 결과
        """
        pass
    
    def improve(self, feedback: Dict[str, Any]) -> None:
        """
        피드백을 받아 스스로 개선
        
        Args:
            feedback: 개선 피드백
                - score: 성능 점수 (0-1)
                - weaknesses: 약점 목록
                - suggestions: 개선 제안
        """
        score = feedback.get('score', 0)
        
        # 성능 기록
        self.performance_history.append({
            'timestamp': datetime.now().isoformat(),
            'score': score,
            'feedback': feedback,
            'strategy': self.current_strategy,
            'version': self.version
        })
        
        logger.info(f"Agent '{self.name}' improving (score: {score:.2f})")
        
        # 점수가 낮으면 개선
        if score < 0.7:  # 70% 미만
            self._adapt_strategy(feedback)
            self._optimize_prompt(feedback)
            self._update_version()
            self.improvement_count += 1
    
    def _adapt_strategy(self, feedback: Dict[str, Any]) -> None:
        """
        전략 적응
        
        피드백을 분석하여 새로운 전략 생성
        """
        weaknesses = feedback.get('weaknesses', [])
        
        # 실패 패턴 분석
        patterns = self._analyze_failure_patterns()
        
        # 새로운 전략 생성
        new_strategy = {
            'name': f'strategy_v{len(self.prompt_strategies) + 1}',
            'created_at': datetime.now().isoformat(),
            'triggered_by': weaknesses,
            'approach': self._generate_new_approach(patterns),
            'tested': False
        }
        
        # 전략 테스트 및 적용
        if self._test_strategy(new_strategy):
            self.current_strategy = new_strategy
            self.prompt_strategies.append(new_strategy)
            logger.info(f"New strategy adopted: {new_strategy['name']}")
    
    def _analyze_failure_patterns(self) -> List[str]:
        """실패 패턴 분석"""
        if len(self.performance_history) < 3:
            return []
        
        patterns = []
        recent = self.performance_history[-3:]
        
        # 연속된 낮은 점수
        if all(p['score'] < 0.6 for p in recent):
            patterns.append('consecutive_low_scores')
        
        # 점수 하띋 추세
        if recent[0]['score'] > recent[1]['score'] > recent[2]['score']:
            patterns.append('declining_trend')
        
        return patterns
    
    def _generate_new_approach(self, patterns: List[str]) -> str:
        """새로운 접근법 생성"""
        if 'consecutive_low_scores' in patterns:
            return 'drastic_change'
        elif 'declining_trend' in patterns:
            return 'incremental_improvement'
        else:
            return 'explore_alternatives'
    
    def _test_strategy(self, strategy: Dict) -> bool:
        """전략 테스트"""
        # 실제로는 A/B 테스트나 시뮬레이션
        # 여기서는 간단히 항상 True 반환
        strategy['tested'] = True
        return True
    
    def _optimize_prompt(self, feedback: Dict[str, Any]) -> None:
        """
        프롬프트 최적화
        
        피드백 유형에 따라 프롬프트 조정
        """
        feedback_type = feedback.get('type', 'general')
        
        if feedback_type == 'fewshot_insufficient':
            self._add_fewshot_examples(feedback.get('examples', []))
        
        elif feedback_type == 'reasoning_unclear':
            self._enhance_cot_prompt()
        
        elif feedback_type == 'context_overflow':
            self._adjust_context_window()
        
        elif feedback_type == 'output_format_error':
            self._refine_output_format()
    
    def _add_fewshot_examples(self, examples: List[Any]) -> None:
        """Few-shot 예제 추가"""
        logger.info(f"Adding {len(examples)} few-shot examples")
    
    def _enhance_cot_prompt(self) -> None:
        """Chain-of-Thought 프롬프트 강화"""
        logger.info("Enhancing Chain-of-Thought prompt")
    
    def _adjust_context_window(self) -> None:
        """컨텍스트 윈도우 조정"""
        logger.info("Adjusting context window")
    
    def _refine_output_format(self) -> None:
        """출력 형식 정제"""
        logger.info("Refining output format")
    
    def _update_version(self) -> None:
        """
        Semantic versioning
        
        Major: 아키텍처 변경
        Minor: 전략 변경
        Patch: 프롬프트 조정
        """
        parts = self.version.split('.')
        major, minor, patch = int(parts[0]), int(parts[1]), int(parts[2])
        
        # 개선 유형에 따라 버전 업데이트
        if self._architecture_changed():
            major += 1
            minor = 0
            patch = 0
        elif self._strategy_changed():
            minor += 1
            patch = 0
        else:
            patch += 1
        
        old_version = self.version
        self.version = f"{major}.{minor}.{patch}"
        
        logger.info(f"Version updated: {old_version} → {self.version}")
    
    def _architecture_changed(self) -> bool:
        """아키텍처 변경 여부"""
        # 5회 이상 개선되면 아키텍처 변경으로 간주
        return self.improvement_count >= 5
    
    def _strategy_changed(self) -> bool:
        """전략 변경 여부"""
        # 새로운 전략이 추가되었는지 확인
        return len(self.prompt_strategies) > 0
    
    def apply_improvement(self, improvement: Any) -> None:
        """
        외부에서 제안된 개선사항 적용
        
        Args:
            improvement: 개선사항
        """
        logger.info(f"Applying improvement: {improvement}")
        
        # 개선사항 유형에 따라 처리
        action = getattr(improvement, 'action', str(improvement))
        
        if 'decompose' in action:
            self._decompose_agent()
        elif 'parallelize' in action:
            self._parallelize_workflow()
        elif 'enhance' in action:
            self._enhance_capabilities()
    
    def _decompose_agent(self) -> None:
        """에이전트 분해"""
        logger.info(f"Decomposing agent '{self.name}'")
    
    def _parallelize_workflow(self) -> None:
        """Workflow 병렬화"""
        logger.info(f"Parallelizing workflow for '{self.name}'")
    
    def _enhance_capabilities(self) -> None:
        """능력 강화"""
        logger.info(f"Enhancing capabilities of '{self.name}'")
    
    def get_stats(self) -> Dict[str, Any]:
        """에이전트 통계"""
        if not self.performance_history:
            return {
                'name': self.name,
                'version': self.version,
                'message': 'No performance data yet'
            }
        
        scores = [p['score'] for p in self.performance_history]
        
        return {
            'name': self.name,
            'version': self.version,
            'improvement_count': self.improvement_count,
            'total_executions': len(self.performance_history),
            'average_score': sum(scores) / len(scores),
            'best_score': max(scores),
            'worst_score': min(scores),
            'strategies_tested': len(self.prompt_strategies),
            'current_strategy': self.current_strategy.get('name') if self.current_strategy else None
        }
