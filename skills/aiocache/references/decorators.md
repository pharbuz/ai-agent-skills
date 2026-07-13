# Decorators

aiocache decorators are for async functions. Do not apply them to synchronous
functions.

## cached

Stable `0.12.x` style:

```python
from aiocache import Cache, cached
from aiocache.serializers import PickleSerializer


@cached(ttl=10, cache=Cache.REDIS, key="user:42",
        serializer=PickleSerializer(), namespace="main", port=6379)
async def load_user():
    return {"id": 42}
```

v1 style:

```python
from aiocache import SimpleMemoryCache, cached

cache = SimpleMemoryCache(namespace="main")


@cached(cache, ttl=10, key_builder=lambda *args, **kwargs: "user:42")
async def load_user():
    return {"id": 42}
```

Behavior:

- The function cache is available as `<function>.cache`.
- Generated keys include module, function, args, and kwargs unless overridden.
- Stable `key` takes precedence over stable `key_builder`.
- Use `noself=True` on methods when instance identity should not affect keys.
- Use `skip_cache_func=lambda result: result is None` to avoid caching misses.
- Increase backend pool size for high-concurrency decorated functions.

Injected call flags:

```python
await load_user(cache_read=False)                 # bypass read
await load_user(cache_write=False)                # do not write result
await load_user(aiocache_wait_for_write=False)    # background write
```

## multi_cached

Use when a function accepts an iterable of keys and returns a dict-like mapping.

Stable `0.12.x` style:

```python
from aiocache import Cache, multi_cached


@multi_cached("ids", cache=Cache.REDIS, namespace="users")
async def load_users(ids: tuple[str, ...]) -> dict[str, dict]:
    return {user_id: await fetch_user(user_id) for user_id in ids}
```

v1 style:

```python
from aiocache import SimpleMemoryCache, multi_cached

cache = SimpleMemoryCache(namespace="users")


@multi_cached(cache, keys_from_attr="ids", ttl=60)
async def load_users(ids: tuple[str, ...]) -> dict[str, dict]:
    return {user_id: await fetch_user(user_id) for user_id in ids}
```

Important details:

- `keys_from_attr` names the positional/keyword argument containing requested
  keys.
- If the requested key iterable is empty, the decorator skips cache and calls
  the function.
- If only some keys are cached, aiocache calls the function only with missing
  keys and merges results.
- By default, `multi_cached` keys do not include the function name. Always use a
  namespace or key builder unless keys are globally unique.
- `skip_cache_func` receives `(key, value)` for each returned pair.

## Key Builder Advice

Use stable, string-only keys. Include tenant, feature, version, and data shape
when invalidation matters:

```python
def user_key_builder(func, user_id: str, *args, **kwargs) -> str:
    return f"v2:user:{user_id}"
```

Avoid keys based on raw dict ordering, object `repr`, timestamps, or `self`
unless those values are intentionally part of cache identity.
