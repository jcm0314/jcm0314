#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
자동 프로그래머스 뱃지 업데이트 스크립트
GitHub Actions에서 매일 실행되어 프로그래머스 뱃지를 자동으로 업데이트합니다.
"""

import requests
import json
import os
from datetime import datetime
from programmers_badge_generator import ProgrammersBadgeGenerator, update_readme_with_badges
from programmers_api_scraper import get_programmers_stats

def get_programmers_stats_from_api(username):
    """프로그래머스 API에서 실제 통계 가져오기"""
    # GitHub Secrets에서 설정된 사용자명 사용
    env_username = os.getenv('PROGRAMMERS_USERNAME', username)
    
    try:
        # 실제 프로그래머스 데이터 가져오기
        stats = get_programmers_stats(env_username)
        return stats
    except Exception as e:
        print(f"실제 데이터 가져오기 실패, 기본 데이터 사용: {e}")
        
        # 기본 데이터 반환
        return {
            'username': env_username,
            'level': 'Level 1',
            'solved_problems': 0,
            'score': 0,
            'rank': 9999,
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

def update_programmers_badges():
    """프로그래머스 뱃지 자동 업데이트"""
    username = "jcm0314"
    
    print(f"프로그래머스 뱃지 자동 업데이트 시작...")
    print(f"사용자명: {username}")
    print(f"시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    try:
        # 프로그래머스 통계 가져오기
        stats = get_programmers_stats_from_api(username)
        
        print("📊 가져온 통계:")
        for key, value in stats.items():
            print(f"   {key}: {value}")
        
        # README.md 업데이트
        success = update_readme_with_badges(username, stats)
        
        if success:
            print("✅ 프로그래머스 뱃지가 성공적으로 업데이트되었습니다!")
            
            # Git 커밋 및 푸시 (GitHub Actions에서만 실행)
            if os.getenv('GITHUB_ACTIONS'):
                commit_and_push_changes()
            
            return True
        else:
            print("❌ 뱃지 업데이트에 실패했습니다.")
            return False
            
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        return False

def commit_and_push_changes():
    """변경사항을 Git에 커밋하고 푸시"""
    try:
        import subprocess
        
        # Git 설정
        subprocess.run(['git', 'config', '--local', 'user.email', 'action@github.com'], check=True)
        subprocess.run(['git', 'config', '--local', 'user.name', 'GitHub Action'], check=True)
        
        # 변경사항 스테이징
        subprocess.run(['git', 'add', 'README.md'], check=True)
        
        # 커밋
        commit_message = f"Update programmers badges - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        
        # 푸시
        subprocess.run(['git', 'push'], check=True)
        
        print("✅ Git 커밋 및 푸시가 완료되었습니다!")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Git 작업 중 오류 발생: {e}")
    except Exception as e:
        print(f"❌ 예상치 못한 오류: {e}")

def main():
    """메인 함수"""
    print("🚀 프로그래머스 뱃지 자동 업데이트 시스템 시작")
    print("=" * 60)
    
    success = update_programmers_badges()
    
    if success:
        print("\n🎉 자동 업데이트가 성공적으로 완료되었습니다!")
        print("📈 다음 업데이트는 24시간 후에 자동으로 실행됩니다.")
    else:
        print("\n❌ 자동 업데이트에 실패했습니다.")
        print("🔧 로그를 확인하여 문제를 해결해주세요.")
    
    print("=" * 60)

if __name__ == "__main__":
    main() 