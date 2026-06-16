# Filters

Strato design-system components in the **Filters** group. Source: <https://developer.dynatrace.com/design/components/>.

Import from `@dynatrace/strato-components` (or `.../strato-components-preview` for preview components). Each section lists the component, its doc path, an overview, and its props.

> Note: prop **Type** values may be partial or empty here — the doc site renders
> full TypeScript types client-side, so static capture misses some. Names, defaults,
> and descriptions are reliable; for exact types open the linked live page.

## FilterBar

`/design/components/filters/FilterBar/`

FilterBar helps users easily filter datasets using one or more filter criteria.
A range of form elements can be added as filter controls.

### Import

`tsx
import { FilterBar } from '@dynatrace/strato-components/filters';
`

### Demo

`FilterBar` is designed for filtering with multiple controls. This example shows
a `FilterBar` with a `TextInput`, a single `Select`, a multi-select `Select`,
and a `TimeframeSelector`. See Usage for best practices.

```tsx
import { useState } from 'react';

import type { Timeframe } from '@dynatrace/strato-components/core';
import {
  FilterBar,
  TimeframeSelector,
} from '@dynatrace/strato-components/filters';
import { Select, TextInput } from '@dynatrace/strato-components/forms';

const owners = [
  'Brandy Barrett',
  'Cleveland Allison',
  'Dora Braun',
  'Lacy Houston',
  'Patrick Gamble',
];

const MultipleFilters = () => {
  const defaultFilterState = {
    lastRun: {
      value: {
        from: {
          value: 'now()@d',
          type: 'expression',
        },
        to: {
          value: 'now()',
          type: 'expression',
        },
      } as Timeframe,
    },
  };
  const [lastRun, setLastRun] = useState<Timeframe | null>(
    defaultFilterState.lastRun.value
  );

  return (
    <FilterBar
      onFilterChange={() => {
        /* Insert filtering logic here */
      }}
    >
      <FilterBar.Item name="text" label="Keyword">
        <TextInput />
      </FilterBar.Item>
      <FilterBar.Item name="owner" label="Owner">
        <Select name="owner" id="owner-select" clearable>
          <Select.Content>
            {owners.map((owner) => (
              <Select.Option key={owner} value={owner}>
                {owner}
              </Select.Option>
            ))}
          </Select.Content>
        </Select>
      </FilterBar.Item>
      <FilterBar.Item name="lastRun" label="Last run">
        <TimeframeSelector value={lastRun} onChange={setLastRun} />
      </FilterBar.Item>
    </FilterBar>
  );
};
```

```tsx
import { useState } from 'react';

import type { Timeframe } from '@dynatrace/strato-components/core';
import {
  FilterBar,
  TimeframeSelector,
} from '@dynatrace/strato-components/filters';
import { Select, TextInput } from '@dynatrace/strato-components/forms';

const owners = [
  'Brandy Barrett',
  'Cleveland Allison',
  'Dora Braun',
  'Lacy Houston',
  'Patrick Gamble',
];

const MultipleFilters = () => {
  const defaultFilterState = {
    lastRun: {
      value: {
        from: {
          value: 'now()@d',
          type: 'expression',
        },
        to: {
          value: 'now()',
          type: 'expression',
        },
      } as Timeframe,
    },
  };
  const [lastRun, setLastRun] = useState<Timeframe | null>(
    defaultFilterState.lastRun.value
  );

  return (
    <FilterBar
      onFilterChange={() => {
        /* Insert filtering logic here */
      }}
    >
      <FilterBar.Item name="text" label="Keyword">
        <TextInput />
      </FilterBar.Item>
      <FilterBar.Item name="owner" label="Owner">
        <Select name="owner" id="owner-select" clearable>
          <Select.Content>
            {owners.map((owner) => (
              <Select.Option key={owner} value={owner}>
                {owner}
              </Select.Option>
            ))}
          </Select.Content>
        </Select>
      </FilterBar.Item>
      <FilterBar.Item name="lastRun" label="Last run">
        <TimeframeSelector value={lastRun} onChange={setLastRun} />
      </FilterBar.Item>
    </FilterBar>
  );
};
```


### Give items unique names

The name provided to the `FilterBar.Item` must be unique to initialize the
`defaultValue` correctly. This is true even if the item is rendered
conditionally. If the same `name` is used for two items, React will map the
`name` of the new item to the old `defaultValue`.

`tsx
{conditionalFilter ? ( ) : ( )}
`

```tsx
{conditionalFilter ? (
          <FilterBar.Item name="conditional-keyword" label="Keyword">
            <TextInput defaultValue='Automation' />
          </FilterBar.Item>
        ) : (
          <FilterBar.Item name="conditional-owner" label="Owner">
            <TextInput defaultValue="Dora Braun" />
          </FilterBar.Item>
        )}
```

```tsx
{conditionalFilter ? (
          <FilterBar.Item name="conditional-keyword" label="Keyword">
            <TextInput defaultValue='Automation' />
          </FilterBar.Item>
        ) : (
          <FilterBar.Item name="conditional-owner" label="Owner">
            <TextInput defaultValue="Dora Braun" />
          </FilterBar.Item>
        )}
```


### Filter text

Use the `SearchInput` within the `FilterBar` for searching accross fields (e.g.,
multiple columns). Only one `SearchInput` should be used per `FilterBar`. Use
the `TextInput` for targeted, text-based filtering (e.g., for one specific
column). This allows users to narrow down results by entering keywords or
phrases.

```tsx
import { FilterBar } from '@dynatrace/strato-components/filters';
import { TextInput, SearchInput } from '@dynatrace/strato-components/forms';

const SimpleText = () => {
  return (
    <FilterBar
      onFilterChange={() => {
        /* Insert your filtering logic here */
      }}
    >
      <FilterBar.Item name="search-filter" label="Search accross fields">
        <SearchInput placeholder="Filter" />
      </FilterBar.Item>
      <FilterBar.Item name="text-filter" label="Filter column">
        <TextInput />
      </FilterBar.Item>
    </FilterBar>
  );
};
```

```tsx
import { FilterBar } from '@dynatrace/strato-components/filters';
import { TextInput, SearchInput } from '@dynatrace/strato-components/forms';

const SimpleText = () => {
  return (
    <FilterBar
      onFilterChange={() => {
        /* Insert your filtering logic here */
      }}
    >
      <FilterBar.Item name="search-filter" label="Search accross fields">
        <SearchInput placeholder="Filter" />
      </FilterBar.Item>
      <FilterBar.Item name="text-filter" label="Filter column">
        <TextInput />
      </FilterBar.Item>
    </FilterBar>
  );
};
```


### Reset filter values

This example shows how to reset filter item values in controlled scenarios. The
`FilterBar.ResetButton` depends on an `onClick` hander to reset the filter
values. Therefore, the reset button can only be used with controlled `FilterBar`
components.

```tsx
import { useState } from 'react';

import type { Timeframe } from '@dynatrace/strato-components/core';
import {
  FilterBar,
  FilterItemValues,
  TimeframeSelector,
} from '@dynatrace/strato-components/filters';
import { Select, TextInput } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import { Code, Text } from '@dynatrace/strato-components/typography';

const ResetValues = () => {
  const defaultFilterState = {
    lastRun: {
      value: {
        from: {
          value: 'now()@d',
          type: 'expression',
        },
        to: {
          value: 'now()',
          type: 'expression',
        },
      } as Timeframe,
    },
  };

  const [filterItemValues, setFilterItemValues] =
    useState<FilterItemValues | null>(null);

  const handleFilterChange = (filterItemValues: FilterItemValues) => {
    setFilterItemValues(filterItemValues);
  };
  const [text, setText] = useState<string | undefined>();
  const [owner, setOwner] = useState<string | null>();
  const [lastRun, setLastRun] = useState<Timeframe | null>(
    defaultFilterState.lastRun.value
  );
  const handleReset = () => {
    setText(undefined);
    setOwner(null);
    setLastRun(defaultFilterState.lastRun.value);
    handleFilterChange(defaultFilterState);
  };
  const owners = [
    'Brandy Barrett',
    'Cleveland Allison',
    'Dora Braun',
    'Lacy Houston',
    'Patrick Gamble',
  ];

  return (
    <Flex flexDirection="column">
      <Flex gap={4} alignItems="flex-end">
        <FilterBar onFilterChange={handleFilterChange}>
          <FilterBar.Item name="text" label="Keyword">
            <TextInput
              value={text}
              onChange={setText}
              data-testid="filter-text"
            />
          </FilterBar.Item>
          <FilterBar.Item name="owner" label="Owner">
            <Select
              name="owner"
              id="owner-select"
              value={owner}
              onChange={setOwner}
              clearable
            >
              <Select.Content>
                {owners.map((owner) => (
                  <Select.Option key={owner} value={owner}>
                    {owner}
                  </Select.Option>
                ))}
              </Select.Content>
            </Select>
          </FilterBar.Item>
          <FilterBar.Item name="lastRun" label="Last run">
            <TimeframeSelector value={lastRun} onChange={setLastRun} />
          </FilterBar.Item>
          <FilterBar.ResetButton onClick={handleReset} />
        </FilterBar>
      </Flex>
      <Text>
        Filter values on change: <Code>{JSON.stringify(filterItemValues)}</Code>
      </Text>
    </Flex>
  );
};
```

```tsx
import { useState } from 'react';

import type { Timeframe } from '@dynatrace/strato-components/core';
import {
  FilterBar,
  FilterItemValues,
  TimeframeSelector,
} from '@dynatrace/strato-components/filters';
import { Select, TextInput } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import { Code, Text } from '@dynatrace/strato-components/typography';

const ResetValues = () => {
  const defaultFilterState = {
    lastRun: {
      value: {
        from: {
          value: 'now()@d',
          type: 'expression',
        },
        to: {
          value: 'now()',
          type: 'expression',
        },
      } as Timeframe,
    },
  };

  const [filterItemValues, setFilterItemValues] =
    useState<FilterItemValues | null>(null);

  const handleFilterChange = (filterItemValues: FilterItemValues) => {
    setFilterItemValues(filterItemValues);
  };
  const [text, setText] = useState<string | undefined>();
  const [owner, setOwner] = useState<string | null>();
  const [lastRun, setLastRun] = useState<Timeframe | null>(
    defaultFilterState.lastRun.value
  );
  const handleReset = () => {
    setText(undefined);
    setOwner(null);
    setLastRun(defaultFilterState.lastRun.value);
    handleFilterChange(defaultFilterState);
  };
  const owners = [
    'Brandy Barrett',
    'Cleveland Allison',
    'Dora Braun',
    'Lacy Houston',
    'Patrick Gamble',
  ];

  return (
    <Flex flexDirection="column">
      <Flex gap={4} alignItems="flex-end">
        <FilterBar onFilterChange={handleFilterChange}>
          <FilterBar.Item name="text" label="Keyword">
            <TextInput
              value={text}
              onChange={setText}
              data-testid="filter-text"
            />
          </FilterBar.Item>
          <FilterBar.Item name="owner" label="Owner">
            <Select
              name="owner"
              id="owner-select"
              value={owner}
              onChange={setOwner}
              clearable
            >
              <Select.Content>
                {owners.map((owner) => (
                  <Select.Option key={owner} value={owner}>
                    {owner}
                  </Select.Option>
                ))}
              </Select.Content>
            </Select>
          </FilterBar.Item>
          <FilterBar.Item name="lastRun" label="Last run">
            <TimeframeSelector value={lastRun} onChange={setLastRun} />
          </FilterBar.Item>
          <FilterBar.ResetButton onClick={handleReset} />
        </FilterBar>
      </Flex>
      <Text>
        Filter values on change: <Code>{JSON.stringify(filterItemValues)}</Code>
      </Text>
    </Flex>
  );
};
```


### Prefill additional filters

If you know the most likely value for an additional, or secondary, filter, you
can help users by setting it as the `defaultValue`.

The user can override the `defaultValue`, but if the filter is removed and
reapplied, it will revert to the `defaultValue`.

To make the changed value persist, the `value` property should be used instead.
In this way, the changed value is saved, even if the filter is removed. (The
`value` is no longer considered for the filtering.)

```tsx
<Flex flexDirection="column">
  <FilterBar
    onFilterChange={handleFilterChange}
    defaultPinnedState={{
      owner: 'pinned-optional',
      lastRun: 'optional',
    }}
  >
    <FilterBar.Item name="keyword" label="Keyword">
      <TextInput defaultValue="Automation" />
    </FilterBar.Item>
    <FilterBar.Item name="owner" label="Owner">
      <Select
        name="owner"
        id="owner-select"
        defaultValue="Dora Braun"
        clearable
      >
        <Select.Content>
          {owners.map((owner) => (
            <Select.Option key={owner} value={owner}>
              {owner}
            </Select.Option>
          ))}
        </Select.Content>
      </Select>
    </FilterBar.Item>
    <FilterBar.Item name="lastRun" label="Last run">
      <TimeframeSelector defaultValue={defaultFilterState.lastRun.value} />
    </FilterBar.Item>
  </FilterBar>
  <Text>
    Filter values on change: <Code>{JSON.stringify(filterItemValues)}</Code>
  </Text>
</Flex>
```

```tsx
<Flex flexDirection="column">
  <FilterBar
    onFilterChange={handleFilterChange}
    defaultPinnedState={{
      owner: 'pinned-optional',
      lastRun: 'optional',
    }}
  >
    <FilterBar.Item name="keyword" label="Keyword">
      <TextInput defaultValue="Automation" />
    </FilterBar.Item>
    <FilterBar.Item name="owner" label="Owner">
      <Select
        name="owner"
        id="owner-select"
        defaultValue="Dora Braun"
        clearable
      >
        <Select.Content>
          {owners.map((owner) => (
            <Select.Option key={owner} value={owner}>
              {owner}
            </Select.Option>
          ))}
        </Select.Content>
      </Select>
    </FilterBar.Item>
    <FilterBar.Item name="lastRun" label="Last run">
      <TimeframeSelector defaultValue={defaultFilterState.lastRun.value} />
    </FilterBar.Item>
  </FilterBar>
  <Text>
    Filter values on change: <Code>{JSON.stringify(filterItemValues)}</Code>
  </Text>
</Flex>
```


### Render filtered data in a table

Connect `FilterBar` with `DataTable` with the `useFilteredData` hook. To filter
the data in the table, pass the unfiltered data as the first argument to the
hook. The `useFilteredData` hook returns the `filteredData` that must be passed
to the table's `data` prop along with the `onChange` handler which can be
plugged into the `onFilterChange` callback.

By default, the filter name must match the column name. If a custom filter logic
is required, provide a filter function as the second argument. This example
shows a custom filter function that searches for a match in every column of a
row.

```tsx
import {
  FilterBar,
  FilterItemValues,
} from '@dynatrace/strato-components/filters';
import { SearchInput } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import {
  DataTable,
  useFilteredData,
} from '@dynatrace/strato-components/tables';

const columns = [
  {
    header: 'Name',
    accessor: 'name',
    id: 'name',
  },
  {
    header: 'Owner',
    accessor: 'owner',
    id: 'owner',
  },
  {
    header: 'Last run',
    accessor: 'lastRun',
    id: 'lastRun',
  },
  {
    header: 'Type',
    accessor: 'type',
    id: 'type',
  },
];
type Data = {
  name: string;
  owner: string;
  lastRun: Date;
  type: string;
};
const data: Data[] = [
  {
    name: 'OutageMonitor',
    owner: 'Brandy Barrett',
    lastRun: new Date('2025-08-13T10:15:00Z'),
    type: 'Event',
  },
  {
    name: 'HeartbeatCheck',
    owner: 'Cleveland Allison',
    lastRun: new Date('2025-08-12T14:30:00Z'),
    type: 'Schedule',
  },
  {
    name: 'DailySweep',
    owner: 'Dora Braun',
    lastRun: new Date('2025-08-11T09:45:00Z'),
    type: 'Schedule',
  },
  {
    name: 'AlertResponder',
    owner: 'Lacy Houston',
    lastRun: new Date('2025-08-10T16:00:00Z'),
    type: 'Event',
  },
  {
    name: 'SmartRestart',
    owner: 'Patrick Gamble',
    lastRun: new Date('2025-08-09T11:20:00Z'),
    type: 'Manual',
  },
  {
    name: 'RecoveryFlow',
    owner: 'Brandy Barrett',
    lastRun: new Date('2025-08-08T08:10:00Z'),
    type: 'Event',
  },
  {
    name: 'MetricWatch',
    owner: 'Cleveland Allison',
    lastRun: new Date('2025-08-07T13:50:00Z'),
    type: 'Schedule',
  },
  {
    name: 'AnomalyCatcher',
    owner: 'Dora Braun',
    lastRun: new Date('2025-08-06T17:25:00Z'),
    type: 'Event',
  },
  {
    name: 'IncidentRadar',
    owner: 'Lacy Houston',
    lastRun: new Date('2025-08-05T12:40:00Z'),
    type: 'Event',
  },
  {
    name: 'ForecastBot',
    owner: 'Patrick Gamble',
    lastRun: new Date('2025-08-04T15:05:00Z'),
    type: 'Schedule',
  },
  {
    name: 'EventTrigger',
    owner: 'Brandy Barrett',
    lastRun: new Date('2025-08-03T07:55:00Z'),
    type: 'Event',
  },
];

const TableFilter = () => {
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  function filterFn(filters: FilterItemValues, entry: any): boolean {
    return Object.keys(filters).every((filterName) =>
      Object.values(entry)
        .join()
        .toLowerCase()
        .includes((filters[filterName].value as string).toLowerCase())
    );
  }

  const { onChange, filteredData } = useFilteredData<Data>(data, filterFn);

  return (
    <Flex gap={8} flexDirection="column" height={400}>
      <DataTable columns={columns} data={filteredData}>
        <DataTable.TableActions>
          <FilterBar onFilterChange={onChange}>
            <FilterBar.Item name="filterItem" label="Filter all columns">
              <SearchInput />
            </FilterBar.Item>
          </FilterBar>
        </DataTable.TableActions>
      </DataTable>
    </Flex>
  );
};
```

```tsx
import {
  FilterBar,
  FilterItemValues,
} from '@dynatrace/strato-components/filters';
import { SearchInput } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import {
  DataTable,
  useFilteredData,
} from '@dynatrace/strato-components/tables';

const columns = [
  {
    header: 'Name',
    accessor: 'name',
    id: 'name',
  },
  {
    header: 'Owner',
    accessor: 'owner',
    id: 'owner',
  },
  {
    header: 'Last run',
    accessor: 'lastRun',
    id: 'lastRun',
  },
  {
    header: 'Type',
    accessor: 'type',
    id: 'type',
  },
];
type Data = {
  name: string;
  owner: string;
  lastRun: Date;
  type: string;
};
const data: Data[] = [
  {
    name: 'OutageMonitor',
    owner: 'Brandy Barrett',
    lastRun: new Date('2025-08-13T10:15:00Z'),
    type: 'Event',
  },
  {
    name: 'HeartbeatCheck',
    owner: 'Cleveland Allison',
    lastRun: new Date('2025-08-12T14:30:00Z'),
    type: 'Schedule',
  },
  {
    name: 'DailySweep',
    owner: 'Dora Braun',
    lastRun: new Date('2025-08-11T09:45:00Z'),
    type: 'Schedule',
  },
  {
    name: 'AlertResponder',
    owner: 'Lacy Houston',
    lastRun: new Date('2025-08-10T16:00:00Z'),
    type: 'Event',
  },
  {
    name: 'SmartRestart',
    owner: 'Patrick Gamble',
    lastRun: new Date('2025-08-09T11:20:00Z'),
    type: 'Manual',
  },
  {
    name: 'RecoveryFlow',
    owner: 'Brandy Barrett',
    lastRun: new Date('2025-08-08T08:10:00Z'),
    type: 'Event',
  },
  {
    name: 'MetricWatch',
    owner: 'Cleveland Allison',
    lastRun: new Date('2025-08-07T13:50:00Z'),
    type: 'Schedule',
  },
  {
    name: 'AnomalyCatcher',
    owner: 'Dora Braun',
    lastRun: new Date('2025-08-06T17:25:00Z'),
    type: 'Event',
  },
  {
    name: 'IncidentRadar',
    owner: 'Lacy Houston',
    lastRun: new Date('2025-08-05T12:40:00Z'),
    type: 'Event',
  },
  {
    name: 'ForecastBot',
    owner: 'Patrick Gamble',
    lastRun: new Date('2025-08-04T15:05:00Z'),
    type: 'Schedule',
  },
  {
    name: 'EventTrigger',
    owner: 'Brandy Barrett',
    lastRun: new Date('2025-08-03T07:55:00Z'),
    type: 'Event',
  },
];

const TableFilter = () => {
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  function filterFn(filters: FilterItemValues, entry: any): boolean {
    return Object.keys(filters).every((filterName) =>
      Object.values(entry)
        .join()
        .toLowerCase()
        .includes((filters[filterName].value as string).toLowerCase())
    );
  }

  const { onChange, filteredData } = useFilteredData<Data>(data, filterFn);

  return (
    <Flex gap={8} flexDirection="column" height={400}>
      <DataTable columns={columns} data={filteredData}>
        <DataTable.TableActions>
          <FilterBar onFilterChange={onChange}>
            <FilterBar.Item name="filterItem" label="Filter all columns">
              <SearchInput />
            </FilterBar.Item>
          </FilterBar>
        </DataTable.TableActions>
      </DataTable>
    </Flex>
  );
};
```


### Persist sorting of filtered data

When using the `useFilteredData` hook to filter table data, the table must
re-render each time the `filteredData` changes, which also resets the sorting.
To keep the sorting, use the `sortBy` and `onSortChange` props along with
`enableDefaultSort`.

```tsx
import { useState } from 'react';

import { FilterBar } from '@dynatrace/strato-components/filters';
import { SearchInput } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import {
  DataTable,
  useFilteredData,
} from '@dynatrace/strato-components/tables';

const columns = [
  {
    header: 'Name',
    accessor: 'name',
    id: 'name',
  },
  {
    header: 'Owner',
    accessor: 'owner',
    id: 'owner',
  },
  {
    header: 'Last run',
    accessor: 'lastRun',
    id: 'lastRun',
  },
  {
    header: 'Type',
    accessor: 'type',
    id: 'type',
  },
];
type Data = {
  name: string;
  owner: string;
  lastRun: Date;
  type: string;
};
const data: Data[] = [
  {
    name: 'OutageMonitor',
    owner: 'Brandy Barrett',
    lastRun: new Date('2025-08-13T10:15:00Z'),
    type: 'Event',
  },
  {
    name: 'HeartbeatCheck',
    owner: 'Cleveland Allison',
    lastRun: new Date('2025-08-12T14:30:00Z'),
    type: 'Schedule',
  },
  {
    name: 'DailySweep',
    owner: 'Dora Braun',
    lastRun: new Date('2025-08-11T09:45:00Z'),
    type: 'Schedule',
  },
  {
    name: 'AlertResponder',
    owner: 'Lacy Houston',
    lastRun: new Date('2025-08-10T16:00:00Z'),
    type: 'Event',
  },
  {
    name: 'SmartRestart',
    owner: 'Patrick Gamble',
    lastRun: new Date('2025-08-09T11:20:00Z'),
    type: 'Manual',
  },
  {
    name: 'RecoveryFlow',
    owner: 'Brandy Barrett',
    lastRun: new Date('2025-08-08T08:10:00Z'),
    type: 'Event',
  },
  {
    name: 'MetricWatch',
    owner: 'Cleveland Allison',
    lastRun: new Date('2025-08-07T13:50:00Z'),
    type: 'Schedule',
  },
  {
    name: 'AnomalyCatcher',
    owner: 'Dora Braun',
    lastRun: new Date('2025-08-06T17:25:00Z'),
    type: 'Event',
  },
  {
    name: 'IncidentRadar',
    owner: 'Lacy Houston',
    lastRun: new Date('2025-08-05T12:40:00Z'),
    type: 'Event',
  },
  {
    name: 'ForecastBot',
    owner: 'Patrick Gamble',
    lastRun: new Date('2025-08-04T15:05:00Z'),
    type: 'Schedule',
  },
  {
    name: 'EventTrigger',
    owner: 'Brandy Barrett',
    lastRun: new Date('2025-08-03T07:55:00Z'),
    type: 'Event',
  },
];

const TableFilterSorting = () => {
  const [sort, setSort] = useState([{ id: 'name', desc: true }]);
  const { onChange, filteredData } = useFilteredData<Data>(data);

  return (
    <Flex gap={8} flexDirection="column" height={400}>
      <DataTable
        columns={columns}
        data={filteredData}
        sortable
        sortBy={sort}
        onSortByChange={setSort}
      >
        <DataTable.TableActions>
          <FilterBar onFilterChange={onChange}>
            <FilterBar.Item name="owner" label="Filter by owner">
              <SearchInput />
            </FilterBar.Item>
          </FilterBar>
        </DataTable.TableActions>
      </DataTable>
    </Flex>
  );
};
```

```tsx
import { useState } from 'react';

import { FilterBar } from '@dynatrace/strato-components/filters';
import { SearchInput } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import {
  DataTable,
  useFilteredData,
} from '@dynatrace/strato-components/tables';

const columns = [
  {
    header: 'Name',
    accessor: 'name',
    id: 'name',
  },
  {
    header: 'Owner',
    accessor: 'owner',
    id: 'owner',
  },
  {
    header: 'Last run',
    accessor: 'lastRun',
    id: 'lastRun',
  },
  {
    header: 'Type',
    accessor: 'type',
    id: 'type',
  },
];
type Data = {
  name: string;
  owner: string;
  lastRun: Date;
  type: string;
};
const data: Data[] = [
  {
    name: 'OutageMonitor',
    owner: 'Brandy Barrett',
    lastRun: new Date('2025-08-13T10:15:00Z'),
    type: 'Event',
  },
  {
    name: 'HeartbeatCheck',
    owner: 'Cleveland Allison',
    lastRun: new Date('2025-08-12T14:30:00Z'),
    type: 'Schedule',
  },
  {
    name: 'DailySweep',
    owner: 'Dora Braun',
    lastRun: new Date('2025-08-11T09:45:00Z'),
    type: 'Schedule',
  },
  {
    name: 'AlertResponder',
    owner: 'Lacy Houston',
    lastRun: new Date('2025-08-10T16:00:00Z'),
    type: 'Event',
  },
  {
    name: 'SmartRestart',
    owner: 'Patrick Gamble',
    lastRun: new Date('2025-08-09T11:20:00Z'),
    type: 'Manual',
  },
  {
    name: 'RecoveryFlow',
    owner: 'Brandy Barrett',
    lastRun: new Date('2025-08-08T08:10:00Z'),
    type: 'Event',
  },
  {
    name: 'MetricWatch',
    owner: 'Cleveland Allison',
    lastRun: new Date('2025-08-07T13:50:00Z'),
    type: 'Schedule',
  },
  {
    name: 'AnomalyCatcher',
    owner: 'Dora Braun',
    lastRun: new Date('2025-08-06T17:25:00Z'),
    type: 'Event',
  },
  {
    name: 'IncidentRadar',
    owner: 'Lacy Houston',
    lastRun: new Date('2025-08-05T12:40:00Z'),
    type: 'Event',
  },
  {
    name: 'ForecastBot',
    owner: 'Patrick Gamble',
    lastRun: new Date('2025-08-04T15:05:00Z'),
    type: 'Schedule',
  },
  {
    name: 'EventTrigger',
    owner: 'Brandy Barrett',
    lastRun: new Date('2025-08-03T07:55:00Z'),
    type: 'Event',
  },
];

const TableFilterSorting = () => {
  const [sort, setSort] = useState([{ id: 'name', desc: true }]);
  const { onChange, filteredData } = useFilteredData<Data>(data);

  return (
    <Flex gap={8} flexDirection="column" height={400}>
      <DataTable
        columns={columns}
        data={filteredData}
        sortable
        sortBy={sort}
        onSortByChange={setSort}
      >
        <DataTable.TableActions>
          <FilterBar onFilterChange={onChange}>
            <FilterBar.Item name="owner" label="Filter by owner">
              <SearchInput />
            </FilterBar.Item>
          </FilterBar>
        </DataTable.TableActions>
      </DataTable>
    </Flex>
  );
};
```


