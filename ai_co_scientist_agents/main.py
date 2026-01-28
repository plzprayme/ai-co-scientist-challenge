#!/usr/bin/env python3
"""
2026 AI Co-Scientist Challenge Korea - Track 1
무한루프 에이전트 시스템 메인 실행 파일

Usage:
    python main.py
    python main.py --phase literature
    python main.py --start-from hypothesis
    python main.py --target-score 85
"""

import argparse
import logging
import sys
from datetime import datetime
from pathlib import Path

from agents.director import ResearchDirectorAgent
from agents.literature import LiteratureReviewAgent
from agents.hypothesis import HypothesisAgent
from agents.data_analysis import DataAnalysisAgent
from agents.paper_writing import PaperWritingAgent
from agents.ai_logging import AILoggingAgent
from agents.validation import ValidationAgent
from agents.quality import QualityAssuranceAgent
from config.settings import RESEARCH_TOPIC, RESEARCH_FIELD, TARGET_DATE, AI_MODELS

# 로깅 설정
def setup_logging():
    """로깅 설정"""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = log_dir / f"workflow_{timestamp}.log"
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    return logging.getLogger(__name__)

logger = setup_logging()


class InfiniteLoopWorkflow:
    """
    무한루프 워크플로우 관리자
    
    연구의 각 단계를 순환하며 품질 기준 충족까지 반복 실행
    """
    
    PHASES = [
        "init",
        "literature",
        "hypothesis",
        "data_analysis",
        "writing",
        "ai_logging",
        "validation",
        "quality"
    ]
    
    def __init__(self, target_score: int = 80, max_iterations: int = 10):
        """
        Args:
            target_score: 목표 품질 점수 (default: 80)
            max_iterations: 최대 반복 횟수 (default: 10)
        """
        self.target_score = target_score
        self.max_iterations = max_iterations
        self.current_iteration = 0
        
        # 에이전트 초기화
        self.director = ResearchDirectorAgent()
        self.literature_agent = LiteratureReviewAgent()
        self.hypothesis_agent = HypothesisAgent()
        self.data_agent = DataAnalysisAgent()
        self.writing_agent = PaperWritingAgent()
        self.ai_logger = AILoggingAgent()
        self.validator = ValidationAgent()
        self.quality_agent = QualityAssuranceAgent()
        
        logger.info(f"InfiniteLoopWorkflow initialized")
        logger.info(f"Target score: {target_score}, Max iterations: {max_iterations}")
    
    def run_phase(self, phase: str) -> dict:
        """
        특정 Phase 실행
        
        Args:
            phase: 실행할 Phase 이름
            
        Returns:
            Phase 실행 결과
        """
        logger.info(f"Running phase: {phase}")
        
        if phase == "init":
            return self.director.initialize_project()
        
        elif phase == "literature":
            return self.literature_agent.conduct_review()
        
        elif phase == "hypothesis":
            literature_results = self.literature_agent.get_results()
            return self.hypothesis_agent.generate_hypothesis(literature_results)
        
        elif phase == "data_analysis":
            hypothesis_results = self.hypothesis_agent.get_results()
            return self.data_agent.analyze_data(hypothesis_results)
        
        elif phase == "writing":
            data_results = self.data_agent.get_results()
            return self.writing_agent.write_paper(data_results)
        
        elif phase == "ai_logging":
            return self.ai_logger.compile_usage_report()
        
        elif phase == "validation":
            paper_results = self.writing_agent.get_results()
            data_results = self.data_agent.get_results()
            return self.validator.validate_results(paper_results, data_results)
        
        elif phase == "quality":
            paper_results = self.writing_agent.get_results()
            ai_usage_results = self.ai_logger.get_results()
            return self.quality_agent.assess_quality(paper_results, ai_usage_results)
        
        else:
            raise ValueError(f"Unknown phase: {phase}")
    
    def run_single_phase(self, phase: str) -> dict:
        """단일 Phase만 실행"""
        if phase not in self.PHASES:
            raise ValueError(f"Invalid phase: {phase}. Available: {self.PHASES}")
        
        logger.info(f"Running single phase: {phase}")
        return self.run_phase(phase)
    
    def run_from_phase(self, start_phase: str) -> dict:
        """특정 Phase부터 순차 실행"""
        if start_phase not in self.PHASES:
            raise ValueError(f"Invalid phase: {start_phase}")
        
        start_idx = self.PHASES.index(start_phase)
        phases_to_run = self.PHASES[start_idx:]
        
        results = {}
        for phase in phases_to_run:
            results[phase] = self.run_phase(phase)
        
        return results
    
    def run_infinite_loop(self) -> dict:
        """
        무한루프 워크플로우 실행
        
        품질 기준 충족 또는 최대 반복 횟수 도달까지 반복
        """
        logger.info("Starting Infinite Loop Workflow")
        
        iteration = 0
        best_score = 0
        best_results = None
        
        while iteration < self.max_iterations:
            iteration += 1
            self.current_iteration = iteration
            
            logger.info(f"\n{'='*60}")
            logger.info(f"ITERATION {iteration}/{self.max_iterations}")
            logger.info(f"{'='*60}\n")
            
            # 모든 Phase 순차 실행
            results = {}
            for phase in self.PHASES:
                try:
                    phase_result = self.run_phase(phase)
                    results[phase] = phase_result
                    
                    # Phase 결과 로깅
                    if isinstance(phase_result, dict):
                        status = phase_result.get('status', 'unknown')
                        logger.info(f"Phase '{phase}' completed with status: {status}")
                    
                except Exception as e:
                    logger.error(f"Error in phase '{phase}': {str(e)}")
                    results[phase] = {'status': 'error', 'error': str(e)}
            
            # 품질 평가 결과 확인
            quality_result = results.get('quality', {})
            total_score = quality_result.get('total_score', 0)
            ai_contribution = quality_result.get('ai_contribution', 'FAIL')
            
            logger.info(f"\n{'='*60}")
            logger.info(f"ITERATION {iteration} RESULTS")
            logger.info(f"{'='*60}")
            logger.info(f"Total Score: {total_score}/{self.target_score}")
            logger.info(f"AI Contribution: {ai_contribution}")
            
            # 최고 점수 업데이트
            if total_score > best_score:
                best_score = total_score
                best_results = results.copy()
                logger.info(f"New best score: {best_score}")
            
            # 품질 기준 충족 확인
            if total_score >= self.target_score and ai_contribution == "PASS":
                logger.info(f"\n{'='*60}")
                logger.info(f"TARGET ACHIEVED! Final Score: {total_score}")
                logger.info(f"{'='*60}")
                return results
            
            # 개선 필요 영역 식별 및 피드백
            improvement_areas = quality_result.get('improvement_areas', [])
            if improvement_areas:
                logger.info(f"\nImprovement areas identified: {improvement_areas}")
                self.director.provide_feedback(improvement_areas)
            
            logger.info(f"\nContinuing to iteration {iteration + 1}...")
        
        # 최대 반복 횟수 도달
        logger.warning(f"\nMax iterations ({self.max_iterations}) reached!")
        logger.info(f"Best score achieved: {best_score}")
        
        return best_results or results
    
    def finalize_submission(self, results: dict) -> Path:
        """
        최종 제출물 생성
        
        Args:
            results: 워크플로우 결과
            
        Returns:
            생성된 ZIP 파일 경로
        """
        logger.info("Finalizing submission...")
        
        # 최종 제출물 준비
        submission_dir = Path("outputs/final_submission")
        submission_dir.mkdir(parents=True, exist_ok=True)
        
        # 1. 연구보고서 복사
        paper_path = Path("outputs/paper/research_paper.md")
        if paper_path.exists():
            import shutil
            shutil.copy(paper_path, submission_dir / "research_paper.md")
            logger.info("Research paper copied")
        
        # 2. AI 활용보고서 복사
        ai_usage_path = Path("outputs/ai_usage/ai_usage_report.md")
        if ai_usage_path.exists():
            shutil.copy(ai_usage_path, submission_dir / "ai_usage_report.md")
            logger.info("AI usage report copied")
        
        # 3. 활용 데이터 목록 복사
        data_list_path = Path("outputs/data/data_usage_list.md")
        if data_list_path.exists():
            shutil.copy(data_list_path, submission_dir / "data_usage_list.md")
            logger.info("Data usage list copied")
        
        # 4. ZIP 파일 생성
        import zipfile
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        zip_path = Path(f"outputs/submission_{timestamp}.zip")
        
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in submission_dir.iterdir():
                if file.is_file():
                    zipf.write(file, file.name)
        
        logger.info(f"Submission ZIP created: {zip_path}")
        
        # 5. 제출 체크리스트 출력
        self._print_submission_checklist()
        
        return zip_path
    
    def _print_submission_checklist(self):
        """제출 체크리스트 출력"""
        checklist = """
        =========================================
        SUBMISSION CHECKLIST
        =========================================
        
        [ ] 연구보고서 (research_paper.md)
            - 논문 형태로 작성
            - 영문으로 작성
            - 개인정보 제거 확인
        
        [ ] AI 활용보고서 (ai_usage_report.md)
            - URL 목록 포함
            - AI 상호작용 로그 포함
            - 체크리스트 포함
            - AI 기여도 자체 평가 포함
        
        [ ] 활용 데이터 목록 (data_usage_list.md)
            - 공개 데이터 정보
            - 생성/수집 데이터 정보
            - 데이터 처리 방법
        
        [ ] ZIP 파일로 압축 완료
        
        [ ] 블라인드 평가 준비 완료
            - 개인정보 제거
            - 팀명/참가자명 제거
        
        =========================================
        """
        print(checklist)


