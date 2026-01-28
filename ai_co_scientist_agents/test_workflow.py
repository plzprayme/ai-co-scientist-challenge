#!/usr/bin/env python3
"""
테스트 스크립트 - 무한루프 에이전트 시스템

Usage:
    python test_workflow.py
"""

import sys
from pathlib import Path

# 프로젝트 루트 추가
sys.path.insert(0, str(Path(__file__).parent))

from agents.director import ResearchDirectorAgent
from agents.literature import LiteratureReviewAgent
from agents.hypothesis import HypothesisAgent
from agents.data_analysis import DataAnalysisAgent
from agents.paper_writing import PaperWritingAgent
from agents.ai_logging import AILoggingAgent
from agents.validation import ValidationAgent
from agents.quality import QualityAssuranceAgent


def test_director_agent():
    """ResearchDirectorAgent 테스트"""
    print("\n" + "="*60)
    print("Testing ResearchDirectorAgent")
    print("="*60)
    
    agent = ResearchDirectorAgent()
    result = agent.initialize_project()
    
    print(f"Status: {result['status']}")
    print(f"Project Info: {result['project_info']}")
    
    assert result['status'] == 'success'
    print("✓ DirectorAgent test passed")


def test_literature_agent():
    """LiteratureReviewAgent 테스트"""
    print("\n" + "="*60)
    print("Testing LiteratureReviewAgent")
    print("="*60)
    
    agent = LiteratureReviewAgent()
    result = agent.conduct_review()
    
    print(f"Status: {result['status']}")
    print(f"Papers Found: {result['papers_found']}")
    print(f"Research Gaps: {len(result['research_gaps'])}")
    
    assert result['status'] == 'completed'
    assert result['papers_found'] > 0
    print("✓ LiteratureAgent test passed")


def test_hypothesis_agent():
    """HypothesisAgent 테스트"""
    print("\n" + "="*60)
    print("Testing HypothesisAgent")
    print("="*60)
    
    # 먼저 문헌 조사 결과 생성
    literature_agent = LiteratureReviewAgent()
    literature_results = literature_agent.conduct_review()
    
    agent = HypothesisAgent()
    result = agent.generate_hypothesis(literature_results)
    
    print(f"Status: {result['status']}")
    print(f"Hypotheses: {len(result['hypotheses'])}")
    print(f"Statistical Methods: {len(result['statistical_methods'])}")
    
    assert result['status'] == 'completed'
    assert len(result['hypotheses']) > 0
    print("✓ HypothesisAgent test passed")


def test_data_analysis_agent():
    """DataAnalysisAgent 테스트"""
    print("\n" + "="*60)
    print("Testing DataAnalysisAgent")
    print("="*60)
    
    # 먼저 가설 결과 생성
    literature_agent = LiteratureReviewAgent()
    literature_results = literature_agent.conduct_review()
    
    hypothesis_agent = HypothesisAgent()
    hypothesis_results = hypothesis_agent.generate_hypothesis(literature_results)
    
    agent = DataAnalysisAgent()
    result = agent.analyze_data(hypothesis_results)
    
    print(f"Status: {result['status']}")
    print(f"Datasets: {len(result['datasets'])}")
    print(f"Statistical Tests: {len(result['statistical_analysis']['hypothesis_tests'])}")
    
    assert result['status'] == 'completed'
    assert len(result['datasets']) > 0
    print("✓ DataAnalysisAgent test passed")


def test_paper_writing_agent():
    """PaperWritingAgent 테스트"""
    print("\n" + "="*60)
    print("Testing PaperWritingAgent")
    print("="*60)
    
    # 먼저 데이터 분석 결과 생성
    literature_agent = LiteratureReviewAgent()
    literature_results = literature_agent.conduct_review()
    
    hypothesis_agent = HypothesisAgent()
    hypothesis_results = hypothesis_agent.generate_hypothesis(literature_results)
    
    data_agent = DataAnalysisAgent()
    data_results = data_agent.analyze_data(hypothesis_results)
    
    agent = PaperWritingAgent()
    result = agent.write_paper(data_results)
    
    print(f"Status: {result['status']}")
    print(f"Word Count: {result['word_count']}")
    print(f"Sections: {list(result['sections'].keys())}")
    
    assert result['status'] == 'completed'
    assert result['word_count'] > 0
    print("✓ PaperWritingAgent test passed")


