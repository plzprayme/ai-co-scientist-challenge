# CLAUDE.md - AI Co-Scientist Challenge Korea

## 프로젝트 개요

2026 AI Co-Scientist Challenge Korea Track 1 참가를 위한 
AI 활용 과학기술 연구 및 연구보고서 작성 프로젝트

---

## 빌드/테스트/배포 명령어

### 환경 설정

```bash
# 가상환경 생성
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 의존성 설치
pip install -r requirements.txt
```

### 실행 명령어

```bash
# 전체 워크플로우 실행
python main.py

# 특정 Phase만 실행
python main.py --phase literature
python main.py --phase hypothesis
python main.py --phase data_analysis
python main.py --phase writing
python main.py --phase ai_logging
python main.py --phase validation
python main.py --phase quality

# 특정 Phase부터 실행
python main.py --start-from hypothesis
python main.py --start-from data_analysis

# 품질 기준 설정
python main.py --target-score 85
python main.py --target-score 90

# 최대 반복 횟수 설정
python main.py --max-iterations 5
python main.py --max-iterations 15
```

### 테스트 명령어

```bash
# 코드 재현성 테스트
python -m pytest tests/

# 데이터 검증
python validate_data.py

# 특정 모듈 테스트
python -m pytest tests/test_agents.py
python -m pytest tests/test_workflow.py
```

---

## 코드 스타일 가이드

### Python 코드 스타일

- **PEP 8** 준수
- **Type hints** 사용
- **Docstring** 필수 (Google style)

```python
def example_function(param1: str, param2: int) -> dict:
    """
    Example function demonstrating code style.
    
    Args:
        param1: First parameter description
        param2: Second parameter description
        
    Returns:
        Dictionary containing results
        
    Raises:
        ValueError: When invalid input provided
    """
    return {"result": param1 * param2}
```

### 문서 작성 스타일

- **Markdown** 형식
- **영문** 작성 (연구보고서)
- **한글** 작성 (AI 활용보고서)

---

## 프로젝트 구조

```
ai_co_scientist_agents/
├── agents/              # 에이전트 정의
│   ├── director.py
│   ├── literature.py
│   ├── hypothesis.py
│   ├── data_analysis.py
│   ├── paper_writing.py
│   ├── ai_logging.py
│   ├── validation.py
│   └── quality.py
├── config/              # 설정 파일
│   └── settings.py
├── outputs/             # 산출물
│   ├── literature_review/
│   ├── hypothesis/
│   ├── analysis_results/
│   ├── paper/
│   ├── ai_usage/
│   ├── validation/
│   ├── quality/
│   └── data/
├── logs/                # 로그 파일
├── main.py              # 메인 실행 파일
├── requirements.txt     # 의존성
├── README.md
└── CLAUDE.md           # 이 파일
```

---

## AI 활용 기록 규칙

1. **모든 AI 상호작용**은 `/logs`에 기록
2. **프롬프트와 응답** 모두 저장
3. **사용 모델명과 버전** 기록
4. **타임스탬프** 필수

### 로그 형식

```markdown
## Interaction Log

### Timestamp: 2026-01-28 10:30:00
### Model: claude-3-5-sonnet-20241022
### Task: Literature Review - Search Query Generation

#### Prompt:
```
[Prompt content here]
```

#### Response:
```
[Response content here]
```

#### Usage:
- Tokens Used: 150/280
- Research Phase: Literature Review
- Contribution Level: High
```

---

## 제출물 체크리스트

### 연구보고서 (research_paper.md)

- [ ] 논문 형태로 작성
- [ ] 영문으로 작성
- [ ] 개인정보 제거 확인
- [ ] Abstract: 250-300 words
- [ ] Keywords: 3-5개
- [ ] 모든 섹션 포함 (Introduction ~ Conclusion)
- [ ] 참고문헌 형식 일관성

### AI 활용보고서 (ai_usage_report.md)

- [ ] URL 목록 포함
- [ ] AI 상호작용 로그 포함
- [ ] 체크리스트 포함
- [ ] AI 기여도 자체 평가 포함
- [ ] 3개 이상 AI 모델 활용 증거

### 활용 데이터 목록 (data_usage_list.md)

- [ ] 공개 데이터 정보
- [ ] 생성/수집 데이터 정보
- [ ] 데이터 처리 방법
- [ ] 라이선스 정보

### ZIP 파일

