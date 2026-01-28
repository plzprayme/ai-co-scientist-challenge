# RALP-MIRROR: GLM-4.7 기반 자기개선 연구 시스템

**2026 AI Co-Scientist Challenge Korea - Track 1**  
**ULTRAWORK RALP + GLM-4.7 최적화**

---

## 🎯 시스템 개요

RALP-MIRROR는 OH MY CLAUDECODE의 ULTRAWORK RALP에 의해 무한으로 실행되는 연구 자동화 시스템입니다.

### 핵심 특징

- **단일 모델**: GLM-4.7만 사용 (3개 모델 self-consistency 평가)
- **파일 기반 상태**: 모든 상태는 파일에 저장, RALP가 관리
- **무한 루프**: RALP에 의해 자동으로 반복 실행
- **자기개선**: iteration마다 학습하며 개선

---

## 🏗️ 아키텍처

```
┌─────────────────────────────────────────────────────────────────┐
│                     RALP-MIRROR System                           │
└─────────────────────────────────────────────────────────────────┘

┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   STATE      │────▶│   GLM-4.7    │────▶│   OUTPUT     │
│   FILE       │     │   MODEL      │     │   FILE       │
└──────────────┘     └──────────────┘     └──────────────┘
       ▲                                          │
       │                                          ▼
┌──────────────┐                         ┌──────────────┐
│   EVALUATE   │◀────────────────────────│   GENERATE   │
│   & LEARN    │                         │   SUBMISSION │
└──────────────┘                         └──────────────┘

Loop: ULTRAWORK RALP가 무한 반복
```

### Phase 구조

```
[init] → [research] → [evaluate] → [improve] → [research] → ...
                           ↓
                    [target met?]
                         ↓ YES
                    [finalize]
```

---

## 📁 파일 구조

```
ai_co_scientist_glm4/
├── main_ralp.py           # 메인 루프 (RALP가 실행)
├── ralp_wrapper.py        # RALP 통합 래퍼
├── glm4_client.py         # GLM-4.7 API 클라이언트
├── config.yaml            # 설정 파일
│
├── workspace/             # 작업 공간 (RALP가 관리)
│   ├── state.json         # 현재 상태
│   ├── rubric.json        # 심사 기준
│   ├── submission/        # 제출물
│   │   ├── paper.md       # 연구보고서
│   │   ├── ai_usage.md    # AI 활용보고서
│   │   └── data_list.md   # 데이터 목록
│   ├── history/           # iteration 히스토리
│   │   ├── iter_001.json
│   │   └── ...
│   └── learnings/         # 학습 내용
│
├── CRITICAL_ANALYSIS.md   # 기존 시스템 분석
└── README.md              # 이 파일
```

---

## 🚀 실행 방법

### 1. 환경 설정

```bash
# 의존성 설치
pip install zhipuai arxiv pyyaml

# API 키 설정
export GLM4_API_KEY="your_api_key_here"
```

### 2. RALP 통합 실행 (권장)

```bash
# RALP가 무한으로 실행
python ralp_wrapper.py
```

### 3. 단일 실행 (테스트)

```bash
# 한 번만 실행
python ralp_wrapper.py --once

# 상태 초기화 후 실행
python ralp_wrapper.py --once --reset
```

### 4. 직접 실행

```bash
# main_ralp.py 직접 실행
python main_ralp.py
```

---

## ⚙️ 설정

### config.yaml

```yaml
research:
  topic: "AI-driven methodology for enhancing scientific research efficiency"
  field: "materials_chemistry"

target:
  score: 85
  max_iterations: 50

model:
  name: "glm-4.7"
  api_key: null  # 환경변수 GLM4_API_KEY 사용
```

### 환경변수

```bash
export GLM4_API_KEY="your_zhipuai_api_key"
```

---

## 📊 심사 기준 (100점 만점)

