# Cache API And Backends

All aiocache backends expose the same core async command interface.

## Core Commands

```python
await cache.add("k", "v", ttl=60)          # fails if key exists
await cache.set("k", "v", ttl=60)
value = await cache.get("k", default=None)
values = await cache.multi_get(["a", "b"])
await cache.multi_set([("a", 1), ("b", 2)], ttl=60)
exists = await cache.exists("k")
count = await cache.increment("counter", delta=1)
await cache.expire("k", ttl=120)
deleted = await cache.delete("k")
await cache.clear(namespace="api")
raw_value = await cache.raw("get", "api:k")
await cache.close()
```

Notes:

- Commands are async and can raise `asyncio.TimeoutError`.
- `add` raises `ValueError` when the key already exists.
- `increment` may create a key and raises `TypeError` for non-incrementable
  values.
- `raw` is not portable across backends; Memcached raw args may need bytes.
- `close()` is still needed for clean shutdown even though later commands may
  reopen resources.

## Constructor Options

Common options:

- `serializer`: `BaseSerializer` instance; default depends on backend.
- `plugins`: list of `BasePlugin` instances.
- `namespace`: prefix used by `build_key`.
- `key_builder`: callable receiving key and namespace.
- `timeout`: operation timeout in seconds; `0` or `None` disables it.
- `ttl`: default expiration in seconds for operations.

TTL compatibility:

- Use integer TTLs for portable Redis/Valkey/Memcached behavior.
- Memory and Redis/Valkey support float TTLs; Memcached portability favors ints.
- `expire(key, 0)` disables expiration.

## Backend Choice

### SimpleMemoryCache

Use for local development, tests, and per-process caches.

```python
from aiocache import SimpleMemoryCache

cache = SimpleMemoryCache(namespace="local", ttl=30, maxsize=1000)
```

Important: with `NullSerializer`, mutable objects are stored by reference. If
you cache a list and mutate it later, reads can observe the mutation.

### RedisCache / ValkeyCache

Use for shared network caches and cross-process state. Stable `0.12.x` projects
commonly use `RedisCache` or `Cache(Cache.REDIS)`. v1 alpha examples use direct
cache instances and may use newer Valkey-oriented examples depending on the
installed package.

```python
from aiocache import Cache
from aiocache.serializers import JsonSerializer

cache = Cache(Cache.REDIS, endpoint="127.0.0.1", port=6379, db=0,
              namespace="api", serializer=JsonSerializer(),
              timeout=1, pool_max_size=20)
```

### MemcachedCache

Use for simple external cache values. Keep TTLs as integers for compatibility.

```python
from aiocache import Cache

cache = Cache(Cache.MEMCACHED, endpoint="127.0.0.1", port=11211, pool_size=2)
```

## Stable Alias Configuration

Stable `0.12.x` supports aliases:

```python
from aiocache import caches

caches.set_config({
    "default": {
        "cache": "aiocache.SimpleMemoryCache",
        "serializer": {"class": "aiocache.serializers.StringSerializer"},
    },
    "redis": {
        "cache": "aiocache.RedisCache",
        "endpoint": "127.0.0.1",
        "port": 6379,
        "serializer": {"class": "aiocache.serializers.JsonSerializer"},
    },
})

same_instance = caches.get("redis")
new_instance = caches.create("redis", namespace="request")
```

`caches.get(alias)` returns the same lazily-created instance. Use
`caches.create(alias, **overrides)` when each caller needs a fresh instance.
