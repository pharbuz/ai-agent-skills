# Version And Migration

The public docs have two important tracks:

- PyPI stable package: `aiocache 0.12.3` is the latest stable release shown on
  PyPI as of 2026-07-13.
- Documentation at `/en/latest/`: `aiocache 1.0.0a0`, a pre-release API with
  breaking changes.

Always inspect the installed version and lockfile before editing. A project may
use stable `0.12.x` even if a user linked the latest docs.

## Stable 0.12.x API

Use this style when the installed package is `0.12.x`:

```python
from aiocache import Cache, caches, cached, multi_cached
from aiocache.serializers import PickleSerializer

cache = Cache(Cache.REDIS, endpoint="127.0.0.1", port=6379,
              namespace="main", serializer=PickleSerializer())
```

Stable features:

- `Cache` factory with `Cache.MEMORY`, `Cache.REDIS`, and `Cache.MEMCACHED`.
- `caches.set_config`, `caches.get`, `caches.create`, and aliases.
- `@cached(ttl=..., cache=Cache.REDIS, serializer=..., namespace=..., **kwargs)`.
- `@multi_cached("ids", cache=Cache.REDIS, namespace=...)`.

## v1.0.0a0 API

Use this style only when the project intentionally targets v1 alpha:

```python
from aiocache import SimpleMemoryCache, cached

cache = SimpleMemoryCache(namespace="main", ttl=60)


@cached(cache, ttl=10, key_builder=lambda *args, **kwargs: "key")
async def expensive_call():
    return "value"
```

v1 changes:

- `aiocache.Cache` has been removed.
- Cache aliases have been removed.
- Decorators take a fully instantiated cache object instead of backend factory
  arguments.
- Use concrete cache classes directly.

## Migration Checklist

- Replace `Cache(Cache.MEMORY)` with `SimpleMemoryCache(...)`.
- Replace `Cache(Cache.MEMCACHED, ...)` with `MemcachedCache(...)`.
- Replace configured aliases with explicit application-level cache instances.
- Replace decorator factory arguments with instantiated cache objects.
- Move `endpoint`, `port`, serializer, namespace, timeout, and plugins into the
  cache constructor.
- Update tests that used `caches.get(...)` to use the app's cache instance.

## Compatibility Rule

When maintaining libraries, avoid importing both APIs at module import time.
Either pin supported `aiocache` versions or hide construction behind a small
adapter that checks feature availability once.
