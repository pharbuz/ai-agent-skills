# Helpers Dsl

> Local snapshot generated from OpenSearch Python Client API Reference on 2026-07-27. Use this file instead of browsing the live documentation during skill execution.


## Source: `api-ref/helpers.html`

## helpers

- aggs
- analysis
- document
- faceted_search
- field
- function
- index
- mapping
- query
- search
- update_by_query
- wrappers


## Source: `api-ref/helpers/aggs.html`

## aggs

### `class opensearchpy.helpers.aggs.Agg(_expand__to_dot=True, **params)`

Bases: DslBase

### `Parameters:`

-
_expand__to_dot (Any)

-
params (Any)

### `to_dict()`

Serialize the DSL object to plain dict

### `Return type:`

Any


## Source: `api-ref/helpers/analysis.html`

## analysis

### `class opensearchpy.helpers.analysis.Analyzer(_expand__to_dot=True, **params)`

Bases: AnalysisBase, DslBase

### `Parameters:`

-
_expand__to_dot (Any)

-
params (Any)


## Source: `api-ref/helpers/document.html`

## document

### `class opensearchpy.helpers.document.Document(meta=None, **kwargs)`

Bases: ObjectBase

Model-like class for persisting documents in opensearch.

### `Parameters:`

-
meta (Any)

-
kwargs (Any)

### `__repr__()`

Return repr(self).

### `Return type:`

str

### `delete(using=None, index=None, **kwargs)`

Delete the instance in opensearch.

### `Parameters:`

-
index (Any | None) – opensearch index to use, if the Document is associated with an index this can be omitted.

-
using (Any | None) – connection alias to use, defaults to 'default'

-
using

-
index

-
kwargs (Any)

### `Return type:`

Any

Any additional keyword arguments will be passed to OpenSearch.delete unchanged.

### `classmethod exists(id, using=None, index=None, **kwargs)`

check if exists a single document from opensearch using its id.

### `Parameters:`

-
id (Any) – id of the document to check if exists

-
index (Any | None) – opensearch index to use, if the Document is associated with an index this can be omitted.

-
using (Any | None) – connection alias to use, defaults to 'default'

-
id

-
using

-
index

-
kwargs (Any)

### `Return type:`

Any

Any additional keyword arguments will be passed to OpenSearch.exists unchanged.

### `classmethod get(id, using=None, index=None, **kwargs)`

Retrieve a single document from opensearch using its id.

### `Parameters:`

-
id (Any) – id of the document to be retrieved

-
index (Any | None) – opensearch index to use, if the Document is associated with an index this can be omitted.

-
using (Any | None) – connection alias to use, defaults to 'default'

-
id

-
using

-
index

-
kwargs (Any)

### `Return type:`

Any

Any additional keyword arguments will be passed to OpenSearch.get unchanged.

### `classmethod init(index=None, using=None)`

Create the index and populate the mappings in opensearch.

### `Parameters:`

-
index (Any | None)

-
using (Any | None)

### `Return type:`

None

### `classmethod mget(docs, using=None, index=None, raise_on_error=True, missing='none', **kwargs)`

Retrieve multiple document by their id’s. Returns a list of instances in the same order as requested.

### `Parameters:`

-
docs (Any) – list of id’s of the documents to be retrieved or a list of document specifications as per https://opensearch.org/docs/latest/opensearch/rest-api/document-apis/multi-get/

-
index (Any | None) – opensearch index to use, if the Document is associated with an index this can be omitted.

-
using (Any | None) – connection alias to use, defaults to 'default'

-
missing (str) – what to do when one of the documents requested is not found. Valid options are 'none' (use None), 'raise' (raise NotFoundError) or 'skip' (ignore the missing document).

-
docs

-
using

-
index

-
raise_on_error (bool)

-
missing

-
kwargs (Any)

### `Return type:`

Any

Any additional keyword arguments will be passed to OpenSearch.mget unchanged.

### `save(using=None, index=None, validate=True, skip_empty=True, return_doc_meta=False, **kwargs)`

