> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions/hash-functions](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions/hash-functions)

# Hash functions

Hash related functions.

## hashCrc32

Returns a CRC32 hash for a given string expression.

#### Syntax

`hashCrc32(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | The string expression that will be hashed. |  |  |

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(s = "DQL is awesome!")
| fieldsAdd hashCrc32(s)

```

Query result:

| s |  | hashCrc32(s) |
| --- | --- | --- |
| `DQL is awesome!` |  | `36481747` |

## hashMd5

Computes the MD5 hash for a given string expression.

#### Syntax

`hashMd5(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | The expression from which the MD5 hash needs to be computed. |  |  |

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(s = "DQL is awesome!")
| fieldsAdd hashMd5(s)

```

Query result:

| s |  | hashMd5(s) |
| --- | --- | --- |
| `DQL is awesome!` |  | `7079b75cde92a3cb0a58b6347ad7bf30` |

## hashSha1

Computes the SHA-1 hash for a given string expression.

#### Syntax

`hashSha1(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | The expression from which the SHA-1 hash needs to be computed. |  |  |

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(s = "DQL is awesome!")
| fieldsAdd hashSha1(s)

```

Query result:

| s |  | hashSha1(s) |
| --- | --- | --- |
| `DQL is awesome!` |  | `baed79aa71682fb2027cf134f5c1e21feb3a3aeb` |

## hashSha256

Returns a SHA-256 hash for the given expression.

#### Syntax

`hashSha256(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | The string expression that will be hashed. |  |  |

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(s = "DQL is awesome!")
| fieldsAdd hashSha256(s)

```

Query result:

| s |  | hashSha256(s) |
| --- | --- | --- |
| `DQL is awesome!` |  | `bdb8d55616dbbbfa1769313b9545064a7f595f31ebf6670c92b96bc40a97068a` |

## hashSha512

Returns a SHA-512 hash for the given expression.

#### Syntax

`hashSha512(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | The string expression that will be hashed. |  |  |

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(s = "DQL is awesome!")
| fieldsAdd hashSha512(s)

```

Query result:

| s |  | hashSha512(s) |
| --- | --- | --- |
| `DQL is awesome!` |  | `f31ed375324e4c1baf4882ebf63351c377ebc0654f2ef557939466e0840672441fbb6abeb9fa7511ea35f88e9d1ebe9a60af7d5682657d17343c2aa6793c5e1f` |

## hashXxHash32

Returns a xxHash32 hash for a given string expression.

#### Syntax

`hashXxHash32(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | The expression that is considered for the hash function. |  |  |

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(s = "DQL is awesome!")
| fieldsAdd hashXxHash32(s)

```

Query result:

| s |  | hashXxHash32(s) |
| --- | --- | --- |
| `DQL is awesome!` |  | `1018219528` |

## hashXxHash64

Returns a xxHash64 hash for a given string expression.

#### Syntax

`hashXxHash64(expression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |
| --- | --- | --- | --- | --- | --- | --- |
| expression |  | string |  | The expression that is considered for the hash function. |  |  |

#### Returns

The data type of the returned value is `string`.

#### Examples

##### Example 1

```
data record(s = "DQL is awesome!")
| fieldsAdd hashXxHash64(s)

```

Query result:

| s |  | hashXxHash64(s) |
| --- | --- | --- |
| `DQL is awesome!` |  | `-458681598079680010` |
