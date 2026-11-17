---
name: jaeger-legacy
description: >-
  Build, configure, instrument, test, and troubleshoot legacy Jaeger tracing
  for Java applications using the Jaeger Java Client 0.32.x and OpenTracing.
  Trigger when a project uses io.jaegertracing, jaeger-client, jaeger-core,
  jaeger-thrift, OpenTracing, Jaeger agent/collector, B3 propagation, or needs
  to maintain older Spring Boot tracing integration.
---

# Jaeger Legacy for Java

Use this skill for the pre-OpenTelemetry Jaeger Java client. Treat it as a
maintenance and compatibility integration, not as a recommendation for new
applications. Preserve the project's existing Java and Spring versions unless
the user explicitly requests an upgrade.

## Identify the integration

1. Inspect `pom.xml` or `build.gradle` for `io.jaegertracing` and
   `io.opentracing` dependencies.
2. Confirm the client version, Java runtime, Spring Boot version, and whether
   the application sends through an agent or directly to a collector.
3. Keep all Jaeger artifacts on one compatible version line. Prefer the
   `io.jaegertracing` group; do not reintroduce the deprecated
   `com.uber.jaeger` coordinates.
4. For a normal application, use `jaeger-client`; add only the modules required
   by the existing build. `jaeger-core` alone provides tracing primitives but
   does not provide a transport.

## Minimal dependency shape

For Maven, the usual application dependency is:

```xml
<dependency>
  <groupId>io.jaegertracing</groupId>
  <artifactId>jaeger-client</artifactId>
  <version>0.32.0</version>
</dependency>
```

For Spring web applications, add the OpenTracing Spring web starter only when
the project already uses that integration style. Avoid adding multiple
instrumentation starters that create duplicate spans.

## Create one tracer

Prefer environment-driven configuration:

```java
import io.jaegertracing.Configuration;
import io.opentracing.Tracer;

Tracer tracer = Configuration.fromEnv().getTracer();
```

Use the builder when custom codecs, reporters, samplers, tags, or metrics are
needed:

```java
Tracer tracer = new Configuration("orders")
    .getTracerBuilder()
    .build();
```

Register the tracer with the application's global OpenTracing registry only
when the framework expects a global tracer. Otherwise inject one shared tracer
instance. Do not construct a tracer per request. Repeated
`Configuration#getTracer()` calls are expected to return the same tracer.

## Configure transport and authentication

Use exactly one primary transport:

- `JAEGER_ENDPOINT`: send over HTTP to a collector endpoint.
- `JAEGER_AGENT_HOST` and `JAEGER_AGENT_PORT`: send over UDP to a Jaeger
  agent.

When both are set, the endpoint takes precedence and agent settings are
ignored. For an endpoint, configure `JAEGER_AUTH_TOKEN` for Bearer
authentication, or `JAEGER_USER` and `JAEGER_PASSWORD` for Basic
authentication. Do not place credentials in source code or tracer tags.

Supported environment settings include:

- `JAEGER_SERVICE_NAME` (required)
- `JAEGER_PROPAGATION` (`jaeger` or `b3`)
- `JAEGER_REPORTER_LOG_SPANS`
- `JAEGER_REPORTER_MAX_QUEUE_SIZE`
- `JAEGER_REPORTER_FLUSH_INTERVAL` in milliseconds
- `JAEGER_SAMPLER_TYPE` (`const`, `probabilistic`, or `ratelimiting`)
- `JAEGER_SAMPLER_PARAM`
- `JAEGER_SAMPLER_MANAGER_HOST_PORT`
- `JAEGER_TAGS` as comma-separated `name=value` pairs

System properties override environment variables. Validate the effective
configuration at startup and log the selected service name and transport,
never secret values.

## Instrument spans and propagation

Use OpenTracing lifecycle semantics:

```java
Span span = tracer.buildSpan("load-order").start();
try (Scope ignored = tracer.scopeManager().activate(span)) {
  span.setTag("order.id", orderId);
  // downstream work
} catch (RuntimeException error) {
  span.log(Collections.singletonMap(Fields.ERROR_OBJECT, error));
  span.setTag(Tags.ERROR, true);
  throw error;
} finally {
  span.finish();
}
```

For incoming requests, extract the context before creating the server span.
For outgoing requests, inject the active context into headers before sending.
Use the standard Jaeger propagation by default. Register B3 codecs when
interoperating with Zipkin-style services and use the same propagation mode
across the call path.

For Spring web applications, let one supported web instrumentation layer create
server/client spans and manually instrument only business boundaries. Verify
that `RestTemplate`, filters, interceptors, and messaging listeners do not
create duplicate spans.

## Sampling and debug traces

- `const`: always sample when parameter is nonzero; never sample at zero.
- `probabilistic`: sample with a parameter from `0.0` to `1.0`.
- `ratelimiting`: sample at the configured traces-per-second rate.
- Use remote sampling only when the sampler manager is reachable.

For tests, use an in-memory reporter and a constant sampler enabled at `1`.
For one production request, set the OpenTracing `sampling.priority` tag to
`1`, or use the Jaeger debug request header when starting a root trace.
Do not enable forced sampling globally in production.

## Verify and troubleshoot

1. Start a compatible Jaeger backend or collector and confirm its ingest
   endpoint/agent port is reachable from the application.
2. Generate a request that creates a root span and at least one child span.
3. Confirm the service name, trace ID continuity, parent/child relationship,
   tags, and error logs in the tracing UI.
4. If no spans arrive, check service name, endpoint-vs-agent precedence,
   UDP reachability, queue/flush settings, sampling, and application shutdown
   flushing.
5. If traces split between services, inspect extraction/injection, header
   forwarding, proxy behavior, and whether both sides use Jaeger or B3 format.
6. If startup fails after adding Thrift, inspect `libthrift` version conflicts;
   use the project's established shaded or dependency-management strategy.

## Testing pattern

Use `InMemoryReporter` with `ConstSampler(true)`, execute the instrumented
operation, flush/close the tracer if the test lifecycle requires it, and assert
on operation name, tags, error logs, and parent context. Keep production
sampling and network senders out of unit tests. Use an integration test for
actual collector delivery and propagation across process boundaries.

## Public API catalogue

For the complete list of externally usable methods and their purposes, read
`references/public-api.md`. Use that catalogue when choosing an API, reviewing
legacy instrumentation, or migrating code. It covers `Configuration`, nested
configuration objects, `JaegerTracer.Builder`, OpenTracing interfaces,
`JaegerSpanContext`, and Jaeger SPI extension points.