Save the document into opensearch. If the document doesn’t exist it is created, it is overwritten otherwise. Returns True if this operations resulted in new document being created.

### `Parameters:`

-
index (Any | None) – opensearch index to use, if the Document is associated with an index this can be omitted.

-
using (Any | None) – connection alias to use, defaults to 'default'

-
validate (bool) – set to False to skip validating the document

-
skip_empty (bool) – if set to False will cause empty values (None, [], {}) to be left on the document. Those values will be stripped out otherwise as they make no difference in opensearch.

-
return_doc_meta (bool) – set to True to return all metadata from the update API call instead of only the operation result

-
using

-
index

-
validate

-
skip_empty

-
return_doc_meta

-
kwargs (Any)

### `Return type:`

Any

Any additional keyword arguments will be passed to OpenSearch.index unchanged.

:return operation result created/updated

### `classmethod search(using=None, index=None)`

Create an Search instance that will search over this Document.

### `Parameters:`

-
using (Any | None)

-
index (Any | None)

### `Return type:`

Any

### `to_dict(include_meta=False, skip_empty=True)`

Serialize the instance into a dictionary so that it can be saved in opensearch.

### `Parameters:`

-
include_meta (bool) – if set to True will include all the metadata (_index, _id etc). Otherwise just the document’s data is serialized. This is useful when passing multiple instances into opensearchpy.helpers.bulk.

-
skip_empty (bool) – if set to False will cause empty values (None, [], {}) to be left on the document. Those values will be stripped out otherwise as they make no difference in opensearch.

-
include_meta

-
skip_empty

### `Return type:`

Any

### `update(using=None, index=None, detect_noop=True, doc_as_upsert=False, refresh=False, retry_on_conflict=0, script=None, script_id=None, scripted_upsert=False, upsert=None, return_doc_meta=False, **fields)`

Partial update of the document, specify fields you wish to update and both the instance and the document in opensearch will be updated:

```python
doc = MyDocument(title='Document Title!')
doc.save()
doc.update(title='New Document Title!')
```

### `Parameters:`

-
index (Any | None) – opensearch index to use, if the Document is associated with an index this can be omitted.

-
using (Any | None) – connection alias to use, defaults to 'default'

-
detect_noop (bool) – Set to False to disable noop detection.

-
refresh (bool) – Control when the changes made by this request are visible to search. Set to True for immediate effect.

-
retry_on_conflict (int) – In between the get and indexing phases of the update, it is possible that another process might have already updated the same document. By default, the update will fail with a version conflict exception. The retry_on_conflict parameter controls how many times to retry the update before finally throwing an exception.

-
doc_as_upsert (bool) – Instead of sending a partial doc plus an upsert doc, setting doc_as_upsert to true will use the contents of doc as the upsert value

-
return_doc_meta (bool) – set to True to return all metadata from the index API call instead of only the operation result

-
using

-
index

-
detect_noop

-
doc_as_upsert

-
refresh

-
retry_on_conflict

-
script (Any | None)

-
script_id (Any | None)

-
scripted_upsert (bool)

-
upsert (Any | None)

-
return_doc_meta

-
fields (Any)

### `Return type:`

Any

:return operation result noop/updated


## Source: `api-ref/helpers/faceted_search.html`

## faceted_search

### `class opensearchpy.helpers.faceted_search.FacetedSearch(query=None, filters={}, sort=())`

Bases: object

Abstraction for creating faceted navigation searches that takes care of composing the queries, aggregations and filters as needed as well as presenting the results in an easy-to-consume fashion:

```python
class BlogSearch(FacetedSearch):
    index = 'blogs'
    doc_types = [Blog, Post]
    fields = ['title^5', 'category', 'description', 'body']

    facets = {
        'type': TermsFacet(field='_type'),
        'category': TermsFacet(field='category'),
        'weekly_posts': DateHistogramFacet(field='published_from', interval='week')
    }

    def search(self):
        ' Override search to add your own filters '
        s = super(BlogSearch, self).search()
        return s.filter('term', published=True)

# when using:
blog_search = BlogSearch("web framework", filters={"category": "python"})

# supports pagination
blog_search[10:20]

response = blog_search.execute()

# easy access to aggregation results:
for category, hit_count, is_selected in response.facets.category:
    print(
        "Category %s has %d hits%s." % (
            category,
            hit_count,
            ' and is chosen' if is_selected else ''
        )
    )
```

