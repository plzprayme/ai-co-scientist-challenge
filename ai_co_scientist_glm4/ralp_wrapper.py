#!/usr/bin/env python3
"""
RALP Wrapper - ULTRAWORK RALP 통합

RALP가 무한으로 실행할 수 있는 래퍼
"""

import subprocess
import sys
import time
from pathlib import Path


def run_ralp_loop():
    """
    ULTRAWORK RALP에 의해 무한으로 실행되는 루프
    
    RALP는 이 함수를 다음과 같이 호출합니다:
    while True:
        run_ralp_loop()
    """
    
    print("\n" + "="*70)
    print(" RALP-MIRROR: AI Co-Scientist Challenge Korea - Track 1")
    print(" Powered by GLM-4.7 + ULTRAWORK RALP")
    print("="*70)
    
    try:
        # main_ralp.py 실행
        result = subprocess.run(
            [sys.executable, "main_ralp.py"],
            capture_output=False,
            text=True,
            timeout=300  # 5분 타임아웃
        )
        
        # 완료 여부 확인
        if result.returncode == 0:
            print("\n✅ 작업 완료!")
            return True  # 완료
        else:
            print(f"\n⚠️ 오류 발생 (exit code: {result.returncode})")
            return False  # 계속 실행
    
    except subprocess.TimeoutExpired:
        print("\n⏱️ 타임아웃 - 다음 반복에서 계속")
        return False
    
    except Exception as e:
        print(f"\n❌ 예외 발생: {e}")
        return False


def run_with_recovery():
    """
    오류 발생 시 자동 복구하며 실행
    """
    max_retries = 10
    retry_count = 0
    
    while True:
        try:
            completed = run_ralp_loop()
            
            if completed:
                print("\n🎉 모든 작업이 완료되었습니다!")
                break
            
            retry_count = 0  # 성공하면 리셋
            
        except KeyboardInterrupt:
            print("\n\n👋 사용자에 의해 중단되었습니다.")
            break
        
        except Exception as e:
            retry_count += 1
            print(f"\n⚠️ 오류 발생 ({retry_count}/{max_retries}): {e}")
            
            if retry_count >= max_retries:
                print("\n❌ 최대 재시도 횟수 초과. 종료합니다.")
                break
            
            time.sleep(5)  # 5초 대기 후 재시도


def main():
    """메인 함수"""
    import argparse
    
    parser = argparse.ArgumentParser(description="RALP-MIRROR Wrapper")
    parser.add_argument(
        '--once',
        action='store_true',
        help='한 번만 실행 (RALP 없이 테스트)'
    )
    parser.add_argument(
        '--reset',
        action='store_true',
        help='상태 초기화 후 실행'
    )
    
    args = parser.parse_args()
    
    # 상태 초기화
    if args.reset:
        state_file = Path("workspace/state.json")
        if state_file.exists():
            state_file.unlink()
            print("상태 파일이 초기화되었습니다.")
    
    if args.once:
        # 한 번만 실행
        run_ralp_loop()
    else:
        # 무한 루프 (RALP에 의해 관리)
        run_with_recovery()


if __name__ == "__main__":
    main()
