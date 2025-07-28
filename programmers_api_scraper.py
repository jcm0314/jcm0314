#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
프로그래머스 API 스크래퍼
실제 프로그래머스 데이터를 가져오는 스크립트
"""

import requests
import json
import re
from bs4 import BeautifulSoup
from datetime import datetime

class ProgrammersAPIScraper:
    def __init__(self, username):
        self.username = username
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
    
    def get_user_stats(self):
        """프로그래머스 사용자 통계 가져오기"""
        try:
            # 프로그래머스 코딩테스트 페이지에서 정보 가져오기
            stats = self._scrape_coding_test_stats()
            
            if stats:
                return stats
            else:
                # 기본 데이터 반환
                return self._get_default_stats()
                
        except Exception as e:
            print(f"프로그래머스 데이터 가져오기 오류: {e}")
            return self._get_default_stats()
    
    def _scrape_coding_test_stats(self):
        """코딩테스트 통계 스크래핑"""
        try:
            # 프로그래머스 코딩테스트 메인 페이지
            url = "https://programmers.co.kr/learn/challenges"
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # 사용자 정보 찾기 (로그인된 경우)
                user_info = self._extract_user_info(soup)
                
                if user_info:
                    return user_info
                    
        except Exception as e:
            print(f"코딩테스트 페이지 스크래핑 오류: {e}")
        
        return None
    
    def _extract_user_info(self, soup):
        """HTML에서 사용자 정보 추출"""
        try:
            # 다양한 선택자로 사용자 정보 찾기
            selectors = [
                '.user-info',
                '.profile-info',
                '.stats-info',
                '.user-stats',
                '[class*="user"]',
                '[class*="profile"]',
                '[class*="stats"]'
            ]
            
            for selector in selectors:
                elements = soup.select(selector)
                if elements:
                    info = self._parse_user_element(elements[0])
                    if info:
                        return info
            
            # 텍스트 기반 검색
            return self._search_text_for_stats(soup)
            
        except Exception as e:
            print(f"사용자 정보 추출 오류: {e}")
            return None
    
    def _parse_user_element(self, element):
        """사용자 요소 파싱"""
        try:
            text = element.get_text()
            
            # 레벨 찾기
            level_match = re.search(r'레벨\s*(\d+)', text)
            level = f"Level {level_match.group(1)}" if level_match else None
            
            # 해결한 문제 수 찾기
            solved_match = re.search(r'해결\s*(\d+)', text) or re.search(r'(\d+)\s*문제', text)
            solved = int(solved_match.group(1)) if solved_match else None
            
            # 점수 찾기
            score_match = re.search(r'점수\s*(\d+)', text) or re.search(r'(\d+)\s*점', text)
            score = int(score_match.group(1)) if score_match else None
            
            # 등수 찾기
            rank_match = re.search(r'등수\s*(\d+)', text) or re.search(r'(\d+)\s*위', text)
            rank = int(rank_match.group(1)) if rank_match else None
            
            if any([level, solved, score, rank]):
                return {
                    'username': self.username,
                    'level': level or 'Level 1',
                    'solved_problems': solved or 0,
                    'score': score or 0,
                    'rank': rank or 9999,
                    'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                
        except Exception as e:
            print(f"사용자 요소 파싱 오류: {e}")
        
        return None
    
    def _search_text_for_stats(self, soup):
        """전체 텍스트에서 통계 검색"""
        try:
            text = soup.get_text()
            
            # 레벨 패턴
            level_patterns = [
                r'레벨\s*(\d+)',
                r'Level\s*(\d+)',
                r'Lv\.\s*(\d+)'
            ]
            
            # 해결한 문제 패턴
            solved_patterns = [
                r'해결\s*(\d+)',
                r'(\d+)\s*문제',
                r'문제\s*(\d+)'
            ]
            
            # 점수 패턴
            score_patterns = [
                r'점수\s*(\d+)',
                r'(\d+)\s*점',
                r'Score\s*(\d+)'
            ]
            
            # 등수 패턴
            rank_patterns = [
                r'등수\s*(\d+)',
                r'(\d+)\s*위',
                r'Rank\s*(\d+)'
            ]
            
            level = None
            solved = None
            score = None
            rank = None
            
            # 각 패턴 검색
            for pattern in level_patterns:
                match = re.search(pattern, text)
                if match:
                    level = f"Level {match.group(1)}"
                    break
            
            for pattern in solved_patterns:
                match = re.search(pattern, text)
                if match:
                    solved = int(match.group(1))
                    break
            
            for pattern in score_patterns:
                match = re.search(pattern, text)
                if match:
                    score = int(match.group(1))
                    break
            
            for pattern in rank_patterns:
                match = re.search(pattern, text)
                if match:
                    rank = int(match.group(1))
                    break
            
            if any([level, solved, score, rank]):
                return {
                    'username': self.username,
                    'level': level or 'Level 1',
                    'solved_problems': solved or 0,
                    'score': score or 0,
                    'rank': rank or 9999,
                    'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                
        except Exception as e:
            print(f"텍스트 검색 오류: {e}")
        
        return None
    
    def _get_default_stats(self):
        """기본 통계 데이터 반환"""
        return {
            'username': self.username,
            'level': 'Level 1',
            'solved_problems': 0,
            'score': 0,
            'rank': 9999,
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

def get_programmers_stats(username):
    """프로그래머스 통계 가져오기 함수"""
    scraper = ProgrammersAPIScraper(username)
    return scraper.get_user_stats()

if __name__ == "__main__":
    # 테스트
    stats = get_programmers_stats("jcm0314")
    print("프로그래머스 통계:")
    for key, value in stats.items():
        print(f"  {key}: {value}") 