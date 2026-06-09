# @dynatrace-sdk/automation-utils

Source: <https://developer.dynatrace.com/develop/sdks/automation-utils/v2/> (latest: `automation-utils/v2`).

## automation-utils/v2

`/develop/sdks/automation-utils/v2/`

- SDK for TypeScript
- Automation Utils
- V2

## Automation Utils
Utility functions for accessing AutomationEngine APIs from the Run JavaScript action.

 @dynatrace-sdk/automation-utils v2.5.0 

`tsx
npm install @dynatrace-sdk/automation-utils
`

### Functions

#### actionExecution

actionExecution(id?): PromiseRequired scope: automation:workflows:readRetrieves the action execution details for the current workflow.
Available for executions of workflows type standard only (simple workflow executions will result in 404)

##### Parameters
 |
 | Name | Type | Description
 | id | string | The ID of the action execution to retrieve. If not provided, the ID from the caller service metadata is used.

##### Returns
 |
 | Description
 | The action execution details.Code example
`tsx
// To get current action execution detailimport { actionExecution } from '@dynatrace-sdk/automation-utils';const actionExe = await actionExecution();
`
Code example
`tsx
// To get loopItem from current action executionimport { actionExecution } from '@dynatrace-sdk/automation-utils';const actionExe = await actionExecution();const loopItem = actionExe.loopItem;// orconst { loopItem } = actionExe;
`

#### execution

execution(id?): PromiseIExecution>Required scope: automation:workflows:readRetrieves the execution details for the current workflow.
Available for executions of workflows type standard only (simple workflow executions will result in 404)

##### Parameters
 |
 | Name | Type | Description
 | id | string | The ID of the execution to retrieve. If not provided, the ID from the caller service metadata is used.

##### Returns
 |
 | Description
 | The execution details.Code example
`tsx
// To get current execution detailimport { execution } from '@dynatrace-sdk/automation-utils';const exe = await execution();
`
Code example
`tsx
// To get event context from current executionimport { execution } from '@dynatrace-sdk/automation-utils';const exe = await execution();const eventContext = exe.event();
`
Code example
`tsx
// To get current task execution resultimport { execution } from '@dynatrace-sdk/automation-utils';const exe = await execution();const result = await exe.result();
`

#### getExecutionLink

getExecutionLink(): null | string

##### Returns
 |
 | Description
 | The link to a workflow execution, or `null` if called within a simple workflow or outside a workflow.

#### getTaskExecutionLink

getTaskExecutionLink(): null | string

##### Returns
 |
 | Description
 | The link to a workflow execution, including the currently executed task name, or `null` if called within a simple workflow or outside a workflow.

#### getWorkflowLink

getWorkflowLink(): null | string

##### Returns
 |
 | Description
 | The link to a workflow, or `null` if called outside a workflow.

#### result

result(predecessorTaskName): Promiseany>Required scope: automation:workflows:readRetrieves the result of a task execution in the current workflow.

##### Parameters
 |
 | Name | Type | Description
 | predecessorTaskName*required | string | The name of the predecessor task.

##### Returns
 |
 | Description
 | The result of the predecessor task execution.Code example
`tsx
//To get a predecessor task execution's resultimport { result } from '@dynatrace-sdk/automation-utils';const taskExecutionResult = await result('predecessor_task_1');
`

### Constants

#### actionExecutionId

ID of the running action execution.
string

#### executionId

ID of the running execution.
string

#### taskName

Name of the running task.
string

#### workflowId

ID of the running workflow.
string

### Types

#### IExecution

Extended execution type.
Adds helper methods to the base Execution:

- IExecution.result—retrieve the result of a task execution.

- IExecution.event—get the event payload context of the execution.

##### Properties

 |
 | Name | Type | Description
 | actor*required | string |
 | endedAt | null | Date |
 | eventTrigger | null | string |
 | id*required | string |
 | input | ExecutionInput |
 | isDraft | boolean |
 | params | ExecutionParams |
 | parentExecution*required | null | string |
 | parentTaskName*required | null | string | Parent task execution's name (subworkflows only)
 | providedInput | null | ExecutionProvidedInput |
 | rootExecution | null | string |
 | rootWorkflow | null | string |
 | runtime*required | number | Calculate the runtime of an execution in seconds. If the execution is not ended, runtime is calculated until now.
 | schedule | null | string |
 | startedAt | Date |
 | state*required | "ERROR" | "RUNNING" | "SUCCESS" | "UNKNOWN" | "PAUSED" | "CANCELLED" |
 | stateInfo | null | string |
 | title*required | string |
 | trigger | null | string |
 | triggerType*required | "Manual" | "Schedule" | "Event" | "Workflow" |
 | triggerTypeDetail | TriggerTypeDetail |
 | user | null | string |
 | workflow*required | string | Executed Workflow
 | workflowType*required | "STANDARD" | "SIMPLE" |
 | workflowVersion*required | null | number |

##### Methods

###### event

event(): null | Recordstring | string>Required scope: automation:workflows:readReturns the event context payload associated with the execution.

##### Returns
 |
 | Description
 | A key-value object if event data is available, otherwise `null`.Code example
`tsx
import { execution } from '@dynatrace-sdk/automation-utils';const exe = await execution();const eventContext = exe.event();
`

###### result

result(taskId): Promiseany>Required scope: automation:workflows:readRetrieves the result of a task execution.

##### Parameters
 |
 | Name | Type | Description
 | taskId*required | string | The ID of the task whose result should be retrieved.

##### Returns
 |
 | Description
 | A promise resolving with the task execution result.Code example
`tsx
import { execution } from '@dynatrace-sdk/automation-utils';const exe = await execution();const result = await exe.result("task-id");
`
