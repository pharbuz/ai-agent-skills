# @dynatrace-sdk/client-classic-environment-v1

Source: <https://developer.dynatrace.com/develop/sdks/client-classic-environment-v1/v2/> (latest: `client-classic-environment-v1/v2`).

> Truncated — this SDK's auto-generated reference is large. Key exports/usage are below; see the full reference at the URL above.

## client-classic-environment-v1/v2

`/develop/sdks/client-classic-environment-v1/v2/`

- SDK for TypeScript
- Classic Environment V1
- V2

## Classic Environment V1
Documentation of the Dynatrace Classic Environment API v1. To read about use cases and examples, see Dynatrace Documentation.

Notes about compatibility:

- Operations marked as early adopter or preview may be changed in non-compatible ways, although we try to avoid this.

- We may add new enum constants without incrementing the API version; thus, clients need to handle unknown enum constants gracefully.

 @dynatrace-sdk/client-classic-environment-v1 v2.1.2 

`tsx
npm install @dynatrace-sdk/client-classic-environment-v1
`

### clusterConfigClient

`tsx
import { clusterConfigClient } from '@dynatrace-sdk/client-classic-environment-v1';
`

#### getClusterId

clusterConfigClient.getClusterId(config): PromiseClusterId>Gets the cluster id of the Dynatrace serverRequired scope: environment-api:cluster-id:read
Required permission: environment:roles:viewer

##### Returns
 |
 | Return type | Status code | Description
 | ClusterId | 200 | Success

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Client side error. | Server side error.Code example
`tsx
import { clusterConfigClient } from "@dynatrace-sdk/client-classic-environment-v1";const data = await clusterConfigClient.getClusterId();
`

### clusterVersionClient

`tsx
import { clusterVersionClient } from '@dynatrace-sdk/client-classic-environment-v1';
`

#### getVersion

clusterVersionClient.getVersion(config): PromiseClusterVersion>Gets the current version of the Dynatrace serverRequired scope: environment-api:cluster-version:read
Required permission: environment:roles:viewer

##### Returns
 |
 | Return type | Status code | Description
 | ClusterVersion | 200 | Success

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Client side error. | Server side error.Code example
`tsx
import { clusterVersionClient } from "@dynatrace-sdk/client-classic-environment-v1";const data = await clusterVersionClient.getVersion();
`

### deploymentClient

`tsx
import { deploymentClient } from '@dynatrace-sdk/client-classic-environment-v1';
`

#### downloadAgentInstallerWithVersion

deploymentClient.downloadAgentInstallerWithVersion(config): PromiseDownloads OneAgent installer of the specified versionRequired scope: environment-api:deployment:download
Required permission: environment:roles:agent-installFor the `paas` or `paas-sh` installer types you can get a configuring installer, by passing additional parameters.

##### Parameters
 |
 | Name | Type | Description
 | config.arch | "all" | "arm" | "ppc" | "ppcle" | "s390" | "sparc" | "x86" | The architecture of your OS:

- `all`: Use this value for AIX and z/OS. Defaults to `x86` for other OS types.

- `x86`: x86 architecture.

- `ppc`: PowerPC architecture, only supported for AIX.

- `ppcle`: PowerPC Little Endian architecture, only supported for Linux.

- `sparc`: Sparc architecture, only supported for Solaris.

- `arm`: ARM architecture, only supported for Linux.

- `s390`: S/390 architecture, only supported for Linux.

 Only applicable to the `paas` and `paas-sh` installer types.
 | config.bitness | "all" | "32" | "64" | The bitness of your OS. Must be supported by the OS.

 Only applicable to the `paas` and `paas-sh` installer types.
 | config.flavor | "default" | "multidistro" | "musl" | The flavor of your Linux distribution:

- `musl` for Linux distributions, which are using the musl C standard library, for example Alpine Linux.

- `multidistro` for Linux distributions, which are using musl C and glibc standard library.

- `default` for Linux distributions, which are using glibc standard library.

 Only applicable to the `paas` and `paas-sh` installer types.
 | config.ifNoneMatch | string | The ETag of the previous request. Do not download if it matches the ETag of the installer.
 | config.include | Array | The code modules to be included to the installer. You can specify several modules in the following format: `include=java&include=dotnet`.

 Only applicable to the `paas` and `paas-sh` installer types.
 | config.installerType*required | "default" | "default-unattended" | "mainframe" | "paas" | "paas-sh" | The type of the installer:

- `default`: Self-extracting installer for manual installation. Downloads an `.exe` file for Windows or an `.sh` file for Unix.
- `default-unattended`: Self-extracting installer for unattended installation. Windows only. Downloads a `.zip` archive, containing the `.msi` installer and the batch file. This option is deprecated with OneAgent version 1.173
- `mainframe`: Downloads all code modules for z/OS combined in a single `*.pax` archive.
- `paas`: Code modules installer. Downloads a `*.zip` archive, containing the `manifest.json` file with meta information or a `.jar` file for z/OS.
- `paas-sh`: Code modules installer. Downloads a self-extracting shell script with the embedded `tar.gz` archive.
 | config.networkZone | string | The network zone you want the result to be configured with.
 | config.osType*required | "windows" | "unix" | "aix" | "solaris" | "zos" | The operating system of the installer.
 | config.skipMetadata | boolean | Set `true` to omit the OneAgent connectivity information from the installer.

 Only applicable to the `paas` and `paas-sh` installer types.
 | config.version*required | string | The required version of the OneAgent in `1.155.275.20181112-084458` format.

 You can retrieve the list of available versions with the GET available versions of OneAgent call.

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 | Success. The payload contains the installer file.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Client side error. | Server side error.Code example
`tsx
import { deploymentClient } from "@dynatrace-sdk/client-classic-environment-v1";const data = await deploymentClient.downloadAgentInstallerWithVersion({ osType: "windows", installerType: "default", version: "...", });
`

#### downloadAgentOrchestrationSignatureWithVersion

deploymentClient.downloadAgentOrchestrationSignatureWithVersion(config): PromiseDownloads the requested version matching OneAgent deployment orchestration tarball's signatureRequired scope: environment-api:deployment:download
Required permission: environment:roles:agent-installDownloading the requested version matching deployment orchestration tarball's signature matching the requested Orchestration Type (ansible, puppet).

##### Parameters
 |
 | Name | Type | Description
 | config.orchestrationType*required | "ansible" | "puppet" | The Orchestration Type of the orchestration deployment script.
 | config.version*required | string | The requested version of the OneAgent deployment orchestration tarball in `0.1.0.20200925-120822` format.

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 | Success. The payload contains the installer file.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Client side error. | Server side error.Code example
`tsx
import { deploymentClient } from "@dynatrace-sdk/client-classic-environment-v1";const data = await deploymentClient.downloadAgentOrchestrationSignatureWithVersion( { orchestrationType: "ansible", version: "..." }, );
`

#### downloadAgentOrchestrationWithVersion

deploymentClient.downloadAgentOrchestrationWithVersion(config): PromiseDownloads the requested version matching OneAgent deployment orchestration tarballRequired scope: environment-api:deployment:download
Required permission: environment:roles:agent-installDownloading the requested version matching deployment orchestration tarball matching the requested Orchestration Type (ansible, puppet).

##### Parameters
 |
 | Name | Type | Description
 | config.orchestrationType*required | "ansible" | "puppet" | The Orchestration Type of the orchestration deployment script.
 | config.version*required | string | The requested version of the OneAgent orchestration deployment tarball in `0.1.0.20200925-120822` format.

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 | Success. The payload contains the installer file.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Client side error. | Server side error.Code example
`tsx
import { deploymentClient } from "@dynatrace-sdk/client-classic-environment-v1";const data = await deploymentClient.downloadAgentOrchestrationWithVersion( { orchestrationType: "ansible", version: "..." }, );
`

#### downloadBoshReleaseWithVersion

deploymentClient.downloadBoshReleaseWithVersion(config): PromiseDownloads BOSH release tarballs of the specified version, OneAgent includedRequired scope: environment-api:deployment:download
Required permission: environment:roles:agent-installFor SaaS, the call is executed on an Environment ActiveGate. Be sure to use the base of an ActiveGate, not the environment.