def main():
    """메인 함수"""
    parser = argparse.ArgumentParser(
        description="2026 AI Co-Scientist Challenge Korea - Infinite Loop Agent System"
    )
    parser.add_argument(
        "--phase",
        type=str,
        choices=InfiniteLoopWorkflow.PHASES,
        help="Run a single phase only"
    )
    parser.add_argument(
        "--start-from",
        type=str,
        choices=InfiniteLoopWorkflow.PHASES,
        help="Start workflow from specific phase"
    )
    parser.add_argument(
        "--target-score",
        type=int,
        default=80,
        help="Target quality score (default: 80)"
    )
    parser.add_argument(
        "--max-iterations",
        type=int,
        default=10,
        help="Maximum loop iterations (default: 10)"
    )
    
    args = parser.parse_args()
    
    # 워크플로우 초기화
    workflow = InfiniteLoopWorkflow(
        target_score=args.target_score,
        max_iterations=args.max_iterations
    )
    
    # 실행 모드 결정
    if args.phase:
        # 단일 Phase 실행
        result = workflow.run_single_phase(args.phase)
        print(f"\nPhase '{args.phase}' result:")
        print(result)
    
    elif args.start_from:
        # 특정 Phase부터 실행
        results = workflow.run_from_phase(args.start_from)
        print(f"\nWorkflow results from '{args.start_from}':")
        for phase, result in results.items():
            print(f"  {phase}: {result.get('status', 'unknown')}")
    
    else:
        # 무한루프 워크플로우 실행
        final_results = workflow.run_infinite_loop()
        
        # 최종 제출물 생성
        zip_path = workflow.finalize_submission(final_results)
        
        print(f"\n{'='*60}")
        print(f"WORKFLOW COMPLETED")
        print(f"{'='*60}")
        print(f"Submission ZIP: {zip_path}")


if __name__ == "__main__":
    main()