| 항목 | 배점 | 설명 |
|------|------|------|
| 주제의 실용성 | 20 | 연구가 실제로 유의미한가 |
| 방법론의 적절성 | 20 | 방법론이 명확하고 과학적인가 |
| 데이터의 적절성 | 25 | 데이터가 논리적이고 신뢰할 수 있는가 |
| 결론의 합리성 | 10 | 결론이 과학적 사실에 부합하는가 |
| 전달력 및 가독성 | 5 | 영문으로 명확하게 전달되었는가 |
| 연구의 창의성 | 20 | 차별화된 창의적 접근인가 |
| AI 연구기여도 | P/F | AI가 충분히 기여했는가 |

---

## 🔄 실행 흐름

### 1. Init Phase
```
작업 공간 초기화
연구 주제 설정
→ 다음: research
```

### 2. Research Phase
```
arxiv 문헌 검색
연구보고서 작성 (GLM-4.7)
AI 활용보고서 작성
데이터 목록 작성
→ 다음: evaluate
```

### 3. Evaluate Phase
```
GLM-4.7로 3번 평가 (temp: 0.3, 0.7, 1.0)
중앙값 집계
약점 식별
→ 목표 달성? finalize : improve
```

### 4. Improve Phase
```
약점 기반 개선
GLM-4.7로 논문 수정
학습 내용 저장
→ 다음: evaluate
```

### 5. Finalize Phase
```
제출물 압축 (submission.zip)
최종 보고서 생성
완료
```

---

## 🧠 Self-Consistency 평가

GLM-4.7 하나로 3번 평가하여 일관성 확보:

```python
# 3번 평가 (다양한 temperature)
evaluations = [
    glm4_evaluate(paper, temperature=0.3),  # 보수적
    glm4_evaluate(paper, temperature=0.7),  # 중립적
    glm4_evaluate(paper, temperature=1.0)   # 창의적
]

# 중앙값 선택
final_score = median(evaluations)
```

---

## 📈 상태 파일 (state.json)

```json
{
  "iteration": 5,
  "phase": "evaluate",
  "best_score": 87.5,
  "current_score": 85.0,
  "target_score": 85,
  "research_topic": "AI-driven methodology...",
  "improvements_history": [...],
  "current_weaknesses": [...],
  "timestamp": "2026-01-28T10:30:00"
}
```

---

## 🛠️ 개발 가이드

### 새로운 Phase 추가

```python
# main_ralp.py
def phase_new(state):
    """새로운 Phase"""
    print("[PHASE: NEW]")
    # 작업 수행
    state['phase'] = 'next_phase'
    save_state(state)
```

### GLM-4.7 API 사용

```python
from glm4_client import glm4_generate, glm4_generate_json

# 텍스트 생성
text = glm4_generate("프롬프트", temperature=0.7)

# JSON 생성
data = glm4_generate_json("JSON을 요청하는 프롬프트")
```

---

## 📋 제출물

완료 시 `workspace/submission.zip` 생성:

- `paper.md`: 연구보고서 (영문)
- `ai_usage.md`: AI 활용보고서
- `data_list.md`: 활용 데이터 목록

---

## ⚠️ 주의사항

1. **API 키**: `GLM4_API_KEY` 환경변수 설정 필수
2. **토큰 제한**: 긴 논문은 분할 처리
3. **타임아웃**: RALP 설정에서 타임아웃 조정
4. **비용**: iteration마다 API 호출 발생

---

## 🔧 문제 해결

### API 오류
```bash
# API 키 확인
echo $GLM4_API_KEY

# zhipuai 설치 확인
pip install zhipuai
```

### 상태 초기화
```bash
rm -rf workspace/
python ralp_wrapper.py --reset
```

### 로그 확인
```bash
tail -f workspace/ralp_mirror.log
```

---

## 📚 참고

- [2026 AI Co-Scientist Challenge](https://aifactory.space/task/9235/overview)
- [ZhipuAI GLM-4](https://open.bigmodel.cn/)
- [ULTRAWORK RALP](https://github.com/ultraware/ralp)

---

**RALP-MIRROR v1.0.0**  
*GLM-4.7 + ULTRAWORK RALP 최적화*
