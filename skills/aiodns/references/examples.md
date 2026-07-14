# Examples

These examples are Markdown reference content for the skill.

## Query A Records

```python
import asyncio
import aiodns


async def main():
    resolver = aiodns.DNSResolver(timeout=5)
    try:
        result = await resolver.query_dns("example.com", "A")
        for record in result.answer:
            print(record.data.addr, record.ttl)
    finally:
        await resolver.close()


asyncio.run(main())
```

## Query MX Records

```python
result = await resolver.query_dns("example.com", "MX")
for record in result.answer:
    print(record.data.exchange, record.data.priority)
```

## Resolve Socket Addresses

```python
import socket

result = await resolver.getaddrinfo(
    "example.com",
    family=socket.AF_UNSPEC,
    port=443,
    type=socket.SOCK_STREAM,
)

for node in result.nodes:
    print(node.family, node.socktype, node.protocol, node.addr)
```

## Reverse Lookup

```python
host = await resolver.gethostbyaddr("8.8.8.8")
print(host.name, host.aliases, host.addresses)
```

## Error Handling

```python
import aiodns

try:
    await resolver.query_dns("does-not-exist.invalid", "A")
except aiodns.error.DNSError as exc:
    if exc.args[0] == aiodns.error.ARES_ENOTFOUND:
        print("not found")
    else:
        raise
```

## Short-Lived Resolver For Tests

```python
async with aiodns.DNSResolver(timeout=1) as resolver:
    result = await resolver.query_dns("example.com", "A")
    assert result.answer
```

Use this pattern sparingly. Normal applications should keep one resolver alive
and reuse it for many queries.