### `Parameters:`

-
query (Any) – the text to search for

-
filters (Any) – facet values to filter

-
sort (Any) – sort information to be passed to Search

-
query

-
filters

-
sort

### `add_filter(name, filter_values)`

Add a filter for a facet.

### `Parameters:`

-
name (Any)

-
filter_values (Any)

### `Return type:`

Any

### `aggregate(search)`

Add aggregations representing the facets selected, including potential filters.

### `Parameters:`

search (Any)

### `Return type:`

Any

### `build_search()`

Construct the Search object.

### `Return type:`

Any

### `execute()`

Execute the search and return the response.

### `Return type:`

Any

### `filter(search)`

Add a post_filter to the search request narrowing the results based on the facet filters.

### `Parameters:`

search (Any)

### `Return type:`

Any

### `highlight(search)`

Add highlighting for all the fields

### `Parameters:`

search (Any)

### `Return type:`

Any

### `query(search, query)`

Add query part to search.

Override this if you wish to customize the query used.

### `Parameters:`

-
search (Any)

-
query (Any)

### `Return type:`

Any

### `search()`

Returns the base Search object to which the facets are added.

You can customize the query by overriding this method and returning a modified search object.

### `Return type:`

Any

### `sort(search)`

Add sorting information to the request.

### `Parameters:`

search (Any)

### `Return type:`

Any


## Source: `api-ref/helpers/field.html`

## field

### `class opensearchpy.helpers.field.Field(multi=False, required=False, *args, **kwargs)`

Bases: DslBase

### `Parameters:`

-
multi (bool) – specifies whether field can contain array of values

-
required (bool) – specifies whether field is required

-
multi

-
required

-
args (Any)

-
kwargs (Any)

### `to_dict()`

Serialize the DSL object to plain dict

### `Return type:`

Any


## Source: `api-ref/helpers/function.html`

## function

### `class opensearchpy.helpers.function.ScoreFunction(_expand__to_dot=True, **params)`

Bases: DslBase

### `Parameters:`

-
_expand__to_dot (Any)

-
params (Any)

### `to_dict()`

Serialize the DSL object to plain dict

### `Return type:`

Any


## Source: `api-ref/helpers/index.html`

## index

### `class opensearchpy.helpers.index.Index(name, using='default')`

Bases: object

### `Parameters:`

-
name (Any) – name of the index

-
using (Any) – connection alias to use, defaults to 'default'

-
name

-
using

### `aliases(**kwargs)`

Add aliases to the index definition:

```python
i = Index('blog-v2')
i.aliases(blog={}, published={'filter': Q('term', published=True)})
```

### `Parameters:`

kwargs (Any)

### `Return type:`

Any

### `analyze(using=None, **kwargs)`

Perform the analysis process on a text and return the tokens breakdown of the text.

Any additional keyword arguments will be passed to OpenSearch.indices.analyze unchanged.

### `Parameters:`

-
using (OpenSearch | None)

-
kwargs (Any)

### `Return type:`

Any

### `analyzer(*args, **kwargs)`

Explicitly add an analyzer to an index. Note that all custom analyzers defined in mappings will also be created. This is useful for search analyzers.

Example:

```python
from opensearchpy import analyzer, tokenizer

my_analyzer = analyzer('my_analyzer',
    tokenizer=tokenizer('trigram', 'nGram', min_gram=3, max_gram=3),
    filter=['lowercase']
)

i = Index('blog')
i.analyzer(my_analyzer)
```

### `Parameters:`

-
args (Any)

-
kwargs (Any)

### `Return type:`

Any

### `clear_cache(using=None, **kwargs)`

Clear all caches or specific cached associated with the index.

