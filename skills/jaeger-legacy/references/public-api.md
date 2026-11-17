# Public API of Jaeger Java Client 0.32.x

This catalogue covers public methods used directly by application code,
instrumentation, configuration, and tests. Methods in `internal` packages that
are not listed here are not stable APIs and should not be used merely because
they are public in bytecode. `Tracer`, `Span`, `Scope`, and `SpanBuilder` come
from OpenTracing and are the primary interfaces for working with a tracer.

## `io.jaegertracing.Configuration`

### Creating and building a tracer

| Method | Purpose |
|---|---|
| `Configuration(String serviceName)` | Creates configuration for a service name. An empty or `null` name throws `IllegalArgumentException`. |
| `static Configuration fromEnv()` | Reads the service name and other settings from system properties and environment variables. System properties take precedence. |
| `static Configuration fromEnv(String serviceName)` | Same as above, but accepts the service name explicitly. |
| `getTracerBuilder()` | Creates a builder with the current reporter, sampler, codecs, and metrics. Use it before `build()` or for further customization. |
| `getTracer()` | Lazily creates and caches one `JaegerTracer`. Later calls return the same instance. |
| `closeTracer()` | Closes the cached tracer, reporter, and sampler. Call during controlled application shutdown. |
| `withServiceName(String)` | Changes the service name and returns the same configuration. |
| `withReporter(ReporterConfiguration)` | Sets reporter configuration. |
| `withSampler(SamplerConfiguration)` | Sets sampler configuration. |
| `withCodec(CodecConfiguration)` | Sets propagation configuration. |
| `withMetricsFactory(MetricsFactory)` | Sets the metrics factory. |
| `withTraceId128Bit(boolean)` | Enables or disables 128-bit trace IDs. The default is 64-bit IDs. |
| `withTracerTags(Map<String,String>)` | Adds tracer tags to every reported span. |
| `getServiceName()` | Returns the service name. |
| `getReporter()` | Returns reporter configuration if it was set. |
| `getSampler()` | Returns sampler configuration if it was set. |
| `getCodec()` | Returns codec configuration if it was set. |
| `getMetricsFactory()` | Returns the metrics factory. |
| `getTracerTags()` | Returns an unmodifiable tracer-tag map or `null`. |

### `Configuration.SamplerConfiguration`

| Method | Purpose |
|---|---|
| `SamplerConfiguration()` | Creates sampler configuration. |
| `static fromEnv()` | Reads the sampler type, parameter, and manager address from the environment. |
| `withType(String)` | Sets `remote`, `const`, `probabilistic`, or `ratelimiting`. |
| `withParam(Number)` | Sets the sampler parameter: a 0/1 decision, probability, or per-second limit. |
| `withManagerHostPort(String)` | Sets the remote sampling manager `host:port`. |
| `getType()`, `getParam()`, `getManagerHostPort()` | Read the current configuration values. |

### `Configuration.CodecConfiguration`

| Method | Purpose |
|---|---|
| `CodecConfiguration()` | Creates empty propagation configuration. |
| `static fromEnv()` | Reads `JAEGER_PROPAGATION`. |
| `static fromString(String)` | Parses a comma-separated list of `jaeger` and `b3`; unknown values are logged as errors. |
| `withPropagation(Configuration.Propagation)` | Registers Jaeger or B3 for `HTTP_HEADERS` and `TEXT_MAP`. |
| `withCodec(Format<?>, Codec<TextMap>)` | Adds a custom codec for a format. |
| `getCodecs()` | Returns an unmodifiable map of formats and codecs. |

### `Configuration.ReporterConfiguration`

| Method | Purpose |
|---|---|
| `ReporterConfiguration()` | Creates reporter configuration. |
| `static fromEnv()` | Reads reporter and sender settings from the environment. |
| `withLogSpans(Boolean)` | Enables additional logging of finished spans. |
| `withFlushInterval(Integer)` | Sets the queue flush interval in milliseconds. |
| `withMaxQueueSize(Integer)` | Sets the maximum queue size. |
| `withSender(SenderConfiguration)` | Sets sender configuration. |
| `getLogSpans()`, `getFlushIntervalMs()`, `getMaxQueueSize()` | Read reporter settings. |
| `getSenderConfiguration()` | Returns sender configuration. |

### `Configuration.SenderConfiguration`

| Method | Purpose |
|---|---|
| `SenderConfiguration()` | Creates sender configuration. |
| `static fromEnv()` | Reads agent host/port, collector endpoint, and authentication settings. |
| `withAgentHost(String)`, `withAgentPort(Integer)` | Set the UDP agent address. |
| `withEndpoint(String)` | Sets the HTTP collector endpoint. |
| `withAuthToken(String)` | Sets the Bearer token. |
| `withAuthUsername(String)`, `withAuthPassword(String)` | Set Basic Auth credentials. |
| `getSender()` | Returns a custom sender or lazily resolves one from the configuration. |
| `getSender()`, `getAgentHost()`, `getAgentPort()`, `getEndpoint()`, `getAuthToken()`, `getAuthUsername()`, `getAuthPassword()` | Read sender and sender settings. |

