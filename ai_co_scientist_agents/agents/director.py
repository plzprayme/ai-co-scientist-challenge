"""
Research Director Agent
연구 총괄 에이전트
"""

import logging
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime

logger = logging.getLogger(__name__)


class ResearchDirectorAgent:
    """
    연구 전체를 총괄하는 디렉터 에이전트
    
    Responsibilities:
    - 연구 주제 선정 및 범위 설정
    - 연구 일정 수립 및 진행 관리
    - 다른 에이전트들의 작업 조율
    - 최종 산출물 품질 확인
    - 무한루프 사이클 관리
    """
    
    def __init__(self):
        self.role = "Research Director"
        self.project_info = {}
        self.improvement_history = []
        logger.info(f"{self.role} initialized")
    
    def initialize_project(self) -> Dict[str, Any]:
        """
        프로젝트 초기화
        
        Returns:
            초기화 결과
        """
        logger.info("Initializing project...")
        
        # 출력 디렉토리 생성
        output_dirs = [
            "outputs/literature_review",
            "outputs/hypothesis",
            "outputs/analysis_results",
            "outputs/paper",
            "outputs/ai_usage",
            "outputs/validation",
            "outputs/quality",
            "outputs/data",
            "logs",
        ]
        
        for dir_path in output_dirs:
            Path(dir_path).mkdir(parents=True, exist_ok=True)
        
        # 프로젝트 정보 설정
        self.project_info = {
            "start_time": datetime.now().isoformat(),
            "status": "initialized",
            "phases_completed": [],
            "current_phase": "init",
        }
        
        # 초기 설정 파일 생성
        self._create_project_config()
        
        logger.info("Project initialized successfully")
        
        return {
            "status": "success",
            "message": "Project initialized",
            "project_info": self.project_info,
        }
    
    def _create_project_config(self):
        """프로젝트 설정 파일 생성"""
        config_content = """# 프로젝트 설정

## 연구 주제
RESEARCH_TOPIC = "[Your Research Topic Here]"

## 연구 분야 (7대 분야 중 선택)
# - bio: 바이오
# - materials_chemistry: 재료·화학
# - earth_science: 지구과학
# - semiconductor: 반도체·디스플레이
# - battery: 이차전지
# - energy: 에너지
# - math: 수학
RESEARCH_FIELD = "[Select Field]"

## 제출 마감일
TARGET_DATE = "2026-01-31"

## AI 모델 설정
AI_MODELS = {
    "primary": "claude-3-5-sonnet-20241022",
    "secondary": "gpt-4",
    "tertiary": "gemini-pro"
}

## 품질 목표
TARGET_SCORE = 85

## 최대 반복 횟수
MAX_ITERATIONS = 10
"""
        
        config_path = Path("config/settings.py")
        config_path.parent.mkdir(exist_ok=True)
        
        if not config_path.exists():
            with open(config_path, 'w', encoding='utf-8') as f:
                f.write(config_content)
            logger.info(f"Created config file: {config_path}")
    
    def provide_feedback(self, improvement_areas: List[str]) -> Dict[str, Any]:
        """
        개선 필요 영역에 대한 피드백 제공
        
        Args:
            improvement_areas: 개선 필요 영역 목록
            
        Returns:
            피드백 결과
        """
        logger.info(f"Providing feedback for: {improvement_areas}")
        
        feedback = {
            "timestamp": datetime.now().isoformat(),
            "improvement_areas": improvement_areas,
            "recommendations": self._generate_recommendations(improvement_areas),
        }
        
        self.improvement_history.append(feedback)
        
        # 피드백 저장
        feedback_path = Path("logs/feedback_history.md")
        with open(feedback_path, 'a', encoding='utf-8') as f:
            f.write(f"\n## Feedback {len(self.improvement_history)}\n")
            f.write(f"**Timestamp**: {feedback['timestamp']}\n\n")
            f.write("**Improvement Areas**:\n")
            for area in improvement_areas:
                f.write(f"- {area}\n")
            f.write("\n**Recommendations**:\n")
            for rec in feedback['recommendations']:
                f.write(f"- {rec}\n")
            f.write("\n---\n")
        
        return feedback
    
    def _generate_recommendations(self, improvement_areas: List[str]) -> List[str]:
        """개선 영역별 권장사항 생성"""
        recommendations = []
        
        for area in improvement_areas:
            if "practicality" in area.lower():
                recommendations.append(
                    "연구 주제의 실용성을 높이기 위해 실제 문제 해결 중심으로 접근하세요."
                )
            elif "methodology" in area.lower():
                recommendations.append(
                    "방법론을 더 명확하게 기술하고, 과학적 근거를 강화하세요."
                )
            elif "data" in area.lower():
                recommendations.append(
                    "데이터의 신뢰성을 높이고, 데이터 출처를 명확히 하세요."
                )
            elif "conclusion" in area.lower():
                recommendations.append(
                    "결론이 데이터와 일치하는지 확인하고, 과학적 근거를 보강하세요."
                )
            elif "readability" in area.lower():
                recommendations.append(
                    "영문 표현을 개선하고, 논리적 흐름을 명확히 하세요."
                )
            elif "creativity" in area.lower():
                recommendations.append(
                    "AI 활용 방식의 참신성을 강조하고, 차별화된 접근을 시도하세요."
                )
            elif "ai_contribution" in area.lower():
                recommendations.append(
                    "AI 활용을 더 적극적으로 확대하고, AI 기여도를 명확히 문서화하세요."
                )
            else:
                recommendations.append(f"{area} 영역을 개선하세요.")
        
        return recommendations
    
    def update_phase_status(self, phase: str, status: str):
        """Phase 상태 업데이트"""
        self.project_info["current_phase"] = phase
        
        if status == "completed":
            if phase not in self.project_info["phases_completed"]:
                self.project_info["phases_completed"].append(phase)
        
        logger.info(f"Phase '{phase}' status updated to: {status}")
    
    def get_project_status(self) -> Dict[str, Any]:
        """프로젝트 상태 조회"""
        return {
            "project_info": self.project_info,
            "improvement_count": len(self.improvement_history),
            "completion_rate": len(self.project_info["phases_completed"]) / 9 * 100,
        }