### Filter sub-row data

The `useFilteredData` hook can also handle filtering of table data with
sub-rows.

By default, on the matching paths, the sibling rows are also displayed for easy
comparison. In other words, when a child matches, other children at the same
level are also included (on all levels of the matching path). Control this
behavior using the `subrowMatchingBehavior` parameter, to include or exclude
those sibling rows.

For nodes which match, all of their sub-rows are included irrespective of
`subrowMatchingBehavior`.

The return value `expandedRowIds` provides all the IDs of ancestors of matching
nodes. Feed those values to `openSubRows` of the `DataTable` to ensure matching
nodes are visible.

```tsx
import {
  randFullName,
  randPastDate,
  randVehicleModel,
  seed,
} from '@ngneat/falso';
import { useEffect, useState } from 'react';

import {
  FilterBar,
  type FilterItemValues,
} from '@dynatrace/strato-components/filters';
import { SearchInput } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import {
  DataTable,
  useFilteredData,
} from '@dynatrace/strato-components/tables';

const columns = [
  {
    header: 'Name',
    accessor: 'name',
    id: 'name',
  },
  {
    header: 'Owner',
    accessor: 'owner',
    id: 'owner',
  },
  {
    header: 'Last run',
    accessor: 'lastRun',
    id: 'lastRun',
    columnType: 'datetime',
    formatter: { dateStyle: 'short' },
  },
  {
    header: 'Type',
    accessor: 'type',
    id: 'type',
  },
];
type Data = {
  id: string;
  name: string;
  owner: string;
  lastRun: Date;
  type: string;
  subRows?: Data[];
};

const types = ['Event', 'Schedule', 'Manual'];

seed('1234');

const generateData = (depth = 0, maxDepth = 6): Data[] => {
  const itemCount = depth === 0 ? 6 : 2;
  return Array.from({ length: itemCount }, (_, i) => {
    const name = randVehicleModel();
    const data: Data = {
      id: `${name.toLowerCase()}-${depth}-${i}`,
      name,
      owner: randFullName(),
      lastRun: randPastDate({ years: 0.1 }),
      type: types[Math.floor(Math.random() * types.length)],
    };

    if (depth < maxDepth) {
      data.subRows = generateData(depth + 1, maxDepth);
    }

    return data;
  });
};

const data: Data[] = generateData();

const TableFilterSubRows = () => {
  const [ready, setReady] = useState<boolean>(false); // keep all rows collapsed initially
  const { filteredData, onChange, expandedRowIds } = useFilteredData(data);
  const [openSubRows, setOpenSubRows] = useState<Record<string, boolean>>({});

  useEffect(() => {
    if (ready && expandedRowIds) {
      const toExpand: Record<string, boolean> = Object.fromEntries(
        expandedRowIds.map((id: string): [string, boolean] => [id, true])
      );
      setOpenSubRows(toExpand);
    }
  }, [ready, expandedRowIds]);

  const handleOnFilterChange = (value: FilterItemValues) => {
    setReady(true);
    onChange(value);
  };

  return (
    <Flex gap={8} flexDirection="column" height={400}>
      <DataTable
        columns={columns}
        data={filteredData}
        subRows
        openSubRows={openSubRows}
        onOpenSubRowsChange={setOpenSubRows}
        rowId={(row) => row.id}
      >
        <DataTable.TableActions>
          <FilterBar onFilterChange={handleOnFilterChange}>
            <FilterBar.Item name="name" label="Filter by name">
              <SearchInput />
            </FilterBar.Item>
          </FilterBar>
        </DataTable.TableActions>
      </DataTable>
    </Flex>
  );
};
```

```tsx
import {
  randFullName,
  randPastDate,
  randVehicleModel,
  seed,
} from '@ngneat/falso';
import { useEffect, useState } from 'react';

import {
  FilterBar,
  type FilterItemValues,
} from '@dynatrace/strato-components/filters';
import { SearchInput } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import {
  DataTable,
  useFilteredData,
} from '@dynatrace/strato-components/tables';

const columns = [
  {
    header: 'Name',
    accessor: 'name',
    id: 'name',
  },
  {
    header: 'Owner',
    accessor: 'owner',
    id: 'owner',
  },
  {
    header: 'Last run',
    accessor: 'lastRun',
    id: 'lastRun',
    columnType: 'datetime',
    formatter: { dateStyle: 'short' },
  },
  {
    header: 'Type',
    accessor: 'type',
    id: 'type',
  },
];
type Data = {
  id: string;
  name: string;
  owner: string;
  lastRun: Date;
  type: string;
  subRows?: Data[];
};

const types = ['Event', 'Schedule', 'Manual'];

seed('1234');

const generateData = (depth = 0, maxDepth = 6): Data[] => {
  const itemCount = depth === 0 ? 6 : 2;
  return Array.from({ length: itemCount }, (_, i) => {
    const name = randVehicleModel();
    const data: Data = {
      id: `${name.toLowerCase()}-${depth}-${i}`,
      name,
      owner: randFullName(),
      lastRun: randPastDate({ years: 0.1 }),
      type: types[Math.floor(Math.random() * types.length)],
    };

    if (depth < maxDepth) {
      data.subRows = generateData(depth + 1, maxDepth);
    }

    return data;
  });
};

const data: Data[] = generateData();

const TableFilterSubRows = () => {
  const [ready, setReady] = useState<boolean>(false); // keep all rows collapsed initially
  const { filteredData, onChange, expandedRowIds } = useFilteredData(data);
  const [openSubRows, setOpenSubRows] = useState<Record<string, boolean>>({});

  useEffect(() => {
    if (ready && expandedRowIds) {
      const toExpand: Record<string, boolean> = Object.fromEntries(
        expandedRowIds.map((id: string): [string, boolean] => [id, true])
      );
      setOpenSubRows(toExpand);
    }
  }, [ready, expandedRowIds]);

  const handleOnFilterChange = (value: FilterItemValues) => {
    setReady(true);
    onChange(value);
  };

  return (
    <Flex gap={8} flexDirection="column" height={400}>
      <DataTable
        columns={columns}
        data={filteredData}
        subRows
        openSubRows={openSubRows}
        onOpenSubRowsChange={setOpenSubRows}
        rowId={(row) => row.id}
      >
        <DataTable.TableActions>
          <FilterBar onFilterChange={handleOnFilterChange}>
            <FilterBar.Item name="name" label="Filter by name">
              <SearchInput />
            </FilterBar.Item>
          </FilterBar>
        </DataTable.TableActions>
      </DataTable>
    </Flex>
  );
};
```


### Pin and unpin optional filters

Important filters should always be visible. However, you can allow users to hide
uncommon, optional filters in the 'Add filter' dropdown. Pass the configuration
object `defaultPinnedState` to the `FilterBar` to set filter states, as follows:

`pinned` items are always visible and can't be unpinned or hidden by the user.

`pinned-optional` items are visible initially, but the user can unpin and hide
them in the dropdown.

`optional` items aren't visible initially, but the user can access them from
the dropdown and pin them. When a filter item is pinned, it's automatically
focused.

Filter items that aren't configured will default to `pinned`.

Dropdown items use the text content of the label, stripping away all other
content. Be sure to add an aria-label or name for each pinned-optional and
optional filter, as these are required for the dropdown. If there's no text
content, the `aria-label` or the `name` will be used as a fallback.

```tsx
import { useState } from 'react';

import {
  FilterBar,
  FilterItemValues,
  TimeframeSelector,
} from '@dynatrace/strato-components/filters';
import { Select, TextInput } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import { Code, Text } from '@dynatrace/strato-components/typography';

const owners = [
  'Brandy Barrett',
  'Cleveland Allison',
  'Dora Braun',
  'Lacy Houston',
  'Patrick Gamble',
];

const AdditionalFilters = () => {
  const [filterItemValues, setFilterItemValues] =
    useState<FilterItemValues | null>(null);

  const handleFilterChange = (filterItemValues: FilterItemValues) => {
    setFilterItemValues(filterItemValues);
  };

  return (
    <Flex flexDirection="column">
      <FilterBar
        onFilterChange={handleFilterChange}
        defaultPinnedState={{
          lastRun: 'optional',
          keyword: 'pinned',
          owner: 'pinned-optional',
        }}
      >
        <FilterBar.Item name="keyword" label="Keyword">
          <TextInput />
        </FilterBar.Item>
        <FilterBar.Item name="owner" label="Owner">
          <Select
            name="owner"
            id="owner-select"
            defaultValue="Dora Braun"
            clearable
          >
            <Select.Content>
              {owners.map((owner) => (
                <Select.Option key={owner} value={owner}>
                  {owner}
                </Select.Option>
              ))}
            </Select.Content>
          </Select>
        </FilterBar.Item>
        <FilterBar.Item name="lastRun" label="Last run">
          <TimeframeSelector />
        </FilterBar.Item>
      </FilterBar>
      <Text>
        Filter values on change: <Code>{JSON.stringify(filterItemValues)}</Code>
      </Text>
    </Flex>
  );
};
```

```tsx
import { useState } from 'react';

import {
  FilterBar,
  FilterItemValues,
  TimeframeSelector,
} from '@dynatrace/strato-components/filters';
import { Select, TextInput } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import { Code, Text } from '@dynatrace/strato-components/typography';

const owners = [
  'Brandy Barrett',
  'Cleveland Allison',
  'Dora Braun',
  'Lacy Houston',
  'Patrick Gamble',
];

const AdditionalFilters = () => {
  const [filterItemValues, setFilterItemValues] =
    useState<FilterItemValues | null>(null);

  const handleFilterChange = (filterItemValues: FilterItemValues) => {
    setFilterItemValues(filterItemValues);
  };

  return (
    <Flex flexDirection="column">
      <FilterBar
        onFilterChange={handleFilterChange}
        defaultPinnedState={{
          lastRun: 'optional',
          keyword: 'pinned',
          owner: 'pinned-optional',
        }}
      >
        <FilterBar.Item name="keyword" label="Keyword">
          <TextInput />
        </FilterBar.Item>
        <FilterBar.Item name="owner" label="Owner">
          <Select
            name="owner"
            id="owner-select"
            defaultValue="Dora Braun"
            clearable
          >
            <Select.Content>
              {owners.map((owner) => (
                <Select.Option key={owner} value={owner}>
                  {owner}
                </Select.Option>
              ))}
            </Select.Content>
          </Select>
        </FilterBar.Item>
        <FilterBar.Item name="lastRun" label="Last run">
          <TimeframeSelector />
        </FilterBar.Item>
      </FilterBar>
      <Text>
        Filter values on change: <Code>{JSON.stringify(filterItemValues)}</Code>
      </Text>
    </Flex>
  );
};
```


### Control pinned state

To control the pinned state of filter items, pass the pinned state configuration
to the `pinnedState` prop. To handle changes in the 'Add filter' dropdown,
provide a callback to the `onPinnedStateChange` prop. The callback triggers
whenever different items are selected, receiving the suggested pinned state and
a list of item names.

```tsx
import { useState } from 'react';

import {
  FilterBar,
  PinnedState,
  TimeframeSelector,
} from '@dynatrace/strato-components/filters';
import { Select, TextInput } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import { Code, Text } from '@dynatrace/strato-components/typography';

const ControlledPinnedState = () => {
  const [changedItems, setChangedItems] = useState<string[]>([]);
  const [pinnedState, setPinnedState] = useState<PinnedState>({
    lastRun: 'optional',
    keyword: 'pinned',
    owner: 'pinned-optional',
  });

  const owners = [
    'Brandy Barrett',
    'Cleveland Allison',
    'Dora Braun',
    'Lacy Houston',
    'Patrick Gamble',
  ];

  const handleFilterChange = () => {
    console.log('Filter changed');
  };

  return (
    <Flex flexDirection="column">
      <FilterBar
        onFilterChange={handleFilterChange}
        pinnedState={pinnedState}
        onPinnedStateChange={(newPinnedState, changes) => {
          setPinnedState(newPinnedState);
          setChangedItems(changes);
        }}
      >
        <FilterBar.Item name="keyword" label="Keyword">
          <TextInput />
        </FilterBar.Item>
        <FilterBar.Item name="owner" label="Owner">
          <Select name="owner" id="owner-select" clearable>
            <Select.Content>
              {owners.map((owner) => (
                <Select.Option key={owner} value={owner}>
                  {owner}
                </Select.Option>
              ))}
            </Select.Content>
          </Select>
        </FilterBar.Item>
        <FilterBar.Item name="lastRun" label="Last run">
          <TimeframeSelector />
        </FilterBar.Item>
      </FilterBar>
      <Text>
        Changed items: <Code>{JSON.stringify(changedItems)}</Code>
      </Text>
    </Flex>
  );
};
```

```tsx
import { useState } from 'react';

import {
  FilterBar,
  PinnedState,
  TimeframeSelector,
} from '@dynatrace/strato-components/filters';
import { Select, TextInput } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import { Code, Text } from '@dynatrace/strato-components/typography';

const ControlledPinnedState = () => {
  const [changedItems, setChangedItems] = useState<string[]>([]);
  const [pinnedState, setPinnedState] = useState<PinnedState>({
    lastRun: 'optional',
    keyword: 'pinned',
    owner: 'pinned-optional',
  });

  const owners = [
    'Brandy Barrett',
    'Cleveland Allison',
    'Dora Braun',
    'Lacy Houston',
    'Patrick Gamble',
  ];

  const handleFilterChange = () => {
    console.log('Filter changed');
  };

  return (
    <Flex flexDirection="column">
      <FilterBar
        onFilterChange={handleFilterChange}
        pinnedState={pinnedState}
        onPinnedStateChange={(newPinnedState, changes) => {
          setPinnedState(newPinnedState);
          setChangedItems(changes);
        }}
      >
        <FilterBar.Item name="keyword" label="Keyword">
          <TextInput />
        </FilterBar.Item>
        <FilterBar.Item name="owner" label="Owner">
          <Select name="owner" id="owner-select" clearable>
            <Select.Content>
              {owners.map((owner) => (
                <Select.Option key={owner} value={owner}>
                  {owner}
                </Select.Option>
              ))}
            </Select.Content>
          </Select>
        </FilterBar.Item>
        <FilterBar.Item name="lastRun" label="Last run">
          <TimeframeSelector />
        </FilterBar.Item>
      </FilterBar>
      <Text>
        Changed items: <Code>{JSON.stringify(changedItems)}</Code>
      </Text>
    </Flex>
  );
};
```


### Use custom component

To use a custom component as a `FilterBar.Item`, use the React
forwardRef. Forward the ref to
the wrapper element and add the following contract props:

`value` if the component is controlled. The `onChange` callback is also
required.

`defaultValue` if the component is uncontrolled. The ref is required to focus
or open items from additional filters in the dropdown. This means that you
must also use the imperative handle in your component to expose the ref of
your input element.

Be sure to add an `aria-label` or `name` for each custom component. If there's
no text content, the `aria-label` or `name` will be used as a fallback.

```tsx
import type { Property } from 'csstype';
import {
  type Ref,
  forwardRef,
  useImperativeHandle,
  useRef,
  useState,
  type ChangeEvent,
} from 'react';

import { useFocusRing } from '@dynatrace/strato-components/core';
import {
  FilterBar,
  FilterItemValues,
} from '@dynatrace/strato-components/filters';
import { FormControlRef } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import { DataTable } from '@dynatrace/strato-components/tables';
import { Code, Text } from '@dynatrace/strato-components/typography';
import Borders from '@dynatrace/strato-design-tokens/borders';
import Colors from '@dynatrace/strato-design-tokens/colors';
import Spacings from '@dynatrace/strato-design-tokens/spacings';
import Typography from '@dynatrace/strato-design-tokens/typography';

const columns = [
  {
    header: 'Name',
    accessor: 'name',
    id: 'name',
  },
  {
    header: 'Owner',
    accessor: 'owner',
    id: 'owner',
  },
  {
    header: 'Last run',
    accessor: 'lastRun',
    id: 'lastRun',
  },
  {
    header: 'Type',
    accessor: 'type',
    id: 'type',
  },
];
type Data = {
  name: string;
  owner: string;
  lastRun: Date;
  type: string;
};
const data: Data[] = [
  {
    name: 'OutageMonitor',
    owner: 'Brandy Barrett',
    lastRun: new Date('2025-08-13T10:15:00Z'),
    type: 'Event',
  },
  {
    name: 'HeartbeatCheck',
    owner: 'Cleveland Allison',
    lastRun: new Date('2025-08-12T14:30:00Z'),
    type: 'Schedule',
  },
  {
    name: 'DailySweep',
    owner: 'Dora Braun',
    lastRun: new Date('2025-08-11T09:45:00Z'),
    type: 'Schedule',
  },
  {
    name: 'AlertResponder',
    owner: 'Lacy Houston',
    lastRun: new Date('2025-08-10T16:00:00Z'),
    type: 'Event',
  },
  {
    name: 'SmartRestart',
    owner: 'Patrick Gamble',
    lastRun: new Date('2025-08-09T11:20:00Z'),
    type: 'Manual',
  },
  {
    name: 'RecoveryFlow',
    owner: 'Brandy Barrett',
    lastRun: new Date('2025-08-08T08:10:00Z'),
    type: 'Event',
  },
  {
    name: 'MetricWatch',
    owner: 'Cleveland Allison',
    lastRun: new Date('2025-08-07T13:50:00Z'),
    type: 'Schedule',
  },
  {
    name: 'AnomalyCatcher',
    owner: 'Dora Braun',
    lastRun: new Date('2025-08-06T17:25:00Z'),
    type: 'Event',
  },
  {
    name: 'IncidentRadar',
    owner: 'Lacy Houston',
    lastRun: new Date('2025-08-05T12:40:00Z'),
    type: 'Event',
  },
  {
    name: 'ForecastBot',
    owner: 'Patrick Gamble',
    lastRun: new Date('2025-08-04T15:05:00Z'),
    type: 'Schedule',
  },
  {
    name: 'EventTrigger',
    owner: 'Brandy Barrett',
    lastRun: new Date('2025-08-03T07:55:00Z'),
    type: 'Event',
  },
];
interface MyCustomItemProps {
  value: string;
  onChange: (newValue: string) => void;
}

const MyCustomItem = forwardRef(
  (
    props: MyCustomItemProps,
    forwardedRef: Ref<Omit<FormControlRef<HTMLDivElement>, 'validate'>>
  ) => {
    const { onChange, value, ...remainingProps } = props;

    const inputRef = useRef<HTMLInputElement>(null);
    const wrapperRef = useRef<HTMLDivElement>(null);

    useImperativeHandle(
      forwardedRef,
      (): Omit<FormControlRef<HTMLDivElement>, 'validate'> => ({
        element: wrapperRef.current,
        inputRef: inputRef.current,
      }),
      []
    );

    const { focusProps, focusClassName } = useFocusRing({
      ignoreModality: true,
    });

    return (
      <div
        className={focusClassName}
        ref={wrapperRef}
        style={{
          paddingLeft: Spacings.Size12,
          paddingRight: Spacings.Size12,
          borderRadius: Borders.Radius.Field.Default,
          backgroundColor: Colors.Background.Field.Neutral.Emphasized,
        }}
      >
        <input
          ref={inputRef}
          value={value}
          onChange={(e: ChangeEvent<HTMLInputElement>) =>
            onChange?.(e.target.value)
          }
          style={{
            textOverflow: 'ellipsis',
            appearance: 'none',
            background: 'transparent',
            border: 'none',
            padding: 0,
            marginTop: Spacings.Size6,
            marginBottom: Spacings.Size6,
            color: Colors.Text.Neutral.Default,
            outline: 'none',
            fontFamily: Typography.Text.Base.Default.Family,
            fontWeight: Typography.Text.Base.Default.Weight,
            fontSize: Typography.Text.Base.Default.Size,
            lineHeight: Typography.Text.Base.Default.LineHeight,
            textDecoration: Typography.Text.Base.Default.TextDecoration,
            textTransform: Typography.Text.Base.Default
              .TextTransform as Property.TextTransform,
          }}
          {...focusProps}
          {...remainingProps}
        />
      </div>
    );
  }
);

(MyCustomItem as typeof MyCustomItem & { displayName: string }).displayName =
  'MyCustomItem';

const CustomFilterItem = () => {
  const [filteredData, setFilteredData] = useState(data);
  const [filterItemValues, setFilterItemValues] =
    useState<FilterItemValues | null>(null);

  function filterData(filterItemValues: FilterItemValues) {
    return data.filter((d) => {
      return Object.entries(filterItemValues).every(([key, { value }]) => {
        if (!value || typeof value !== 'string') {
          return true;
        }

        switch (key) {
          case 'text-full':
            return (
              d.name.toLowerCase().includes(value.toLowerCase()) ||
              d.type.toLowerCase().includes(value.toLowerCase())
            );
          case 'text-owner':
            return d.owner.toLowerCase().includes(value.toLowerCase());
          default:
            return true;
        }
      });
    });
  }

  const handleFilterChange = (filterItemValues: FilterItemValues) => {
    setFilterItemValues(filterItemValues);
    const result = filterData(filterItemValues);
    setFilteredData(result);
  };

  const [textValue, setTextValue] = useState('');
  const [textValue2, setTextValue2] = useState('');

  return (
    <Flex gap={8} flexDirection="column" height={400}>
      <DataTable columns={columns} data={filteredData}>
        <DataTable.TableActions>
          <FilterBar
            onFilterChange={handleFilterChange}
            defaultPinnedState={{
              'text-full': 'optional',
              'text-owner': 'pinned',
            }}
          >
            <FilterBar.Item name="text-full" label="Full text">
              <MyCustomItem value={textValue} onChange={setTextValue} />
            </FilterBar.Item>

            <FilterBar.Item name="text-owner" label="Owner">
              <MyCustomItem value={textValue2} onChange={setTextValue2} />
            </FilterBar.Item>
          </FilterBar>
        </DataTable.TableActions>
      </DataTable>
      <Text>
        Filter values on change: <Code>{JSON.stringify(filterItemValues)}</Code>
      </Text>
    </Flex>
  );
};
```

```tsx
import type { Property } from 'csstype';
import {
  type Ref,
  forwardRef,
  useImperativeHandle,
  useRef,
  useState,
  type ChangeEvent,
} from 'react';

import { useFocusRing } from '@dynatrace/strato-components/core';
import {
  FilterBar,
  FilterItemValues,
} from '@dynatrace/strato-components/filters';
import { FormControlRef } from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import { DataTable } from '@dynatrace/strato-components/tables';
import { Code, Text } from '@dynatrace/strato-components/typography';
import Borders from '@dynatrace/strato-design-tokens/borders';
import Colors from '@dynatrace/strato-design-tokens/colors';
import Spacings from '@dynatrace/strato-design-tokens/spacings';
import Typography from '@dynatrace/strato-design-tokens/typography';

const columns = [
  {
    header: 'Name',
    accessor: 'name',
    id: 'name',
  },
  {
    header: 'Owner',
    accessor: 'owner',
    id: 'owner',
  },
  {
    header: 'Last run',
    accessor: 'lastRun',
    id: 'lastRun',
  },
  {
    header: 'Type',
    accessor: 'type',
    id: 'type',
  },
];
type Data = {
  name: string;
  owner: string;
  lastRun: Date;
  type: string;
};
const data: Data[] = [
  {
    name: 'OutageMonitor',
    owner: 'Brandy Barrett',
    lastRun: new Date('2025-08-13T10:15:00Z'),
    type: 'Event',
  },
  {
    name: 'HeartbeatCheck',
    owner: 'Cleveland Allison',
    lastRun: new Date('2025-08-12T14:30:00Z'),
    type: 'Schedule',
  },
  {
    name: 'DailySweep',
    owner: 'Dora Braun',
    lastRun: new Date('2025-08-11T09:45:00Z'),
    type: 'Schedule',
  },
  {
    name: 'AlertResponder',
    owner: 'Lacy Houston',
    lastRun: new Date('2025-08-10T16:00:00Z'),
    type: 'Event',
  },
  {
    name: 'SmartRestart',
    owner: 'Patrick Gamble',
    lastRun: new Date('2025-08-09T11:20:00Z'),
    type: 'Manual',
  },
  {
    name: 'RecoveryFlow',
    owner: 'Brandy Barrett',
    lastRun: new Date('2025-08-08T08:10:00Z'),
    type: 'Event',
  },
  {
    name: 'MetricWatch',
    owner: 'Cleveland Allison',
    lastRun: new Date('2025-08-07T13:50:00Z'),
    type: 'Schedule',
  },
  {
    name: 'AnomalyCatcher',
    owner: 'Dora Braun',
    lastRun: new Date('2025-08-06T17:25:00Z'),
    type: 'Event',
  },
  {
    name: 'IncidentRadar',
    owner: 'Lacy Houston',
    lastRun: new Date('2025-08-05T12:40:00Z'),
    type: 'Event',
  },
  {
    name: 'ForecastBot',
    owner: 'Patrick Gamble',
    lastRun: new Date('2025-08-04T15:05:00Z'),
    type: 'Schedule',
  },
  {
    name: 'EventTrigger',
    owner: 'Brandy Barrett',
    lastRun: new Date('2025-08-03T07:55:00Z'),
    type: 'Event',
  },
];
interface MyCustomItemProps {
  value: string;
  onChange: (newValue: string) => void;
}

const MyCustomItem = forwardRef(
  (
    props: MyCustomItemProps,
    forwardedRef: Ref<Omit<FormControlRef<HTMLDivElement>, 'validate'>>
  ) => {
    const { onChange, value, ...remainingProps } = props;

    const inputRef = useRef<HTMLInputElement>(null);
    const wrapperRef = useRef<HTMLDivElement>(null);

    useImperativeHandle(
      forwardedRef,
      (): Omit<FormControlRef<HTMLDivElement>, 'validate'> => ({
        element: wrapperRef.current,
        inputRef: inputRef.current,
      }),
      []
    );

    const { focusProps, focusClassName } = useFocusRing({
      ignoreModality: true,
    });

    return (
      <div
        className={focusClassName}
        ref={wrapperRef}
        style={{
          paddingLeft: Spacings.Size12,
          paddingRight: Spacings.Size12,
          borderRadius: Borders.Radius.Field.Default,
          backgroundColor: Colors.Background.Field.Neutral.Emphasized,
        }}
      >
        <input
          ref={inputRef}
          value={value}
          onChange={(e: ChangeEvent<HTMLInputElement>) =>
            onChange?.(e.target.value)
          }
          style={{
            textOverflow: 'ellipsis',
            appearance: 'none',
            background: 'transparent',
            border: 'none',
            padding: 0,
            marginTop: Spacings.Size6,
            marginBottom: Spacings.Size6,
            color: Colors.Text.Neutral.Default,
            outline: 'none',
            fontFamily: Typography.Text.Base.Default.Family,
            fontWeight: Typography.Text.Base.Default.Weight,
            fontSize: Typography.Text.Base.Default.Size,
            lineHeight: Typography.Text.Base.Default.LineHeight,
            textDecoration: Typography.Text.Base.Default.TextDecoration,
            textTransform: Typography.Text.Base.Default
              .TextTransform as Property.TextTransform,
          }}
          {...focusProps}
          {...remainingProps}
        />
      </div>
    );
  }
);

(MyCustomItem as typeof MyCustomItem & { displayName: string }).displayName =
  'MyCustomItem';

const CustomFilterItem = () => {
  const [filteredData, setFilteredData] = useState(data);
  const [filterItemValues, setFilterItemValues] =
    useState<FilterItemValues | null>(null);

  function filterData(filterItemValues: FilterItemValues) {
    return data.filter((d) => {
      return Object.entries(filterItemValues).every(([key, { value }]) => {
        if (!value || typeof value !== 'string') {
          return true;
        }

        switch (key) {
          case 'text-full':
            return (
              d.name.toLowerCase().includes(value.toLowerCase()) ||
              d.type.toLowerCase().includes(value.toLowerCase())
            );
          case 'text-owner':
            return d.owner.toLowerCase().includes(value.toLowerCase());
          default:
            return true;
        }
      });
    });
  }

  const handleFilterChange = (filterItemValues: FilterItemValues) => {
    setFilterItemValues(filterItemValues);
    const result = filterData(filterItemValues);
    setFilteredData(result);
  };

  const [textValue, setTextValue] = useState('');
  const [textValue2, setTextValue2] = useState('');

  return (
    <Flex gap={8} flexDirection="column" height={400}>
      <DataTable columns={columns} data={filteredData}>
        <DataTable.TableActions>
          <FilterBar
            onFilterChange={handleFilterChange}
            defaultPinnedState={{
              'text-full': 'optional',
              'text-owner': 'pinned',
            }}
          >
            <FilterBar.Item name="text-full" label="Full text">
              <MyCustomItem value={textValue} onChange={setTextValue} />
            </FilterBar.Item>

            <FilterBar.Item name="text-owner" label="Owner">
              <MyCustomItem value={textValue2} onChange={setTextValue2} />
            </FilterBar.Item>
          </FilterBar>
        </DataTable.TableActions>
      </DataTable>
      <Text>
        Filter values on change: <Code>{JSON.stringify(filterItemValues)}</Code>
      </Text>
    </Flex>
  );
};
```


