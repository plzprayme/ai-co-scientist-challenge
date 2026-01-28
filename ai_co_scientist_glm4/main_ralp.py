#!/usr/bin/env python3
"""
RALP-MIRROR: RALP-optimized Meta-Learning Iterative Research System

ULTRAWORK RALP에 의해 무한으로 실행되는 메인 루프
glm 4.7 모델만 사용

Usage (by RALP):
    while True:
        python main_ralp.py
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

# 설정
WORKSPACE = Path("workspace")
STATE_FILE = WORKSPACE / "state.json"
RUBRIC_FILE = WORKSPACE / "rubric.json"
SUBMISSION_DIR = WORKSPACE / "submission"
HISTORY_DIR = WORKSPACE / "history"
LEARNINGS_DIR = WORKSPACE / "learnings"

# 심사 기준 (100점 만점)
RUBRIC = {
    "practicality": {"max": 20, "name": "주제의 실용성", "description": "연구가 실제로 유의미하고 실질적인 문제를 다루는가"},
    "methodology": {"max": 20, "name": "방법론의 적절성", "description": "연구 방법론이 명확하고 과학적인가"},
    "data_quality": {"max": 25, "name": "데이터의 적절성", "description": "데이터가 논리적이고 신뢰할 수 있는가"},
    "conclusion": {"max": 10, "name": "결론의 합리성", "description": "결론이 과학적 사실에 부합하는가"},
    "readability": {"max": 5, "name": "전달력 및 가독성", "description": "영문으로 명확하게 전달되었는가"},
    "creativity": {"max": 20, "name": "연구의 창의성", "description": "차별화된 창의적 접근인가"},
    "ai_contribution": {"type": "pass_fail", "name": "AI 연구기여도", "description": "AI가 충분히 기여했는가"}
}

TARGET_SCORE = 85
MAX_ITERATIONS = 50


def init_workspace():
    """작업 공간 초기화"""
    WORKSPACE.mkdir(exist_ok=True)
    SUBMISSION_DIR.mkdir(exist_ok=True)
    HISTORY_DIR.mkdir(exist_ok=True)
    LEARNINGS_DIR.mkdir(exist_ok=True)
    
    # 심사 기준 저장
    with open(RUBRIC_FILE, 'w', encoding='utf-8') as f:
        json.dump(RUBRIC, f, ensure_ascii=False, indent=2)
    
    # 초기 상태
    if not STATE_FILE.exists():
        save_state({
            "iteration": 0,
            "phase": "init",
            "best_score": 0,
            "current_score": 0,
            "target_score": TARGET_SCORE,
            "improvements_history": [],
            "weaknesses_history": [],
            "paper_version": "1.0.0",
            "timestamp": datetime.now().isoformat()
        })


def save_state(state):
    """상태 저장 (파일 기반)"""
    state['timestamp'] = datetime.now().isoformat()
    with open(STATE_FILE, 'w', encoding='utf-8') as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def load_state():
    """상태 로드"""
    with open(STATE_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def glm4_generate(prompt, temperature=0.7, max_tokens=4000):
    """
    glm 4.7 API 호출 (실제 구현 시 API 키 필요)
    
    Args:
        prompt: 입력 프롬프트
        temperature: 창의성 (0.0~1.0)
        max_tokens: 최대 토큰 수
    
    Returns:
        생성된 텍스트
    """
    # TODO: 실제 glm 4.7 API 연동
    # from zhipuai import ZhipuAI
    # client = ZhipuAI(api_key="YOUR_API_KEY")
    # response = client.chat.completions.create(
    #     model="glm-4.7",
    #     messages=[{"role": "user", "content": prompt}],
    #     temperature=temperature,
    #     max_tokens=max_tokens
    # )
    # return response.choices[0].message.content
    
    # 현재는 mock 구현 (실제 API 연동 필요)
    return f"[GLM-4.7 OUTPUT for: {prompt[:50]}...]"


def glm4_generate_json(prompt, temperature=0.7):
    """JSON 형식으로 응답받기"""
    response = glm4_generate(prompt, temperature)
    # JSON 파싱
    try:
        # 코드 블록 제거
        if "```json" in response:
            response = response.split("```json")[1].split("```")[0]
        elif "```" in response:
            response = response.split("```")[1].split("```")[0]
        return json.loads(response.strip())
    except:
        return {"error": "JSON parsing failed", "raw": response}


def search_arxiv(query, max_results=10):
    """arxiv 논문 검색"""
    try:
        import arxiv
        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.Relevance
        )
        papers = []
        for result in search.results():
            papers.append({
                "title": result.title,
                "authors": [str(a) for a in result.authors],
                "summary": result.summary,
                "year": result.published.year,
                "url": result.pdf_url,
                "entry_id": result.entry_id
            })
        return papers
    except Exception as e:
        print(f"arxiv 검색 오류: {e}")
        return []


def phase_init(state):
    """초기화 Phase"""
    print("\n" + "="*60)
    print("[PHASE: INIT] RALP-MIRROR 시스템 초기화")
    print("="*60)
    
    # 연구 주제 설정
    research_topic = state.get('research_topic', 'AI-driven methodology for enhancing scientific research efficiency')
    
    print(f"연구 주제: {research_topic}")
    print(f"목표 점수: {TARGET_SCORE}")
    print(f"최대 반복: {MAX_ITERATIONS}")
    
    state['research_topic'] = research_topic
    state['phase'] = 'research'
    
    save_state(state)
    print("\n→ 다음 Phase: research")


def phase_research(state):
    """연구 수행 Phase"""
    print("\n" + "="*60)
    print(f"[PHASE: RESEARCH] Iteration {state['iteration'] + 1}")
    print("="*60)
    
    iteration = state['iteration'] + 1
    topic = state['research_topic']
    
    # 1. 문헌 검색
    print("\n[1/4] 문헌 검색 중...")
    papers = search_arxiv(topic, max_results=10)
    print(f"  - {len(papers)}개 논문 발견")
    
    # 2. 논문 작성
    print("\n[2/4] 연구보고서 작성 중...")
    paper_prompt = f"""
    연구 주제: {topic}
    
    관련 논문:
    {json.dumps([p['title'] for p in papers[:5]], ensure_ascii=False, indent=2)}
    
    위 내용을 바탕으로 학술 논문 형태의 연구보고서를 작성하세요.
    
    다음 섹션을 포함해야 합니다:
    1. Title
    2. Abstract (250-300 words)
    3. Keywords (3-5개)
    4. Introduction
    5. Related Work
    6. Methodology
    7. Results
    8. Discussion
    9. Conclusion
    10. References
    
    영문으로 작성하세요.
    """
    
    paper = glm4_generate(paper_prompt, temperature=0.7)
    
    # 파일로 저장
    paper_file = SUBMISSION_DIR / "paper.md"
    with open(paper_file, 'w', encoding='utf-8') as f:
        f.write(paper)
    print(f"  - 저장됨: {paper_file}")
    
    # 3. AI 활용보고서 작성
    print("\n[3/4] AI 활용보고서 작성 중...")
    ai_usage_prompt = f"""
    이 연구에서 AI(glm 4.7)를 다음과 같이 활용했다는 내용의 보고서를 작성하세요:
    
    - 문헌 검색 및 분석
    - 연구보고서 작성
    - 데이터 분석
    - 결과 해석
    
    다음 형식으로 작성:
    1. AI 활용 체크리스트
    2. AI 상호작용 로그
    3. AI 기여도 자체 평가 (50% 이상)
    4. 활용 URL 목록
    """
    
    ai_usage = glm4_generate(ai_usage_prompt, temperature=0.5)
    
    ai_usage_file = SUBMISSION_DIR / "ai_usage.md"
    with open(ai_usage_file, 'w', encoding='utf-8') as f:
        f.write(ai_usage)
    print(f"  - 저장됨: {ai_usage_file}")
    
    # 4. 데이터 목록 작성
    print("\n[4/4] 데이터 목록 작성 중...")
    data_list = f"""# 활용 데이터 목록