##### Parameters
 |
 | Name | Type | Description
 | config.networkZone | string | The network zone you want the result to be configured with.
 | config.osType*required | "windows" | "unix" | The operating system of the installer.
 | config.skipMetadata | boolean | Set `true` to omit the OneAgent connectivity information from the installer.

 If not set, `false` is used.
 | config.version*required | string | The required version of the OneAgent in the `1.155.275.20181112-084458` format.

 You can retrieve the list of available versions with the GET available versions of BOSH tarballs call.

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 | Success. The payload contains the BOSH release tarball file.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Client side error. | Server side error.Code example
`tsx
import { deploymentClient } from "@dynatrace-sdk/client-classic-environment-v1";const data = await deploymentClient.downloadBoshReleaseWithVersion({ osType: "windows", version: "...", });
`

#### downloadGatewayInstallerWithVersion

deploymentClient.downloadGatewayInstallerWithVersion(config): PromiseDownloads the ActiveGate installer of the specified versionRequired scope: environment-api:deployment:download
Required permission: environment:roles:agent-install

##### Parameters
 |
 | Name | Type | Description
 | config.arch | "all" | "s390" | "amd64" | "arm64" | The architecture of your OS:

- `all`: Defaults to `amd64`.
- `amd64`: amd64 architecture.
- `s390`: S/390 architecture, only supported for Linux.
- `arm64`: arm64 architecture, only supported for Linux.
 | config.ifNoneMatch | string | The ETag of the previous request. Do not download if it matches the ETag of the installer.
 | config.networkZone | string | The network zone you want the result to be configured with. Provided network zone must exist, otherwise the request will fail. Requires at least ActiveGate version 1.247.
 | config.osType*required | "windows" | "unix" | The operating system of the installer.
 | config.version*required | string | The required version of the ActiveGate installer, in `1.155.275.20181112-084458` format.

 You can retrieve the list of available versions with the GET available versions of ActiveGate call.

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 | Success. The payload contains the installer file.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Client side error. | Server side error.Code example
`tsx
import { deploymentClient } from "@dynatrace-sdk/client-classic-environment-v1";const data = await deploymentClient.downloadGatewayInstallerWithVersion( { osType: "windows", version: "..." }, );
`

#### downloadLatestAgentInstaller

deploymentClient.downloadLatestAgentInstaller(config): PromiseDownloads the latest OneAgent installerRequired scope: environment-api:deployment:download
Required permission: environment:roles:agent-installFor the `paas` or `paas-sh` installer types you can get a configuring installer, by passing additional parameters.

##### Parameters
 |
 | Name | Type | Description
 | config.arch | "all" | "arm" | "ppc" | "ppcle" | "s390" | "sparc" | "x86" | The architecture of your OS:

- `all`: Use this value for AIX and z/OS. Defaults to `x86` for other OS types.

- `x86`: x86 architecture.

- `ppc`: PowerPC architecture, only supported for AIX.

- `ppcle`: PowerPC Little Endian architecture, only supported for Linux.

- `sparc`: Sparc architecture, only supported for Solaris.

- `arm`: ARM architecture, only supported for Linux.

- `s390`: S/390 architecture, only supported for Linux.

 Only applicable to the `paas` and `paas-sh` installer types.
 | config.bitness | "all" | "32" | "64" | The bitness of your OS. Must be supported by the OS.

 Only applicable to the `paas` and `paas-sh` installer types.
 | config.flavor | "default" | "multidistro" | "musl" | The flavor of your Linux distribution:

- `musl` for Linux distributions, which are using the musl C standard library, for example Alpine Linux.

- `multidistro` for Linux distributions, which are using musl C and glibc standard library.

- `default` for Linux distributions, which are using glibc standard library.

 Only applicable to the `paas` and `paas-sh` installer types.
 | config.ifNoneMatch | string | The ETag of the previous request. Do not download if it matches the ETag of the installer.
 | config.include | Array | The code modules to be included to the installer. You can specify several modules in the following format: `include=java&include=dotnet`.

 Only applicable to the `paas` and `paas-sh` installer types.
 | config.installerType*required | "default" | "default-unattended" | "mainframe" | "paas" | "paas-sh" | The type of the installer:

- `default`: Self-extracting installer for manual installation. Downloads an `.exe` file for Windows or an `.sh` file for Unix.
- `default-unattended`: Self-extracting installer for unattended installation. Windows only. Downloads a `.zip` archive, containing the `.msi` installer and the batch file. This option is deprecated with OneAgent version 1.173
- `mainframe`: Downloads all code modules for z/OS combined in a single `*.pax` archive.
- `paas`: Code modules installer. Downloads a `*.zip` archive, containing the `manifest.json` file with meta information or a `.jar` file for z/OS.
- `paas-sh`: Code modules installer. Downloads a self-extracting shell script with the embedded `tar.gz` archive.
 | config.networkZone | string | The network zone you want the result to be configured with.
 | config.osType*required | "windows" | "unix" | "aix" | "solaris" | "zos" | The operating system of the installer.
 | config.skipMetadata | boolean | Set `true` to omit the OneAgent connectivity information from the installer.

 Only applicable to the `paas` and `paas-sh` installer types.

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 | Success. The payload contains the installer file.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Client side error. | Server side error.Code example
`tsx
import { deploymentClient } from "@dynatrace-sdk/client-classic-environment-v1";const data = await deploymentClient.downloadLatestAgentInstaller({ osType: "windows", installerType: "default", });
`

#### downloadLatestAgentOrchestration

deploymentClient.downloadLatestAgentOrchestration(config): PromiseDownloads the latest OneAgent deployment orchestration tarballRequired scope: environment-api:deployment:download
Required permission: environment:roles:agent-installDownloading the latest available deployment orchestration script tarball matching the requested Orchestration Type (ansible, puppet).

##### Parameters
 |
 | Name | Type | Description
 | config.orchestrationType*required | "ansible" | "puppet" | The Orchestration Type of the orchestration deployment script.

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 | Success. The payload contains the installer file.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Client side error. | Server side error.Code example
`tsx
import { deploymentClient } from "@dynatrace-sdk/client-classic-environment-v1";const data = await deploymentClient.downloadLatestAgentOrchestration({ orchestrationType: "ansible", });
`

#### downloadLatestAgentOrchestrationSignature

deploymentClient.downloadLatestAgentOrchestrationSignature(config): PromiseDownloads the latest OneAgent deployment orchestration tarball's signatureRequired scope: environment-api:deployment:download
Required permission: environment:roles:agent-installDownloading the latest available deployment orchestration tarball's sigature matching the requested Orchestration Type (ansible, puppet).

##### Parameters
 |
 | Name | Type | Description
 | config.orchestrationType*required | "ansible" | "puppet" | The Orchestration Type of the orchestration deployment script.

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 | Success. The payload contains the installer file.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Client side error. | Server side error.Code example
`tsx
import { deploymentClient } from "@dynatrace-sdk/client-classic-environment-v1";const data = await deploymentClient.downloadLatestAgentOrchestrationSignature( { orchestrationType: "ansible" }, );
`

#### downloadLatestGatewayInstaller

deploymentClient.downloadLatestGatewayInstaller(config): PromiseDownloads the configured standard ActiveGate installer of the latest version for the specified OSRequired scope: environment-api:deployment:download
Required permission: environment:roles:agent-install

##### Parameters
 |
 | Name | Type | Description
 | config.arch | "all" | "s390" | "amd64" | "arm64" | The architecture of your OS:

- `all`: Defaults to `amd64`.
- `amd64`: amd64 architecture.
- `s390`: S/390 architecture, only supported for Linux.
- `arm64`: arm64 architecture, only supported for Linux.
 | config.ifNoneMatch | string | The ETag of the previous request. Do not download if it matches the ETag of the installer.
 | config.networkZone | string | The network zone you want the result to be configured with. Provided network zone must exist, otherwise the request will fail. Requires at least ActiveGate version 1.247.
 | config.osType*required | "windows" | "unix" | The operating system of the installer.

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 | Success. The payload contains the installer file.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Client side error. | Server side error.Code example
`tsx
import { deploymentClient } from "@dynatrace-sdk/client-classic-environment-v1";const data = await deploymentClient.downloadLatestGatewayInstaller({ osType: "windows", });
`