### Related

#### Patterns

FilteringStill have questions?Find answers in the Dynatrace Community
- Import
- Demo
- Give items unique names
- Filter text
- Reset filter values
- Prefill additional filters
- Render filtered data in a table
- Persist sorting of filtered data
- Filter sub-row data
- Pin and unpin optional filters
- Control pinned state
- Use custom component
- Related
- Patterns

### Props

FilterBar helps users easily filter datasets using one or more filter criteria.
A range of form elements can be added as filter controls.

#### FilterBarProps

##### Signature:
`export declare type FilterBarProps = ( | ) & ;`

### FilterBar.Item

You can use the `FilterBar.Item` component to render an item inside the
`FilterBar`, as shown above.

#### FilterBarItemProps
extends`, , ` |
 | Name | Type | Default | Description
 | `name` | | | A unique identifier for this sub-filter (must only be unique for this filter). In case custom labels are used without text children, this is displayed on the MoreMenu trigger instead.
 | `label` | | | Description text of this sub-filter. If you use a custom label without text children, the name will be displayed on the MoreMenu instead.
 | `children` | <> | | Only one element, is expected here.
 | `showLabel?` | | | Defines if the label is shown for the filter item. If set specifically, it also overwrites the general configuration set with the showLabels prop on the FilterBar for one item.

### FilterBar.ResetButton

You can use the `FilterBar.ResetButton` component to render a button that resets
all filters, as shown above.

#### ResetButtonProps
extends`, , , , ` |
 | Name | Type | Default | Description
 | `onClick` | () => | | Handler that is called when the ResetButton is clicked.Still have questions?Find answers in the Dynatrace Community
- FilterBar.Item
- FilterBar.ResetButton

---

## FilterField

`/design/components/filters/FilterField/`

`FilterField` is an advanced, text-based filtering component. It supports
complex data filtering with intuitive filter field syntax and auto-suggestions.

### Import

`tsx
import { FilterField } from '@dynatrace/strato-components/filters';
`

### Demo

`FilterField` uses a simple and intuitive
filter field syntax.
When the user begins to type, a dropdown with suggestions for the next key,
value, or operator appears. See Usage for best practices to
implement the component.

```tsx
import { useMemo, useState } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import {
  FilterField,
  isFilterFieldLeafNode,
  isFilterFieldListNode,
} from '@dynatrace/strato-components/filters';
import type {
  FilterFieldGroupNode,
  FilterFieldNode,
  FilterFieldTree,
  FilterFieldValidatorMap,
} from '@dynatrace/strato-components/filters';
import {
  FormField,
  FormFieldMessages,
} from '@dynatrace/strato-components/forms';
import { Flex, Grid } from '@dynatrace/strato-components/layouts';
import {
  DataTable,
  type DataTableColumnDef,
} from '@dynatrace/strato-components/tables';
import { PlayIcon, RefreshIcon } from '@dynatrace/strato-icons';

type Pod = {
  Name: string;
  Running: boolean;
  'Container restarts': number;
  Annotations: string;
  Fields: string;
};

const data: Pod[] = [
  {
    Name: 'frontend-app-7c9d8f7b6d-abc12',
    Running: true,
    'Container restarts': 2,
    Annotations: 'prometheus.io/scrape=true',
    Fields:
      '{"metadata":{"name":"frontend-app-7c9d8f7b6d-abc12","labels":{"app":"frontend"},"annotations":{"prometheus.io/scrape":"true"}},"spec":{"nodeName":"k8s-node-01","restartPolicy":"Always"},"status":{"phase":"Running","podIP":"10.244.1.15"}}',
  },
  {
    Name: 'backend-worker-5f8e9d6c4b-df34',
    Running: false,
    'Container restarts': 0,
    Annotations: 'prometheus.io/port=8080',
    Fields:
      '{"metadata":{"name":"backend-worker-5f8e9d6c4b-df34","labels":{"app":"backend"},"annotations":{"prometheus.io/port":"8080"}},"spec":{"nodeName":"k8s-node-02","restartPolicy":"OnFailure"},"status":{"phase":"Pending","podIP":"10.244.2.21"}}',
  },
  {
    Name: 'db-migrator-2a7b6c5d8e-ghi56',
    Running: true,
    'Container restarts': 1,
    Annotations: 'kubectl.kubernetes.io/restartedAt=2024-06-01T12:34:56Z',
    Fields:
      '{"metadata":{"name":"db-migrator-2a7b6c5d8e-ghi56","labels":{"app":"db"},"annotations":{"kubectl.kubernetes.io/restartedAt":"2024-06-01T12:34:56Z"}},"spec":{"nodeName":"k8s-node-03","restartPolicy":"Never"},"status":{"phase":"Running","podIP":"10.244.3.33"}}',
  },
  {
    Name: 'cache-redis-1b2c3d4e5f-jkl78',
    Running: false,
    'Container restarts': 3,
    Annotations: 'sidecar.istio.io/inject=false',
    Fields:
      '{"metadata":{"name":"cache-redis-1b2c3d4e5f-jkl78","labels":{"app":"cache"},"annotations":{"sidecar.istio.io/inject":"false"}},"spec":{"nodeName":"k8s-node-04","restartPolicy":"Always"},"status":{"phase":"CrashLoopBackOff","podIP":"10.244.4.44"}}',
  },
  {
    Name: 'metrics-exporter-9e8d7c6b5a-mno90',
    Running: true,
    'Container restarts': 0,
    Annotations: 'linkerd.io/inject=enabled',
    Fields:
      '{"metadata":{"name":"metrics-exporter-9e8d7c6b5a-mno90","labels":{"app":"metrics"},"annotations":{"linkerd.io/inject":"enabled"}},"spec":{"nodeName":"k8s-node-05","restartPolicy":"Always"},"status":{"phase":"Running","podIP":"10.244.5.55"}}',
  },
];

function filterData(dataset: Pod[], node?: FilterFieldTree): Pod[] {
  if (!node || dataset.length === 0) {
    return dataset;
  }
  return dataset.filter((item) => filterFunction(item, node));
}

function filterFunction(item: Pod, node: FilterFieldGroupNode): boolean {
  const { logicalOperator, children } = node;
  return logicalOperator === 'OR'
    ? children.some((childNode) => evaluateFilter(item, childNode, false))
    : children.every((childNode) => evaluateFilter(item, childNode, true));
}

function getByPath(obj: object | undefined, path: string): unknown {
  return path.split('.').reduce<unknown>((acc, key) => {
    if (acc && typeof acc === 'object' && key in acc) {
      return (acc as Record<string, unknown>)[key];
    }
    return undefined;
  }, obj);
}

function evaluateFilter(
  item: Pod,
  node: FilterFieldNode,
  defaultReturn: boolean
): boolean {
  switch (node.type) {
    case 'Group':
      return filterFunction(item, node);
    case 'Statement': {
      const { key, comparisonOperator, value } = node;
      const isValidStatementKey = (needleKey: string): needleKey is keyof Pod =>
        needleKey in item;

      switch (comparisonOperator?.type) {
        case 'ComparisonOperator': {
          if (
            !(
              key &&
              comparisonOperator &&
              value &&
              isFilterFieldLeafNode(value)
            )
          ) {
            return defaultReturn;
          }
          const { value: statementComparisonOperator } = comparisonOperator;
          let { value: statementKey } = key;
          const { type: statementKeyType } = key;
          const { value: statementValue } = value;

          if (!statementValue) {
            return defaultReturn;
          }

          statementKey =
            statementKeyType === 'JSONPath' ? key.root : statementKey;

          if (!isValidStatementKey(statementKey)) {
            return defaultReturn;
          }

          let itemKey = item[statementKey];

          if (statementKeyType === 'JSONPath') {
            try {
              const itemKeyJSONObject = JSON.parse(String(itemKey));
              itemKey = JSON.stringify(
                // Remove $. from key.path. Also, we for the sake of the demo we assume
                // that we can only parse paths with dot notation.
                getByPath(itemKeyJSONObject, key.path.slice(2))
                // Remove leading/trailing quotes from itemKey if present
              ).replace(/^"+|"+$/g, '');
            } catch {
              return defaultReturn;
            }
          }

          switch (statementComparisonOperator) {
            case '=':
              return itemKey === statementValue;
            case '!=':
              return itemKey !== statementValue;
            case '<':
              return itemKey !== undefined && itemKey < statementValue;
            case '<=':
              return itemKey !== undefined && itemKey <= statementValue;
            case '>':
              return itemKey !== undefined && itemKey > statementValue;
            case '>=':
              return itemKey !== undefined && itemKey >= statementValue;
            case 'contains':
              return (
                itemKey !== undefined &&
                typeof itemKey === 'string' &&
                typeof statementValue === 'string' &&
                itemKey.includes(statementValue)
              );
            case 'not-contains':
              return (
                itemKey !== undefined &&
                typeof itemKey === 'string' &&
                typeof statementValue === 'string' &&
                !itemKey.includes(statementValue)
              );
            case 'starts-with':
              return (
                itemKey !== undefined &&
                typeof itemKey === 'string' &&
                typeof statementValue === 'string' &&
                itemKey.startsWith(statementValue)
              );
            case 'not-starts-with':
              return (
                itemKey !== undefined &&
                typeof itemKey === 'string' &&
                typeof statementValue === 'string' &&
                !itemKey.startsWith(statementValue)
              );
            case 'ends-with':
              return (
                itemKey !== undefined &&
                typeof itemKey === 'string' &&
                typeof statementValue === 'string' &&
                itemKey.endsWith(statementValue)
              );
            case 'not-ends-with':
              return (
                itemKey !== undefined &&
                typeof itemKey === 'string' &&
                typeof statementValue === 'string' &&
                !itemKey.endsWith(statementValue)
              );
            default:
              // In case a new comparison operator was added, it should be handled accordingly.
              console.warn(
                `Comparison operator '${statementComparisonOperator}' not handled.`
              );
              return defaultReturn;
          }
        }
        case 'InclusionOperator': {
          if (
            !(
              key &&
              comparisonOperator &&
              value &&
              isFilterFieldListNode(value)
            )
          ) {
            return defaultReturn;
          }
          const { value: statementComparisonOperator } = comparisonOperator;
          const { value: statementKey } = key;
          if (!isValidStatementKey(statementKey)) {
            return defaultReturn;
          }
          const { value: listValues } = value;
          const values = listValues.map((entry) => entry.value);
          return statementComparisonOperator === 'in'
            ? values.includes(item[statementKey])
            : !values.includes(item[statementKey]);
        }
        case 'ExistsOperator': {
          if (!(key && comparisonOperator)) {
            return defaultReturn;
          }

          const { value: statementKey } = key;
          const { value } = comparisonOperator;

          if (!isValidStatementKey(statementKey)) {
            return defaultReturn;
          }

          return value
            ? item[statementKey] !== undefined
            : item[statementKey] === undefined;
        }
        case 'SearchOperator': {
          if (!(value && isFilterFieldLeafNode(value))) {
            return defaultReturn;
          }
          const { value: statementValue } = value;
          if (!statementValue) {
            return defaultReturn;
          }
          return Object.values(item).some(
            (itemValue) =>
              typeof itemValue === 'string' &&
              itemValue.includes(statementValue.toString())
          );
        }
        case undefined:
          return defaultReturn;
        default:
          // In case a new comparison operator was added, it should be handled accordingly.
          console.warn(
            `Comparison operator '${comparisonOperator?.type}' not handled.`
          );
          return defaultReturn;
      }
    }
    default:
      // The only nodes we want to handle are groups and statements.
      // Any other nodes included in the tree (explicit logical operator) will be ignored.
      return defaultReturn;
  }
}

const validatorMap: FilterFieldValidatorMap = {
  keyPredicates: [
    {
      key: 'Annotations',
      valuePredicate: data.map((pod) => pod.Annotations),
      valueType: 'String',
    },
    {
      key: 'Container restarts',
      valuePredicate: data.map((pod) => pod['Container restarts']),
      valueType: 'Number',
    },
    {
      key: 'Fields',
      valueType: 'JSONPath',
    },
    {
      key: 'Name',
      valuePredicate: data.map((pod) => pod.Name),
      valueType: 'String',
    },
    {
      key: 'Running',
      valueType: 'Boolean',
    },
  ],
  exhaustive: true,
};

const StaticSuggestions = () => {
  const [value, setValue] = useState('');
  const [tree, setTree] = useState<FilterFieldTree>();
  const [submittedValue, setSubmittedValue] = useState('');
  const [filteredData, setFilteredData] = useState(data);

  const columns = useMemo<DataTableColumnDef<Pod>[]>(
    () => [
      {
        header: 'Name',
        accessor: 'Name',
        id: 'Name',
        width: '1fr',
      },
      {
        header: 'Running',
        accessor: 'Running',
        id: 'Running',
        width: 'content',
      },
      {
        header: 'Container restarts',
        accessor: 'Container restarts',
        id: 'Container restarts',
        width: 'content',
        alignment: 'right',
      },
      {
        header: 'Annotations',
        accessor: 'Annotations',
        id: 'Annotations',
        width: 200,
      },
      { header: 'Fields', accessor: 'Fields', id: 'Fields', width: '1fr' },
    ],
    []
  );

  return (
    <Flex flexDirection="column">
      <form
        onSubmit={(event) => {
          event.preventDefault();
          setSubmittedValue(value);
          setFilteredData(filterData(data, tree));
        }}
      >
        <FormField>
          <Grid gridTemplateColumns="1fr auto">
            <FilterField
              aria-label="Filter data"
              onChange={(value, tree) => {
                setValue(value);
                setTree(tree);
              }}
              validatorMap={validatorMap}
              parserConfig={{
                searchConversion: true,
                jsonPathConversion: true,
              }}
              autoSuggestions
            />
            <Button
              variant={value !== submittedValue ? 'accent' : 'emphasized'}
              color={value !== submittedValue ? 'primary' : 'neutral'}
              type="submit"
            >
              <Button.Prefix>
                {value === submittedValue ? <RefreshIcon /> : <PlayIcon />}
              </Button.Prefix>
              {value === submittedValue ? 'Refresh' : 'Update'}
            </Button>
          </Grid>
          <FormFieldMessages />
        </FormField>
      </form>
      <DataTable columns={columns} data={filteredData} fullWidth resizable />
    </Flex>
  );
};
```

```tsx
import { useMemo, useState } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import {
  FilterField,
  isFilterFieldLeafNode,
  isFilterFieldListNode,
} from '@dynatrace/strato-components/filters';
import type {
  FilterFieldGroupNode,
  FilterFieldNode,
  FilterFieldTree,
  FilterFieldValidatorMap,
} from '@dynatrace/strato-components/filters';
import {
  FormField,
  FormFieldMessages,
} from '@dynatrace/strato-components/forms';
import { Flex, Grid } from '@dynatrace/strato-components/layouts';
import {
  DataTable,
  type DataTableColumnDef,
} from '@dynatrace/strato-components/tables';
import { PlayIcon, RefreshIcon } from '@dynatrace/strato-icons';

type Pod = {
  Name: string;
  Running: boolean;
  'Container restarts': number;
  Annotations: string;
  Fields: string;
};

const data: Pod[] = [
  {
    Name: 'frontend-app-7c9d8f7b6d-abc12',
    Running: true,
    'Container restarts': 2,
    Annotations: 'prometheus.io/scrape=true',
    Fields:
      '{"metadata":{"name":"frontend-app-7c9d8f7b6d-abc12","labels":{"app":"frontend"},"annotations":{"prometheus.io/scrape":"true"}},"spec":{"nodeName":"k8s-node-01","restartPolicy":"Always"},"status":{"phase":"Running","podIP":"10.244.1.15"}}',
  },
  {
    Name: 'backend-worker-5f8e9d6c4b-df34',
    Running: false,
    'Container restarts': 0,
    Annotations: 'prometheus.io/port=8080',
    Fields:
      '{"metadata":{"name":"backend-worker-5f8e9d6c4b-df34","labels":{"app":"backend"},"annotations":{"prometheus.io/port":"8080"}},"spec":{"nodeName":"k8s-node-02","restartPolicy":"OnFailure"},"status":{"phase":"Pending","podIP":"10.244.2.21"}}',
  },
  {
    Name: 'db-migrator-2a7b6c5d8e-ghi56',
    Running: true,
    'Container restarts': 1,
    Annotations: 'kubectl.kubernetes.io/restartedAt=2024-06-01T12:34:56Z',
    Fields:
      '{"metadata":{"name":"db-migrator-2a7b6c5d8e-ghi56","labels":{"app":"db"},"annotations":{"kubectl.kubernetes.io/restartedAt":"2024-06-01T12:34:56Z"}},"spec":{"nodeName":"k8s-node-03","restartPolicy":"Never"},"status":{"phase":"Running","podIP":"10.244.3.33"}}',
  },
  {
    Name: 'cache-redis-1b2c3d4e5f-jkl78',
    Running: false,
    'Container restarts': 3,
    Annotations: 'sidecar.istio.io/inject=false',
    Fields:
      '{"metadata":{"name":"cache-redis-1b2c3d4e5f-jkl78","labels":{"app":"cache"},"annotations":{"sidecar.istio.io/inject":"false"}},"spec":{"nodeName":"k8s-node-04","restartPolicy":"Always"},"status":{"phase":"CrashLoopBackOff","podIP":"10.244.4.44"}}',
  },
  {
    Name: 'metrics-exporter-9e8d7c6b5a-mno90',
    Running: true,
    'Container restarts': 0,
    Annotations: 'linkerd.io/inject=enabled',
    Fields:
      '{"metadata":{"name":"metrics-exporter-9e8d7c6b5a-mno90","labels":{"app":"metrics"},"annotations":{"linkerd.io/inject":"enabled"}},"spec":{"nodeName":"k8s-node-05","restartPolicy":"Always"},"status":{"phase":"Running","podIP":"10.244.5.55"}}',
  },
];

function filterData(dataset: Pod[], node?: FilterFieldTree): Pod[] {
  if (!node || dataset.length === 0) {
    return dataset;
  }
  return dataset.filter((item) => filterFunction(item, node));
}

function filterFunction(item: Pod, node: FilterFieldGroupNode): boolean {
  const { logicalOperator, children } = node;
  return logicalOperator === 'OR'
    ? children.some((childNode) => evaluateFilter(item, childNode, false))
    : children.every((childNode) => evaluateFilter(item, childNode, true));
}

function getByPath(obj: object | undefined, path: string): unknown {
  return path.split('.').reduce<unknown>((acc, key) => {
    if (acc && typeof acc === 'object' && key in acc) {
      return (acc as Record<string, unknown>)[key];
    }
    return undefined;
  }, obj);
}

function evaluateFilter(
  item: Pod,
  node: FilterFieldNode,
  defaultReturn: boolean
): boolean {
  switch (node.type) {
    case 'Group':
      return filterFunction(item, node);
    case 'Statement': {
      const { key, comparisonOperator, value } = node;
      const isValidStatementKey = (needleKey: string): needleKey is keyof Pod =>
        needleKey in item;

      switch (comparisonOperator?.type) {
        case 'ComparisonOperator': {
          if (
            !(
              key &&
              comparisonOperator &&
              value &&
              isFilterFieldLeafNode(value)
            )
          ) {
            return defaultReturn;
          }
          const { value: statementComparisonOperator } = comparisonOperator;
          let { value: statementKey } = key;
          const { type: statementKeyType } = key;
          const { value: statementValue } = value;

          if (!statementValue) {
            return defaultReturn;
          }

          statementKey =
            statementKeyType === 'JSONPath' ? key.root : statementKey;

          if (!isValidStatementKey(statementKey)) {
            return defaultReturn;
          }

          let itemKey = item[statementKey];

          if (statementKeyType === 'JSONPath') {
            try {
              const itemKeyJSONObject = JSON.parse(String(itemKey));
              itemKey = JSON.stringify(
                // Remove $. from key.path. Also, we for the sake of the demo we assume
                // that we can only parse paths with dot notation.
                getByPath(itemKeyJSONObject, key.path.slice(2))
                // Remove leading/trailing quotes from itemKey if present
              ).replace(/^"+|"+$/g, '');
            } catch {
              return defaultReturn;
            }
          }

          switch (statementComparisonOperator) {
            case '=':
              return itemKey === statementValue;
            case '!=':
              return itemKey !== statementValue;
            case '<':
              return itemKey !== undefined && itemKey < statementValue;
            case '<=':
              return itemKey !== undefined && itemKey <= statementValue;
            case '>':
              return itemKey !== undefined && itemKey > statementValue;
            case '>=':
              return itemKey !== undefined && itemKey >= statementValue;
            case 'contains':
              return (
                itemKey !== undefined &&
                typeof itemKey === 'string' &&
                typeof statementValue === 'string' &&
                itemKey.includes(statementValue)
              );
            case 'not-contains':
              return (
                itemKey !== undefined &&
                typeof itemKey === 'string' &&
                typeof statementValue === 'string' &&
                !itemKey.includes(statementValue)
              );
            case 'starts-with':
              return (
                itemKey !== undefined &&
                typeof itemKey === 'string' &&
                typeof statementValue === 'string' &&
                itemKey.startsWith(statementValue)
              );
            case 'not-starts-with':
              return (
                itemKey !== undefined &&
                typeof itemKey === 'string' &&
                typeof statementValue === 'string' &&
                !itemKey.startsWith(statementValue)
              );
            case 'ends-with':
              return (
                itemKey !== undefined &&
                typeof itemKey === 'string' &&
                typeof statementValue === 'string' &&
                itemKey.endsWith(statementValue)
              );
            case 'not-ends-with':
              return (
                itemKey !== undefined &&
                typeof itemKey === 'string' &&
                typeof statementValue === 'string' &&
                !itemKey.endsWith(statementValue)
              );
            default:
              // In case a new comparison operator was added, it should be handled accordingly.
              console.warn(
                `Comparison operator '${statementComparisonOperator}' not handled.`
              );
              return defaultReturn;
          }
        }
        case 'InclusionOperator': {
          if (
            !(
              key &&
              comparisonOperator &&
              value &&
              isFilterFieldListNode(value)
            )
          ) {
            return defaultReturn;
          }
          const { value: statementComparisonOperator } = comparisonOperator;
          const { value: statementKey } = key;
          if (!isValidStatementKey(statementKey)) {
            return defaultReturn;
          }
          const { value: listValues } = value;
          const values = listValues.map((entry) => entry.value);
          return statementComparisonOperator === 'in'
            ? values.includes(item[statementKey])
            : !values.includes(item[statementKey]);
        }
        case 'ExistsOperator': {
          if (!(key && comparisonOperator)) {
            return defaultReturn;
          }

          const { value: statementKey } = key;
          const { value } = comparisonOperator;

          if (!isValidStatementKey(statementKey)) {
            return defaultReturn;
          }

          return value
            ? item[statementKey] !== undefined
            : item[statementKey] === undefined;
        }
        case 'SearchOperator': {
          if (!(value && isFilterFieldLeafNode(value))) {
            return defaultReturn;
          }
          const { value: statementValue } = value;
          if (!statementValue) {
            return defaultReturn;
          }
          return Object.values(item).some(
            (itemValue) =>
              typeof itemValue === 'string' &&
              itemValue.includes(statementValue.toString())
          );
        }
        case undefined:
          return defaultReturn;
        default:
          // In case a new comparison operator was added, it should be handled accordingly.
          console.warn(
            `Comparison operator '${comparisonOperator?.type}' not handled.`
          );
          return defaultReturn;
      }
    }
    default:
      // The only nodes we want to handle are groups and statements.
      // Any other nodes included in the tree (explicit logical operator) will be ignored.
      return defaultReturn;
  }
}

const validatorMap: FilterFieldValidatorMap = {
  keyPredicates: [
    {
      key: 'Annotations',
      valuePredicate: data.map((pod) => pod.Annotations),
      valueType: 'String',
    },
    {
      key: 'Container restarts',
      valuePredicate: data.map((pod) => pod['Container restarts']),
      valueType: 'Number',
    },
    {
      key: 'Fields',
      valueType: 'JSONPath',
    },
    {
      key: 'Name',
      valuePredicate: data.map((pod) => pod.Name),
      valueType: 'String',
    },
    {
      key: 'Running',
      valueType: 'Boolean',
    },
  ],
  exhaustive: true,
};

const StaticSuggestions = () => {
  const [value, setValue] = useState('');
  const [tree, setTree] = useState<FilterFieldTree>();
  const [submittedValue, setSubmittedValue] = useState('');
  const [filteredData, setFilteredData] = useState(data);

  const columns = useMemo<DataTableColumnDef<Pod>[]>(
    () => [
      {
        header: 'Name',
        accessor: 'Name',
        id: 'Name',
        width: '1fr',
      },
      {
        header: 'Running',
        accessor: 'Running',
        id: 'Running',
        width: 'content',
      },
      {
        header: 'Container restarts',
        accessor: 'Container restarts',
        id: 'Container restarts',
        width: 'content',
        alignment: 'right',
      },
      {
        header: 'Annotations',
        accessor: 'Annotations',
        id: 'Annotations',
        width: 200,
      },
      { header: 'Fields', accessor: 'Fields', id: 'Fields', width: '1fr' },
    ],
    []
  );

  return (
    <Flex flexDirection="column">
      <form
        onSubmit={(event) => {
          event.preventDefault();
          setSubmittedValue(value);
          setFilteredData(filterData(data, tree));
        }}
      >
        <FormField>
          <Grid gridTemplateColumns="1fr auto">
            <FilterField
              aria-label="Filter data"
              onChange={(value, tree) => {
                setValue(value);
                setTree(tree);
              }}
              validatorMap={validatorMap}
              parserConfig={{
                searchConversion: true,
                jsonPathConversion: true,
              }}
              autoSuggestions
            />
            <Button
              variant={value !== submittedValue ? 'accent' : 'emphasized'}
              color={value !== submittedValue ? 'primary' : 'neutral'}
              type="submit"
            >
              <Button.Prefix>
                {value === submittedValue ? <RefreshIcon /> : <PlayIcon />}
              </Button.Prefix>
              {value === submittedValue ? 'Refresh' : 'Update'}
            </Button>
          </Grid>
          <FormFieldMessages />
        </FormField>
      </form>
      <DataTable columns={columns} data={filteredData} fullWidth resizable />
    </Flex>
  );
};
```


### Validate user input

To validate user input, set restrictions for keys, comparison operators, and
values using the `validatorMap` property. `FilterField` will highlight errors
and show appropriate suggestions in the suggestions overlay as long as the
`autoSuggestions` property of the `FilterField` is set to `true`.

