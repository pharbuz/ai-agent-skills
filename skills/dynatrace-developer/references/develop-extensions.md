# Develop — Extensions

Scraped from <https://developer.dynatrace.com/develop/>. Each section is one doc page (its path is shown) with the prose and code captured.

## about-extensions-v2

`/develop/extensions/about-extensions-v2/`

- About Extensions

## About Extensions

- Explanation
- 1-min readGet your data into Dynatrace with Extensions 2.0.

Dynatrace can ingest data from hundreds of tools, which means you get:

- A single source of truth for observability.

- A continuous flow of actionable data to help you fix problems quickly, maintain complex systems, improve code quality, and speed up digital transformation.

If we don't have a pre-built solution for your situation, you can declaratively bring metrics into Dynatrace that feed platform analytics and monitoring capabilities. Dynatrace links your data meaningfully so you can explore it, build instrumentation, and set up alerts.

### Troubleshooting

- See the troubleshooting articles available in Dynatrace Community.

### Related topics

- Extensions docs

---

## dynatrace-extensions-vscode

`/develop/extensions/dynatrace-extensions-vscode/`

- Add-on for VS Code

## Add-on for VS Code

- Explanation
- 2-min readDynatrace Extensions is an add-on for Visual Studio Code that supports all aspects of developing Extensions 2.0 running on Dynatrace. Find it by searching the VS Code extensions marketplace.

It gives you access to a specialized toolkit that's ready to use and helps you out with the following:

- Operational efficiency

- Content creation

- Content validation

Check out the instructions for getting started, or keep reading to learn some of its features.

### Features

Following are some features of Dynatrace Extensions.

#### Operational efficiency

Dynatrace Extensions makes you more operationally efficient when developing Extensions 2.0. It includes the following features:

- Extension 2.0 project management and organization at scale.

- Overview of deployments across multiple environments.

- All extension-related operations available within your editor:

- Create, build, sign, upload, and activate extensions.

- Create and manage monitoring configurations.

- Create and manage credentials used in signing your extensions.

#### Content creation

You can also automatically generate significant portions of your extension's manifest and other content. Following are the features that you can use:

- Generate Unified analysis screens for your entities.

- Generate documentation, dashboards, and alerts.

- Run Windows Management Instrumentation (WMI) Queries to extract metrics and dimensions automatically.

- Connect to Prometheus exporters to extract metrics, dimensions, and metadata automatically.

- Use code completions where the values depend on data from your environment.

#### Content validation

You can use the Dynatrace Extensions to validate your extension manifest early. Following are the features that you can use:

- Validate against targeted YAML schema versions.

- Get custom diagnostics beyond what's included in the schema.

- Validate your metric and entity selectors against environment data.

### Support

This open source project relies on community feedback and contribution and isn't officially supported by Dynatrace.

For any issues, concerns, or contributions, leverage the issues page of the GitHub repository hosting this project.

---

## dynatrace-extensions-vscode/commands

`/develop/extensions/dynatrace-extensions-vscode/commands/`

- Add-on for VS Code
- Commands reference

## Commands reference

- 10-min readAll major workflows automated by the Dynatrace Extensions add-on are exposed as VS Code commands and accessible from the editor's command palette. To open the command palette, press the F1 key, where you can find all available commands with the Dynatrace extensions prefix.

### Command overview

 |
 | Command | Description
 | Initialize workspace | Register and initialize your workspace. The first step to get started
 | Load schemas | Download schema files and setup manifest validation
 | Generate certificates | Generate developer certificates for signing extensions
 | Distribute certificate | Distribute your CA certificate to components that use it
 | Build | Build your extension and create a signed package
 | Upload | Upload the latest extension package to your Dynatrace environment
 | Activate | Activate a version of the current extension
 | Create documentation | Generate a README.md file about the extension and its contents
 | Create a dashboard | Generate a landing page dashboard to bundle with your extension
 | Create alert | Generate metric events for alerting to bundle with your extension
 | Convert JMX | Convert a Java management extensions (JMX) extension to the 2.0 framework

### Initialize workspace

This command initializes a new or existing workspace for Extension 2.0 development and registers it with our VS Code add-on. As part of initialization, a starting folder structure and some template extension files are created to help any project start correctly.

You can explore this command in detail by visiting our Getting started guide.

#### Command prerequisites

- A workspace or folder needs to be opened in the VS Code window.

- You need to be connected to a Dynatrace environment.

#### Workflow steps

- Provisions internal storage for this project.

- Invoke the workflow from Load schemas. You can skip this step if you have already registered your workspace with Dynatrace Extensions.

- Associate certificates with the workspace. Allow choice:

- Use existing: Checks settings for developer certificate and key.

- Generate new ones: Invokes workflow from Generate certificates.

- Register the workspace with Dynatrace Extensions.

- Create a project folder and files based on the chosen template.

#### Project templates

##### Extension 2.0

It's the default choice. Whether you already have all the contents and want to register the workspace with our add-on or start a new extension from scratch. It'll generate the extension folder and a manifest with the minimum mandatory details required for any extension.

##### Python extension 2.0

This option creates a new extension that uses the Python data source. As part of the setup, we'll also download and install the Dynatrace Extensions SDK module for Python.

##### JMX 1.0 conversion

The JMX data source is now available with Extensions 2.0, meaning it's time to convert your JMX extensions from the 1.0 framework. This type of project will guide you to provide a 1.0 JMX Extension (either from a local file or your tenant), and it will convert it to the new framework and create your manifest.

##### Existing 2.0 extension

Need to edit an already deployed extension? Are you curious about what the content of a Dynatrace-built extension looks like? This option downloads an extension 2.0 package from your tenant and unpacks it into your workspace.

### Load schemas

This command downloads schema files of a specific version from your connected Dynatrace environment and sets up validation for the extension manifest. If your project already has an extension manifest, this is updated with the chosen version.

#### Command prerequisites

- You need to be connected to a Dynatrace environment.

#### Workflow steps

- Your Dynatrace environment is queried for the list of available schema versions. And you'll be prompted to select which version to use.

- The files associated with the selected schema version are downloaded and stored in the global Visual Studio Code storage.

- If you have downloaded the files before, you'll be prompted and can skip this step.

- Workspace settings are updated to enable validation of your extension manifest with the selected schema.

- If a manifest file is present in the workspace, it will be updated with the selected minimum version.

### Generate certificates

This command generates all the credentials needed for signing and validating Extensions 2.0.

#### Command prerequisites

- A workspace or folder needs to be opened in the VS Code window.

#### Workflow steps

- An RSA key pair is generated to generate your CA certificate.

- Another RSA key pair is generated, then used to generate your developer certificate, adding your CA certificate as the issuing authority on this credential.

- The developer certificate is generated from the RSA key pair, and the CA certificate is added as the issuing authority on this certificate.

- Note: You can customize all details used for generating these certificates through the settings.

- All intermediary files are stored in the VS Code workspace storage, and the credential settings for this workspace are updated with the paths to the generated files. And this is done in the `./vscode/settings.json` file.

