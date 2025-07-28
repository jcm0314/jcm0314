#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub 프로필 설정 스크립트
config.json 파일의 설정을 README.md에 적용합니다.
"""

import json
import re
from datetime import datetime

def load_config():
    """config.json 파일 로드"""
    try:
        with open('config.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("config.json 파일을 찾을 수 없습니다.")
        return None
    except json.JSONDecodeError:
        print("config.json 파일 형식이 올바르지 않습니다.")
        return None

def update_readme_with_config(config):
    """config.json의 설정을 README.md에 적용"""
    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # GitHub 사용자명 업데이트
        content = re.sub(
            r'username=jcm0314',
            f'username={config["github"]["username"]}',
            content
        )
        
        # 연락처 정보 업데이트
        content = re.sub(
            r'mailto:your\.email@example\.com',
            f'mailto:{config["contact"]["email"]}',
            content
        )
        
        content = re.sub(
            r'https://linkedin\.com/in/your-profile',
            config["contact"]["linkedin"],
            content
        )
        
        content = re.sub(
            r'https://blog\.naver\.com/your-blog',
            config["contact"]["blog"],
            content
        )
        
        # 목표 업데이트
        goals_section = "## 🎯 목표\n\n"
        for goal in config["goals"]:
            goals_section += f"- [ ] {goal}\n"
        
        # 기존 목표 섹션 교체
        content = re.sub(
            r'## 🎯 목표\n\n- \[ \].*\n- \[ \].*\n- \[ \].*\n- \[ \].*\n',
            goals_section,
            content
        )
        
        # README.md 파일 업데이트
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("README.md 파일이 성공적으로 업데이트되었습니다!")
        
    except Exception as e:
        print(f"README.md 업데이트 오류: {e}")

def update_programmers_scraper(config):
    """프로그래머스 스크래퍼의 사용자명 업데이트"""
    try:
        with open('programmers_scraper.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 프로그래머스 사용자명 업데이트
        content = re.sub(
            r"scraper = ProgrammersScraper\('your_programmers_username'\)",
            f"scraper = ProgrammersScraper('{config['programmers']['username']}')",
            content
        )
        
        content = re.sub(
            r"'username': 'your_programmers_username'",
            f"'username': '{config['programmers']['username']}'",
            content
        )
        
        # programmers_scraper.py 파일 업데이트
        with open('programmers_scraper.py', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("programmers_scraper.py 파일이 성공적으로 업데이트되었습니다!")
        
    except Exception as e:
        print(f"programmers_scraper.py 업데이트 오류: {e}")

def main():
    """메인 함수"""
    print("GitHub 프로필 설정을 시작합니다...")
    
    # config.json 로드
    config = load_config()
    if not config:
        return
    
    # README.md 업데이트
    update_readme_with_config(config)
    
    # programmers_scraper.py 업데이트
    update_programmers_scraper(config)
    
    print("\n설정이 완료되었습니다!")
    print("\n다음 단계:")
    print("1. config.json 파일에서 실제 정보로 업데이트하세요")
    print("2. GitHub Secrets에 PROGRAMMERS_USERNAME을 추가하세요")
    print("3. 이 저장소를 GitHub에 푸시하세요")
    print("4. GitHub Actions가 자동으로 프로그래머스 통계를 업데이트합니다")

if __name__ == "__main__":
    main() 