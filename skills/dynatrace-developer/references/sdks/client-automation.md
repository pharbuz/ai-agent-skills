# @dynatrace-sdk/client-automation

Source: <https://developer.dynatrace.com/develop/sdks/client-automation/v8/> (latest: `client-automation/v8`).

> Truncated — this SDK's auto-generated reference is large. Key exports/usage are below; see the full reference at the URL above.

## client-automation/v8

`/develop/sdks/client-automation/v8/`

- SDK for TypeScript
- Automation
- V8

## Automation
Manage and run workflows with the AutomationEngine API.

 @dynatrace-sdk/client-automation v8.3.0 

`tsx
npm install @dynatrace-sdk/client-automation
`

### actionExecutionsClient

`tsx
import { actionExecutionsClient } from '@dynatrace-sdk/client-automation';
`

#### getActionExecution

actionExecutionsClient.getActionExecution(config): PromiseActionExecution>Required scope: automation:workflows:read

##### Parameters
 |
 | Name | Type | Description
 | config.adminAccess | boolean | Allow access to all workflows/executions - additionally requires automation:workflows:admin
 | config.id*required | string | A UUID string identifying this action execution.

##### Returns
 |
 | Return type | Status code | Description
 | ActionExecution | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { actionExecutionsClient } from "@dynatrace-sdk/client-automation";const data = await actionExecutionsClient.getActionExecution({ id: "...", });
`

#### getActionExecutionLog

actionExecutionsClient.getActionExecutionLog(config): Promisestring>Required scope: automation:workflows:readReturns the log output of a specific ActionExecution.

##### Parameters
 |
 | Name | Type | Description
 | config.adminAccess | boolean | Allow access to all workflows/executions - additionally requires automation:workflows:admin
 | config.id*required | string | A UUID string identifying this action execution.

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { actionExecutionsClient } from "@dynatrace-sdk/client-automation";const data = await actionExecutionsClient.getActionExecutionLog({ id: "...", });
`

### actionsSampleResultClient

`tsx
import { actionsSampleResultClient } from '@dynatrace-sdk/client-automation';
`

#### getActionSampleResult

⚠️ Deprecated

actionsSampleResultClient.getActionSampleResult(config): Promiseany>Required scope: automation:workflows:read

##### Parameters
 |
 | Name | Type
 | config.actionIdentifier*required | string

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { actionsSampleResultClient } from "@dynatrace-sdk/client-automation";const data = await actionsSampleResultClient.getActionSampleResult({ actionIdentifier: "...", });
`

### businessCalendarsClient

`tsx
import { businessCalendarsClient } from '@dynatrace-sdk/client-automation';
`

#### createBusinessCalendar

businessCalendarsClient.createBusinessCalendar(config): PromiseBusinessCalendarResponse>Required scope: automation:calendars:write

##### Parameters
 |
 | Name | Type
 | config.body*required | BusinessCalendarCreate

##### Returns
 |
 | Return type | Status code | Description
 | BusinessCalendarResponse | 201 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { businessCalendarsClient } from "@dynatrace-sdk/client-automation";const data = await businessCalendarsClient.createBusinessCalendar({ body: { title: "..." }, });
`

#### deleteBusinessCalendar

businessCalendarsClient.deleteBusinessCalendar(config): PromiseRequired scope: automation:calendars:write

##### Parameters
 |
 | Name | Type | Description
 | config.id*required | string | A UUID string identifying this business calendar.

##### Returns
 |
 | Return type | Status code | Description
 | void | 204 | No response body

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { businessCalendarsClient } from "@dynatrace-sdk/client-automation";const data = await businessCalendarsClient.deleteBusinessCalendar({ id: "...", });
`

#### duplicateBusinessCalendar

businessCalendarsClient.duplicateBusinessCalendar(config): PromiseBusinessCalendarResponse>Required scope: automation:calendars:write

##### Parameters
 |
 | Name | Type | Description
 | config.body*required | DuplicationRequest |
 | config.id*required | string | A UUID string identifying this business calendar.

##### Returns
 |
 | Return type | Status code | Description
 | BusinessCalendarResponse | 201 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { businessCalendarsClient } from "@dynatrace-sdk/client-automation";const data = await businessCalendarsClient.duplicateBusinessCalendar({ id: "...", body: {}, });
`

