# 2026 AI Co-Scientist Challenge Korea - 무한루프 에이전트 시스템 설계

## 📋 대회 정보 요약

### Track 1: AI 활용 과학기술 연구 수행 및 연구보고서 작성

**대회 목적**: 과학기술 연구 동반자로서 AI의 가능성을 탐색하고, 연구자와 AI 간 새로운 연구 협업 촉진

**주요 정보**:
- **7대 지정주제 분야**: 바이오, 재료·화학, 지구과학, 반도체·디스플레이, 이차전지, 에너지, 수학
- **제출 마감**: 2026년 1월 31일(토) 18:00
- **제출물**:
  1. 연구보고서 (논문 형태, 영문)
  2. AI 활용보고서 (URL, 로그, 체크리스트 등)
  3. 활용 데이터 목록

**심사 기준 (100점)**:
| 평가 항목 | 배점 | 내용 |
|-----------|------|------|
| 주제의 실용성 | 20 | 연구의 유의미성, 사회적·학문적 가치 |
| 방법론의 적절성 | 20 | 연구 방법론 명확성, 과학적 기준 부합 |
| 데이터의 적절성 | 25 | 논리적 결과, 신뢰성, 명확한 결론 |
| 결론의 합리성 | 10 | 과학적 사실 부합, 입증 여부 |
| 전달력 및 가독성 | 5 | 명확한 전달, 이해 가능한 구성 |
| 연구의 창의성 및 참신성 | 20 | 차별화된 접근, AI 활용 참신성 |
| AI 연구기여도 | Pass/Fail | AI 충분한 기여 여부 |

**AI 활용 심사**: 다중 AI 패널 심사 (3개 모델 이상 활용) - 연구 유용성, AI 참여도 평가

---

## 🏗️ 무한루프 에이전트 시스템 아키텍처

### 시스템 개요

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AI Co-Scientist 무한루프 에이전트 시스템                    │
│                         (Infinite Loop Agent System)                         │
└─────────────────────────────────────────────────────────────────────────────┘

    ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
    │   Research   │────▶│   Planning   │────▶│  Execution   │
    │   Agent      │     │   Agent      │     │   Agent      │
    └──────────────┘     └──────────────┘     └──────────────┘
           ▲                                          │
           │                                          ▼
    ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
    │   Review     │◀────│   Analysis   │◀────│  Validation  │
    │   Agent      │     │   Agent      │     │   Agent      │
    └──────────────┘     └──────────────┘     └──────────────┘
```

---

## 🎯 SKILL 정의

### 1. ResearchSkill (연구 스킬)

```python
class ResearchSkill:
    """과학기술 연구 수행을 위한 핵심 스킬"""
    
    name = "research"
    description = "과학기술 연구의 전 과정을 수행하는 스킬"
    
    capabilities = [
        "literature_review",      # 문헌 조사
        "hypothesis_generation",  # 가설 생성
        "experimental_design",    # 실험 설계
        "data_collection",        # 데이터 수집
        "statistical_analysis",   # 통계 분석
        "result_interpretation",  # 결과 해석
    ]
    
    tools = [
        "web_search",             # 웹 검색
        "paper_search",           # 논문 검색 (arxiv, google_scholar)
        "data_analysis",          # 데이터 분석 (Python)
        "visualization",          # 시각화
        "code_execution",         # 코드 실행
    ]
```

### 2. WritingSkill (작성 스킬)

```python
class WritingSkill:
    """연구보고서 작성을 위한 스킬"""
    
    name = "writing"
    description = "논문 형태의 연구보고서 작성 스킬"
    
    capabilities = [
        "paper_structure",        # 논문 구조화
        "abstract_writing",       # 초록 작성
        "introduction_writing",   # 서론 작성
        "methodology_writing",    # 방법론 작성
        "results_writing",        # 결과 작성
        "discussion_writing",     # 토론 작성
        "conclusion_writing",     # 결론 작성
        "reference_management",   # 참고문헌 관리
    ]
    
    tools = [
        "markdown_editor",        # 마크다운 편집
        "latex_editor",           # LaTeX 편집
        "citation_manager",       # 인용 관리
        "grammar_checker",        # 문법 검사
    ]
