# Examples

These examples are Markdown reference content for the skill. Adapt imports to
the installed aiocache version before using them in application code.

## Stable 0.12.x Decorator With Redis

```python
import asyncio
from collections import namedtuple

from aiocache import Cache, cached
from aiocache.serializers import PickleSerializer

Result = namedtuple("Result", "content, status")


@cached(ttl=10, cache=Cache.REDIS, key="key",
        serializer=PickleSerializer(), port=6379, namespace="main")
async def cached_call():
    return Result("content", 200)


async def main():
    await cached_call()
    await cached_call()

    cache = Cache(Cache.REDIS, endpoint="127.0.0.1", port=6379, namespace="main")
    assert await cache.exists("key")
    await cache.delete("key")
    await cache.close()


if __name__ == "__main__":
    asyncio.run(main())
```

## v1-Style Decorator With Cache Instance

```python
import asyncio
from collections import namedtuple

from aiocache import SimpleMemoryCache, cached
from aiocache.serializers import PickleSerializer

Result = namedtuple("Result", "content, status")
cache = SimpleMemoryCache(namespace="main", serializer=PickleSerializer())


@cached(cache, ttl=10, key_builder=lambda *args, **kwargs: "key")
async def cached_call():
    return Result("content", 200)


async def main():
    async with cache:
        await cached_call()
        assert await cache.exists("key")
        await cache.delete("key")


if __name__ == "__main__":
    asyncio.run(main())
```

## Stable multi_cached

```python
from aiocache import Cache, multi_cached

DATA = {"a": "Z", "b": "Y", "c": "X", "d": "W"}


@multi_cached("ids", cache=Cache.REDIS, namespace="letters")
async def load_letters(ids=None):
    return {id_: DATA[id_] for id_ in ids}
```

## Custom Compression Serializer

```python
import zlib

from aiocache import Cache
from aiocache.serializers import BaseSerializer


class CompressionSerializer(BaseSerializer):
    DEFAULT_ENCODING = None

    def dumps(self, value):
        return zlib.compress(value.encode())

    def loads(self, value):
        return zlib.decompress(value).decode()


cache = Cache(Cache.REDIS, namespace="main", serializer=CompressionSerializer())
```

## Metrics Plugins

```python
import random

from aiocache import SimpleMemoryCache
from aiocache.plugins import HitMissRatioPlugin, TimingPlugin

cache = SimpleMemoryCache(
    plugins=[HitMissRatioPlugin(), TimingPlugin()],
    namespace="main",
)


async def warm_and_measure():
    await cache.multi_set([("a", "1"), ("b", "2"), ("c", "3")])
    for _ in range(100):
        await cache.get(random.choice(["a", "b", "c", "missing"]))

    return {
        "hit_ratio": cache.hit_miss_ratio["hit_ratio"],
        "get_avg": cache.profiling["get_avg"],
    }
```

## FastAPI Lifespan Pattern

```python
from contextlib import asynccontextmanager

from aiocache import Cache
from fastapi import FastAPI, Request


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.cache = Cache(Cache.REDIS, endpoint="127.0.0.1", namespace="api")
    try:
        yield
    finally:
        await app.state.cache.close()


app = FastAPI(lifespan=lifespan)


@app.get("/items/{item_id}")
async def read_item(item_id: str, request: Request):
    cache = request.app.state.cache
    key = f"item:{item_id}"
    cached = await cache.get(key)
    if cached is not None:
        return cached

    item = {"id": item_id}
    await cache.set(key, item, ttl=60)
    return item
```
