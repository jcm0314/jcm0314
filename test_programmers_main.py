#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
프로그래머스 메인 페이지 테스트 스크립트
"""

import requests
from bs4 import BeautifulSoup

def test_programmers_main():
    """프로그래머스 메인 페이지와 관련 URL들을 테스트"""
    
    urls_to_test = [
        "https://programmers.co.kr",
        "https://programmers.co.kr/",
        "https://programmers.co.kr/learn",
        "https://programmers.co.kr/learn/",
        "https://programmers.co.kr/learn/challenges",
        "https://programmers.co.kr/learn/courses",
        "https://programmers.co.kr/learn/me"
    ]
    
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    })
    
    print("프로그래머스 메인 페이지 테스트:")
    print("=" * 50)
    
    for url in urls_to_test:
        try:
            response = session.get(url, timeout=10)
            status = response.status_code
            if status == 200:
                print(f"✅ {url} - 성공 (200)")
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # 페이지 제목 확인
                title = soup.find('title')
                if title:
                    print(f"   제목: {title.get_text().strip()}")
                
                # 프로그래머스 관련 링크 찾기
                links = soup.find_all('a', href=True)
                programmers_links = [link['href'] for link in links if 'programmers.co.kr' in link['href']]
                if programmers_links:
                    print(f"   발견된 프로그래머스 링크들: {programmers_links[:5]}...")
                
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
    test_programmers_main() 