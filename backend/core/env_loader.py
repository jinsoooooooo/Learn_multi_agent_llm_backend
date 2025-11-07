import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

APP_NAME = os.getenv("APP_NAME", "DefaultApp")
APP_ENV = os.getenv("APP_ENV", "production")

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_DB = int(os.getenv("REDIS_DB", 0))

# Naver API 
NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID", "jFgOLYH8gUFQ2_0DhekQ")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET", "Y1xqeZZfF4")