- Invoke workflow from Distribute certificate

### Distribute certficate

This command uploads the workspace's CA certificate to the Dynatrace Credentials Vault. Additionally, if it detects locally installed OneAgents or ActiveGates, it also uploads this certificate to them.

#### Command prerequisites

- A workspace or folder needs to be opened in the VS Code window.

- You need to be connected to a Dynatrace environment.

- The `dynatraceExtensions.rootOrCaCertificate` setting needs to be set either globally or for the workspace.

#### Workflow steps

The add-on checks whether a Dynatrace Credentials Vault entry ID is already associated with this workspace and prompts whether the entry should be overwritten.

- If overwrite is selected, the entry is updated with the new file.

- Otherwise, the workflow continues with creating a new Credential Vault entry.

You are prompted to provide a name for this credential and an optional description. Then the file is uploaded with these details.

Local OneAgent and ActiveGate paths are checked for existence, and the flow prompts whether the certificate should also be uploaded to these locations.

- On Windows:

- OneAgent: `%PROGRAMDATA%\dynatrace\oneagent\agent\config\certificates`

- ActiveGate: `%PROGRAMDATA%\dynatrace\remotepluginmodule\agent\conf\certificates`

- On Linux:

- OneAgent: `/var/lib/dynatrace/oneagent/agent/config/certificates`

- ActiveGate: `/remotepluginmodule/agent/conf/certificates/`

NoteThis step requires VS Code to run with administrator-level permissions. For example, for Windows, use Run As Administrator.

### Build

This command builds your extension and bundles it into a signed ZIP file archive, then places it in the `dist` folder of the workspace.

#### Command prerequisites

- A registered workspace needs to be open in the VS Code window.

- Developer certificates need to be associated with the workspace.

- No error/problems need to be detected with the extension manifest.

#### Workflow steps

- The extension version is picked up from the manifest. If you're connected to a Dynatrace environment, the version is checked for conflicts and automatically incremented if needed.

- The extension manifest and assets are bundled into a ZIP file archive signed using your developer credentials. The resulting signature and the archive are added to a final ZIP file representing the extension package.

- If you're connected to a Dynatrace environment, the package is validated against it. Any validation errors are communicated in an Output Channel (within your editor window), and the workflow terminates. Only valid packages are moved to your workspace's `dist` folder.

- Invoke workflow from Upload.

### Upload

This command uploads the most recent package from your workspace's `dist` folder to your connected environment.

#### Command prerequisites

- A registered workspace needs to be open in the VS Code window.

- You need to be connected to a Dynatrace environment.

- A ZIP file archive needs to be in the workspace's `dist` folder.

#### Workflow steps

- We check if an upload is possible by querying the number of versions already deployed for this extension.

- If too many versions exist, you'll be prompted to remove the oldest one.

- The add-on attempts to remove the oldest version; however, if this fails (for example, monitoring configurations may be linked to it), you'll be prompted to choose a different version to remove.

- When it's possible, the extension is uploaded.

- Invoke workflow from Activate to activate this version.

### Activate

This command activates a version of your workspace's extension.

#### Command prerequisites

- A registered workspace needs to be open in the VS Code window.

- You need to be connected to a Dynatrace environment.

#### Workflow steps

- The extension name is read from the manifest in your workspace.

- Your Dynatrace environment is queried for the available versions of the extension, and you'll be prompted to choose which one to activate.

- This step is skipped when the command is invoked from another workflow. For example, Upload

- The chosen version is activated in your Dynatrace environment.

### Create documentation

This command automatically generates rich documentation in a `README.md` file by analyzing the extension package and its contents.

#### Command prerequisites

- A registered workspace needs to be open in the VS Code window.

#### Workflow steps

- The command reads through the extension manifest, extracting all generic topology entities.

- Next, metrics are extracted from the manifest.

- Next, dashboards are extracted from the manifest.

- After that, alerts are processed into human-readable summaries.

- Metrics are mapped to feature sets and linked to the defined entities.

- The readme file is created, with missing information skipped as needed.

### Create a dashboard

This command reads through the extension manifest and generates an overview dashboard which serves as a landing page for the extension.

#### Command prerequisites

- A registered workspace needs to be open in the VS Code window.

- The extension manifest needs to contain at least a topology definition.

#### Workflow steps

- The command extracts the generic entity types defined in your manifest and any metrics associated with them. The first one or two metrics are taken for each entity type.

- Your dashboard is created from a template containing the following:

- Single value tiles which show the count of distinct monitored entities.

- A list of markdown links so that each entity has a quick entry point to its unified analysis screen.

- Tables for each entity type, alongside graph charts based on associated metrics.

- Your dashboard is saved in the `./extension/dashboards/overview_dashboard.json` file, and the extension manifest is edited to include the reference to this asset.

- The workflow finishes with the prompt to upload this dashboard to your Dynatrace environment.
NoteYour dashboard will automatically be uploaded as part of the extension deployment. This final step is offered if you want an early preview of the asset before your extension deployment.

### Create alert

This command creates a metric event based on metrics defined in your extension's manifest.

#### Command prerequisites

- A registered workspace needs to be open in the VS Code window.

- The extension manifest needs to contain metrics metadata.

#### Workflow steps

- The command parses your extension manifest and presents a selection box with all available metrics. Select one to continue.

- You are then prompted for a title for this alert.

- You need to choose whether your threshold breach happens when the metric goes above or below a given level.

- Finally, provide the actual value the alert threshold relates to.

- The command completes by writing your alert JSON file in the `./extension/alerts` folder and updating your extension manifest to include the newly generated alert.

### Convert JMX

This command converts an existing JMX extension to Extension 2.0.

#### Workflow steps

- You're prompted on how the JMX extension should be loaded in:

- Locally - browse your filesystem and select a JSON or ZIP file containing the JMX extension.

- Remotely - browse JMX extensions available on your connected tenant.

- You're prompted to select a process technology if one can't be detected automatically.

- You're asked whether to include the data on your host's details page.

- The workflow processes the JMX extension JSON file and converts it to an equivalent extension 2.0 manifest.

- The workflow saves the generated manifest at `extension/extension.yaml` or prompts you for a save destination if this folder doesn't exist in your workspace.

TipYou can explore this workflow as part of our JMX 1.0 Conversion guide.

---

## dynatrace-extensions-vscode/development_assistance

`/develop/extensions/dynatrace-extensions-vscode/development_assistance/`

- Add-on for VS Code
- Development assistance

## Development assistance

- 10-min readDynatrace Extensions leverages the full power of your VS Code editor to help you create better extensions faster.

Read on to learn how to make the most out of these features.

### Feature overview

 |
 | Feature type | Description
 | Code completions | Suggestions for auto-completing words or fields of the manifest
 | Code actions | Commands generating or editing the content of your extension's manifest
 | Code lens | Additional commands to interact with extension data
 | Fast development mode | A workflow focused on speed of delivery
 | Diagnostics | Additional diagnostics beyond simple schema validation

### Code completions