Any additional keyword arguments will be passed to OpenSearch.indices.clear_cache unchanged.

### `Parameters:`

-
using (OpenSearch | None)

-
kwargs (Any)

### `Return type:`

Any

### `clone(name=None, using=None)`

Create a copy of the instance with another name or connection alias. Useful for creating multiple indices with shared configuration:

```python
i = Index('base-index')
i.settings(number_of_shards=1)
i.create()

i2 = i.clone('other-index')
i2.create()
```

### `Parameters:`

-
name (Any | None) – name of the index

-
using (Any | None) – connection alias to use, defaults to 'default'

-
name

-
using

### `Return type:`

Any

### `close(using=None, **kwargs)`

Closes the index in opensearch.

Any additional keyword arguments will be passed to OpenSearch.indices.close unchanged.

### `Parameters:`

-
using (OpenSearch | None)

-
kwargs (Any)

### `Return type:`

Any

### `create(using=None, **kwargs)`

Creates the index in opensearch.

Any additional keyword arguments will be passed to OpenSearch.indices.create unchanged.

### `Parameters:`

-
using (OpenSearch | None)

-
kwargs (Any)

### `Return type:`

Any

### `delete(using=None, **kwargs)`

Deletes the index in opensearch.

Any additional keyword arguments will be passed to OpenSearch.indices.delete unchanged.

### `Parameters:`

-
using (OpenSearch | None)

-
kwargs (Any)

### `Return type:`

Any

### `delete_alias(using=None, **kwargs)`

Delete specific alias.

Any additional keyword arguments will be passed to OpenSearch.indices.delete_alias unchanged.

### `Parameters:`

-
using (OpenSearch | None)

-
kwargs (Any)

### `Return type:`

Any

### `document(document)`

Associate a Document subclass with an index. This means that, when this index is created, it will contain the mappings for the Document. If the Document class doesn’t have a default index yet (by defining classIndex), this instance will be used. Can be used as a decorator:

```python
i = Index('blog')

@i.document
class Post(Document):
    title = Text()

# create the index, including Post mappings
i.create()

# .search() will now return a Search object that will return
# properly deserialized Post instances
s = i.search()
```

### `Parameters:`

document (Any)

### `Return type:`

Any

### `exists(using=None, **kwargs)`

Returns True if the index already exists in opensearch.

Any additional keyword arguments will be passed to OpenSearch.indices.exists unchanged.

### `Parameters:`

-
using (OpenSearch | None)

-
kwargs (Any)

### `Return type:`

Any

### `exists_alias(using=None, **kwargs)`

Return a boolean indicating whether given alias exists for this index.

Any additional keyword arguments will be passed to OpenSearch.indices.exists_alias unchanged.

### `Parameters:`

-
using (OpenSearch | None)

-
kwargs (Any)

### `Return type:`

Any

### `flush(using=None, **kwargs)`

Performs a flush operation on the index.

Any additional keyword arguments will be passed to OpenSearch.indices.flush unchanged.

### `Parameters:`

-
using (OpenSearch | None)

-
kwargs (Any)

### `Return type:`

Any

### `forcemerge(using=None, **kwargs)`

The force merge API allows to force merging of the index through an API. The merge relates to the number of segments a Lucene index holds within each shard. The force merge operation allows to reduce the number of segments by merging them.

This call will block until the merge is complete. If the http connection is lost, the request will continue in the background, and any new requests will block until the previous force merge is complete.

Any additional keyword arguments will be passed to OpenSearch.indices.forcemerge unchanged.

### `Parameters:`

-
using (OpenSearch | None)

-
kwargs (Any)

### `Return type:`

Any

### `get(using=None, **kwargs)`

The get index API allows to retrieve information about the index.

Any additional keyword arguments will be passed to OpenSearch.indices.get unchanged.

### `Parameters:`

-
using (OpenSearch | None)

-
kwargs (Any)

### `Return type:`

Any

### `get_alias(using=None, **kwargs)`

Retrieve a specified alias.

Any additional keyword arguments will be passed to OpenSearch.indices.get_alias unchanged.