```

### 3. AILoggingSkill (AI 활용 로깅 스킬)

```python
class AILoggingSkill:
    """AI 활용 과정 기록을 위한 스킬"""
    
    name = "ai_logging"
    description = "AI 활용보고서 작성을 위한 상세 로깅 스킬"
    
    capabilities = [
        "prompt_logging",         # 프롬프트 로깅
        "response_logging",       # 응답 로깅
        "model_tracking",         # 모델 추적
        "version_control",        # 버전 관리
        "interaction_archive",    # 상호작용 아카이브
        "contribution_analysis",  # 기여도 분석
    ]
    
    tools = [
        "log_formatter",          # 로그 포맷터
        "timestamp_manager",      # 타임스탬프 관리
        "url_collector",          # URL 수집
        "checklist_generator",    # 체크리스트 생성
    ]
```

### 4. ValidationSkill (검증 스킬)

```python
class ValidationSkill:
    """연구 결과 검증을 위한 스킬"""
    
    name = "validation"
    description = "연구의 과학적 타당성 검증 스킬"
    
    capabilities = [
        "reproducibility_check",  # 재현성 검사
        "statistical_validation", # 통계적 검증
        "literature_comparison",  # 문헌 비교
        "logical_consistency",    # 논리적 일관성
        "data_integrity",         # 데이터 무결성
        "scientific_accuracy",    # 과학적 정확성
    ]
    
    tools = [
        "code_reviewer",          # 코드 리뷰
        "data_validator",         # 데이터 검증
        "peer_review_simulator",  # 동료 심사 시뮬레이션
    ]
```

### 5. QualitySkill (품질 스킬)

```python
class QualitySkill:
    """제출물 품질 관리를 위한 스킬"""
    
    name = "quality"
    description = "심사 기준에 따른 품질 관리 스킬"
    
    capabilities = [
        "practicality_score",     # 실용성 점수
        "methodology_score",      # 방법론 점수
        "data_quality_score",     # 데이터 품질 점수
        "conclusion_score",       # 결론 점수
        "readability_score",      # 가독성 점수
        "creativity_score",       # 창의성 점수
        "ai_contribution_score",  # AI 기여도 점수
    ]
    
    tools = [
        "scoring_rubric",         # 채점 기준
        "blind_review_checker",   # 블라인드 검사
        "format_validator",       # 형식 검증
    ]
```

---

## 🤖 AGENT 정의

### 1. ResearchDirectorAgent (연구 총괄 에이전트)

```python
class ResearchDirectorAgent:
    """연구 전체를 총괄하는 디렉터 에이전트"""
    
    role = "Research Director"
    description = "연구 방향 설정, 자원 할당, 진행 관리"
    
    skills = ["research", "writing", "quality"]
    
    responsibilities = [
        "연구 주제 선정 및 범위 설정",
        "연구 일정 수립 및 진행 관리",
        "다른 에이전트들의 작업 조율",
        "최종 산출물 품질 확인",
        "무한루프 사이클 관리",
    ]
    
    workflow = """
    1. 초기 연구 주제 분석
    2. 하위 에이전트 작업 분배
    3. 중간 결과 검토 및 피드백
    4. 품질 기준 충족 확인
    5. 최종 제출물 승인
    """
```

### 2. LiteratureReviewAgent (문헌 조사 에이전트)

```python
class LiteratureReviewAgent:
    """문헌 조사 및 배경 연구 수행 에이전트"""
    
    role = "Literature Reviewer"
    description = "관련 문헌 조사 및 연구 동향 파악"
    
    skills = ["research"]
    
    responsibilities = [
        "관련 논문 검색 및 분석",
        "연구 동향 파악",
        "연구 간극(Research Gap) 식별",
        "참고문헌 목록 생성",
    ]
    
    tools = ["arxiv", "google_scholar", "web_search"]
    
    output = "literature_review_report.md"
