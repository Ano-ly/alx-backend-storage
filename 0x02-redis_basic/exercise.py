"""Redis instance/class"""
#!/usr/bin/env python3
import redis
import uuid


class Cache:
    """Class cache"""

    def __init__(self):
        """Initialise the class"""

        self._redis = redis.Redis()
	self._redis.flushdb()

    def store(self, data: (str | int | bytes | float)):
        """Store a key-value pair in the Redis server"""

        keyy = uuid.uuid1()
	self._redis.set(key, data)
	return (key)
