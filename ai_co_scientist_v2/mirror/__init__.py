"""
MIRROR: Meta-Learning Iterative Research Optimization & Reflection System

2026 AI Co-Scientist Challenge Korea - Track 1
"""

from .engine import MIRROREngine
from .meta_learning import MetaLearningEngine
from .reflection import ReflectionEngine
from .version_control import VersionController

__version__ = "2.0.0"
__all__ = ["MIRROREngine", "MetaLearningEngine", "ReflectionEngine", "VersionController"]
