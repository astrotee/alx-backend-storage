#!/usr/bin/env python3
"redis"
from functools import wraps
from typing import Callable, Optional, Union
import redis
import uuid


def replay(method: Callable) -> None:
    "display the history of calls of a particular function"
    client = redis.Redis()
    name = method.__qualname__
    ncalls = client.get(name).decode()
    inputs = client.lrange(name + ':inputs', 0, -1)
    outputs = client.lrange(name + ':outputs', 0, -1)
    print(f"{name} was called {ncalls} times:")
    for i, o in zip(inputs, outputs):
        print(f"{name}(*{i.decode()}) -> {o.decode()}")


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args):
        self._redis.rpush(method.__qualname__ + ':inputs', str(args))
        output = method(self, *args)
        self._redis.rpush(method.__qualname__ + ':outputs', output)
        return output

    return wrapper


class Cache:
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id

    def get(self, key: str, fn: Optional[Callable] = None):
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is None:
            return value
        return fn(value)

    def get_str(self, key: str):
        return self.get(key, str)

    def get_int(self, key: str):
        return self.get(key, int)
