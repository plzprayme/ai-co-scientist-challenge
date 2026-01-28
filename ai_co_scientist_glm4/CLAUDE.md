# CLAUDE.md - RALP-MIRROR

## 프로젝트 개요

**RALP-MIRROR**: GLM-4.7 기반 자기개선 연구 시스템  
**2026 AI Co-Scientist Challenge Korea - Track 1**

### 핵심 특징

- **단일 모델**: GLM-4.7만 사용
- **RALP 통합**: ULTRAWORK RALP에 의해 무한 실행
- **파일 기반 상태**: 모든 상태는 파일에 저장
- **Self-Consistency**: 하나의 모델로 3번 평가

---

## 빌드/실행 명령어

### 환경 설정

```bash
# 의존성 설치
pip install -r requirements.txt

# API 키 설정
export GLM4_API_KEY="your_zhipuai_api_key"
```

### 실행

```bash
# RALP 통합 실행 (무한 루프)
python ralp_wrapper.py

# 한 번만 실행 (테스트)
python ralp_wrapper.py --once

# 상태 초기화 후 실행
python ralp_wrapper.py --once --reset

# 직접 실행
python main_ralp.py
```

---

## 프로젝트 구조

```
ai_co_scientist_glm4/
├── main_ralp.py           # 메인 루프 (RALP가 실행)
├── ralp_wrapper.py        # RALP 통합 래퍼
├── glm4_client.py         # GLM-4.7 API 클라이언트
├── config.yaml            # 설정 파일
│
├── workspace/             # 작업 공간 (자동 생성)
│   ├── state.json         # 현재 상태
│   ├── submission/        # 제출물
│   ├── history/           # iteration 히스토리
│   └── learnings/         # 학습 내용
│
├── README.md              # 사용자 가이드
└── CLAUDE.md              # 이 파일
```

---

## 코드 스타일

### 함수 기반 구조

```python
# 클래스 상속 대신 함수 사용
def phase_research(state):
    """연구 수행 Phase"""
    # 작업 수행
    state['phase'] = 'evaluate'
    save_state(state)
```

### 파일 기반 상태 관리

```python
# 메모리 대신 파일 사용
def save_state(state):
    with open('workspace/state.json', 'w') as f:
        json.dump(state, f)

def load_state():
    with open('workspace/state.json', 'r') as f:
        return json.load(f)
```

---

## GLM-4.7 API 사용

### 기본 사용

```python
from glm4_client import glm4_generate, glm4_generate_json

# 텍스트 생성
text = glm4_generate("프롬프트", temperature=0.7)

# JSON 생성
data = glm4_generate_json("JSON 요청 프롬프트")
```

### 평가

```python
from glm4_client import GLM4Client

client = GLM4Client()
result = client.evaluate_paper(paper, rubric)
```

### Self-Consistency

```python
result = client.self_consistency_evaluate(paper, rubric, n=3)
```

---

## Phase 개발

### 새로운 Phase 추가

```python
# main_ralp.py

def phase_mynew(state):
    """내 Phase"""
    print("\n" + "="*60)
    print("[PHASE: MYNEW]")
    print("="*60)
    
    # 작업 수행
    result = do_something()
    
    # 상태 업데이트
    state['my_result'] = result
    state['phase'] = 'next_phase'
    
    save_state(state)
    print("\n→ 다음 Phase: next_phase")
```

### Phase 등록

```python
# main() 함수에 추가
elif state['phase'] == 'mynew':
    phase_mynew(state)
```

---

## RALP 통합

### RALP 설정

```python
# ralp_wrapper.py

def run_ralp_loop():
    """RALP가 무한으로 호출"""
    result = subprocess.run(
        [sys.executable, "main_ralp.py"],
        timeout=300  # 5분 타임아웃
    )
    return result.returncode == 0  # True면 완료
```

### 무한 루프

```python
# RALP가 실행
while True:
    run_ralp_loop()
```

---

## 디버깅

### 로그 확인

```bash
tail -f workspace/ralp_mirror.log
```

### 상태 확인

```bash
cat workspace/state.json | python -m json.tool
```

### 히스토리 확인

```bash
ls workspace/history/
cat workspace/history/iter_001.json | python -m json.tool
```

---

## 테스트

### 단일 실행 테스트

```bash
python ralp_wrapper.py --once
```

### 상태 초기화

```bash
rm -rf workspace/
python ralp_wrapper.py --once --reset
```

### Mock 모드 (API 없이)

```python
# glm4_client.py에서
if not self.client:
    return f"[MOCK] {prompt[:50]}..."
```

---

## 심사 기준

```python
RUBRIC = {
    "practicality": {"max": 20, "name": "주제의 실용성"},
    "methodology": {"max": 20, "name": "방법론의 적절성"},
    "data_quality": {"max": 25, "name": "데이터의 적절성"},
    "conclusion": {"max": 10, "name": "결론의 합리성"},
    "readability": {"max": 5, "name": "전달력 및 가독성"},
    "creativity": {"max": 20, "name": "연구의 창의성"},
    "ai_contribution": {"type": "pass_fail", "name": "AI 연구기여도"}
}
```

---

## 제출물 체크리스트

### 연구보고서 (paper.md)

- [ ] 영문 작성
- [ ] Abstract 250-300 words
- [ ] Keywords 3-5개
- [ ] 모든 섹션 포함

### AI 활용보고서 (ai_usage.md)

- [ ] AI 활용 체크리스트
- [ ] AI 상호작용 로그
- [ ] AI 기여도 평가 (50%+)
- [ ] 활용 URL 목록

### 데이터 목록 (data_list.md)

- [ ] 공개 데이터 정보
- [ ] 데이터 처리 방법
- [ ] 라이선스 정보

---

## 확장 가이드

### 새로운 검색 소스 추가

```python
# main_ralp.py
def search_papers(query):
    # arxiv
    arxiv_papers = search_arxiv(query)
    
    # 추가 소스
    # google_scholar_papers = search_google_scholar(query)
    
    return arxiv_papers
```

### 새로운 평가 기준 추가

```python
# config.yaml
rubric:
  my_criterion:
    max: 10
    name: "내 기준"
    description: "설명"
```

---

## 참고

- `main_ralp.py` - 메인 루프
- `glm4_client.py` - GLM-4.7 클라이언트
- `config.yaml` - 설정
- `README.md` - 사용자 가이드

---

**RALP-MIRROR v1.0.0**
