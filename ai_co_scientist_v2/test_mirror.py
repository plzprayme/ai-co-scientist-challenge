#!/usr/bin/env python3
"""
MIRROR System Test Suite
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from mirror.engine import MIRROREngine
from mirror.meta_learning import MetaLearningEngine, SystemImprovement
from mirror.reflection import ReflectionEngine
from mirror.version_control import VersionController
from mirror.agents.base import SelfImprovingAgent


def test_meta_learning():
    """메타러닝 엔진 테스트"""
    print("\n=== Testing MetaLearningEngine ===")
    
    engine = MetaLearningEngine()
    
    # Mock iteration data
    from dataclasses import dataclass
    
    @dataclass
    class MockIteration:
        iteration: int
        evaluation: dict
        reflection: dict
    
    # 여러 iteration 학습
    for i in range(1, 6):
        data = MockIteration(
            iteration=i,
            evaluation={
                'total_score': 70 + i * 3,
                'aggregated': {
                    'practicality': 15 + i,
                    'methodology': 16 + i,
                    'data_quality': 20 + i,
                    'conclusion': 8,
                    'readability': 4,
                    'creativity': 15 + i,
                    'ai_contribution': 'PASS'
                }
            },
            reflection={
                'weaknesses': [
                    {'category': 'practicality', 'gap': 5},
                    {'category': 'creativity', 'gap': 5}
                ],
                'improvements': [
                    {'target': 'practicality', 'action': 'add_examples'}
                ]
            }
        )
        engine.learn_from_iteration(data)
    
    # 패턴 분석
    patterns = engine.analyze_patterns([])
    print(f"Patterns: {patterns}")
    
    # 개선사항 생성
    improvements = engine.generate_improvements(patterns)
    print(f"Generated {len(improvements)} improvements")
    for imp in improvements:
        print(f"  - [{imp.priority}] {imp.target}: {imp.action}")
    
    # 지식 요약
    summary = engine.get_knowledge_summary()
    print(f"Knowledge summary: {summary}")
    
    print("✓ MetaLearningEngine test passed")


def test_reflection():
    """리플렉션 엔진 테스트"""
    print("\n=== Testing ReflectionEngine ===")
    
    engine = ReflectionEngine()
    
    submission = {
        'paper': {'title': 'Test Paper'},
        'ai_usage': {'contribution': {'total_contribution_percentage': 60}}
    }
    
    evaluation = {
        'aggregated': {
            'practicality': 15,
            'methodology': 18,
            'data_quality': 22,
            'conclusion': 9,
            'readability': 4,
            'creativity': 16,
            'ai_contribution': 'PASS'
        },
        'total_score': 84
    }
    
    result = engine.reflect(submission, evaluation)
    
    print(f"Overall score: {result['overall_score']}")
    print(f"Weaknesses: {len(result['weaknesses'])}")
    for w in result['weaknesses']:
        print(f"  - {w['category']}: {w['score']}/{w['max_score']} (gap: {w['gap']})")
    
    print(f"Improvements: {len(result['improvements'])}")
    for imp in result['improvements']:
        print(f"  - [{imp['priority']}] {imp['target']}: {imp['action']}")
    
    print(f"Insights: {result['insights']}")
    print(f"Next steps: {result['next_steps']}")
    
    print("✓ ReflectionEngine test passed")


def test_version_control():
    """버전 컨트롤러 테스트"""
    print("\n=== Testing VersionController ===")
    
    vc = VersionController()
    
    # 여러 commit 생성
    for i in range(1, 4):
        commit_info = {
            'iteration': i,
            'score': 80 + i * 3,
            'improvements': [
                {'target': 'practicality', 'action': 'add_examples', 'priority': 'high'},
                {'target': 'methodology', 'action': 'enhance_design', 'priority': 'medium'}
            ],
            'agent_versions': {'literature': f'1.0.{i}'}
        }
        commit = vc.commit(commit_info)
        print(f"Created commit: {commit.tag}")
    
    # 통계
    stats = vc.get_stats()
    print(f"Stats: {stats}")
    
    # commit 목록
    commits = vc.list_commits()
    print(f"Commits: {len(commits)}")
    for c in commits:
        print(f"  - {c['tag']}: {c['score']:.1f}")
    
    # diff
    if len(commits) >= 2:
        diff = vc.get_diff(commits[0]['tag'], commits[-1]['tag'])
        print(f"Diff: {diff}")
    
    # changelog
    changelog = vc.generate_changelog()
    print(f"Changelog generated: {len(changelog)} chars")
    
    print("✓ VersionController test passed")


def test_self_improving_agent():
    """Self-Improving Agent 테스트"""
    print("\n=== Testing SelfImprovingAgent ===")
    
    class TestAgent(SelfImprovingAgent):
        def execute(self, task):
            return {'result': 'test'}
    
    agent = TestAgent('test_agent')
    
    # 초기 버전
    print(f"Initial version: {agent.version}")
    
    # 피드백 기반 개선
    feedback = {
        'score': 0.5,
        'weaknesses': ['reasoning_unclear'],
        'type': 'reasoning_unclear'
    }
    agent.improve(feedback)
    
    print(f"After improvement: {agent.version}")
    print(f"Performance history: {len(agent.performance_history)}")
    
    # 통계
    stats = agent.get_stats()
    print(f"Stats: {stats}")
    
    print("✓ SelfImprovingAgent test passed")


def test_full_engine():
    """전체 엔진 테스트"""
    print("\n=== Testing Full MIRROREngine ===")
    
    config = {
        'target_score': 85,
        'max_iterations': 5
    }
    
    engine = MIRROREngine(config)
    
    # Mock agents 등록
    from main import create_agents
    agents = create_agents()
    for name, agent in agents.items():
        engine.register_agent(name, agent)
    
    # 단일 iteration 테스트
    print("Testing single iteration...")
    submission = engine._execute_research()
    print(f"Submission keys: {list(submission.keys())}")
    
    evaluation = engine._multi_judge_evaluation(submission)
    print(f"Evaluation score: {evaluation.get('total_score')}")
    
    reflection = engine._reflect(submission, evaluation)
    print(f"Reflection weaknesses: {len(reflection.get('weaknesses', []))}")
    
    print("✓ Full engine test passed")


def main():
    """메인 테스트"""
    print("=" * 60)
    print("MIRROR System Test Suite")
    print("=" * 60)
    
    tests = [
        ("MetaLearningEngine", test_meta_learning),
        ("ReflectionEngine", test_reflection),
        ("VersionController", test_version_control),
        ("SelfImprovingAgent", test_self_improving_agent),
        ("Full Engine", test_full_engine),
    ]
    
    passed = 0
    failed = 0
    
    for name, test_func in tests:
        try:
            test_func()
            passed += 1
        except Exception as e:
            print(f"\n✗ {name} test failed: {str(e)}")
            import traceback
            traceback.print_exc()
            failed += 1
    
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    print(f"Passed: {passed}/{len(tests)}")
    print(f"Failed: {failed}/{len(tests)}")
    
    if failed == 0:
        print("\n🎉 All tests passed!")
        return 0
    else:
        print(f"\n⚠️ {failed} test(s) failed")
        return 1


if __name__ == '__main__':
    sys.exit(main())