```tsx
import { useEffect, useRef } from 'react';

import {
  FilterField,
  type FilterFieldValidatorMap,
} from '@dynatrace/strato-components/filters';
import {
  type FormControlWithOverlayRef,
  FormField,
  FormFieldMessages,
} from '@dynatrace/strato-components/forms';

const defaultValue =
  'Cluster = k8s-cluster-loadtest Namespace = local-dev-namespace-4 ';

const clusterValues = [
  'k8s-cluster-loadtest',
  'k8s-cluster-loadtest-sm',
  'k8s-cluster-e2e',
  'aws-topology',
  'local-dev',
];

const namespaceValues = [
  'kube-public',
  'kube-scheduler',
  'local-dev-namespace-1',
  'local-dev-namespace-2',
  'local-dev-namespace-3',
];

const validatorMap: FilterFieldValidatorMap = {
  keyPredicates: [
    {
      key: 'Cluster',
      valuePredicate: clusterValues,
      valueType: 'String',
    },
    {
      key: 'Namespace',
      valuePredicate: namespaceValues,
      comparisonOperators: ['equals', 'not-equals'],
    },
  ],
  comparisonOperators: ['equals', 'not-equals', 'exists', 'not-exists'],
  exhaustive: false,
};

const ValidatorMap = () => {
  const filterFieldRef = useRef<FormControlWithOverlayRef>(null);
  useEffect(() => {
    filterFieldRef.current?.validate();
  }, []);

  return (
    <FormField>
      <FilterField
        aria-label="Filter data"
        ref={filterFieldRef}
        defaultValue={defaultValue}
        validatorMap={validatorMap}
        autoSuggestions
      />
      <FormFieldMessages />
    </FormField>
  );
};
```

```tsx
import { useEffect, useRef } from 'react';

import {
  FilterField,
  type FilterFieldValidatorMap,
} from '@dynatrace/strato-components/filters';
import {
  type FormControlWithOverlayRef,
  FormField,
  FormFieldMessages,
} from '@dynatrace/strato-components/forms';

const defaultValue =
  'Cluster = k8s-cluster-loadtest Namespace = local-dev-namespace-4 ';

const clusterValues = [
  'k8s-cluster-loadtest',
  'k8s-cluster-loadtest-sm',
  'k8s-cluster-e2e',
  'aws-topology',
  'local-dev',
];

const namespaceValues = [
  'kube-public',
  'kube-scheduler',
  'local-dev-namespace-1',
  'local-dev-namespace-2',
  'local-dev-namespace-3',
];

const validatorMap: FilterFieldValidatorMap = {
  keyPredicates: [
    {
      key: 'Cluster',
      valuePredicate: clusterValues,
      valueType: 'String',
    },
    {
      key: 'Namespace',
      valuePredicate: namespaceValues,
      comparisonOperators: ['equals', 'not-equals'],
    },
  ],
  comparisonOperators: ['equals', 'not-equals', 'exists', 'not-exists'],
  exhaustive: false,
};

const ValidatorMap = () => {
  const filterFieldRef = useRef<FormControlWithOverlayRef>(null);
  useEffect(() => {
    filterFieldRef.current?.validate();
  }, []);

  return (
    <FormField>
      <FilterField
        aria-label="Filter data"
        ref={filterFieldRef}
        defaultValue={defaultValue}
        validatorMap={validatorMap}
        autoSuggestions
      />
      <FormFieldMessages />
    </FormField>
  );
};
```


### Define valid keys

You can define a list of keys in the `validatorMap` property to be interpreted
as valid. For any keys that aren't in the list, `FilterField` will show an
error. By setting the `exhaustive` property of `validatorMap` to `false`, users
can enter any key without triggering an error.

```tsx
import { useEffect, useRef, useState } from 'react';

import {
  FilterField,
  type FilterFieldValidatorMap,
} from '@dynatrace/strato-components/filters';
import {
  FormField,
  Switch,
  type FormControlWithOverlayRef,
} from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';

const defaultValue =
  'Cluster = k8s-cluster-loadtest Namespace = local-dev-namespace-3 Duration < 100s ';

const ValidatorMapKeyPredicates = () => {
  const [exhaustive, setExhaustive] = useState<boolean>(true);
  const filterFieldRef = useRef<FormControlWithOverlayRef>(null);

  const validatorMap: FilterFieldValidatorMap = {
    keyPredicates: ['Cluster', 'Namespace'],
    exhaustive: exhaustive,
  };

  useEffect(() => {
    filterFieldRef.current?.validate();
  }, []);

  return (
    <Flex flexDirection="column">
      <FormField style={{ flexGrow: '1' }}>
        <FilterField
          aria-label="Filter data"
          ref={filterFieldRef}
          defaultValue={defaultValue}
          validatorMap={validatorMap}
          autoSuggestions
        />
      </FormField>
      <Switch value={exhaustive} onChange={setExhaustive}>
        Exhaustive
      </Switch>
    </Flex>
  );
};
```

```tsx
import { useEffect, useRef, useState } from 'react';

import {
  FilterField,
  type FilterFieldValidatorMap,
} from '@dynatrace/strato-components/filters';
import {
  FormField,
  Switch,
  type FormControlWithOverlayRef,
} from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';

const defaultValue =
  'Cluster = k8s-cluster-loadtest Namespace = local-dev-namespace-3 Duration < 100s ';

const ValidatorMapKeyPredicates = () => {
  const [exhaustive, setExhaustive] = useState<boolean>(true);
  const filterFieldRef = useRef<FormControlWithOverlayRef>(null);

  const validatorMap: FilterFieldValidatorMap = {
    keyPredicates: ['Cluster', 'Namespace'],
    exhaustive: exhaustive,
  };

  useEffect(() => {
    filterFieldRef.current?.validate();
  }, []);

  return (
    <Flex flexDirection="column">
      <FormField style={{ flexGrow: '1' }}>
        <FilterField
          aria-label="Filter data"
          ref={filterFieldRef}
          defaultValue={defaultValue}
          validatorMap={validatorMap}
          autoSuggestions
        />
      </FormField>
      <Switch value={exhaustive} onChange={setExhaustive}>
        Exhaustive
      </Switch>
    </Flex>
  );
};
```


### Define key types

You can set one or multiple types for `FilterField` keys and thus restrict the
list of comparison operators and values that will be accepted. Set the
`valueType` property on a `FilterFieldKeySuggestionConfig` in the
`keyPredicates` array. The type must be set for each key individually. The type
can't be set for all keys globally.

To overwrite the type restriction of a comparison operator, set the allowed
comparison operators for that key.

Available types and their comparison operators are:

 |
 | Type | Comparison operators
 | `Any` | `equals`, `not-equals`, `less-than`, `less-or-equal`, `greater-than`, `greater-or-equal`, `in`, `not in`, `exists`, `not-exists`
 | `Boolean` | `equals`, `not-equals`, `exists`, `not-exists`
 | `Duration` | `equals`, `not-equals`, `less-than`, `less-or-equal`, `greater-than`, `greater-or-equal`, `in`, `not in`, `exists`, `not-exists`
 | `Number` | `equals`, `not-equals`, `less-than`, `less-or-equal`, `greater-than`, `greater-or-equal`, `in`, `not in`, `exists`, `not-exists`
 | `String` | `equals`, `not-equals`, `in`, `not in`, `exists`, `not-exists`, `starts-with`, `not-starts-with`, `ends-with`, `not-ends-with`, `contains`, `not-contains`

```tsx
import { useEffect, useRef } from 'react';

import {
  FilterField,
  type FilterFieldValidatorMap,
} from '@dynatrace/strato-components/filters';
import {
  FormField,
  FormFieldMessages,
  type FormControlWithOverlayRef,
} from '@dynatrace/strato-components/forms';

const defaultValue =
  'Any = any Boolean = true Boolean = string Duration = 5s Duration = 5 Number = 5 Number = false String = string String = 5 MultipleTypes = 5 MultipleTypes = string ';

const validatorMap: FilterFieldValidatorMap = {
  keyPredicates: [
    { key: 'Any', valueType: 'Any' },
    { key: 'Boolean', valueType: 'Boolean' },
    { key: 'Duration', valueType: 'Duration' },
    { key: 'Number', valueType: 'Number' },
    { key: 'String', valueType: 'String' },
    { key: 'MultipleTypes', valueType: ['Number', 'String'] },
  ],
};

const ValidatorMapTypes = () => {
  const filterFieldRef = useRef<FormControlWithOverlayRef>(null);
  useEffect(() => {
    filterFieldRef.current?.validate();
  }, []);

  return (
    <FormField>
      <FilterField
        aria-label="Filter data"
        ref={filterFieldRef}
        defaultValue={defaultValue}
        validatorMap={validatorMap}
        autoSuggestions
      />
      <FormFieldMessages />
    </FormField>
  );
};
```

```tsx
import { useEffect, useRef } from 'react';

import {
  FilterField,
  type FilterFieldValidatorMap,
} from '@dynatrace/strato-components/filters';
import {
  FormField,
  FormFieldMessages,
  type FormControlWithOverlayRef,
} from '@dynatrace/strato-components/forms';

const defaultValue =
  'Any = any Boolean = true Boolean = string Duration = 5s Duration = 5 Number = 5 Number = false String = string String = 5 MultipleTypes = 5 MultipleTypes = string ';

const validatorMap: FilterFieldValidatorMap = {
  keyPredicates: [
    { key: 'Any', valueType: 'Any' },
    { key: 'Boolean', valueType: 'Boolean' },
    { key: 'Duration', valueType: 'Duration' },
    { key: 'Number', valueType: 'Number' },
    { key: 'String', valueType: 'String' },
    { key: 'MultipleTypes', valueType: ['Number', 'String'] },
  ],
};

const ValidatorMapTypes = () => {
  const filterFieldRef = useRef<FormControlWithOverlayRef>(null);
  useEffect(() => {
    filterFieldRef.current?.validate();
  }, []);

  return (
    <FormField>
      <FilterField
        aria-label="Filter data"
        ref={filterFieldRef}
        defaultValue={defaultValue}
        validatorMap={validatorMap}
        autoSuggestions
      />
      <FormFieldMessages />
    </FormField>
  );
};
```


### Define values for keys

For any key in the `validatorMap` property, you can define a list of values that
are valid by passing an array to the `valuePredicate`. `FilterField` will return
an error for any value that isn't on the list.

If, in addition to a list of values, you pass a key type as a `valuePredicate`,
`FilterField` will accept any value that is in the list and of that key type.

```tsx
import { useEffect, useRef } from 'react';

import {
  type FilterFieldValidatorMap,
  FilterField,
} from '@dynatrace/strato-components/filters';
import {
  type FormControlWithOverlayRef,
  FormField,
  FormFieldMessages,
} from '@dynatrace/strato-components/forms';

const defaultValue =
  'Cluster = k8s-cluster-loadtest-lg Namespace = local-dev-namespace-3 Duration < 300s ';

const clusterValues = [
  'k8s-cluster-loadtest',
  'k8s-cluster-loadtest-sm',
  'k8s-cluster-e2e',
  'aws-topology',
  'local-dev',
];

const namespaceValues = [
  'kube-public',
  'kube-scheduler',
  'local-dev-namespace-1',
  'local-dev-namespace-2',
  'local-dev-namespace-3',
];

const durationValues = ['100s', '200s'];

const ValidatorMapValuePredicates = () => {
  const filterFieldRef = useRef<FormControlWithOverlayRef>(null);
  useEffect(() => {
    filterFieldRef.current?.validate();
  }, []);

  const validatorMap: FilterFieldValidatorMap = {
    keyPredicates: [
      {
        key: 'Cluster',
        valuePredicate: clusterValues,
        valueType: 'String',
      },
      {
        key: 'Namespace',
        valuePredicate: namespaceValues,
      },
      {
        key: 'Duration',
        valuePredicate: durationValues,
      },
    ],
  };

  return (
    <FormField>
      <FilterField
        aria-label="Filter data"
        ref={filterFieldRef}
        defaultValue={defaultValue}
        validatorMap={validatorMap}
        autoSuggestions
      />
      <FormFieldMessages />
    </FormField>
  );
};
```

```tsx
import { useEffect, useRef } from 'react';

import {
  type FilterFieldValidatorMap,
  FilterField,
} from '@dynatrace/strato-components/filters';
import {
  type FormControlWithOverlayRef,
  FormField,
  FormFieldMessages,
} from '@dynatrace/strato-components/forms';

const defaultValue =
  'Cluster = k8s-cluster-loadtest-lg Namespace = local-dev-namespace-3 Duration < 300s ';

const clusterValues = [
  'k8s-cluster-loadtest',
  'k8s-cluster-loadtest-sm',
  'k8s-cluster-e2e',
  'aws-topology',
  'local-dev',
];

const namespaceValues = [
  'kube-public',
  'kube-scheduler',
  'local-dev-namespace-1',
  'local-dev-namespace-2',
  'local-dev-namespace-3',
];

const durationValues = ['100s', '200s'];

const ValidatorMapValuePredicates = () => {
  const filterFieldRef = useRef<FormControlWithOverlayRef>(null);
  useEffect(() => {
    filterFieldRef.current?.validate();
  }, []);

  const validatorMap: FilterFieldValidatorMap = {
    keyPredicates: [
      {
        key: 'Cluster',
        valuePredicate: clusterValues,
        valueType: 'String',
      },
      {
        key: 'Namespace',
        valuePredicate: namespaceValues,
      },
      {
        key: 'Duration',
        valuePredicate: durationValues,
      },
    ],
  };

  return (
    <FormField>
      <FilterField
        aria-label="Filter data"
        ref={filterFieldRef}
        defaultValue={defaultValue}
        validatorMap={validatorMap}
        autoSuggestions
      />
      <FormFieldMessages />
    </FormField>
  );
};
```


### Additional and custom types

In addition to the built-in types (`Number`, `String`, `Boolean`, `Duration`,
`JSONPath`, `IPAddress`, `UID`, `Timestamp`, `SmartscapeId`), you can register
custom types using the `customTypes` prop. Custom types let you define
domain-specific validation logic and can be referenced in the `validatorMap`
just like built-in types by using `{ type: 'CustomTypeName' }` in the
`valuePredicate`.

Each custom type requires a validation function that returns `true` when a value
is valid for that type. Optionally, you can provide an icon to display in the
suggestions overlay.

```tsx
import { useEffect, useRef } from 'react';

import {
  FilterField,
  type FilterFieldCustomTypes,
  type FilterFieldRef,
  type FilterFieldValidatorMap,
} from '@dynatrace/strato-components/filters';
import {
  FormField,
  FormFieldMessages,
} from '@dynatrace/strato-components/forms';
import { MailIcon } from '@dynatrace/strato-icons';

const defaultValue = 'email = musterman@dynatrace.com OR email = dynatrace.com';

const customTypes: FilterFieldCustomTypes = {
  Email: {
    valuePredicate(value: string) {
      return value.includes('@');
    },
    icon: <MailIcon />,
  },
};

const validatorMap: FilterFieldValidatorMap = {
  keyPredicates: [
    {
      key: 'email',
      valueType: 'Email',
    },
  ],
};

const CustomTypes = () => {
  const filterFieldRef = useRef<FilterFieldRef>(null);
  useEffect(() => {
    filterFieldRef.current?.validate();
  }, []);

  return (
    <FormField>
      <FilterField
        aria-label="Filter data"
        ref={filterFieldRef}
        defaultValue={defaultValue}
        validatorMap={validatorMap}
        customTypes={customTypes}
        autoSuggestions
      />
      <FormFieldMessages />
    </FormField>
  );
};
```

```tsx
import { useEffect, useRef } from 'react';

import {
  FilterField,
  type FilterFieldCustomTypes,
  type FilterFieldRef,
  type FilterFieldValidatorMap,
} from '@dynatrace/strato-components/filters';
import {
  FormField,
  FormFieldMessages,
} from '@dynatrace/strato-components/forms';
import { MailIcon } from '@dynatrace/strato-icons';

const defaultValue = 'email = musterman@dynatrace.com OR email = dynatrace.com';

const customTypes: FilterFieldCustomTypes = {
  Email: {
    valuePredicate(value: string) {
      return value.includes('@');
    },
    icon: <MailIcon />,
  },
};

const validatorMap: FilterFieldValidatorMap = {
  keyPredicates: [
    {
      key: 'email',
      valueType: 'Email',
    },
  ],
};

const CustomTypes = () => {
  const filterFieldRef = useRef<FilterFieldRef>(null);
  useEffect(() => {
    filterFieldRef.current?.validate();
  }, []);

  return (
    <FormField>
      <FilterField
        aria-label="Filter data"
        ref={filterFieldRef}
        defaultValue={defaultValue}
        validatorMap={validatorMap}
        customTypes={customTypes}
        autoSuggestions
      />
      <FormFieldMessages />
    </FormField>
  );
};
```


### Suggestion Ordering

By default, key and value suggestions from the `validatorMap` are sorted
alphabetically for string values, numerically in ascending order for numbers,
and by unit order (smallest to largest, e.g. `ns`, `ms`, `s`, `m`, `h`) then
numerically within the same unit for durations. When the user types, suggestions
are reordered by match relevance: exact matches appear first, followed by
starts-with, and then contains or ends-with matches. Within each relevance tier,
alphabetical or ascending order is preserved.

To preserve the original order defined in `keyPredicates` and `valuePredicate`,
set `sortSuggestions: false` on the `validatorMap`. Relevance-based sorting when
the user is typing remains active regardless of this setting.

```tsx
import {
  FilterField,
  type FilterFieldValidatorMap,
} from '@dynatrace/strato-components/filters';

// Keys are defined in non-alphabetical order to show they appear alphabetically in suggestions.
// Numbers are placed before strings and sorted in ascending order.
const validatorMap: FilterFieldValidatorMap = {
  keyPredicates: [
    // Intentionally non-alphabetical: workload comes before cluster, namespace, age
    {
      key: 'workload',
      valuePredicate: ['frontend', 'backend', 'database', 'cache'],
    },
    {
      key: 'cluster',
      valuePredicate: [
        // Numbers are sorted in ascending order and shown before string values
        3,
        1,
        10,
        2,
        'cluster-eu-west',
        'cluster-us-east',
        'cluster-ap-south',
      ],
    },
    {
      key: 'namespace',
      valuePredicate: ['staging', 'production', 'development'],
    },
    {
      key: 'age',
      valueType: 'Number',
    },
  ],
  exhaustive: false,
};

const SuggestionOrdering = () => {
  return (
    <FilterField
      aria-label="Filter data"
      validatorMap={validatorMap}
      autoSuggestions
    />
  );
};
```

```tsx
import {
  FilterField,
  type FilterFieldValidatorMap,
} from '@dynatrace/strato-components/filters';

// Keys are defined in non-alphabetical order to show they appear alphabetically in suggestions.
// Numbers are placed before strings and sorted in ascending order.
const validatorMap: FilterFieldValidatorMap = {
  keyPredicates: [
    // Intentionally non-alphabetical: workload comes before cluster, namespace, age
    {
      key: 'workload',
      valuePredicate: ['frontend', 'backend', 'database', 'cache'],
    },
    {
      key: 'cluster',
      valuePredicate: [
        // Numbers are sorted in ascending order and shown before string values
        3,
        1,
        10,
        2,
        'cluster-eu-west',
        'cluster-us-east',
        'cluster-ap-south',
      ],
    },
    {
      key: 'namespace',
      valuePredicate: ['staging', 'production', 'development'],
    },
    {
      key: 'age',
      valueType: 'Number',
    },
  ],
  exhaustive: false,
};

const SuggestionOrdering = () => {
  return (
    <FilterField
      aria-label="Filter data"
      validatorMap={validatorMap}
      autoSuggestions
    />
  );
};
```


### Suggest full statements when typing values

Complete filter statements (key, operator, value) can be suggested automatically
based on typed input. This allows users to type a value like `error` and
immediately see suggestions like `status = error` without needing to know the
key name first.

To enable this feature, add `suggestStatementOnValueMatch` to the key predicate
in your `validatorMap`. The property accepts either:

- `true` — Enables statement suggestions for all values defined in the
`valuePredicate` array (suggestions are displayed for exact matches,
starts-with, ends-with, and contains matches)

- A function — A custom match function that receives the current token and
returns `true` if a statement suggestion should be shown

Statement suggestions always use the `=` (equals) comparison operator. If
multiple keys have the same value configured, suggestions for all matching keys
will be shown.

```tsx
import {
  FilterField,
  type FilterFieldValidatorMap,
  type FilterFieldLeafNode,
} from '@dynatrace/strato-components/filters';

// A custom match function that validates trace IDs (32-character hex strings)
const isValidTraceId = (currentToken: FilterFieldLeafNode) => {
  const traceIdRegex = /^[a-fA-F0-9]{32}$/;
  return traceIdRegex.test(currentToken.textValue);
};

const validatorMap: FilterFieldValidatorMap = {
  keyPredicates: [
    // Enable statement suggestions with a boolean for predefined values
    {
      key: 'status',
      valuePredicate: ['error', 'warning', 'info', 'success'],
      suggestStatementOnValueMatch: true,
    },
    // Multiple keys can share values - all will be suggested
    {
      key: 'environment',
      valuePredicate: ['dev', 'staging', 'prod'],
      suggestStatementOnValueMatch: true,
    },
    // Enable statement suggestions with a custom match function
    {
      key: 'traceId',
      valueType: 'String',
      suggestStatementOnValueMatch: isValidTraceId,
    },
  ],
  exhaustive: false,
};

const StatementSuggestions = () => {
  return (
    <FilterField
      aria-label="Filter data"
      validatorMap={validatorMap}
      autoSuggestions
    />
  );
};
```

```tsx
import {
  FilterField,
  type FilterFieldValidatorMap,
  type FilterFieldLeafNode,
} from '@dynatrace/strato-components/filters';

// A custom match function that validates trace IDs (32-character hex strings)
const isValidTraceId = (currentToken: FilterFieldLeafNode) => {
  const traceIdRegex = /^[a-fA-F0-9]{32}$/;
  return traceIdRegex.test(currentToken.textValue);
};

const validatorMap: FilterFieldValidatorMap = {
  keyPredicates: [
    // Enable statement suggestions with a boolean for predefined values
    {
      key: 'status',
      valuePredicate: ['error', 'warning', 'info', 'success'],
      suggestStatementOnValueMatch: true,
    },
    // Multiple keys can share values - all will be suggested
    {
      key: 'environment',
      valuePredicate: ['dev', 'staging', 'prod'],
      suggestStatementOnValueMatch: true,
    },
    // Enable statement suggestions with a custom match function
    {
      key: 'traceId',
      valueType: 'String',
      suggestStatementOnValueMatch: isValidTraceId,
    },
  ],
  exhaustive: false,
};

const StatementSuggestions = () => {
  return (
    <FilterField
      aria-label="Filter data"
      validatorMap={validatorMap}
      autoSuggestions
    />
  );
};
```


### Define fallback keys for free-text search

The `fallbackKey` property allows you to define commonly used keys that generate
suggestions using the currently typed token as the value. This is useful when
you want users to search within specific fields without knowing the exact key
name.

To enable this feature, add `fallbackKey` to the key predicate in your
`validatorMap`. The property accepts either:

- `true` — Generates statement suggestions using the `matches-phrase` (`~`)
operator

- An array of comparison operators — Generates one statement suggestion for each
specified operator

When a user starts typing in an empty `FilterField`, suggestions like
`content ~ typed-value` are shown, allowing quick searches in common fields.

The difference to `suggestStatementOnValueMatch` is that `fallbackKey` uses the
currently typed token as the value regardless of whether it matches predefined
values, while `suggestStatementOnValueMatch` only suggests statements when the
typed value matches values defined in the `valuePredicate`.

```tsx
import {
  FilterField,
  type FilterFieldValidatorMap,
} from '@dynatrace/strato-components/filters';

const validatorMap: FilterFieldValidatorMap = {
  keyPredicates: [
    // Use fallbackKey: true to suggest statements with matches-phrase (~) operator
    {
      key: 'content',
      fallbackKey: true,
    },
    // Use fallbackKey with an array of operators for specific comparison operators
    {
      key: 'status',
      valuePredicate: ['error', 'warning', 'info', 'success'],
      suggestStatementOnValueMatch: true,
      fallbackKey: ['equals', 'not-equals'],
    },
    // Regular key without fallbackKey - no fallback suggestions generated
    {
      key: 'environment',
      valuePredicate: ['dev', 'staging', 'prod'],
    },
  ],
  comparisonOperators: ['equals', 'not-equals', 'matches-phrase'],
  exhaustive: false,
};

const FallbackKey = () => {
  return (
    <FilterField
      aria-label="Filter data"
      validatorMap={validatorMap}
      autoSuggestions
    />
  );
};
```

```tsx
import {
  FilterField,
  type FilterFieldValidatorMap,
} from '@dynatrace/strato-components/filters';

const validatorMap: FilterFieldValidatorMap = {
  keyPredicates: [
    // Use fallbackKey: true to suggest statements with matches-phrase (~) operator
    {
      key: 'content',
      fallbackKey: true,
    },
    // Use fallbackKey with an array of operators for specific comparison operators
    {
      key: 'status',
      valuePredicate: ['error', 'warning', 'info', 'success'],
      suggestStatementOnValueMatch: true,
      fallbackKey: ['equals', 'not-equals'],
    },
    // Regular key without fallbackKey - no fallback suggestions generated
    {
      key: 'environment',
      valuePredicate: ['dev', 'staging', 'prod'],
    },
  ],
  comparisonOperators: ['equals', 'not-equals', 'matches-phrase'],
  exhaustive: false,
};

const FallbackKey = () => {
  return (
    <FilterField
      aria-label="Filter data"
      validatorMap={validatorMap}
      autoSuggestions
    />
  );
};
```


### Add display labels and descriptions to suggestions

You can enrich key and value suggestions from the `validatorMap` with a
`displayValue` (a human-readable label shown instead of the raw value) and
`details` (a secondary description). Both are optional and only affect the
suggestion overlay — they have no effect on validation or the applied filter
value.

For keys — add `displayValue` and `details` directly to the
`FilterFieldKeySuggestionConfig` object in `keyPredicates`.

For values — replace string, number, boolean, or duration entries in
`valuePredicate` with a `FilterFieldRichValuePredicate` object. Set `value` to
the actual filter value that gets applied. `displayValue` and `details` are
optional.

```tsx
const defaultValue =
  'Host = web-server-01 Namespace = namespace-1 Duration = 20ms ';

const validatorMap: FilterFieldValidatorMap = {
  keyPredicates: [
    {
      key: 'host',
      displayValue: 'Host',
      details: 'The host on which the monitored process is running.',
      valueType: 'String',
    },
    {
      key: 'namespace',
      displayValue: 'Namespace',
      details: 'The namespace associated with the monitored process.',
      valuePredicate: [
        {
          value: 'namespace-1',
          displayValue: 'Namespace 1',
          details: 'The first namespace',
        },
        {
          value: 'namespace-2',
          displayValue: 'Namespace 2',
          details: 'The second namespace',
        },
      ],
    },
  ],
};
```

```tsx
const defaultValue =
  'Host = web-server-01 Namespace = namespace-1 Duration = 20ms ';

const validatorMap: FilterFieldValidatorMap = {
  keyPredicates: [
    {
      key: 'host',
      displayValue: 'Host',
      details: 'The host on which the monitored process is running.',
      valueType: 'String',
    },
    {
      key: 'namespace',
      displayValue: 'Namespace',
      details: 'The namespace associated with the monitored process.',
      valuePredicate: [
        {
          value: 'namespace-1',
          displayValue: 'Namespace 1',
          details: 'The first namespace',
        },
        {
          value: 'namespace-2',
          displayValue: 'Namespace 2',
          details: 'The second namespace',
        },
      ],
    },
  ],
};
```


### Group key suggestions

Key suggestions from the `validatorMap` can be organized into labeled groups
using `FilterFieldKeySuggestionGroupConfig` objects in the `keyPredicates`
array.

The `keyPredicates` property accepts an array of key names (strings),
`FilterFieldKeySuggestionConfig` objects, or
`FilterFieldKeySuggestionGroupConfig` objects. The array format is required to
use key suggestion groups.

```tsx
const validatorMap: FilterFieldValidatorMap = {
  keyPredicates: [
    { key: 'host', valueType: 'String' },
    { key: 'service', valueType: 'String' },

    // Keys grouped under "Status"
    {
      label: 'Status',
      suggestions: [
        { key: 'status', valuePredicate: ['active', 'inactive', 'pending'] },
        { key: 'health', valuePredicate: ['healthy', 'unhealthy'] },
      ],
    },

    // Keys grouped under "Metrics"
    {
      label: 'Metrics',
      suggestions: [
        { key: 'cpu', valueType: 'Number' },
        { key: 'memory', valueType: 'Number' },
        { key: 'responseTime', valueType: 'Duration' },
      ],
    },
  ],
  exhaustive: false,
};
```