```

### 3. HypothesisAgent (가설 생성 에이전트)

```python
class HypothesisAgent:
    """연구 가설 생성 및 실험 설계 에이전트"""
    
    role = "Hypothesis Generator"
    description = "연구 가설 생성 및 실험 설계"
    
    skills = ["research"]
    
    responsibilities = [
        "문헌 기반 가설 생성",
        "실험 설계 및 방법론 수립",
        "변수 정의 및 측정 방법 설정",
        "통계적 검정 방법 선정",
    ]
    
    output = "hypothesis_and_methodology.md"
```

### 4. DataAnalysisAgent (데이터 분석 에이전트)

```python
class DataAnalysisAgent:
    """데이터 수집 및 분석 수행 에이전트"""
    
    role = "Data Analyst"
    description = "데이터 수집, 처리, 통계 분석 수행"
    
    skills = ["research"]
    
    responsibilities = [
        "데이터 수집 (공개 데이터 또는 생성 데이터)",
        "데이터 전처리 및 정제",
        "탐색적 데이터 분석 (EDA)",
        "통계 분석 수행",
        "결과 시각화",
    ]
    
    tools = ["python", "pandas", "numpy", "matplotlib", "seaborn", "scipy"]
    
    output = "analysis_results/"
```

### 5. PaperWritingAgent (논문 작성 에이전트)

```python
class PaperWritingAgent:
    """연구보고서 작성 에이전트"""
    
    role = "Paper Writer"
    description = "논문 형태의 연구보고서 작성"
    
    skills = ["writing"]
    
    responsibilities = [
        "논문 구조 설계",
        "각 섹션 작성 (Abstract, Introduction, Methods, Results, Discussion, Conclusion)",
        "영문 작성 및 문법 검사",
        "참고문헌 형식화",
    ]
    
    paper_structure = """
    1. Title
    2. Abstract (250-300 words)
    3. Keywords
    4. Introduction
    5. Related Work
    6. Methodology
    7. Experiments/Results
    8. Discussion
    9. Conclusion
    10. References
    """
    
    output = "research_paper.md"
```

### 6. AILoggingAgent (AI 활용 로깅 에이전트)

```python
class AILoggingAgent:
    """AI 활용 과정 상세 기록 에이전트"""
    
    role = "AI Logger"
    description = "AI 활용보고서 작성을 위한 모든 상호작용 기록"
    
    skills = ["ai_logging"]
    
    responsibilities = [
        "모든 AI 상호작용 로깅",
        "프롬프트 및 응답 아카이브",
        "사용 모델 및 버전 기록",
        "URL 및 체크리스트 관리",
        "AI 기여도 자체 평가",
    ]
    
    log_format = """
    ## Interaction Log
    
    ### Timestamp: [YYYY-MM-DD HH:MM:SS]
    ### Model: [Model Name & Version]
    ### Task: [Research Task Description]
    
    #### Prompt:
    ```
    [Prompt Content]
    ```
    
    #### Response:
    ```
    [Response Content]
    ```
    
    #### Usage:
    - Tokens Used: [Input/Output tokens]
    - Research Phase: [Phase Name]
    - Contribution Level: [High/Medium/Low]
    """
    
    output = "ai_usage_report.md"
```

### 7. ValidationAgent (검증 에이전트)

```python
class ValidationAgent:
    """연구 결과 검증 에이전트"""
    
    role = "Validator"
    description = "연구의 과학적 타당성 및 재현성 검증"
    
    skills = ["validation"]
    
    responsibilities = [
        "코드 재실행 및 결과 재현",
        "통계적 유의성 검증",
        "논리적 일관성 검사",
        "문헌과의 비교 분석",
    ]
    
    validation_checklist = """
    ## Validation Checklist
    
    - [ ] 코드 재실행 시 동일 결과 확인
    - [ ] 통계 검정 방법 적절성
    - [ ] p-value 및 신뢰구간 계산
    - [ ] 데이터 출처 및 사용 권한 확인
    - [ ] 논리적 흐름 일관성
    - [ ] 과학적 사실과의 일치성
    """
    
    output = "validation_report.md"