Code completions or suggestions happen at key points within the extension manifest. Either automatically or on-demand (using Ctrl + Space), these offer known values that can be inserted at the location of your cursor.

#### Implemented triggers

 |
 | Keyword trigger | Effects
 | On `fromType:` or `toType:` inside `topology.relationships` list items | Browse built-in and custom entity types
 | On `sourceAttribute:` inside `mappingRules` list items of topology relationships | Browse entity attributes (entity needs to be present in the `fromType` attribute)
 | On `destinationAttribute:` inside `mappingRules` list items of topology relationships | Browse entity attributes (entity needs to be present in `toType` attribute)
 | On `entityType:` and `entityTypes:` | Browse relevant entity types
 | On `key:` (of attributes inside screen properties) | Attributes are suggested from topology and built-in values
 | On `entitySelectorTemplate:` | Use Ctrl + Space to trigger completions as you build your selector or choose one of the pre-built selectors (from relationships seen in your manifest)
 | On `iconPattern:` (within topology rules) or `icon:` (within staticContent header) | Browse available Barista icon codes
 | On `key:` (of cards in `screens`, either in layout or individual lists) | Browse keys of cards defined but not yet utilized
 | On `value:`, for metrics and dimensions of a Prometheus extension | Browse metrics and dimensions scraped using the Prometheus code lens
 | On `description:` (in the `metrics` section of the manifest) | For those metrics that have been scraped using the Prometheus code lens, add the description from the scraped data

### Code actions

Code actions happen on key lines of your extension manifest. Your editor will automatically show a lightbulb icon
whenever actions are relevant to the clicked line. Typically these will generate and insert content into
your extension manifest or fix issues highlighted by Dynatrace Extensions.

#### Currently implemented triggers

 |
 | Action trigger | Effects
 | Inside `propertiesCard` when clicking on properties | Automatically add properties for the entity's attributes and relations
 | Inside `entitiesListCards` when clicking on columns | Automatically add columns for the listed entity's attributes and relations
 | Inside `chartsCards` and `entitiesListCards` when clicking on charts inside a card | Automatically add charts for metrics that aren't already in the card
 | Inside `graphChartConfig` when clicking on metrics | Add more metrics to your chart that aren't used within the surrounding card
 | Inside `screens` when clicking on `chartsCards` | Automatically add chart cards for entire feature sets of metrics
 | Inside `screens` when clicking on `entitiesListCards` | Automatically add cards for listing this entity as well as the related ones
 | When clicking on `metrics` within the Prometheus data source | Automatically add details from a scraped Prometheus endpoint
 | On `screens` | Automatically generate entire unified analysis screens for your entities
 | Inside `entitiesListCards` when clicking on `filtering` | Insert entire filtering blocks with a default filter by name
 | Inside `entitiesListCards` and inside `filtering`, when clicking on `filters` | Insert individual filter for the entity's attributes
 | Inside `screens` when clicking on `actions` | Insert global actions to configure the extension
 | Inside `actions` when clicking on `actions` | Insert an action expression to configure the extension

### Code lens

Code lenses are actionable, contextual information interspersed with your code. For Dynatrace Extensions, these can help trigger
code-related actions to your Dynatrace environment or other external endpoints.

#### Metric selectors

The lens appears automatically wherever `metricSelector` and shows:

- Query data - an action that runs the metric selector query and visualizes its results

- Validate selector - an action to verify this selector against your Dynatrace environment

- An icon representing the last validation status for this selector. You can hover over it for more details

Metric selector results are displayed within a separate metric panel:

Any errors from querying your environment are displayed in the Dynatrace output panel (by default at the bottom of your editor):

#### Entity selectors

The lens appears automatically wherever `entitySelector` is mentioned and shows:

- Query data - an action that runs the entity selector query and visualizes its results

- Validate selector - an action to verify this selector against your Dynatrace environment

- An icon representing the last validation status for this selector. You can hover over it for more details

Entity selector results, as well as any errors, are displayed within the Dynatrace output panel (by default at the bottom of your editor):

#### Prometheus

The lens appears automatically when the Prometheus data source is defined and shows:

- Scrape data - an action that connects to a Prometheus scraper endpoint and collects its data

- Edit config - an action that allows you to make changes to the connected Prometheus endpoint

- Text indicating the status of the last scrape action, such as the timestamp and number of metrics scraped

After the data has been scraped, this can be used with Code actions to:

- insert metric definitions in the `prometheus` section of the manifest

- insert dimensions in the `prometheus` section of the manifest

- insert metric metadata in the `metrics` section of the manifest

#### Windows Management Interface (WMI) queries

The lens appears automatically over queries inside the WMI data source definition and shows:

- Run WMI Query: an action that runs your query against the local Windows machine

- Text indicating the summary of the query results (i.e., how many object instances were found)

The full results of running the WMI query are displayed in a separate panel:

After a query is run, you can use the results with Code completions

#### Unified analysis screens

The lens appears automatically over entity type definitions inside the `screens` element of the manifest
and shows:

- Open List View: an action to open a browser window to this entity's Unified analysis list view

- Open Details view: an action to open a browser window to this entity's Unified analysis details view

NoteA 404 response code is expected if your entity type does exist yet.

### Fast development mode

Fast development mode is a workflow designed to allow advanced developers to gain immediate feedback on the current state of their extension and minimize the steps and time it takes to see updates in their connected Dynatrace environment.

#### How does it work?

When enabled, every time the extension manifest saves, the extension version automatically increments, and the extension is packaged, signed, and uploaded to your connected environment. The workflow is hands-free, so if the maximum number of extension versions is reached, one will be removed automatically so the upload can succeed.

An accompanying status bar confirms the mode is active and displays the status of the last attempted build.

With this workflow, pre-upload validation is skipped in favor of speed, and any issues are communicated immediately via an
output channel.

When developing your static assets, such as the unified analysis screens, this mode is the quickest way
to cycle through a variety of changes before finding your ideal configuration.

### Diagnostics

Often, perfectly valid YAML still produces a manifest that causes issues when we upload the
extension to Dynatrace or later when it tries to run. Many of these situations can be caught early, and Dynatrace Extensions aims to bring these to light so you can fix them and reduce the number
of failed deployment attempts.

#### How do custom diagnostics work?

On every edit of your extension manifest, the diagnostics suite will trigger an update of all diagnostic
items applicable to that file. Based on findings, relevant content is highlighted within the manifest, and
hovering over the highlight will provide more details about the issue.

Some issues may provide a Quick fix link as part of the hover information. If this is available, it will
trigger a content change of the document to resolve the highlighted issue.

Diagnostic severities:

- `Error` - these findings are highlighted in red and represent issues that would break your extension when deployed. The Build command won't work if `Error` severity diagnostics are in your manifest.

- `Warning` - these findings are highlighted in yellow and represent issues that would not stop an extension from functioning but may still produce undesired behaviors.

