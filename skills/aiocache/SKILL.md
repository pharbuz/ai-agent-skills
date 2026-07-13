---
name: aiocache
description: >-
  Build, configure, debug, test, or migrate asynchronous Python caching code with
  `aiocache`. Trigger WHENEVER the user installs or imports `aiocache`; uses
  `SimpleMemoryCache`, `RedisCache`, `MemcachedCache`, `ValkeyCache`, `Cache`,
  `caches`, `cached`, `multi_cached`, serializers, plugins, RedLock,
  OptimisticLock, `AIOCACHE_DISABLE`, cache aliases, TTLs, namespaces, raw
  commands, multi_get/multi_set, async cache decorators, FastAPI/aiohttp/Sanic
  caching, Redis/Valkey/Memcached backends, custom serializers/plugins, or fixes
  key collisions, stale values, cache misses, timeout errors, mutable in-memory
  values, decorator behavior, pool/concurrency issues, and v0.12-to-v1 API
  migration problems.
---

# aiocache

Use this skill for Python async caching with `aiocache`. Always inspect the
installed version before editing: current PyPI stable is `0.12.x`, while the
`/en/latest/` docs describe the pre-release `1.0.0a0` API. Do not mix the two
styles in one code path.

```bash
python -m pip show aiocache
python - <<'PY'
import aiocache
print(getattr(aiocache, "__version__", "unknown"))
PY
```

## Version Decision

- For normal `pip install aiocache` projects, assume the stable `0.12.x` API
  unless the lockfile proves otherwise: `Cache`, `caches`, `Cache.REDIS`, and
  decorator cache factories are valid.
- For `1.0.0a0` or docs from `/en/latest/`, use direct cache instances:
  `SimpleMemoryCache(...)`, `MemcachedCache(...)`, or the available network
  backend instance passed into decorators.
- When migrating to v1, remove `Cache(...)` factory usage and `caches` aliases;
  instantiate concrete cache classes and pass instances to decorators.

## Default Workflow

1. Check `aiocache` version, Python version, and optional extras/backend clients.
2. Identify the cache scope: per request, app singleton, decorated function, or
   test double.
3. Choose backend: memory for local/per-process cache, Redis/Valkey for shared
   network cache, Memcached for simple external cache, third-party backends only
   when already used.
4. Pick serializer deliberately: `NullSerializer` only for memory/simple values,
   `JsonSerializer` for JSON-safe data, `PickleSerializer` for trusted Python
   objects, `MsgPackSerializer` when `msgpack` is installed.
5. Set namespaces and key builders to prevent collisions.
6. Set `ttl`, `timeout`, and backend pool size with concurrency in mind.
7. Close network caches during app shutdown or test teardown.
8. Test cache hits, misses, expiry, skipped values, and disabled-cache behavior.

## Minimal Stable API Pattern

```python
from aiocache import Cache
from aiocache.serializers import JsonSerializer


cache = Cache(Cache.REDIS, endpoint="127.0.0.1", port=6379,
              namespace="api", serializer=JsonSerializer(), timeout=1)


async def get_profile(user_id: str) -> dict | None:
    key = f"profile:{user_id}"
    cached = await cache.get(key)
    if cached is not None:
        return cached

    profile = await load_profile(user_id)
    await cache.set(key, profile, ttl=300)
    return profile
```

## Minimal v1-Style Pattern

```python
from aiocache import SimpleMemoryCache
from aiocache.serializers import JsonSerializer


cache = SimpleMemoryCache(namespace="api", serializer=JsonSerializer(), ttl=60)


async def get_value(key: str) -> dict | None:
    return await cache.get(key)
```

## Decision Rules

- Prefer explicit get/set caching when keys, invalidation, or error handling are
  business-critical; use decorators for pure async functions with stable inputs.
- Do not decorate synchronous functions; aiocache decorators are for async
  functions.
- For `multi_cached`, always set a namespace or key builder unless cache keys
  are globally unique.
- Treat `raw(...)` as backend-specific and avoid it in portable abstractions.
- Catch `asyncio.TimeoutError` around cache operations when the app must degrade
  gracefully.
- Do not use aiocache `RedLock` for correctness-critical exclusion; it is a
  performance stampede-reduction tool, not a strong distributed lock.
- In tests, use `AIOCACHE_DISABLE=1`, clear/close function cache objects, or
  mock `BaseCache` instead of relying on shared global cache state.

## References

- Read [references/version-and-migration.md](references/version-and-migration.md)
  before changing imports, decorators, or cache construction.
- Read [references/cache-api-and-backends.md](references/cache-api-and-backends.md)
  for commands, TTLs, namespaces, backend options, and close behavior.
- Read [references/decorators.md](references/decorators.md) for `cached`,
  `multi_cached`, generated keys, injected flags, and collision prevention.
- Read [references/serializers-and-plugins.md](references/serializers-and-plugins.md)
  for built-in serializers, custom serializers, timing/hit-ratio metrics, and
  custom hooks.
- Read [references/locking-testing-troubleshooting.md](references/locking-testing-troubleshooting.md)
  for locks, testing, disable mode, and common failure modes.
- Read [references/examples.md](references/examples.md) for complete code
  patterns copied into Markdown references.
