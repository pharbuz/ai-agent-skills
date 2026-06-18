> Source: [https://docs.dynatrace.com/docs/secure/threat-observability/dql-examples](https://docs.dynatrace.com/docs/secure/threat-observability/dql-examples)

# DQL examples for security data

This page has been updated to align with the new Grail security events table. For the complete list of updates and actions needed to accomplish the migration, follow the steps in the [Grail security table migration guide](/secure/threat-observability/migration).

The examples below illustrate how to slice and dice [security data](/secure/threat-observability/concepts#security-data) and build powerful and flexible security reports with [Dynatrace Query Language (DQL)](/platform/grail/dynatrace-query-language).

## Query Dynatrace events

### Total number of open vulnerabilities

Get the total number of open, non-muted vulnerabilities in your environment.

**Query example**:

```
fetch security.events
| filter dt.system.bucket=="default_securityevents_builtin"
     AND event.provider=="Dynatrace"
     AND event.type=="VULNERABILITY_STATE_REPORT_EVENT"
     AND event.level=="ENTITY"
// filter for the latest snapshot per entity
| dedup {vulnerability.display_id, affected_entity.id}, sort:{timestamp desc}
// filter for open non-muted vulnerabilities
| filter vulnerability.resolution.status=="OPEN"
     AND vulnerability.mute.status!="MUTED"
// count unique vulnerabilities
| summarize {`Open vulnerabilities`=countDistinctExact(vulnerability.display_id)}

```

**Query result**:

### Total number of critical open vulnerabilities

Get the total number of critical open, non-muted vulnerabilities in your environment.

**Query example**:

```
fetch security.events
| filter dt.system.bucket=="default_securityevents_builtin"
     AND event.provider=="Dynatrace"
     AND event.type=="VULNERABILITY_STATE_REPORT_EVENT"
     AND event.level=="ENTITY"
// filter for the latest snapshot per entity
| dedup {vulnerability.display_id, affected_entity.id}, sort:{timestamp desc}
// filter for critical open non-muted vulnerabilities
| filter vulnerability.resolution.status=="OPEN"
     AND vulnerability.mute.status!="MUTED"
     AND vulnerability.risk.level=="CRITICAL"
// count unique vulnerabilities
| summarize {`Critical open vulnerabilities`=countDistinctExact(vulnerability.display_id)}

```

**Query result**:

### Total number of open vulnerabilities in a management zone

Get the total number of open, non-muted vulnerabilities in a specific management zone (in this example, `AppSec: UNGUARD`).

**Query example**:

```
fetch security.events
| filter dt.system.bucket=="default_securityevents_builtin"
     AND event.provider=="Dynatrace"
     AND event.type=="VULNERABILITY_STATE_REPORT_EVENT"
     AND event.level=="ENTITY"
// filter for the latest snapshot per entity
| dedup {vulnerability.display_id, affected_entity.id}, sort:{timestamp desc}
// filter for open non-muted vulnerabilities in a specific management zone
| filter vulnerability.resolution.status == "OPEN"
     AND vulnerability.mute.status != "MUTED"
     AND in("AppSec: Unguard", affected_entity.management_zones.names)
// count unique vulnerabilities
| summarize {`Open vulnerabilities (unguard)`=countDistinctExact(vulnerability.display_id)}

```

**Query result**:

### Total number of open vulnerabilities with internet exposure

Get the total number of open, non-muted vulnerabilities with public internet exposure in your environment.

**Query example**:

```
fetch security.events
| filter dt.system.bucket=="default_securityevents_builtin"
     AND event.provider=="Dynatrace"
     AND event.type=="VULNERABILITY_STATE_REPORT_EVENT"
     AND event.level=="ENTITY"
// filter for the latest snapshot per entity
| dedup {vulnerability.display_id, affected_entity.id}, sort:{timestamp desc}
// filter for open non-muted vulnerabilities with public internet exposure
| filter vulnerability.resolution.status == "OPEN"
     AND vulnerability.mute.status != "MUTED"
     AND vulnerability.davis_assessment.exposure_status=="PUBLIC_NETWORK"
// count unique vulnerabilities
| summarize {`With internet exposure`=countDistinctExact(vulnerability.display_id)}

```

**Query result**:

### Total number of affected entities

Get the total number of affected entities in your environment.

**Query example**:

```
fetch security.events
| filter dt.system.bucket=="default_securityevents_builtin"
     AND event.provider=="Dynatrace"
     AND event.type=="VULNERABILITY_STATE_REPORT_EVENT"
     AND event.level=="ENTITY"
// filter for the latest snapshot per entity
| dedup {vulnerability.display_id, affected_entity.id}, sort:{timestamp desc}
// filter for open non-muted vulnerabilities
| filter vulnerability.resolution.status == "OPEN"
     AND vulnerability.mute.status != "MUTED"
// count unique entities
| summarize {`Affected entities`=countDistinctExact(affected_entity.id)}

```

**Query result**:

### Total number of affected process groups

Get the total number of affected process groups in your environment.

**Query example**:

```
fetch security.events
| filter dt.system.bucket=="default_securityevents_builtin"
     AND event.provider=="Dynatrace"
     AND event.type=="VULNERABILITY_STATE_REPORT_EVENT"
     AND event.level=="ENTITY"
// filter for the latest snapshot per entity
| dedup {vulnerability.display_id, affected_entity.id}, sort:{timestamp desc}
// filter for open non-muted vulnerabilities detected in running processes
| filter vulnerability.resolution.status == "OPEN"
     AND vulnerability.mute.status != "MUTED"
     AND affected_entity.type=="PROCESS_GROUP"
// count unique entities
| summarize {`Affected process groups`=countDistinctExact(affected_entity.id)}

```

**Query result**:

### Total number of affected entities over time

Get the total number of affected, non-muted entities over time (in three-hour buckets).

**Query example**:

```
fetch security.events
| filter dt.system.bucket=="default_securityevents_builtin"
     AND event.provider=="Dynatrace"
     AND event.type=="VULNERABILITY_STATE_REPORT_EVENT"
     AND event.level=="ENTITY"
     // filter for open non-muted vulnerabilities
     AND vulnerability.resolution.status == "OPEN"
     AND vulnerability.mute.status != "MUTED"
// count unique entities for each timestamp bucket of 3h
| sort timestamp desc
| summarize {entities=countDistinctExact(affected_entity.id)}, by: {timestamp=bin(timestamp, 3h)}

```

**Query result**:

### Total number of hosts related to vulnerabilities

Get the total number of hosts that are indirectly affected by open vulnerabilities in your environment.

**Query example**:

```
fetch security.events
| filter dt.system.bucket=="default_securityevents_builtin"
     AND event.provider=="Dynatrace"
     AND event.type=="VULNERABILITY_STATE_REPORT_EVENT"
     AND event.level=="ENTITY"
// filter for the latest snapshot per entity
| dedup {vulnerability.display_id, affected_entity.id}, sort:{timestamp desc}
// filter for open non-muted vulnerabilities
|filter  vulnerability.resolution.status == "OPEN"
     AND vulnerability.mute.status != "MUTED"
// count hosts
| summarize {`Related hosts`=arraySize(collectDistinct(related_entities.hosts.ids, expand:true))}

```

**Query result**:

### Open vulnerabilities by risk level

Get a count of open vulnerabilities split by risk levels.

**Query example**:

```
$25
```

**Query result**:

### Open vulnerabilities by type

Get a count of open vulnerabilities split by type.

**Query example**:

```
fetch security.events
| filter dt.system.bucket=="default_securityevents_builtin"
     AND event.provider=="Dynatrace"
     AND event.type=="VULNERABILITY_STATE_REPORT_EVENT"
     AND event.level=="ENTITY"
// filter for the latest snapshot per entity
| dedup {vulnerability.display_id, affected_entity.id}, sort:{timestamp desc}
// filter for open non-muted vulnerabilities
| filter vulnerability.resolution.status == "OPEN"
     AND vulnerability.mute.status != "MUTED"
// count vulnerabilities per type
| summarize { Vulnerabilities=countDistinctExact(vulnerability.display_id) }, by:{vulnerability.type}
| sort Vulnerabilities, direction:"descending"
| limit 10

```

**Query result**:

### Open vulnerabilities over time

Get the open vulnerability count over time, in three-hour buckets.

**Query example**:

```
fetch security.events
| filter dt.system.bucket=="default_securityevents_builtin"
     AND event.provider=="Dynatrace"
     AND event.type=="VULNERABILITY_STATE_REPORT_EVENT"
     AND event.level=="ENTITY"
     // filter for open non-muted vulnerabilities
     AND vulnerability.resolution.status == "OPEN"
     AND vulnerability.mute.status != "MUTED"
| sort timestamp desc
| summarize {Open=countDistinctExact(vulnerability.display_id)}, by: {timestamp=bin(timestamp,3h)}

```

**Query result**:

### Vulnerabilities on a library

Get the open vulnerabilities on a specific library (in this example, `log4j`).

**Query example**:

```
$26
```

**Query result**:

### Vulnerabilities on a host

Get the open vulnerabilities directly or indirectly affecting a specific host (in this example, `i-05f1305a50721e04d`).

**Query example**:

```
$27
```

**Query result**:

### Vulnerabilities on an application

Get the open vulnerabilities affecting a specific application (in this example, `www.easytravel.com`).

**Query example**:

```
$28
```

**Query result**:

### Top 10 affected entities by vulnerability count

Get the top 10 affected entities by the number of open vulnerabilities.

**Query example**:

```
fetch security.events
| filter dt.system.bucket=="default_securityevents_builtin"
     AND event.provider=="Dynatrace"
     AND event.type=="VULNERABILITY_STATE_REPORT_EVENT"
     AND event.level=="ENTITY"
// filter for the latest snapshot per entity
| dedup {vulnerability.display_id, affected_entity.id}, sort:{timestamp desc}
// filter for open non-muted vulnerabilities
| filter vulnerability.resolution.status == "OPEN"
     AND vulnerability.mute.status != "MUTED"
| summarize {
    `Affected entity name` = takeFirst(affected_entity.name),
    Type = takeFirst(affected_entity.type),
    Vulnerabilities = countDistinctExact(vulnerability.display_id)
}, by: {dt.source_entity=affected_entity.id}
| sort {Vulnerabilities, direction:"descending"}
| limit 10

```

**Query result**:

### Top 10 process groups with owners

Get the top five process groups by the count of open vulnerabilities, with their respective owners.

**Query example**:

```
$29
```

**Query result**:

### Hosts related to vulnerabilities on a library with owners

Get the hosts that are indirectly related to open vulnerabilities on a specific library (in this example, `tomcat`), with their respective owners.

**Query example**:

```
$2a
```

**Query result**:

### Vulnerable software components of a host with owners

Get the vulnerable components of a specific host (in this example, `HOST-4CF0F659B8823D74`) with owners.

**Query example**:

```
$2b
```

**Query result**:

### Vulnerable functions of a software component

Get the vulnerable functions of a specific software component (in this example, `SOFTWARE_COMPONENT-1D466FB7ADEBF92E`).

**Query example**:

```
fetch security.events
| filter dt.system.bucket=="default_securityevents_builtin"
     AND event.provider=="Dynatrace"
     AND event.type=="VULNERABILITY_STATE_REPORT_EVENT"
     AND event.level=="ENTITY"
// filter for the latest snapshot per entity
| dedup {vulnerability.display_id, affected_entity.id}, sort:{timestamp desc}
// filter for open non-muted vulnerabilities
| filter vulnerability.resolution.status == "OPEN"
     AND vulnerability.mute.status != "MUTED"
     // filter for the software component ID
     AND affected_entity.vulnerable_component.id=="SOFTWARE_COMPONENT-1D466FB7ADEBF92E"
| expand vulnerable_function=affected_entity.vulnerable_functions
| filter isNotNull(vulnerable_function)
| summarize{Usages=countIf(in(vulnerable_function,affected_entity.vulnerable_functions))}, by: {vulnerable_function}
| sort {Usages, direction:"descending"}

```

**Query result**:

## Query ingested events

### Total number of critical vulnerability findings

Get the total number of critical vulnerability findings ingested into Dynatrace.

**Query example**:

```
fetch security.events
| filter dt.system.bucket == "default_securityevents"
     AND event.type == "VULNERABILITY_FINDING"
     AND isNotNull(component.name)
// latest findings per affected object, vulnerability and component
| dedup {object.id, vulnerability.id, component.name, component.version}, sort: {timestamp desc}
// aggregation and custom filtering
| filter dt.security.risk.level=="CRITICAL"
| summarize {Vulnerabilities=countDistinctExact(vulnerability.id)}

```

**Query result**:

### Total number of vulnerable container images

Get the total number of container images containing vulnerability findings ingested into Dynatrace.

**Query example**:

```
fetch security.events
| filter dt.system.bucket == "default_securityevents"
     AND event.type == "VULNERABILITY_FINDING"
     AND isNotNull(component.name)
// latest findings per affected object, vulnerability and component
| dedup {object.id, vulnerability.id, component.name, component.version,
         container_image.registry, container_image.repository, container_image.tags}, sort: {timestamp desc}
// aggregation and custom filtering
| summarize {containerImages=countDistinctExact(container_image.digest)}

```

**Query result**:

### Total number of vulnerable components

Get the total number of vulnerable components in the container images containing vulnerability findings ingested into Dynatrace.

**Query example**:

```
fetch security.events
| filter dt.system.bucket == "default_securityevents"
     AND event.type == "VULNERABILITY_FINDING"
     AND isNotNull(component.name)
// latest findings per affected object, vulnerability and component
| dedup {object.id, vulnerability.id, component.name, component.version}, sort: {timestamp desc}
// aggregation and custom filtering
| summarize {components=countDistinctExact(component.name)}

```

**Query result**:

### Most recent vulnerability findings

Get the most recent vulnerability findings ingested into Dynatrace.

**Query example**:

```
fetch security.events
// data access
| filter dt.system.bucket == "default_securityevents"
     AND event.type == "VULNERABILITY_FINDING"
     AND isNotNull(component.name)
// latest findings per affected object, vulnerability and component
| dedup {object.id, vulnerability.id, component.name, component.version}, sort: {timestamp desc}
| sort timestamp desc

```

**Query result**:

### Number of scanned container images

Get the total number of ingested container images that have been scanned.

**Query example**:

```
fetch security.events
| filter dt.system.bucket == "default_securityevents"
| filter object.type == "CONTAINER_IMAGE" // includes both SCAN_EVENTS and VULNERABILITY_FINDINGS without scan events
| dedup {container_image.digest}, sort: {timestamp desc}
| summarize {containerImages=count()}

```

**Query result**:

### Number of container image scan events

Get the total number of scan events from ingested container images.

**Query example**:

```
fetch security.events
| filter dt.system.bucket == "default_securityevents"
| filter event.type == "VULNERABILITY_SCAN"
  AND object.type == "CONTAINER_IMAGE"
| summarize {scanEvents=count()}

```

**Query result**:

## Query compliance events

### Latest results for all covered systems

Get the latest compliance results of supported standards for all systems [covered by Security Posture Management](/secure/xspm/assess-coverage#coverage).

**Query example**:

```
fetch security.events
| filter dt.system.bucket == "default_securityevents_builtin"
  AND event.type == "COMPLIANCE_SCAN_COMPLETED"
// filter for the latest assessment
| dedup {object.name}, sort:{timestamp desc}
// parse the compliance percentage from json
| parse `scan.result.summary_json`, """JSON{JSON_ARRAY{JSON{ STRING:standardCode, INT:compliancePercentage }}:standardResultSummaries}(flat=true)"""
| expand standardResultSummaries
| fieldsFlatten standardResultSummaries
| fields timestamp, object.name, standard = standardResultSummaries.standardCode, compliance = standardResultSummaries.compliancePercentage

```

**Query result**:

### Historical compliance results for a standard for all covered systems

Get the historical compliance results for a standard (in this case, DORA) for all systems [covered by Security Posture Management](/secure/xspm/assess-coverage#coverage).

**Query example**:

```
fetch security.events
| filter dt.system.bucket == "default_securityevents_builtin"
  AND event.type == "COMPLIANCE_SCAN_COMPLETED"
// parse the compliance percentage from json
| parse `scan.result.summary_json`, """JSON{JSON_ARRAY{JSON{ STRING:standardCode, INT:compliancePercentage }}:standardResultSummaries}(flat=true)"""
| expand standardResultSummaries
| fieldsFlatten standardResultSummaries
// filter for the specific standard
| filter standardResultSummaries.standardCode == "DORA"
| fields timestamp, object.name, standardResultSummaries.compliancePercentage

```

**Query result**:

### Latest analysis results for a system in a selected timeframe

Get the latest analysis results for a given system in a selected timeframe.

This results in a view similar to that displayed in  **Security Posture Management** on the **Assessment results** page.

**Query example**:

```
$2c
```

**Query result**:

### Historical assessment results for selected rule and system

Get the counts for every assessment that happened in a selected period for a selected rule and system (in this case, `dt-cluster-01`).

**Query example**:

```
fetch security.events
| filter dt.system.bucket == "default_securityevents_builtin"
  AND event.type == "COMPLIANCE_FINDING"
  AND k8s.cluster.name == "dt-cluster-01"
  // filter for the specific rule
  AND compliance.rule.id == "DORA-67950"
// summarize findings on rule level
| summarize {
  timestamp = takeFirst(timestamp),
  Passed=countIf(compliance.result.status.level == "PASSED"),
  Failed=countIf(compliance.result.status.level == "FAILED"),
  Manual=countIf(compliance.result.status.level == "MANUAL")
}, by: {scan.id}
| makeTimeseries avg(Passed), avg(Failed), avg(Manual)

```

**Query result**:

### Latest misconfigurations of the object according to a specific standard

Get the counts of the latest misconfigurations of the object (in this case, `ip-10-45-243-57`) for a specific standard (in this case, CIS).

**Query example**:

```
fetch security.events
| filter dt.system.bucket == "default_securityevents_builtin"
  AND event.type == "COMPLIANCE_FINDING"
  // filter for desired object
  AND object.name == "ip-10-45-243-57"
  // filter for compliance findings reporting misconfigurations
  AND compliance.result.status.level == "FAILED"
  // filter for the specific standard
  AND compliance.standard.short_name == "CIS"
// filter for the latest rule assessment results in the timeframe
| join [
  fetch security.events
    | filter dt.system.bucket == "default_securityevents_builtin"
      AND event.type == "COMPLIANCE_SCAN_COMPLETED"
    // filter for desired system
      AND object.name == "demo-kspm"
    | dedup object.name, sort: { timestamp desc }
    | fields scan.id
  ], on: {scan.id}

```

**Query result**:
