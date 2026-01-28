#!/usr/bin/env python3
"""
GLM-4.7 API Client

ZhipuAI GLM-4.7 모델 연동 클라이언트
"""

import os
import json
import time
from typing import Optional, Dict, Any, List


class GLM4Client:
    """GLM-4.7 API 클라이언트"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Args:
            api_key: ZhipuAI API 키 (없으면 환경변수 GLM4_API_KEY 사용)
        """
        self.api_key = api_key or os.getenv("GLM4_API_KEY")
        if not self.api_key:
            raise ValueError("API 키가 필요합니다. GLM4_API_KEY 환경변수를 설정하세요.")
        
        try:
            from zhipuai import ZhipuAI
            self.client = ZhipuAI(api_key=self.api_key)
        except ImportError:
            print("경고: zhipuai 패키지가 설치되지 않았습니다. pip install zhipuai")
            self.client = None
        
        self.model = "glm-4.7"  # 또는 "glm-4-flash", "glm-4-plus" 등
    
    def generate(
        self,
        prompt: str,
        temperature: float = 0.7,
        max_tokens: int = 4096,
        top_p: float = 0.7,
        system_prompt: Optional[str] = None,
        retry_count: int = 3
    ) -> str:
        """
        텍스트 생성
        
        Args:
            prompt: 사용자 프롬프트
            temperature: 창의성 (0.0~1.0)
            max_tokens: 최대 토큰 수
            top_p: nucleus sampling
            system_prompt: 시스템 프롬프트
            retry_count: 재시도 횟수
            
        Returns:
            생성된 텍스트
        """
        if not self.client:
            return f"[MOCK] {prompt[:50]}..."
        
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        
        for attempt in range(retry_count):
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    top_p=top_p
                )
                return response.choices[0].message.content
            
            except Exception as e:
                print(f"API 호출 실패 (시도 {attempt + 1}/{retry_count}): {e}")
                if attempt < retry_count - 1:
                    time.sleep(2 ** attempt)  # 지수 백오프
                else:
                    raise
        
        return ""
    
    def generate_json(
        self,
        prompt: str,
        temperature: float = 0.7,
        max_tokens: int = 4096
    ) -> Dict[str, Any]:
        """
        JSON 형식으로 응답받기
        
        Args:
            prompt: 사용자 프롬프트
            temperature: 창의성
            max_tokens: 최대 토큰 수
            
        Returns:
            파싱된 JSON 객체
        """
        # JSON 출력 유도
        json_prompt = f"""
{prompt}

중요: 반드시 유효한 JSON 형식으로만 응답하세요. 추가 설명 없이 JSON만 출력하세요.
"""
        
        response = self.generate(json_prompt, temperature, max_tokens)
        
        # JSON 추출
        try:
            # 코드 블록 제거
            if "```json" in response:
                response = response.split("```json")[1].split("```")[0]
            elif "```" in response:
                response = response.split("```")[1].split("```")[0]
            
            return json.loads(response.strip())
        
        except json.JSONDecodeError as e:
            print(f"JSON 파싱 실패: {e}")
            print(f"원본 응답: {response[:500]}...")
            return {"error": "JSON parsing failed", "raw": response}
    
    def evaluate_paper(
        self,
        paper: str,
        rubric: Dict[str, Any],
        temperature: float = 0.5
    ) -> Dict[str, Any]:
        """
        논문 평가 (심사 기준 기반)
        
        Args:
            paper: 논문 내용
            rubric: 심사 기준
            temperature: 평가 일관성을 위해 낮은 값 권장
            
        Returns:
            평가 결과
        """
        prompt = f"""
당신은 2026 AI Co-Scientist Challenge Korea의 전문 심사위원입니다.
다음 연구보고서를 심사 기준에 따라 객관적으로 평가하세요.

=== 연구보고서 ===
{paper[:5000]}...

=== 심사 기준 ===
1. 주제의 실용성 (20점): {rubric.get('practicality', {}).get('description', '')}
2. 방법론의 적절성 (20점): {rubric.get('methodology', {}).get('description', '')}
3. 데이터의 적절성 (25점): {rubric.get('data_quality', {}).get('description', '')}
4. 결론의 합리성 (10점): {rubric.get('conclusion', {}).get('description', '')}
5. 전달력 및 가독성 (5점): {rubric.get('readability', {}).get('description', '')}
6. 연구의 창의성 (20점): {rubric.get('creativity', {}).get('description', '')}
7. AI 연구기여도 (Pass/Fail): AI가 충분히 기여했는가

=== 응답 형식 ===
반드시 다음 JSON 형식으로만 응답하세요:

{{
    "practicality": {{
        "score": 0-20,
        "reason": "점수를 준 이유",
        "improvement": "개선 방안"
    }},
    "methodology": {{
        "score": 0-20,
        "reason": "점수를 준 이유",
        "improvement": "개선 방안"
    }},
    "data_quality": {{
        "score": 0-25,
        "reason": "점수를 준 이유",
        "improvement": "개선 방안"
    }},
    "conclusion": {{
        "score": 0-10,
        "reason": "점수를 준 이유",
        "improvement": "개선 방안"
    }},
    "readability": {{
        "score": 0-5,
        "reason": "점수를 준 이유",
        "improvement": "개선 방안"
    }},
    "creativity": {{
        "score": 0-20,
        "reason": "점수를 준 이유",
        "improvement": "개선 방안"
    }},
    "ai_contribution": {{
        "pass": true/false,
        "reason": "PASS/FAIL 이유"
    }},
    "total_score": 0-100,
    "summary": "전체 평가 요약"
}}
"""
        
        return self.generate_json(prompt, temperature)
    
    def improve_paper(
        self,
        paper: str,
        weaknesses: List[Dict[str, Any]],
        temperature: float = 0.8
    ) -> str:
        """
        논문 개선
        
        Args:
            paper: 현재 논문
            weaknesses: 약점 목록
            temperature: 창의성
            
        Returns:
            개선된 논문
        """
        prompt = f"""
다음 연구보고서의 약점을 개선하세요.

=== 현재 논문 ===
{paper}

=== 개선이 필요한 부분 ===
{json.dumps(weaknesses, ensure_ascii=False, indent=2)}

=== 지시사항 ===
1. 위 약점들을 해결하세요
2. 전체 구조와 톤은 유지하세요
3. 영문으로 작성하세요
4. 학술 논문 형식을 유지하세요

개선된 논문 전체를 작성하세요.
"""
        
        return self.generate(prompt, temperature, max_tokens=8000)
    
    def self_consistency_evaluate(
        self,
        paper: str,
        rubric: Dict[str, Any],
        n: int = 3
    ) -> Dict[str, Any]:
        """
        Self-consistency 평가 (n번 평가 후 중앙값 선택)
        
        Args:
            paper: 논문 내용
            rubric: 심사 기준
            n: 평가 횟수
            
        Returns:
            집계된 평가 결과
        """
        import statistics
        
        temperatures = [0.3, 0.7, 1.0][:n]  # 다양한 temperature로 평가
        
        evaluations = []
        for i, temp in enumerate(temperatures):
            print(f"  평가 {i+1}/{n} (temp={temp})...")
            result = self.evaluate_paper(paper, rubric, temp)
            evaluations.append(result)
        
        # 중앙값 집계
        def median(values):
            try:
                return statistics.median(values)
            except:
                return sum(values) / len(values)
        
        aggregated = {}
        
        for criterion in ['practicality', 'methodology', 'data_quality', 
                         'conclusion', 'readability', 'creativity']:
            scores = [e.get(criterion, {}).get('score', 0) for e in evaluations 
                     if isinstance(e.get(criterion, {}).get('score'), (int, float))]
            
            if scores:
                aggregated[criterion] = {
                    'score': median(scores),
                    'reason': evaluations[1].get(criterion, {}).get('reason', ''),  # 중간값 사용
                    'improvement': evaluations[1].get(criterion, {}).get('improvement', '')
                }
        
        # AI 기여도는 모두 PASS여야 PASS
        ai_passes = [e.get('ai_contribution', {}).get('pass', False) for e in evaluations]
        aggregated['ai_contribution'] = {
            'pass': all(ai_passes),
            'reason': evaluations[1].get('ai_contribution', {}).get('reason', '')
        }
        
        # 총점
        total = sum([
            aggregated.get(c, {}).get('score', 0) 
            for c in ['practicality', 'methodology', 'data_quality', 
                     'conclusion', 'readability', 'creativity']
        ])
        aggregated['total_score'] = total
        
        return aggregated


# 전역 클라이언트 인스턴스
_glm4_client = None

def get_glm4_client() -> GLM4Client:
    """전역 GLM4Client 인스턴스 가져오기"""
    global _glm4_client
    if _glm4_client is None:
        _glm4_client = GLM4Client()
    return _glm4_client


def glm4_generate(prompt: str, temperature: float = 0.7, max_tokens: int = 4096) -> str:
    """간편한 텍스트 생성 함수"""
    try:
        client = get_glm4_client()
        return client.generate(prompt, temperature, max_tokens)
    except:
        # API 없을 때 mock
        return f"[GLM-4.7: {prompt[:30]}...]"


def glm4_generate_json(prompt: str, temperature: float = 0.7) -> Dict[str, Any]:
    """간편한 JSON 생성 함수"""
    try:
        client = get_glm4_client()
        return client.generate_json(prompt, temperature)
    except:
        return {"error": "API not available"}


def glm4_evaluate(paper: str, rubric: Dict[str, Any]) -> Dict[str, Any]:
    """간편한 평가 함수"""
    try:
        client = get_glm4_client()
        return client.self_consistency_evaluate(paper, rubric)
    except:
        return {"error": "API not available", "total_score": 0}
