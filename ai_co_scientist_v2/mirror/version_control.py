#!/usr/bin/env python3
"""
Version Controller - 버전 컨트롤러

iteration마다 commit을 생성하고 버전을 관리
"""

import logging
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict

logger = logging.getLogger(__name__)


@dataclass
class Commit:
    """Git-style commit"""
    iteration: int
    message: str
    timestamp: str
    score: float
    score_change: float
    improvements: List[Dict]
    agent_versions: Dict[str, str]
    tag: str


class VersionController:
    """
    버전 컨트롤러
    
    - iteration마다 commit 생성
    - diff 추적
    - rollback 지원
    - changelog 생성
    """
    
    def __init__(self, repo_path: str = "./"):
        self.repo_path = Path(repo_path)
        self.commits: List[Commit] = []
        self.current_version = "1.0.0"
        
        # 출력 디렉토리
        self.submissions_dir = Path("submissions")
        self.submissions_dir.mkdir(exist_ok=True)
        
        self.versions_dir = Path("versions")
        self.versions_dir.mkdir(exist_ok=True)
        
        logger.info("VersionController initialized")
    
    def commit(self, commit_info: Dict[str, Any]) -> Commit:
        """
        iteration 결과를 commit
        
        Args:
            commit_info: 커밋 정보
            
        Returns:
            생성된 Commit 객체
        """
        iteration = commit_info['iteration']
        score = commit_info['score']
        improvements = commit_info.get('improvements', [])
        
        # 점수 변화 계산
        score_change = 0
        if self.commits:
            score_change = score - self.commits[-1].score
        
        # 커밋 메시지 생성
        message = self._generate_commit_message(iteration, score, score_change, improvements)
        
        # 태그 생성 (semantic versioning)
        tag = self._generate_tag(iteration, improvements)
        
        # Commit 객체 생성
        commit = Commit(
            iteration=iteration,
            message=message,
            timestamp=datetime.now().isoformat(),
            score=score,
            score_change=score_change,
            improvements=improvements,
            agent_versions=commit_info.get('agent_versions', {}),
            tag=tag
        )
        
        # 저장
        self.commits.append(commit)
        self._save_commit(commit)
        self._save_submission(iteration, commit_info)
        
        logger.info(f"Commit created: {tag}")
        logger.info(f"  Score: {score:.1f} ({score_change:+.1f})")
        
        return commit
    
    def _generate_commit_message(self, iteration: int, score: float, 
                                  score_change: float, improvements: List[Dict]) -> str:
        """커밋 메시지 생성"""
        lines = [
            f"[Iteration {iteration}] Submission Improvement",
            "",
            f"Score: {score:.1f} ({score_change:+.1f})",
            "",
            "## Improvements",
        ]
        
        # 우선순위별 정렬
        priority_order = {'high': 0, 'medium': 1, 'low': 2}
        sorted_improvements = sorted(
            improvements, 
            key=lambda x: priority_order.get(x.get('priority', 'medium'), 1)
        )
        
        for imp in sorted_improvements[:5]:  # 상위 5개만
            priority = imp.get('priority', 'medium').upper()
            target = imp.get('target', 'unknown')
            action = imp.get('action', 'unknown')
            lines.append(f"- [{priority}] {target}: {action}")
        
        lines.extend([
            "",
            "## Reflection",
            f"- Total improvements: {len(improvements)}",
            f"- High priority: {len([i for i in improvements if i.get('priority') == 'high'])}",
        ])
        
        return "\n".join(lines)
    
    def _generate_tag(self, iteration: int, improvements: List[Dict]) -> str:
        """Semantic versioning 태그 생성"""
        parts = self.current_version.split('.')
        major, minor, patch = int(parts[0]), int(parts[1]), int(parts[2])
        
        # 개선사항 분석
        has_major = any('architecture' in str(i.get('target', '')) for i in improvements)
        has_minor = any('workflow' in str(i.get('target', '')) for i in improvements)
        
        if has_major:
            major += 1
            minor = 0
            patch = 0
        elif has_minor:
            minor += 1
            patch = 0
        else:
            patch += 1
        
        self.current_version = f"{major}.{minor}.{patch}"
        
        return f"v{self.current_version}-iter{iteration}"
    
    def _save_commit(self, commit: Commit) -> None:
        """Commit 저장"""
        # JSON으로 저장
        commit_file = self.versions_dir / f"{commit.tag}.json"
        with open(commit_file, 'w', encoding='utf-8') as f:
            json.dump(asdict(commit), f, ensure_ascii=False, indent=2)
        
        # Commit log에 추가
        log_file = self.versions_dir / "commit_log.txt"
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(f"\n{'='*60}\n")
            f.write(f"Tag: {commit.tag}\n")
            f.write(f"Iteration: {commit.iteration}\n")
            f.write(f"Score: {commit.score:.1f} ({commit.score_change:+.1f})\n")
            f.write(f"Timestamp: {commit.timestamp}\n")
            f.write(f"\n{commit.message}\n")
    
    def _save_submission(self, iteration: int, commit_info: Dict[str, Any]) -> None:
        """제출물 저장"""
        submission_dir = self.submissions_dir / f"iter_{iteration:03d}"
        submission_dir.mkdir(exist_ok=True)
        
        # 메타데이터 저장
        metadata = {
            'iteration': iteration,
            'score': commit_info.get('score', 0),
            'timestamp': datetime.now().isoformat(),
            'improvements': commit_info.get('improvements', [])
        }
        
        with open(submission_dir / "metadata.json", 'w', encoding='utf-8') as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)
    
    def get_diff(self, tag1: str, tag2: str) -> Dict[str, Any]:
        """
        두 버전 간 diff 생성
        
        Args:
            tag1: 첫 번째 태그
            tag2: 두 번째 태그
            
        Returns:
            diff 정보
        """
        commit1 = self._find_commit_by_tag(tag1)
        commit2 = self._find_commit_by_tag(tag2)
        
        if not commit1 or not commit2:
            return {'error': 'Commit not found'}
        
        return {
            'from_tag': tag1,
            'to_tag': tag2,
            'score_change': commit2.score - commit1.score,
            'iteration_delta': commit2.iteration - commit1.iteration,
            'improvements_added': len(commit2.improvements) - len(commit1.improvements),
            'agent_version_changes': self._compare_agent_versions(
                commit1.agent_versions, commit2.agent_versions
            )
        }
    
    def _find_commit_by_tag(self, tag: str) -> Optional[Commit]:
        """태그로 commit 찾기"""
        for commit in self.commits:
            if commit.tag == tag:
                return commit
        return None
    
    def _compare_agent_versions(self, v1: Dict, v2: Dict) -> Dict[str, Any]:
        """에이전트 버전 비교"""
        changes = {}
        
        all_agents = set(v1.keys()) | set(v2.keys())
        
        for agent in all_agents:
            old_ver = v1.get(agent, 'N/A')
            new_ver = v2.get(agent, 'N/A')
            
            if old_ver != new_ver:
                changes[agent] = {
                    'from': old_ver,
                    'to': new_ver
                }
        
        return changes
    
    def rollback(self, tag: str) -> Optional[Commit]:
        """
        특정 버전으로 롤백
        
        Args:
            tag: 롤백할 태그
            
        Returns:
            롤백된 Commit
        """
        commit = self._find_commit_by_tag(tag)
        
        if not commit:
            logger.error(f"Commit with tag {tag} not found")
            return None
        
        # 해당 iteration 이후의 commits 제거
        self.commits = [c for c in self.commits if c.iteration <= commit.iteration]
        
        logger.info(f"Rolled back to {tag}")
        
        return commit
    
    def generate_changelog(self) -> str:
        """
        Changelog 생성
        
        Returns:
            Changelog 내용
        """
        lines = [
            "# Changelog",
            "",
            f"## Total Iterations: {len(self.commits)}",
            f"## Best Score: {max(c.score for c in self.commits) if self.commits else 0:.1f}",
            ""
        ]
        
        for commit in reversed(self.commits):  # 최신순
            lines.extend([
                f"### {commit.tag}",
                "",
                f"**Iteration:** {commit.iteration}",
                f"**Score:** {commit.score:.1f} ({commit.score_change:+.1f})",
                f"**Timestamp:** {commit.timestamp}",
                "",
                "**Improvements:**"
            ])
            
            for imp in commit.improvements[:3]:
                priority = imp.get('priority', 'medium').upper()
                lines.append(f"- [{priority}] {imp.get('target')}: {imp.get('action')}")
            
            lines.append("")
        
        changelog = "\n".join(lines)
        
        # 파일로 저장
        with open(self.versions_dir / "CHANGELOG.md", 'w', encoding='utf-8') as f:
            f.write(changelog)
        
        return changelog
    
    def get_stats(self) -> Dict[str, Any]:
        """버전 통계"""
        if not self.commits:
            return {'message': 'No commits yet'}
        
        scores = [c.score for c in self.commits]
        
        return {
            'total_commits': len(self.commits),
            'current_version': self.current_version,
            'best_score': max(scores),
            'worst_score': min(scores),
            'average_score': sum(scores) / len(scores),
            'score_improvement': scores[-1] - scores[0],
            'total_improvements': sum(len(c.improvements) for c in self.commits)
        }
    
    def list_commits(self) -> List[Dict[str, Any]]:
        """모든 commit 목록"""
        return [
            {
                'tag': c.tag,
                'iteration': c.iteration,
                'score': c.score,
                'score_change': c.score_change,
                'timestamp': c.timestamp,
                'improvement_count': len(c.improvements)
            }
            for c in self.commits
        ]
