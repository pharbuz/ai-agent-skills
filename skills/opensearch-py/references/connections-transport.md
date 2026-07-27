# Connections Transport

> Local snapshot generated from OpenSearch Python Client API Reference on 2026-07-27. Use this file instead of browsing the live documentation during skill execution.


## Source: `api-ref/connection.html`

## Connection Types

### `class opensearchpy.Connection(host='localhost', port=None, use_ssl=False, url_prefix='', timeout=10, headers=None, http_compress=None, opaque_id=None, **kwargs)`

Bases: object

Class responsible for maintaining a connection to an OpenSearch node. It holds persistent connection pool to it and its main interface (perform_request) is thread-safe.

Also responsible for logging.

### `Parameters:`

-
host (str) – hostname of the node (default: localhost)

-
port (int | None) – port to use (integer, default: 9200)

-
use_ssl (bool) – use ssl for the connection if True

-
url_prefix (str) – optional url prefix for opensearch

-
timeout (int) – default timeout in seconds (float, default: 10)

-
http_compress (bool | None) – Use gzip compression

-
opaque_id (str | None) – Send this value in the ‘X-Opaque-Id’ HTTP header For tracing all requests made by this transport.

-
host

-
port

-
use_ssl

-
url_prefix

-
timeout

-
headers (Dict[str, str] | None)

-
http_compress

-
opaque_id

-
kwargs (Any)

### `__eq__(other)`

Return self==value.

### `Parameters:`

other (object)

### `Return type:`

bool

### `__hash__()`

Return hash(self).

### `Return type:`

int

### `__lt__(other)`

Return self<value.

### `Parameters:`

other (object)

### `Return type:`

bool

### `__repr__()`

Return repr(self).

### `Return type:`

str

### `_raise_error(status_code, raw_data, content_type=None)`

Locate appropriate exception and raise it.

### `Parameters:`

-
status_code (int)

-
raw_data (str | bytes)

-
content_type (str | None)

### `Return type:`

None

### `_raise_warnings(warning_headers)`

If ‘headers’ contains a ‘Warning’ header raise the warnings to be seen by the user. Takes an iterable of string values from any number of ‘Warning’ headers.

### `Parameters:`

warning_headers (Any)

### `Return type:`

None

### `staticdefault_ca_certs()`

Get the default CA certificate bundle, preferring those configured in the standard OpenSSL environment variables before those provided by certifi (if available)

### `Return type:`

str | None

### `log_request_fail(method, full_url, path, body, duration, status_code=None, response=None, exception=None)`

Log an unsuccessful API call.

### `Parameters:`

-
method (str)

-
full_url (str)

-
path (str)

-
body (Any)

-
duration (float)

-
status_code (int | None)

-
response (str | None)

-
exception (Exception | None)

### `Return type:`

None

### `log_request_success(method, full_url, path, body, status_code, response, duration)`

Log a successful API call.

### `Parameters:`

-
method (str)

-
full_url (str)

-
path (str)

-
body (Any)

-
status_code (int)

-
response (str)

-
duration (float)

### `Return type:`

None

### `class opensearchpy.RequestsHttpConnection(host='localhost', port=None, http_auth=None, use_ssl=False, verify_certs=True, ssl_show_warn=True, ca_certs=None, client_cert=None, client_key=None, headers=None, http_compress=None, opaque_id=None, pool_maxsize=None, metrics=<opensearchpy.metrics.metrics_none.MetricsNone object>, proxies=None, **kwargs)`

Bases: Connection

Connection using the requests library.

### `Parameters:`

-
http_auth (Any) – optional http auth information as either ‘:’ separated string or a tuple. Any value will be passed into requests as auth.

-
use_ssl (bool) – use ssl for the connection if True

-
verify_certs (bool) – whether to verify SSL certificates

-
ssl_show_warn (bool) – show warning when verify certs is disabled

-
ca_certs (Any) – optional path to CA bundle. Defaults to configured OpenSSL bundles from environment variables and then certifi before falling back to the standard requests bundle to improve consistency with other Connection implementations

-
client_cert (Any) – path to the file containing the private key and the certificate, or cert only if using client_key

-
client_key (Any) – path to the file containing the private key if using separate cert and key files (client_cert will contain only the cert)

-
headers (Any) – any custom http headers to be add to requests

