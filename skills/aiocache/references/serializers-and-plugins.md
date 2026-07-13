# Serializers And Plugins

Serializers transform values before writing to the backend and after reading
from it. Plugins add async pre/post hooks around cache commands.

## Built-In Serializers

- `NullSerializer`: no transformation. Best for `SimpleMemoryCache` only.
- `StringSerializer`: casts values to `str`; reading an int returns a string.
- `PickleSerializer`: preserves Python objects as bytes. Use only for trusted
  data because pickle is unsafe with untrusted input.
- `JsonSerializer`: stores JSON strings. Good for dict/list/string/number/bool
  data; not for arbitrary Python objects.
- `MsgPackSerializer`: stores msgpack bytes; requires `msgpack`.

```python
from aiocache import Cache
from aiocache.serializers import JsonSerializer

cache = Cache(Cache.REDIS, serializer=JsonSerializer(), namespace="api")
```

## Custom Serializer

Set `DEFAULT_ENCODING = None` when the backend should receive raw bytes.

```python
import zlib
from aiocache.serializers import BaseSerializer


class CompressionSerializer(BaseSerializer):
    DEFAULT_ENCODING = None

    def dumps(self, value: str) -> bytes:
        return zlib.compress(value.encode())

    def loads(self, value: bytes) -> str:
        return zlib.decompress(value).decode()
```

Use custom serializers for compression, schema-aware object encoding, or
compatibility with existing cache values. Keep them deterministic and test both
round-trip and backend raw representation.

## Built-In Plugins

```python
from aiocache import Cache
from aiocache.plugins import HitMissRatioPlugin, TimingPlugin

cache = Cache(plugins=[HitMissRatioPlugin(), TimingPlugin()])
```

- `TimingPlugin` writes timing data to `cache.profiling`, e.g.
  `cache.profiling["get_avg"]`.
- `HitMissRatioPlugin` writes hit data to `cache.hit_miss_ratio`, including
  `total`, `hits`, and `hit_ratio`.

## Custom Plugin

Plugin hook methods must be async. Every command can have `pre_<command>` and
`post_<command>` hooks.

```python
import logging
from aiocache.plugins import BasePlugin

log = logging.getLogger(__name__)


class LoggingPlugin(BasePlugin):
    async def pre_get(self, client, key, *args, **kwargs):
        log.debug("cache get: %s", key)

    async def post_get(self, client, key, took=0, ret=None, **kwargs):
        log.debug("cache get done: key=%s took=%s hit=%s", key, took, ret is not None)
```

Keep hooks cheap. They are awaited inline and count toward command latency and
timeouts. If a post hook fails after a backend write, aiocache will not roll the
backend operation back.