#### Currently implemented diagnostics

 |
 | Code | Severity | What does it mean?
 | DED001 | `Error` | Your extension doesn't have a name, which is mandatory.
 | DED002 | `Error` | Your extension's name needs to be less that 50 character. characters.
 | DED003 | `Error` | Your extension's name is invalid. It should only contain lowercase letters, numbers, hyphens, underscores, or dots.
 | DED004 | `Error` | Your extension's name needs to start with custom: but it doesn't.
 | DED005 | `Warning` | Internal Dynatrace extension names shouldn't start with custom:.
 | DED006 | `Warning` | Metrics of type count should have keys ending in .count or _count.
 | DED007 | `Warning` | Metrics of type gauge shouldn't have keys ending in .count or _count.
 | DED008 | `Error` | You referenced this card key in a screen layout, but it doesn't have a definition.
 | DED009 | `Warning` | You defined this card, but you're not referencing it in the screen layout.
 | DED010 | `Warning` | There is no online data about this Object Identifier (OID). You may want to validate it.
 | DED011 | `Error` | This OID isn't readable. The access permissions (MAX-ACCESS) don't allow it.
 | DED012 | `Error` | This OID returns a string, but you're using it as a metric value.
 | DED013 | `Warning` | This OID returns a Counter, but you're using it as a Gauge metric.
 | DED014 | `Warning` | This OID returns a Gauge, but you're using it as a Counter metric.
 | DED015 | `Error` | Invalid OID syntax. OID shouldn't start/end with '.' and may only contain dots and digits.
 | DED016 | `Error` | Invalid OID syntax. OIDs shouldn't end in '.0' when 'table' is set to 'true' in the subgroup.
 | DED017 | `Error` | Invalid OID syntax. OIDs needs to end in '.0' when 'table' is set to 'false' in the subgroup.
 | DED018 | `Error` | Online data lists this OID as static, but you're using it inside a 'table' subgroup.
 | DED019 | `Error` | Online data maps this OID to table entries, but you're not using it inside a 'table' subgroup.
NoteThe code itself doesn't mean anything; it just provides a unique identifier within all diagnostics that may come up
in VS Code. We chose the DED prefix to stand for Dynatrace Extensions Diagnostic.

---

## dynatrace-extensions-vscode/getting-started

`/develop/extensions/dynatrace-extensions-vscode/getting-started/`

- Add-on for VS Code
- Getting started

## Getting started

- How-to guide
- 5-min readGet started with Dynatrace Extensions by following this guide to set up your Visual Studio Code editor and get your first extension built and uploaded to Dynatrace in 5 minutes.

### Before you begin

#### Installation

You can find Dynatrace Extensions in the Visual Studio Code marketplace. Install it from there or via the VS Code extension search.

#### Access token

Our VS Code add-on automates many operations around Extension 2.0 development by using the Dynatrace API.

To get the most out of it, create an API Access Token with the following scopes:

- `WriteConfig`

- `ReadConfig`

- `credentialVault.read`

- `credentialVault.write`

- `extensions.read`

- `extensions.write`

- `extensionEnvironment.write`

- `extensionEnvironment.read`

- `extensionConfigurations.read`

- `extensionConfigurations.write`

- `metrics.read`

- `entities.read`

- `settings.read`

- `settings.write`

TipThe Dynatrace UI provides a dedicated template called Extension Development, which applies these exact token scopes.

#### Connectivity settings

This step is only required if your Dynatrace environment is accessible through a dedicated URL that uses a custom-signed or a self-signed SSL certificate.

In this situation, you need to adapt your settings before you can continue with this guide. Go to File > Preferences > Settings, expand on Extensions, and find the Dynatrace Extensions section. Scroll down until you see Tenant Connectivity Settings and select Edit in settings.json.

Register your dedicated environment URL in the file you've opened and either provide the path to your CA file or turn off SSL verification. For example:

settings.json
`tsx
{ "dynatraceExtensions.tenantConnectivitySettings": [ { "tenantUrl": "https://my.custom.dynatrace/e/abcd-123", "certificatePath": "/tmp/certificates/ca.crt" } ]}
`

NoteYou can explore these settings in more detail here

### Connect to Dynatrace

Begin by connecting with your Dynatrace environment. To connect, you need to do the following:

Go to the Dynatrace Extensions view in the VS Code UI, then select the Add environment button as shown.

You'll need to provide the base URL to access Dynatrace. It should follow one of these patterns:

- `https://.live.dynatrace.com` for SaaS environments.

- `https:///e/` for Managed environments.

- `https://.apps.dynatrace.com` for the latest Dynatrace Platform.

Note: Replace with your environment ID and with your managed environment domain.

Provide the API Access Token you prepared earlier and optionally provide a label.

Set this as your current environment.

The add-on displays your environment in the list and will use the current environment for all API operations. Visit Environments to learn more about using the Environment view.

### Initialize your workspace

It's time to create your first project. If you need to open a different workspace folder, select Open folder. Otherwise, select the Initialize workspace button to start.

To learn how to use the Workspaces view, visit Extension 2.0 workspaces.

#### 1. Schema validation

The workflow starts with your target schema version. Choose any from the list. It ensures that we can validate your extension manifest while you're writing it, allowing you to spot any issues early on.

#### 2. Developer certificates

Extensions 2.0 use developer certificates for signing and packaging extensions. Choose Generate new ones to generate a new set of certificates kept in VS Code's storage.

TipCheck the extension's settings to get the exact path to where your credentials are stored.
The workflow offers some additional convenience steps:

Whether to use these certificates as defaults for all workspaces:

- This will update your global settings for Dynatrace Extensions to reflect this choice.

- As part of this guide, choose Yes.

Whether to upload the new CA certificate to the Dynatrace Credentials Vault.

- You need to provide a name and, optionally, a description.

- As part of this guide, choose Yes and provide the additional details.

Whether to upload the new CA certificate to locally installed OneAgents and ActiveGates.

- This step only appears if a local OneAgent or ActiveGate installation is detected.

- This step requires running VS Code with Administrator privileges.

- As part of this guide, choose No.

To learn how to use your existing developer certificates, visit Credentials.

#### 3. Project template

The final step of the workflow is to choose the type of project you want to start. It allows the extension to generate relevant files.

Since this is your first extension, choose Extension 2.0 ⭐ at this step.

This option is the default choice for new projects and will create the following starting setup:

- `extension` - the folder where all extension assets are placed.

- `extension/extension.yaml` - this is your extension's manifest file.

NoteTo learn more about the other types of projects, visit Project templates.
In addition, all templates also create the following folders and files:

- `.vscode` - a folder for storing workspace-specific VS Code settings.

- `dist` - a folder for storing all extension packages.

- `config` - a folder for storing your monitoring configuration files.

- `.gitignore` - a file containing useful rules for ignoring unnecessary items from your git repository.

### Make some changes to your extension

Start by opening up the extension manifest and making some changes. Give your extension a name, and add yourself as the author.

For example, update the `extension/extension.yaml` file with the following information:

extension/extension.yaml
`tsx
name: custom:my.first.extensionversion: "0.0.1"minDynatraceVersion: "1.265.0"author: name:
`

NoteReplace with the author's name.