-
http_compress (Any) – Use gzip compression

-
opaque_id (Any) – Send this value in the ‘X-Opaque-Id’ HTTP header For tracing all requests made by this transport.

-
pool_maxsize (Any) – Maximum connection pool size used by pool-manager For custom connection-pooling on current session

-
metrics (Metrics) – metrics is an instance of a subclass of the Metrics class, used for collecting and reporting metrics related to the client’s operations;

-
proxies (MutableMapping[str, str] | None) – optional dictionary mapping protocol to the URL of the proxy.

-
host (str)

-
port (int | None)

-
http_auth

-
use_ssl

-
verify_certs

-
ssl_show_warn

-
ca_certs

-
client_cert

-
client_key

-
headers

-
http_compress

-
opaque_id

-
pool_maxsize

-
metrics

-
proxies

-
kwargs (Any)

### `close()`

Explicitly closes connections

### `Return type:`

None

### `class opensearchpy.Urllib3HttpConnection(host='localhost', port=None, http_auth=None, use_ssl=False, verify_certs=<object object>, ssl_show_warn=<object object>, ca_certs=None, client_cert=None, client_key=None, ssl_version=None, ssl_assert_hostname=None, ssl_assert_fingerprint=None, pool_maxsize=None, headers=None, ssl_context=None, http_compress=None, opaque_id=None, metrics=<opensearchpy.metrics.metrics_none.MetricsNone object>, **kwargs)`

Bases: Connection

Default connection class using the urllib3 library and the http protocol.

### `Parameters:`

-
host (str) – hostname of the node (default: localhost)

-
port (int | None) – port to use (integer, default: 9200)

-
url_prefix – optional url prefix for opensearch

-
timeout – default timeout in seconds (float, default: 10)

-
http_auth (Any) – optional http auth information as either ‘:’ separated string or a tuple

-
use_ssl (bool) – use ssl for the connection if True

-
verify_certs (Any) – whether to verify SSL certificates

-
ssl_show_warn (Any) – show warning when verify certs is disabled

-
ca_certs (Any) – optional path to CA bundle. See https://urllib3.readthedocs.io/en/latest/security.html#using-certifi-with-urllib3 for instructions how to get default set

-
client_cert (Any) – path to the file containing the private key and the certificate, or cert only if using client_key

-
client_key (Any) – path to the file containing the private key if using separate cert and key files (client_cert will contain only the cert)

-
ssl_version (Any) – version of the SSL protocol to use. Choices are: SSLv23 (default) SSLv2 SSLv3 TLSv1 (see PROTOCOL_* constants in the ssl module for exact options for your environment).

-
ssl_assert_hostname (Any) – use hostname verification if not False

-
ssl_assert_fingerprint (Any) – verify the supplied certificate fingerprint if not None

-
pool_maxsize (Any) – the number of connections which will be kept open to this host. See https://urllib3.readthedocs.io/en/1.4/pools.html#api for more information.

-
headers (Any) – any custom http headers to be add to requests

-
http_compress (Any) – Use gzip compression

-
opaque_id (Any) – Send this value in the ‘X-Opaque-Id’ HTTP header For tracing all requests made by this transport.

-
metrics (Metrics) – metrics is an instance of a subclass of the Metrics class, used for collecting and reporting metrics related to the client’s operations;

-
host

-
port

-
http_auth

-
use_ssl

-
verify_certs

-
ssl_show_warn

-
ca_certs

-
client_cert

-
client_key

-
ssl_version

-
ssl_assert_hostname

-
ssl_assert_fingerprint

-
pool_maxsize

-
headers

-
ssl_context (Any)

-
http_compress

-
opaque_id

-
metrics

-
kwargs (Any)

### `close()`

Explicitly closes connection

### `Return type:`

None

### `class opensearchpy.AIOHttpConnection(host='localhost', port=None, url_prefix='', timeout=10, http_auth=None, use_ssl=False, verify_certs=<object object>, ssl_show_warn=<object object>, ca_certs=None, client_cert=None, client_key=None, ssl_version=None, ssl_assert_hostname=True, ssl_assert_fingerprint=None, maxsize=10, headers=None, ssl_context=None, http_compress=None, opaque_id=None, loop=None, trust_env=False, **kwargs)`