#### getBusinessCalendar

businessCalendarsClient.getBusinessCalendar(config): PromiseBusinessCalendarResponse>Required scope: automation:calendars:read

##### Parameters
 |
 | Name | Type | Description
 | config.id*required | string | A UUID string identifying this business calendar.

##### Returns
 |
 | Return type | Status code | Description
 | BusinessCalendarResponse | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { businessCalendarsClient } from "@dynatrace-sdk/client-automation";const data = await businessCalendarsClient.getBusinessCalendar({ id: "...", });
`

#### getBusinessCalendarHistoryRecord

businessCalendarsClient.getBusinessCalendarHistoryRecord(config): PromiseBusinessCalendarResponse>Required scope: automation:calendars:read

##### Parameters
 |
 | Name | Type | Description
 | config.id*required | string | A UUID string identifying this business calendar.
 | config.version*required | string | Pattern: `^[\d]+$`

##### Returns
 |
 | Return type | Status code | Description
 | BusinessCalendarResponse | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { businessCalendarsClient } from "@dynatrace-sdk/client-automation";const data = await businessCalendarsClient.getBusinessCalendarHistoryRecord( { id: "...", version: "..." }, );
`

#### getBusinessCalendarHistoryRecords

businessCalendarsClient.getBusinessCalendarHistoryRecords(config): PromisePaginatedChangeHistory>Required scope: automation:calendars:read

##### Parameters
 |
 | Name | Type | Description
 | config.all | boolean | When false, the latest historical record is not returned.
 | config.id*required | string | A UUID string identifying this business calendar.

##### Returns
 |
 | Return type | Status code | Description
 | PaginatedChangeHistory | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { businessCalendarsClient } from "@dynatrace-sdk/client-automation";const data = await businessCalendarsClient.getBusinessCalendarHistoryRecords( { id: "..." }, );
`

#### getBusinessCalendars

businessCalendarsClient.getBusinessCalendars(config): PromisePaginatedBusinessCalendarResponseList>Required scope: automation:calendars:read

##### Parameters
 |
 | Name | Type | Description
 | config.limit | number | Number of results to return per page.
 | config.offset | number | The initial index from which to return the results.
 | config.ordering | string | Which field to use when ordering the results.
 | config.search | string | A search term.

##### Returns
 |
 | Return type | Status code | Description
 | PaginatedBusinessCalendarResponseList | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { businessCalendarsClient } from "@dynatrace-sdk/client-automation";const data = await businessCalendarsClient.getBusinessCalendars();
`

#### patchBusinessCalendar

businessCalendarsClient.patchBusinessCalendar(config): PromiseBusinessCalendarResponse>Required scope: automation:calendars:write

##### Parameters
 |
 | Name | Type | Description
 | config.body*required | BusinessCalendarUpdate |
 | config.id*required | string | A UUID string identifying this business calendar.

##### Returns
 |
 | Return type | Status code | Description
 | BusinessCalendarResponse | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { businessCalendarsClient } from "@dynatrace-sdk/client-automation";const data = await businessCalendarsClient.patchBusinessCalendar({ id: "...", body: {}, });
`

#### restoreBusinessCalendarHistoryRecord

businessCalendarsClient.restoreBusinessCalendarHistoryRecord(config): PromiseRequired scope: automation:calendars:write

##### Parameters
 |
 | Name | Type | Description
 | config.id*required | string | A UUID string identifying this business calendar.
 | config.version*required | string | Pattern: `^[\d]+$`

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 | No response body

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { businessCalendarsClient } from "@dynatrace-sdk/client-automation";const data = await businessCalendarsClient.restoreBusinessCalendarHistoryRecord( { id: "...", version: "..." }, );
`

