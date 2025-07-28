#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
프로그래머스 사용자 ID 찾기 스크립트
"""

import requests
from bs4 import BeautifulSoup
import re

def find_programmers_user_info(username):
    """프로그래머스 사용자 정보 찾기"""
    
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    })
    
    # 다양한 URL 패턴 시도
    test_urls = [
        f"https://programmers.co.kr/learn/users/{username}",
        f"https://programmers.co.kr/learn/profile/{username}",
        f"https://programmers.co.kr/learn/users/{username}/profile",
        f"https://programmers.co.kr/learn/users/{username}/solutions",
        f"https://programmers.co.kr/learn/users/{username}/challenges",
        # 숫자 ID 기반 (일반적인 패턴)
        f"https://programmers.co.kr/learn/users/1",
        f"https://programmers.co.kr/learn/users/10",
        f"https://programmers.co.kr/learn/users/100",
        f"https://programmers.co.kr/learn/users/1000",
        f"https://programmers.co.kr/learn/users/10000",
    ]
    
    print(f"프로그래머스 사용자 '{username}' 정보 찾기:")
    print("=" * 60)
    
    for url in test_urls:
        try:
            response = session.get(url, timeout=10)
            if response.status_code == 200:
                print(f"✅ {url} - 성공")
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # 페이지 제목 확인
                title = soup.find('title')
                if title:
                    print(f"   제목: {title.get_text().strip()}")
                
                # 사용자 정보 찾기
                user_info = extract_user_info(soup)
                if user_info:
                    print(f"   사용자 정보: {user_info}")
                
                # 페이지 내용 일부 확인
                content = soup.get_text()[:200]
                print(f"   내용: {content}...")
                
            elif response.status_code == 404:
                print(f"❌ {url} - 찾을 수 없음")
            else:
                print(f"⚠️  {url} - 상태 코드: {response.status_code}")
                
        except Exception as e:
            print(f"❌ {url} - 오류: {e}")
        print()

def extract_user_info(soup):
    """HTML에서 사용자 정보 추출"""
    info = {}
    
    # 레벨 정보 찾기
    level_elements = soup.find_all(text=re.compile(r'레벨|level|Level', re.IGNORECASE))
    if level_elements:
        info['level'] = level_elements[0].strip()
    
    # 점수 정보 찾기
    score_elements = soup.find_all(text=re.compile(r'점수|score|Score', re.IGNORECASE))
    if score_elements:
        info['score'] = score_elements[0].strip()
    
    # 등수 정보 찾기
    rank_elements = soup.find_all(text=re.compile(r'등수|rank|Rank', re.IGNORECASE))
    if rank_elements:
        info['rank'] = rank_elements[0].strip()
    
    # 해결한 문제 수 찾기
    solved_elements = soup.find_all(text=re.compile(r'해결|solved|문제', re.IGNORECASE))
    if solved_elements:
        info['solved'] = solved_elements[0].strip()
    
    return info if info else None

if __name__ == "__main__":
    find_programmers_user_info("jcm0314") 