Bases: AsyncConnection

Default connection class for AsyncOpenSearch using the aiohttp library and the http protocol.

### `Parameters:`

-
host (str) – hostname of the node (default: localhost)

-
port (int | None) – port to use (integer, default: 9200)

-
url_prefix (str) – optional url prefix for opensearch

-
timeout (int) – default timeout in seconds (float, default: 10)

-
http_auth (Any) – optional http auth information as either ‘:’ separated string or a tuple

-
use_ssl (bool) – use ssl for the connection if True

-
verify_certs (Any) – whether to verify SSL certificates

-
ssl_show_warn (Any) – show warning when verify certs is disabled

-
ca_certs (Any) – optional path to CA bundle. See https://urllib3.readthedocs.io/en/latest/security.html#using-certifi-with-urllib3 for instructions how to get default set

-
client_cert (Any) – path to the file containing the private key and the certificate, or cert only if using client_key

-
client_key (Any) – path to the file containing the private key if using separate cert and key files (client_cert will contain only the cert)

-
ssl_version (Any) – version of the SSL protocol to use. Choices are: SSLv23 (default) SSLv2 SSLv3 TLSv1 (see PROTOCOL_* constants in the ssl module for exact options for your environment).

-
ssl_assert_hostname (bool) – use hostname verification if not False

-
ssl_assert_fingerprint (str | None) – verify the supplied certificate fingerprint if not None

-
maxsize (int | None) – the number of connections which will be kept open to this host. See https://urllib3.readthedocs.io/en/1.4/pools.html#api for more information.

-
headers (Any) – any custom http headers to be add to requests

-
http_compress (bool | None) – Use gzip compression

-
opaque_id (str | None) – Send this value in the ‘X-Opaque-Id’ HTTP header For tracing all requests made by this transport.

-
loop (Any) – asyncio Event Loop to use with aiohttp. This is set by default to the currently running loop.

-
host

-
port

-
url_prefix

-
timeout

-
http_auth

-
use_ssl

-
verify_certs

-
ssl_show_warn

-
ca_certs

-
client_cert

-
client_key

-
ssl_version

-
ssl_assert_hostname

-
ssl_assert_fingerprint

-
maxsize

-
headers

-
ssl_context (Any)

-
http_compress

-
opaque_id

-
loop

-
trust_env (bool | None)

-
kwargs (Any)

### `async_create_aiohttp_session()`

Creates an aiohttp.ClientSession(). This is delayed until the first call to perform_request() so that AsyncTransport has a chance to set AIOHttpConnection.loop

### `Return type:`

Any

### `asyncclose()`

Explicitly closes connection

### `Return type:`

Any

### `opensearchpy.connections`

alias of <module ‘opensearchpy.connection.connections’ from ‘/home/runner/work/opensearch-py/opensearch-py/.nox/docs/lib/python3.10/site-packages/opensearchpy/connection/connections.py’>


## Source: `api-ref/connection_pool.html`

## connection_pool

### `class opensearchpy.ConnectionPool(connections, dead_timeout=60, timeout_cutoff=5, selector_class=<class 'opensearchpy.connection_pool.RoundRobinSelector'>, randomize_hosts=True, **kwargs)`

Bases: object

Container holding the Connection instances, managing the selection process (via a ConnectionSelector) and dead connections.

It’s only interactions are with the Transport class that drives all the actions within ConnectionPool.

Initially connections are stored on the class as a list and, along with the connection options, get passed to the ConnectionSelector instance for future reference.

Upon each request the Transport will ask for a Connection via the get_connection method. If the connection fails (its perform_request raises a ConnectionError) it will be marked as dead (via mark_dead) and put on a timeout (if it fails N times in a row the timeout is exponentially longer - the formula is default_timeout * 2 ** (fail_count - 1)). When the timeout is over the connection will be resurrected and returned to the live pool. A connection that has been previously marked as dead and succeeds will be marked as live (its fail count will be deleted).

### `Parameters:`

-
connections (Any) – list of tuples containing the Connection instance and its options

-
dead_timeout (float) – number of seconds a connection should be retired for after a failure, increases on consecutive failures

-
timeout_cutoff (int) – number of consecutive failures after which the timeout doesn’t increase

-
selector_class (Type[ConnectionSelector]) – ConnectionSelector subclass to use if more than one connection is live