#### getActiveGateInstallerAvailableVersions

deploymentClient.getActiveGateInstallerAvailableVersions(config): PromiseActiveGateInstallerVersions>Lists all available versions of ActiveGate installerRequired scope: environment-api:deployment:download
Required permission: environment:roles:agent-install

##### Parameters
 |
 | Name | Type | Description
 | config.arch | "all" | "s390" | "amd64" | "arm64" | The architecture of your OS:

- `all`: Defaults to `amd64`.
- `amd64`: amd64 architecture.
- `s390`: S/390 architecture, only supported for Linux.
- `arm64`: arm64 architecture, only supported for Linux.
 | config.osType*required | "windows" | "unix" | The operating system of the installer.

##### Returns
 |
 | Return type | Status code | Description
 | ActiveGateInstallerVersions | 200 | Success. The payload contains the available versions.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Client side error. | Server side error.Code example
`tsx
import { deploymentClient } from "@dynatrace-sdk/client-classic-environment-v1";const data = await deploymentClient.getActiveGateInstallerAvailableVersions( { osType: "windows" }, );
`

#### getActiveGateInstallerConnectionInfo

deploymentClient.getActiveGateInstallerConnectionInfo(config): PromiseActiveGateConnectionInfo>Gets the connectivity information for Environment ActiveGateRequired scope: environment-api:deployment:download
Required permission: environment:roles:agent-install

##### Parameters
 |
 | Name | Type | Description
 | config.defaultZoneFallback | boolean | Set `true` to perform a fallback to the default network zone if the provided network zone does not exist.
 | config.networkZone | string | The network zone you want the result to be configured with.

##### Returns
 |
 | Return type | Status code | Description
 | ActiveGateConnectionInfo | 200 | Success

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Client side error. | Server side error.Code example
`tsx
import { deploymentClient } from "@dynatrace-sdk/client-classic-environment-v1";const data = await deploymentClient.getActiveGateInstallerConnectionInfo();
`

#### getAgentInstallerAvailableVersions

deploymentClient.getAgentInstallerAvailableVersions(config): PromiseAgentInstallerVersions>Lists all available versions of OneAgent installerRequired scope: environment-api:deployment:download
Required permission: environment:roles:agent-install

##### Parameters
 |
 | Name | Type | Description
 | config.arch | "all" | "arm" | "ppc" | "ppcle" | "s390" | "sparc" | "x86" | The architecture of your OS:

- `all`: Use this value for AIX and z/OS. Defaults to `x86` for other OS types.

- `x86`: x86 architecture.

- `ppc`: PowerPC architecture, only supported for AIX.

- `ppcle`: PowerPC Little Endian architecture, only supported for Linux.

- `sparc`: Sparc architecture, only supported for Solaris.

- `arm`: ARM architecture, only supported for Linux.

- `s390`: S/390 architecture, only supported for Linux.

 Only applicable to the `paas` and `paas-sh` installer types.
 | config.flavor | "default" | "multidistro" | "musl" | The flavor of your Linux distribution:

- `musl` for Linux distributions, which are using the musl C standard library, for example Alpine Linux.

- `multidistro` for Linux distributions, which are using musl C and glibc standard library.

- `default` for Linux distributions, which are using glibc standard library.

 Only applicable to the `paas` and `paas-sh` installer types.
 | config.installerType*required | "default" | "default-unattended" | "mainframe" | "paas" | "paas-sh" | The type of the installer:

- `default`: Self-extracting installer for manual installation. Downloads an `.exe` file for Windows or an `.sh` file for Unix.
- `default-unattended`: Self-extracting installer for unattended installation. Windows only. Downloads a `.zip` archive, containing the `.msi` installer and the batch file. This option is deprecated with OneAgent version 1.173
- `mainframe`: Downloads all code modules for z/OS combined in a single `*.pax` archive.
- `paas`: Code modules installer. Downloads a `*.zip` archive, containing the `manifest.json` file with meta information or a `.jar` file for z/OS.
- `paas-sh`: Code modules installer. Downloads a self-extracting shell script with the embedded `tar.gz` archive.
 | config.osType*required | "windows" | "unix" | "aix" | "solaris" | "zos" | The operating system of the installer.