```

### 8. QualityAssuranceAgent (품질 보증 에이전트)

```python
class QualityAssuranceAgent:
    """심사 기준 기반 품질 검사 에이전트"""
    
    role = "Quality Assurance"
    description = "심사 기준에 따른 품질 평가 및 개선"
    
    skills = ["quality"]
    
    responsibilities = [
        "심사 기준별 자가 평가",
        "점수 산정 및 개선점 식별",
        "블라인드 평가 준비",
        "제출 형식 검증",
    ]
    
    scoring_rubric = """
    ## Quality Scoring Rubric (100점)
    
    ### 1. 주제의 실용성 (20점)
    - [ ] 18-20: 매우 유의미하고 혁신적인 문제
    - [ ] 14-17: 실용적인 문제 다룸
    - [ ] 10-13: 보통 수준의 문제
    - [ ] 0-9: 실용성이 낮음
    
    ### 2. 방법론의 적절성 (20점)
    - [ ] 18-20: 명확하고 효과적이며 과학적
    - [ ] 14-17: 적절한 방법론 사용
    - [ ] 10-13: 방법론에 일부 문제
    - [ ] 0-9: 부적절한 방법론
    
    ### 3. 데이터의 적절성 (25점)
    - [ ] 22-25: 논리적이고 신뢰할 수 있으며 일치
    - [ ] 17-21: 적절한 데이터와 결론
    - [ ] 12-16: 데이터에 일부 문제
    - [ ] 0-11: 데이터 부적절
    
    ### 4. 결론의 합리성 (10점)
    - [ ] 9-10: 과학적 사실에 부합하며 입증됨
    - [ ] 7-8: 합리적인 결론
    - [ ] 5-6: 결론에 일부 문제
    - [ ] 0-4: 비합리적 결론
    
    ### 5. 전달력 및 가독성 (5점)
    - [ ] 5: 명확하고 이해하기 쉬움
    - [ ] 4: 전달력 양호
    - [ ] 3: 보통 수준
    - [ ] 0-2: 낮은 가독성
    
    ### 6. 연구의 창의성 및 참신성 (20점)
    - [ ] 18-20: 차별화된 창의적 접근
    - [ ] 14-17: 참신한 요소 포함
    - [ ] 10-13: 일부 참신성
    - [ ] 0-9: 낮은 참신성
    
    ### 7. AI 연구기여도 (Pass/Fail)
    - [ ] PASS: AI가 충분히 기여함
    - [ ] FAIL: AI 기여도 불충분
    """
    
    output = "quality_report.md"
