"""
Project Configuration Settings
프로젝트 설정 파일

2026 AI Co-Scientist Challenge Korea - Track 1
"""

# =============================================================================
# 연구 설정
# =============================================================================

## 연구 주제 (영문)
RESEARCH_TOPIC = "AI-Driven Methodology for Enhancing Scientific Research Efficiency"

## 연구 분야 (7대 분야 중 선택)
# - bio: 바이오
# - materials_chemistry: 재료·화학
# - earth_science: 지구과학
# - semiconductor: 반도체·디스플레이
# - battery: 이차전지
# - energy: 에너지
# - math: 수학
RESEARCH_FIELD = "materials_chemistry"

## 제출 마감일
TARGET_DATE = "2026-01-31"

# =============================================================================
# AI 모델 설정
# =============================================================================

AI_MODELS = {
    "primary": {
        "name": "claude-3-5-sonnet-20241022",
        "provider": "anthropic",
        "description": "Primary AI for research planning and writing",
    },
    "secondary": {
        "name": "gpt-4",
        "provider": "openai",
        "description": "Secondary AI for data analysis and interpretation",
    },
    "tertiary": {
        "name": "gemini-pro",
        "provider": "google",
        "description": "Tertiary AI for review and feedback",
    },
}

# =============================================================================
# 품질 목표 설정
# =============================================================================

## 목표 품질 점수 (0-100)
TARGET_SCORE = 85

## 최대 반복 횟수
MAX_ITERATIONS = 10

## 최소 AI 기여도 (%)
MIN_AI_CONTRIBUTION = 50

# =============================================================================
# 심사 기준 설정
# =============================================================================

EVALUATION_CRITERIA = {
    "practicality": {
        "name": "주제의 실용성",
        "max_score": 20,
        "weight": 1.0,
    },
    "methodology": {
        "name": "방법론의 적절성",
        "max_score": 20,
        "weight": 1.0,
    },
    "data_quality": {
        "name": "데이터의 적절성",
        "max_score": 25,
        "weight": 1.0,
    },
    "conclusion": {
        "name": "결론의 합리성",
        "max_score": 10,
        "weight": 1.0,
    },
    "readability": {
        "name": "전달력 및 가독성",
        "max_score": 5,
        "weight": 1.0,
    },
    "creativity": {
        "name": "연구의 창의성 및 참신성",
        "max_score": 20,
        "weight": 1.0,
    },
    "ai_contribution": {
        "name": "AI 연구기여도",
        "type": "pass_fail",
        "weight": 1.0,
    },
}

# =============================================================================
# 출력 설정
# =============================================================================

OUTPUT_DIRS = {
    "literature_review": "outputs/literature_review",
    "hypothesis": "outputs/hypothesis",
    "analysis_results": "outputs/analysis_results",
    "paper": "outputs/paper",
    "ai_usage": "outputs/ai_usage",
    "validation": "outputs/validation",
    "quality": "outputs/quality",
    "data": "outputs/data",
    "logs": "logs",
}

# =============================================================================
# 로깅 설정
# =============================================================================

LOGGING_CONFIG = {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "file_encoding": "utf-8",
}

# =============================================================================
# 논문 작성 설정
# =============================================================================

PAPER_CONFIG = {
    "language": "english",
    "format": "academic",
    "sections": [
        "title",
        "abstract",
        "keywords",
        "introduction",
        "related_work",
        "methodology",
        "results",
        "discussion",
        "conclusion",
        "references",
    ],
    "abstract_word_limit": 300,
    "keyword_count": 5,
}

# =============================================================================
# 데이터 설정
# =============================================================================

DATA_CONFIG = {
    "min_sample_size": 30,
    "significance_level": 0.05,
    "confidence_level": 0.95,
    "effect_size_threshold": {
        "small": 0.2,
        "medium": 0.5,
        "large": 0.8,
    },
}

# =============================================================================
# API 설정 (실제 사용 시 채워넣기)
# =============================================================================

API_KEYS = {
    "anthropic": "",  # Claude API Key
    "openai": "",     # OpenAI API Key
    "google": "",     # Google API Key
}

# =============================================================================
# 검색 설정
# =============================================================================

SEARCH_CONFIG = {
    "arxiv": {
        "max_results": 50,
        "sort_by": "relevance",
    },
    "google_scholar": {
        "max_results": 50,
        "sort_by": "relevance",
    },
    "pubmed": {
        "max_results": 50,
        "sort_by": "relevance",
    },
}

# =============================================================================
# 블라인드 평가 설정
# =============================================================================

BLIND_REVIEW_CONFIG = {
    "remove_personal_info": True,
    "remove_institution": True,
    "remove_acknowledgments": True,
    "remove_author_names": True,
}
