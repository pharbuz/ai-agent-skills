> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions/vector-distance-functions](https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/functions/vector-distance-functions)

# Vector distance functions

## vectorL1Distance

Calculates the taxicab distance between numeric array expressions. It can be used to query embedding vectors that are most similar (for example, have the lowest distance) to a given vector.

#### Syntax

`vectorL1Distance(firstExpression, secondExpression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| firstExpression |  | array |  | The first vector between which the distance should be computed |  |  |  | secondExpression |  | array |  | The second vector between which the distance should be computed |  |  |

#### Returns

The data type of the returned value is `double`. Returns `null` for arrays of different lengths and arrays of other types.

#### Examples

##### Example 1

```
data record(a = array(1, 1, 1), b = array(1, 2, 3)),
     record(a = array(1.0, 1.0, 1.0), b = array(1.0, 2.0, 3.0)),
     record(a = array(1, 2), b = array(1, 2)),
     record(a = array(1, 2), b = array(1, 2, 3)),
     record(a = array(1, 2), b = array(1, "foo"))
| fields a, b, vectorL1Distance(a, b)

```

Query result:

| a |  | b |  | vectorL1Distance(a, b) |  | `[1, 1, 1]` |  | `[1, 2, 3]` |  | `3.00` |  | `[1.00, 1.00, 1.00]` |  | `[1.00, 2.00, 3.00]` |  | `3.00` |  | `[1, 2]` |  | `[1, 2]` |  | `0.00` |  | `[1, 2]` |  | `[1, 2, 3]` |  | *null* |  | `[1, 2]` |  | `[1, foo]` |  | *null* |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## vectorL2Distance

Calculates the Euclidean distance between numeric array expressions. It can be used to query embedding vectors that are most similar (for example, have the lowest distance) to a given vector.

#### Syntax

`vectorL2Distance(firstExpression, secondExpression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| firstExpression |  | array |  | The first vector between which the distance should be computed |  |  |  | secondExpression |  | array |  | The second vector between which the distance should be computed |  |  |

#### Returns

The data type of the returned value is `double`. Returns `null` for arrays of different lengths and arrays of other types.

#### Examples

##### Example 1

```
data record(a = array(1, 1, 1), b = array(1, 2, 3)),
     record(a = array(1.0, 1.0, 1.0), b = array(1.0, 2.0, 3.0)),
     record(a = array(1, 2), b = array(1, 2)),
     record(a = array(1, 2), b = array(1, 2, 3)),
     record(a = array(1, 2), b = array(1, "foo"))
| fields a, b, vectorL2Distance(a, b)

```

Query result:

| a |  | b |  | vectorL2Distance(a, b) |  | `[1, 1, 1]` |  | `[1, 2, 3]` |  | `2.24` |  | `[1.00, 1.00, 1.00]` |  | `[1.00, 2.00, 3.00]` |  | `2.24` |  | `[1, 2]` |  | `[1, 2]` |  | `0.00` |  | `[1, 2]` |  | `[1, 2, 3]` |  | *null* |  | `[1, 2]` |  | `[1, foo]` |  | *null* |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## vectorCosineDistance

Calculates the cosine distance between numeric array expressions. It can be used to query embedding vectors that are most similar (for example, have the lowest distance) to a given vector.

#### Syntax

`vectorCosineDistance(firstExpression, secondExpression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| firstExpression |  | array |  | The first vector between which the distance should be computed |  |  |  | secondExpression |  | array |  | The second vector between which the distance should be computed |  |  |

#### Returns

The data type of the returned value is `double`. Returns `null` for arrays of different lengths and arrays of other types.

#### Examples

##### Example 1

```
data record(a = array(1, 1, 1), b = array(1, 2, 3)),
     record(a = array(1.0, 1.0, 1.0), b = array(1.0, 2.0, 3.0)),
     record(a = array(1, 2), b = array(1, 2)),
     record(a = array(1, 2), b = array(1, 2, 3)),
     record(a = array(1, 2), b = array(1, "foo"))
| fields a, b, vectorCosineDistance(a, b)

```

Query result:

| a |  | b |  | vectorCosineDistance(a, b) |  | `[1, 1, 1]` |  | `[1, 2, 3]` |  | `0.07` |  | `[1.00, 1.00, 1.00]` |  | `[1.00, 2.00, 3.00]` |  | `0.07` |  | `[1, 2]` |  | `[1, 2]` |  | `0.00` |  | `[1, 2]` |  | `[1, 2, 3]` |  | *null* |  | `[1, 2]` |  | `[1, foo]` |  | *null* |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## vectorInnerProductDistance

Calculates the negative dot product between numeric array expressions. It can be used to query embedding vectors that are most similar to a given vector.

#### Syntax

`vectorInnerProductDistance(firstExpression, secondExpression)`

#### Parameters

| Parameter |  | Type |  | Description |  | Required |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| firstExpression |  | array |  | The first vector between which the distance should be computed |  |  |  | secondExpression |  | array |  | The second vector between which the distance should be computed |  |  |

#### Returns

The data type of the returned value is `double`. Returns `null` for arrays of different lengths and arrays of other types.

#### Examples

##### Example 1

```
data record(a = array(1, 1, 1), b = array(1, 2, 3)),
     record(a = array(1.0, 1.0, 1.0), b = array(1.0, 2.0, 3.0)),
     record(a = array(1, 2), b = array(1, 2)),
     record(a = array(1, 2), b = array(1, 2, 3)),
     record(a = array(1, 2), b = array(1, "foo"))
| fields a, b, vectorInnerProductDistance(a, b)

```

Query result:

| a |  | b |  | vectorInnerProductDistance(a, b) |  | `[1, 1, 1]` |  | `[1, 2, 3]` |  | `-6.00` |  | `[1.00, 1.00, 1.00]` |  | `[1.00, 2.00, 3.00]` |  | `-6.00` |  | `[1, 2]` |  | `[1, 2]` |  | `-5.00` |  | `[1, 2]` |  | `[1, 2, 3]` |  | *null* |  | `[1, 2]` |  | `[1, foo]` |  | *null* |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