```

---

## 🔄 무한루프 워크플로우

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                         INFINITE LOOP WORKFLOW                                   │
└─────────────────────────────────────────────────────────────────────────────────┘

[START]
    │
    ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 1: INIT (초기화)                                                           │
│ ┌─────────────────────────────────────────────────────────────────────────────┐ │
│ │ ResearchDirectorAgent: 연구 주제 선정, 팀 구성, 초기 계획 수립                    │ │
│ └─────────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 2: LITERATURE (문헌 조사)                                                   │
│ ┌─────────────────────────────────────────────────────────────────────────────┐ │
│ │ LiteratureReviewAgent: 관련 문헌 검색 및 분석                                   │ │
│ │ - arxiv, google_scholar, web_search 활용                                      │ │
│ │ - Research Gap 식별                                                           │ │
│ └─────────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 3: HYPOTHESIS (가설 생성)                                                   │
│ ┌─────────────────────────────────────────────────────────────────────────────┐ │
│ │ HypothesisAgent: 가설 생성 및 실험 설계                                        │ │
│ │ - 가설 명확화                                                                 │ │
│ │ - 방법론 수립                                                                 │ │
│ └─────────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 4: DATA (데이터 분석)                                                       │
│ ┌─────────────────────────────────────────────────────────────────────────────┐ │
│ │ DataAnalysisAgent: 데이터 수집 및 분석                                         │ │
│ │ - 데이터 수집/전처리                                                          │ │
│ │ - 통계 분석 및 시각화                                                          │ │
│ └─────────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 5: WRITING (논문 작성)                                                      │
│ ┌─────────────────────────────────────────────────────────────────────────────┐ │
│ │ PaperWritingAgent: 연구보고서 작성                                             │ │
│ │ - 논문 형태로 작성 (영문)                                                      │ │
│ │ - 각 섹션별 작성                                                              │ │
│ └─────────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 6: AI_LOGGING (AI 활용 기록)                                                │
│ ┌─────────────────────────────────────────────────────────────────────────────┐ │
│ │ AILoggingAgent: AI 활용보고서 작성                                             │ │
│ │ - 모든 AI 상호작용 로깅                                                        │ │
│ │ - URL, 로그, 체크리스트 정리                                                    │ │
│ └─────────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 7: VALIDATION (검증)                                                        │
│ ┌─────────────────────────────────────────────────────────────────────────────┐ │
│ │ ValidationAgent: 연구 결과 검증                                                │ │
│ │ - 재현성 검사                                                                 │ │
│ │ - 통계적 검증                                                                 │ │
│ └─────────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 8: QUALITY (품질 평가)                                                      │
│ ┌─────────────────────────────────────────────────────────────────────────────┐ │
│ │ QualityAssuranceAgent: 심사 기준 기반 품질 평가                                 │ │
│ │ - 6개 평가 항목 자가 평가                                                      │ │
│ │ - 개선점 식별                                                                 │ │
│ └─────────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ DECISION: 품질 기준 충족 여부 확인                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
    │
    ├── [품질 불충족] ──▶ [개선 필요 영역 식별] ──▶ [해당 PHASE로 LOOP BACK]
    │
    └── [품질 충족] ──▶ [FINALIZE]
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 9: FINALIZE (최종 제출물 생성)                                               │
│ ┌─────────────────────────────────────────────────────────────────────────────┐ │
│ │ ResearchDirectorAgent: 최종 제출물 검토 및 승인                                │ │
│ │ - 연구보고서 (영문)                                                           │ │
│ │ - AI 활용보고서                                                               │ │
│ │ - 활용 데이터 목록                                                            │ │
│ │ - ZIP 파일로 압축                                                             │ │
│ └─────────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────────┘
    │
    ▼
[END]
```

---

## 📁 파일 구조

```
ai_co_scientist_project/
├── agents/
│   ├── __init__.py
│   ├── director.py          # ResearchDirectorAgent
│   ├── literature.py        # LiteratureReviewAgent
│   ├── hypothesis.py        # HypothesisAgent
│   ├── data_analysis.py     # DataAnalysisAgent
│   ├── paper_writing.py     # PaperWritingAgent
│   ├── ai_logging.py        # AILoggingAgent
│   ├── validation.py        # ValidationAgent
│   └── quality.py           # QualityAssuranceAgent
├── skills/
│   ├── __init__.py
│   ├── research.py          # ResearchSkill
│   ├── writing.py           # WritingSkill
│   ├── ai_logging.py        # AILoggingSkill
│   ├── validation.py        # ValidationSkill
│   └── quality.py           # QualitySkill
├── tools/
│   ├── __init__.py
│   ├── search_tools.py      # 검색 도구
│   ├── analysis_tools.py    # 분석 도구
│   └── writing_tools.py     # 작성 도구
├── outputs/                 # 산출물 디렉토리
│   ├── literature_review/
│   ├── hypothesis/
│   ├── analysis_results/
│   ├── paper/
│   ├── ai_usage/
│   ├── validation/
│   └── quality/
├── data/                    # 데이터 디렉토리
├── logs/                    # 로그 디렉토리
├── config/
│   ├── __init__.py
│   └── settings.py          # 설정 파일
├── workflow.py              # 무한루프 워크플로우
├── main.py                  # 메인 실행 파일
└── requirements.txt         # 의존성 패키지
```

---

## 🛠️ CLAUDE CODE 설정

### CLAUDE.md 설정 파일

```markdown
# CLAUDE.md - AI Co-Scientist Challenge Korea

## 프로젝트 개요
2026 AI Co-Scientist Challenge Korea Track 1 참가를 위한 
AI 활용 과학기술 연구 및 연구보고서 작성 프로젝트

## 빌드/테스트/배포 명령어

### 환경 설정
```bash
# 가상환경 생성
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# 의존성 설치
pip install -r requirements.txt
```

### 실행 명령어
```bash
# 전체 워크플로우 실행
python main.py