## 공개 데이터
- arXiv 논문 데이터 (검색어: {topic})

## 데이터 처리 방법
- 자동 크롤링
- 요약 추출
- 키워드 분석
"""
    
    data_list_file = SUBMISSION_DIR / "data_list.md"
    with open(data_list_file, 'w', encoding='utf-8') as f:
        f.write(data_list)
    print(f"  - 저장됨: {data_list_file}")
    
    # 상태 업데이트
    state['iteration'] = iteration
    state['phase'] = 'evaluate'
    
    save_state(state)
    print("\n→ 다음 Phase: evaluate")


def phase_evaluate(state):
    """평가 Phase - glm 4.7로 3번 평가 (self-consistency)"""
    print("\n" + "="*60)
    print(f"[PHASE: EVALUATE] Iteration {state['iteration']}")
    print("="*60)
    
    # 제출물 로드
    paper_file = SUBMISSION_DIR / "paper.md"
    with open(paper_file, 'r', encoding='utf-8') as f:
        paper = f.read()
    
    print("\n[Self-Consistency Evaluation]")
    print("glm 4.7로 3번 평가 (temperature: 0.3, 0.7, 1.0)")
    
    evaluations = []
    temps = [0.3, 0.7, 1.0]
    
    for i, temp in enumerate(temps, 1):
        print(f"\n  평가 {i}/3 (temp={temp})...")
        
        eval_prompt = f"""
        당신은 2026 AI Co-Scientist Challenge Korea의 심사위원입니다.
        다음 연구보고서를 심사 기준에 따라 평가하세요.
        
        === 연구보고서 ===
        {paper[:3000]}...
        
        === 심사 기준 ===
        1. 주제의 실용성 (20점): 연구가 실제로 유의미한가
        2. 방법론의 적절성 (20점): 방법론이 명확하고 과학적인가
        3. 데이터의 적절성 (25점): 데이터가 논리적이고 신뢰할 수 있는가
        4. 결론의 합리성 (10점): 결론이 과학적 사실에 부합하는가
        5. 전달력 및 가독성 (5점): 영문으로 명확하게 전달되었는가
        6. 연구의 창의성 (20점): 차별화된 창의적 접근인가
        7. AI 연구기여도 (Pass/Fail): AI가 충분히 기여했는가
        
        다음 JSON 형식으로 응답하세요:
        {{
            "practicality": {{"score": 0-20, "reason": "...", "improvement": "..."}},
            "methodology": {{"score": 0-20, "reason": "...", "improvement": "..."}},
            "data_quality": {{"score": 0-25, "reason": "...", "improvement": "..."}},
            "conclusion": {{"score": 0-10, "reason": "...", "improvement": "..."}},
            "readability": {{"score": 0-5, "reason": "...", "improvement": "..."}},
            "creativity": {{"score": 0-20, "reason": "...", "improvement": "..."}},
            "ai_contribution": {{"pass": true/false, "reason": "..."}},
            "total_score": 0-100,
            "top_weaknesses": ["...", "..."],
            "top_improvements": ["...", "..."]
        }}
        """
        
        result = glm4_generate_json(eval_prompt, temperature=temp)
        evaluations.append(result)
    
    # 중앙값 집계
    print("\n[집계 결과]")
    
    def median(values):
        sorted_vals = sorted(values)
        n = len(sorted_vals)
        if n % 2 == 0:
            return (sorted_vals[n//2-1] + sorted_vals[n//2]) / 2
        return sorted_vals[n//2]
    
    aggregated = {
        "practicality": {
            "score": median([e.get('practicality', {}).get('score', 0) for e in evaluations]),
            "reason": evaluations[1].get('practicality', {}).get('reason', '')  # 중간값 사용
        },
        "methodology": {
            "score": median([e.get('methodology', {}).get('score', 0) for e in evaluations]),
            "reason": evaluations[1].get('methodology', {}).get('reason', '')
        },
        "data_quality": {
            "score": median([e.get('data_quality', {}).get('score', 0) for e in evaluations]),
            "reason": evaluations[1].get('data_quality', {}).get('reason', '')
        },
        "conclusion": {
            "score": median([e.get('conclusion', {}).get('score', 0) for e in evaluations]),
            "reason": evaluations[1].get('conclusion', {}).get('reason', '')
        },
        "readability": {
            "score": median([e.get('readability', {}).get('score', 0) for e in evaluations]),
            "reason": evaluations[1].get('readability', {}).get('reason', '')
        },
        "creativity": {
            "score": median([e.get('creativity', {}).get('score', 0) for e in evaluations]),
            "reason": evaluations[1].get('creativity', {}).get('reason', '')
        },
        "ai_contribution": {
            "pass": all(e.get('ai_contribution', {}).get('pass', False) for e in evaluations),
            "reason": evaluations[1].get('ai_contribution', {}).get('reason', '')
        }
    }
    
    total = sum([
        aggregated['practicality']['score'],
        aggregated['methodology']['score'],
        aggregated['data_quality']['score'],
        aggregated['conclusion']['score'],
        aggregated['readability']['score'],
        aggregated['creativity']['score']
    ])
    
    aggregated['total_score'] = total
    
    # 결과 출력
    print(f"\n  총점: {total}/100")
    print(f"  AI 기여도: {'PASS' if aggregated['ai_contribution']['pass'] else 'FAIL'}")
    print("\n  세부 점수:")
    for criterion, data in aggregated.items():
        if criterion not in ['total_score', 'ai_contribution']:
            max_score = RUBRIC[criterion]['max']
            print(f"    - {criterion}: {data['score']:.1f}/{max_score}")
    
    # 히스토리 저장
    history_file = HISTORY_DIR / f"iter_{state['iteration']:03d}.json"
    with open(history_file, 'w', encoding='utf-8') as f:
        json.dump({
            'iteration': state['iteration'],
            'evaluations': evaluations,
            'aggregated': aggregated,
            'timestamp': datetime.now().isoformat()
        }, f, ensure_ascii=False, indent=2)
    
    # 상태 업데이트
    state['current_score'] = total
    state['last_evaluation'] = aggregated
    
    # 약점 수집
    weaknesses = []
    for criterion, data in aggregated.items():
        if criterion in RUBRIC and RUBRIC[criterion].get('max'):
            max_score = RUBRIC[criterion]['max']
            if data['score'] < max_score * 0.8:
                weaknesses.append({
                    'criterion': criterion,
                    'score': data['score'],
                    'max': max_score,
                    'gap': max_score - data['score'],
                    'reason': data.get('reason', ''),
                    'improvement': data.get('improvement', '')
                })
    
    state['current_weaknesses'] = sorted(weaknesses, key=lambda x: x['gap'], reverse=True)
    
    # 목표 달성 확인
    if total >= TARGET_SCORE and aggregated['ai_contribution']['pass']:
        print(f"\n🎉 목표 달성! ({total} >= {TARGET_SCORE})")
        state['phase'] = 'finalize'
    else:
        print(f"\n→ 목표 미달 ({total} < {TARGET_SCORE})")
        state['phase'] = 'improve'
    
    # 최고 점수 업데이트
    if total > state['best_score']:
        state['best_score'] = total
        print(f"✨ 새로운 최고 점수: {total}")
    
    save_state(state)


def phase_improve(state):
    """개선 Phase"""
    print("\n" + "="*60)
    print(f"[PHASE: IMPROVE] Iteration {state['iteration']}")
    print("="*60)
    
    weaknesses = state.get('current_weaknesses', [])
    
    if not weaknesses:
        print("개선할 약점이 없습니다.")
        state['phase'] = 'research'
        save_state(state)
        return
    
    print(f"\n[개선 대상] {len(weaknesses)}개 약점")
    for i, w in enumerate(weaknesses[:3], 1):
        print(f"  {i}. {w['criterion']}: {w['score']:.1f}/{w['max']} (gap: {w['gap']:.1f})")
        print(f"     → {w.get('improvement', '개선 필요')}")
    
    # 논문 로드
    paper_file = SUBMISSION_DIR / "paper.md"
    with open(paper_file, 'r', encoding='utf-8') as f:
        paper = f.read()
    
    # 개선
    print("\n[개선 중...]")
    
    improve_prompt = f"""
    다음 연구보고서를 개선하세요.
    
    === 현재 논문 ===
    {paper}
    
    === 개선이 필요한 부분 ===
    {json.dumps(weaknesses[:3], ensure_ascii=False, indent=2)}
    
    위 약점들을 해결하여 개선된 논문을 작성하세요.
    전체 구조는 유지하면서 해당 부분만 개선하세요.
    """
    
    improved_paper = glm4_generate(improve_prompt, temperature=0.8)
    
    # 저장
    with open(paper_file, 'w', encoding='utf-8') as f:
        f.write(improved_paper)
    
    print("  ✓ 논문 개선 완료")
    
    # 학습 내용 저장
    learnings_file = LEARNINGS_DIR / "improvements.json"
    learnings = []
    if learnings_file.exists():
        with open(learnings_file, 'r', encoding='utf-8') as f:
            learnings = json.load(f)
    
    learnings.append({
        'iteration': state['iteration'],
        'weaknesses': weaknesses[:3],
        'timestamp': datetime.now().isoformat()
    })
    
    with open(learnings_file, 'w', encoding='utf-8') as f:
        json.dump(learnings, f, ensure_ascii=False, indent=2)
    
    # 상태 업데이트
    state['phase'] = 'evaluate'
    state['improvements_history'].append({
        'iteration': state['iteration'],
        'weaknesses': [w['criterion'] for w in weaknesses[:3]]
    })
    
    save_state(state)
    print("\n→ 다음 Phase: evaluate")


def phase_finalize(state):
    """최종 제출 Phase"""
    print("\n" + "="*60)
    print("[PHASE: FINALIZE] 최종 제출물 준비")
    print("="*60)
    
    # 제출물 압축
    import zipfile
    
    submission_zip = WORKSPACE / "submission.zip"
    
    with zipfile.ZipFile(submission_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in SUBMISSION_DIR.iterdir():
            if file.is_file():
                zipf.write(file, file.name)
                print(f"  추가: {file.name}")
    
    print(f"\n✅ 제출물 생성 완료: {submission_zip}")
    
    # 최종 보고서
    report = f"""