## `io.jaegertracing.internal.JaegerTracer`

This is the concrete `Tracer` implementation. Prefer the
`io.opentracing.Tracer` type in application code, but the following methods
are public and useful for diagnostics:

| Method | Purpose |
|---|---|
| `scopeManager()` | Returns the active-scope manager. |
| `activeSpan()` | Returns the active span for the current thread or `null`. |
| `buildSpan(String)` | Starts configuring a new span. |
| `inject(SpanContext, Format<C>, C)` | Writes span context to a carrier, such as HTTP headers. |
| `extract(Format<C>, C)` | Reads context from a carrier; an unsupported format may throw an exception. |
| `close()` | Closes the reporter and sampler; call once during shutdown. |
| `getVersion()` | Returns the client version in `Java-x.y.z` format. |
| `getServiceName()` | Returns the service name. |
| `tags()` | Returns tracer tags. |
| `getMetrics()` | Returns the internal metrics object. |
| `getIpv4()` | Returns the numeric IPv4 representation used by the client. |
| `isUseTraceId128Bit()` | Reports whether the tracer uses 128-bit trace IDs. |

## `JaegerTracer.Builder`

The builder is available through `new JaegerTracer.Builder(serviceName)` or
`Configuration#getTracerBuilder()`.

| Method | Purpose |
|---|---|
| `Builder(String)` | Creates a builder and registers default `TEXT_MAP` and `HTTP_HEADERS` codecs. |
| `withReporter(Reporter)` | Sets the reporter for finished spans. |
| `withSampler(Sampler)` | Sets the sampler. |
| `registerInjector(Format<T>, Injector<T>)` | Registers context injection behavior. |
| `registerExtractor(Format<T>, Extractor<T>)` | Registers context extraction behavior. |
| `withMetricsFactory(MetricsFactory)` | Sets the metrics factory. |
| `withMetrics(Metrics)` | Sets an existing metrics object. |
| `withScopeManager(ScopeManager)` | Sets the scope manager, for example for a custom threading model. |
| `withClock(Clock)` | Sets the clock; mainly useful in tests. |
| `withZipkinSharedRpcSpan()` | Enables compatibility with the Zipkin shared RPC span model. |
| `withExpandExceptionLogs()` | Enables expanded exception logging. |
| `withTraceId128Bit()` | Enables 128-bit trace IDs. |
| `withTag(String,String)`, `withTag(String,boolean)`, `withTag(String,Number)` | Add a tracer tag. |
| `withTags(Map<String,String>)` | Adds multiple tracer tags. |
| `withBaggageRestrictionManager(BaggageRestrictionManager)` | Sets the allowed-baggage-key controller. |
| `build()` | Builds the tracer and creates default reporter/sampler instances when not configured. |
| `static checkValidServiceName(String)` | Validates a service name and throws `IllegalArgumentException` when it is empty. |

## `Tracer` and `Tracer.SpanBuilder`

| Method | Purpose |
|---|---|
| `scopeManager()` | Returns the active-scope manager. |
| `activeSpan()` | Returns the active span or `null`. |
| `buildSpan(String)` | Creates a span builder with an operation name. |
| `inject(...)` | Propagates `SpanContext` into a carrier. In 0.32.x, support `TextMap` and `HTTP_HEADERS`. |
| `extract(...)` | Reads `SpanContext` from a carrier. |
| `asChildOf(SpanContext)` | Sets the context as a `CHILD_OF` reference. |
| `asChildOf(Span)` | Sets the span's context as the parent. |
| `addReference(String, SpanContext)` | Adds `CHILD_OF` or `FOLLOWS_FROM`; Jaeger ignores other types. |
| `ignoreActiveSpan()` | Disables automatic use of the active span as parent. |
| `withTag(...)` | Adds a tag to the span being created. Overloads accept `String`, `boolean`, and `Number`. |
| `withStartTimestamp(long)` | Sets the start time in microseconds since the epoch. |
| `start()` | Creates a span without activating it. |
| `startActive(boolean)` | Creates and activates a span; the parameter controls whether `Scope.close()` finishes it. |
| `startManual()` | Deprecated alias for `start()`. Do not use in new code. |

## `Span`

| Method | Purpose |
|---|---|
| `context()` | Returns context propagated to descendant services; works after `finish()` as well. |
| `setTag(String,String)`, `setTag(String,boolean)`, `setTag(String,Number)` | Set a span tag and return the span for chaining. |
| `log(Map<String,?>)` | Records an event with fields at the current time. |
| `log(long, Map<String,?>)` | Records an event with an explicit timestamp in microseconds. |
| `log(String)` | Records a text event. |
| `log(long,String)` | Records a text event with an explicit timestamp. |
| `setBaggageItem(String,String)` | Sets baggage propagated to descendants. In Jaeger, `null` removes the value. |
| `getBaggageItem(String)` | Reads baggage or returns `null`. |
| `setOperationName(String)` | Changes the operation name. |
| `finish()` | Finishes the span at the current time and passes it to the reporter. |
| `finish(long)` | Finishes the span at an explicit time in microseconds. |

