#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
프로그래머스 URL 구조 테스트 스크립트
"""

import requests

def test_programmers_urls(username):
    """다양한 프로그래머스 URL 패턴을 테스트"""
    
    urls_to_test = [
        f"https://programmers.co.kr/users/{username}",
        f"https://programmers.co.kr/profile/{username}",
        f"https://programmers.co.kr/learn/users/{username}",
        f"https://programmers.co.kr/learn/profile/{username}",
        f"https://programmers.co.kr/learn/users/{username}/profile",
        f"https://programmers.co.kr/learn/users/{username}/solutions",
        # 새로운 URL 패턴들 추가
        f"https://programmers.co.kr/learn/users/{username}/challenges",
        f"https://programmers.co.kr/learn/users/{username}/stats",
        f"https://programmers.co.kr/learn/users/{username}/achievements",
        # 숫자 ID 기반 URL (일반적인 패턴)
        f"https://programmers.co.kr/learn/users/1",
        f"https://programmers.co.kr/learn/users/100",
        f"https://programmers.co.kr/learn/users/1000"
    ]
    
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    })
    
    print(f"프로그래머스 사용자명 '{username}'에 대한 URL 테스트:")
    print("=" * 60)
    
    for url in urls_to_test:
        try:
            response = session.get(url, timeout=10)
            status = response.status_code
            if status == 200:
                print(f"✅ {url} - 성공 (200)")
                # 페이지 제목이나 특정 텍스트 확인
                if "프로그래머스" in response.text or "programmers" in response.text.lower():
                    print(f"   ✅ 프로그래머스 페이지 확인됨")
                else:
                    print(f"   ⚠️  프로그래머스 페이지가 아닐 수 있음")
            elif status == 404:
                print(f"❌ {url} - 찾을 수 없음 (404)")
            elif status == 403:
                print(f"🚫 {url} - 접근 거부 (403)")
            else:
                print(f"⚠️  {url} - 상태 코드: {status}")
        except Exception as e:
            print(f"❌ {url} - 오류: {e}")
        print()

if __name__ == "__main__":
    test_programmers_urls("jcm0314") 