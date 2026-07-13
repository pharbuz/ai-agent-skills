# Locking, Testing, And Troubleshooting

## Locking

aiocache locks are not correctness-grade distributed locks. Use them to reduce
duplicate expensive work when occasional duplicate execution is acceptable.

### RedLock

```python
from aiocache import Cache
from aiocache.lock import RedLock

cache = Cache(Cache.REDIS)

async with RedLock(cache, "profile:42:lock", lease=1):
    result = await cache.get("profile:42")
    if result is None:
        result = await load_profile("42")
        await cache.set("profile:42", result, ttl=300)
```

Limits:

- If the lease expires while calls are waiting, all waiting calls may proceed.
- New calls wait at most the lease time.
- Memory locks apply only within the current process.
- Memcached cannot atomically get-and-delete, so any client may release a lock.

### OptimisticLock

```python
from aiocache import Cache
from aiocache.lock import OptimisticLock, OptimisticLockError

cache = Cache(Cache.REDIS)

try:
    async with OptimisticLock(cache, "counter") as lock:
        current = await cache.get("counter", default=0)
        await lock.cas(current + 1)
except OptimisticLockError:
    raise RetryLater()
```

`cas(value)` raises `OptimisticLockError` if another caller changed the value
after the lock was created. If the key did not exist when locked, conflicts are
not produced.

## Testing

Cut dependency on real backends with a `BaseCache` mock:

```python
from unittest.mock import MagicMock
from aiocache.base import BaseCache

cache = MagicMock(spec=BaseCache)
cache.get.return_value = {"id": 1}
```

Disable caching while debugging or in selected test runs:

```bash
AIOCACHE_DISABLE=1 pytest
```

For decorator tests:

- Access the cache via `<function>.cache`.
- Clear or delete concrete keys between tests.
- Close network caches in teardown.
- Avoid sharing alias-backed cache instances between unrelated tests unless that
  is the behavior under test.

## Common Failure Modes

- `asyncio.TimeoutError`: operation exceeded `timeout`; lower backend latency,
  increase timeout, or degrade gracefully.
- Values never expire: check default `ttl`, per-call `ttl`, and `expire(key, 0)`.
- Cached `None` blocks refresh: use `skip_cache_func=lambda r: r is None`.
- `multi_cached` overwrites unrelated values: add `namespace` or a key builder.
- Mutable memory value changes after write: use a serializer that copies data or
  avoid mutating cached objects.
- Redis/Memcached value type mismatch: choose serializer intentionally and check
  old values written by previous serializers.
- Decorated method caches per instance unexpectedly: use `noself=True` when
  instance identity should not be part of the key.
- `raw` works in one backend and fails in another: raw commands are explicitly
  backend-specific.