# 특정 Phase만 실행
python main.py --phase literature
python main.py --phase data_analysis
python main.py --phase writing

# 품질 검사만 실행
python main.py --phase quality
```

### 테스트 명령어
```bash
# 코드 재현성 테스트
python -m pytest tests/

# 데이터 검증
python validate_data.py
```

## 코드 스타일 가이드

### Python 코드 스타일
- PEP 8 준수
- Type hints 사용
- Docstring 필수

### 문서 작성 스타일
- Markdown 형식
- 영문 작성 (연구보고서)
- 한글 작성 (AI 활용보고서)

## 프로젝트 구조
- `/agents` - 에이전트 정의
- `/skills` - 스킬 정의
- `/tools` - 도구 정의
- `/outputs` - 산출물
- `/data` - 데이터
- `/logs` - 로그

## AI 활용 기록 규칙
1. 모든 AI 상호작용은 `/logs`에 기록
2. 프롬프트와 응답 모두 저장
3. 사용 모델명과 버전 기록
4. 타임스탬프 필수

## 제출물 체크리스트
- [ ] 연구보고서 (영문, 논문 형태)
- [ ] AI 활용보고서 (URL, 로그, 체크리스트)
- [ ] 활용 데이터 목록
- [ ] ZIP 파일로 압축
- [ ] 개인정보 제거 확인
```

---

## 📝 주요 산출물 템플릿

### 1. 연구보고서 템플릿 (영문)

```markdown
# [Research Title]

## Abstract
[250-300 words summarizing the research]

**Keywords**: [3-5 keywords]

## 1. Introduction
[Research background, motivation, and objectives]

## 2. Related Work
[Literature review and research gap]

## 3. Methodology
[Detailed description of research methods]

### 3.1 Data Collection
[Data sources and collection methods]

### 3.2 Experimental Design
[Experimental setup and procedures]

### 3.3 Analysis Methods
[Statistical and analytical methods]

## 4. Results
[Research findings with figures and tables]

## 5. Discussion
[Interpretation of results and implications]

## 6. Conclusion
[Summary and future work]

## References
[Formatted references]

## Acknowledgments
[Optional acknowledgments]
```

### 2. AI 활용보고서 템플릿

```markdown
# AI 활용보고서

## 1. 개요
- 연구 주제: [주제]
- 사용 AI 모델: [모델명 및 버전]
- AI 활용 범위: [전 과정/특정 단계]

## 2. AI 활용 체크리스트

### 2.1 연구 계획 단계
- [ ] 주제 선정 AI 활용
- [ ] 문헌 조사 AI 활용
- [ ] 가설 생성 AI 활용

### 2.2 연구 수행 단계
- [ ] 실험 설계 AI 활용
- [ ] 데이터 수집 AI 활용
- [ ] 데이터 분석 AI 활용
- [ ] 통계 처리 AI 활용

### 2.3 결과 정리 단계
- [ ] 결과 해석 AI 활용
- [ ] 보고서 작성 AI 활용
- [ ] 참고문헌 정리 AI 활용

## 3. AI 상호작용 로그

### 3.1 [Phase Name]
**Timestamp**: YYYY-MM-DD HH:MM:SS
**Model**: [Model Name & Version]
**Task**: [Task Description]

**Prompt**:
```
[Prompt content]
```

**Response**:
```
[Response content]
```

**Usage**:
- Tokens: [Input/Output]
- Contribution: [High/Medium/Low]

## 4. AI 기여도 자체 평가

| 연구 단계 | AI 기여도 | 비고 |
|-----------|-----------|------|
| 주제 선정 | [ %] | |
| 문헌 조사 | [ %] | |
| 가설 생성 | [ %] | |
| 실험 설계 | [ %] | |
| 데이터 분석 | [ %] | |
| 결과 해석 | [ %] | |
| 보고서 작성 | [ %] | |
| **총계** | **[ %]** | |

## 5. 활용 URL 목록
- [URL 1]: [Description]
- [URL 2]: [Description]

## 6. 참고사항
[기타 참고사항]
```

### 3. 활용 데이터 목록 템플릿