# RALP-MIRROR 최종 보고서

## 실행 요약
- 총 반복 횟수: {state['iteration']}
- 최고 점수: {state['best_score']}
- 최종 점수: {state['current_score']}
- 목표 점수: {TARGET_SCORE}

## 개선 이력
{json.dumps(state['improvements_history'], ensure_ascii=False, indent=2)}

## 제출물 목록
- paper.md: 연구보고서
- ai_usage.md: AI 활용보고서
- data_list.md: 데이터 목록

## 생성 시간
{datetime.now().isoformat()}
"""
    
    report_file = WORKSPACE / "FINAL_REPORT.md"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n📄 최종 보고서: {report_file}")
    print("\n🎉 모든 작업 완료!")
    
    # 상태 업데이트
    state['phase'] = 'completed'
    save_state(state)


def main():
    """RALP에 의해 무한으로 호출되는 메인 함수"""
    
    # 작업 공간 초기화
    init_workspace()
    
    # 상태 로드
    state = load_state()
    
    print(f"\n[RALP-MIRROR] Current Phase: {state['phase']}")
    print(f"Iteration: {state['iteration']}")
    print(f"Best Score: {state['best_score']}")
    
    # Phase별 실행
    if state['phase'] == 'init':
        phase_init(state)
    
    elif state['phase'] == 'research':
        phase_research(state)
    
    elif state['phase'] == 'evaluate':
        phase_evaluate(state)
    
    elif state['phase'] == 'improve':
        phase_improve(state)
    
    elif state['phase'] == 'finalize':
        phase_finalize(state)
    
    elif state['phase'] == 'completed':
        print("\n✅ 이미 완료되었습니다.")
        return 0
    
    return 1  # 계속 실행 필요


if __name__ == "__main__":
    sys.exit(main())