### Publish your extension

Finally, perform the following steps to upload your extension to Dynatrace.

- Press the F1 key and choose the Dynatrace extensions: Build command. The workflow will build your extension, creating a package inside your `dist` folder.

- When prompted about uploading your extension to Dynatrace, choose Yes.

- When prompted about activating this extension version, choose Yes.

Congratulations. You created, built, uploaded, and activated your first Extension 2.0. You can view this in the Dynatrace UI by navigating to Extensions.

---

## dynatrace-extensions-vscode/guides/create_extension

`/develop/extensions/dynatrace-extensions-vscode/guides/create_extension/`

- Add-on for VS Code
- How-to guides
- Create a Python extension

## Create a Python extension

- How-to guide
- 8-min readDynatrace provides a means to develop Python extensions using the new Extensions 2.0 framework.
You should use these extensions when the existing data sources can't cover your use cases.

Develop Python extensions when:

- You need complex logic to fetch metrics, events, or logs from a source.

- You can't achieve data collection with a declarative data source (SQL, SNMP, WMI, JMX, Prometheus, etc).

The dt-extensions-sdk python package provides a Software Development Kit (SDK) and a Command Line Interface (CLI) delivering support for your Python extension.

Python extensions are also supported by our Visual Studio Code Add-on, our recommended way of developing them.

In this step-by-step guide, we will create a working `RabbitMQ` extension from scratch.

This extension will leverage the RabbitMQ Management API to bring metrics for the cluster, nodes, and queues.

### Requirements

You'll need the following:

- Visual Studio Code with the Extensions Add-On installed and configured.

- Python 3.10

- dt-extensions-sdk

- Dynatrace 1.286+

### Create a new extension

- Open an empty folder on Visual Studio Code.

- Run the command `Dynatrace extensions: Initialize workspace`.

- Choose the latest available schema version.

- Create a new certificate or use an existing one.

- Choose the project type `Python Extension 2.0`.

- Give the extension the name `rabbitmq_extension`.

Python extensions are simply Python modules that must follow the PEP8 naming conventions, meaning that the name should be lowercase and separated by underscores.

TipTo run a command on Visual Studio Code, press `F1` or `Ctrl+Shift+P` and type the command name.

Our Visual Studio Code extension will automatically invoke the `dt-sdk create` command, which will create the necessary files and folders for the extension.

If you open the file `extension/extension.yaml`, you can examine the construction of a Python extension.

It declares the Python module name, the minimum Python version, and the activation schema for a remote ActiveGate or local OneAgent extension.

Clicking the `Simulate extension` code lens will start the extension in the Visual Studio Code environment.

TipIf you don't see the `Simulate extension` button, reload the Visual Studio Code window with `F1 > Reload Window`.

### RabbitMQ

We suggest you use docker to test this extension against a real RabbitMQ broker.

You can start a RabbitMQ node with the management extension enabled by:

`tsx
docker run -d --name rabbit -p 15672:15672 rabbitmq:3-management
`

To make the extension more interesting, log in to `http://localhost:15672` with the default credentials `guest:guest` and create a new queue.

### Activation schema

We need to ask the user for three pieces of information when they're configuring our extension:

- RabbitMQ Management URL

- Username

- Password

You can define these in the `extension/activationSchema.json` file.
By default, the SDK creates this file with fields for a URL, Username, and Password, which is convenient for us.
You should modify this file to fit the specific needs of the extension for most use cases.

During development, the SDK reads these configuration values from the file `activation.json`. Modify this file to point to our local RabbitMQ instance.

`tsx
{ "enabled": true, "description": "rabbitmq_extension activation", "version": "0.0.1", "activationContext": "REMOTE", "pythonRemote": { "endpoints": [ { "url": "http://localhost:15672", "user": "guest", "password": "guest" } ] }}
`

TipYou can only use the `activation.json` during development, and it's not bundled with the extension. You must be careful not to commit secrets to your source control accidentally.

### Fetch the data

In this section, we will implement the `query` method of the extension. This method is called every minute and is responsible for fetching the data from the RabbitMQ instance.

#### Cluster level metrics

Let's start by reporting a metric for the number of queues in our RabbitMQ instance.

To do that, we can call the /api/overview endpoint.

We will also need to include `requests` as a dependency of our extension.

`tsx
from dynatrace_extension import Extension, Status, StatusValueimport requestsclass ExtensionImpl(Extension): def initialize(self): self.extension_name = "rabbitmq_extension" def query(self): """ The query method is automatically scheduled to run every minute """ self.logger.info("query method started for rabbitmq_extension.") for endpoint in self.activation_config["endpoints"]: url = endpoint["url"] user = endpoint["user"] password = endpoint["password"] self.logger.debug(f"Running endpoint with url '{url}'") # We've added these three lines # 1 - Make a request to the /api/overview endpoint cluster = requests.get(f"{url}/api/overview", auth=(user, password)).json() # 2 - Collect some dimensions for our metrics dimensions = { "cluster": cluster["cluster_name"], "rabbitmq_version": cluster["rabbitmq_version"] } # 3 - Send a metric to Dynatrace self.report_metric("rabbitmq.cluster.queues", cluster["object_totals"]["queues"], dimensions) self.logger.info("query method ended for rabbitmq_extension.") def fastcheck(self) -> Status: """ This is called when the extension runs for the first time. If this AG cannot run this extension, raise an Exception or return StatusValue.ERROR! """ return Status(StatusValue.OK)def main(): ExtensionImpl().run()if __name__ == '__main__': main()
`

To include requests as a dependency, add it to `install_requires` in `setup.py`:

`tsx
from setuptools import setup, find_packagessetup(name="rabbitmq_extension", version="0.0.1", description="Rabbitmq_extension python EF2 extension", author="Dynatrace", packages=find_packages(), python_requires=">=3.10", include_package_data=True, install_requires=["dt-extensions-sdk", "requests"], extras_require={"dev": ["dt-extensions-sdk[cli]"]}, )
`

TipDon't forget to also install the `requests` package in your development environment
with `pip install requests`
Running the extension should now show you a metric being collected:

`tsx
2024-02-29 21:42:56,099 [INFO] api (MainThread): send_metric: rabbitmq.cluster.queues,cluster="rabbit@49bf21ab3628",rabbitmq_version="3.12.12" gauge,1 1709264569592
`

For this tutorial, we won't add more metrics
but you can visit the RabbitMQ Management API
in your local instance and add more metrics to your extension.

#### Node level metrics

Adding metrics to the nodes of the RabbitMQ cluster is a similar process.

A cluster can have many nodes, so let's loop through them and report some metrics.

Add the following lines after reporting the `cluster` metric:

`tsx
# 4 - Get nodes nodes = requests.get(f"{url}/api/nodes", auth=(user, password)).json() for node in nodes: # 5 - Add node specific dimensions, including it's parent (the cluster) dimensions node_dimensions = { "node": node["name"], **dimensions } # 6 - Report a metric for each node self.report_metric("rabbitmq.node.mem_used", node["mem_used"], node_dimensions)
`

