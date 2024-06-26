#!/usr/bin/env python3
"""Redis instance class"""
import redis
import uuid
from redis import Redis
from typing import Union


class Cache:
    """Class cache"""

    def __init__(self):
        """Initialise the class"""

        self._redis: Redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, int, bytes, float]) -> str:
        """Store a key-value pair in the Redis server"""

        keyy: str = str(uuid.uuid4())
        self._redis.set(keyy, data)
        return (keyy)
