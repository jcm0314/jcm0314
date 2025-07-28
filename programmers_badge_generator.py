#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
프로그래머스 랭킹 뱃지 생성기
CodingTestStudy 저장소 정보를 바탕으로 프로그래머스 통계 뱃지를 생성합니다.
"""

import os
import json
from datetime import datetime

def generate_programmers_badges():
    """프로그래머스 랭킹 뱃지 생성 (마크다운 형식)"""
    
    # CodingTestStudy 저장소 정보 (실제 데이터 기반)
    programmers_stats = {
        'total_problems': 260,  # 총 커밋 수에서 추정
        'level': '1단계',  # README에서 확인
        'current_streak': '진행중',  # 2025.04.03 ~ 현재
        'study_period': '2024.09.26 ~ 현재',
        'daily_goal': '1단계 1문제',
        'languages': ['Python', 'Java', 'C++', 'C'],
        'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    # 프로그래머스 뱃지 마크다운 생성
    badges_markdown = f"""
## 🏆 프로그래머스 코딩 테스트 현황

<div align="center">

![Level](https://img.shields.io/badge/Level-{programmers_stats['level']}-00B4AB?style=for-the-badge&logo=programmers&logoColor=white)
![Problems](https://img.shields.io/badge/Problems-{programmers_stats['total_problems']}-4F8CC9?style=for-the-badge)
![Streak](https://img.shields.io/badge/Streak-{programmers_stats['current_streak']}-FF6B6B?style=for-the-badge)
![Goal](https://img.shields.io/badge/Goal-{programmers_stats['daily_goal'].replace(' ', '%20')}-28A745?style=for-the-badge)

</div>

### 📊 상세 통계

| 항목 | 내용 |
|------|------|
| 📅 **학습 기간** | {programmers_stats['study_period']} |
| 🎯 **현재 목표** | {programmers_stats['daily_goal']} |
| 💻 **사용 언어** | {', '.join(programmers_stats['languages'])} |
| 📊 **총 문제 수** | {programmers_stats['total_problems']}문제 |

<div align="center">

[![View Repository](https://img.shields.io/badge/View%20Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/jcm0314/CodingTestStudy)

</div>

---

*마지막 업데이트: {programmers_stats['last_updated']}*
"""
    
    return badges_markdown

def update_readme_with_badges():
    """README.md 파일에 프로그래머스 뱃지 추가"""
    try:
        # README.md 파일 읽기
        with open('README.md', 'r', encoding='utf-8') as f:
            readme_content = f.read()
        
        # 프로그래머스 뱃지 생성
        badges_markdown = generate_programmers_badges()
        
        # 기존 프로그래머스 통계 부분 교체
        start_marker = '<!-- 프로그래머스 통계는 API나 웹 스크래핑을 통해 동적으로 업데이트됩니다 -->'
        end_marker = '## 📈 최근 활동'
        
        start_idx = readme_content.find(start_marker)
        end_idx = readme_content.find(end_marker)
        
        if start_idx != -1 and end_idx != -1:
            new_content = (
                readme_content[:start_idx] +
                start_marker + '\n' +
                badges_markdown + '\n' +
                readme_content[end_idx:]
            )
            
            # README.md 파일 업데이트
            with open('README.md', 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print("✅ 프로그래머스 뱃지가 성공적으로 추가되었습니다!")
            return True
        else:
            print("❌ README.md 파일에서 마커를 찾을 수 없습니다.")
            return False
            
    except Exception as e:
        print(f"❌ README.md 업데이트 오류: {e}")
        return False

def create_programmers_stats_json():
    """프로그래머스 통계를 JSON 파일로 저장"""
    stats = {
        'username': 'jcm0314',
        'repository': 'CodingTestStudy',
        'total_problems': 260,
        'level': '1단계',
        'current_streak': '진행중',
        'study_period': '2024.09.26 ~ 현재',
        'daily_goal': '1단계 1문제',
        'languages': ['Python', 'Java', 'C++', 'C'],
        'last_updated': datetime.now().isoformat(),
        'repository_url': 'https://github.com/jcm0314/CodingTestStudy'
    }
    
    with open('programmers_stats.json', 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    
    print("✅ programmers_stats.json 파일이 생성되었습니다.")

if __name__ == "__main__":
    print("🏆 프로그래머스 랭킹 뱃지 생성기 시작...")
    
    # JSON 파일 생성
    create_programmers_stats_json()
    
    # README.md 업데이트
    if update_readme_with_badges():
        print("🎉 모든 작업이 완료되었습니다!")
    else:
        print("⚠️ README.md 업데이트에 실패했습니다.") 