#### Queue level metrics

Finally, let's add some metrics for the queues in our RabbitMQ instance.

`tsx
# 7 - Get queues queues = requests.get(f"{url}/api/queues", auth=(user, password)).json() for queue in queues: # 8 - Add queue specific dimensions, including it's parent (the cluster) dimensions queue_dimensions = { "name": queue["name"], "node": queue["node"], "state": queue["state"], **dimensions } # 9 - Report a metric for each queue self.report_metric("rabbitmq.queue.messages", queue["messages"], queue_dimensions)
`

#### Final code

`tsx
from dynatrace_extension import Extension, Status, StatusValueimport requestsclass ExtensionImpl(Extension): def initialize(self): self.extension_name = "rabbitmq_extension" def query(self): """ The query method is automatically scheduled to run every minute """ self.logger.info("query method started for rabbitmq_extension.") for endpoint in self.activation_config["endpoints"]: url = endpoint["url"] user = endpoint["user"] password = endpoint["password"] self.logger.debug(f"Running endpoint with url '{url}'") # We've added these three lines # 1 - Make a request to the /api/overview endpoint cluster = requests.get(f"{url}/api/overview", auth=(user, password)).json() # 2 - Collect some dimensions for our metrics dimensions = { "cluster": cluster["cluster_name"], "rabbitmq_version": cluster["rabbitmq_version"] } # 3 - Send a metric to Dynatrace self.report_metric("rabbitmq.cluster.queues", cluster["object_totals"]["queues"], dimensions) # 4 - Get nodes nodes = requests.get(f"{url}/api/nodes", auth=(user, password)).json() for node in nodes: # 5 - Add node specific dimensions, including it's parent (the cluster) dimensions node_dimensions = { "node": node["name"], **dimensions } # 6 - Report a metric for each node self.report_metric("rabbitmq.node.mem_used", node["mem_used"], node_dimensions) # 7 - Get queues queues = requests.get(f"{url}/api/queues", auth=(user, password)).json() for queue in queues: # 8 - Add queue specific dimensions, including it's parent (the cluster) dimensions queue_dimensions = { "name": queue["name"], "node": queue["node"], "state": queue["state"], **dimensions } # 9 - Report a metric for each queue self.report_metric("rabbitmq.queue.messages", queue["messages"], queue_dimensions) self.logger.info("query method ended for rabbitmq_extension.") def fastcheck(self) -> Status: """ This is called when the extension runs for the first time. If this AG cannot run this extension, raise an Exception or return StatusValue.ERROR! """ return Status(StatusValue.OK)def main(): ExtensionImpl().run()if __name__ == '__main__': main()
`

TipYou should separate the `query` method into smaller methods.For the complete code you can visit our real RabbitMQ extension in Github
that includes dashboards, topology, screens, all metrics, and more.

### Build the extension

If you haven't done it yet, you can generate developer certificates using the
Visual Studio Code command
`Dynatrace extensions: Generate certificates`. For more information about this command,
visit the Generate certificates documentation.

To create the extension package, run the `Dynatrace extensions: Build` command.

This command will run the `dt-sdk build` command,
which will create the `custom_rabbitmq-extension-0.0.1.zip` file in the `dist` folder,
a signed extension file.
Dynatrace will only run extensions signed by a trusted certificate.

The Visual Studio Code extension will also prompt you to upload the extension
to your Dynatrace environment, a nice quality of life feature.

### Configure the extension

Navigate to Dynatrace and configure your extension.

You can use the Extensions app from the Hub,
or navigate to `Infrastructure Observability` and then to `Extensions`
to configure your extension.

CautionIt must trust your developer certificate to run this extension from an
ActiveGate or OneAgent.To find information on how to distribute it, visit Sign extensions documentation.

### Visualize data

For now, we're only sending metric data points to Dynatrace.

We can visualize these metrics via `Dashboards`, `Notebooks` or the `Metric Explorer`:

A full fledged extension would include dashboards, topology, screens, and more.
For the complete code example, visit RabbitMQ extension on GitHub.
For more information about extending Dynatrace, visit Extend Dynatrace documentaion.

---

## dynatrace-extensions-vscode/guides/migrate/jmx-conversion

`/develop/extensions/dynatrace-extensions-vscode/guides/migrate/jmx-conversion/`

- Add-on for VS Code
- How-to guides
- Migrate from EF 1.0
- JMX extensions

## JMX extensions

- How-to guide
- 4-min readThe Extensions Framework 2.0 for JMX has been available since version 1.213 and brings you new possibilities for visualizing and querying your data. Follow this guide to learn how to leverage Visual Studio Code to convert your 1.0 extensions to the new format automatically.

### Prerequisites

Complete the first-time setup for your editor

For simplicity, this guide will assume you have already configured your editor for first-time use. If you haven't used Dynatrace Extensions for VS Code before, follow our Getting started guide to complete your first-time setup.

NoteThis guide will assume you have access to developer credentials. If you followed the "Getting started" guide, store the generated credentials in VS Code's global settings - an example is shown here

Enable JMX 2.0 extensions in your environment

Go to Settings > Preferences > OneAgent features and enable Java Metric Extensions 2.0 (JMX), then restart your monitored Java processes.

### Convert a JMX Extension as a new project

#### Initialize your workspace

Create a new folder on your computer and open it in VS Code.

Press F1 then select the command Dynatrace extensions: Initialize workspace

Next, choose schema version 1.275.0 from the list

When prompted about certificates, choose Use existing

When prompted about project type, choose JMX 1.0 Conversion

Your workspace has been initialized, and you're ready to convert your old extension.

#### Convert your extension

You need to load the JMX 1.0 Extension for conversion. You can browse your local filesystem for a `.zip` or `plugin.json` file or browse your connected Dynatrace environment. As part of this guide, we'll do the latter. Choose to load it Remotely:

You are now presented with a list of extensions from your tenant. Choose which one you want to convert. For example:

NoteAfter selecting an extension, you may be prompted for a new extension name if your old one is too long.

Next, you should select a technology so that Process pages can be configured automatically. Choose one that applies to your Java process. Otherwise, choose All other

Optionally, we can also show the data on your Host's page. To follow along with this guide, select Yes

The conversion will generate your new extension manifest at `extension/extension.yaml`.

### Convert a JMX Extension standalone

If you don't want to initialize a new workspace for your project or you're already working within a registered workspace, you can run our automation as a standalone command.

Press F1 and select the command Dynatrace Extensions: Convert JMX. This workflow starts by first prompting you to load the extension and follows the same steps as mentioned above.

At the end, your new manifest will be placed in `extension/extension.yaml`, or you'll be prompted for a save destination if this folder doesn't exist in the currently opened workspace.

### Deploy and configure your new extension

#### Build and upload to Dynatrace

Build the extension by pressing F1 then clicking the command Dynatrace extensions: Build

Then, choose to upload it to Dynatrace by clicking Yes

Next, activate this extension by clicking Yes

#### Add a monitoring configuration

- Open your extension either from the prompt or from the Extensions menu in Dynatrace