##### Returns
 |
 | Return type | Status code | Description
 | AgentInstallerVersions | 200 | Success. The payload contains the available versions.

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Client side error. | Server side error.Code example
`tsx
import { deploymentClient } from "@dynatrace-sdk/client-classic-environment-v1";const data = await deploymentClient.getAgentInstallerAvailableVersions( { osType: "windows", installerType: "default" }, );
`

#### getAgentInstallerConnectionInfo

deploymentClient.getAgentInstallerConnectionInfo(config): PromiseConnectionInfo>Gets the connectivity information for OneAgentRequired scope: environment-api:deployment:download
Required permission: environment:roles:agent-install

##### Parameters
 |
 | Name | Type | Description
 | config.defaultZoneFallback | boolean | Set `true` to perform a fallback to the default network zone if the provided network zone does not exist.
 | config.networkZone | string | The network zone you want the result to be configured with.
 | config.version | string | The version of the OneAgent for which you're requesting connectivity information, in the `1.221` format.

 Set this parameter to get the best format of endpoint list for optimal performance.

##### Returns
 |
 | Return type | Status code | Description
 | ConnectionInfo | 200 | Success

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Client side error. | Server side error.Code example
`tsx
import { deploymentClient } from "@dynatrace-sdk/client-classic-environment-v1";const data = await deploymentClient.getAgentInstallerConnectionInfo();
`

#### getAgentInstallerConnectionInfoEndpoints

deploymentClient.getAgentInstallerConnectionInfoEndpoints(config): Promisestring>Gets the list of the ActiveGate-Endpoints to be used for Agents ordered by networkzone-priorities.Required scope: environment-api:deployment:download
Required permission: environment:roles:agent-installHighest priority first, separated by a semicolon.If no network zone provided the default zone is used. Responds with 404 if network zone is not known.

##### Parameters
 |
 | Name | Type | Description
 | config.defaultZoneFallback | boolean | Set `true` to perform a fallback to the default network zone if the provided network zone does not exist.
 | config.networkZone | string |

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 | Success

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Client side error. | Server side error.Code example
`tsx
import { deploymentClient } from "@dynatrace-sdk/client-classic-environment-v1";const data = await deploymentClient.getAgentInstallerConnectionInfoEndpoints();
`

#### getAgentInstallerMetaInfo

deploymentClient.getAgentInstallerMetaInfo(config): PromiseAgentInstallerMetaInfoDto>Gets the latest available version of a OneAgent installerRequired scope: environment-api:deployment:download
Required permission: environment:roles:agent-installIf a target version is configured, then this is the downloaded version.Non-required parameters are only applicable to the `paas` and `paas-sh` installer types.

##### Parameters
 |
 | Name | Type | Description
 | config.arch | "all" | "arm" | "ppc" | "ppcle" | "s390" | "sparc" | "x86" | The architecture of your OS:

- `all`: Use this value for AIX and z/OS. Defaults to `x86` for other OS types.

- `x86`: x86 architecture.

- `ppc`: PowerPC architecture, only supported for AIX.

- `ppcle`: PowerPC Little Endian architecture, only supported for Linux.

- `sparc`: Sparc architecture, only supported for Solaris.

- `arm`: ARM architecture, only supported for Linux.

- `s390`: S/390 architecture, only supported for Linux.

 Only applicable to the `paas` and `paas-sh` installer types.
 | config.bitness | "all" | "32" | "64" | The bitness of your OS. Must be supported by the OS.

 Only applicable to the `paas` and `paas-sh` installer types.
 | config.flavor | "default" | "multidistro" | "musl" | The flavor of your Linux distribution:

- `musl` for Linux distributions, which are using the musl C standard library, for example Alpine Linux.

- `multidistro` for Linux distributions, which are using musl C and glibc standard library.

- `default` for Linux distributions, which are using glibc standard library.

 Only applicable to the `paas` and `paas-sh` installer types.
 | config.installerType*required | "default" | "default-unattended" | "mainframe" | "paas" | "paas-sh" | The type of the installer:

- `default`: Self-extracting installer for manual installation. Downloads an `.exe` file for Windows or an `.sh` file for Unix.
