#!/usr/bin/env python3
"""
MIRROR System - Main Execution Script

2026 AI Co-Scientist Challenge Korea - Track 1
메타러닝 기반 자기개선 무한루프 에이전트 시스템

Usage:
    python main.py
    python main.py --target-score 90
    python main.py --max-iterations 15
"""

import argparse
import logging
import sys
from pathlib import Path

# 프로젝트 경로 추가
sys.path.insert(0, str(Path(__file__).parent))

from mirror.engine import MIRROREngine
from mirror.agents.base import SelfImprovingAgent

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# =============================================================================
# Mock Agents for Testing
# =============================================================================

class LiteratureAgent(SelfImprovingAgent):
    """문헌 조사 에이전트"""
    
    def review(self) -> dict:
        return {
            'papers': [
                {'title': 'AI in Scientific Research', 'year': 2024},
                {'title': 'Machine Learning for Discovery', 'year': 2025}
            ],
            'gaps': ['limited multi-modal integration', 'insufficient validation']
        }
    
    def execute(self, task):
        return self.review()


class HypothesisAgent(SelfImprovingAgent):
    """가설 생성 에이전트"""
    
    def generate(self, literature: dict) -> dict:
        return {
            'hypotheses': [
                {'id': 'H1', 'statement': 'AI improves research efficiency by 40%'},
                {'id': 'H2', 'statement': 'Multi-modal data enhances accuracy'}
            ],
            'methodology': 'Comparative study with control group'
        }
    
    def execute(self, task):
        return self.generate(task)


class DataAgent(SelfImprovingAgent):
    """데이터 분석 에이전트"""
    
    def analyze(self, hypothesis: dict) -> dict:
        return {
            'results': {
                'efficiency_improvement': 42,
                'accuracy_improvement': 15,
                'p_value': 0.001
            },
            'metadata': {
                'sample_size': 100,
                'datasets': ['benchmark', 'experimental']
            }
        }
    
    def execute(self, task):
        return self.analyze(task)


class WritingAgent(SelfImprovingAgent):
    """논문 작성 에이전트"""
    
    def write(self, data: dict) -> dict:
        return {
            'title': 'AI-Driven Methodology for Enhancing Scientific Research',
            'abstract': 'This study demonstrates...',
            'sections': ['Introduction', 'Methods', 'Results', 'Discussion', 'Conclusion'],
            'word_count': 3500
        }
    
    def execute(self, task):
        return self.write(task)


class LoggingAgent(SelfImprovingAgent):
    """AI 활용 로깅 에이전트"""
    
    def compile(self) -> dict:
        return {
            'interactions': [
                {'model': 'claude', 'task': 'literature review'},
                {'model': 'gpt4', 'task': 'data analysis'},
                {'model': 'gemini', 'task': 'review'}
            ],
            'contribution': {
                'total_contribution_percentage': 65,
                'assessment': 'PASS'
            }
        }
    
    def execute(self, task):
        return self.compile()


class ClaudeJudge(SelfImprovingAgent):
    """Claude 심사위원"""
    
    def evaluate(self, submission: dict) -> dict:
        return {
            'practicality': 17,
            'methodology': 18,
            'data_quality': 22,
            'conclusion': 9,
            'readability': 4,
            'creativity': 17,
            'ai_contribution': 'PASS',
            'total': 87
        }
    
    def execute(self, task):
        return self.evaluate(task)


class GPT4Judge(SelfImprovingAgent):
    """GPT-4 심사위원"""
    
    def evaluate(self, submission: dict) -> dict:
        return {
            'practicality': 16,
            'methodology': 17,
            'data_quality': 21,
            'conclusion': 8,
            'readability': 5,
            'creativity': 16,
            'ai_contribution': 'PASS',
            'total': 83
        }
    
    def execute(self, task):
        return self.evaluate(task)


class GeminiJudge(SelfImprovingAgent):
    """Gemini 심사위원"""
    
    def evaluate(self, submission: dict) -> dict:
        return {
            'practicality': 18,
            'methodology': 19,
            'data_quality': 23,
            'conclusion': 9,
            'readability': 4,
            'creativity': 18,
            'ai_contribution': 'PASS',
            'total': 91
        }
    
    def execute(self, task):
        return self.evaluate(task)


def create_agents() -> dict:
    """에이전트 생성 및 등록"""
    return {
        'literature': LiteratureAgent('literature'),
        'hypothesis': HypothesisAgent('hypothesis'),
        'data': DataAgent('data'),
        'writer': WritingAgent('writer'),
        'logger': LoggingAgent('logger'),
        'claude': ClaudeJudge('claude_judge'),
        'gpt4': GPT4Judge('gpt4_judge'),
        'gemini': GeminiJudge('gemini_judge')
    }


def main():
    """메인 함수"""
    parser = argparse.ArgumentParser(
        description='MIRROR: Meta-Learning Self-Improving Agent System'
    )
    parser.add_argument(
        '--target-score',
        type=int,
        default=85,
        help='Target quality score (default: 85)'
    )
    parser.add_argument(
        '--max-iterations',
        type=int,
        default=20,
        help='Maximum iterations (default: 20)'
    )
    parser.add_argument(
        '--test',
        action='store_true',
        help='Run in test mode with mock data'
    )
    
    args = parser.parse_args()
    
    logger.info("=" * 60)
    logger.info("MIRROR System - Meta-Learning Self-Improving Agent")
    logger.info("2026 AI Co-Scientist Challenge Korea - Track 1")
    logger.info("=" * 60)
    
    # 설정
    config = {
        'target_score': args.target_score,
        'max_iterations': args.max_iterations
    }
    
    logger.info(f"Configuration: {config}")
    
    # 엔진 생성
    engine = MIRROREngine(config)
    
    # 에이전트 등록
    agents = create_agents()
    for name, agent in agents.items():
        engine.register_agent(name, agent)
    
    # 실행
    try:
        result = engine.run()
        
        logger.info("")
        logger.info("=" * 60)
        logger.info("FINAL RESULT")
        logger.info("=" * 60)
        logger.info(f"Final Score: {result.get('final_score', 0)}")
        logger.info(f"Iterations: {result.get('iteration_count', 0)}")
        logger.info(f"Best Submission: {result.get('research_paper', {}).get('title', 'N/A')}")
        
        # 통계 출력
        stats = engine.get_stats()
        logger.info("")
        logger.info("Execution Statistics:")
        for key, value in stats.items():
            logger.info(f"  {key}: {value}")
        
        # Changelog 생성
        engine.version_ctrl.generate_changelog()
        
        return 0
        
    except KeyboardInterrupt:
        logger.info("\nInterrupted by user")
        return 1
    except Exception as e:
        logger.error(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
