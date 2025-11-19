#  backend/core/redis_cache.py
import redis
import json
from backend.core.env_loader import REDIS_HOST, REDIS_PORT, REDIS_DB

def get_redis_connection():
    try:
        conn = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            db=REDIS_DB,
            decode_responses=True
        )
        conn.ping()
        print(f"✅ Redis connected at {REDIS_HOST}:{REDIS_PORT}")
        return conn
    except redis.ConnectionError:
        print("❌ Redis connection failed")
        return None

class RedisChatMemory:
    def __init__(self):
        self.client = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            decode_responses=True
        )
        self.key = "chat_memory"

    def add_message(self, role: str, content: str):
        self.client.rpush(self.key, json.dumps({"role": role, "content": content}))
        # 최근 10개만 유지
        self.client.ltrim(self.key, -10, -1)

    def get_messages(self):
        items = self.client.lrange(self.key, 0, -1)
        return [json.loads(i) for i in items]

    def clear(self):
        self.client.delete(self.key)
