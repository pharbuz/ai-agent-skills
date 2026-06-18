> Source: [https://docs.dynatrace.com/docs/analyze-explore-automate/metrics/dql-examples](https://docs.dynatrace.com/docs/analyze-explore-automate/metrics/dql-examples)

# DQL timeseries examples

Metrics on Grail enable you to pinpoint and retrieve any metric data with the help of [Dynatrace Query Language](/platform/grail/dynatrace-query-language). After reviewing the [fundamentals of DQL queries](/platform/grail/dynatrace-query-language/dql-guide#metrics) and the [timeseries command](/platform/grail/dynatrace-query-language/commands/metric-commands), use the examples on this page to start getting answers from your metrics.

### Example 1: Average CPU usage across all hosts

In this example, you'll query the average CPU usage across all monitored hosts in your environment.

OneAgent collects CPU measurements from its host machine. These metrics are accessible through metric keys beginning with `dt.host.cpu`.

Observing the aggregate CPU usage across all hosts can help you visually confirm how your infrastructure responds to and recovers from usage spikes or slow, imperceptible growth trends over time.

```
timeseries usage=avg(dt.host.cpu.usage)

```

### Example 2: Average CPU usage by host, limit to top 3 hosts

In this example, you get every monitored host's average CPU usage and focus on the three hosts with the highest usage.

OneAgent collects CPU measurements from its host machine. These metrics are accessible through metric keys beginning with `dt.host.cpu`.

Charting individual hosts' CPU usage helps to visualize normal and outlier usage. By focusing on the three hosts with highest CPU usage, you can begin investigating under-provisioned applications. Likewise, focusing on hosts with the lowest CPU usage may reveal over-provisioning and lead to cost-saving opportunities.

1.

2.
- Query the data.
3.

```
timeseries usage = avg(dt.host.cpu.usage), usage_summary = avg(dt.host.cpu.usage, scalar: true), by: {dt.smartscape.host}
| fieldsAdd host_name = getNodeName(dt.smartscape.host)
| sort usage_summary desc
| limit 3

```

1.

2.
- Simplify results.
Tables are easier to scan than line charts when comparing values across hosts. To simplify your results, query only the columns you need—`dt.smartscape.host` and `usage`. This example is similar to the previous one, but drops the time series and keeps only the columns you need.
3.

```
timeseries usage = avg(dt.host.cpu.usage, scalar: true), by: {dt.smartscape.host}
| fieldsAdd host_name = getNodeName(dt.smartscape.host)
| sort usage desc
| limit 3
| fields dt.smartscape.host, host_name, usage

```

### Example 3: Average CPU usage based on host tags

In this example, you'll use an `in` condition to query hosts based on their tags.

By using the `in` operator with `smartscapeNodes`, you can filter on `tags` and other host attributes.

```
timeseries usage=avg(dt.host.cpu.usage), filter:dt.smartscape.host in [smartscapeNodes "HOST"|filter tags ~ "BF"|fields id]

```

### Example 4: Number of hosts sending CPU usage data

In this example, you'll learn how to chain `timeseries` with `summarize`. You'll first query hosts sending CPU usage data, and then count the number of hosts in the result.

Other DQL commands can also be chained with `timeseries` as demonstrated in previous examples, but unlike those examples, `summarize` further aggregates the dataset returned by `timeseries`. You'll find this two-step aggregation helpful as your questions become more complex and nuanced.

```
timeseries usage = avg(dt.host.cpu.usage), by: {dt.smartscape.host}
| summarize count()

```

### Example 5: Top hosts by bytes read with corresponding bytes written

In this example, you'll enrich a single result with context from another metric.

Even when focused on disk read operations, the corresponding disk writes can provide helpful context.

```
timeseries by:{dt.smartscape.host}, {
      bytes_read = sum(dt.host.disk.bytes_read, scalar: true),
      bytes_written = sum(dt.host.disk.bytes_written, scalar: true)
    }
| sort bytes_read desc
| limit 3
| fields
    dt.smartscape.host,
    host_name = getNodeName(dt.smartscape.host),
    bytes_read,
    bytes_written

```

### Example 6: Available CPU by Kubernetes Node

In this example, you'll calculate the available CPU on all nodes of your hypothetical "openfeature" cluster.

To return a timeseries instead of a single value, we use the `[]` operator to take the difference of individual timeseries values. The result is another timeseries that you can visualize with a line chart.

The available CPU is integral for efficient resource utilization and avoiding resource contention. A timeseries visualized with a line chart is one way to show how the available CPU changes over time.

```
timeseries {
      cpu_allocatable = min(dt.kubernetes.node.cpu_allocatable),
      requests_cpu = max(dt.kubernetes.container.requests_cpu)
    },
    by:{dt.smartscape.k8s_cluster, dt.smartscape.k8s_node}
| fieldsAdd
    k8s_cluster_name = getNodeName(dt.smartscape.k8s_cluster),
    k8s_node_name = getNodeName(dt.smartscape.k8s_node)
| fieldsAdd result = cpu_allocatable[] - requests_cpu[]
| fieldsRemove cpu_allocatable, requests_cpu

```

### Example 7: Average host CPU usage by host size

In this example, you'll learn how to use a [`getNodeField` function](/platform/grail/dynatrace-query-language/functions/join-functions#getNodeField) to analyze host CPU usage by host size.

OneAgent collects local context from its host: information such as how many CPUs are installed and how much memory it has. You can add this information to your query with the `getNodeField` function.

Host-level information can sometimes be too fine-grained and difficult to interpret. In these situations, a well-chosen smartscape attribute can help you explore and analyze how individual hosts contribute to broader trends.

```
timeseries usage = avg(dt.host.cpu.usage, scalar: true), by:{dt.smartscape.host}
| fieldsAdd cores = getNodeField(dt.smartscape.host, "cores")
| summarize by:{cores}, avg(usage), count_hosts = count()

```

### Example 8: Query multiple CPU usage metrics with a single query

In this example, you'll learn how to use the [`append` command](/platform/grail/dynatrace-query-language/commands/correlation-and-join-commands#append) to return multiple CPU metrics with a single query.

Combining queries into one command can be useful for comparing measurements from different contexts, as they will be charted together.

As you query many metrics from a single host and perform no arithmetic, the `append` command here is preferred to querying multiple metrics with a single `timeseries` command. The `append` command is a comparatively more flexible option, as it doesn't require equivalent `by` or `filter` arguments, for example. Additionally, chaining `append` is more efficient from a DQL perspective.

```
timeseries idle = avg(dt.host.cpu.idle),
    by:{dt.smartscape.host},
    filter:{dt.smartscape.host == toSmartscapeId("HOST-EFAB6D2FE7274823")}
| append [
      timeseries system = avg(dt.host.cpu.system),
          by:{dt.smartscape.host},
          filter:{dt.smartscape.host == toSmartscapeId("HOST-EFAB6D2FE7274823")}
    ]
| append [
      timeseries user = avg(dt.host.cpu.user),
          by:{dt.smartscape.host},
          filter:{dt.smartscape.host == toSmartscapeId("HOST-EFAB6D2FE7274823")}
    ]

```

### Example 9: Connection failure rate by host

In this example, you'll apply what you've learned from previous examples to calculate the failure rate and find hosts running processes with many failed connections.

This example uses the `default` parameter to control for the case where there are no failures. It inserts a `0` value anywhere data is missing.

Failure rate calculations are common and critical for monitoring service-level objectives. Spotting persistent or recurring high failure rates in testing environments could indicate a deployment problem before the application reaches production.

```
timeseries {
      new = sum(dt.process.network.sessions.new),
      reset = sum(dt.process.network.sessions.reset, default: 0),
      timeout = sum(dt.process.network.sessions.timeout, default: 0)
    },
    by:{dt.smartscape.host}
| fieldsAdd result = 100 * (reset[] + timeout[]) / new[]
| filter arrayAvg(result) > 0
| sort arrayAvg(result) desc

```

### Example 10: Monitoring host availability

In this example you will monitor the availability of hosts and count those that are currently up.

You can use the timeseries command with the [`nonempty` parameter](/platform/grail/dynatrace-query-language/commands/metric-commands#expand--nonempty-parameter--1) to calculate host availability. This parameter ensures that you get a result even when no data match the filter–such as when no hosts are up. This provides a more accurate representation of host availability.

```
timeseries availability = sum(dt.host.availability, default:0),
    nonempty:true,
    filter:{availability.state == "up"}

```

### Example 11: Readiness probe

In this example you'll query [log metrics](/analyze-explore-automate/logs/lma-log-processing/lma-log-metrics) to count successful and failed readiness probes by host.

You can use the [`union` parameter](/platform/grail/dynatrace-query-language/commands/metric-commands#union) to capture all hosts, including those with no failures or no successes.

```
timeseries
    failure_count = sum(log.readiness_probe.failure_count, default: 0),
    success_count = sum(log.readiness_probe.success_count, default: 0),
    by:{dt.smartscape.host},
    union: true

```

The `union:true` argument captures all hosts, even if they had no failures or no successes.

### Example 12: Failure rate

In this example, you will query the per-second failure rate for a specific endpoint ("/api/accounts"). By using the [`rate` parameter](/platform/grail/dynatrace-query-language/commands/metric-commands#rate), you can normalize the timeseries data to a specific duration.

Monitoring request failure rates is crucial for understanding application performance, identifying bottlenecks, and ensuring optimal user experience.

Dynatrace shows the per-minute request count by default, as Dynatrace service metrics collect one-minute granularity request data.

```
timeseries sum(dt.service.request.failure_count, rate:1s),
    filter:{startsWith(endpoint.name, "/api/accounts")}

```

### Example 13: Capacity planning

In this example, you will query current host-disk availability and use the [`shift`](/platform/grail/dynatrace-query-language/commands/metric-commands#shift) parameter to compare it to usage 7 days ago.

Monitoring host-disk availability helps with capacity planning. If today's disk space usage is consistently higher than 7 days ago, it may signal the need for additional storage resources. Conversely, a decrease in usage might allow for resource optimization.

```
timeseries avail = avg(dt.host.disk.avail), by:{dt.smartscape.host}, from:-24h
| append [
    timeseries avail.yesterday = avg(dt.host.disk.avail), by:{dt.smartscape.host}, shift:-168h
  ]
| filter startsWith(getNodeName(dt.smartscape.host), "prod-")

```

### Example 14: Verify host availability and redundance

In this example you'll use the [`count` aggregation](/platform/grail/dynatrace-query-language/commands/metric-commands#timeseries-count) to track the number of hosts monitored in each AZ of AWS region us-east-1.

Applications frequently deploy hosts across multiple availability zones (AZs) to ensure high availability. Counting hosts in each AZ helps verify that the distribution is balanced and, should one AZ experience network disruptions or other issues, the workload can fail over to another AZ.

```
timeseries num_hosts = count(dt.host.cpu.usage),
    by:{aws.availability_zone},
    filter:{startsWith(aws.availability_zone, "us-east-1")}

```

### Example 15: Performance optimization

In this example you'll use the [`percentile` aggregation](/platform/grail/dynatrace-query-language/commands/metric-commands#timeseries-percentile) to track the 90th percentile response time of the contrived /api/accounts endpoint.

Tracking the service response time [percentiles](https://www.dynatrace.com/news/blog/why-averages-suck-and-percentiles-are-great/) helps identify bottlenecks and areas for improvement. If a specific transaction consistently exceeds this threshold, you can decide if it warrants investigation and additional optimization.

```
timeseries p90 = percentile(dt.service.request.response_time, 90),
    filter:{startsWith(endpoint.name, "/api/accounts")}

```

### Example 16: Right-sizing deployments

In this example you'll use the [`if` function](/platform/grail/dynatrace-query-language/functions/conditional-functions#if) to label underused host-disk pairs.

Identifying overprovisioned deployments helps reduce operating costs. By removing overprovisioned infrastructure, you can determine the right size deployment for your application.

```
timeseries avail = avg(dt.host.disk.avail, scalar: true),
    by:{dt.smartscape.disk, dt.smartscape.host},
    filter:{startsWith(getNodeName(dt.smartscape.host), "my-app-")}
| fieldsAdd disk_usage = if(avail > 450000000000, "underused", else: "optimal")
| limit 3

```

### Example 17: Split CPU usage by kubernetes annotations

In this example you'll split CPU usage by kubernetes annotation.

You can use kubernetes annotation `app.kubernetes.io/component` to evaluate the performance of your application components. Annotations are cloud application attributes and aren't typically ingested with a metric. You should split by the cloud application and look up the relevant annotation.

Many [`summarize` command functions](/platform/grail/dynatrace-query-language/commands/aggregation-commands#summarize) accept iterative expressions like `cpu_usage[]` to preserve the timeseries.

```
timeseries cpu_usage = sum(dt.kubernetes.container.cpu_usage, rollup: max),by:{dt.smartscape.k8s_deployment}
| fieldsAdd annotations = getNodeField(dt.smartscape.k8s_deployment, "k8s.annotations")
| fieldsAdd component = annotations[`app.kubernetes.io/component`]
| summarize cpu_usage = sum(cpu_usage[]), by:{timeframe, interval, component}

```