### `Parameters:`

-
using (OpenSearch | None)

-
kwargs (Any)

### `Return type:`

Any

### `get_field_mapping(using=None, **kwargs)`

Retrieve mapping definition of a specific field.

Any additional keyword arguments will be passed to OpenSearch.indices.get_field_mapping unchanged.

### `Parameters:`

-
using (OpenSearch | None)

-
kwargs (Any)

### `Return type:`

Any

### `get_mapping(using=None, **kwargs)`

Retrieve specific mapping definition for a specific type.

Any additional keyword arguments will be passed to OpenSearch.indices.get_mapping unchanged.

### `Parameters:`

-
using (OpenSearch | None)

-
kwargs (Any)

### `Return type:`

Any

### `get_settings(using=None, **kwargs)`

Retrieve settings for the index.

Any additional keyword arguments will be passed to OpenSearch.indices.get_settings unchanged.

### `Parameters:`

-
using (OpenSearch | None)

-
kwargs (Any)

### `Return type:`

Any

### `get_upgrade(using=None, **kwargs)`

Monitor how much of the index is upgraded.

Any additional keyword arguments will be passed to OpenSearch.indices.get_upgrade unchanged.

### `Parameters:`

-
using (OpenSearch | None)

-
kwargs (Any)

### `Return type:`

Any

### `mapping(mapping)`

Associate a mapping (an instance of Mapping) with this index. This means that, when this index is created, it will contain the mappings for the document type defined by those mappings.

### `Parameters:`

mapping (Any)

### `Return type:`

Any

### `open(using=None, **kwargs)`

Opens the index in opensearch.

Any additional keyword arguments will be passed to OpenSearch.indices.open unchanged.

### `Parameters:`

-
using (OpenSearch | None)

-
kwargs (Any)

### `Return type:`

Any

### `put_alias(using=None, **kwargs)`

Create an alias for the index.

Any additional keyword arguments will be passed to OpenSearch.indices.put_alias unchanged.

### `Parameters:`

-
using (OpenSearch | None)

-
kwargs (Any)

### `Return type:`

Any

### `put_mapping(using=None, **kwargs)`

Register specific mapping definition for a specific type.

Any additional keyword arguments will be passed to OpenSearch.indices.put_mapping unchanged.

### `Parameters:`

-
using (OpenSearch | None)

-
kwargs (Any)

### `Return type:`

Any

### `put_settings(using=None, **kwargs)`

Change specific index level settings in real time.

Any additional keyword arguments will be passed to OpenSearch.indices.put_settings unchanged.

### `Parameters:`

-
using (OpenSearch | None)

-
kwargs (Any)

### `Return type:`

Any

### `recovery(using=None, **kwargs)`

The indices recovery API provides insight into on-going shard recoveries for the index.

Any additional keyword arguments will be passed to OpenSearch.indices.recovery unchanged.

### `Parameters:`

-
using (OpenSearch | None)

-
kwargs (Any)

### `Return type:`

Any

### `refresh(using=None, **kwargs)`

Performs a refresh operation on the index.

Any additional keyword arguments will be passed to OpenSearch.indices.refresh unchanged.

### `Parameters:`

-
using (OpenSearch | None)

-
kwargs (Any)

### `Return type:`

Any

### `save(using=None)`

Sync the index definition with opensearch, creating the index if it doesn’t exist and updating its settings and mappings if it does.

Note some settings and mapping changes cannot be done on an open index (or at all on an existing index) and for those this method will fail with the underlying exception.

### `Parameters:`

using (OpenSearch | None)

### `Return type:`

Any

### `search(using=None)`

Return a Search object searching over the index (or all the indices belonging to this template) and its Documents.

### `Parameters:`

using (OpenSearch | None)

### `Return type:`

Search

### `segments(using=None, **kwargs)`

Provide low level segments information that a Lucene index (shard level) is built with.

Any additional keyword arguments will be passed to OpenSearch.indices.segments unchanged.

### `Parameters:`

-
using (OpenSearch | None)