#### updateBusinessCalendar

businessCalendarsClient.updateBusinessCalendar(config): PromiseBusinessCalendarResponse>Required scope: automation:calendars:write

##### Parameters
 |
 | Name | Type | Description
 | config.body*required | BusinessCalendarUpdate |
 | config.id*required | string | A UUID string identifying this business calendar.

##### Returns
 |
 | Return type | Status code | Description
 | BusinessCalendarResponse | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { businessCalendarsClient } from "@dynatrace-sdk/client-automation";const data = await businessCalendarsClient.updateBusinessCalendar({ id: "...", body: {}, });
`

### eventTriggersClient

`tsx
import { eventTriggersClient } from '@dynatrace-sdk/client-automation';
`

#### previewFilter

⚠️ Deprecated

eventTriggersClient.previewFilter(config): PromiseEventTriggerPreviewResponse>Required scope: automation:workflows:read

##### Parameters
 |
 | Name | Type
 | config.body*required | EventTriggerPreviewRequest

##### Returns
 |
 | Return type | Status code | Description
 | EventTriggerPreviewResponse | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { eventTriggersClient } from "@dynatrace-sdk/client-automation";const data = await eventTriggersClient.previewFilter({ body: { triggerConfiguration: { type: "event", value: { query: "..." }, }, },});
`

### executionsClient

`tsx
import { executionsClient } from '@dynatrace-sdk/client-automation';
`

#### cancelExecution

executionsClient.cancelExecution(config): PromiseRequired scope: automation:workflows:runTries to cancel an Execution.
Can only be done, if the Execution is in an active state.

##### Parameters
 |
 | Name | Type | Description
 | config.adminAccess | boolean | Allow access to all workflows/executions - additionally requires automation:workflows:admin
 | config.id*required | string | A UUID string identifying this execution.

##### Returns
 |
 | Return type | Status code | Description
 | void | 204 | No response body

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { executionsClient } from "@dynatrace-sdk/client-automation";const data = await executionsClient.cancelExecution({ id: "...",});
`

#### cancelTaskExecution

executionsClient.cancelTaskExecution(config): PromiseRequired scope: automation:workflows:runCancels task execution.
Canceling action executions cause the task to be cancelled, which
causes the workflow to be canceled.

##### Parameters
 |
 | Name | Type | Description
 | config.adminAccess | boolean | Allow access to all workflows/executions - additionally requires automation:workflows:admin
 | config.executionId*required | string |
 | config.id*required | string | Task name

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 | No response body

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { executionsClient } from "@dynatrace-sdk/client-automation";const data = await executionsClient.cancelTaskExecution({ executionId: "...", id: "...",});
`

#### getAllEventLogs

executionsClient.getAllEventLogs(config): PromiseEventLogs>Required scope: automation:workflows:readGet all event logs

##### Parameters
 |
 | Name | Type | Description
 | config.adminAccess | boolean | Allow access to all workflows/executions - additionally requires automation:workflows:admin
 | config.id*required | string | A UUID string identifying this execution.

##### Returns
 |
 | Return type | Status code | Description
 | EventLogs | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { executionsClient } from "@dynatrace-sdk/client-automation";const data = await executionsClient.getAllEventLogs({ id: "...",});
`

#### getExecution

executionsClient.getExecution(config): PromiseExecution>Required scope: automation:workflows:readGet execution

##### Parameters
 |
 | Name | Type | Description
 | config.adminAccess | boolean | Allow access to all workflows/executions - additionally requires automation:workflows:admin
 | config.id*required | string | A UUID string identifying this execution.

##### Returns
 |
 | Return type | Status code | Description
 | Execution | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { executionsClient } from "@dynatrace-sdk/client-automation";const data = await executionsClient.getExecution({ id: "...",});
`

#### getExecutionActions

executionsClient.getExecutionActions(config): Promisestring>>Required scope: automation:workflows:readReturn list of actions assigned to tasks in a given Execution.

##### Parameters
 |
 | Name | Type | Description
 | config.adminAccess | boolean | Allow access to all workflows/executions - additionally requires automation:workflows:admin
 | config.id*required | string | A UUID string identifying this execution.

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { executionsClient } from "@dynatrace-sdk/client-automation";const data = await executionsClient.getExecutionActions({ id: "...",});
`

#### getExecutionLog

executionsClient.getExecutionLog(config): Promisestring>Required scope: automation:workflows:readGets the execution log

##### Parameters
 |
 | Name | Type | Description
 | config.adminAccess | boolean | Allow access to all workflows/executions - additionally requires automation:workflows:admin
 | config.id*required | string | A UUID string identifying this execution.

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { executionsClient } from "@dynatrace-sdk/client-automation";const data = await executionsClient.getExecutionLog({ id: "...",});
`

#### getExecutions

executionsClient.getExecutions(config): PromisePaginatedExecutionList>Required scope: automation:workflows:readGet list of executions (executions of draft and simple workflows aren't included in the response).

##### Parameters
 |
 | Name | Type | Description
 | config.adminAccess | boolean | Allow access to all workflows/executions - additionally requires automation:workflows:admin
 | config.limit | number | Number of results to return per page.
 | config.offset | number | The initial index from which to return the results.
 | config.ordering | string | Which field to use when ordering the results.
 | config.parentExecution | string |
 | config.parentWorkflow | string |
 | config.schedule | Arraystring> | Multiple values may be separated by commas.
 | config.search | string | A search term.
 | config.startedAtGte | string |
 | config.startedAtLte | string |
 | config.state | Arraystring> | Multiple values may be separated by commas.
 | config.subworkflowOfTask | string | Filter executions by `parentExecution/task`.
 | config.trigger | string |
 | config.triggerType | string |
 | config.user | Arraystring> | Multiple values may be separated by commas.
 | config.workflow | Arraystring> | Multiple values may be separated by commas.

##### Returns
 |
 | Return type | Status code | Description
 | PaginatedExecutionList | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { executionsClient } from "@dynatrace-sdk/client-automation";const data = await executionsClient.getExecutions();
`

#### getTaskExecution

executionsClient.getTaskExecution(config): PromiseTaskExecution>Required scope: automation:workflows:read

##### Parameters
 |
 | Name | Type | Description
 | config.adminAccess | boolean | Allow access to all workflows/executions - additionally requires automation:workflows:admin
 | config.executionId*required | string |
 | config.id*required | string | Task name

##### Returns
 |
 | Return type | Status code | Description
 | TaskExecution | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { executionsClient } from "@dynatrace-sdk/client-automation";const data = await executionsClient.getTaskExecution({ executionId: "...", id: "...",});
`

#### getTaskExecutionInput

executionsClient.getTaskExecutionInput(config): Promiseany>Required scope: automation:workflows:readReturns merged inputs from all ActionExecutions belonging to the TaskExecution.

##### Parameters
 |
 | Name | Type | Description
 | config.adminAccess | boolean | Allow access to all workflows/executions - additionally requires automation:workflows:admin
 | config.executionId*required | string |
 | config.id*required | string | Task name

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { executionsClient } from "@dynatrace-sdk/client-automation";const data = await executionsClient.getTaskExecutionInput({ executionId: "...", id: "...",});
`

#### getTaskExecutionLog

executionsClient.getTaskExecutionLog(config): Promisestring>Required scope: automation:workflows:readReturns the log output of a specific task.
This can be large as its the STDOUT of the Action
as defined by the user.

##### Parameters
 |
 | Name | Type | Description
 | config.adminAccess | boolean | Allow access to all workflows/executions - additionally requires automation:workflows:admin
 | config.executionId*required | string |
 | config.id*required | string | Task name

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { executionsClient } from "@dynatrace-sdk/client-automation";const data = await executionsClient.getTaskExecutionLog({ executionId: "...", id: "...",});
`

#### getTaskExecutionResult

executionsClient.getTaskExecutionResult(config): Promiseany>Required scope: automation:workflows:readReturns merged results from all ActionExecutions belonging to the TaskExecution.

##### Parameters
 |
 | Name | Type | Description
 | config.adminAccess | boolean | Allow access to all workflows/executions - additionally requires automation:workflows:admin
 | config.executionId*required | string |
 | config.id*required | string | Task name

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { executionsClient } from "@dynatrace-sdk/client-automation";const data = await executionsClient.getTaskExecutionResult({ executionId: "...", id: "...",});
`

#### getTaskExecutions

executionsClient.getTaskExecutions(config): PromiseTaskExecutions>Required scope: automation:workflows:read

##### Parameters
 |
 | Name | Type | Description
 | config.adminAccess | boolean | Allow access to all workflows/executions - additionally requires automation:workflows:admin
 | config.executionId*required | string |

##### Returns
 |
 | Return type | Status code | Description
 | TaskExecutions | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { executionsClient } from "@dynatrace-sdk/client-automation";const data = await executionsClient.getTaskExecutions({ executionId: "...",});
`

#### getTransitions

executionsClient.getTransitions(config): PromiseTaskTransitions>Required scope: automation:workflows:read

##### Parameters
 |
 | Name | Type | Description
 | config.adminAccess | boolean | Allow access to all workflows/executions - additionally requires automation:workflows:admin
 | config.executionId*required | string |

##### Returns
 |
 | Return type | Status code | Description
 | TaskTransitions | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { executionsClient } from "@dynatrace-sdk/client-automation";const data = await executionsClient.getTransitions({ executionId: "...",});
`

#### pauseExecution

executionsClient.pauseExecution(config): PromiseRequired scope: automation:workflows:runPauses an Execution.
Can only be done, if the Execution is in an active state.

##### Parameters
 |
 | Name | Type | Description
 | config.adminAccess | boolean | Allow access to all workflows/executions - additionally requires automation:workflows:admin
 | config.id*required | string | A UUID string identifying this execution.

##### Returns
 |
 | Return type | Status code | Description
 | void | 204 | No response body

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { executionsClient } from "@dynatrace-sdk/client-automation";const data = await executionsClient.pauseExecution({ id: "...",});
`

#### resumeExecution

executionsClient.resumeExecution(config): PromiseRequired scope: automation:workflows:runResumes an Execution.
Can only be done, if the Execution is in an inactive state.

##### Parameters
 |
 | Name | Type | Description
 | config.adminAccess | boolean | Allow access to all workflows/executions - additionally requires automation:workflows:admin
 | config.id*required | string | A UUID string identifying this execution.

##### Returns
 |
 | Return type | Status code | Description
 | void | 204 | No response body

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { executionsClient } from "@dynatrace-sdk/client-automation";const data = await executionsClient.resumeExecution({ id: "...",});
`

### schedulesClient

`tsx
import { schedulesClient } from '@dynatrace-sdk/client-automation';
`

#### getCountries

schedulesClient.getCountries(config): PromiseCountryList>Required scope: automation:workflows:readReturns the list of countries that can be used to look up the holiday calendar

##### Returns
 |
 | Return type | Status code | Description
 | CountryList | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { schedulesClient } from "@dynatrace-sdk/client-automation";const data = await schedulesClient.getCountries();
`

#### getHolidayCalendar

schedulesClient.getHolidayCalendar(config): PromiseHolidayCalendarList>Required scope: automation:workflows:read

##### Parameters
 |
 | Name | Type | Description
 | config.from | string | From date in ISO format
 | config.key*required | string | The country name
 | config.to | string | To date in ISO format

##### Returns
 |
 | Return type | Status code | Description
 | HolidayCalendarList | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { schedulesClient } from "@dynatrace-sdk/client-automation";const data = await schedulesClient.getHolidayCalendar({ key: "...",});
`

#### getTimezones

schedulesClient.getTimezones(config): Promisestring>>Required scope: automation:workflows:read

##### Returns
 |
 | Return type | Status code | Description
 | void | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { schedulesClient } from "@dynatrace-sdk/client-automation";const data = await schedulesClient.getTimezones();
`

#### previewSchedule

⚠️ Deprecated

schedulesClient.previewSchedule(config): PromiseSchedulePreviewResponse>Required scope: automation:workflows:read

##### Parameters
 |
 | Name | Type
 | config.body*required | SchedulePreviewRequest

##### Returns
 |
 | Return type | Status code | Description
 | SchedulePreviewResponse | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { schedulesClient } from "@dynatrace-sdk/client-automation";const data = await schedulesClient.previewSchedule({ body: { schedule: { trigger: { type: "cron", cron: "0 0 * * *" }, }, },});
`

### schedulingRulesClient

`tsx
import { schedulingRulesClient } from '@dynatrace-sdk/client-automation';
`

#### createRule

schedulingRulesClient.createRule(config): PromiseRule>Required scope: automation:rules:write

##### Parameters
 |
 | Name | Type
 | config.body*required | RuleCreate

##### Returns
 |
 | Return type | Status code | Description
 | Rule | 201 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { schedulingRulesClient } from "@dynatrace-sdk/client-automation";const data = await schedulingRulesClient.createRule({ body: { title: "...", ruleType: "rrule" },});
`

#### deleteRule

schedulingRulesClient.deleteRule(config): PromiseRequired scope: automation:rules:write

##### Parameters
 |
 | Name | Type | Description
 | config.id*required | string | A UUID string identifying this rule.

##### Returns
 |
 | Return type | Status code | Description
 | void | 204 | No response body

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { schedulingRulesClient } from "@dynatrace-sdk/client-automation";const data = await schedulingRulesClient.deleteRule({ id: "...",});
`

#### duplicateRule

schedulingRulesClient.duplicateRule(config): PromiseRule>Required scope: automation:rules:write

##### Parameters
 |
 | Name | Type | Description
 | config.body*required | DuplicationRequest |
 | config.id*required | string | A UUID string identifying this rule.

##### Returns
 |
 | Return type | Status code | Description
 | Rule | 201 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { schedulingRulesClient } from "@dynatrace-sdk/client-automation";const data = await schedulingRulesClient.duplicateRule({ id: "...", body: {},});
`

#### getRule

schedulingRulesClient.getRule(config): PromiseRule>Required scope: automation:rules:read

##### Parameters
 |
 | Name | Type | Description
 | config.id*required | string | A UUID string identifying this rule.

##### Returns
 |
 | Return type | Status code | Description
 | Rule | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { schedulingRulesClient } from "@dynatrace-sdk/client-automation";const data = await schedulingRulesClient.getRule({ id: "...",});
`

#### getRuleHistoryRecord

schedulingRulesClient.getRuleHistoryRecord(config): PromiseRule>Required scope: automation:rules:read

##### Parameters
 |
 | Name | Type | Description
 | config.id*required | string | A UUID string identifying this rule.
 | config.version*required | string | Pattern: `^[\d]+$`

##### Returns
 |
 | Return type | Status code | Description
 | Rule | 200 |

##### Throws
 |
 | Error Type | Error Message
 | ErrorEnvelopeError | Code example
`tsx
import { schedulingRulesClient } from "@dynatrace-sdk/client-automation";const data = await schedulingRulesClient.getRuleHistoryRecord({ id: "...", version: "...", });
`

#### getRuleHistoryRecords

schedulingRulesClient.getRuleHistoryRecords(config): PromisePaginatedChangeHistory>Required scope: automation:rules:read