- Add a monitoring configuration by clicking the button

- Select a Host running your Java process, then click Next step.

- On the next page click Next step once again, then add a description and click Activate.

Once your monitoring configuration is activated, data collection starts automatically.

### Find your extension's data

Open the details page of one of the hosts running your monitored Java process. You should see a card (towards the bottom) with a title starting with JMX Metrics.

From that card, select any of the processes listed. Then click `...` and choose Metrics and logs analysis.

On the page that opens, you'll have multiple cards from your extension.

NoteThe cards on the Process page are only added if you selected a technology during the conversion.

---

## dynatrace-extensions-vscode/guides/migrate/python-migrate

`/develop/extensions/dynatrace-extensions-vscode/guides/migrate/python-migrate/`

- Add-on for VS Code
- How-to guides
- Migrate from EF 1.0
- Python extensions

## Python extensions

- How-to guide
- 3-min read

### Requirements

- You have installed Python 3.10.

- You're running Dynatrace 1.286 version or later.

- You have `dt-extensions-sdk[cli]` installed and in your `PATH`.

TipCheck you've installed the dt-extensions-sdk in your `PATH` by running `dt-sdk --version` on your terminal.

### Steps

To migrate an existing Python EF1 extension using Visual Studio Code, follow these steps:

- Create a new EF2 extension.

- Import the EF1 extension using the `Dynatrace extensions: Convert Python` command.

- Convert the code, moving the class from the original extension to the new extension's `__main__.py` file.

#### Create a new EF2 extension

- Open an empty folder in Visual Studio Code, then run the `Dynatrace extensions: Initialize Workspace` command.

- Select the schema version (latest recommended) and the certificates you want to use to sign the extension.

- Choose the `Python Extension 2.0` project type.

- Give your extension a name; it must respect the Python module naming convention using all lowercase with optional underscores.

#### Import the existing EF1 extension

The first step is to convert the old `plugin.json` file to the new `activationSchema.json` format.
This automatically creates the Settings 2.0 UI for your extension, which defines the UI for the user to configure the extension.

Run the command `Dynatrace extensions: Convert Python`.
You can choose to import an existing Python extension from:

- The extension zip file

- The plugin.json file

- Your Dynatrace environment

In this example, we're importing from a Dynatrace environment, which gives you a list of all Python extensions in that environment.

If you would like to import from your computer, a file picker will open, and you can select your extension's ZIP file or plugin.json file.

After you select an extension, your `activationSchema.json` will be overwritten with the correct settings. You'll need to review that file to ensure your UI looks the way you want it to.

When importing a local OneAgent extension, delete the entry `activation > remote` from the `extension.yaml file`.

However, when importing a remote ActiveGate extension, delete `activation > local`.

TipYou can also make your extension work remotely and locally by keeping both entries and modifying the `activationSchema.json` file accordingly.

#### Change the extension code

Move your existing extension code to the `__main__.py` file of the new extension.
The easiest way to do this is by pasting the code from your existing extension class into the new `ExtensionImpl` class.

Here are the most significant changes you need to make to your code:

##### Code conversion reference

 |
 | Description | EF1 method | EF2 method | Notes
 | Logging | `self.logger.info("message")` | `self.logger.info("message")` | Stays the same
 | Obtaining user defined parameters | `self.config.get("param_name", "default_value")` | `self.activation_config.get("param_name", "default_value")` | You can find and replace all `self.config.` entries with `self.activation_config.`
 | Report an event | `self.results_builder.report_custom_info_event` | `self.report_dt_event` | Try to keep topology (groups, device, IDs) out of the code; this is defined later in the `extension.yaml` file.
 | Report a metric | `device.absolute("metric_key", metric_value, {"dimension_name": "dimension_value"})` | `self.report_metric("metric_key", metric_value, {"dimension_name": "dimension_value"})` | There is no concept of a `device` in the Python code anymore; send metrics directly.
 | Create groups and custom devices | `self.topology_builder.create_group`, `group.create_device` | `n/a` | Doesn't exist; topology is defined in the `extension.yaml` file.

#### Build and upload the extension

Build the extension by running the command `Dynatrace extensions: Build`.
If the build is successful, you'll see a prompt to upload the extension to your Dynatrace environment and activate it.
Accept both prompts.

Your extension is now uploaded to Dynatrace, and you can create monitoring configurations to start monitoring.

---

## dynatrace-extensions-vscode/settings

`/develop/extensions/dynatrace-extensions-vscode/settings/`

- Add-on for VS Code
- Settings

## Settings

- 4-min readYou can define all settings either globally or for each workspace.

NoteYou can learn more about accessing these settings in Visual Studio Code's official documentation.

### Credentials

Dynatrace Extensions can either generate all the credentials required for Extension 2.0 development or allow you to bring your own credential files.

#### When using your credentials

You need to provide your files by using these settings:

 |
 | Setting | Description
 | `dynatraceExtensions.developerCertkeyLocation` | This is the path to your developer credential file.
 | `dynatraceExtensions.rootOrCaCertificateLocation` | is the path to your root (CA) certificate.
Example usage:

./vscode/settings.json
`tsx
{ "dynatraceExtensions.developerCertkeyLocation": "C:\\Temp\\certificates\\dev.pem", "dynatraceExtensions.rootOrCaCertificateLocation": "C:\\Temp\\certificates\\ca.pem"}
`

#### When generating credentials

You can customize the details that are embedded into the generated certificates by using these settings:

 |
 | Setting | Default value | Description
 | `dynatraceExtensions.certificateCommonName` | Extension Developer | The certificate's common name (CN) attribute.
 | `dynatraceExtensions.certificateOrganization` | | The certificate's organization (O) attribute.
 | `dynatraceExtensions.certificateOrganizationUnit` | | The certificate's organization unit (OU) attribute.
 | `dynatraceExtensions.certificateStateOrProvince` | | The certificate's state or province (ST) attribute.
 | `dynatraceExtensions.certificateCountryCode` | | The certificate's country code (C) attribute.

### Behavior

The add-on aims to allow users to customize their extension development experience as much as possible. The following settings allow turning various features on or off on demand.

#### Features

 |
 | Setting | Default value | Description
 | `dynatraceExtensions.metricSelectorsCodeLens` | true | Metric selector code lens
 | `dynatraceExtensions.entitySelectorsCodeLens` | true | Entity selector code lens
 | `dynatraceExtensions.fastDevelopmentMode` | false | Fast development mode
 | `dynatraceExtensions.wmiCodeLens` | true | WMI queries code lens
 | `dynatraceExtensions.screenCodeLens` | true | Unified analysis screen code lens

#### Logging

 |
 | Setting | Default value | Description
 | `dynatraceExtensions.logging.level` | `INFO` | The minimum level of log messages
 | `dynatraceExtensions.logging.maxFiles` | 10 | The maximum number of log files (by age) kept on disk.
 | `dynatraceExtensions.logging.maxFileSize` | 10 | The maximum size of a single log file (in MB).

#### Tenant Connectivity Settings

