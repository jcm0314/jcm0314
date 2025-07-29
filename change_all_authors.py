`#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
최근 8개 커밋의 사용자 정보를 변경하는 스크립트
"""

import subprocess
import sys

def run_command(command):
    """명령어 실행"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except Exception as e:
        return "", str(e), 1

def change_author_info():
    """최근 8개 커밋의 사용자 정보 변경"""
    
    print("🔧 최근 8개 커밋의 사용자 정보를 변경합니다...")
    print("새로운 사용자: jcm0314 <jcm03141@gmail.com>")
    print()
    
    # 현재 브랜치 확인
    stdout, stderr, code = run_command("git branch --show-current")
    if code != 0:
        print("❌ Git 브랜치 확인 실패")
        return False
    
    current_branch = stdout
    print(f"현재 브랜치: {current_branch}")
    
    # 최근 8개 커밋 확인
    print("\n📋 최근 8개 커밋:")
    stdout, stderr, code = run_command("git log --oneline -8")
    if code == 0:
        print(stdout)
    else:
        print("❌ 커밋 히스토리 확인 실패")
        return False
    
    print("\n⚠️  주의사항:")
    print("1. 이 작업은 커밋 히스토리를 변경합니다.")
    print("2. 이미 푸시된 커밋이라면 강제 푸시가 필요합니다.")
    print("3. 다른 사람과 협업 중이라면 주의가 필요합니다.")
    
    # 사용자 확인
    confirm = input("\n계속하시겠습니까? (y/N): ").strip().lower()
    if confirm != 'y':
        print("❌ 작업이 취소되었습니다.")
        return False
    
    # filter-branch 명령 실행
    print("\n🔄 사용자 정보를 변경하는 중...")
    
    # 최근 8개 커밋만 대상으로 하는 명령
    filter_command = '''
    if [ $GIT_COMMIT = $(git rev-parse HEAD~8) ]; then
        exit 0
    fi
    export GIT_AUTHOR_NAME="jcm0314"
    export GIT_AUTHOR_EMAIL="jcm03141@gmail.com"
    export GIT_COMMITTER_NAME="jcm0314"
    export GIT_COMMITTER_EMAIL="jcm03141@gmail.com"
    '''
    
    # Git filter-branch 실행
    stdout, stderr, code = run_command(f'git filter-branch -f --env-filter "{filter_command}" HEAD~8..HEAD')
    
    if code == 0:
        print("✅ 사용자 정보 변경이 완료되었습니다!")
        print("\n📊 변경된 커밋 확인:")
        stdout, stderr, code = run_command("git log --oneline -8")
        if code == 0:
            print(stdout)
        
        print(f"\n🚀 원격 저장소에 강제 푸시하려면:")
        print(f"git push --force-with-lease origin {current_branch}")
        return True
    else:
        print(f"❌ 사용자 정보 변경 실패: {stderr}")
        return False

if __name__ == "__main__":
    change_author_info() 