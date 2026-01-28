#!/usr/bin/env python3
"""
Git Auto-Commit Module

Provides automatic git commit and push functionality for AI Co-Scientist systems.
Handles checkpoint commits, score tracking, and remote synchronization.
"""

import logging
import subprocess
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List, Any, Optional

logger = logging.getLogger(__name__)


@dataclass
class CommitResult:
    """Result of a commit operation"""
    success: bool
    commit_hash: str
    commit_message: str
    push_success: bool
    error_message: Optional[str] = None
    files_committed: List[str] = None

    def __post_init__(self):
        if self.files_committed is None:
            self.files_committed = []


class GitAutoCommit:
    """
    Automatic git commit and push for AI Co-Scientist iterations

    Features:
    - Checkpoint commits (every N iterations or on score improvement)
    - Structured commit messages with iteration data
    - Automatic push to remote
    - Error handling with retry logic
    - Pre-flight validation
    """

    def __init__(
        self,
        repo_path: str = "./",
        allowed_paths: List[str] = None,
        remote_name: str = "origin",
        max_retries: int = 3,
        retry_delay: float = 1.0
    ):
        """
        Initialize GitAutoCommit

        Args:
            repo_path: Path to git repository (default: "./")
            allowed_paths: List of paths to commit (default: None = all)
            remote_name: Git remote name (default: "origin")
            max_retries: Max push retry attempts (default: 3)
            retry_delay: Delay between retries in seconds (default: 1.0)
        """
        self.repo_path = Path(repo_path).resolve()
        self.allowed_paths = allowed_paths or []
        self.remote_name = remote_name
        self.max_retries = max_retries
        self.retry_delay = retry_delay

        # Validate git repository
        self._validate_repo()

        logger.info(f"GitAutoCommit initialized for {self.repo_path}")

    def pre_flight_check(self) -> Dict[str, Any]:
        """
        Pre-flight validation checks

        Returns:
            Dictionary with check results
        """
        results = {
            'valid_repo': False,
            'has_remote': False,
            'current_branch': None,
            'is_clean': False,
            'errors': []
        }

        try:
            # Check if clean working tree
            status = self._git_command(['status', '--porcelain'])
            results['is_clean'] = len(status.strip()) == 0

            # Get current branch
            branch = self._git_command(['branch', '--show-current'])
            results['current_branch'] = branch.strip()

            # Check remote
            try:
                remote = self._git_command(['remote', '-v'])
                results['has_remote'] = self.remote_name in remote
            except Exception:
                results['errors'].append("No git remote configured")

            results['valid_repo'] = True

        except Exception as e:
            results['errors'].append(str(e))

        return results

    def commit_iteration(
        self,
        iteration: int,
        score: float,
        prev_score: Optional[float] = None,
        improvements: List[Dict[str, Any]] = None,
        checkpoint_only: bool = False
    ) -> CommitResult:
        """
        Commit an iteration's results

        Args:
            iteration: Iteration number
            score: Current score
            prev_score: Previous score (for delta calculation)
            improvements: List of improvements made
            checkpoint_only: If True, only commit without push

        Returns:
            CommitResult with operation details
        """
        try:
            # Calculate score delta
            score_delta = score - (prev_score or score)

            # Generate commit message
            commit_message = self._generate_commit_message(
                iteration, score, score_delta, improvements
            )

            # Stage allowed files
            staged = self._stage_allowed_files()
            if not staged:
                logger.warning("No files to stage")
                return CommitResult(
                    success=False,
                    commit_hash="",
                    commit_message=commit_message,
                    push_success=False,
                    error_message="No files to stage"
                )

            # Create commit
            commit_hash = self._create_commit(commit_message)

            if not commit_hash:
                return CommitResult(
                    success=False,
                    commit_hash="",
                    commit_message=commit_message,
                    push_success=False,
                    error_message="Failed to create commit"
                )

            # Push to remote
            push_success = True
            if not checkpoint_only:
                push_success = self._push_with_retry()

            # Get committed files
            files = self._get_committed_files(commit_hash)

            logger.info(f"Commit created: {commit_hash[:8]}")
            logger.info(f"  Score: {score:.1f} ({score_delta:+.1f})")
            logger.info(f"  Push: {'Success' if push_success else 'Failed'}")

            return CommitResult(
                success=True,
                commit_hash=commit_hash,
                commit_message=commit_message,
                push_success=push_success,
                files_committed=files
            )

        except Exception as e:
            logger.error(f"Commit failed: {e}")
            return CommitResult(
                success=False,
                commit_hash="",
                commit_message="",
                push_success=False,
                error_message=str(e)
            )

    def _validate_repo(self) -> None:
        """Validate git repository"""
        if not (self.repo_path / '.git').exists():
            raise RuntimeError(f"Not a git repository: {self.repo_path}")

    def _git_command(self, args: List[str], capture: bool = True) -> str:
        """
        Execute git command

        Args:
            args: Command arguments
            capture: Whether to capture output

        Returns:
            Command output (if captured)
        """
        cmd = ['git'] + args

        kwargs = {'cwd': self.repo_path}
        if capture:
            kwargs.update({
                'capture_output': True,
                'text': True,
                'check': True
            })

        result = subprocess.run(cmd, **kwargs)

        if capture:
            return result.stdout.strip()
        return ""

    def _generate_commit_message(
        self,
        iteration: int,
        score: float,
        score_delta: float,
        improvements: List[Dict[str, Any]]
    ) -> str:
        """Generate structured commit message"""

        lines = [
            f"[Iteration {iteration}] AI Co-Scientist Progress",
            "",
            f"Score: {score:.1f} ({score_delta:+.1f})",
            ""
        ]

        if improvements:
            lines.append("## Improvements")
            for imp in improvements[:5]:  # Top 5
                priority = imp.get('priority', 'medium').upper()
                target = imp.get('target', 'unknown')
                action = imp.get('action', 'unknown')
                reason = imp.get('reason', '')
                lines.append(f"- [{priority}] {target}: {action}")
                if reason:
                    lines.append(f"  Reason: {reason}")

            if len(improvements) > 5:
                lines.append(f"- ... and {len(improvements) - 5} more")

        lines.extend([
            "",
            f"---",
            f"Generated by AI Co-Scientist System",
            f"Iteration: {iteration}"
        ])

        return "\n".join(lines)

    def _stage_allowed_files(self) -> bool:
        """
        Stage allowed files for commit

        Returns:
            True if files were staged
        """
        # If no restrictions, stage all changes
        if not self.allowed_paths:
            try:
                self._git_command(['add', '-A'], capture=False)
                return True
            except Exception as e:
                logger.error(f"Failed to stage files: {e}")
                return False

        # Stage specific paths
        try:
            for path in self.allowed_paths:
                path_obj = Path(path)
                if path_obj.exists():
                    self._git_command(['add', str(path_obj)], capture=False)

            # Check if anything was staged
            staged = self._git_command(['diff', '--cached', '--name-only'])
            return len(staged.strip()) > 0

        except Exception as e:
            logger.error(f"Failed to stage files: {e}")
            return False

    def _create_commit(self, message: str) -> Optional[str]:
        """
        Create git commit

        Args:
            message: Commit message

        Returns:
            Commit hash or None
        """
        try:
            # Create commit with message
            self._git_command(['commit', '-m', message], capture=False)

            # Get commit hash
            commit_hash = self._git_command(['rev-parse', 'HEAD'])
            return commit_hash

        except Exception as e:
            logger.error(f"Failed to create commit: {e}")
            return None

    def _push_with_retry(self) -> bool:
        """
        Push to remote with retry logic

        Returns:
            True if push succeeded
        """
        for attempt in range(self.max_retries):
            try:
                logger.info(f"Pushing to remote (attempt {attempt + 1}/{self.max_retries})...")

                self._git_command(['push', self.remote_name], capture=False)

                logger.info("Push successful")
                return True

            except subprocess.CalledProcessError as e:
                logger.warning(f"Push attempt {attempt + 1} failed: {e}")

                if attempt < self.max_retries - 1:
                    # Exponential backoff
                    delay = self.retry_delay * (2 ** attempt)
                    logger.info(f"Retrying in {delay:.1f}s...")
                    time.sleep(delay)
                else:
                    logger.error("Push failed after all retries")

        return False

    def _get_committed_files(self, commit_hash: str) -> List[str]:
        """
        Get list of files in commit

        Args:
            commit_hash: Commit hash

        Returns:
            List of file paths
        """
        try:
            output = self._git_command(['diff-tree', '--no-commit-id', '--name-only', '-r', commit_hash])
            return output.split('\n') if output else []
        except Exception:
            return []

    def get_latest_commit(self) -> Optional[str]:
        """
        Get latest commit hash

        Returns:
            Commit hash or None
        """
        try:
            return self._git_command(['rev-parse', 'HEAD'])
        except Exception:
            return None

    def get_commit_log(self, max_count: int = 10) -> List[Dict[str, str]]:
        """
        Get recent commit history

        Args:
            max_count: Maximum number of commits

        Returns:
            List of commit info dictionaries
        """
        try:
            output = self._git_command([
                'log',
                f'-{max_count}',
                '--pretty=format:%H|%s|%ai'
            ])

            commits = []
            for line in output.split('\n'):
                if line:
                    parts = line.split('|')
                    if len(parts) == 3:
                        commits.append({
                            'hash': parts[0],
                            'message': parts[1],
                            'date': parts[2]
                        })

            return commits

        except Exception as e:
            logger.error(f"Failed to get commit log: {e}")
            return []

    def create_checkpoint(self, iteration: int, score: float) -> Optional[str]:
        """
        Create a checkpoint commit (without push)

        Args:
            iteration: Iteration number
            score: Current score

        Returns:
            Commit hash or None
        """
        message = f"[Checkpoint] Iteration {iteration} - Score: {score:.1f}"

        try:
            staged = self._stage_allowed_files()
            if not staged:
                return None

            commit_hash = self._create_commit(message)
            logger.info(f"Checkpoint created: {commit_hash[:8] if commit_hash else 'failed'}")
            return commit_hash

        except Exception as e:
            logger.error(f"Failed to create checkpoint: {e}")
            return None
