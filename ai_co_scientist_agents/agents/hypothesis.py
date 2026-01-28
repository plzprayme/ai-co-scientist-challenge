"""
Hypothesis Agent
가설 생성 및 실험 설계 에이전트
"""

import logging
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime

logger = logging.getLogger(__name__)


class HypothesisAgent:
    """
    연구 가설 생성 및 실험 설계 에이전트
    
    Responsibilities:
    - 문헌 기반 가설 생성
    - 실험 설계 및 방법론 수립
    - 변수 정의 및 측정 방법 설정
    - 통계적 검정 방법 선정
    """
    
    def __init__(self):
        self.role = "Hypothesis Generator"
        self.results = {}
        logger.info(f"{self.role} initialized")
    
    def generate_hypothesis(self, literature_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        가설 생성 및 실험 설계
        
        Args:
            literature_results: 문헌 조사 결과
            
        Returns:
            가설 및 실험 설계 결과
        """
        logger.info("Generating hypothesis and experimental design...")
        
        # 1. Research Gap 기반 가설 생성
        research_gaps = literature_results.get("research_gaps", [])
        hypotheses = self._generate_hypotheses(research_gaps)
        
        # 2. 실험 설계
        experimental_design = self._design_experiment(hypotheses)
        
        # 3. 변수 정의
        variables = self._define_variables()
        
        # 4. 통계 방법 선정
        statistical_methods = self._select_statistical_methods()
        
        # 5. 결과 저장
        self.results = {
            "status": "completed",
            "timestamp": datetime.now().isoformat(),
            "hypotheses": hypotheses,
            "experimental_design": experimental_design,
            "variables": variables,
            "statistical_methods": statistical_methods,
        }
        
        self._save_results()
        
        logger.info(f"Hypothesis generation completed. Generated {len(hypotheses)} hypotheses.")
        
        return self.results
    
    def _generate_hypotheses(self, research_gaps: List[str]) -> List[Dict[str, Any]]:
        """가설 생성"""
        hypotheses = [
            {
                "id": "H1",
                "statement": "AI-driven methodology significantly improves research efficiency compared to traditional approaches",
                "type": "main",
                "variables": {
                    "independent": "Methodology type (AI-driven vs Traditional)",
                    "dependent": "Research efficiency metrics",
                },
                "testable": True,
                "based_on_gap": research_gaps[0] if research_gaps else "General research need",
            },
            {
                "id": "H2",
                "statement": "Integration of multi-modal data sources enhances prediction accuracy",
                "type": "secondary",
                "variables": {
                    "independent": "Data source integration level",
                    "dependent": "Prediction accuracy",
                },
                "testable": True,
                "based_on_gap": research_gaps[1] if len(research_gaps) > 1 else "Data integration gap",
            },
            {
                "id": "H3",
                "statement": "Automated validation processes reduce time-to-insight by 40%",
                "type": "secondary",
                "variables": {
                    "independent": "Validation process (Automated vs Manual)",
                    "dependent": "Time-to-insight",
                },
                "testable": True,
                "based_on_gap": research_gaps[2] if len(research_gaps) > 2 else "Validation gap",
            },
        ]
        
        return hypotheses
    
    def _design_experiment(self, hypotheses: List[Dict[str, Any]]) -> Dict[str, Any]:
        """실험 설계"""
        return {
            "design_type": "Comparative Study with Control Group",
            "duration": "4-6 weeks",
            "phases": [
                {
                    "name": "Preparation",
                    "duration": "1 week",
                    "activities": [
                        "Data collection and preprocessing",
                        "Tool setup and configuration",
                        "Baseline measurement",
                    ],
                },
                {
                    "name": "Implementation",
                    "duration": "2-3 weeks",
                    "activities": [
                        "Apply AI-driven methodology",
                        "Collect performance metrics",
                        "Document observations",
                    ],
                },
                {
                    "name": "Analysis",
                    "duration": "1-2 weeks",
                    "activities": [
                        "Statistical analysis",
                        "Result interpretation",
                        "Comparison with baseline",
                    ],
                },
            ],
            "control_group": "Traditional methodology approach",
            "treatment_group": "AI-driven methodology approach",
            "sample_size": "Minimum 30 per group (statistical power: 0.8)",
            "randomization": "Stratified random sampling",
            "blinding": "Single-blind (analysts blinded to group assignment)",
        }
    
    def _define_variables(self) -> Dict[str, Any]:
        """변수 정의"""
        return {
            "independent_variables": [
                {
                    "name": "methodology_type",
                    "type": "categorical",
                    "levels": ["AI-driven", "Traditional"],
                    "operational_definition": "Type of research methodology employed",
                },
                {
                    "name": "data_integration_level",
                    "type": "ordinal",
                    "levels": ["Low", "Medium", "High"],
                    "operational_definition": "Number of data sources integrated",
                },
            ],
            "dependent_variables": [
                {
                    "name": "research_efficiency",
                    "type": "continuous",
                    "unit": "tasks per hour",
                    "measurement": "Number of research tasks completed per hour",
                },
                {
                    "name": "prediction_accuracy",
                    "type": "continuous",
                    "unit": "percentage",
                    "measurement": "Percentage of correct predictions",
                },
                {
                    "name": "time_to_insight",
                    "type": "continuous",
                    "unit": "hours",
                    "measurement": "Time from data collection to insight generation",
                },
            ],
            "control_variables": [
                {
                    "name": "researcher_experience",
                    "control_method": "Stratified sampling by experience level",
                },
                {
                    "name": "data_complexity",
                    "control_method": "Use standardized datasets",
                },
            ],
        }
    
    def _select_statistical_methods(self) -> List[Dict[str, Any]]:
        """통계 방법 선정"""
        return [
            {
                "test": "Independent t-test",
                "purpose": "Compare means between two groups",
                "assumptions": [
                    "Normality of residuals",
                    "Homogeneity of variance",
                    "Independence of observations",
                ],
                "alpha": 0.05,
            },
            {
                "test": "ANOVA",
                "purpose": "Compare means across multiple groups",
                "assumptions": [
                    "Normality",
                    "Homoscedasticity",
                    "Independence",
                ],
                "alpha": 0.05,
            },
            {
                "test": "Pearson correlation",
                "purpose": "Measure linear relationships",
                "assumptions": [
                    "Linearity",
                    "Normality",
                    "No outliers",
                ],
                "alpha": 0.05,
            },
            {
                "test": "Regression analysis",
                "purpose": "Predict outcomes and model relationships",
                "assumptions": [
                    "Linearity",
                    "Independence",
                    "Homoscedasticity",
                    "Normality of residuals",
                ],
                "alpha": 0.05,
            },
        ]
    
    def _save_results(self):
        """결과 저장"""
        output_path = Path("outputs/hypothesis/hypothesis_and_methodology.md")
        
        content = f"""# Hypothesis and Methodology

**Generated**: {self.results['timestamp']}

## Research Hypotheses

"""
        for h in self.results['hypotheses']:
            content += f"""
### {h['id']} ({h['type'].upper()})
**Statement**: {h['statement']}

**Variables**:
- Independent: {h['variables']['independent']}
- Dependent: {h['variables']['dependent']}

**Testable**: {h['testable']}
**Based on Gap**: {h['based_on_gap']}

---
"""
        
        content += f"""
## Experimental Design

**Design Type**: {self.results['experimental_design']['design_type']}
**Duration**: {self.results['experimental_design']['duration']}
**Sample Size**: {self.results['experimental_design']['sample_size']}
**Randomization**: {self.results['experimental_design']['randomization']}
**Blinding**: {self.results['experimental_design']['blinding']}

### Phases
"""
        for phase in self.results['experimental_design']['phases']:
            content += f"""
#### {phase['name']} ({phase['duration']})
"""
            for activity in phase['activities']:
                content += f"- {activity}\n"
        
        content += f"""
## Variables

### Independent Variables
"""
        for iv in self.results['variables']['independent_variables']:
            content += f"""
#### {iv['name']}
- **Type**: {iv['type']}
- **Levels**: {', '.join(iv['levels']) if isinstance(iv['levels'], list) else iv['levels']}
- **Definition**: {iv['operational_definition']}
"""
        
        content += f"""
### Dependent Variables
"""
        for dv in self.results['variables']['dependent_variables']:
            content += f"""
#### {dv['name']}
- **Type**: {dv['type']}
- **Unit**: {dv['unit']}
- **Measurement**: {dv['measurement']}
"""
        
        content += f"""
### Control Variables
"""
        for cv in self.results['variables']['control_variables']:
            content += f"""
#### {cv['name']}
- **Control Method**: {cv['control_method']}
"""
        
        content += f"""
## Statistical Methods

"""
        for method in self.results['statistical_methods']:
            content += f"""
### {method['test']}
- **Purpose**: {method['purpose']}
- **Alpha**: {method['alpha']}
- **Assumptions**:
"""
            for assumption in method['assumptions']:
                content += f"  - {assumption}\n"
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        logger.info(f"Hypothesis saved to: {output_path}")
    
    def get_results(self) -> Dict[str, Any]:
        """결과 조회"""
        return self.results