```tsx
const validatorMap: FilterFieldValidatorMap = {
  keyPredicates: [
    { key: 'host', valueType: 'String' },
    { key: 'service', valueType: 'String' },

    // Keys grouped under "Status"
    {
      label: 'Status',
      suggestions: [
        { key: 'status', valuePredicate: ['active', 'inactive', 'pending'] },
        { key: 'health', valuePredicate: ['healthy', 'unhealthy'] },
      ],
    },

    // Keys grouped under "Metrics"
    {
      label: 'Metrics',
      suggestions: [
        { key: 'cpu', valueType: 'Number' },
        { key: 'memory', valueType: 'Number' },
        { key: 'responseTime', valueType: 'Duration' },
      ],
    },
  ],
  exhaustive: false,
};
```


### Group value suggestions

Value suggestions for a key can be organized into labeled groups by replacing
string or number entries in `valuePredicate` with
`FilterFieldValueSuggestionGroupConfig` objects.

```tsx
const validatorMap: FilterFieldValidatorMap = {
  keyPredicates: [
    {
      key: 'severity',
      valuePredicate: [
        'info',

        // Values grouped under "Critical Levels"
        {
          label: 'Critical Levels',
          suggestions: ['critical', 'error'],
        },

        // Values grouped under "Warning Levels"
        {
          label: 'Warning Levels',
          suggestions: ['warning', 'notice'],
        },
      ],
    },
    {
      key: 'status',
      valuePredicate: [
        {
          label: 'Active States',
          suggestions: ['running', 'active', 'online'],
        },
        {
          label: 'Inactive States',
          suggestions: ['stopped', 'inactive', 'offline'],
        },
      ],
    },
  ],
};
```

```tsx
const validatorMap: FilterFieldValidatorMap = {
  keyPredicates: [
    {
      key: 'severity',
      valuePredicate: [
        'info',

        // Values grouped under "Critical Levels"
        {
          label: 'Critical Levels',
          suggestions: ['critical', 'error'],
        },

        // Values grouped under "Warning Levels"
        {
          label: 'Warning Levels',
          suggestions: ['warning', 'notice'],
        },
      ],
    },
    {
      key: 'status',
      valuePredicate: [
        {
          label: 'Active States',
          suggestions: ['running', 'active', 'online'],
        },
        {
          label: 'Inactive States',
          suggestions: ['stopped', 'inactive', 'offline'],
        },
      ],
    },
  ],
};
```


### Specify validation logic

To validate a value according to a particular logic, pass a validator function
to the `valuePredicate`. This allows you to write a custom error message in case
of an error. You can also use this approach to check whether a value follows a
particular pattern.

Make sure to pass only pure or cached functions and avoid calling
`convertStringToFilterFieldTree` in combination with a `validatorMap` inside of
the validator function, as this may cause infinite loops.

```tsx
import { useEffect, useRef } from 'react';

import {
  type FilterFieldStatementNode,
  type FilterFieldValidatorMap,
  FilterField,
} from '@dynatrace/strato-components/filters';
import {
  type FormControlWithOverlayRef,
  FormField,
  FormFieldMessages,
} from '@dynatrace/strato-components/forms';

const defaultValue = 'IPAddress = 0.0.0.0 IPAddress = 127.0.0.1.0 ';

const isValidIpAddress = (state: {
  currentStatement: FilterFieldStatementNode;
  filterFieldValue: string;
}) => {
  const ipAddressRegex = /^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$/;
  if (
    state.currentStatement.value?.type === 'String' &&
    ipAddressRegex.test(state.currentStatement.value.value)
  ) {
    return true;
  }

  return 'Invalid filter value. A full IP address is required for this key.';
};

const validatorMap: FilterFieldValidatorMap = {
  keyPredicates: [
    {
      key: 'IPAddress',
      valuePredicate: isValidIpAddress,
    },
  ],
};

const ValidatorMapValidatorFunction = () => {
  const filterFieldRef = useRef<FormControlWithOverlayRef>(null);
  useEffect(() => {
    filterFieldRef.current?.validate();
  }, []);

  return (
    <FormField>
      <FilterField
        aria-label="Filter data"
        ref={filterFieldRef}
        defaultValue={defaultValue}
        validatorMap={validatorMap}
        autoSuggestions
      />
      <FormFieldMessages />
    </FormField>
  );
};
```

```tsx
import { useEffect, useRef } from 'react';

import {
  type FilterFieldStatementNode,
  type FilterFieldValidatorMap,
  FilterField,
} from '@dynatrace/strato-components/filters';
import {
  type FormControlWithOverlayRef,
  FormField,
  FormFieldMessages,
} from '@dynatrace/strato-components/forms';

const defaultValue = 'IPAddress = 0.0.0.0 IPAddress = 127.0.0.1.0 ';

const isValidIpAddress = (state: {
  currentStatement: FilterFieldStatementNode;
  filterFieldValue: string;
}) => {
  const ipAddressRegex = /^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$/;
  if (
    state.currentStatement.value?.type === 'String' &&
    ipAddressRegex.test(state.currentStatement.value.value)
  ) {
    return true;
  }

  return 'Invalid filter value. A full IP address is required for this key.';
};

const validatorMap: FilterFieldValidatorMap = {
  keyPredicates: [
    {
      key: 'IPAddress',
      valuePredicate: isValidIpAddress,
    },
  ],
};

const ValidatorMapValidatorFunction = () => {
  const filterFieldRef = useRef<FormControlWithOverlayRef>(null);
  useEffect(() => {
    filterFieldRef.current?.validate();
  }, []);

  return (
    <FormField>
      <FilterField
        aria-label="Filter data"
        ref={filterFieldRef}
        defaultValue={defaultValue}
        validatorMap={validatorMap}
        autoSuggestions
      />
      <FormFieldMessages />
    </FormField>
  );
};
```


### Define comparison operators

The `validatorMap` property lets you define a list of comparison operators
globally (for all keys) or individually (per key). For any comparison operator
that isn't defined in the list, `FilterField` will show an error.

If you define comparison operators globally, be aware that the key types may
also narrow down the list of allowed comparison operators. If you define
comparison operators specifically for a key, they will overwrite restrictions
set by the type of the key.

```tsx
import { useEffect, useRef } from 'react';

import {
  type FilterFieldValidatorMap,
  FilterField,
} from '@dynatrace/strato-components/filters';
import {
  FormField,
  FormFieldMessages,
  type FormControlWithOverlayRef,
} from '@dynatrace/strato-components/forms';

const defaultValue =
  'Cluster ~ k8s-cluster-loadtest Namespace > local-dev-namespace-1 Health != true ';

const clusterValues = [
  'k8s-cluster-loadtest',
  'k8s-cluster-loadtest-sm',
  'k8s-cluster-e2e',
  'aws-topology',
  'local-dev',
];

const validatorMap: FilterFieldValidatorMap = {
  keyPredicates: [
    {
      key: 'Cluster',
      valuePredicate: clusterValues,
      comparisonOperators: ['equals', 'not-equals'],
    },
    {
      key: 'Health',
      valueType: 'Boolean',
    },
  ],
  comparisonOperators: ['equals'],
  exhaustive: false,
};

const ValidatorMapOperators = () => {
  const filterFieldRef = useRef<FormControlWithOverlayRef>(null);
  useEffect(() => {
    filterFieldRef.current?.validate();
  }, []);

  return (
    <FormField>
      <FilterField
        aria-label="Filter data"
        ref={filterFieldRef}
        defaultValue={defaultValue}
        validatorMap={validatorMap}
        autoSuggestions
      />
      <FormFieldMessages />
    </FormField>
  );
};
```

```tsx
import { useEffect, useRef } from 'react';

import {
  type FilterFieldValidatorMap,
  FilterField,
} from '@dynatrace/strato-components/filters';
import {
  FormField,
  FormFieldMessages,
  type FormControlWithOverlayRef,
} from '@dynatrace/strato-components/forms';

const defaultValue =
  'Cluster ~ k8s-cluster-loadtest Namespace > local-dev-namespace-1 Health != true ';

const clusterValues = [
  'k8s-cluster-loadtest',
  'k8s-cluster-loadtest-sm',
  'k8s-cluster-e2e',
  'aws-topology',
  'local-dev',
];

const validatorMap: FilterFieldValidatorMap = {
  keyPredicates: [
    {
      key: 'Cluster',
      valuePredicate: clusterValues,
      comparisonOperators: ['equals', 'not-equals'],
    },
    {
      key: 'Health',
      valueType: 'Boolean',
    },
  ],
  comparisonOperators: ['equals'],
  exhaustive: false,
};

const ValidatorMapOperators = () => {
  const filterFieldRef = useRef<FormControlWithOverlayRef>(null);
  useEffect(() => {
    filterFieldRef.current?.validate();
  }, []);

  return (
    <FormField>
      <FilterField
        aria-label="Filter data"
        ref={filterFieldRef}
        defaultValue={defaultValue}
        validatorMap={validatorMap}
        autoSuggestions
      />
      <FormFieldMessages />
    </FormField>
  );
};
```


### Work with syntax tree

`FilterField` provides a tokenized version of the entered value and groups
statements that are connected by the same logical operator. As the logical `AND`
takes precedence over the logical `OR`, the statements `a = 1 b = 2 OR c = 3`
will be grouped as follows:

Each statement is represented by a node holding the key, operator, and value of
the statement, provided as properties of the statement node. Depending on the
type of value and operator used, additional information (e.g. `starts-with`,
`contains`) is provided in the syntax tree.

If there is an error in the syntax, a node with type `Error` is included in the
syntax tree and the accompanying `isValid` flag is set to `false`.

```tsx
import { CodeEditor } from '@dynatrace/strato-components/editors';
import { convertStringToFilterFieldTree } from '@dynatrace/strato-components/filters';

const TreePrecedence = () => {
  return (
    <CodeEditor
      value={JSON.stringify(
        convertStringToFilterFieldTree('a = 1 b = 2 OR c = 3'),
        null,
        2
      )}
      readOnly
    />
  );
};
```

```tsx
import { CodeEditor } from '@dynatrace/strato-components/editors';
import { convertStringToFilterFieldTree } from '@dynatrace/strato-components/filters';

const TreePrecedence = () => {
  return (
    <CodeEditor
      value={JSON.stringify(
        convertStringToFilterFieldTree('a = 1 b = 2 OR c = 3'),
        null,
        2
      )}
      readOnly
    />
  );
};
```


#### Explicit logical operator nodes

Explicit logical operators are included in the syntax tree so it can be
converted back into a string without losing information. The logical operator
needed to evaluate a group of statements is included on the `Group` node. Ignore
logical operators in the `children` array of groups.

#### Convert string to syntax tree

Use the `convertStringToFilterFieldTree` utility to convert a string into a
`FilterTree`. Setting the value programmatically doesn't trigger the `onChange`
callback. Use the provided utility function for the converted syntax tree and
filter data.

#### Convert syntax tree to string

Use the `convertFilterFieldTreeToString` utility to convert a syntax tree to a
string.

CautionWe can't guarantee that converting a string to a tree and back yields the exact
same result. The `value` of every node (except for `Error` nodes) doesn't
contain escape characters (both wrapping doublequotes and backslashes). Hence,
the simple value `foo` may be written `"foo"`, `\f\o\o`, or using any other
combination of escape characters. With the `textValue` of tree nodes being
optional for the conversion util input, it is impossible to re-build the exact
same string as the original input for certain trees unless the `textValue` is
included.
This example demonstrates the conversion from string to tree, and back:

```tsx
import { useMemo, useState } from 'react';

import { CodeEditor } from '@dynatrace/strato-components/editors';
import {
  convertFilterFieldTreeToString,
  convertStringToFilterFieldTree,
  FilterField,
} from '@dynatrace/strato-components/filters';
import { FormField, Label } from '@dynatrace/strato-components/forms';
import { Grid } from '@dynatrace/strato-components/layouts';
import Colors from '@dynatrace/strato-design-tokens/colors';
import Spacings from '@dynatrace/strato-design-tokens/spacings';

const ConversionUtils = () => {
  const [value, setValue] = useState('Health = healthy');
  const [syntaxTree, setSyntaxTree] = useState(() =>
    JSON.stringify(convertStringToFilterFieldTree(value).tree, null, 2)
  );
  const convertedTree = useMemo(() => {
    try {
      return convertFilterFieldTreeToString(JSON.parse(syntaxTree));
    } catch {
      return undefined;
    }
  }, [syntaxTree]);

  return (
    <Grid style={{ position: 'relative' }}>
      <div
        style={{
          position: 'sticky',
          top: 0,
          padding: `${Spacings.Size4} 0`,
          backgroundColor: Colors.Background.Surface.Default,
          zIndex: 10,
        }}
      >
        <FormField>
          <Label>String to FilterField tree</Label>
          <FilterField
            defaultValue={value}
            onChange={(value, tree) => {
              setValue(value);
              setSyntaxTree(JSON.stringify(tree, null, 2));
            }}
            style={{ gridTemplateColumns: '1 / 3' }}
          />
        </FormField>
      </div>
      <CodeEditor
        language="ts"
        defaultFolding={[138, 291, 453]}
        value={syntaxTree}
        onChange={setSyntaxTree}
        style={{ marginBottom: Spacings.Size48 }}
      />
      <div
        style={{
          position: 'fixed',
          bottom: 0,
          width: `calc(100% - 2 * ${Spacings.Size16})`,
          padding: `${Spacings.Size4} 0`,
          backgroundColor: Colors.Background.Surface.Default,
        }}
      >
        <FormField>
          <Label>FilterField tree to string</Label>
          <FilterField value={convertedTree} onChange={() => null} readOnly />
        </FormField>
      </div>
    </Grid>
  );
};
```

```tsx
import { useMemo, useState } from 'react';

import { CodeEditor } from '@dynatrace/strato-components/editors';
import {
  convertFilterFieldTreeToString,
  convertStringToFilterFieldTree,
  FilterField,
} from '@dynatrace/strato-components/filters';
import { FormField, Label } from '@dynatrace/strato-components/forms';
import { Grid } from '@dynatrace/strato-components/layouts';
import Colors from '@dynatrace/strato-design-tokens/colors';
import Spacings from '@dynatrace/strato-design-tokens/spacings';

const ConversionUtils = () => {
  const [value, setValue] = useState('Health = healthy');
  const [syntaxTree, setSyntaxTree] = useState(() =>
    JSON.stringify(convertStringToFilterFieldTree(value).tree, null, 2)
  );
  const convertedTree = useMemo(() => {
    try {
      return convertFilterFieldTreeToString(JSON.parse(syntaxTree));
    } catch {
      return undefined;
    }
  }, [syntaxTree]);

  return (
    <Grid style={{ position: 'relative' }}>
      <div
        style={{
          position: 'sticky',
          top: 0,
          padding: `${Spacings.Size4} 0`,
          backgroundColor: Colors.Background.Surface.Default,
          zIndex: 10,
        }}
      >
        <FormField>
          <Label>String to FilterField tree</Label>
          <FilterField
            defaultValue={value}
            onChange={(value, tree) => {
              setValue(value);
              setSyntaxTree(JSON.stringify(tree, null, 2));
            }}
            style={{ gridTemplateColumns: '1 / 3' }}
          />
        </FormField>
      </div>
      <CodeEditor
        language="ts"
        defaultFolding={[138, 291, 453]}
        value={syntaxTree}
        onChange={setSyntaxTree}
        style={{ marginBottom: Spacings.Size48 }}
      />
      <div
        style={{
          position: 'fixed',
          bottom: 0,
          width: `calc(100% - 2 * ${Spacings.Size16})`,
          padding: `${Spacings.Size4} 0`,
          backgroundColor: Colors.Background.Surface.Default,
        }}
      >
        <FormField>
          <Label>FilterField tree to string</Label>
          <FilterField value={convertedTree} onChange={() => null} readOnly />
        </FormField>
      </div>
    </Grid>
  );
};
```


### Customize comparison operator suggestions

With the `autoSuggestions` prop set to true, relevant operator suggestions are
added automatically. To customize the suggestions, omit `autoSuggestions` and
use the returned `autoSuggestions` in the `onSuggest` callback. The `onSuggest`
callback provides the information you need to determine which suggestions to
show.

```tsx
import { useCallback, useState } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import {
  FilterField,
  FilterFieldGroupedSuggestions,
  FilterFieldSuggestion,
  FilterFieldSuggestionGroup,
  FilterFieldSuggestionsCallback,
  isFilterFieldListNode,
} from '@dynatrace/strato-components/filters';
import {
  FormField,
  FormFieldMessages,
} from '@dynatrace/strato-components/forms';
import { Grid } from '@dynatrace/strato-components/layouts';
import { RefreshIcon, PlayIcon } from '@dynatrace/strato-icons';

const keySuggestions = [
  { value: 'Health', details: 'Uses customized comparison operators.' },
  { value: 'Age' },
  { value: 'Cluster' },
  { value: 'Container count' },
  { value: 'Namespace' },
  { value: 'Namespace labels' },
  { value: 'Workload warning events' },
];

const valueSuggestions: Record<string, FilterFieldSuggestion[]> = {
  Health: [{ value: 'healthy' }, { value: 'unhealthy' }],
  Cluster: [
    { value: 'k8s-cluster-loadtest' },
    { value: 'k8s-cluster-loadtest-sm' },
    { value: 'k8s-cluster-e2e' },
    { value: 'aws-topology' },
    { value: 'local-dev' },
  ],
  'Workload warning events': [{ value: 'yes' }, { value: 'no' }],
  Namespace: [
    { value: 'kube-public' },
    { value: 'kube-scheduler' },
    { value: 'local-dev-namespace-1' },
    { value: 'local-dev-namespace-2' },
    { value: 'local-dev-namespace-3' },
  ],
  'Namespace labels': [
    { value: 'kubernetes.io/metadata.name : ab-cd-1' },
    { value: 'kubernetes.io/metadata.name : kube-public' },
  ],
};

/**
 * Shows the example of the FilterField with static suggestions.
 */
const FilteredAutoSuggestEntries = () => {
  const [value, setValue] = useState('');
  const [submittedValue, setSubmittedValue] = useState(value);

  const [suggestions, setSuggestions] = useState<FilterFieldGroupedSuggestions>(
    {}
  );
  const getSuggestions: FilterFieldSuggestionsCallback = useCallback(
    (state) => {
      if (state === undefined) {
        setSuggestions({});
        return;
      }

      const { currentTokens, currentStatement, groupedSuggestions } = state;

      const suggestions: Record<
        string,
        FilterFieldSuggestionGroup | undefined
      > = {};

      for (const currentToken of currentTokens) {
        const { type, token } = currentToken;
        switch (type) {
          case 'key':
            suggestions.key = {
              id: 'key-suggestions',
              label: 'Custom key label',
              suggestions: [
                ...keySuggestions.filter(
                  (suggestion) =>
                    token.value === '' ||
                    suggestion.value
                      ?.toLocaleLowerCase()
                      .includes(token.textValue.toLocaleLowerCase())
                ),
                ...(groupedSuggestions[type]?.suggestions ?? []),
              ],
            };
            break;
          case 'value':
            suggestions.value = {
              id: 'value-suggestions',
              label: 'Custom value label',
              suggestions: [
                ...(
                  valueSuggestions[currentStatement?.key?.value ?? ''] ?? []
                ).filter(
                  (suggestion) =>
                    isFilterFieldListNode(token) ||
                    token.value === '' ||
                    suggestion.value
                      ?.toLocaleLowerCase()
                      .includes(token.textValue.toLocaleLowerCase())
                ),
                ...(groupedSuggestions[type]?.suggestions ?? []),
              ],
            };
            break;
          case 'comparisonOperator': {
            if (currentStatement?.key?.value.toLowerCase().includes('age')) {
              suggestions.comparisonOperator = {
                id: 'comparison-operator-suggestions',
                label: 'Custom comparison operator label',
                suggestions: [
                  ...(groupedSuggestions[type]?.suggestions ?? []).filter(
                    ({ value }) => value === '>' || value === '<'
                  ),
                ],
              };
              return;
            }

            groupedSuggestions.comparisonOperator &&
              (suggestions.comparisonOperator =
                groupedSuggestions.comparisonOperator);
            break;
          }
        }
        setSuggestions(suggestions);
      }
    },
    []
  );

  return (
    <form
      onSubmit={(event) => {
        event.preventDefault();
        setSubmittedValue(value);
      }}
    >
      <FormField>
        <Grid gridTemplateColumns="1fr auto" gap={4}>
          <FilterField
            aria-label="Filter data"
            defaultValue={value}
            onChange={setValue}
            onSuggest={getSuggestions}
          >
            {Array.from(Object.values(suggestions)).map(
              (suggestionGroup) =>
                suggestionGroup && (
                  <FilterField.SuggestionGroup
                    key={suggestionGroup.id}
                    {...suggestionGroup}
                  />
                )
            )}
          </FilterField>
          <Button
            variant={value !== submittedValue ? 'accent' : 'emphasized'}
            color={value !== submittedValue ? 'primary' : 'neutral'}
            type="submit"
          >
            <Button.Prefix>
              {value === submittedValue ? <RefreshIcon /> : <PlayIcon />}
            </Button.Prefix>
            {value === submittedValue ? 'Refresh' : 'Update'}
          </Button>
        </Grid>
        <FormFieldMessages />
      </FormField>
    </form>
  );
};
```

```tsx
import { useCallback, useState } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import {
  FilterField,
  FilterFieldGroupedSuggestions,
  FilterFieldSuggestion,
  FilterFieldSuggestionGroup,
  FilterFieldSuggestionsCallback,
  isFilterFieldListNode,
} from '@dynatrace/strato-components/filters';
import {
  FormField,
  FormFieldMessages,
} from '@dynatrace/strato-components/forms';
import { Grid } from '@dynatrace/strato-components/layouts';
import { RefreshIcon, PlayIcon } from '@dynatrace/strato-icons';

const keySuggestions = [
  { value: 'Health', details: 'Uses customized comparison operators.' },
  { value: 'Age' },
  { value: 'Cluster' },
  { value: 'Container count' },
  { value: 'Namespace' },
  { value: 'Namespace labels' },
  { value: 'Workload warning events' },
];

const valueSuggestions: Record<string, FilterFieldSuggestion[]> = {
  Health: [{ value: 'healthy' }, { value: 'unhealthy' }],
  Cluster: [
    { value: 'k8s-cluster-loadtest' },
    { value: 'k8s-cluster-loadtest-sm' },
    { value: 'k8s-cluster-e2e' },
    { value: 'aws-topology' },
    { value: 'local-dev' },
  ],
  'Workload warning events': [{ value: 'yes' }, { value: 'no' }],
  Namespace: [
    { value: 'kube-public' },
    { value: 'kube-scheduler' },
    { value: 'local-dev-namespace-1' },
    { value: 'local-dev-namespace-2' },
    { value: 'local-dev-namespace-3' },
  ],
  'Namespace labels': [
    { value: 'kubernetes.io/metadata.name : ab-cd-1' },
    { value: 'kubernetes.io/metadata.name : kube-public' },
  ],
};

/**
 * Shows the example of the FilterField with static suggestions.
 */
const FilteredAutoSuggestEntries = () => {
  const [value, setValue] = useState('');
  const [submittedValue, setSubmittedValue] = useState(value);

  const [suggestions, setSuggestions] = useState<FilterFieldGroupedSuggestions>(
    {}
  );
  const getSuggestions: FilterFieldSuggestionsCallback = useCallback(
    (state) => {
      if (state === undefined) {
        setSuggestions({});
        return;
      }

      const { currentTokens, currentStatement, groupedSuggestions } = state;

      const suggestions: Record<
        string,
        FilterFieldSuggestionGroup | undefined
      > = {};

      for (const currentToken of currentTokens) {
        const { type, token } = currentToken;
        switch (type) {
          case 'key':
            suggestions.key = {
              id: 'key-suggestions',
              label: 'Custom key label',
              suggestions: [
                ...keySuggestions.filter(
                  (suggestion) =>
                    token.value === '' ||
                    suggestion.value
                      ?.toLocaleLowerCase()
                      .includes(token.textValue.toLocaleLowerCase())
                ),
                ...(groupedSuggestions[type]?.suggestions ?? []),
              ],
            };
            break;
          case 'value':
            suggestions.value = {
              id: 'value-suggestions',
              label: 'Custom value label',
              suggestions: [
                ...(
                  valueSuggestions[currentStatement?.key?.value ?? ''] ?? []
                ).filter(
                  (suggestion) =>
                    isFilterFieldListNode(token) ||
                    token.value === '' ||
                    suggestion.value
                      ?.toLocaleLowerCase()
                      .includes(token.textValue.toLocaleLowerCase())
                ),
                ...(groupedSuggestions[type]?.suggestions ?? []),
              ],
            };
            break;
          case 'comparisonOperator': {
            if (currentStatement?.key?.value.toLowerCase().includes('age')) {
              suggestions.comparisonOperator = {
                id: 'comparison-operator-suggestions',
                label: 'Custom comparison operator label',
                suggestions: [
                  ...(groupedSuggestions[type]?.suggestions ?? []).filter(
                    ({ value }) => value === '>' || value === '<'
                  ),
                ],
              };
              return;
            }

            groupedSuggestions.comparisonOperator &&
              (suggestions.comparisonOperator =
                groupedSuggestions.comparisonOperator);
            break;
          }
        }
        setSuggestions(suggestions);
      }
    },
    []
  );

  return (
    <form
      onSubmit={(event) => {
        event.preventDefault();
        setSubmittedValue(value);
      }}
    >
      <FormField>
        <Grid gridTemplateColumns="1fr auto" gap={4}>
          <FilterField
            aria-label="Filter data"
            defaultValue={value}
            onChange={setValue}
            onSuggest={getSuggestions}
          >
            {Array.from(Object.values(suggestions)).map(
              (suggestionGroup) =>
                suggestionGroup && (
                  <FilterField.SuggestionGroup
                    key={suggestionGroup.id}
                    {...suggestionGroup}
                  />
                )
            )}
          </FilterField>
          <Button
            variant={value !== submittedValue ? 'accent' : 'emphasized'}
            color={value !== submittedValue ? 'primary' : 'neutral'}
            type="submit"
          >
            <Button.Prefix>
              {value === submittedValue ? <RefreshIcon /> : <PlayIcon />}
            </Button.Prefix>
            {value === submittedValue ? 'Refresh' : 'Update'}
          </Button>
        </Grid>
        <FormFieldMessages />
      </FormField>
    </form>
  );
};
```


### Escape characters in suggestions

`FilterField` uses `space` as a delimiter between keys, comparison operators,
values, and statements. Learn the
filter field syntax.

To avoid invalid syntax when suggestions are applied, use the `value` prop and
the children of the `FilterField.Suggestion` component. The `value` is used to
apply the suggestion, while the `children` are used to render the suggestion in
the overlay.

In general, the following characters need to be escaped, either by wrapping the
whole value in double quotes, or by using a `\` to escape single characters:

- Asterisk

- , Comma

- () Parentheses

- ! Exclamation

- Angles

- = Equals

- " Quote

- $ Dollar sign

- : Colon

- [] Brackets

- ~ Tilde

When the insertion strategy for suggestions is set to `replace-token`, the
applied value is automatically escaped, if needed.

The following examples are also valid for keys:

- Exact match of comparison operator

- `foo = \=`

- `foo = \

- `foo = ">"`

- `foo = "!="`

- Starts with / ends with operator in value

- `foo = *"ba*r"` (ends with `ba*r`)

- `foo = ba\*r*` (starts with `ba*r`)

- `foo = *"ba*r"*` (contains `ba*r`)

- Space in value

- `foo = "b a r"`

- `foo = b\ ar`

#### Programmatically escape suggestion values

The `escapeFilterFieldSuggestion` utility allows you to escape suggestion
values. This is the same function applied internally by the `FilterField`,
making it ideal for verifying that manually escaped values match the expected
format.

### Group suggestions

If there are many suggestions that fit into different categories, you can use
`FilterField.SuggestionGroup` to separate them visually. Use the
`FilterField.SuggestionGroupLabel` to add short labels above the groups.

