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
        f"https://programmers.co.kr/learn/users/{username}/solutions"
    ]
    
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    })
    
    print(f"프로그래머스 사용자명 '{username}'에 대한 URL 테스트:")
    print("=" * 60)
    
    for url in urls_to_test:
        try:
            response = session.get(url)
            status = response.status_code
            if status == 200:
                print(f"✅ {url} - 성공 (200)")
                print(f"   페이지 제목: {response.text[:100]}...")
            elif status == 404:
                print(f"❌ {url} - 찾을 수 없음 (404)")
            else:
                print(f"⚠️  {url} - 상태 코드: {status}")
        except Exception as e:
            print(f"❌ {url} - 오류: {e}")
        print()

if __name__ == "__main__":
    test_programmers_urls("jcm0314") 