-
randomize_hosts (bool) – shuffle the list of connections upon arrival to avoid dog piling effect across processes

-
connections

-
dead_timeout

-
timeout_cutoff

-
selector_class

-
randomize_hosts

-
kwargs (Any)

### `__repr__()`

Return repr(self).

### `Return type:`

str

### `close()`

Explicitly closes connections

### `Return type:`

Any

### `get_connection()`

Return a connection from the pool using the ConnectionSelector instance.

It tries to resurrect eligible connections, forces a resurrection when no connections are available and passes the list of live connections to the selector instance to choose from.

Returns a connection instance and its current fail count.

### `Return type:`

Any

### `mark_dead(connection, now=None)`

Mark the connection as dead (failed). Remove it from the live pool and put it on a timeout.

### `Parameters:`

-
connection (Any) – the failed instance

-
connection

-
now (float | None)

### `Return type:`

None

### `mark_live(connection)`

Mark connection as healthy after a resurrection. Resets the fail counter for the connection.

### `Parameters:`

-
connection (Any) – the connection to redeem

-
connection

### `Return type:`

None

### `resurrect(force=False)`

Attempt to resurrect a connection from the dead pool. It will try to locate one (not all) eligible (its timeout is over) connection to return to the live pool. Any resurrected connection is also returned.

### `Parameters:`

-
force (bool) – resurrect a connection even if there is none eligible (used when we have no live connections). If force is specified resurrect always returns a connection.

-
force

### `Return type:`

Any

### `class opensearchpy.ConnectionSelector(opts)`

Bases: object

Simple class used to select a connection from a list of currently live connection instances. In init time it is passed a dictionary containing all the connections’ options which it can then use during the selection process. When the select method is called it is given a list of currently live connections to choose from.

The options dictionary is the one that has been passed to Transport as hosts param and the same that is used to construct the Connection object itself. When the Connection was created from information retrieved from the cluster via the sniffing process it will be the dictionary returned by the host_info_callback.

Example of where this would be useful is a zone-aware selector that would only select connections from its own zones and only fall back to other connections where there would be none in its zones.

### `Parameters:`

-
opts (Sequence[Tuple[Connection, Any]]) – dictionary of connection instances and their options

-
opts

### `select(connections)`

Select a connection from the given list.

### `Parameters:`

-
connections (Sequence[Connection]) – list of live connections to choose from

-
connections

### `Return type:`

None

### `class opensearchpy.RoundRobinSelector(opts)`

Bases: ConnectionSelector

Selector using round-robin.

### `Parameters:`

-
opts (Sequence[Tuple[Connection, Any]]) – dictionary of connection instances and their options

-
opts

### `select(connections)`

Select a connection from the given list.

### `Parameters:`

-
connections (Sequence[Connection]) – list of live connections to choose from

-
connections

### `Return type:`

Any


## Source: `api-ref/serializer.html`

## serializer

### `class opensearchpy.JSONSerializer`

Bases: Serializer


## Source: `api-ref/transport.html`

## transport

### `class opensearchpy.Transport(hosts, connection_class=None, connection_pool_class=<class 'opensearchpy.connection_pool.ConnectionPool'>, host_info_callback=<function get_host_info>, sniff_on_start=False, sniffer_timeout=None, sniff_timeout=0.1, sniff_on_connection_fail=False, serializer=<opensearchpy.serializer.JSONSerializer object>, serializers=None, default_mimetype='application/json', max_retries=3, pool_maxsize=None, retry_on_status=(502, 503, 504), retry_on_timeout=False, send_get_body_as='GET', metrics=<opensearchpy.metrics.metrics_none.MetricsNone object>, **kwargs)`

Bases: object

Encapsulation of transport-related to logic. Handles instantiation of the individual connections as well as creating a connection pool to hold them.

Main interface is the perform_request method.

### `Parameters:`

-
hosts (Any) – list of dictionaries, each containing keyword arguments to create a connection_class instance

-
connection_class (Type[Connection]) – subclass of Connection to use

-
connection_pool_class (Any) – subclass of ConnectionPool to use

-
host_info_callback (Any) – callback responsible for taking the node information from /_cluster/nodes, along with already extracted information, and producing a list of arguments (same as hosts parameter)

