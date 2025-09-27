import os
import redis
import json
from config import Settings

settings = Settings()

redis_client = redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)

CACHE_EXPIRATION = 60 * 60 * 12

def get_cache(key: str):
    """Retrieve data from Redis by key."""
    cached = redis_client.get(key)
    if cached:
        return json.loads(cached)
    return None

def set_cache(key: str, value: dict):
    """Store data in Redis with expiration."""
    redis_client.setex(key, CACHE_EXPIRATION, json.dumps(value))