-
kwargs (Any)

### `Return type:`

Any

### `settings(**kwargs)`

Add settings to the index:

```python
i = Index('i')
i.settings(number_of_shards=1, number_of_replicas=0)
```

Multiple calls to settings will merge the keys, later overriding the earlier.

### `Parameters:`

kwargs (Any)

### `Return type:`

Any

### `shard_stores(using=None, **kwargs)`

Provides store information for shard copies of the index. Store information reports on which nodes shard copies exist, the shard copy version, indicating how recent they are, and any exceptions encountered while opening the shard index or from earlier engine failure.

Any additional keyword arguments will be passed to OpenSearch.indices.shard_stores unchanged.

### `Parameters:`

-
using (OpenSearch | None)

-
kwargs (Any)

### `Return type:`

Any

### `shrink(using=None, **kwargs)`

The shrink index API allows you to shrink an existing index into a new index with fewer primary shards. The number of primary shards in the target index must be a factor of the shards in the source index. For example an index with 8 primary shards can be shrunk into 4, 2 or 1 primary shards or an index with 15 primary shards can be shrunk into 5, 3 or 1. If the number of shards in the index is a prime number it can only be shrunk into a single primary shard. Before shrinking, a (primary or replica) copy of every shard in the index must be present on the same node.

Any additional keyword arguments will be passed to OpenSearch.indices.shrink unchanged.

### `Parameters:`

-
using (OpenSearch | None)

-
kwargs (Any)

### `Return type:`

Any

### `stats(using=None, **kwargs)`

Retrieve statistics on different operations happening on the index.

Any additional keyword arguments will be passed to OpenSearch.indices.stats unchanged.

### `Parameters:`

-
using (OpenSearch | None)

-
kwargs (Any)

### `Return type:`

Any

### `updateByQuery(using=None)`

Return a UpdateByQuery object searching over the index (or all the indices belonging to this template) and updating Documents that match the search criteria.

For more information, see here: https://opensearch.org/docs/latest/opensearch/rest-api/document-apis/update-by-query/

### `Parameters:`

using (OpenSearch | None)

### `Return type:`

UpdateByQuery

### `upgrade(using=None, **kwargs)`

Upgrade the index to the latest format.

Any additional keyword arguments will be passed to OpenSearch.indices.upgrade unchanged.

### `Parameters:`

-
using (OpenSearch | None)

-
kwargs (Any)

### `Return type:`

Any

### `validate_query(using=None, **kwargs)`

Validate a potentially expensive query without executing it.

Any additional keyword arguments will be passed to OpenSearch.indices.validate_query unchanged.

### `Parameters:`

-
using (OpenSearch | None)

-
kwargs (Any)

### `Return type:`

Any


## Source: `api-ref/helpers/mapping.html`

## mapping

### `class opensearchpy.helpers.mapping.Mapping`

Bases: object

### `__repr__()`

Return repr(self).

### `Return type:`

str


## Source: `api-ref/helpers/query.html`

## query

### `class opensearchpy.helpers.query.Query(_expand__to_dot=True, **params)`

Bases: DslBase

### `Parameters:`

-
_expand__to_dot (Any)

-
params (Any)

### `__or__(other)`

Return self|value.

### `Parameters:`

other (Any)

### `Return type:`

Any


## Source: `api-ref/helpers/search.html`

## search

### `class opensearchpy.helpers.search.Search(**kwargs)`

Bases: Request

Search request to opensearch.

### `Parameters:`

-
using – OpenSearch instance to use

-
index – limit the search to index

-
doc_type – only query this type.

-
kwargs (Any)

All the parameters supplied (or omitted) at creation type can be later overridden by methods (using, index and doc_type respectively).

### `__getitem__(n)`

Support slicing the Search instance for pagination.

Slicing equates to the from/size parameters. E.g.:

```python
s = Search().query(...)[0:25]
```

is equivalent to:

```python
s = Search().query(...).extra(from_=0, size=25)
```

### `Parameters:`

n (Any)

### `Return type:`

Any

### `__iter__()`