```tsx
import { useCallback, useState } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import {
  FilterField,
  FilterFieldSuggestion,
  FilterFieldSuggestionsCallback,
  isFilterFieldListNode,
} from '@dynatrace/strato-components/filters';
import {
  FormField,
  FormFieldMessages,
} from '@dynatrace/strato-components/forms';
import { Grid } from '@dynatrace/strato-components/layouts';
import { RefreshIcon, PlayIcon } from '@dynatrace/strato-icons';

const recommendedKeySuggestions = [{ value: 'Cluster' }, { value: 'Health' }];

const otherKeySuggestions = [
  { value: 'Age' },
  { value: 'Container count' },
  { value: 'Namespace' },
  { value: 'Namespace labels' },
  { value: 'Workload warning events' },
];

const valueSuggestions: Record<string, FilterFieldSuggestion[]> = {
  Health: [{ value: 'healthy' }, { value: 'unhealthy' }],
  Cluster: [
    { value: 'k8s-cluster-loadtest' },
    { value: 'k8s-cluster-loadtest-sm' },
    { value: 'k8s-cluster-e2e' },
    { value: 'aws-topology' },
    { value: 'local-dev' },
  ],
  'Workload warning events': [{ value: 'yes' }, { value: 'no' }],
  Namespace: [
    { value: 'kube-public' },
    { value: 'kube-scheduler' },
    { value: 'local-dev-namespace-1' },
    { value: 'local-dev-namespace-2' },
    { value: 'local-dev-namespace-3' },
  ],
  'Namespace labels': [
    { value: 'kubernetes.io/metadata.name : ab-cd-1' },
    { value: 'kubernetes.io/metadata.name : kube-public' },
  ],
};

/**
 * Shows the example of the FilterField with static suggestions.
 */
const SuggestionDetailsAndGroups = () => {
  const [value, setValue] = useState('');
  const [submittedValue, setSubmittedValue] = useState(value);

  const [suggestions, setSuggestions] = useState<
    { group: string | undefined; suggestions: FilterFieldSuggestion[] }[]
  >([]);
  const getSuggestions: FilterFieldSuggestionsCallback = useCallback(
    (state) => {
      if (state === undefined) {
        setSuggestions([]);
        return;
      }

      const { currentTokens, currentStatement } = state;
      for (const currentToken of currentTokens) {
        const { type, token } = currentToken;

        switch (type) {
          case 'key':
            setSuggestions([
              {
                group: 'Recommended',
                suggestions: [
                  ...recommendedKeySuggestions.filter(
                    (suggestion) =>
                      isFilterFieldListNode(token) ||
                      token.value === '' ||
                      suggestion.value
                        ?.toLowerCase()
                        .includes(token.textValue.toLowerCase())
                  ),
                ],
              },
              {
                group: 'Other',
                suggestions: [
                  ...otherKeySuggestions.filter(
                    (suggestion) =>
                      isFilterFieldListNode(token) ||
                      token.value === '' ||
                      suggestion.value
                        ?.toLowerCase()
                        .includes(token.textValue.toLowerCase())
                  ),
                ],
              },
            ]);
            break;
          case 'value':
            setSuggestions([
              {
                group: undefined,
                suggestions: [
                  ...(
                    valueSuggestions[currentStatement?.key?.value ?? ''] ?? []
                  ).filter(
                    (suggestion) =>
                      isFilterFieldListNode(token) ||
                      token.value === '' ||
                      suggestion.value
                        ?.toLowerCase()
                        .includes(token.textValue.toLowerCase())
                  ),
                ],
              },
            ]);
            break;
          default:
            setSuggestions([]);
        }
      }
    },
    []
  );

  return (
    <form
      onSubmit={(event) => {
        event.preventDefault();
        setSubmittedValue(value);
      }}
    >
      <FormField>
        <Grid gridTemplateColumns="1fr auto" gap={4}>
          <FilterField
            aria-label="Filter data"
            defaultValue={value}
            onChange={setValue}
            onSuggest={getSuggestions}
            autoSuggestions
          >
            {suggestions?.map((suggestion) => (
              <FilterField.SuggestionGroup>
                {suggestion.group && (
                  <FilterField.SuggestionGroupLabel>
                    {suggestion.group}
                  </FilterField.SuggestionGroupLabel>
                )}
                {suggestion.suggestions?.map((suggestion) => (
                  <FilterField.Suggestion
                    key={suggestion.value}
                    {...suggestion}
                  />
                ))}
              </FilterField.SuggestionGroup>
            ))}
          </FilterField>
          <Button
            variant={value !== submittedValue ? 'accent' : 'emphasized'}
            color={value !== submittedValue ? 'primary' : 'neutral'}
            type="submit"
          >
            <Button.Prefix>
              {value === submittedValue ? <RefreshIcon /> : <PlayIcon />}
            </Button.Prefix>
            {value === submittedValue ? 'Refresh' : 'Update'}
          </Button>
        </Grid>
        <FormFieldMessages />
      </FormField>
    </form>
  );
};
```

```tsx
import { useCallback, useState } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import {
  FilterField,
  FilterFieldSuggestion,
  FilterFieldSuggestionsCallback,
  isFilterFieldListNode,
} from '@dynatrace/strato-components/filters';
import {
  FormField,
  FormFieldMessages,
} from '@dynatrace/strato-components/forms';
import { Grid } from '@dynatrace/strato-components/layouts';
import { RefreshIcon, PlayIcon } from '@dynatrace/strato-icons';

const recommendedKeySuggestions = [{ value: 'Cluster' }, { value: 'Health' }];

const otherKeySuggestions = [
  { value: 'Age' },
  { value: 'Container count' },
  { value: 'Namespace' },
  { value: 'Namespace labels' },
  { value: 'Workload warning events' },
];

const valueSuggestions: Record<string, FilterFieldSuggestion[]> = {
  Health: [{ value: 'healthy' }, { value: 'unhealthy' }],
  Cluster: [
    { value: 'k8s-cluster-loadtest' },
    { value: 'k8s-cluster-loadtest-sm' },
    { value: 'k8s-cluster-e2e' },
    { value: 'aws-topology' },
    { value: 'local-dev' },
  ],
  'Workload warning events': [{ value: 'yes' }, { value: 'no' }],
  Namespace: [
    { value: 'kube-public' },
    { value: 'kube-scheduler' },
    { value: 'local-dev-namespace-1' },
    { value: 'local-dev-namespace-2' },
    { value: 'local-dev-namespace-3' },
  ],
  'Namespace labels': [
    { value: 'kubernetes.io/metadata.name : ab-cd-1' },
    { value: 'kubernetes.io/metadata.name : kube-public' },
  ],
};

/**
 * Shows the example of the FilterField with static suggestions.
 */
const SuggestionDetailsAndGroups = () => {
  const [value, setValue] = useState('');
  const [submittedValue, setSubmittedValue] = useState(value);

  const [suggestions, setSuggestions] = useState<
    { group: string | undefined; suggestions: FilterFieldSuggestion[] }[]
  >([]);
  const getSuggestions: FilterFieldSuggestionsCallback = useCallback(
    (state) => {
      if (state === undefined) {
        setSuggestions([]);
        return;
      }

      const { currentTokens, currentStatement } = state;
      for (const currentToken of currentTokens) {
        const { type, token } = currentToken;

        switch (type) {
          case 'key':
            setSuggestions([
              {
                group: 'Recommended',
                suggestions: [
                  ...recommendedKeySuggestions.filter(
                    (suggestion) =>
                      isFilterFieldListNode(token) ||
                      token.value === '' ||
                      suggestion.value
                        ?.toLowerCase()
                        .includes(token.textValue.toLowerCase())
                  ),
                ],
              },
              {
                group: 'Other',
                suggestions: [
                  ...otherKeySuggestions.filter(
                    (suggestion) =>
                      isFilterFieldListNode(token) ||
                      token.value === '' ||
                      suggestion.value
                        ?.toLowerCase()
                        .includes(token.textValue.toLowerCase())
                  ),
                ],
              },
            ]);
            break;
          case 'value':
            setSuggestions([
              {
                group: undefined,
                suggestions: [
                  ...(
                    valueSuggestions[currentStatement?.key?.value ?? ''] ?? []
                  ).filter(
                    (suggestion) =>
                      isFilterFieldListNode(token) ||
                      token.value === '' ||
                      suggestion.value
                        ?.toLowerCase()
                        .includes(token.textValue.toLowerCase())
                  ),
                ],
              },
            ]);
            break;
          default:
            setSuggestions([]);
        }
      }
    },
    []
  );

  return (
    <form
      onSubmit={(event) => {
        event.preventDefault();
        setSubmittedValue(value);
      }}
    >
      <FormField>
        <Grid gridTemplateColumns="1fr auto" gap={4}>
          <FilterField
            aria-label="Filter data"
            defaultValue={value}
            onChange={setValue}
            onSuggest={getSuggestions}
            autoSuggestions
          >
            {suggestions?.map((suggestion) => (
              <FilterField.SuggestionGroup>
                {suggestion.group && (
                  <FilterField.SuggestionGroupLabel>
                    {suggestion.group}
                  </FilterField.SuggestionGroupLabel>
                )}
                {suggestion.suggestions?.map((suggestion) => (
                  <FilterField.Suggestion
                    key={suggestion.value}
                    {...suggestion}
                  />
                ))}
              </FilterField.SuggestionGroup>
            ))}
          </FilterField>
          <Button
            variant={value !== submittedValue ? 'accent' : 'emphasized'}
            color={value !== submittedValue ? 'primary' : 'neutral'}
            type="submit"
          >
            <Button.Prefix>
              {value === submittedValue ? <RefreshIcon /> : <PlayIcon />}
            </Button.Prefix>
            {value === submittedValue ? 'Refresh' : 'Update'}
          </Button>
        </Grid>
        <FormFieldMessages />
      </FormField>
    </form>
  );
};
```


### Load suggestions async

To load suggestions async and display a loading state in the suggestions
overlay, set the `loading` prop on `FilterField.Suggestions`.

```tsx
import { useCallback, useState } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import {
  FilterField,
  FilterFieldSuggestionsCallback,
  isFilterFieldListNode,
  type FilterFieldSuggestion,
} from '@dynatrace/strato-components/filters';
import {
  FormField,
  FormFieldMessages,
} from '@dynatrace/strato-components/forms';
import { Grid } from '@dynatrace/strato-components/layouts';
import { PlayIcon, RefreshIcon } from '@dynatrace/strato-icons';

const keySuggestions = [
  { value: 'Age' },
  { value: 'Cluster' },
  { value: 'Container count' },
  { value: 'Health' },
  { value: 'Namespace' },
  { value: 'Namespace labels' },
  { value: 'Workload warning events' },
];

const valueSuggestions: Record<string, FilterFieldSuggestion[]> = {
  Health: [{ value: 'healthy' }, { value: 'unhealthy' }],
  Cluster: [
    { value: 'k8s-cluster-loadtest' },
    { value: 'k8s-cluster-loadtest-sm' },
    { value: 'k8s-cluster-e2e' },
    { value: 'aws-topology' },
    { value: 'local-dev' },
  ],
  'Workload warning events': [{ value: 'yes' }, { value: 'no' }],
  Namespace: [
    { value: 'kube-public' },
    { value: 'kube-scheduler' },
    { value: 'local-dev-namespace-1' },
    { value: 'local-dev-namespace-2' },
    { value: 'local-dev-namespace-3' },
  ],
  'Namespace labels': [
    { value: 'kubernetes.io/metadata.name : ab-cd-1' },
    { value: 'kubernetes.io/metadata.name : kube-public' },
  ],
};

/**
 * Shows the example of the FilterField with async suggestions.
 */
const AsyncSuggestions = () => {
  const [value, setValue] = useState('Health = healthy ');
  const [submittedValue, setSubmittedValue] = useState(value);

  const [suggestions, setSuggestions] = useState<
    FilterFieldSuggestion[] | undefined
  >(keySuggestions);
  const [loading, setLoading] = useState(false);
  const getSuggestions: FilterFieldSuggestionsCallback = useCallback(
    (state) => {
      if (state === undefined) {
        setSuggestions([]);
        return;
      }

      const { currentTokens, currentStatement } = state;

      setLoading(true);

      setTimeout(() => {
        setLoading(false);
        for (const currentToken of currentTokens) {
          const { token, type } = currentToken;

          switch (type) {
            case 'key':
              setSuggestions([
                ...keySuggestions.filter(
                  (suggestion) =>
                    isFilterFieldListNode(token) ||
                    token.value === '' ||
                    suggestion.value
                      ?.toLowerCase()
                      .includes(token.textValue.toLowerCase())
                ),
              ]);
              break;
            case 'value':
              setSuggestions([
                ...(
                  valueSuggestions[currentStatement?.key?.value ?? ''] ?? []
                ).filter(
                  (suggestion) =>
                    isFilterFieldListNode(token) ||
                    token.value === '' ||
                    suggestion.value
                      ?.toLowerCase()
                      .includes(token.textValue.toLowerCase())
                ),
              ]);
              break;
            default:
              setSuggestions([]);
          }
        }
      }, 2000);
    },
    []
  );

  return (
    <form
      onSubmit={(event) => {
        event.preventDefault();
        setSubmittedValue(value);
      }}
    >
      <FormField>
        <Grid gridTemplateColumns="1fr auto" gap={4}>
          <FilterField
            aria-label="Filter data"
            defaultValue={value}
            onChange={setValue}
            onSuggest={getSuggestions}
            autoSuggestions
          >
            <FilterField.Suggestions loading={loading}>
              {suggestions?.map((suggestion) => (
                <FilterField.Suggestion
                  key={suggestion.value}
                  {...suggestion}
                />
              ))}
            </FilterField.Suggestions>
          </FilterField>
          <Button
            variant={value !== submittedValue ? 'accent' : 'emphasized'}
            color={value !== submittedValue ? 'primary' : 'neutral'}
            type="submit"
          >
            <Button.Prefix>
              {value === submittedValue ? <RefreshIcon /> : <PlayIcon />}
            </Button.Prefix>
            {value === submittedValue ? 'Refresh' : 'Update'}
          </Button>
        </Grid>
        <FormFieldMessages />
      </FormField>
    </form>
  );
};
```

```tsx
import { useCallback, useState } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import {
  FilterField,
  FilterFieldSuggestionsCallback,
  isFilterFieldListNode,
  type FilterFieldSuggestion,
} from '@dynatrace/strato-components/filters';
import {
  FormField,
  FormFieldMessages,
} from '@dynatrace/strato-components/forms';
import { Grid } from '@dynatrace/strato-components/layouts';
import { PlayIcon, RefreshIcon } from '@dynatrace/strato-icons';

const keySuggestions = [
  { value: 'Age' },
  { value: 'Cluster' },
  { value: 'Container count' },
  { value: 'Health' },
  { value: 'Namespace' },
  { value: 'Namespace labels' },
  { value: 'Workload warning events' },
];

const valueSuggestions: Record<string, FilterFieldSuggestion[]> = {
  Health: [{ value: 'healthy' }, { value: 'unhealthy' }],
  Cluster: [
    { value: 'k8s-cluster-loadtest' },
    { value: 'k8s-cluster-loadtest-sm' },
    { value: 'k8s-cluster-e2e' },
    { value: 'aws-topology' },
    { value: 'local-dev' },
  ],
  'Workload warning events': [{ value: 'yes' }, { value: 'no' }],
  Namespace: [
    { value: 'kube-public' },
    { value: 'kube-scheduler' },
    { value: 'local-dev-namespace-1' },
    { value: 'local-dev-namespace-2' },
    { value: 'local-dev-namespace-3' },
  ],
  'Namespace labels': [
    { value: 'kubernetes.io/metadata.name : ab-cd-1' },
    { value: 'kubernetes.io/metadata.name : kube-public' },
  ],
};

/**
 * Shows the example of the FilterField with async suggestions.
 */
const AsyncSuggestions = () => {
  const [value, setValue] = useState('Health = healthy ');
  const [submittedValue, setSubmittedValue] = useState(value);

  const [suggestions, setSuggestions] = useState<
    FilterFieldSuggestion[] | undefined
  >(keySuggestions);
  const [loading, setLoading] = useState(false);
  const getSuggestions: FilterFieldSuggestionsCallback = useCallback(
    (state) => {
      if (state === undefined) {
        setSuggestions([]);
        return;
      }

      const { currentTokens, currentStatement } = state;

      setLoading(true);

      setTimeout(() => {
        setLoading(false);
        for (const currentToken of currentTokens) {
          const { token, type } = currentToken;

          switch (type) {
            case 'key':
              setSuggestions([
                ...keySuggestions.filter(
                  (suggestion) =>
                    isFilterFieldListNode(token) ||
                    token.value === '' ||
                    suggestion.value
                      ?.toLowerCase()
                      .includes(token.textValue.toLowerCase())
                ),
              ]);
              break;
            case 'value':
              setSuggestions([
                ...(
                  valueSuggestions[currentStatement?.key?.value ?? ''] ?? []
                ).filter(
                  (suggestion) =>
                    isFilterFieldListNode(token) ||
                    token.value === '' ||
                    suggestion.value
                      ?.toLowerCase()
                      .includes(token.textValue.toLowerCase())
                ),
              ]);
              break;
            default:
              setSuggestions([]);
          }
        }
      }, 2000);
    },
    []
  );

  return (
    <form
      onSubmit={(event) => {
        event.preventDefault();
        setSubmittedValue(value);
      }}
    >
      <FormField>
        <Grid gridTemplateColumns="1fr auto" gap={4}>
          <FilterField
            aria-label="Filter data"
            defaultValue={value}
            onChange={setValue}
            onSuggest={getSuggestions}
            autoSuggestions
          >
            <FilterField.Suggestions loading={loading}>
              {suggestions?.map((suggestion) => (
                <FilterField.Suggestion
                  key={suggestion.value}
                  {...suggestion}
                />
              ))}
            </FilterField.Suggestions>
          </FilterField>
          <Button
            variant={value !== submittedValue ? 'accent' : 'emphasized'}
            color={value !== submittedValue ? 'primary' : 'neutral'}
            type="submit"
          >
            <Button.Prefix>
              {value === submittedValue ? <RefreshIcon /> : <PlayIcon />}
            </Button.Prefix>
            {value === submittedValue ? 'Refresh' : 'Update'}
          </Button>
        </Grid>
        <FormFieldMessages />
      </FormField>
    </form>
  );
};
```


### Limit suggestions shown

To limit the number of default suggestions rendered, provide the
`defaultSuggestionsCount` config. You can set limits for an empty and a filled
`FilterField`.

If the suggestions exceed the limit, a show more / less button will be rendered
to expand / collapse the remaining suggestions.

```tsx
import { useMemo } from 'react';

import {
  FilterField,
  FilterFieldValidatorMap,
} from '@dynatrace/strato-components/filters';

const ShowMore = () => {
  const validatorMap = useMemo<FilterFieldValidatorMap>(
    () => ({
      keyPredicates: [
        'Age',
        'Cluster',
        'Container count',
        'Health',
        'Namespace',
        'Namespace labels',
        'Workload warning events',
      ],
    }),
    []
  );

  return (
    <FilterField
      aria-label="Filter data"
      defaultSuggestionsCount={{ empty: 3, filled: 5 }}
      validatorMap={validatorMap}
      autoSuggestions
    />
  );
};
```

```tsx
import { useMemo } from 'react';

import {
  FilterField,
  FilterFieldValidatorMap,
} from '@dynatrace/strato-components/filters';

const ShowMore = () => {
  const validatorMap = useMemo<FilterFieldValidatorMap>(
    () => ({
      keyPredicates: [
        'Age',
        'Cluster',
        'Container count',
        'Health',
        'Namespace',
        'Namespace labels',
        'Workload warning events',
      ],
    }),
    []
  );

  return (
    <FilterField
      aria-label="Filter data"
      defaultSuggestionsCount={{ empty: 3, filled: 5 }}
      validatorMap={validatorMap}
      autoSuggestions
    />
  );
};
```


### Persist recent and pinned filters

To enhance user experience and streamline workflows, `FilterField` supports
persisting recent and pinned filters across sessions. This feature stores
user-defined filters in the Dynatrace platform's `userAppState`, allowing users
to quickly reapply commonly used filters.

To enable this feature, set the `filterNamespace` prop on the `FilterField`
component. This string value acts as a unique identifier for the storage scope.
Filters are persisted per user and namespace, ensuring isolation between
different use cases or components under the keys
`strato-FilterField-pinnedFilters-{filterNameSpace}` and
`strato-FilterField-recentFilters-{filterNameSpace}`.

CautionIf your application uses namespaced recent and pinned filters that are no longer
relevant or supported, it is your responsibility to explicitly clean them up in
the application code. The system does not automatically remove unused namespaces
from the userAppState.

```tsx
import { useRef } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import {
  FilterField,
  FilterFieldRef,
} from '@dynatrace/strato-components/filters';
import { Grid } from '@dynatrace/strato-components/layouts';

const RecentAndPinned = () => {
  const filterFieldRef = useRef<FilterFieldRef>(null);

  return (
    <Grid gridTemplateColumns="1fr max-content">
      <FilterField
        aria-label="Filter data"
        ref={filterFieldRef}
        filterNamespace="root"
        autoSuggestions
      />
      <Button onClick={() => filterFieldRef.current?.saveRecentFilter()}>
        Apply
      </Button>
    </Grid>
  );
};
```

```tsx
import { useRef } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import {
  FilterField,
  FilterFieldRef,
} from '@dynatrace/strato-components/filters';
import { Grid } from '@dynatrace/strato-components/layouts';

const RecentAndPinned = () => {
  const filterFieldRef = useRef<FilterFieldRef>(null);

  return (
    <Grid gridTemplateColumns="1fr max-content">
      <FilterField
        aria-label="Filter data"
        ref={filterFieldRef}
        filterNamespace="root"
        autoSuggestions
      />
      <Button onClick={() => filterFieldRef.current?.saveRecentFilter()}>
        Apply
      </Button>
    </Grid>
  );
};
```


### Use the FilterField in a form

The user can submit a filter statement using `Enter` or `Ctrl / Cmd + Enter`.
This triggers the `onFilter` callback, which provides the string representation
of the value, the syntax tree, and its validity state. Clearing the
`FilterField` also triggers the `onFilter` callback.

`FilterField` can be displayed in a form. By default, the form shows a set of
error messages based on the entered value, rendered as tooltips. Use the
`FormField` to make the error state visible and add an error message beneath the
`FilterField`. Learn about using the `FormField`
here.

To provide the same functionality for pointer users, add a dedicated button next
to the `FilterField`, as outlined in Usage.

```tsx
import { useState } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import { FilterField } from '@dynatrace/strato-components/filters';
import {
  FormField,
  FormFieldMessages,
} from '@dynatrace/strato-components/forms';
import { Grid } from '@dynatrace/strato-components/layouts';
import { PlayIcon, RefreshIcon } from '@dynatrace/strato-icons';

const FormValidation = () => {
  const [value, setValue] = useState('');
  const [submittedValue, setSubmittedValue] = useState(value);

  return (
    <form
      onSubmit={(event) => {
        event.preventDefault();
        setSubmittedValue(value);
      }}
    >
      <FormField>
        <Grid gridTemplateColumns="1fr auto" gap={4}>
          <FilterField
            aria-label="Filter data"
            value={value}
            onChange={setValue}
            autoSuggestions
          />
          <Button
            variant={value !== submittedValue ? 'accent' : 'emphasized'}
            color={value !== submittedValue ? 'primary' : 'neutral'}
            type="submit"
          >
            <Button.Prefix>
              {value === submittedValue ? <RefreshIcon /> : <PlayIcon />}
            </Button.Prefix>
            {value === submittedValue ? 'Refresh' : 'Update'}
          </Button>
        </Grid>
        <FormFieldMessages />
      </FormField>
    </form>
  );
};
```

```tsx
import { useState } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import { FilterField } from '@dynatrace/strato-components/filters';
import {
  FormField,
  FormFieldMessages,
} from '@dynatrace/strato-components/forms';
import { Grid } from '@dynatrace/strato-components/layouts';
import { PlayIcon, RefreshIcon } from '@dynatrace/strato-icons';

const FormValidation = () => {
  const [value, setValue] = useState('');
  const [submittedValue, setSubmittedValue] = useState(value);

  return (
    <form
      onSubmit={(event) => {
        event.preventDefault();
        setSubmittedValue(value);
      }}
    >
      <FormField>
        <Grid gridTemplateColumns="1fr auto" gap={4}>
          <FilterField
            aria-label="Filter data"
            value={value}
            onChange={setValue}
            autoSuggestions
          />
          <Button
            variant={value !== submittedValue ? 'accent' : 'emphasized'}
            color={value !== submittedValue ? 'primary' : 'neutral'}
            type="submit"
          >
            <Button.Prefix>
              {value === submittedValue ? <RefreshIcon /> : <PlayIcon />}
            </Button.Prefix>
            {value === submittedValue ? 'Refresh' : 'Update'}
          </Button>
        </Grid>
        <FormFieldMessages />
      </FormField>
    </form>
  );
};
```


### Variables

Variables are a default feature of every `FilterField`. Any value starting with
`$` is automatically interpreted as a variable and returned as type `Variable`
in the value node.

Use the `validatorMap` to allow only specific variables or variable patterns.

```tsx
import { useCallback, useEffect, useRef } from 'react';

import {
  FilterField,
  type FilterFieldStatementNode,
  type FilterFieldValidatorMap,
} from '@dynatrace/strato-components/filters';
import {
  FormField,
  type FormControlWithOverlayRef,
} from '@dynatrace/strato-components/forms';

const Variables = () => {
  const isValidVariablePattern = useCallback(
    (state: {
      currentStatement: FilterFieldStatementNode;
      filterFieldValue: string;
    }) => {
      if (state.currentStatement.value?.type === 'Variable') {
        const variableRegex = /^\$\w+$/;

        return variableRegex.test(state.currentStatement.value.value)
          ? true
          : 'Only alpha-numerical values and underscores are allowed in variables.';
      }

      return true;
    },
    []
  );

  const validatorMap: FilterFieldValidatorMap = {
    keyPredicates: [
      {
        key: 'patternForVariables',
        valuePredicate: isValidVariablePattern,
      },
      {
        key: 'specificVariables',
        valuePredicate: ['$a', '$b', '$c'],
      },
    ],
    exhaustive: false,
  };

  const ref = useRef<FormControlWithOverlayRef>(null);
  useEffect(() => {
    ref.current?.validate();
  }, []);

  return (
    <FormField>
      <FilterField
        ref={ref}
        aria-label="Enter filter"
        defaultValue="specificVariables = $a any = $b patternForVariables = $asdf%as patternForVariables = $a_1"
        autoSuggestions
        validatorMap={validatorMap}
      />
    </FormField>
  );
};
```

```tsx
import { useCallback, useEffect, useRef } from 'react';

import {
  FilterField,
  type FilterFieldStatementNode,
  type FilterFieldValidatorMap,
} from '@dynatrace/strato-components/filters';
import {
  FormField,
  type FormControlWithOverlayRef,
} from '@dynatrace/strato-components/forms';

const Variables = () => {
  const isValidVariablePattern = useCallback(
    (state: {
      currentStatement: FilterFieldStatementNode;
      filterFieldValue: string;
    }) => {
      if (state.currentStatement.value?.type === 'Variable') {
        const variableRegex = /^\$\w+$/;

        return variableRegex.test(state.currentStatement.value.value)
          ? true
          : 'Only alpha-numerical values and underscores are allowed in variables.';
      }

      return true;
    },
    []
  );

  const validatorMap: FilterFieldValidatorMap = {
    keyPredicates: [
      {
        key: 'patternForVariables',
        valuePredicate: isValidVariablePattern,
      },
      {
        key: 'specificVariables',
        valuePredicate: ['$a', '$b', '$c'],
      },
    ],
    exhaustive: false,
  };

  const ref = useRef<FormControlWithOverlayRef>(null);
  useEffect(() => {
    ref.current?.validate();
  }, []);

  return (
    <FormField>
      <FilterField
        ref={ref}
        aria-label="Enter filter"
        defaultValue="specificVariables = $a any = $b patternForVariables = $asdf%as patternForVariables = $a_1"
        autoSuggestions
        validatorMap={validatorMap}
      />
    </FormField>
  );
};
```