```markdown
# 활용 데이터 목록

## 1. 공개 데이터

| No | 데이터명 | 출처 | 라이선스 | 사용 목적 | 비고 |
|----|----------|------|----------|-----------|------|
| 1 | [Name] | [Source] | [License] | [Purpose] | |

## 2. 생성/수집 데이터

| No | 데이터명 | 수집 방법 | 데이터 형식 | 크기 | 비고 |
|----|----------|-----------|-------------|------|------|
| 1 | [Name] | [Method] | [Format] | [Size] | |

## 3. 데이터 처리 방법
[데이터 전처리 및 처리 방법 설명]

## 4. 데이터 공개 여부
- [ ] 공개 가능
- [ ] 공개 불가 (사유: )
```

---

## 🚀 실행 가이드

### 1. 초기 설정

```bash
# 프로젝트 클론
git clone [repository-url]
cd ai_co_scientist_project

# 가상환경 설정
python -m venv venv
source venv/bin/activate

# 의존성 설치
pip install -r requirements.txt
```

### 2. 설정 파일 수정

```python
# config/settings.py
RESEARCH_TOPIC = "[Your Research Topic]"
RESEARCH_FIELD = "[Bio/Materials/Chemistry/Earth Science/Semiconductor/Battery/Energy/Math]"
TARGET_DATE = "2026-01-31"

# AI 모델 설정
AI_MODELS = {
    "primary": "claude-3-5-sonnet-20241022",
    "secondary": "gpt-4",
    "tertiary": "gemini-pro"
}
```

### 3. 워크플로우 실행

```bash
# 전체 워크플로우 실행
python main.py

# 특정 단계부터 실행
python main.py --start-from hypothesis

# 품질 기준 설정
python main.py --target-score 85
```

### 4. 무한루프 모니터링

```bash
# 로그 실시간 모니터링
tail -f logs/workflow.log

# 품질 점수 추적
cat outputs/quality/quality_report.md
```

---

## ⚠️ 주의사항

### 연구윤리
1. **표절 금지**: AI 생성 텍스트와 문헌의 실재 여부 반드시 확인
2. **데이터 사용**: 적법한 데이터 수집 및 사용 권한 확보
3. **재현성**: AI 모델명, 버전, 설정값, 프롬프트 상세 기록
4. **투명성**: AI와의 상호작용 성실히 기록

### 블라인드 평가
- 제출물 내 개인정보 기입 금지
- 팀명, 참가자명 등 식별 정보 제거

### AI 활용
- 최소 3개 이상의 AI 모델 활용 권장
- AI 활용보고서에 상세한 로그 포함

---

## 📊 성과 지표

### 심사 기준별 목표 점수

| 평가 항목 | 배점 | 목표 점수 | 전략 |
|-----------|------|-----------|------|
| 주제의 실용성 | 20 | 18 | 실제 문제 해결 중심 |
| 방법론의 적절성 | 20 | 18 | 명확한 방법론 기술 |
| 데이터의 적절성 | 25 | 22 | 신뢰할 수 있는 데이터 |
| 결론의 합리성 | 10 | 9 | 과학적 근거 기반 |
| 전달력 및 가독성 | 5 | 5 | 명확한 영문 작성 |
| 연구의 창의성 | 20 | 18 | 차별화된 AI 활용 |
| AI 연구기여도 | P/F | PASS | 충분한 AI 기여 |
| **총점** | **100** | **90** | |

---

## 🔗 참고 자료

### 공식 링크
- 대회 홈페이지: https://aifactory.space/task/9235/overview
- 공식 사이트: https://co-scientist.kr/
- 공고문 다운로드: [Google Drive Link]

### AI 도구
- Claude: https://claude.ai/
- ChatGPT: https://chat.openai.com/
- Gemini: https://gemini.google.com/

### 학술 데이터베이스
- arXiv: https://arxiv.org/
- Google Scholar: https://scholar.google.com/
- PubMed: https://pubmed.ncbi.nlm.nih.gov/

---

*이 문서는 2026 AI Co-Scientist Challenge Korea Track 1 참가를 위해 작성되었습니다.*
*최종 수정일: 2026-01-28*
