#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
프로그래머스 랭킹 뱃지 생성기
GitHub 프로필용 프로그래머스 랭킹 뱃지를 자동으로 생성합니다.
"""

import requests
import json
import os
from datetime import datetime

class ProgrammersBadgeGenerator:
    def __init__(self, username):
        self.username = username
        self.base_url = "https://programmers.co.kr"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
    
    def get_user_stats(self):
        """프로그래머스 사용자 통계 가져오기"""
        # 실제 프로그래머스 API나 웹 스크래핑을 통해 정보를 가져옵니다
        # 현재는 샘플 데이터를 반환합니다
        sample_data = {
            'username': self.username,
            'level': 'Level 2',
            'solved_problems': 45,
            'score': 1250,
            'rank': 1234,
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        return sample_data
    
    def generate_badge_url(self, stats):
        """Shields.io를 사용한 뱃지 URL 생성"""
        # 프로그래머스 레벨 뱃지
        level_badge = f"https://img.shields.io/badge/Programmers-{stats['level']}-00B4AB?style=for-the-badge&logo=programmers&logoColor=white"
        
        # 해결한 문제 수 뱃지
        solved_badge = f"https://img.shields.io/badge/Solved-{stats['solved_problems']}%20Problems-4CAF50?style=for-the-badge&logo=leetcode&logoColor=white"
        
        # 점수 뱃지
        score_badge = f"https://img.shields.io/badge/Score-{stats['score']}-FF6B6B?style=for-the-badge&logo=javascript&logoColor=white"
        
        # 등수 뱃지
        rank_badge = f"https://img.shields.io/badge/Rank-{stats['rank']}-9C27B0?style=for-the-badge&logo=github&logoColor=white"
        
        return {
            'level': level_badge,
            'solved': solved_badge,
            'score': score_badge,
            'rank': rank_badge
        }

def update_readme_with_badges(username, stats):
    """README.md에 프로그래머스 뱃지 추가"""
    badge_gen = ProgrammersBadgeGenerator(username)
    badges = badge_gen.generate_badge_url(stats)
    
    # README.md 파일 읽기
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 프로그래머스 통계 섹션 찾기
    start_marker = '<!-- 프로그래머스 통계는 API나 웹 스크래핑을 통해 동적으로 업데이트됩니다 -->'
    end_marker = '## 📈 최근 활동'
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    if start_idx != -1 and end_idx != -1:
        # 새로운 프로그래머스 섹션 생성
        new_section = f"""
{start_marker}

<div align="center">
    <h3>🏆 프로그래머스 랭킹</h3>
    
    <!-- 프로그래머스 뱃지들 -->
    <div>
        <img src="{badges['level']}" alt="Programmers Level" />
        <img src="{badges['solved']}" alt="Solved Problems" />
        <img src="{badges['score']}" alt="Score" />
        <img src="{badges['rank']}" alt="Rank" />
    </div>
    
    <!-- 상세 통계 테이블 -->
    <table>
        <tr>
            <td><strong>사용자명:</strong></td>
            <td>{stats['username']}</td>
        </tr>
        <tr>
            <td><strong>레벨:</strong></td>
            <td>{stats['level']}</td>
        </tr>
        <tr>
            <td><strong>푼 문제:</strong></td>
            <td>{stats['solved_problems']}문제</td>
        </tr>
        <tr>
            <td><strong>점수:</strong></td>
            <td>{stats['score']}점</td>
        </tr>
        <tr>
            <td><strong>등수:</strong></td>
            <td>{stats['rank']}위</td>
        </tr>
    </table>
    
    <h4>📝 프로그래머스 링크</h4>
    <p>
        <a href="https://programmers.co.kr/learn/challenges">코딩테스트 연습</a> | 
        <a href="https://programmers.co.kr/learn/courses">프로그래밍 강의</a> | 
        <a href="https://programmers.co.kr/learn/me">내 학습</a>
    </p>
    <p><em>마지막 업데이트: {stats['last_updated']}</em></p>
</div>
"""
        
        # README.md 업데이트
        new_content = content[:start_idx] + new_section + content[end_idx:]
        
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("README.md가 프로그래머스 뱃지로 업데이트되었습니다!")
        return True
    else:
        print("README.md에서 마커를 찾을 수 없습니다.")
        return False

def main():
    """메인 함수"""
    username = "jcm0314"
    
    # 샘플 통계 데이터 (실제로는 프로그래머스에서 가져와야 함)
    sample_stats = {
        'username': username,
        'level': 'Level 2',
        'solved_problems': 45,
        'score': 1250,
        'rank': 1234,
        'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    print("프로그래머스 뱃지 생성 중...")
    
    # README.md 업데이트
    success = update_readme_with_badges(username, sample_stats)
    
    if success:
        print("\n✅ 프로그래머스 뱃지가 성공적으로 생성되었습니다!")
        print("📊 샘플 데이터:")
        for key, value in sample_stats.items():
            print(f"   {key}: {value}")
        print("\n💡 실제 데이터로 업데이트하려면 프로그래머스 정보를 알려주세요!")
    else:
        print("❌ 뱃지 생성에 실패했습니다.")

if __name__ == "__main__":
    main() 