-
sniff_on_start (bool) – flag indicating whether to obtain a list of nodes from the cluster at startup time

-
sniffer_timeout (float | None) – number of seconds between automatic sniffs

-
sniff_on_connection_fail (bool) – flag controlling if connection failure triggers a sniff

-
sniff_timeout (float | None) – timeout used for the sniff request - it should be a fast api call and we are talking potentially to more nodes so we want to fail quickly. Not used during initial sniffing (if sniff_on_start is on) when the connection still isn’t initialized.

-
serializer (Serializer) – serializer instance

-
serializers (Mapping[str, Serializer] | None) – optional dict of serializer instances that will be used for deserializing data coming from the server. (key is the mimetype)

-
default_mimetype (str) – when no mimetype is specified by the server response assume this mimetype, defaults to ‘application/json’

-
max_retries (int) – maximum number of retries before an exception is propagated

-
retry_on_status (Collection[int]) – set of HTTP status codes on which we should retry on a different node. defaults to (502,503,504)

-
retry_on_timeout (bool) – should timeout trigger a retry on different node? (default False)

-
send_get_body_as (str) – for GET requests with body this option allows you to specify an alternate way of execution for environments that don’t support passing bodies with GET requests. If you set this to ‘POST’ a POST method will be used instead, if to ‘source’ then the body will be serialized and passed as a query parameter source.

-
pool_maxsize (int | None) – Maximum connection pool size used by pool-manager For custom connection-pooling on current session

-
metrics (Metrics) – metrics is an instance of a subclass of the Metrics class, used for collecting and reporting metrics related to the client’s operations;

-
hosts

-
connection_class

-
connection_pool_class

-
host_info_callback

-
sniff_on_start

-
sniffer_timeout

-
sniff_timeout

-
sniff_on_connection_fail

-
serializer

-
serializers

-
default_mimetype

-
max_retries

-
pool_maxsize

-
retry_on_status

-
retry_on_timeout

-
send_get_body_as

-
metrics

-
kwargs (Any)

Any extra keyword arguments will be passed to the connection_class when creating and instance unless overridden by that connection’s options provided as part of the hosts parameter.

### `DEFAULT_CONNECTION_CLASS`

alias of Urllib3HttpConnection

### `_get_sniff_data(initial=False)`

Perform the request to get sniffing information. Returns a list of dictionaries (one per node) containing all the information from the cluster.

It also sets the last_sniff attribute in case of a successful attempt.

In rare cases it might be possible to override this method in your custom Transport class to serve data from alternative source like configuration management.

### `Parameters:`

initial (bool)

### `Return type:`

Any

### `_resolve_request_args(method, params, body, ignore, timeout)`

Resolves parameters for .perform_request()

### `Parameters:`

-
method (str)

-
params (Any)

-
body (Any)

-
ignore (Collection[int])

-
timeout (int | float | None)

### `Return type:`

Any

### `add_connection(host)`

Create a new Connection instance and add it to the pool.

### `Parameters:`

-
host (Any) – kwargs that will be used to create the instance

-
host

### `Return type:`

None

### `close()`

Explicitly closes connections

### `Return type:`

Any

### `get_connection()`

Retrieve a Connection instance from the ConnectionPool instance.

### `Return type:`

Any

### `mark_dead(connection)`

Mark a connection as dead (failed) in the connection pool. If sniffing on failure is enabled this will initiate the sniffing process.

### `Parameters:`

-
connection (Connection) – instance of Connection that failed

-
connection

### `Return type:`

None

### `perform_request(method, url, params=None, body=None, timeout=None, ignore=(), headers=None)`

Perform the actual request. Retrieve a connection from the connection pool, pass all the information to its perform_request method and return the data.

If an exception was raised, mark the connection as failed and retry (up to max_retries times).

If the operation was successful and the connection used was previously marked as dead, mark it as live, resetting its failure count.

### `Parameters:`

-
method (str) – HTTP method to use

-
url (str) – absolute url (without host) to target

-
headers (Mapping[str, str] | None) – dictionary of headers, will be handed over to the underlying Connection class

-
params (Mapping[str, Any] | None) – dictionary of query parameters, will be handed over to the underlying Connection class for serialization

-
body (Any | None) – body of the request, will be serialized using serializer and passed to the connection

