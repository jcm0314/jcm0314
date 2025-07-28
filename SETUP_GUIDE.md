# 🚀 GitHub 프로필 설정 가이드

이 가이드를 따라하면 멋진 GitHub 프로필과 프로그래머스 연동 기능을 가진 프로필을 만들 수 있습니다!

## 📋 목차

1. [사전 준비](#사전-준비)
2. [GitHub 저장소 설정](#github-저장소-설정)
3. [개인 정보 설정](#개인-정보-설정)
4. [프로그래머스 연동](#프로그래머스-연동)
5. [자동 업데이트 설정](#자동-업데이트-설정)
6. [커스터마이징](#커스터마이징)

## 🔧 사전 준비

### 필요한 것들
- GitHub 계정
- 프로그래머스 계정
- Python 3.9 이상

### 패키지 설치
```bash
pip install -r requirements.txt
```

## 🏗️ GitHub 저장소 설정

### 1. 특별한 저장소 생성
GitHub에서 **사용자명과 동일한 이름**의 저장소를 생성하세요.
- 예: 사용자명이 `jcm0314`라면 저장소명도 `jcm0314`로 설정
- 이 저장소의 README.md가 GitHub 프로필에 표시됩니다

### 2. 저장소를 Public으로 설정
프로필이 보이려면 저장소가 Public이어야 합니다.

## 👤 개인 정보 설정

### 1. config.json 파일 수정
`config.json` 파일을 열어서 실제 정보로 업데이트하세요:

```json
{
  "programmers": {
    "username": "실제_프로그래머스_사용자명",
    "update_interval_hours": 24
  },
  "github": {
    "username": "실제_GitHub_사용자명",
    "repository": "저장소명"
  },
  "contact": {
    "email": "실제_이메일@example.com",
    "linkedin": "https://linkedin.com/in/실제_프로필",
    "blog": "https://blog.naver.com/실제_블로그"
  },
  "skills": [
    "JavaScript",
    "TypeScript", 
    "React",
    "Node.js",
    "Python",
    "Java"
  ],
  "goals": [
    "프로그래머스 레벨 3 달성",
    "오픈소스 프로젝트 기여",
    "기술 블로그 운영",
    "알고리즘 문제 1000문제 풀이"
  ]
}
```

### 2. 설정 적용
```bash
python setup_profile.py
```

## 🔗 프로그래머스 연동

### 1. GitHub Secrets 설정
1. GitHub 저장소 페이지로 이동
2. Settings → Secrets and variables → Actions
3. "New repository secret" 클릭
4. Name: `PROGRAMMERS_USERNAME`
5. Value: 실제 프로그래머스 사용자명
6. "Add secret" 클릭

### 2. 수동 테스트
```bash
python programmers_scraper.py
```

## ⚙️ 자동 업데이트 설정

### GitHub Actions 활성화
1. 저장소의 Actions 탭으로 이동
2. "Update Programmers Stats" 워크플로우 클릭
3. "Run workflow" 버튼 클릭하여 수동 실행 테스트

### 스케줄 설정
기본적으로 매일 오전 9시에 자동 업데이트됩니다.
`.github/workflows/update-programmers-stats.yml` 파일에서 스케줄을 변경할 수 있습니다.

## 🎨 커스터마이징

### 기술 스택 변경
`README.md` 파일의 기술 스택 섹션을 수정하세요:

```markdown
<div align="center">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" />
  <!-- 원하는 기술 스택 추가 -->
</div>
```

### 테마 변경
GitHub Stats의 테마를 변경할 수 있습니다:
- `theme=radical` (기본값)
- `theme=dark`
- `theme=light`
- `theme=merko`
- `theme=gruvbox`
- `theme=tokyonight`

### 배지 추가
[Shields.io](https://shields.io/)에서 다양한 배지를 찾아 추가할 수 있습니다.

## 🔍 문제 해결

### 프로그래머스 데이터가 업데이트되지 않는 경우
1. 프로그래머스 사용자명이 정확한지 확인
2. GitHub Secrets 설정 확인
3. GitHub Actions 로그 확인

### README.md가 업데이트되지 않는 경우
1. 파일 권한 확인
2. Git 설정 확인
3. GitHub Actions 권한 확인

## 📈 추가 기능

### 다른 플랫폼 연동
- 백준 온라인 저지
- LeetCode
- HackerRank
- CodeForces

### 커스텀 위젯
- WakaTime 통계
- Spotify Now Playing
- GitHub Trophies

## 🎯 완성 예시

설정이 완료되면 다음과 같은 멋진 프로필을 볼 수 있습니다:

- ✨ 애니메이션 타이핑 효과
- 📊 실시간 GitHub 통계
- 🏆 프로그래머스 연동 통계
- 📈 활동 그래프
- 🛠️ 기술 스택 배지
- 📫 연락처 정보
- 🎯 목표 목록

## 📞 지원

문제가 있거나 개선 사항이 있다면:
1. GitHub Issues 생성
2. Pull Request 제출
3. 이메일로 문의

---

**즐거운 코딩하세요! 🚀** 