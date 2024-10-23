#!/usr/bin/env python3
"redis"
from typing import Union
import redis
import uuid


class Cache:
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id