-
timeout (int | float | None) – timeout of the request. If it is not presented as argument will be extracted from params

-
method

-
url

-
params

-
body

-
timeout

-
ignore (Collection[int])

-
headers

### `Return type:`

Any

### `set_connections(hosts)`

Instantiate all the connections and create new connection pool to hold them. Tries to identify unchanged hosts and re-use existing Connection instances.

### `Parameters:`

-
hosts (Any) – same as __init__

-
hosts

### `Return type:`

None

### `sniff_hosts(initial=False)`

Obtain a list of nodes from the cluster and create a new connection pool using the information retrieved.

To extract the node connection parameters use the nodes_to_host_callback.

### `Parameters:`

-
initial (bool) – flag indicating if this is during startup (sniff_on_start), ignore the sniff_timeout if True

-
initial

### `Return type:`

Any


## Source: `api-ref/metrics.html`

## metrics

### `class opensearchpy.Metrics`

Bases: ABC

The Metrics class defines methods and properties for managing request metrics, including start time, end time, and service time, serving as a blueprint for concrete implementations.

### `class opensearchpy.MetricsEvents`

Bases: Metrics

The MetricsEvents class implements the Metrics abstract base class and tracks metrics such as start time, end time, and service time during request processing.

### `class opensearchpy.MetricsNone`

Bases: Metrics

Default metrics class. It sets the start time, end time, and service time to None.


## Source: `api-ref/exceptions.html`

## exceptions

### `class opensearchpy.AuthenticationException`

Bases: TransportError

Exception representing a 401 status code.

### `class opensearchpy.AuthorizationException`

Bases: TransportError

Exception representing a 403 status code.

### `class opensearchpy.ConflictError`

Bases: TransportError

Exception representing a 409 status code.

### `class opensearchpy.ConnectionError`

Bases: TransportError

Error raised when there was an exception while talking to OpenSearch. Original exception from the underlying Connection implementation is available as .info.

### `__str__()`

Return str(self).

### `Return type:`

str

### `class opensearchpy.ConnectionTimeout`

Bases: ConnectionError

A network timeout. Doesn’t cause a node retry by default.

### `__str__()`

Return str(self).

### `Return type:`

str

### `class opensearchpy.ImproperlyConfigured`

Bases: Exception

Exception raised when the config passed to the client is inconsistent or invalid.

### `class opensearchpy.NotFoundError`

Bases: TransportError

Exception representing a 404 status code.

### `opensearchpy.OpenSearchDeprecationWarning`

alias of OpenSearchWarning

### `class opensearchpy.OpenSearchException`

Bases: Exception

Base class for all exceptions raised by this package’s operations (doesn’t apply to ImproperlyConfigured).

### `class opensearchpy.OpenSearchWarning`

Bases: Warning

Warning that is raised when a deprecated option or incorrect usage is flagged via the ‘Warning’ HTTP header.

### `class opensearchpy.RequestError`

Bases: TransportError

Exception representing a 400 status code.

### `class opensearchpy.SerializationError`

Bases: OpenSearchException

Data passed in failed to serialize properly in the Serializer being used.

### `class opensearchpy.SSLError`

Bases: ConnectionError

Error raised when encountering SSL errors.

### `class opensearchpy.TransportError`

Bases: OpenSearchException

Exception raised when OpenSearch returns a non-OK (>=400) HTTP status code. Or when an actual connection error happens; in that case the status_code will be set to 'N/A'.

### `__str__()`

Return str(self).

### `Return type:`

str

### `propertyerror:str`

A string error message.

### `propertyinfo:Dict[str,Any]|Exception|Any`

Dict of returned error info from OpenSearch, where available, underlying exception when not.

### `propertystatus_code:str|int`

The HTTP status code of the response that precipitated the error or 'N/A' if not applicable.

### `class opensearchpy.OpenSearchDslException`

Bases: Exception

Base class for all OpenSearchDsl exceptions

### `class opensearchpy.IllegalOperation`

Bases: OpenSearchDslException

Exception representing IllegalOperation

### `class opensearchpy.UnknownDslObject`

Bases: OpenSearchDslException

Exception representing UnknownDSLObject

### `class opensearchpy.ValidationException`

Bases: ValueError, OpenSearchDslException

Exception representing Validation Error
