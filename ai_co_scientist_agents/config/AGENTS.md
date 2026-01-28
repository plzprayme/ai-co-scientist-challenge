<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-01-29 | Updated: 2026-01-29 -->

# config

## Purpose

시스템 설정 및 연구 파라미터 관리 - 연구 주제, API 키, 품질 기준 등 중요 설정을 중앙에서 관리합니다.

## Key Files

| File | Description |
|------|-------------|
| `__init__.py` | 설정 패키지 초기화 |
| `settings.py` | 메인 설정 파일 - 연구 설정, API 키, 품질 기준 등 |

## Subdirectories

이 디렉토리에는 하위 디렉토리가 없습니다.

## For AI Agents

### Working In This Directory

이 디렉토리는 **읽기 전용**으로 취급합니다. 설정은 직접 수정하지 말고, 환경 변수나 설정 파일을 통해 관리합니다.

### Configuration Structure

```python
# config/settings.py

# =============================================================================
# 연구 설정
# =============================================================================

RESEARCH_TOPIC = "Your Research Topic"
RESEARCH_FIELD = "materials_chemistry"  # 7대 분야 중 선택
TARGET_SCORE = 85  # 목표 점수 (0-100)
MAX_ITERATIONS = 15  # 최대 반복 횟수

# =============================================================================
# 7대 지정주제 분야
# =============================================================================

RESEARCH_FIELDS = {
    "bio": "바이오",
    "materials_chemistry": "재료·화학",
    "earth_science": "지구과학",
    "semiconductor_display": "반도체·디스플레이",
    "secondary_battery": "이차전지",
    "energy": "에너지",
    "mathematics": "수학"
}

# =============================================================================
# API 설정 (환경 변수에서 로드)
# =============================================================================

import os

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# =============================================================================
# 모델 설정
# =============================================================================

DEFAULT_MODEL = "claude-3-5-sonnet-20241022"
MODEL_CONFIGS = {
    "claude": {
        "model": "claude-3-5-sonnet-20241022",
        "temperature": 0.7,
        "max_tokens": 4096
    },
    "gpt4": {
        "model": "gpt-4-turbo-preview",
        "temperature": 0.7,
        "max_tokens": 4096
    },
    "gemini": {
        "model": "gemini-pro",
        "temperature": 0.7,
        "max_tokens": 4096
    }
}

# =============================================================================
# 심사 기준
# =============================================================================

QUALITY_CRITERIA = {
    "practicality": {"max_score": 20, "weight": 0.20},
    "methodology": {"max_score": 20, "weight": 0.20},
    "data": {"max_score": 25, "weight": 0.25},
    "conclusion": {"max_score": 10, "weight": 0.10},
    "clarity": {"max_score": 5, "weight": 0.05},
    "creativity": {"max_score": 20, "weight": 0.20}
}

# =============================================================================
# 출력 경로
# =============================================================================

OUTPUT_DIR = "outputs"
LITERATURE_OUTPUT_DIR = f"{OUTPUT_DIR}/literature_review"
HYPOTHESIS_OUTPUT_DIR = f"{OUTPUT_DIR}/hypothesis"
ANALYSIS_OUTPUT_DIR = f"{OUTPUT_DIR}/analysis_results"
PAPER_OUTPUT_DIR = f"{OUTPUT_DIR}/paper"
AI_USAGE_OUTPUT_DIR = f"{OUTPUT_DIR}/ai_usage"
VALIDATION_OUTPUT_DIR = f"{OUTPUT_DIR}/validation"
QUALITY_OUTPUT_DIR = f"{OUTPUT_DIR}/quality"

# =============================================================================
# 로깅 설정
# =============================================================================

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        }
    },
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "filename": "logs/workflow.log",
            "formatter": "standard"
        }
    },
    "loggers": {
        "": {
            "handlers": ["file"],
            "level": "INFO"
        }
    }
}
```

### Common Patterns

#### 설정 사용

```python
from config.settings import RESEARCH_TOPIC, TARGET_SCORE, DEFAULT_MODEL

# 설정 값 사용
print(f"Research Topic: {RESEARCH_TOPIC}")
print(f"Target Score: {TARGET_SCORE}")
print(f"Default Model: {DEFAULT_MODEL}")
```

#### 모델 설정 사용

