# 2026 AI Co-Scientist Challenge Korea - Track 1

## 무한루프 에이전트 시스템 (Infinite Loop Agent System)

AI 활용 과학기술 연구 수행 및 연구보고서 작성을 위한 자동화 시스템

---

## 📋 프로젝트 개요

이 프로젝트는 **2026 AI Co-Scientist Challenge Korea**의 **Track 1** 참가를 위해 설계된 무한루프 에이전트 시스템입니다.

### 주요 특징

- **8개의 전문 에이전트**가 연구 전 과정을 담당
- **무한루프 워크플로우**로 품질 기준 충족까지 자동 반복
- **심사 기준 기반 자가 평가** 시스템
- **CLAUDE CODE**와 완벽하게 통합

---

## 🏗️ 시스템 아키텍처

```
┌─────────────────────────────────────────────────────────────────┐
│                    무한루프 에이전트 시스템                       │
└─────────────────────────────────────────────────────────────────┘

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

### 에이전트 구성

| 에이전트 | 역할 | 주요 기능 |
|----------|------|-----------|
| **ResearchDirectorAgent** | 연구 총괄 | 프로젝트 관리, 진행 조율 |
| **LiteratureReviewAgent** | 문헌 조사 | 논문 검색, Research Gap 식별 |
| **HypothesisAgent** | 가설 생성 | 가설 생성, 실험 설계 |
| **DataAnalysisAgent** | 데이터 분석 | 데이터 수집, 통계 분석 |
| **PaperWritingAgent** | 논문 작성 | 영문 연구보고서 작성 |
| **AILoggingAgent** | AI 활용 로깅 | AI 상호작용 기록, 기여도 평가 |
| **ValidationAgent** | 검증 | 재현성, 통계적 검증 |
| **QualityAssuranceAgent** | 품질 보증 | 심사 기준 기반 자가 평가 |

---

## 🚀 빠른 시작

### 1. 환경 설정

```bash
# 프로젝트 클론
git clone [repository-url]
cd ai_co_scientist_agents

# 가상환경 생성
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# 의존성 설치
pip install -r requirements.txt
```

### 2. 설정 파일 수정

```python
# config/settings.py 수정
RESEARCH_TOPIC = "Your Research Topic"
RESEARCH_FIELD = "materials_chemistry"  # 7대 분야 중 선택
TARGET_SCORE = 85
```

### 3. 워크플로우 실행

```bash
# 전체 무한루프 워크플로우 실행
python main.py

# 특정 Phase만 실행
python main.py --phase literature
python main.py --phase data_analysis

# 특정 Phase부터 실행
python main.py --start-from hypothesis

# 목표 점수 설정
python main.py --target-score 90
```

---

## 📁 프로젝트 구조

```
ai_co_scientist_agents/
├── agents/                      # 에이전트 모듈
│   ├── __init__.py
│   ├── director.py             # ResearchDirectorAgent
│   ├── literature.py           # LiteratureReviewAgent
│   ├── hypothesis.py           # HypothesisAgent
│   ├── data_analysis.py        # DataAnalysisAgent
│   ├── paper_writing.py        # PaperWritingAgent
│   ├── ai_logging.py           # AILoggingAgent
│   ├── validation.py           # ValidationAgent
│   └── quality.py              # QualityAssuranceAgent
├── config/                      # 설정 파일
│   ├── __init__.py
│   └── settings.py             # 프로젝트 설정
├── outputs/                     # 산출물 디렉토리
│   ├── literature_review/      # 문헌 조사 결과
│   ├── hypothesis/             # 가설 및 방법론
│   ├── analysis_results/       # 데이터 분석 결과
│   ├── paper/                  # 연구보고서
│   ├── ai_usage/               # AI 활용보고서
│   ├── validation/             # 검증 보고서
│   ├── quality/                # 품질 평가 보고서
│   └── data/                   # 데이터 목록
├── logs/                        # 로그 파일
├── main.py                      # 메인 실행 파일
├── requirements.txt             # 의존성 패키지
├── README.md                    # 이 파일
└── CLAUDE.md                    # CLAUDE CODE 설정
```

---

## 🔄 무한루프 워크플로우

```
[START]
    │
    ▼
┌─────────────┐
│  PHASE 1    │  init - 프로젝트 초기화
│    INIT     │
└─────────────┘
    │
    ▼
┌─────────────┐
│  PHASE 2    │  literature - 문헌 조사
│ LITERATURE  │
└─────────────┘
    │
    ▼
┌─────────────┐
│  PHASE 3    │  hypothesis - 가설 생성
│ HYPOTHESIS  │
└─────────────┘
    │
    ▼
