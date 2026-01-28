"""
AI Co-Scientist Challenge Korea - Agents Package
"""

from .director import ResearchDirectorAgent
from .literature import LiteratureReviewAgent
from .hypothesis import HypothesisAgent
from .data_analysis import DataAnalysisAgent
from .paper_writing import PaperWritingAgent
from .ai_logging import AILoggingAgent
from .validation import ValidationAgent
from .quality import QualityAssuranceAgent

__all__ = [
    "ResearchDirectorAgent",
    "LiteratureReviewAgent",
    "HypothesisAgent",
    "DataAnalysisAgent",
    "PaperWritingAgent",
    "AILoggingAgent",
    "ValidationAgent",
    "QualityAssuranceAgent",
]
