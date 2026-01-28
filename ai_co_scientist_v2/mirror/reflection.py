#!/usr/bin/env python3
"""
Reflection Engine - 리플렉션 엔진

iteration 결과를 분석하고 insight를 추출하는 리플렉션 엔진
"""

import logging
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from datetime import datetime

logger = logging.getLogger(__name__)


@dataclass
class Weakness:
    """식별된 약점"""
    category: str
    score: float
    max_score: float
    gap: float
    possible_causes: List[str]
    suggested_fixes: List[str]


@dataclass
class Improvement:
    """개선사항"""
    target: str
    action: str
    description: str
    expected_impact: str
    priority: str = "medium"


@dataclass
class ReflectionReport:
    """리플렉션 보고서"""
    timestamp: datetime = field(default_factory=datetime.now)
    overall_score: float = 0
    score_change: float = 0
    weaknesses: List[Weakness] = field(default_factory=list)
    improvements: List[Improvement] = field(default_factory=list)
    insights: List[str] = field(default_factory=list)
    next_steps: List[str] = field(default_factory=list)


class ReflectionEngine:
    """
    리플렉션 엔진
    
    iteration 결과를 분석하여:
    1. 약점 식별
    2. 개선사항 생성
    3. 학습 포인트 추출
    """
    
    # 심사 기준 정의
    RUBRIC = {
        'practicality': {'max': 20, 'name': '주제의 실용성'},
        'methodology': {'max': 20, 'name': '방법론의 적절성'},
        'data_quality': {'max': 25, 'name': '데이터의 적절성'},
        'conclusion': {'max': 10, 'name': '결론의 합리성'},
        'readability': {'max': 5, 'name': '전달력 및 가독성'},
        'creativity': {'max': 20, 'name': '연구의 창의성 및 참신성'}
    }
    
    def __init__(self):
        self.reflection_history: List[ReflectionReport] = []
        logger.info("ReflectionEngine initialized")
    
    def reflect(self, submission: Dict[str, Any], evaluation: Dict[str, Any]) -> Dict[str, Any]:
        """
        iteration에 대한 리플렉션 수행
        
        Args:
            submission: 제출물
            evaluation: 평가 결과
            
        Returns:
            리플렉션 보고서
        """
        logger.info("Reflecting on iteration...")
        
        report = ReflectionReport()
        
        # 1. 전체 점수 분석
        aggregated = evaluation.get('aggregated', {})
        report.overall_score = evaluation.get('total_score', 0)
        
        # 2. 약점 식별
        report.weaknesses = self._identify_weaknesses(aggregated)
        
        # 3. 개선사항 생성
        report.improvements = self._generate_improvements(report.weaknesses)
        
        # 4. 인사이트 추출
        report.insights = self._extract_insights(submission, evaluation, report.weaknesses)
        
        # 5. 다음 단계 제안
        report.next_steps = self._suggest_next_steps(report)
        
        # 히스토리 저장
        self.reflection_history.append(report)
        
        return self._report_to_dict(report)
    
    def _identify_weaknesses(self, scores: Dict[str, Any]) -> List[Weakness]:
        """약점 식별"""
        weaknesses = []
        
        for criterion, info in self.RUBRIC.items():
            score = scores.get(criterion, 0)
            max_score = info['max']
            
            # 80% 미만이면 약점으로 간주
            if score < max_score * 0.8:
                gap = max_score - score
                
                weakness = Weakness(
                    category=criterion,
                    score=score,
                    max_score=max_score,
                    gap=gap,
                    possible_causes=self._investigate_cause(criterion, score),
                    suggested_fixes=self._suggest_fixes(criterion, score)
                )
                
                weaknesses.append(weakness)
                logger.debug(f"Weakness identified: {criterion} ({score}/{max_score})")
        
        # AI 기여도 체크
        ai_contribution = scores.get('ai_contribution', 'FAIL')
        if ai_contribution == 'FAIL':
            weaknesses.append(Weakness(
                category='ai_contribution',
                score=0,
                max_score=100,
                gap=100,
                possible_causes=[
                    'AI 활용 로그 불충분',
                    'AI 기여도 자체 평가 미흡',
                    '3개 이상 AI 모델 활용 증거 부족'
                ],
                suggested_fixes=[
                    'AI 활용보고서 상세화',
                    '모든 AI 상호작용 로깅',
                    'Claude, GPT-4, Gemini 3개 모델 활용'
                ]
            ))
        
        return sorted(weaknesses, key=lambda w: w.gap, reverse=True)
    
    def _investigate_cause(self, criterion: str, score: float) -> List[str]:
        """약점의 가능한 원인 조사"""
        causes = {
            'practicality': [
                '연구 주제가 실제 문제를 다루지 않음',
                '사회적/학문적 가치 제시 미흡',
                '기존 연구와의 차별점 불분명'
            ],
            'methodology': [
                '연구 방법론이 명확하지 않음',
                '실험 설계가 과학적 기준에 미달',
                '데이터 처리 방법의 문제',
                '통계 방법 부적절'
            ],
            'data_quality': [
                '데이터가 논리적이지 않음',
                '결론이 데이터와 일치하지 않음',
                '데이터 신뢰성 문제',
                '샘플 크기 부족'
            ],
            'conclusion': [
                '결론이 과학적 사실에 부합하지 않음',
                '입증이 충분하지 않음',
                '한계점 논의 미흡'
            ],
            'readability': [
                '영문 표현이 명확하지 않음',
                '논리적 흐름이 자연스럽지 않음',
                '전문 용어 사용 부적절'
            ],
            'creativity': [
                '기존 방법론과 차별화 부족',
                'AI 활용 방법이 참신하지 않음',
                '기존 연구와 유사성 높음'
            ]
        }
        
        return causes.get(criterion, ['원인 분석 필요'])
    
    def _suggest_fixes(self, criterion: str, score: float) -> List[str]:
        """개선 방안 제안"""
        fixes = {
            'practicality': [
                '실제 사례 추가',
                '사회적 영향력 강조',
                '기존 연구와의 명확한 차별화',
                '응용 가능성 제시'
            ],
            'methodology': [
                '방법론 섹션 상세화',
                '통계적 가정 검증',
                '대조군 설정',
                '재현성 확보를 위한 상세 기술'
            ],
            'data_quality': [
                '데이터 전처리 과정 문서화',
                '이상치 처리 방법 명시',
                '추가 데이터 수집',
                '교차 검증 수행'
            ],
            'conclusion': [
                '결론이 데이터를 직접 지지하도록 수정',
                '한계점 명확히 논의',
                '미래 연구 방향 제시',
                '실무 적용 방안 제안'
            ],
            'readability': [
                '영문 교정',
                '논리적 구조 개선',
                '시각적 자료 추가',
                '전문 용어 일관성 확보'
            ],
            'creativity': [
                '혁신적인 AI 활용 방법 탐색',
                '멀티모달 AI 활용',
                '기존에 없던 접근법 시도',
                '도메인 특화 AI 도구 개발'
            ]
        }
        
        return fixes.get(criterion, ['개선 방안 필요'])
    
    def _generate_improvements(self, weaknesses: List[Weakness]) -> List[Improvement]:
        """개선사항 생성"""
        improvements = []
        
        for weakness in weaknesses:
            # 우선순위 결정
            if weakness.gap > weakness.max_score * 0.5:
                priority = "high"
            elif weakness.gap > weakness.max_score * 0.3:
                priority = "medium"
            else:
                priority = "low"
            
            # 개선사항 생성
            for fix in weakness.suggested_fixes[:2]:  # 상위 2개만
                improvement = Improvement(
                    target=weakness.category,
                    action=fix,
                    description=f"Improve {weakness.category}: {fix}",
                    expected_impact=f"+{weakness.gap * 0.5:.1f} points",
                    priority=priority
                )
                improvements.append(improvement)
        
        return improvements
    
    def _extract_insights(self, submission: Dict[str, Any], 
                         evaluation: Dict[str, Any],
                         weaknesses: List[Weakness]) -> List[str]:
        """인사이트 추출"""
        insights = []
        
        # 강점 인식
        aggregated = evaluation.get('aggregated', {})
        for criterion, info in self.RUBRIC.items():
            score = aggregated.get(criterion, 0)
            if score >= info['max'] * 0.9:  # 90% 이상
                insights.append(f"Strength: {info['name']} is excellent ({score}/{info['max']})")
        
        # 개선 추세 인식
        if len(self.reflection_history) >= 2:
            prev_score = self.reflection_history[-1].overall_score
            curr_score = evaluation.get('total_score', 0)
            
            if curr_score > prev_score:
                insights.append(f"Improving trend: +{curr_score - prev_score:.1f} points from last iteration")
            elif curr_score < prev_score:
                insights.append(f"Declining trend: {curr_score - prev_score:.1f} points from last iteration")
        
        # AI 활용 인사이트
        ai_usage = submission.get('ai_usage', {})
        contribution = ai_usage.get('contribution', {}).get('total_contribution_percentage', 0)
        if contribution < 50:
            insights.append(f"AI contribution is low ({contribution}%), need to increase AI utilization")
        
        return insights
    
    def _suggest_next_steps(self, report: ReflectionReport) -> List[str]:
        """다음 단계 제안"""
        steps = []
        
        # 우선순위 높은 개선사항 먼저
        high_priority = [i for i in report.improvements if i.priority == 'high']
        for improvement in high_priority[:3]:
            steps.append(f"[HIGH] {improvement.target}: {improvement.action}")
        
        # 중간 우선순위
        medium_priority = [i for i in report.improvements if i.priority == 'medium']
        for improvement in medium_priority[:2]:
            steps.append(f"[MED] {improvement.target}: {improvement.action}")
        
        # 일반적인 조언
        if not report.weaknesses:
            steps.append("All criteria met! Focus on polishing and final submission.")
        else:
            steps.append(f"Focus on top {len(high_priority)} high-priority improvements")
        
        return steps
    
    def _report_to_dict(self, report: ReflectionReport) -> Dict[str, Any]:
        """보고서를 dict로 변환"""
        return {
            'timestamp': report.timestamp.isoformat(),
            'overall_score': report.overall_score,
            'weaknesses': [
                {
                    'category': w.category,
                    'score': w.score,
                    'max_score': w.max_score,
                    'gap': w.gap,
                    'possible_causes': w.possible_causes,
                    'suggested_fixes': w.suggested_fixes
                }
                for w in report.weaknesses
            ],
            'improvements': [
                {
                    'target': i.target,
                    'action': i.action,
                    'description': i.description,
                    'expected_impact': i.expected_impact,
                    'priority': i.priority
                }
                for i in report.improvements
            ],
            'insights': report.insights,
            'next_steps': report.next_steps
        }
    
    def get_reflection_summary(self) -> Dict[str, Any]:
        """리플렉션 요약"""
        if not self.reflection_history:
            return {'message': 'No reflections yet'}
        
        scores = [r.overall_score for r in self.reflection_history]
        
        return {
            'total_reflections': len(self.reflection_history),
            'average_score': sum(scores) / len(scores),
            'best_score': max(scores),
            'worst_score': min(scores),
            'score_trend': 'improving' if scores[-1] > scores[0] else 'declining' if scores[-1] < scores[0] else 'stable',
            'common_weaknesses': self._get_common_weaknesses()
        }
    
    def _get_common_weaknesses(self) -> Dict[str, int]:
        """가장 흔한 약점"""
        weakness_count = {}
        
        for report in self.reflection_history:
            for weakness in report.weaknesses:
                category = weakness.category
                weakness_count[category] = weakness_count.get(category, 0) + 1
        
        return dict(sorted(weakness_count.items(), key=lambda x: x[1], reverse=True)[:5])
