# RAG Multi-Agent 프로젝트

**프로젝트 설명:**

이 프로젝트는 RAG (Retrieval-Augmented Generation) 기술과 Multi-Agent 시스템을 활용하여 다양한 작업을 수행하는 것을 목표로 합니다. 현재 다음과 같은 기능을 제공합니다.

*   챗봇: 기본적인 질문 응답 기능
*   뉴스 검색: Naver News API를 이용하여 뉴스 검색 기능 제공

**기술 스택:**

*   Python
*   FastAPI
*   Langchain
*   Redis

**설치 방법:**

1.  Python 3.8 이상 설치
2.  가상 환경 생성 (선택 사항): `python -m venv .venv`
3.  가상 환경 활성화:
    *   Linux/macOS: `source .venv/bin/activate`
    *   Windows: `.venv\Scripts\activate`
4.  패키지 설치: `pip install -r requirements.txt`

**실행 방법:**

1.  `.env` 파일 설정: `backend/.env` 파일을 복사하여 필요한 환경 변수 (예: Naver News API 키)를 설정합니다.
2.  백엔드 실행: `python backend/main.py`

**API 엔드포인트:**

*   `/health`: 헬스 체크 API
*   `/chat`: 챗봇 API

**기여 방법:**

[CONTRIBUTING.md](CONTRIBUTING.md) 파일을 참고해주세요.

**라이선스:**

MIT License