- [ ] 3개 파일 압축 완료
- [ ] 파일명 규칙 준수
- [ ] 개인정보 제거 확인

---

## 심사 기준별 체크리스트

### 주제의 실용성 (20점)

- [ ] 실제 문제 다루는가?
- [ ] 사회적/학문적 가치 명확한가?
- [ ] 혁신적인 접근인가?

### 방법론의 적절성 (20점)

- [ ] 방법론이 명확한가?
- [ ] 과학적 기준에 부합하는가?
- [ ] 재현 가능한가?

### 데이터의 적절성 (25점)

- [ ] 데이터가 논리적인가?
- [ ] 신뢰할 수 있는가?
- [ ] 결론과 일치하는가?

### 결론의 합리성 (10점)

- [ ] 과학적 사실에 부합하는가?
- [ ] 입증되었는가?
- [ ] 한계가 논의되었는가?

### 전달력 및 가독성 (5점)

- [ ] 영문 표현이 명확한가?
- [ ] 논리적 흐름이 자연스러운가?
- [ ] 전문 용어가 적절한가?

### 연구의 창의성 (20점)

- [ ] 차별화된 접근인가?
- [ ] AI 활용이 참신한가?
- [ ] 기존 연구와 차이점이 명확한가?

### AI 연구기여도 (Pass/Fail)

- [ ] AI가 충분히 기여했는가? (50%+)
- [ ] 3개 이상 AI 모델을 활용했는가?
- [ ] AI 활용이 상세히 기록되었는가?

---

## 개발 워크플로우

### 1. 새로운 기능 추가

```bash
# 브랜치 생성
git checkout -b feature/new-feature

# 개발
# ... 코드 작성 ...

# 테스트
python -m pytest tests/

# 커밋
git add .
git commit -m "Add new feature"

# 푸시
git push origin feature/new-feature
```

### 2. 버그 수정

```bash
# 브랜치 생성
git checkout -b fix/bug-description

# 수정
# ... 코드 수정 ...

# 테스트
python -m pytest tests/

# 커밋
git add .
git commit -m "Fix bug: description"

# 푸시
git push origin fix/bug-description
```

---

## 디버깅 팁

### 로그 레벨 조정

```python
# config/settings.py
LOGGING_CONFIG = {
    "level": "DEBUG",  # INFO -> DEBUG
    ...
}
```

### 특정 에이전트만 실행

```python
# main.py 수정
workflow = InfiniteLoopWorkflow()
result = workflow.run_single_phase("literature")
print(result)
```

### 중간 결과 확인

```python
# Python 인터프리터
from agents.literature import LiteratureReviewAgent

agent = LiteratureReviewAgent()
result = agent.conduct_review()
print(result['papers_found'])
```

---

## 자주 발생하는 문제

### 문제 1: ModuleNotFoundError

**해결**:
```bash
pip install -r requirements.txt
```

### 문제 2: 로그 파일 없음

**해결**:
```bash
mkdir -p logs
```

### 문제 3: 출력 디렉토리 없음

**해결**:
```bash
python -c "from pathlib import Path; [Path(d).mkdir(parents=True, exist_ok=True) for d in ['outputs/paper', 'outputs/ai_usage', 'outputs/data']]"
```

---

## 성능 최적화

### 병렬 처리

```python
# 여러 에이전트 병렬 실행
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [
        executor.submit(agent.run)
        for agent in agents
    ]
```

### 캐싱

```python
# 결과 캐싱
import functools

@functools.lru_cache(maxsize=128)
def expensive_operation(param):
    return result
```

---

## 보안 고려사항

### API 키 관리

```python
# .env 파일 사용
# .env
ANTHROPIC_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here

# Python에서 로드
from dotenv import load_dotenv
load_dotenv()
```

### 데이터 프라이버시

- 개인 식별 정보(PII) 제거
- 민감한 데이터 암호화
- 접근 로그 기록

---

## 참고 자료

### Python

- [PEP 8](https://pep8.org/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

### 연구 방법론

- [APA Style](https://apastyle.apa.org/)
- [Nature Guidelines](https://www.nature.com/nature/for-authors)

### AI 윤리

- [AI Ethics Guidelines](https://www.aiethics.org/)
- [Responsible AI](https://www.microsoft.com/en-us/ai/responsible-ai)

---

*이 문서는 2026 AI Co-Scientist Challenge Korea 참가를 위해 작성되었습니다.*

*최종 수정일: 2026-01-28*