The add-on always performs web requests to your Dynatrace environment over HTTPS. In specific scenarios—for example, in Dynatrace Managed—your environment may be accessible through a dedicated endpoint that uses either a custom-signed or a self-signed SSL certificate. While valid for encryption, most frameworks and browsers don't recognize these certificates as trusted, which causes requests to fail.

The `dynatraceExtensions.tenantConnectivitySettings` setting is only available from your `settings.json` file and represents an array of environment endpoints that require special settings for HTTPS connectivity. Each entry in the array is an object with the following details:

 |
 | Attribute | Default value | Description
 | `tenantUrl` | "" | The base URL to your Dynatrace environment. The add-on will use the URL to decide when to apply special connectivity settings on web requests.
 | `certificatePath` | "" | The path on disk to a Root/CA file in `.pem` or `.crt` format. The add-on will load this file and add it to the list of trusted CAs for the given `tenantUrl`.
 | `disableSSLVerification` | `false` | When enabled, the add-on ignores SSL certificates for the given `tenantUrl`. Enable this only when using self-signed certificates on your Dynatrace endpoint.
Example:

Adding a custom certificate to the trusted CAs:

settings.json
`tsx
"dynatraceExtensions.tenantConnectivitySettings": [ { "tenantUrl": "https://10.0.0.1:5555/e/my-tenant", "certificatePath": "C:\\Temp\\my_custom.crt" }]
`

Using a self-signed certificate on an endpoint:

settings.json
`tsx
"dynatraceExtensions.tenantConnectivitySettings": [ { "tenantUrl": "https://my.custom.endpoint/e/my-other-tenant", "disableSSLVerification": true }]
`

### Diagnostics

 |
 | Setting | Default value | Description
 | `dynatraceExtensions.diagnostics.all` | true | All diagnostics
 | `dynatraceExtensions.diagnostics.extensionName` | true | The name of the extension
 | `dynatraceExtensions.diagnostics.metricKeys` | true | Keys used for metric definitions
 | `dynatraceExtensions.diagnostics.cardKeys` | true | Keys of cards referenced/defined in the screens section
 | `dynatraceExtensions.diagnostics.snmp` | true | SNMP data source, especially the use of OIDs
TipLearn more about Dynatrace Extensions custom diagnostics.

### Python environment

The settings in this section allow you to customize the details of your virtual environment when working with Python extensions.

 |
 | Setting | Default value | Description
 | `dynatraceExtensions.pythonExtraPlatforms` | `[ "linux_x86_64", "win_amd64" ]` | A list of platforms to build Python packages for.

---

## dynatrace-extensions-vscode/specialized_views

`/develop/extensions/dynatrace-extensions-vscode/specialized_views/`

- Add-on for VS Code
- Specialized views

## Specialized views

- 2-min readDynatrace Extensions creates its entry in the VS Code activity bar. This entry provides two specialized views to help you manage Extension projects at scale and become more efficient.

You can easily find it by this icon:

### Extension 2.0 workspaces

This view is intended to help you keep track of all Extension 2.0 projects and their workspaces, no matter where they're stored on your filesystem. Each registered workspace is shown by its root folder name, and your currently opened workspace is shown in green, whereas others are in blue.

In this view, you can do the following:

- Use the plus button to register a new workspace.

- Use the refresh button to update the list.

Top-level items in this list represent your Extension projects. For each one, you can do the following:

- Use the folder button to open the associated workspace in the VS Code editor.

- Use the bin button to un-register the project. It'll not delete the workspace from your filesystem.

- Select the label to see the extension's name within that workspace, along with its version.

- Use the file button to open the extension's manifest for a quick look. It'll open in the same window.

This view lets you easily update some Dynatrace Extensions behavior settings associated with each workspace. You can do this by right-clicking on any registered workspace label.

### Environments

As its name implies, this view is focused on Dynatrace environments and your deployed extensions. Your currently connected Dynatrace environment is shown in green, while others are in blue.

In this view, you can do the following:

- Use the plus button to register a new environment.

- Use the refresh button to update the list.

Top-level items in this list are your registered Dynatrace environments. For each one, you can do the following:

- Use the pen button to change any details.

- Use the bin button to remove this environment.

- Select the label to expand a list of deployed extensions.

Children items to an environment are its deployed extensions. Select any extension to expand the list further and show the extension's monitoring configurations (the status is indicated next to its name). You can do the following:

- Use the plus button to create a new monitoring configuration.

- Use the pen button to make changes to a configuration.

- Use the bin button to delete the configuration.

- Use the file button to save this configuration to a file. It'll be saved in your workspace's `./config` folder.

---

## dynatrace-extensions-vscode/troubleshooting

`/develop/extensions/dynatrace-extensions-vscode/troubleshooting/`

- Add-on for VS Code
- Troubleshooting

## Troubleshooting

- 2-min readDynatrace Extensions runs as a NodeJS application within VS Code's runtime, coexisting with all other extensions installed in your editor. The application will always start along with your editor, regardless of whether you're working on an extensions project. This behavior makes for quite a complex environment that may not consistently execute normal features as planned.

Continue reading to see how you can troubleshoot when the extension isn't running as expected and how you can reach out if you need further support.

### Output channels

Most features in the extension are designed to use UI notifications or VS Code's output channels to give feedback when operations go wrong or can't continue.

You can access output channels from the bottom part of your editor. Simply select the Output tab and use the dropdown to the right. Two main channels are available for communicating error details:

- Dynatrace: A JSON formatted channel, which most features will use for sharing error details payloads.

- Dynatrace Fast Mode: This JSON formatted channel communicates build-related errors when Fast Development Mode is enabled.

Here's an example of the build command failing due to an invalid extension name:

### Logs

Beyond this, you can get more detailed information via the extension's logs. The extension posts its logs to a dedicated output channel called Dynatrace Log. Unlike the other two output channels, this channel will format the data as a log and provide timestamps for every message.

You can set the verbosity of the messages posted to this channel in your editor's global settings. Find the Behavior section and adjust the log level as you see fit.

#### Collect a log archive

The extension also maintains execution logs on disk, which have debug-level verbosity. Dynatrace Extensions offers a command for packaging up the internal logs folder and saving it in a dedicated location. To run this command, press F1, then choose Download support archive.

TipYou can adjust the logs file aging mechanism from settings

### Support

This project is open source and community-driven. If you need help with any feature or you've found a bug, reach out by opening an issue on GitHub.

When reporting bugs, use our Bug template and describe your issue as clearly as possible. Include details such as your operating system and the version of the extension, and attach any relevant files or snippets of YAML.

When requesting help with features, you can begin by opening a blank issue. Describe what you're trying to achieve, where things aren't going as expected, and use the help wanted label.

In either case, attach a log archive.

---

## extensions

`/develop/extensions/`

## Extensions

- 1-min read

###

#### About Extensions
Introduction to ingesting data into Dynatrace with ExtensionsExplanation

#### Add-on for VS Code
Introduction to the Dynatrace Extensions add-on for VS CodeExplanation