### Enable matches phrase (~)

To enable matches phrase comparison operators (`~` and `!~`), provide a
`validatorMap` with `matches-phrase` or `not-matches-phrase` in the list of
allowed operators. You can enable comparison operators globally, for all keys at
once, or for individual keys. Matches phrase comparison operators are compatible
with keys of the type `Any` and `String`, or any type that you list as an
allowed comparison operator for a key.

For details on mapping `matches-phrase` and `not-matches-phrase` to a DQL
command, and when to use different comparison operators, see the documentation
on translation to DQL.

```tsx
import {
  FilterField,
  type FilterFieldValidatorMap,
} from '@dynatrace/strato-components/filters';
import {
  FormField,
  FormFieldMessages,
} from '@dynatrace/strato-components/forms';

const defaultValue = 'Cluster ~ cluster Namespace !~ local ';

const clusterValues = [
  'k8s-cluster-loadtest',
  'k8s-cluster-loadtest-sm',
  'k8s-cluster-e2e',
  'aws-topology',
  'local-dev',
];
const namespaceValues = [
  'kube-public',
  'kube-scheduler',
  'local-dev-namespace-1',
  'local-dev-namespace-2',
  'local-dev-namespace-3',
];
const validatorMap: FilterFieldValidatorMap = {
  keyPredicates: [
    {
      key: 'Cluster',
      valuePredicate: clusterValues,
      valueType: 'String',
    },
    {
      key: 'Namespace',
      valuePredicate: namespaceValues,
      valueType: 'String',
      comparisonOperators: ['matches-phrase', 'not-matches-phrase'],
    },
  ],
  comparisonOperators: ['matches-phrase'],
};

const EnableMatchesPhrase = () => {
  return (
    <FormField>
      <FilterField
        aria-label="Filter data"
        defaultValue={defaultValue}
        validatorMap={validatorMap}
        autoSuggestions
      />
      <FormFieldMessages />
    </FormField>
  );
};
```

```tsx
import {
  FilterField,
  type FilterFieldValidatorMap,
} from '@dynatrace/strato-components/filters';
import {
  FormField,
  FormFieldMessages,
} from '@dynatrace/strato-components/forms';

const defaultValue = 'Cluster ~ cluster Namespace !~ local ';

const clusterValues = [
  'k8s-cluster-loadtest',
  'k8s-cluster-loadtest-sm',
  'k8s-cluster-e2e',
  'aws-topology',
  'local-dev',
];
const namespaceValues = [
  'kube-public',
  'kube-scheduler',
  'local-dev-namespace-1',
  'local-dev-namespace-2',
  'local-dev-namespace-3',
];
const validatorMap: FilterFieldValidatorMap = {
  keyPredicates: [
    {
      key: 'Cluster',
      valuePredicate: clusterValues,
      valueType: 'String',
    },
    {
      key: 'Namespace',
      valuePredicate: namespaceValues,
      valueType: 'String',
      comparisonOperators: ['matches-phrase', 'not-matches-phrase'],
    },
  ],
  comparisonOperators: ['matches-phrase'],
};

const EnableMatchesPhrase = () => {
  return (
    <FormField>
      <FilterField
        aria-label="Filter data"
        defaultValue={defaultValue}
        validatorMap={validatorMap}
        autoSuggestions
      />
      <FormFieldMessages />
    </FormField>
  );
};
```


### Enable search (* ~)

To enable the search operator (`* ~`), set `searchConversion: true` in the
`parserConfig` prop. While the matches phrase comparison operator is used to
search in a specific field, the search operator is used to look for matches in
the whole record.

For details on mapping `search` to a DQL command, and when to use different
comparison operators, see the documentation on
translation to DQL.

```tsx
import { FilterField } from '@dynatrace/strato-components/filters';

const Search = () => {
  return (
    <FilterField
      aria-label="Filter data with search"
      parserConfig={{ searchConversion: true }}
      autoSuggestions
    />
  );
};
```

```tsx
import { FilterField } from '@dynatrace/strato-components/filters';

const Search = () => {
  return (
    <FilterField
      aria-label="Filter data with search"
      parserConfig={{ searchConversion: true }}
      autoSuggestions
    />
  );
};
```


### Enable JSONPath filtering

JSONPath filtering lets users target nested JSON data using JSONPath
expressions. To enable JSONPath filtering, set `jsonPathConversion: true` in the
`parserConfig` prop and add `{ type: 'JSONPath' }` to the `valuePredicate` array
in your validator map. You can combine JSONPath with other types, such as
`{type: Number}` or specific values, for flexible filtering. When combined, the
filter key appears twice in the suggestions: once with `$.` notation for
JSONPath, and once without for the expected type.

```tsx
import {
  FilterField,
  type FilterFieldValidatorMap,
} from '@dynatrace/strato-components/filters';

const jsonPathValidatorMap: FilterFieldValidatorMap = {
  keyPredicates: [
    {
      key: 'JSONPath',
      valueType: 'JSONPath',
    },
    {
      key: 'JSONPathAndAdditionalTypes',
      valueType: ['JSONPath', 'Number'],
    },
    {
      key: 'JSONPathAndAdditionalValue',
      valuePredicate: ['active', 'inactive'],
      valueType: 'JSONPath',
    },
  ],
  exhaustive: true,
};

const JSONPath = () => {
  return (
    <FilterField
      aria-label="Filter data with JSONPath"
      validatorMap={jsonPathValidatorMap}
      parserConfig={{ jsonPathConversion: true }}
      autoSuggestions
    />
  );
};
```

```tsx
import {
  FilterField,
  type FilterFieldValidatorMap,
} from '@dynatrace/strato-components/filters';

const jsonPathValidatorMap: FilterFieldValidatorMap = {
  keyPredicates: [
    {
      key: 'JSONPath',
      valueType: 'JSONPath',
    },
    {
      key: 'JSONPathAndAdditionalTypes',
      valueType: ['JSONPath', 'Number'],
    },
    {
      key: 'JSONPathAndAdditionalValue',
      valuePredicate: ['active', 'inactive'],
      valueType: 'JSONPath',
    },
  ],
  exhaustive: true,
};

const JSONPath = () => {
  return (
    <FilterField
      aria-label="Filter data with JSONPath"
      validatorMap={jsonPathValidatorMap}
      parserConfig={{ jsonPathConversion: true }}
      autoSuggestions
    />
  );
};
```


### Change insertion strategy

`FilterField` uses
filter field syntax
to parse the user's input and transform it into tokens. Each token represents a
filter key, value, comparison operator, or logical operator.

By default, applying a suggestion replaces the token that the cursor is
currently positioned on with the value of the suggestion. Use the
`insertionStrategy` prop to alter the behavior.

The following replacement strategies are supported:

 |
 | Strategy | Behavior
 | `replace-token` (default) | Replace the token at the cursor position.
 | `replace-statement` | Replace the whole statement at the cursor position.
 | `replace-all` | Replace the whole filter.
 | `insert` | Insert at the cursor position without any replacements.

```tsx
const [value, setValue] = useState('Health = healthy');
const [submittedValue, setSubmittedValue] = useState(value);
```

```tsx
const [value, setValue] = useState('Health = healthy');
const [submittedValue, setSubmittedValue] = useState(value);
```


### React to pasted content

To react to pasted content, implement an `onSuggest` callback and check whether
`pastedContent` is included in the provided suggestion types. When it is, you
can offer suggestions based on the pasted content, optionally using insertion
strategies like `replace-statement` or `replace-all` to turn the raw pasted
content into a full statement.

```tsx
import { useState, useCallback } from 'react';

import {
  FilterField,
  type FilterFieldSuggestionGroup,
  type FilterFieldSuggestionsCallback,
  type FilterFieldValidatorMap,
} from '@dynatrace/strato-components/filters';
import {
  FormField,
  FormFieldMessages,
  Label,
} from '@dynatrace/strato-components/forms';
import { Container, Flex } from '@dynatrace/strato-components/layouts';
import { Text } from '@dynatrace/strato-components/typography';

const validatorMap: FilterFieldValidatorMap = {
  keyPredicates: [
    {
      key: 'podName',
      valueType: 'String',
      comparisonOperators: ['not-matches-phrase', 'matches-phrase'],
    },
    {
      key: 'healthy',
      valueType: 'Boolean',
    },
  ],
};

const PastedContent = () => {
  const [suggestions, setSuggestions] = useState<
    Record<string, FilterFieldSuggestionGroup | undefined>
  >({});

  const getSuggestions: FilterFieldSuggestionsCallback = useCallback(
    (state) => {
      if (state === undefined) {
        setSuggestions({});
        return;
      }

      const { currentTokens } = state;

      const suggestions: Record<
        string,
        FilterFieldSuggestionGroup | undefined
      > = {};

      for (const currentToken of currentTokens) {
        const { type, token } = currentToken;

        if (type === 'pastedContent') {
          const matchesPhrase = `podName ~ ${token.textValue}`;
          const notMatchesPhrase = `podName !~ ${token.textValue}`;

          suggestions.value = {
            id: 'pasted-content-suggestions',
            label: 'Pasted content suggestion group',
            suggestions: [
              {
                value: matchesPhrase,
                details: 'Matches phrase',
                displayValue: matchesPhrase,
                insertionStrategy: 'replace-statement',
              },
              {
                value: notMatchesPhrase,
                details: 'Not matches phrase',
                displayValue: notMatchesPhrase,
                insertionStrategy: 'replace-statement',
              },
            ],
          };
        }

        setSuggestions(suggestions);
      }
    },
    []
  );

  return (
    <Flex flexDirection="column">
      <FormField>
        <Label>Filter field</Label>
        <FilterField
          defaultValue="healthy = true"
          onSuggest={getSuggestions}
          validatorMap={validatorMap}
          autoSuggestions
        >
          <FilterField.Suggestions>
            {Array.from(Object.values(suggestions)).map(
              (suggestionGroup) =>
                suggestionGroup && (
                  <FilterField.SuggestionGroup
                    key={suggestionGroup.id}
                    {...suggestionGroup}
                  />
                )
            )}
          </FilterField.Suggestions>
        </FilterField>
        <FormFieldMessages />
      </FormField>

      <Container as={Flex} flexDirection="column" gap={4} paddingY={12}>
        <Text textStyle="base-emphasized">Text to try out pasting</Text>
        <Flex flexDirection="column" gap={0}>
          <Text style={{ userSelect: 'all' }}>pod_(frontend_1)</Text>
          <Text style={{ userSelect: 'all' }}>pod&lt;&gt; service:8080</Text>
          <Text style={{ userSelect: 'all' }}>pod = $backend[1]"v1"</Text>
          <Text style={{ userSelect: 'all' }}>"pod-backend-2"</Text>
        </Flex>
      </Container>
    </Flex>
  );
};
```

```tsx
import { useState, useCallback } from 'react';

import {
  FilterField,
  type FilterFieldSuggestionGroup,
  type FilterFieldSuggestionsCallback,
  type FilterFieldValidatorMap,
} from '@dynatrace/strato-components/filters';
import {
  FormField,
  FormFieldMessages,
  Label,
} from '@dynatrace/strato-components/forms';
import { Container, Flex } from '@dynatrace/strato-components/layouts';
import { Text } from '@dynatrace/strato-components/typography';

const validatorMap: FilterFieldValidatorMap = {
  keyPredicates: [
    {
      key: 'podName',
      valueType: 'String',
      comparisonOperators: ['not-matches-phrase', 'matches-phrase'],
    },
    {
      key: 'healthy',
      valueType: 'Boolean',
    },
  ],
};

const PastedContent = () => {
  const [suggestions, setSuggestions] = useState<
    Record<string, FilterFieldSuggestionGroup | undefined>
  >({});

  const getSuggestions: FilterFieldSuggestionsCallback = useCallback(
    (state) => {
      if (state === undefined) {
        setSuggestions({});
        return;
      }

      const { currentTokens } = state;

      const suggestions: Record<
        string,
        FilterFieldSuggestionGroup | undefined
      > = {};

      for (const currentToken of currentTokens) {
        const { type, token } = currentToken;

        if (type === 'pastedContent') {
          const matchesPhrase = `podName ~ ${token.textValue}`;
          const notMatchesPhrase = `podName !~ ${token.textValue}`;

          suggestions.value = {
            id: 'pasted-content-suggestions',
            label: 'Pasted content suggestion group',
            suggestions: [
              {
                value: matchesPhrase,
                details: 'Matches phrase',
                displayValue: matchesPhrase,
                insertionStrategy: 'replace-statement',
              },
              {
                value: notMatchesPhrase,
                details: 'Not matches phrase',
                displayValue: notMatchesPhrase,
                insertionStrategy: 'replace-statement',
              },
            ],
          };
        }

        setSuggestions(suggestions);
      }
    },
    []
  );

  return (
    <Flex flexDirection="column">
      <FormField>
        <Label>Filter field</Label>
        <FilterField
          defaultValue="healthy = true"
          onSuggest={getSuggestions}
          validatorMap={validatorMap}
          autoSuggestions
        >
          <FilterField.Suggestions>
            {Array.from(Object.values(suggestions)).map(
              (suggestionGroup) =>
                suggestionGroup && (
                  <FilterField.SuggestionGroup
                    key={suggestionGroup.id}
                    {...suggestionGroup}
                  />
                )
            )}
          </FilterField.Suggestions>
        </FilterField>
        <FormFieldMessages />
      </FormField>

      <Container as={Flex} flexDirection="column" gap={4} paddingY={12}>
        <Text textStyle="base-emphasized">Text to try out pasting</Text>
        <Flex flexDirection="column" gap={0}>
          <Text style={{ userSelect: 'all' }}>pod_(frontend_1)</Text>
          <Text style={{ userSelect: 'all' }}>pod&lt;&gt; service:8080</Text>
          <Text style={{ userSelect: 'all' }}>pod = $backend[1]"v1"</Text>
          <Text style={{ userSelect: 'all' }}>"pod-backend-2"</Text>
        </Flex>
      </Container>
    </Flex>
  );
};
```


### Map FilterField syntax to DQL

To ensure predictable and consistent behavior for end users, map FilterField
syntax to
Dynatrace Query Language (DQL)
using these equivalents:

 |
 | FilterField syntax | DQL equivalent
 | `=` | `matchesValue(key, "value")`
 | `!=` | `not matchesValue(key, "value")`
 | | `>`
 | `>=` | `>=`
 | `= *` | `isNotNull()`
 | `!= *` | `isNull()`
 | `AND` | `and`
 | `OR` | `or`
 | `in` | `matchesValue(key, array("value1", "value2"))`
 | `not in` | `not matchesValue(key, array("value1", "value2"))`
 | `*value` | `matchesValue(key, "*value")`
 | `value*` | `matchesValue(key, "value*")`
 | `*value*` | `matchesValue(key, "*value*")`
 | `~` | `matchesPhrase(key, "*value*")`
 | `!~` | `not matchesPhrase(key, "*value*")`
 | `* ~` | `search "value"`

### Related

#### Patterns

- Filtering

#### Documentation

- Filter field

- Filtering and sorting
Still have questions?Find answers in the Dynatrace Community
- Import
- Demo
- Validate user input
- Define valid keys
- Define key types
- Define values for keys
- Additional and custom types
- Suggestion Ordering
- Suggest full statements when typing values
- Define fallback keys for free-text search
- Add display labels and descriptions to suggestions
- Group key suggestions
- Group value suggestions
- Specify validation logic
- Define comparison operators
- Work with syntax tree
- Explicit logical operator nodes
- Convert string to syntax tree
- Convert syntax tree to string
- Customize comparison operator suggestions
- Escape characters in suggestions
- Programmatically escape suggestion values
- Group suggestions
- Load suggestions async
- Limit suggestions shown
- Persist recent and pinned filters
- Use the FilterField in a form
- Variables
- Enable matches phrase (~)
- Enable search (* ~)
- Enable JSONPath filtering
- Change insertion strategy
- React to pasted content
- Map FilterField syntax to DQL
- Related
- Patterns
- Documentation

### Props

`FilterField` is an advanced, text-based filtering component. It supports
complex data filtering with intuitive filter field syntax and auto-suggestions.

#### FilterFieldProps

##### Signature:
`export declare type FilterFieldProps = > & {
 /**
 * Placeholder text displayed when the filter field is empty.
 * @defaultValue
 */
 placeholder?: ;
 /**
 * Whether the automatically determined suggestions (logical / comparison operators) should be shown.
 * If set to true, the suggestions will automatically be added to the suggestions overlay.
 * @defaultValue false
 */
 autoSuggestions?: ;
 /**
 * The of default suggestions rendered before showing a button.
 * Set to -1 to always render all the available suggestions.
 * You can specify different counts for when the input is empty and when the user has typed something.
 * @defaultValue \{ empty: 5, filled: 10 \}
 */
 defaultSuggestionsCount?: {
 empty?: ;
 filled?: ;
 } | ;
 /**
 * Callback triggered when the suggestions may need to be updated.
 * @defaultValue
 */
 onSuggest?: ;
 /**
 * Callback triggered when the user submits the currently entered filter for filtering.
 * @defaultValue
 */
 onFilter?: (filterState: {
 /** The current value of the filter field. */
 value: ;
 /** Syntax tree of the current value. */
 syntaxTree: ;
 /** Whether the current value is valid. */
 isValid: ;
 }) => ;
 /**
 * Custom types to restrict allowed values in the validator map.
 * Keys are type names that can be used in the validatorMap, values are validation functions.
 * @example
 * `tsx
 *
 * `
 */
 customTypes?: ;
 /** Validators to restrict allowed keys and their operators. */
 validatorMap?: ;
 /** Config to enable new nodes in the . */
 parserConfig?: {
 /**
 * Whether search operators are enabled in the filter field. If set to false,
 * they will be marked as error and returned accordingly in the syntax tree.
 * @defaultValue false
 * @deprecated With the next breaking change cycle, the SearchOperator node will be returned by default
 */
 searchConversion?: ;
 /**
 * Whether a key will be converted to a JSONPath node if a JSONPath is entered in the FilterField.
 * If set to false, they will be marked as error and returned accordingly in the syntax tree.
 * @defaultValue false
 * @deprecated With the next breaking change cycle, the jsonPathConversion will be enabled by default
 */
 jsonPathConversion?: ;
 /**
 * Whether a value will be converted to an IPAddress node if an IPAddress is entered in the FilterField.
 * If set to false, they will be returned as a node in the syntax tree.
 * @defaultValue false
 * @deprecated With the next breaking change cycle, the ipAddressConversion will be enabled by default
 */
 ipAddressConversion?: ;
 /**
 * Whether a value will be converted to a UID node if a UID is entered in the FilterField.
 * If set to false, they will be returned as a node in the syntax tree.
 * @defaultValue false
 * @deprecated With the next breaking change cycle, the uidConversion will be enabled by default
 */
 uidConversion?: ;
 /**
 * Whether a value will be converted to a Timestamp node if a Timestamp is entered in the FilterField.
 * If set to false, they will be returned as a node in the syntax tree.
 * @defaultValue false
 * @deprecated With the next breaking change cycle, the timestampConversion will be enabled by default
 */
 timestampConversion?: ;
 /**
 * Whether a value will be converted to a SmartscapeId node if a SmartscapeId is entered in the FilterField.
 * If set to false, they will be returned as a node in the syntax tree.
 * @defaultValue false
 * @deprecated With the next breaking change cycle, the smartscapeIdConversion will be enabled by default
 */
 smartscapeIdConversion?: ;
 };
 /**
 * Namespace identifying the used key for the recent and saved filters storage.
 * Defaults currently to and will default to with the next breaking change.
 * Set the value to if you want to opt out of the recent and saved filters api.
 * @defaultValue
 *
 */
 filterNamespace?: | ;
}>;`

### FilterField.Suggestions

The `FilterField.Suggestions` component to render a list of suggestions is
optional, but can be used to set options specific to the suggestions.

#### FilterFieldSuggestionsProps

##### Signature:
`export declare type FilterFieldSuggestionsProps = & & & & {
 /** Whether the suggestions are loading. If true, a loading indicator is shown and otherwise the suggestions are shown. */
 loading?: ;
};`

### FilterField.Suggestion

Use the `FilterField.Suggestion` component for each suggestion list entry.

#### FilterFieldSuggestionProps

##### Signature:
`export declare type Props = ;`

### FilterField.SuggestionDetails

Use the `FilterField.SuggestionDetails` component inside a
`FilterField.Suggestion` to provide additional information.

#### FilterFieldSuggestionDetailsProps

##### Signature:
`export declare type FilterFieldSuggestionDetailsProps = & & & ;`

### FilterField.SuggestionGroup

Use the `FilterField.SuggestionGroup` to add separators between groups of
related suggestions.

#### FilterFieldSuggestionGroupProps

##### Signature:
`export declare type Props = ;`

### FilterField.SuggestionGroupLabel

To label a set of grouped suggestions, use the
`FilterField.SuggestionGroupLabel` component.

#### FilterFieldSuggestionGroupLabelProps

##### Signature:
`export declare type FilterFieldSuggestionGroupLabelProps = & & & & ;`Still have questions?Find answers in the Dynatrace Community
- FilterField.Suggestions
- FilterField.Suggestion
- FilterField.SuggestionDetails
- FilterField.SuggestionGroup
- FilterField.SuggestionGroupLabel

---

## SegmentSelector

`/design/components/filters/SegmentSelector/`

`SegmentSelector` is a top-level filter component that filters data by segments,
setting the scope for additional filters.

### Import

`tsx
import { SegmentSelector } from '@dynatrace/strato-components/filters';
`

### Demo

`SegmentSelector` lets users filter data from specific datasets called
Segments. The
`useSegments` hook provides access to the selected values. See
Usage for best practices.

```tsx
import {
  SegmentSelector,
  useSegments,
} from '@dynatrace/strato-components/filters';

const Basic = () => {
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const { segments } = useSegments();

  return (
    <div style={{ height: '300px' }}>
      <SegmentSelector />
    </div>
  );
};
```

```tsx
import {
  SegmentSelector,
  useSegments,
} from '@dynatrace/strato-components/filters';

const Basic = () => {
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const { segments } = useSegments();

  return (
    <div style={{ height: '300px' }}>
      <SegmentSelector />
    </div>
  );
};
```


### Set the scope

Use the `SegmentsProvider` to restrict the scope of one or more
`SegmentSelector` components. This will apply only those segments within a given
scope and ignore any globally-set segments.

The `SegmentsProvider` accepts default segments as well and filters out any
faulty segments. If the default selection should apply to all `SegmentsSelector`
components, place the `SegmentsProvider` at a high level. For example, right
after the `AppRoot`.

```tsx
import {
  SegmentSelector,
  SegmentsProvider,
} from '@dynatrace/strato-components/filters';
import { Flex, Surface } from '@dynatrace/strato-components/layouts';

const ScopedSegmentSelector = () => {
  return (
    <Flex flexDirection="column" gap={24} height="300px">
      <SegmentSelector />
      <Surface elevation="raised">
        <SegmentsProvider defaultSegments={[{ id: '1ttwUGTwDsC' }]}>
          <SegmentSelector />
        </SegmentsProvider>
      </Surface>
    </Flex>
  );
};
```

```tsx
import {
  SegmentSelector,
  SegmentsProvider,
} from '@dynatrace/strato-components/filters';
import { Flex, Surface } from '@dynatrace/strato-components/layouts';

const ScopedSegmentSelector = () => {
  return (
    <Flex flexDirection="column" gap={24} height="300px">
      <SegmentSelector />
      <Surface elevation="raised">
        <SegmentsProvider defaultSegments={[{ id: '1ttwUGTwDsC' }]}>
          <SegmentSelector />
        </SegmentsProvider>
      </Surface>
    </Flex>
  );
};
```


### Configure segments programmatically

The `useSegments` hook provides the following helper functions to
programmatically configure selected segments:

 |
 | Function | Description
 | `addSegment` | Adds one segment to the selection. If the segment is unavailable, it won't be added to the selection.
 | `removeSegment` | Removes one segment from the selection.
 | `removeAllSegments` | Removes all segments from the selection.
 | `setSegments` | Overrides all currently applied segments. Similarly to `addSegment`, `setSegments` checks the availability of each segment.

```tsx
import { Button } from '@dynatrace/strato-components/buttons';
import {
  SegmentSelector,
  useSegments,
} from '@dynatrace/strato-components/filters';
import { Flex } from '@dynatrace/strato-components/layouts';

const CRUDFunctions = () => {
  const { setSegments, addSegment, removeAllSegments, removeSegment } =
    useSegments();

  return (
    <Flex flexDirection="column" height="300px">
      <Flex>
        <Button
          onClick={() => {
            addSegment({ id: '1ttwUGTwDsC' })
              .then((response) => {
                /** in case something depends on the change, handle it here */
              })
              .catch((error) => {
                /** handle error in case the operation fails */
              });
          }}
          variant="accent"
        >
          add 'Simple Segment'
        </Button>
        <Button
          onClick={() => {
            removeSegment('1ttwUGTwDsC');
          }}
          variant="accent"
        >
          remove 'Simple Segment'
        </Button>

        <Button onClick={removeAllSegments} variant="accent">
          remove all
        </Button>
        <Button
          onClick={() => {
            setSegments([
              { id: '1ttwUGTwDsC' },
              {
                id: 'HmtRPIOrwm',
                variables: [{ name: 'type', values: ['INFO'] }],
              },
            ])
              .then((response) => {
                /** in case something depends on the change, handle it here */
              })
              .catch((error) => {
                /** handle error in case the operation fails */
              });
          }}
          variant="accent"
        >
          set to 'Simple Segment' and 'Log Level'
        </Button>
      </Flex>
      <SegmentSelector />
    </Flex>
  );
};
```

```tsx
import { Button } from '@dynatrace/strato-components/buttons';
import {
  SegmentSelector,
  useSegments,
} from '@dynatrace/strato-components/filters';
import { Flex } from '@dynatrace/strato-components/layouts';

const CRUDFunctions = () => {
  const { setSegments, addSegment, removeAllSegments, removeSegment } =
    useSegments();

  return (
    <Flex flexDirection="column" height="300px">
      <Flex>
        <Button
          onClick={() => {
            addSegment({ id: '1ttwUGTwDsC' })
              .then((response) => {
                /** in case something depends on the change, handle it here */
              })
              .catch((error) => {
                /** handle error in case the operation fails */
              });
          }}
          variant="accent"
        >
          add 'Simple Segment'
        </Button>
        <Button
          onClick={() => {
            removeSegment('1ttwUGTwDsC');
          }}
          variant="accent"
        >
          remove 'Simple Segment'
        </Button>

        <Button onClick={removeAllSegments} variant="accent">
          remove all
        </Button>
        <Button
          onClick={() => {
            setSegments([
              { id: '1ttwUGTwDsC' },
              {
                id: 'HmtRPIOrwm',
                variables: [{ name: 'type', values: ['INFO'] }],
              },
            ])
              .then((response) => {
                /** in case something depends on the change, handle it here */
              })
              .catch((error) => {
                /** handle error in case the operation fails */
              });
          }}
          variant="accent"
        >
          set to 'Simple Segment' and 'Log Level'
        </Button>
      </Flex>
      <SegmentSelector />
    </Flex>
  );
};
```


### Show private and outdated segments

Users can share private segments with other users, for example, through a link.
If the recipient removes a private segment from their view, it will not be
visible to them any longer. However, they can access the private segment once
more by re-opening the link.

Outdated segments remain visible in the segments array but are marked as
`unavailable`.

```tsx
import {
  SegmentSelector,
  SegmentsProvider,
} from '@dynatrace/strato-components/filters';

const UnlistedUnavailableSegments = () => {
  return (
    <div style={{ height: '300px' }}>
      <SegmentsProvider
        defaultSegments={[
          { id: 'uUPbhpKv93E' },
          {
            id: 'QbtRPIOrwm',
            variables: [
              {
                name: 'name',
                values: ['Host 1', 'Host 3'],
              },
            ],
          },
          {
            id: 'TnGWfXgHZwR',
            variables: [
              {
                name: 'name',
                values: ['outdated variable'],
              },
            ],
          },
        ]}
      >
        <SegmentSelector />
      </SegmentsProvider>
    </div>
  );
};
```