For errors, use `Tags.ERROR` and `Fields.ERROR_OBJECT`, or an `event` field in
`log`. Do not modify a span after `finish()`.

## `Scope`, `ScopeManager`, and `SpanContext`

| Type and method | Purpose |
|---|---|
| `Scope.close()` | Ends the active scope and restores the previous scope. |
| `Scope.span()` | Returns the span associated with the scope. |
| `ScopeManager.activate(Span, boolean)` | Activates a span and returns a scope; the parameter controls automatic `finish()`. |
| `ScopeManager.active()` | Returns the active scope or `null`. |
| `SpanContext.baggageItems()` | Returns all propagated baggage entries. |

## `JaegerSpanContext`

Use these methods only when code genuinely depends on Jaeger implementation
details; general code should use `SpanContext`.

| Method | Purpose |
|---|---|
| `JaegerSpanContext(long,long,long,long,byte)` | Creates context from high/low trace IDs, span ID, parent ID, and flags. |
| `getTraceId()` | Returns the trace ID as hexadecimal text. |
| `getTraceIdHigh()`, `getTraceIdLow()` | Return parts of a 128-bit trace ID. |
| `getSpanId()` | Returns the span ID. |
| `getParentId()` | Returns the parent ID. |
| `getFlags()` | Returns context flags. |
| `isSampled()` | Reports whether the trace is sampled. |
| `isDebug()` | Reports whether debug mode forced sampling. |
| `getBaggageItem(String)` | Reads baggage. |
| `withBaggageItem(String,String)` | Creates a new context with baggage added or removed. |
| `withBaggage(Map<String,String>)` | Creates a new context with the supplied baggage map. |
| `withFlags(byte)` | Creates a new context with the supplied flags. |
| `baggageItems()` | Returns a copy of baggage entries. |
| `toString()` | Returns the context in text propagation format. |

## SPI for extensions and tests

| Type and method | Purpose |
|---|---|
| `Reporter.report(JaegerSpan)` | Receives a finished span. |
| `Reporter.close()` | Releases reporter resources and flushes when supported by the implementation. |
| `Sampler.sample(String,long)` | Decides whether a new trace should be stored; returns `SamplingStatus`. |
| `Sampler.close()` | Releases sampler resources. |
| `Sender.append(JaegerSpan)` | Adds a span to the sender buffer and returns the implementation result. |
| `Sender.flush()` | Sends the buffer and returns the implementation result. |
| `Sender.close()` | Closes the sender and returns the implementation result. |

`Reporter`, `Sampler`, and `Sender` accept `JaegerSpan`, so they are
Jaeger-specific extension points rather than portable OpenTracing APIs.

## Built-in implementations useful in tests

| Type and method | Purpose |
|---|---|
| `new ConstSampler(boolean)` | Always samples or never samples. |
| `ConstSampler.sample(String,long)` | Returns the constant sampling decision. Operation name and ID do not change the result. |
| `ConstSampler.close()` | Does nothing; call through the `Sampler` interface during teardown. |
| `new ProbabilisticSampler(double)` | Creates a sampler with probability from `0.0` to `1.0`. Values outside the range throw `IllegalArgumentException`. |
| `ProbabilisticSampler.getSamplingRate()` | Returns the configured probability. |
| `ProbabilisticSampler.sample(String,long)` | Makes a deterministic decision based on the trace ID. |
| `ProbabilisticSampler.close()` | Releases resources; this implementation has none. |
| `new RateLimitingSampler(double)` | Limits sampled traces per second. |
| `RateLimitingSampler.getMaxTracesPerSecond()` | Returns the configured limit. |
| `RateLimitingSampler.sample(String,long)` | Checks available rate-limiter credit. |
| `RateLimitingSampler.close()` | Closes the sampler; this implementation has no additional resources. |
| `new InMemoryReporter()` | Creates a reporter that stores finished spans in memory. |
| `InMemoryReporter.report(JaegerSpan)` | Adds a finished span to the collection. |
| `InMemoryReporter.getSpans()` | Returns collected spans for test assertions. |
| `InMemoryReporter.clear()` | Removes collected spans. |
| `InMemoryReporter.close()` | Closes the reporter; it sends nothing. |
| `SamplingStatus.isSampled()` | Reads the sampler decision. |
| `SamplingStatus.getTags()` | Reads tags describing the sampler decision. |

`InMemoryReporter.getSpans()` returns the implementation's internal list. Do
not modify it directly; use `clear()` to reset the reporter.
