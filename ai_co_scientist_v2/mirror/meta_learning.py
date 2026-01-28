#!/usr/bin/env python3
"""
Meta-Learning Engine - 메타러닝 엔진

iteration을 거치며 시스템 자체를 개선하는 메타러닝 엔진
"""

import logging
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from collections import defaultdict

logger = logging.getLogger(__name__)


@dataclass
class Pattern:
    """발견된 패턴"""
    type: str
    description: str
    frequency: int
    confidence: float
    examples: List[Any]


@dataclass
class SystemImprovement:
    """시스템 개선사항"""
    target: str
    action: str
    reason: str
    priority: str = "medium"


class MetaLearningEngine:
    """
    메타러닝 엔진
    
    - 에피소딕 메모리: 개별 iteration의 구체적 경험
    - 시맨틱 메모리: 추상화된 지식과 패턴
    - 프로시저럴 메모리: workflow와 절차적 지식
    """
    
    def __init__(self):
        # 메모리 시스템
        self.episodic_memory: List[Dict] = []  # 단기 기억
        self.semantic_memory: Dict[str, Any] = {}  # 장기 기억
        self.procedural_memory: Dict[str, Any] = {}  # 절차 기억
        
        # 패턴 저장소
        self.patterns: List[Pattern] = []
        
        # 개선 히스토리
        self.improvement_history: List[SystemImprovement] = []
        
        logger.info("MetaLearningEngine initialized")
    
    def learn_from_iteration(self, iteration_data: Any) -> None:
        """
        iteration으로부터 학습
        
        Args:
            iteration_data: IterationData 객체
        """
        logger.info(f"Learning from iteration {iteration_data.iteration}")
        
        # 1. 에피소딕 메모리 저장
        self._store_episodic(iteration_data)
        
        # 2. 패턴 추출 및 시맨틱 메모리 업데이트
        if len(self.episodic_memory) >= 3:
            self._consolidate_to_semantic()
        
        # 3. 프로시저럴 메모리 업데이트
        self._update_procedural_memory(iteration_data)
    
    def _store_episodic(self, iteration_data: Any) -> None:
        """에피소딕 메모리에 저장"""
        episode = {
            'iteration': iteration_data.iteration,
            'score': iteration_data.evaluation.get('total_score', 0),
            'scores': iteration_data.evaluation.get('aggregated', {}),
            'improvements': iteration_data.reflection.get('improvements', []),
            'weaknesses': iteration_data.reflection.get('weaknesses', []),
            'success': iteration_data.evaluation.get('total_score', 0) >= 85
        }
        
        self.episodic_memory.append(episode)
        
        # 최근 10개만 유지
        if len(self.episodic_memory) > 10:
            self.episodic_memory.pop(0)
        
        logger.debug(f"Stored episode: iteration {episode['iteration']}, score {episode['score']}")
    
    def _consolidate_to_semantic(self) -> None:
        """에피소딕 → 시맨틱 통합"""
        logger.info("Consolidating to semantic memory...")
        
        # 패턴 추출
        patterns = self._extract_patterns()
        
        # 시맨틱 메모리 업데이트
        for pattern in patterns:
            key = f"{pattern.type}:{pattern.description[:50]}"
            
            if key in self.semantic_memory:
                # 기존 패턴 강화
                self.semantic_memory[key]['frequency'] += pattern.frequency
                self.semantic_memory[key]['confidence'] = min(0.95, 
                    self.semantic_memory[key]['confidence'] + 0.05)
            else:
                # 새로운 패턴 추가
                self.semantic_memory[key] = {
                    'type': pattern.type,
                    'description': pattern.description,
                    'frequency': pattern.frequency,
                    'confidence': pattern.confidence,
                    'first_seen': len(self.episodic_memory)
                }
        
        logger.info(f"Semantic memory now has {len(self.semantic_memory)} patterns")
    
    def _extract_patterns(self) -> List[Pattern]:
        """패턴 추출"""
        patterns = []
        
        # 1. 반복적인 약점 패턴
        weakness_patterns = self._extract_weakness_patterns()
        patterns.extend(weakness_patterns)
        
        # 2. 성공/실패 패턴
        outcome_patterns = self._extract_outcome_patterns()
        patterns.extend(outcome_patterns)
        
        # 3. 개선 효과 패턴
        improvement_patterns = self._extract_improvement_patterns()
        patterns.extend(improvement_patterns)
        
        return patterns
    
    def _extract_weakness_patterns(self) -> List[Pattern]:
        """약점 패턴 추출"""
        weakness_count = defaultdict(int)
        
        for episode in self.episodic_memory:
            for weakness in episode.get('weaknesses', []):
                category = weakness.get('category', 'unknown')
                weakness_count[category] += 1
        
        patterns = []
        for category, count in weakness_count.items():
            if count >= 2:  # 2회 이상 반복
                patterns.append(Pattern(
                    type='recurring_weakness',
                    description=f"Recurring weakness in {category}",
                    frequency=count,
                    confidence=min(0.9, count * 0.2),
                    examples=[]
                ))
        
        return patterns
    
    def _extract_outcome_patterns(self) -> List[Pattern]:
        """성공/실패 패턴 추출"""
        if len(self.episodic_memory) < 2:
            return []
        
        patterns = []
        
        # 연속된 성공/실패 패턴
        recent = self.episodic_memory[-3:]
        scores = [e['score'] for e in recent]
        
        if all(s < 70 for s in scores):
            patterns.append(Pattern(
                type='consecutive_failure',
                description="Consecutive low scores, need major strategy change",
                frequency=3,
                confidence=0.8,
                examples=scores
            ))
        elif all(s >= 80 for s in scores):
            patterns.append(Pattern(
                type='consecutive_success',
                description="Consecutive high scores, current strategy working",
                frequency=3,
                confidence=0.85,
                examples=scores
            ))
        
        return patterns
    
    def _extract_improvement_patterns(self) -> List[Pattern]:
        """개선 효과 패턴 추출"""
        if len(self.episodic_memory) < 2:
            return []
        
        patterns = []
        
        # 점수 변화 추이
        scores = [e['score'] for e in self.episodic_memory]
        
        if len(scores) >= 3:
            # 상승 추세
            if scores[-1] > scores[-2] > scores[-3]:
                patterns.append(Pattern(
                    type='improving_trend',
                    description="Score consistently improving",
                    frequency=3,
                    confidence=0.75,
                    examples=scores[-3:]
                ))
            # 하띋 추세
            elif scores[-1] < scores[-2] < scores[-3]:
                patterns.append(Pattern(
                    type='declining_trend',
                    description="Score consistently declining",
                    frequency=3,
                    confidence=0.75,
                    examples=scores[-3:]
                ))
        
        return patterns
    
    def _update_procedural_memory(self, iteration_data: Any) -> None:
        """프로시저럴 메모리 업데이트"""
        success = iteration_data.evaluation.get('total_score', 0) >= 85
        
        # 성공한 workflow 강화
        if success:
            for improvement in iteration_data.reflection.get('improvements', []):
                action = improvement.get('action')
                if action:
                    if action not in self.procedural_memory:
                        self.procedural_memory[action] = {'success_count': 0, 'failure_count': 0}
                    self.procedural_memory[action]['success_count'] += 1
        else:
            # 실패한 workflow 약화
            for improvement in iteration_data.reflection.get('improvements', []):
                action = improvement.get('action')
                if action:
                    if action not in self.procedural_memory:
                        self.procedural_memory[action] = {'success_count': 0, 'failure_count': 0}
                    self.procedural_memory[action]['failure_count'] += 1
    
    def analyze_patterns(self, iteration_history: List[Any]) -> Dict[str, Any]:
        """iteration 히스토리에서 패턴 분석"""
        logger.info("Analyzing patterns from iteration history...")
        
        patterns = {
            'score_trend': self._analyze_score_trend(iteration_history),
            'bottlenecks': self._identify_bottlenecks(iteration_history),
            'successful_strategies': self._identify_successful_strategies(),
            'failed_strategies': self._identify_failed_strategies()
        }
        
        return patterns
    
    def _analyze_score_trend(self, history: List[Any]) -> Dict[str, Any]:
        """점수 추이 분석"""
        scores = [h.evaluation.get('total_score', 0) for h in history]
        
        if len(scores) < 2:
            return {'trend': 'insufficient_data'}
        
        import numpy as np
        
        trend = np.polyfit(range(len(scores)), scores, 1)[0]
        
        if trend > 2:
            return {'trend': 'improving', 'slope': trend, 'scores': scores}
        elif trend < -2:
            return {'trend': 'declining', 'slope': trend, 'scores': scores}
        else:
            return {'trend': 'stable', 'slope': trend, 'scores': scores}
    
    def _identify_bottlenecks(self, history: List[Any]) -> List[Dict]:
        """병목 지점 식별"""
        bottlenecks = []
        
        # 심사 기준별 평균 점수
        criterion_scores = defaultdict(list)
        
        for h in history:
            aggregated = h.evaluation.get('aggregated', {})
            for criterion, score in aggregated.items():
                if isinstance(score, (int, float)):
                    criterion_scores[criterion].append(score)
        
        # 가장 낮은 평균 점수를 가진 기준 식별
        for criterion, scores in criterion_scores.items():
            if scores:
                avg_score = sum(scores) / len(scores)
                max_possible = {'practicality': 20, 'methodology': 20, 'data_quality': 25, 
                              'conclusion': 10, 'readability': 5, 'creativity': 20}.get(criterion, 20)
                
                if avg_score < max_possible * 0.7:  # 70% 미만
                    bottlenecks.append({
                        'criterion': criterion,
                        'average_score': avg_score,
                        'max_possible': max_possible,
                        'severity': 'high' if avg_score < max_possible * 0.5 else 'medium'
                    })
        
        return sorted(bottlenecks, key=lambda x: x['average_score'])
    
    def _identify_successful_strategies(self) -> List[str]:
        """성공한 전략 식별"""
        successful = []
        
        for action, counts in self.procedural_memory.items():
            success_rate = counts['success_count'] / (counts['success_count'] + counts['failure_count'] + 1e-6)
            if success_rate > 0.7 and counts['success_count'] >= 2:
                successful.append(action)
        
        return successful
    
    def _identify_failed_strategies(self) -> List[str]:
        """실패한 전략 식별"""
        failed = []
        
        for action, counts in self.procedural_memory.items():
            success_rate = counts['success_count'] / (counts['success_count'] + counts['failure_count'] + 1e-6)
            if success_rate < 0.3 and counts['failure_count'] >= 2:
                failed.append(action)
        
        return failed
    
    def generate_improvements(self, patterns: Dict[str, Any]) -> List[SystemImprovement]:
        """개선사항 생성"""
        logger.info("Generating system improvements...")
        
        improvements = []
        
        # 1. 병목 개선
        for bottleneck in patterns.get('bottlenecks', []):
            criterion = bottleneck['criterion']
            severity = bottleneck['severity']
            
            improvements.append(SystemImprovement(
                target=f'agent:{criterion}_agent',
                action='enhance_capabilities',
                reason=f"{criterion} is a bottleneck with avg score {bottleneck['average_score']:.1f}/{bottleneck['max_possible']}",
                priority=severity
            ))
        
        # 2. 추세 기반 개선
        trend = patterns.get('score_trend', {}).get('trend')
        
        if trend == 'declining':
            improvements.append(SystemImprovement(
                target='workflow',
                action='major_redesign',
                reason="Score consistently declining, need major workflow redesign",
                priority='high'
            ))
        elif trend == 'stable':
            improvements.append(SystemImprovement(
                target='prompt',
                action='explore_new_strategies',
                reason="Score stable but not improving, need to explore new strategies",
                priority='medium'
            ))
        
        # 3. 성공한 전략 강화
        successful = patterns.get('successful_strategies', [])
        for strategy in successful:
            improvements.append(SystemImprovement(
                target='workflow',
                action=f'reinforce:{strategy}',
                reason=f"Strategy '{strategy}' has been successful",
                priority='low'
            ))
        
        self.improvement_history.extend(improvements)
        
        return improvements
    
    def get_knowledge_summary(self) -> Dict[str, Any]:
        """학습된 지식 요약"""
        return {
            'episodes_stored': len(self.episodic_memory),
            'semantic_patterns': len(self.semantic_memory),
            'procedural_rules': len(self.procedural_memory),
            'improvements_made': len(self.improvement_history),
            'top_patterns': sorted(
                self.semantic_memory.items(),
                key=lambda x: x[1].get('confidence', 0),
                reverse=True
            )[:5]
        }
