#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
프로그래머스 프로필 스크래퍼
GitHub 프로필용 프로그래머스 통계를 가져오는 스크립트
"""

import requests
from bs4 import BeautifulSoup
import json
import time
import os
from datetime import datetime

class ProgrammersScraper:
    def __init__(self, username):
        self.username = username
        self.base_url = "https://programmers.co.kr"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
    
    def get_user_profile(self):
        """프로그래머스 사용자 프로필 정보 가져오기"""
        try:
            # 프로그래머스 사용자 프로필 URL (실제 사용자명으로 변경 필요)
            profile_url = f"{self.base_url}/users/{self.username}"
            response = self.session.get(profile_url)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                return self._parse_profile(soup)
            else:
                print(f"프로필을 찾을 수 없습니다: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"프로필 가져오기 오류: {e}")
            return None
    
    def _parse_profile(self, soup):
        """HTML에서 프로필 정보 파싱"""
        profile_data = {
            'username': self.username,
            'level': 'N/A',
            'solved_problems': 0,
            'rank': 'N/A',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        try:
            # 레벨 정보 찾기
            level_elements = soup.find_all('div', class_='level')
            if level_elements:
                profile_data['level'] = level_elements[0].get_text().strip()
            
            # 해결한 문제 수 찾기
            solved_elements = soup.find_all('span', class_='solved-count')
            if solved_elements:
                profile_data['solved_problems'] = int(solved_elements[0].get_text().strip())
            
            # 순위 정보 찾기 (있는 경우)
            rank_elements = soup.find_all('div', class_='rank')
            if rank_elements:
                profile_data['rank'] = rank_elements[0].get_text().strip()
                
        except Exception as e:
            print(f"프로필 파싱 오류: {e}")
        
        return profile_data
    
    def get_recent_solutions(self, limit=5):
        """최근 해결한 문제들 가져오기"""
        try:
            solutions_url = f"{self.base_url}/users/{self.username}/solutions"
            response = self.session.get(solutions_url)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                return self._parse_solutions(soup, limit)
            else:
                return []
                
        except Exception as e:
            print(f"최근 해결 문제 가져오기 오류: {e}")
            return []
    
    def _parse_solutions(self, soup, limit):
        """해결한 문제 목록 파싱"""
        solutions = []
        try:
            solution_elements = soup.find_all('div', class_='solution-item')[:limit]
            
            for element in solution_elements:
                solution = {
                    'title': element.find('h3').get_text().strip() if element.find('h3') else 'N/A',
                    'language': element.find('span', class_='language').get_text().strip() if element.find('span', class_='language') else 'N/A',
                    'date': element.find('span', class_='date').get_text().strip() if element.find('span', class_='date') else 'N/A'
                }
                solutions.append(solution)
                
        except Exception as e:
            print(f"해결 문제 파싱 오류: {e}")
        
        return solutions

def generate_programmers_stats_html(profile_data, solutions):
    """프로그래머스 통계를 HTML로 생성"""
    html = f"""
    <div align="center">
        <h3>🏆 프로그래머스 통계</h3>
        <table>
            <tr>
                <td><strong>레벨:</strong></td>
                <td>{profile_data['level']}</td>
            </tr>
            <tr>
                <td><strong>해결한 문제:</strong></td>
                <td>{profile_data['solved_problems']}문제</td>
            </tr>
            <tr>
                <td><strong>순위:</strong></td>
                <td>{profile_data['rank']}</td>
            </tr>
        </table>
        
        <h4>📝 최근 해결한 문제</h4>
        <ul>
    """
    
    for solution in solutions:
        html += f"""
            <li>
                <strong>{solution['title']}</strong> 
                ({solution['language']}) - {solution['date']}
            </li>
        """
    
    html += """
        </ul>
        <p><em>마지막 업데이트: {}</em></p>
    </div>
    """.format(profile_data['last_updated'])
    
    return html

def update_readme_with_programmers_data():
    """README.md 파일을 프로그래머스 데이터로 업데이트"""
    # 실제 프로그래머스 사용자명으로 변경하세요
    scraper = ProgrammersScraper('your_programmers_username')
    
    # 프로필 정보 가져오기
    profile_data = scraper.get_user_profile()
    if not profile_data:
        profile_data = {
            'username': 'your_programmers_username',
            'level': 'N/A',
            'solved_problems': 0,
            'rank': 'N/A',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    
    # 최근 해결한 문제 가져오기
    solutions = scraper.get_recent_solutions(5)
    
    # HTML 생성
    programmers_html = generate_programmers_stats_html(profile_data, solutions)
    
    # README.md 파일 읽기
    with open('README.md', 'r', encoding='utf-8') as f:
        readme_content = f.read()
    
    # 프로그래머스 통계 부분 교체
    start_marker = '<!-- 프로그래머스 통계는 API나 웹 스크래핑을 통해 동적으로 업데이트됩니다 -->'
    end_marker = '## 📈 최근 활동'
    
    start_idx = readme_content.find(start_marker)
    end_idx = readme_content.find(end_marker)
    
    if start_idx != -1 and end_idx != -1:
        new_content = (
            readme_content[:start_idx] +
            start_marker + '\n' +
            programmers_html + '\n' +
            readme_content[end_idx:]
        )
        
        # README.md 파일 업데이트
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("README.md 파일이 성공적으로 업데이트되었습니다!")
    else:
        print("README.md 파일에서 마커를 찾을 수 없습니다.")

if __name__ == "__main__":
    print("프로그래머스 스크래퍼 시작...")
    update_readme_with_programmers_data()
    print("완료!") 