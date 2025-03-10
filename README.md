# 장고 챗봇 프로젝트

이 저장소는 Django를 사용하여 개발된 챗봇 애플리케이션의 기본 코드입니다.

## 프로젝트 구조

프로젝트는 다음과 같은 구조로 구성되어 있습니다:

- **chatbot/** - 메인 애플리케이션 디렉토리
- **config/** - Django 설정 파일 디렉토리
- **static/** - 정적 파일(CSS, JavaScript 등)
- **templates/** - HTML 템플릿 파일
- **.gitignore** - Git에서 무시할 파일 목록
- **db.sqlite3** - SQLite 데이터베이스 파일
- **manage.py** - Django 프로젝트 관리 스크립트

## 기술 스택

이 프로젝트는 다음 기술을 사용합니다:
- **Python** (72.8%)
- **HTML** (17.0%)
- **CSS** (10.2%)

## 시작하기

### 필수 조건
- Python 3.x
- Django

### 설치

1. 저장소를 클론합니다:
```bash
git clone https://github.com/greatsangho/chatbot.git
cd chatbot
```

2. 가상환경을 생성하고 활성화합니다:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. 필요한 패키지를 설치합니다:
```bash
pip install -r requirements.txt
```

### 실행

1. 데이터베이스 마이그레이션을 적용합니다:
```bash
python manage.py migrate
```

2. 개발 서버를 실행합니다:
```bash
python manage.py runserver
```

3. 웹 브라우저에서 `http://127.0.0.1:8000/`으로 접속하여 챗봇을 사용합니다.

## 기능

- 사용자 입력을 처리하는 챗봇 인터페이스
- Django 백엔드를 통한 응답 생성
- 간단한 웹 인터페이스