┌─────────────┐
│  PHASE 4    │  data_analysis - 데이터 분석
│    DATA     │
└─────────────┘
    │
    ▼
┌─────────────┐
│  PHASE 5    │  writing - 논문 작성
│   WRITING   │
└─────────────┘
    │
    ▼
┌─────────────┐
│  PHASE 6    │  ai_logging - AI 활용 기록
│  AI_LOGGING │
└─────────────┘
    │
    ▼
┌─────────────┐
│  PHASE 7    │  validation - 검증
│ VALIDATION  │
└─────────────┘
    │
    ▼
┌─────────────┐
│  PHASE 8    │  quality - 품질 평가
│   QUALITY   │
└─────────────┘
    │
    ├── [품질 불충족] ──▶ [개선] ──▶ [해당 PHASE로 이동]
    │
    └── [품질 충족] ──▶ [FINALIZE] ──▶ [END]
```

---

## 📊 심사 기준 (100점)

| 평가 항목 | 배점 | 목표 점수 |
|-----------|------|-----------|
| 주제의 실용성 | 20 | 18 |
| 방법론의 적절성 | 20 | 18 |
| 데이터의 적절성 | 25 | 22 |
| 결론의 합리성 | 10 | 9 |
| 전달력 및 가독성 | 5 | 5 |
| 연구의 창의성 및 참신성 | 20 | 18 |
| AI 연구기여도 | Pass/Fail | Pass |
| **총점** | **100** | **90** |

---

## 📝 제출물

### 1. 연구보고서 (영문)

```
outputs/paper/research_paper.md
```

**구성**:
- Title
- Abstract (250-300 words)
- Keywords (3-5개)
- Introduction
- Related Work
- Methodology
- Results
- Discussion
- Conclusion
- References

### 2. AI 활용보고서

```
outputs/ai_usage/ai_usage_report.md
```

**구성**:
- AI 활용 체크리스트
- AI 상호작용 로그
- AI 기여도 자체 평가
- 활용 URL 목록

### 3. 활용 데이터 목록

```
outputs/data/data_usage_list.md
```

**구성**:
- 공개 데이터 정보
- 생성/수집 데이터 정보
- 데이터 처리 방법

---

## ⚙️ 설정 옵션

### config/settings.py

```python
# 연구 설정
RESEARCH_TOPIC = "Your Research Topic"
RESEARCH_FIELD = "materials_chemistry"
TARGET_DATE = "2026-01-31"

# AI 모델 설정
AI_MODELS = {
    "primary": "claude-3-5-sonnet-20241022",
    "secondary": "gpt-4",
    "tertiary": "gemini-pro"
}

# 품질 목표
TARGET_SCORE = 85
MAX_ITERATIONS = 10
```

---

## 🛠️ 개발 가이드

### 새로운 에이전트 추가

```python
# agents/new_agent.py

class NewAgent:
    def __init__(self):
        self.role = "New Agent"
        self.results = {}
    
    def execute(self, input_data: dict) -> dict:
        # 에이전트 로직 구현
        self.results = {
            "status": "completed",
            "data": processed_data,
        }
        return self.results
```

### 새로운 스킬 추가

```python
# skills/new_skill.py

class NewSkill:
    name = "new_skill"
    description = "New skill description"
    
    capabilities = [
        "capability_1",
        "capability_2",
    ]
    
    tools = [
        "tool_1",
        "tool_2",
    ]
```

---

## 📈 모니터링

### 로그 확인

```bash
# 실시간 로그 모니터링
tail -f logs/workflow_*.log

# 품질 점수 확인
cat outputs/quality/quality_report.md
```

### 진행 상황 확인

```python
# Python 인터프리터에서
from main import InfiniteLoopWorkflow

workflow = InfiniteLoopWorkflow()
status = workflow.director.get_project_status()
print(status)
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

## 📚 참고 자료

### 공식 링크

- [대회 홈페이지](https://aifactory.space/task/9235/overview)
- [공식 사이트](https://co-scientist.kr/)

### AI 도구

- [Claude](https://claude.ai/)
- [ChatGPT](https://chat.openai.com/)
- [Gemini](https://gemini.google.com/)

### 학술 데이터베이스

- [arXiv](https://arxiv.org/)
- [Google Scholar](https://scholar.google.com/)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/)

---

## 🤝 기여

프로젝트 개선을 위한 기여를 환영합니다!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다.

---

## 📞 문의

- 대회 문의: cs@aifactory.page
- 프로젝트 문의: [Your Email]

---

**2026 AI Co-Scientist Challenge Korea - Track 1**

*과학기술 연구 동반자로서 AI의 가능성을 탐색합니다.*
