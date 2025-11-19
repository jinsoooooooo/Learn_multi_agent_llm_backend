from fastapi import APIRouter
from backend.core.redis_cache import get_redis_connection

router = APIRouter()

@router.get("/health")
def health_check():
    redis_conn = get_redis_connection()
    redis_status = "connected" if redis_conn else "not connected"
    return {
        "status": "ok",
        "redis": redis_status
    }