Iterate over the hits.

### `Return type:`

Any

### `_clone()`

Return a clone of the current search request. Performs a shallow copy of all the underlying objects. Used internally by most state modifying APIs.

### `Return type:`

Any

### `collapse(field=None, inner_hits=None, max_concurrent_group_searches=None)`

Add collapsing information to the search request.

If called without providing field, it will remove all collapse requirements, otherwise it will replace them with the provided arguments.

The API returns a copy of the Search object and can thus be chained.

### `Parameters:`

-
field (Any | None)

-
inner_hits (Any | None)

-
max_concurrent_group_searches (Any | None)

### `Return type:`

Any

### `count()`

Return the number of hits matching the query and filters. Note that only the actual number is returned.

### `Return type:`

Any

### `delete()executesthequerybydelegatingtodelete_by_query()`

### `Return type:`

Any

### `execute(ignore_cache=False)`

Execute the search and return an instance of Response wrapping all the data.

### `Parameters:`

-
ignore_cache (bool) – if set to True, consecutive calls will hit OpenSearch, while cached result will be ignored. Defaults to False

-
ignore_cache

### `Return type:`

Any

### `classmethod from_dict(d)`

Construct a new Search instance from a raw dict containing the search body. Useful when migrating from raw dictionaries.

Example:

```python
s = Search.from_dict({
    "query": {
        "bool": {
            "must": [...]
        }
    },
    "aggs": {...}
})
s = s.filter('term', published=True)
```

### `Parameters:`

d (Any)

### `Return type:`

Any

### `highlight(*fields, **kwargs)`

Request highlighting of some fields. All keyword arguments passed in will be used as parameters for all the fields in the fields parameter. Example:

```python
Search().highlight('title', 'body', fragment_size=50)
```

will produce the equivalent of:

```python
{
    "highlight": {
        "fields": {
            "body": {"fragment_size": 50},
            "title": {"fragment_size": 50}
        }
    }
}
```

If you want to have different options for different fields you can call highlight twice:

```python
Search().highlight('title', fragment_size=50).highlight('body', fragment_size=100)
```

which will produce:

```python
{
    "highlight": {
        "fields": {
            "body": {"fragment_size": 100},
            "title": {"fragment_size": 50}
        }
    }
}
```

### `Parameters:`

-
fields (Any)

-
kwargs (Any)

### `Return type:`

Any

### `highlight_options(**kwargs)`

Update the global highlighting options used for this request. For example:

```python
s = Search()
s = s.highlight_options(order='score')
```

### `Parameters:`

kwargs (Any)

### `Return type:`

Any

### `response_class(cls)`

Override the default wrapper used for the response.

### `Parameters:`

cls (Any)

### `Return type:`

Any

### `scan()`

Turn the search into a scan search and return a generator that will iterate over all the documents matching the query.

Use params method to specify any additional arguments you with to pass to the underlying scan helper from opensearchpy

### `Return type:`

Any

### `script_fields(**kwargs)`

Define script fields to be calculated on hits.

Example:

```python
s = Search()
s = s.script_fields(times_two="doc['field'].value * 2")
s = s.script_fields(
    times_three={
        'script': {
            'lang': 'painless',
            'source': "doc['field'].value * params.n",
            'params': {'n': 3}
        }
    }
)
```

### `Parameters:`

kwargs (Any)

### `Return type:`

Any

### `sort(*keys)`

Add sorting information to the search request. If called without arguments it will remove all sort requirements. Otherwise it will replace them. Acceptable arguments are:

```python
'some.field'
'-some.other.field'
{'different.field': {'any': 'dict'}}
```

so for example:

```python
s = Search().sort(
    'category',
    '-title',
    {"price" : {"order" : "asc", "mode" : "avg"}}
)
```

will sort by category, title (in descending order) and price in ascending order using the avg mode.

The API returns a copy of the Search object and can thus be chained.

### `Parameters:`

keys (Any)

### `Return type:`

Any

### `source(fields=None, **kwargs)`

Selectively control how the _source field is returned.

### `Parameters:`

