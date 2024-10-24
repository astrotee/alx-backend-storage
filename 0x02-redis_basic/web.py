#!/usr/bin/env python3
"web cache"
from functools import wraps
from typing import Callable
import redis
import requests


client = redis.Redis()


def cache(fn: Callable) -> Callable:
    "cache the the return value for 10 seconds"
    @wraps(fn)
    def wrapper(url: str) -> str:
        "function wrapper"
        client.incr(f'count:{url}')
        cached = client.get(url)
        if cached:
            return cached.decode()
        res = fn(url)
        client.setex(url, 10, res)
        return res
    return wrapper


@cache
def get_page(url: str) -> str:
    "get a webpage"
    res = requests.get(url)
    return res.text