def test_ai_logging_agent():
    """AILoggingAgent 테스트"""
    print("\n" + "="*60)
    print("Testing AILoggingAgent")
    print("="*60)
    
    agent = AILoggingAgent()
    result = agent.compile_usage_report()
    
    print(f"Status: {result['status']}")
    print(f"Interactions: {len(result['interactions'])}")
    print(f"AI Contribution: {result['contribution']['total_contribution_percentage']}%")
    
    assert result['status'] == 'completed'
    assert len(result['interactions']) > 0
    print("✓ AILoggingAgent test passed")


def test_validation_agent():
    """ValidationAgent 테스트"""
    print("\n" + "="*60)
    print("Testing ValidationAgent")
    print("="*60)
    
    # 먼저 필요한 결과들 생성
    literature_agent = LiteratureReviewAgent()
    literature_results = literature_agent.conduct_review()
    
    hypothesis_agent = HypothesisAgent()
    hypothesis_results = hypothesis_agent.generate_hypothesis(literature_results)
    
    data_agent = DataAnalysisAgent()
    data_results = data_agent.analyze_data(hypothesis_results)
    
    paper_agent = PaperWritingAgent()
    paper_results = paper_agent.write_paper(data_results)
    
    agent = ValidationAgent()
    result = agent.validate_results(paper_results, data_results)
    
    print(f"Status: {result['status']}")
    print(f"Overall Passed: {result['overall_passed']}")
    print(f"Reproducibility: {result['reproducibility']['passed']}")
    print(f"Statistical: {result['statistical']['passed']}")
    
    assert result['status'] == 'completed'
    print("✓ ValidationAgent test passed")


def test_quality_agent():
    """QualityAssuranceAgent 테스트"""
    print("\n" + "="*60)
    print("Testing QualityAssuranceAgent")
    print("="*60)
    
    # 먼저 필요한 결과들 생성
    literature_agent = LiteratureReviewAgent()
    literature_results = literature_agent.conduct_review()
    
    hypothesis_agent = HypothesisAgent()
    hypothesis_results = hypothesis_agent.generate_hypothesis(literature_results)
    
    data_agent = DataAnalysisAgent()
    data_results = data_agent.analyze_data(hypothesis_results)
    
    paper_agent = PaperWritingAgent()
    paper_results = paper_agent.write_paper(data_results)
    
    ai_logger = AILoggingAgent()
    ai_usage_results = ai_logger.compile_usage_report()
    
    agent = QualityAssuranceAgent()
    result = agent.assess_quality(paper_results, ai_usage_results)
    
    print(f"Status: {result['status']}")
    print(f"Total Score: {result['total_score']}/{result['max_possible']}")
    print(f"AI Contribution: {result['ai_contribution_status']}")
    print(f"Passed: {result['passed']}")
    
    assert result['status'] == 'completed'
    assert result['total_score'] > 0
    print("✓ QualityAssuranceAgent test passed")


def test_full_workflow():
    """전체 워크플로우 테스트"""
    print("\n" + "="*60)
    print("Testing Full Workflow")
    print("="*60)
    
    from main import InfiniteLoopWorkflow
    
    workflow = InfiniteLoopWorkflow(target_score=70, max_iterations=2)
    
    # Phase별 실행 테스트
    phases = ['init', 'literature', 'hypothesis']
    
    for phase in phases:
        print(f"\nRunning phase: {phase}")
        result = workflow.run_phase(phase)
        print(f"Result: {result.get('status', 'unknown')}")
        assert result.get('status') in ['success', 'completed']
    
    print("\n✓ Full workflow test passed")


def main():
    """메인 테스트 함수"""
    print("\n" + "="*60)
    print("AI Co-Scientist Agent System - Test Suite")
    print("="*60)
    
    tests = [
        ("Director Agent", test_director_agent),
        ("Literature Agent", test_literature_agent),
        ("Hypothesis Agent", test_hypothesis_agent),
        ("Data Analysis Agent", test_data_analysis_agent),
        ("Paper Writing Agent", test_paper_writing_agent),
        ("AI Logging Agent", test_ai_logging_agent),
        ("Validation Agent", test_validation_agent),
        ("Quality Agent", test_quality_agent),
        ("Full Workflow", test_full_workflow),
    ]
    
    passed = 0
    failed = 0
    
    for name, test_func in tests:
        try:
            test_func()
            passed += 1
        except Exception as e:
            print(f"\n✗ {name} test failed: {str(e)}")
            failed += 1
    
    print("\n" + "="*60)
    print("Test Summary")
    print("="*60)
    print(f"Passed: {passed}/{len(tests)}")
    print(f"Failed: {failed}/{len(tests)}")
    
    if failed == 0:
        print("\n🎉 All tests passed!")
        return 0
    else:
        print(f"\n⚠️ {failed} test(s) failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