-
fields (Any | None) – wildcard string, array of wildcards, or dictionary of includes and excludes

-
fields

-
kwargs (Any)

### `Return type:`

Any

If fields is None, the entire document will be returned for each hit. If fields is a dictionary with keys of ‘includes’ and/or ‘excludes’ the fields will be either included or excluded appropriately.

Calling this multiple times with the same named parameter will override the previous values with the new ones.

Example:

```python
s = Search()
s = s.source(includes=['obj1.*'], excludes=["*.description"])

s = Search()
s = s.source(includes=['obj1.*']).source(excludes=["*.description"])
```

### `suggest(name, text, **kwargs)`

Add a suggestions request to the search.

### `Parameters:`

-
name (Any) – name of the suggestion

-
text (Any) – text to suggest on

-
name

-
text

-
kwargs (Any)

### `Return type:`

Any

All keyword arguments will be added to the suggestions body. For example:

```python
s = Search()
s = s.suggest('suggestion-1', 'OpenSearch', term={'field': 'body'})
```

### `to_dict(count=False, **kwargs)`

Serialize the search into the dictionary that will be sent over as the request’s body.

### `Parameters:`

-
count (bool) – a flag to specify if we are interested in a body for count - no aggregations, no pagination bounds etc.

-
count

-
kwargs (Any)

### `Return type:`

Any

All additional keyword arguments will be included into the dictionary.

### `update_from_dict(d)`

Apply options from a serialized body to the current instance. Modifies the object in-place. Used mostly by from_dict.

### `Parameters:`

d (Any)

### `Return type:`

Search


## Source: `api-ref/helpers/update_by_query.html`

## update_by_query

### `class opensearchpy.helpers.update_by_query.UpdateByQuery(**kwargs)`

Bases: Request

Update by query request to opensearch.

### `Parameters:`

-
using – OpenSearch instance to use

-
index – limit the search to index

-
doc_type – only query this type.

-
kwargs (Any)

All the parameters supplied (or omitted) at creation type can be later overridden by methods (using, index and doc_type respectively).

### `_clone()`

Return a clone of the current search request. Performs a shallow copy of all the underlying objects. Used internally by most state modifying APIs.

### `Return type:`

Any

### `execute()`

Execute the search and return an instance of Response wrapping all the data.

### `Return type:`

Any

### `classmethod from_dict(d)`

Construct a new UpdateByQuery instance from a raw dict containing the search body. Useful when migrating from raw dictionaries.

Example:

```python
ubq = UpdateByQuery.from_dict({
    "query": {
        "bool": {
            "must": [...]
        }
    },
    "script": {...}
})
ubq = ubq.filter('term', published=True)
```

### `Parameters:`

d (Any)

### `Return type:`

Any

### `response_class(cls)`

Override the default wrapper used for the response.

### `Parameters:`

cls (Any)

### `Return type:`

Any

### `script(**kwargs)`

Define update action to take:

Note: the API only accepts a single script, so calling the script multiple times will overwrite.

Example:

```python
ubq = Search()
ubq = ubq.script(source="ctx._source.likes++"")
ubq = ubq.script(source="ctx._source.likes += params.f"",
             lang="expression",
             params={'f': 3})
```

### `Parameters:`

kwargs (Any)

### `Return type:`

Any

### `to_dict(**kwargs)`

Serialize the search into the dictionary that will be sent over as the request’ubq body.

All additional keyword arguments will be included into the dictionary.

### `Parameters:`

kwargs (Any)

### `Return type:`

Any

### `update_from_dict(d)`

Apply options from a serialized body to the current instance. Modifies the object in-place. Used mostly by from_dict.

### `Parameters:`

d (Any)

### `Return type:`

UpdateByQuery


## Source: `api-ref/helpers/wrappers.html`

## wrappers

### `class opensearchpy.helpers.wrappers.Range(*args, **kwargs)`

Bases: AttrDict

### `Parameters:`

-
args (Any)

-
kwargs (Any)

### `__repr__()`

Return repr(self).

### `Return type:`

str