```python
from config.settings import MODEL_CONFIGS

# Claude 설정
claude_config = MODEL_CONFIGS["claude"]
client = Anthropic(api_key=ANTHROPIC_API_KEY)
response = client.messages.generate(
    model=claude_config["model"],
    temperature=claude_config["temperature"],
    max_tokens=claude_config["max_tokens"],
    ...
)
```

#### API 키 사용

```python
from config.settings import ANTHROPIC_API_KEY, OPENAI_API_KEY

# API 키로 클라이언트 초기화
claude_client = Anthropic(api_key=ANTHROPIC_API_KEY)
openai_client = OpenAI(api_key=OPENAI_API_KEY)
```

### Environment Variables

`.env` 파일에서 API 키를 관리합니다:

```bash
# .env
ANTHROPIC_API_KEY=your_anthropic_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

```python
# .gitignore에 .env 추가
echo ".env" >> .gitignore
```

### Dynamic Configuration

```python
# 설정 동적 변경
from config import settings

# 연구 주제 변경
settings.RESEARCH_TOPIC = "New Research Topic"

# 목표 점수 변경
settings.TARGET_SCORE = 90

# 최대 반복 횟수 변경
settings.MAX_ITERATIONS = 20
```

### Validation

```python
# 설정 검증
def validate_settings():
    assert settings.RESEARCH_TOPIC, "RESEARCH_TOPIC is required"
    assert settings.RESEARCH_FIELD in settings.RESEARCH_FIELDS, \
        f"Invalid field: {settings.RESEARCH_FIELD}"
    assert 0 <= settings.TARGET_SCORE <= 100, \
        f"Invalid score: {settings.TARGET_SCORE}"
    assert settings.ANTHROPIC_API_KEY, "ANTHROPIC_API_KEY is required"
```

### Code Style

- **상수**: UPPER_SNAKE_CASE
- **클래스**: PascalCase
- **함수**: lower_snake_case
- **Type hints** 필수

## Configuration Categories

### 1. Research Configuration

```python
RESEARCH_TOPIC = "Machine Learning for Materials Discovery"
RESEARCH_FIELD = "materials_chemistry"
TARGET_SCORE = 85
MAX_ITERATIONS = 15
```

### 2. API Configuration

```python
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
```

### 3. Model Configuration

```python
DEFAULT_MODEL = "claude-3-5-sonnet-20241022"
MODEL_CONFIGS = {
    "claude": {...},
    "gpt4": {...},
    "gemini": {...}
}
```

### 4. Quality Criteria

```python
QUALITY_CRITERIA = {
    "practicality": {"max_score": 20, "weight": 0.20},
    "methodology": {"max_score": 20, "weight": 0.20},
    "data": {"max_score": 25, "weight": 0.25},
    "conclusion": {"max_score": 10, "weight": 0.10},
    "clarity": {"max_score": 5, "weight": 0.05},
    "creativity": {"max_score": 20, "weight": 0.20}
}
```

### 5. Output Paths

```python
OUTPUT_DIR = "outputs"
LITERATURE_OUTPUT_DIR = f"{OUTPUT_DIR}/literature_review"
HYPOTHESIS_OUTPUT_DIR = f"{OUTPUT_DIR}/hypothesis"
ANALYSIS_OUTPUT_DIR = f"{OUTPUT_DIR}/analysis_results"
PAPER_OUTPUT_DIR = f"{OUTPUT_DIR}/paper"
AI_USAGE_OUTPUT_DIR = f"{OUTPUT_DIR}/ai_usage"
VALIDATION_OUTPUT_DIR = f"{OUTPUT_DIR}/validation"
QUALITY_OUTPUT_DIR = f"{OUTPUT_DIR}/quality"
```

### 6. Logging Configuration

```python
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {...},
    "handlers": {...},
    "loggers": {...}
}
```

## Security Best Practices

1. **API 키는 환경 변수로 관리**
   - `.env` 파일에 저장
   - `.gitignore`에 추가
   - 절대 커밋하지 않음

2. **민감한 정보는 하드코딩하지 않음**
   - 모든 토큰, 키는 환경 변수
   - 설정 파일은 버전 관리

3. **설정 검증**
   - 시작 필수 설정 확인
   - 유효성 검사

## Dependencies

### Internal

- 없음 (최상위 설정 모듈)

### External

- **python-dotenv** - 환경 변수 로드
- **pydantic** - 설정 데이터 검증 (선택)

<!-- MANUAL: -->