```tsx
import {
  SegmentSelector,
  SegmentsProvider,
} from '@dynatrace/strato-components/filters';

const UnlistedUnavailableSegments = () => {
  return (
    <div style={{ height: '300px' }}>
      <SegmentsProvider
        defaultSegments={[
          { id: 'uUPbhpKv93E' },
          {
            id: 'QbtRPIOrwm',
            variables: [
              {
                name: 'name',
                values: ['Host 1', 'Host 3'],
              },
            ],
          },
          {
            id: 'TnGWfXgHZwR',
            variables: [
              {
                name: 'name',
                values: ['outdated variable'],
              },
            ],
          },
        ]}
      >
        <SegmentSelector />
      </SegmentsProvider>
    </div>
  );
};
```


### Customize trigger

`SegmentSelector` comes with a default trigger to ensure a consistent user
experience. In exceptional cases, if necessary, it's possible to override the
default trigger.

Props are automatically applied with the custom trigger we provide to ensure
correct semantics. The `SegmentSelector.CustomTrigger` accepts a render function
with two objects as arguments:

- The first object provides access to the default `displayValue` and the
`isLoading` state.

- The second object provides all the trigger props necessary for the trigger
button to function.

If you override the default trigger, make sure to spread the props to the
trigger element to tie interactions back to the `SegmentSelector`. This enables
you to customize the trigger component, while leveraging the internal logic of
the `SegmentSelector` component.

```tsx
import { Button } from '@dynatrace/strato-components/buttons';
import { SegmentSelector } from '@dynatrace/strato-components/filters';
import { ChevronDownSmallIcon, ContainerIcon } from '@dynatrace/strato-icons';

const CustomTrigger = () => {
  return (
    <div style={{ height: '300px' }}>
      <SegmentSelector>
        <SegmentSelector.CustomTrigger>
          {({ displayValue, isLoading }, props) => (
            <Button {...props} loading={isLoading}>
              <Button.Prefix>
                <ContainerIcon />
              </Button.Prefix>
              {displayValue}
              <Button.Suffix>
                <ChevronDownSmallIcon />
              </Button.Suffix>
            </Button>
          )}
        </SegmentSelector.CustomTrigger>
      </SegmentSelector>
    </div>
  );
};
```

```tsx
import { Button } from '@dynatrace/strato-components/buttons';
import { SegmentSelector } from '@dynatrace/strato-components/filters';
import { ChevronDownSmallIcon, ContainerIcon } from '@dynatrace/strato-icons';

const CustomTrigger = () => {
  return (
    <div style={{ height: '300px' }}>
      <SegmentSelector>
        <SegmentSelector.CustomTrigger>
          {({ displayValue, isLoading }, props) => (
            <Button {...props} loading={isLoading}>
              <Button.Prefix>
                <ContainerIcon />
              </Button.Prefix>
              {displayValue}
              <Button.Suffix>
                <ChevronDownSmallIcon />
              </Button.Suffix>
            </Button>
          )}
        </SegmentSelector.CustomTrigger>
      </SegmentSelector>
    </div>
  );
};
```


### Related

#### Patterns

- Filtering

#### Documentation

- Segments
Still have questions?Find answers in the Dynatrace Community
- Import
- Demo
- Set the scope
- Configure segments programmatically
- Show private and outdated segments
- Customize trigger
- Related
- Patterns
- Documentation

### Props

`SegmentSelector` is a top-level filter component that filters data by segments,
setting the scope for additional filters.

#### SegmentSelectorProps

##### Signature:
`export declare type SegmentSelectorProps = & & & & & & & {
 /**
 * Configures the style of the trigger.
 * @defaultValue 'default
 */
 variant?: | ;
 /** Callback that is triggered when the open state of the SegmentSelector's overlay changes its open state. */
 onOpenChange?: (isOpen: ) => ;
};`

#### useSegments

#### useSegments

##### Signature:
`export declare const useSegments: () => {
 segments: FilterSegment[];
 addSegment: (segment: FilterSegment) => Promise;
 removeSegment: (id?: | ) => ;
 removeAllSegments: () => ;
 setSegments: (segments: FilterSegment[], force?: ) => Promise<>;
};`

#### SegmentSelector.CustomTrigger

#### SegmentSelectorCustomTriggerProps

##### Signature:
`export declare type SegmentSelectorCustomTriggerProps = & & & {
 /** Elements to be displayed in the CustomTrigger. */
 children: | ((customTriggerProps: {
 displayValue: ;
 isLoading: ;
 }, props: ( & & (>> & )) | ) => );
};`Still have questions?Find answers in the Dynatrace Community
- useSegments
- SegmentSelector.CustomTrigger

---

## TimeframeSelector

`/design/components/filters/TimeframeSelector/`

`TimeframeSelector` is a filtering component that lets users choose from preset
timeframes or add unique "from" and "to" time values of their own.

### Import

`tsx
import { TimeframeSelector } from '@dynatrace/strato-components/filters';
`

### Demo

`TimeframeSelector` takes its information from the user's Dynatrace user
settings. The timezone setting determines the timezone offset in
`TimeframeSelector`, while the region setting determines its display format.
Both the timezone and the region can be set independently. If either is set to
"use browser default," `TimeframeSelector` will fall back to the user's browser
settings for that value. The value passed to the `onChange` is converted back to
an ISO string or passed as an expression. See Usage for best
practices.

```tsx
import { TimeframeSelector } from '@dynatrace/strato-components/filters';

const Basic = () => {
  return <TimeframeSelector defaultValue={{ from: 'now-2h', to: 'now' }} />;
};
```

```tsx
import { TimeframeSelector } from '@dynatrace/strato-components/filters';

const Basic = () => {
  return <TimeframeSelector defaultValue={{ from: 'now-2h', to: 'now' }} />;
};
```


### Control state

`TimeframeSelector` can be controlled, meaning that you can handle the selection
state. To do so, use the `onChange` prop to provide a handler to be called when
the internal state changes. You must assign the value from the state to the
`TimeframeSelector` by setting the `value` prop.

```tsx
import { useState } from 'react';

import type { Timeframe } from '@dynatrace/strato-components/core';
import { TimeframeSelector } from '@dynatrace/strato-components/filters';

const Controlled = () => {
  const [value, setValue] = useState<Timeframe | null>(null);

  return <TimeframeSelector value={value} onChange={setValue} />;
};
```

```tsx
import { useState } from 'react';

import type { Timeframe } from '@dynatrace/strato-components/core';
import { TimeframeSelector } from '@dynatrace/strato-components/filters';

const Controlled = () => {
  const [value, setValue] = useState<Timeframe | null>(null);

  return <TimeframeSelector value={value} onChange={setValue} />;
};
```


### Set initial values

When you create the state for controlling `TimeframeSelector`, you can pass a
`Timeframe` to pre-fill the `from` and `to` inputs. To make a pre-filled value
the default or preset selection, initialize the state with an expression
matching the preset.

```tsx
import { useState } from 'react';

import {
  TimeframeSelector,
  type TimeframeSelectorProps,
} from '@dynatrace/strato-components/filters';

const InitialValue = () => {
  const [value, setValue] = useState<TimeframeSelectorProps['value']>({
    from: 'now-2h',
    to: 'now',
  });

  return <TimeframeSelector value={value} onChange={setValue} />;
};
```

```tsx
import { useState } from 'react';

import {
  TimeframeSelector,
  type TimeframeSelectorProps,
} from '@dynatrace/strato-components/filters';

const InitialValue = () => {
  const [value, setValue] = useState<TimeframeSelectorProps['value']>({
    from: 'now-2h',
    to: 'now',
  });

  return <TimeframeSelector value={value} onChange={setValue} />;
};
```


### Customize presets

Use `TimeframeSelector.Presets` to customize presets and show any timeframe
inside the overlay. Default presets are exported, so you can either add to the
list of default items or override them entirely.

The preset list can display up to ten items. If an invalid preset item is added,
it won't be rendered and a console.warn will be called, with details to help you
resolve the issue.

```tsx
import { useState } from 'react';

import type { Timeframe } from '@dynatrace/strato-components/core';
import {
  TimeframeSelector,
  TIMEFRAME_SELECTOR_PRESETS,
} from '@dynatrace/strato-components/filters';
import { Label, FormField } from '@dynatrace/strato-components/forms';

const CustomPresets = () => {
  const presetValues = [
    {
      from: '-10d',
      to: 'now()',
    },
    {
      from: '-15d',
      to: 'now()',
    },
    {
      from: '2024-01-01T16:18:18.229Z',
      to: '2024-01-15T16:18:18.229Z',
    },
    {
      from: '2024-02-15T12:18:18.229Z',
      to: '2024-02-15T16:18:18.229Z',
    },
    {
      from: 'now()+2d',
      to: 'now()', // invalid order, so this preset will be hidden and an error will be shown in dev mode
    },
  ];

  const [value, setValue] = useState<Timeframe | null>(null);

  return (
    <FormField>
      <Label>Select timeframe</Label>
      <TimeframeSelector value={value} onChange={setValue}>
        <TimeframeSelector.Presets>
          {[...TIMEFRAME_SELECTOR_PRESETS, ...presetValues].map((item) => (
            <TimeframeSelector.PresetItem
              key={item.from + item.to}
              value={item}
            />
          ))}
        </TimeframeSelector.Presets>
      </TimeframeSelector>
    </FormField>
  );
};
```

```tsx
import { useState } from 'react';

import type { Timeframe } from '@dynatrace/strato-components/core';
import {
  TimeframeSelector,
  TIMEFRAME_SELECTOR_PRESETS,
} from '@dynatrace/strato-components/filters';
import { Label, FormField } from '@dynatrace/strato-components/forms';

const CustomPresets = () => {
  const presetValues = [
    {
      from: '-10d',
      to: 'now()',
    },
    {
      from: '-15d',
      to: 'now()',
    },
    {
      from: '2024-01-01T16:18:18.229Z',
      to: '2024-01-15T16:18:18.229Z',
    },
    {
      from: '2024-02-15T12:18:18.229Z',
      to: '2024-02-15T16:18:18.229Z',
    },
    {
      from: 'now()+2d',
      to: 'now()', // invalid order, so this preset will be hidden and an error will be shown in dev mode
    },
  ];

  const [value, setValue] = useState<Timeframe | null>(null);

  return (
    <FormField>
      <Label>Select timeframe</Label>
      <TimeframeSelector value={value} onChange={setValue}>
        <TimeframeSelector.Presets>
          {[...TIMEFRAME_SELECTOR_PRESETS, ...presetValues].map((item) => (
            <TimeframeSelector.PresetItem
              key={item.from + item.to}
              value={item}
            />
          ))}
        </TimeframeSelector.Presets>
      </TimeframeSelector>
    </FormField>
  );
};
```


### Enable timeframe reset

This component provides a button to 'Reset timeframe', giving users the option
to clear a selected timeframe. To display this button, the `clearable` prop must
be set to true.

```tsx
import { useState } from 'react';

import type { Timeframe } from '@dynatrace/strato-components/core';
import { TimeframeSelector } from '@dynatrace/strato-components/filters';

const ClearSelection = () => {
  const [value, setValue] = useState<Timeframe | null>(null);

  /* eslint-disable-next-line @typescript-eslint/no-deprecated */
  return <TimeframeSelector value={value} onChange={setValue} clearable />;
};
```

```tsx
import { useState } from 'react';

import type { Timeframe } from '@dynatrace/strato-components/core';
import { TimeframeSelector } from '@dynatrace/strato-components/filters';

const ClearSelection = () => {
  const [value, setValue] = useState<Timeframe | null>(null);

  /* eslint-disable-next-line @typescript-eslint/no-deprecated */
  return <TimeframeSelector value={value} onChange={setValue} clearable />;
};
```


### Set display precision

Change the default display precision of minutes by setting the `precision` prop
to either seconds or milliseconds. This also sets the precision of the inputs
shown in the overlay or the returned ISOStrings from the `onChange`.

```tsx
import { TimeframeSelector } from '@dynatrace/strato-components/filters';

const Precision = () => {
  return (
    <TimeframeSelector
      defaultValue={{
        from: {
          absoluteDate: '2022-02-22T04:42:35.393Z',
          value: '2022-02-22T14:42:35.393Z',
          type: 'iso8601',
        },
        to: {
          absoluteDate: new Date().toISOString(),
          value: 'now()',
          type: 'expression',
        },
      }}
      precision="seconds"
    />
  );
};
```

```tsx
import { TimeframeSelector } from '@dynatrace/strato-components/filters';

const Precision = () => {
  return (
    <TimeframeSelector
      defaultValue={{
        from: {
          absoluteDate: '2022-02-22T04:42:35.393Z',
          value: '2022-02-22T14:42:35.393Z',
          type: 'iso8601',
        },
        to: {
          absoluteDate: new Date().toISOString(),
          value: 'now()',
          type: 'expression',
        },
      }}
      precision="seconds"
    />
  );
};
```


### Set min and max values

The default `min` and `max` values for `TimeframeSelector` follow the current
Grail limitations for timeframes. You can define a custom min and max range by
setting the `min` and `max` props to valid `isoString` dates or expressions. Use
`FormField` and `FormFieldMessages` to provide users with helpful error
messages.

```tsx
import { useEffect, useRef } from 'react';

import { TimeframeSelector } from '@dynatrace/strato-components/filters';
import {
  FormField,
  FormFieldMessages,
  type TimeRangePickerRef,
} from '@dynatrace/strato-components/forms';

const MinMax = () => {
  const timeframeSelectorRef = useRef<TimeRangePickerRef>(null);

  useEffect(() => {
    timeframeSelectorRef.current?.validate();
  }, []);

  return (
    <FormField>
      <TimeframeSelector
        aria-label="Timeframe selector"
        ref={timeframeSelectorRef}
        defaultValue={{
          from: 'now-8d',
          to: 'now',
        }}
        min="now-7d"
        max="now"
      />
      <FormFieldMessages />
    </FormField>
  );
};
```

```tsx
import { useEffect, useRef } from 'react';

import { TimeframeSelector } from '@dynatrace/strato-components/filters';
import {
  FormField,
  FormFieldMessages,
  type TimeRangePickerRef,
} from '@dynatrace/strato-components/forms';

const MinMax = () => {
  const timeframeSelectorRef = useRef<TimeRangePickerRef>(null);

  useEffect(() => {
    timeframeSelectorRef.current?.validate();
  }, []);

  return (
    <FormField>
      <TimeframeSelector
        aria-label="Timeframe selector"
        ref={timeframeSelectorRef}
        defaultValue={{
          from: 'now-8d',
          to: 'now',
        }}
        min="now-7d"
        max="now"
      />
      <FormFieldMessages />
    </FormField>
  );
};
```


### Validate user input

This example shows how to validate user input in `TimeframeSelector` using the
`react-hook-form` package, which handles error messages. To connect the form
with `TimeframeSelector`, register the field with the custom error message and
use the `useForm` hook from `react-hook-form`.

```tsx
import { Controller, useForm } from 'react-hook-form';

import { Button } from '@dynatrace/strato-components/buttons';
import type { Timeframe } from '@dynatrace/strato-components/core';
import { TimeframeSelector } from '@dynatrace/strato-components/filters';
import {
  FormField,
  FormFieldMessages,
} from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import { Heading, Text } from '@dynatrace/strato-components/typography';

const Validate = () => {
  const {
    handleSubmit,
    control,
    formState: { isSubmitSuccessful },
    reset,
  } = useForm<{
    timeframe: Timeframe | null;
  }>({
    mode: 'all',
  });

  return (
    <form
      onSubmit={handleSubmit(() => void 0)}
      onReset={() => reset()}
      noValidate
    >
      <Flex flexDirection="column" gap={16}>
        <Heading level={2}>Register</Heading>
        <Flex flexDirection="column" gap={16}>
          <Controller
            name="timeframe"
            control={control}
            rules={{
              validate: (value) =>
                (value?.from &&
                  value.from.type === 'expression' &&
                  value?.to &&
                  value.to.type === 'expression') ||
                'Please only enter expressions in the from and to value',
            }}
            render={({ field, fieldState: { error } }) => (
              <FormField required>
                <TimeframeSelector
                  aria-label="Timeframe selector"
                  /* eslint-disable-next-line @typescript-eslint/no-deprecated */
                  clearable
                  {...field}
                />
                <FormFieldMessages>
                  {(msgs) => {
                    if (msgs.length > 0) {
                      return msgs.map((msgs) => (
                        <FormFieldMessages.Item key={msgs.id} {...msgs} />
                      ));
                    }

                    if (error) {
                      return (
                        <FormFieldMessages.Item
                          variant="error"
                          key={error.type}
                        >
                          {error.message}
                        </FormFieldMessages.Item>
                      );
                    }
                  }}
                </FormFieldMessages>
              </FormField>
            )}
          />
          <Button type="submit" variant="emphasized">
            Submit
          </Button>
          <Text>
            The form has{!isSubmitSuccessful && ' not'} been submitted.
          </Text>
        </Flex>
      </Flex>
    </form>
  );
};
```

```tsx
import { Controller, useForm } from 'react-hook-form';

import { Button } from '@dynatrace/strato-components/buttons';
import type { Timeframe } from '@dynatrace/strato-components/core';
import { TimeframeSelector } from '@dynatrace/strato-components/filters';
import {
  FormField,
  FormFieldMessages,
} from '@dynatrace/strato-components/forms';
import { Flex } from '@dynatrace/strato-components/layouts';
import { Heading, Text } from '@dynatrace/strato-components/typography';

const Validate = () => {
  const {
    handleSubmit,
    control,
    formState: { isSubmitSuccessful },
    reset,
  } = useForm<{
    timeframe: Timeframe | null;
  }>({
    mode: 'all',
  });

  return (
    <form
      onSubmit={handleSubmit(() => void 0)}
      onReset={() => reset()}
      noValidate
    >
      <Flex flexDirection="column" gap={16}>
        <Heading level={2}>Register</Heading>
        <Flex flexDirection="column" gap={16}>
          <Controller
            name="timeframe"
            control={control}
            rules={{
              validate: (value) =>
                (value?.from &&
                  value.from.type === 'expression' &&
                  value?.to &&
                  value.to.type === 'expression') ||
                'Please only enter expressions in the from and to value',
            }}
            render={({ field, fieldState: { error } }) => (
              <FormField required>
                <TimeframeSelector
                  aria-label="Timeframe selector"
                  /* eslint-disable-next-line @typescript-eslint/no-deprecated */
                  clearable
                  {...field}
                />
                <FormFieldMessages>
                  {(msgs) => {
                    if (msgs.length > 0) {
                      return msgs.map((msgs) => (
                        <FormFieldMessages.Item key={msgs.id} {...msgs} />
                      ));
                    }

                    if (error) {
                      return (
                        <FormFieldMessages.Item
                          variant="error"
                          key={error.type}
                        >
                          {error.message}
                        </FormFieldMessages.Item>
                      );
                    }
                  }}
                </FormFieldMessages>
              </FormField>
            )}
          />
          <Button type="submit" variant="emphasized">
            Submit
          </Button>
          <Text>
            The form has{!isSubmitSuccessful && ' not'} been submitted.
          </Text>
        </Flex>
      </Flex>
    </form>
  );
};
```


### Add custom trigger

`TimeframeSelector` comes with a default trigger for consistent user experience.
In exceptional cases, if it's necessary, you may override the default trigger.
Make sure to communicate whether a timeframe is selected and, if so, the
timeframe itself.

Props are applied automatically to the `TimeframeSelector.CustomTrigger` to
ensure correct semantics. Ideally, use a button as the outermost HTML element
inside the custom trigger.

```tsx
import { useState } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import type { Timeframe } from '@dynatrace/strato-components/core';
import { TimeframeSelector } from '@dynatrace/strato-components/filters';
import { ClockIcon } from '@dynatrace/strato-icons';

const CustomTrigger = () => {
  const [value, setValue] = useState<Timeframe | null>(null);

  return (
    <TimeframeSelector
      aria-label="Timeframe selector (icon only)"
      value={value}
      onChange={setValue}
    >
      <TimeframeSelector.CustomTrigger>
        <Button
          aria-label="Timeframe selector decorative trigger"
          variant="emphasized"
        >
          <Button.Prefix>
            <ClockIcon />
          </Button.Prefix>
        </Button>
      </TimeframeSelector.CustomTrigger>
    </TimeframeSelector>
  );
};
```

```tsx
import { useState } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import type { Timeframe } from '@dynatrace/strato-components/core';
import { TimeframeSelector } from '@dynatrace/strato-components/filters';
import { ClockIcon } from '@dynatrace/strato-icons';

const CustomTrigger = () => {
  const [value, setValue] = useState<Timeframe | null>(null);

  return (
    <TimeframeSelector
      aria-label="Timeframe selector (icon only)"
      value={value}
      onChange={setValue}
    >
      <TimeframeSelector.CustomTrigger>
        <Button
          aria-label="Timeframe selector decorative trigger"
          variant="emphasized"
        >
          <Button.Prefix>
            <ClockIcon />
          </Button.Prefix>
        </Button>
      </TimeframeSelector.CustomTrigger>
    </TimeframeSelector>
  );
};
```


### Show custom placeholder

Use the `TimeframeSelector.Trigger` and the `placeholder` prop to show a
placeholder for the trigger button. If no option is selected, the `placeholder`
value is shown by default. Notice that the `clearable` prop is used here to
enable empty selection.

```tsx
import { useState } from 'react';

import type { Timeframe } from '@dynatrace/strato-components/core';
import { TimeframeSelector } from '@dynatrace/strato-components/filters';

const Placeholder = () => {
  const [value, setValue] = useState<Timeframe | null>(null);

  return (
    <TimeframeSelector
      aria-label="Timeframe selector"
      /* eslint-disable-next-line @typescript-eslint/no-deprecated */
      clearable
      value={value}
      onChange={setValue}
    >
      <TimeframeSelector.Trigger
        placeholder="Select a timeframe"
        aria-label="Open timeframe selector overlay"
      />
    </TimeframeSelector>
  );
};
```

```tsx
import { useState } from 'react';

import type { Timeframe } from '@dynatrace/strato-components/core';
import { TimeframeSelector } from '@dynatrace/strato-components/filters';

const Placeholder = () => {
  const [value, setValue] = useState<Timeframe | null>(null);

  return (
    <TimeframeSelector
      aria-label="Timeframe selector"
      /* eslint-disable-next-line @typescript-eslint/no-deprecated */
      clearable
      value={value}
      onChange={setValue}
    >
      <TimeframeSelector.Trigger
        placeholder="Select a timeframe"
        aria-label="Open timeframe selector overlay"
      />
    </TimeframeSelector>
  );
};
```


### Render custom trigger

We also provide a render function for the `TimeframeSelector.CustomTrigger`,
giving you access to the `displayValue` that the TimeframeSelector would have
applied. This enables you to understand the internal logic of the component
before you customize it. When using a render function here, make sure to spread
the props to the trigger element so the interactions tie back to the
`TimeframeSelector`.

```tsx
<TimeframeSelector
  aria-label="Timeframe selector (icon only)"
  value={value}
  onChange={setValue}
>
  <TimeframeSelector.CustomTrigger>
    {({ displayValue }, props) => (
      <Button {...props} aria-label="Timeframe selector trigger">
        Custom element with default displayValue:&nbsp;{displayValue}
      </Button>
    )}
  </TimeframeSelector.CustomTrigger>
</TimeframeSelector>
```

```tsx
<TimeframeSelector
  aria-label="Timeframe selector (icon only)"
  value={value}
  onChange={setValue}
>
  <TimeframeSelector.CustomTrigger>
    {({ displayValue }, props) => (
      <Button {...props} aria-label="Timeframe selector trigger">
        Custom element with default displayValue:&nbsp;{displayValue}
      </Button>
    )}
  </TimeframeSelector.CustomTrigger>
</TimeframeSelector>
```


### Enable stepper

When a timeframe is selected, backward and forward arrows are shown next to the
`TimeframeSelector` trigger. Clicking an arrow shifts the timeframe by its
current duration. Set the `stepper` prop to `false` to disable the stepper if
desired.

NoteThe `onChange` callback is debounced by 300 ms, so rapidly clicking the
arrows will only trigger a single `onChange` call once the user stops clicking.
The trigger value updates immediately for responsive UI feedback.

```tsx
import { TimeframeSelector } from '@dynatrace/strato-components/filters';

const TimeframeStepper = () => {
  return (
    <TimeframeSelector
      defaultValue={{ from: 'now()-2h', to: 'now()' }}
      stepper
    />
  );
};
```

```tsx
import { TimeframeSelector } from '@dynatrace/strato-components/filters';

const TimeframeStepper = () => {
  return (
    <TimeframeSelector
      defaultValue={{ from: 'now()-2h', to: 'now()' }}
      stepper
    />
  );
};
```


### Related

#### Patterns

- Filtering

#### Documentation

- Timeframe selector
Still have questions?Find answers in the Dynatrace Community
- Import
- Demo
- Control state
- Set initial values
- Customize presets
- Enable timeframe reset
- Set display precision
- Set min and max values
- Validate user input
- Add custom trigger
- Show custom placeholder
- Render custom trigger
- Enable stepper
- Related
- Patterns
- Documentation

### Props

`TimeframeSelector` is a filtering component that lets users choose from preset
timeframes or add unique "from" and "to" time values of their own.

#### TimeframeSelectorProps

##### Signature:
`export declare type SelectorProps = | <> | , (value: | ) => > & & & & & & {
 /**
 * Shows the button if set to true.
 * @defaultValue false
 * @deprecated The `clearable` prop is deprecated in favor of the new clear button directly located in the input.
 */
 clearable?: ;
 /**
 * The ISODatetime of the earliest datetime that can be configured.
 * @defaultValue '1677-09-21T00:12:43.145224192Z'
 */
 min?: ;
 /**
 * The ISODatetime of the latest datetime that can be configured.
 * @defaultValue '2262-04-11T23:47:16.854775807Z'
 */
 max?: ;
 /**
 * The precision of the time shown in the display value.
 * @defaultValue
 */
 precision?: | | ;
 /**
 * Whether the Stepper is shown.
 * @defaultValue true
 */
 stepper?: ;
};`

#### TimeframeSelector presets components

##### TimeframeSelector.Presets

The `TimeframeSelector.Presets` component is used to render the list of preset
items shown in the overlay.

#### TimeframeSelectorPresetsProps
extends`, , , , ` |
 | Name | Type | Default | Description
 | `children?` | | | Children shown inside the presets list. A default list of presets is shown if no children are set.

##### TimeframeSelector.PresetItem

The `TimeframeSelector.PresetItem` component is used to render a preset item to
the list of presets shown in the overlay. This needs to be used inside the
`TimeframeSelector.Presets` component.

#### TimeframeSelectorPresetItemProps
extends`<>, , , , ` |
 | Name | Type | Default | Description
 | `value` | {
 /** Start of the time frame. */
 from: ;
 /** End of the time frame. */
 to: ;
 } | | The value of the timeframe preset.

#### TimeframeSelector trigger components

##### TimeframeSelector.Trigger

The `TimeframeSelector.Trigger` component is used to render the trigger that
opens or closes the overlay.

#### TimeframeSelectorTriggerProps

##### Signature:
`export declare type TimeframeSelectorTriggerProps = & & & & & {
 /**
 * The placeholder text displayed in the TimeframeSelector.Trigger.
 */
 placeholder?: ;
};`

##### TimeframeSelector.DisplayValue

#### TimeframeSelectorDisplayValueProps

##### Signature:
`export declare type TimeframeSelectorDisplayValueProps = & {
 children?: | ((customTriggerProps: {
 displayValue: ;
 }) => );
};`

##### TimeframeSelector.CustomTrigger

#### TimeframeSelectorCustomTriggerProps

##### Signature:
`export declare type TimeframeSelectorCustomTriggerProps = & & & & {
 /** Elements to be displayed in the CustomTrigger. */
 children: | | ((customTriggerProps: {
 displayValue: ;
 isInvalid: ;
 hint: ;
 }, props: ( & & & (>> & )) | ) => );
};`Still have questions?Find answers in the Dynatrace Community
- TimeframeSelector presets components
- TimeframeSelector trigger components

---

