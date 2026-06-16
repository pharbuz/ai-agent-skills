# Geo maps (data visualizations)

Strato design-system components in the **Geo maps (data visualizations)** group. Source: <https://developer.dynatrace.com/design/components/>.

Import from `@dynatrace/strato-components` (or `.../strato-components-preview` for preview components). Each section lists the component, its doc path, an overview, and its props.

> Note: prop **Type** values may be partial or empty here — the doc site renders
> full TypeScript types client-side, so static capture misses some. Names, defaults,
> and descriptions are reliable; for exact types open the linked live page.

## BaseLayer

`/design/data-visualizations/geo-maps/BaseLayer/`

The base layer component, used to configure the inclusion and exclusion of
countries and regions

OverviewProperties

### Import

`tsx
import { BaseLayer } from '@dynatrace/strato-geo';
`

### Use cases

Use the `BaseLayer` component to render a map with controlled countries and
regions. It accepts an array of country codes and region codes in ISO 3166-2
format as `include` or `exclude` props to control the display of regions on the
map. Use the `*` symbol to include all countries and the `-*` suffix to include
all country states. You can control the display of both countries and regions in
the same array.

`tsx
const include = ['ES-*', 'AT'];const exclude = ['ES-CT'];
`

Learn more about the data format here.

#### Inclusion/Exclusion of countries

##### Include only Spain and Austria

```tsx
import { BaseLayer, MapView } from '@dynatrace/strato-geo';

const BaseLayerSimple = () => {
  const austriaSpainViewState = {
    longitude: 11,
    latitude: 42,
    zoom: 3,
  };

  return (
    <MapView initialViewState={austriaSpainViewState} height={500}>
      <BaseLayer include={['ES', 'AT']}></BaseLayer>
    </MapView>
  );
};
```

```tsx
import { BaseLayer, MapView } from '@dynatrace/strato-geo';

const BaseLayerSimple = () => {
  const austriaSpainViewState = {
    longitude: 11,
    latitude: 42,
    zoom: 3,
  };

  return (
    <MapView initialViewState={austriaSpainViewState} height={500}>
      <BaseLayer include={['ES', 'AT']}></BaseLayer>
    </MapView>
  );
};
```


##### Include all countries, without Spain and Austria

```tsx
import { BaseLayer, MapView } from '@dynatrace/strato-geo';

const BaseLayerExcludeCountries = () => {
  const austriaSpainViewState = {
    longitude: 11,
    latitude: 42,
    zoom: 3,
  };

  return (
    <MapView initialViewState={austriaSpainViewState} height={500}>
      <BaseLayer include={['*']} exclude={['ES', 'AT']}></BaseLayer>
    </MapView>
  );
};
```

```tsx
import { BaseLayer, MapView } from '@dynatrace/strato-geo';

const BaseLayerExcludeCountries = () => {
  const austriaSpainViewState = {
    longitude: 11,
    latitude: 42,
    zoom: 3,
  };

  return (
    <MapView initialViewState={austriaSpainViewState} height={500}>
      <BaseLayer include={['*']} exclude={['ES', 'AT']}></BaseLayer>
    </MapView>
  );
};
```


#### Mix of country and state level regions

##### Include all countries, and all regions of Spain and Austria

```tsx
import { BaseLayer, MapView } from '@dynatrace/strato-geo';

const BaseLayerRegions = () => {
  const austriaSpainViewState = {
    longitude: 11,
    latitude: 42,
    zoom: 3,
  };

  return (
    <MapView initialViewState={austriaSpainViewState} height={500}>
      <BaseLayer include={['*', 'AT-*', 'ES-*']}></BaseLayer>
    </MapView>
  );
};
```

```tsx
import { BaseLayer, MapView } from '@dynatrace/strato-geo';

const BaseLayerRegions = () => {
  const austriaSpainViewState = {
    longitude: 11,
    latitude: 42,
    zoom: 3,
  };

  return (
    <MapView initialViewState={austriaSpainViewState} height={500}>
      <BaseLayer include={['*', 'AT-*', 'ES-*']}></BaseLayer>
    </MapView>
  );
};
```


##### Include Spain and Austria, without regions: Catalonia, Madrid, Vienna, Upper Austria

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Inclusion/Exclusion of countries
- Mix of country and state level regions

```tsx
import { BaseLayer, MapView } from '@dynatrace/strato-geo';

const BaseLayerExcludeRegions = () => {
  const austriaSpainViewState = {
    longitude: 11,
    latitude: 42,
    zoom: 3,
  };

  return (
    <MapView initialViewState={austriaSpainViewState} height={500}>
      <BaseLayer
        include={['ES-*', 'AT-*']}
        exclude={['ES-CT', 'ES-MD', 'AT-9', 'AT-4']}
      ></BaseLayer>
    </MapView>
  );
};
```

```tsx
import { BaseLayer, MapView } from '@dynatrace/strato-geo';

const BaseLayerExcludeRegions = () => {
  const austriaSpainViewState = {
    longitude: 11,
    latitude: 42,
    zoom: 3,
  };

  return (
    <MapView initialViewState={austriaSpainViewState} height={500}>
      <BaseLayer
        include={['ES-*', 'AT-*']}
        exclude={['ES-CT', 'ES-MD', 'AT-9', 'AT-4']}
      ></BaseLayer>
    </MapView>
  );
};
```


### Props

The base layer component, used to configure the inclusion and exclusion of
countries and regions

OverviewProperties

### BaseLayer

#### BaseLayerProps
 |
 | Name | Type | Default | Description
 | `include?` | [] | | Include countries
 | `exclude?` | [] | | Exclude countriesStill have questions?Find answers in the Dynatrace Community
---

## BubbleLayer

`/design/data-visualizations/geo-maps/BubbleLayer/`

The `BubbleLayer` component renders data points as bubbles on a map, accepting
an array of data points with required properties like latitude and longitude. It
supports customization of bubble size using the radius prop and optional
tooltips for displaying additional information.

OverviewProperties

### Import

`tsx
import { BubbleLayer } from '@dynatrace/strato-geo';
`

### Use cases

Use the `BubbleLayer` component to render data points with customizable radius.
The `BubbleLayer` component accepts an array of data points as the data prop.
Each data point must have `latitude` and `longitude` as minimum required
properties.

`tsx
[ { radius: 85, longitude: -115.195615, latitude: 36.171462, }, { radius: 35, longitude: -94.556725, latitude: 39.104532, }, { radius: 40, longitude: -73.998772, latitude: 40.717575, },];
`

Learn more about the data format here.

```tsx
import { BubbleLayer, Location, MapView } from '@dynatrace/strato-geo';

type CyberAttackEvent = {
  id: string;
  distancePrecision: number;
  severity: 'high' | 'medium' | 'low';
} & Location;

const cyberAttacks: CyberAttackEvent[] = [
  {
    id: 'CYB-2024-001',
    distancePrecision: 85,
    severity: 'high',
    longitude: -115.195615,
    latitude: 36.171462,
  },
  {
    id: 'CYB-2024-002',
    distancePrecision: 35,
    severity: 'medium',
    longitude: -94.556725,
    latitude: 39.104532,
  },
  {
    id: 'CYB-2024-003',
    distancePrecision: 40,
    severity: 'low',
    longitude: -73.998772,
    latitude: 40.717575,
  },
  {
    id: 'CYB-2024-004',
    distancePrecision: 50,
    severity: 'high',
    longitude: -87.773124,
    latitude: 41.786535,
  },
  {
    id: 'CYB-2024-005',
    distancePrecision: 60,
    severity: 'low',
    longitude: -122.293741,
    latitude: 47.545032,
  },
];

const BubbleLayerSimple = () => {
  const initialViewState = {
    longitude: -101.465989,
    latitude: 40.822381,
    zoom: 3,
  };

  return (
    <MapView initialViewState={initialViewState} height={400}>
      <BubbleLayer
        data={cyberAttacks}
        radius={(cyberAttack: CyberAttackEvent) =>
          cyberAttack.distancePrecision
        }
      />
    </MapView>
  );
};
```

```tsx
import { BubbleLayer, Location, MapView } from '@dynatrace/strato-geo';

type CyberAttackEvent = {
  id: string;
  distancePrecision: number;
  severity: 'high' | 'medium' | 'low';
} & Location;

const cyberAttacks: CyberAttackEvent[] = [
  {
    id: 'CYB-2024-001',
    distancePrecision: 85,
    severity: 'high',
    longitude: -115.195615,
    latitude: 36.171462,
  },
  {
    id: 'CYB-2024-002',
    distancePrecision: 35,
    severity: 'medium',
    longitude: -94.556725,
    latitude: 39.104532,
  },
  {
    id: 'CYB-2024-003',
    distancePrecision: 40,
    severity: 'low',
    longitude: -73.998772,
    latitude: 40.717575,
  },
  {
    id: 'CYB-2024-004',
    distancePrecision: 50,
    severity: 'high',
    longitude: -87.773124,
    latitude: 41.786535,
  },
  {
    id: 'CYB-2024-005',
    distancePrecision: 60,
    severity: 'low',
    longitude: -122.293741,
    latitude: 47.545032,
  },
];

const BubbleLayerSimple = () => {
  const initialViewState = {
    longitude: -101.465989,
    latitude: 40.822381,
    zoom: 3,
  };

  return (
    <MapView initialViewState={initialViewState} height={400}>
      <BubbleLayer
        data={cyberAttacks}
        radius={(cyberAttack: CyberAttackEvent) =>
          cyberAttack.distancePrecision
        }
      />
    </MapView>
  );
};
```


#### Size interpolation

The `sizeInterpolation` prop determines how the size of the bubbles changes with
zoom level.

- `'zoom'`: The size of the bubbles adjusts dynamically based on the zoom level
of the map. As the user zooms in or out, the bubble sizes change accordingly
to maintain relative proportions.

- `'fixed'`:The size of the bubbles remains constant regardless of the zoom
level. This means that as the user zooms in or out, the size of the bubbles on
the map remains the same, offering consistent visual representation.

```tsx
import { useState } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import { BubbleLayer, Location, MapView } from '@dynatrace/strato-geo';

type CyberAttackEvent = {
  id: string;
  distancePrecision: number;
  severity: 'high' | 'medium' | 'low';
} & Location;

const cyberAttacks: CyberAttackEvent[] = [
  {
    id: 'CYB-2024-001',
    distancePrecision: 85,
    severity: 'high',
    longitude: -115.195615,
    latitude: 36.171462,
  },
  {
    id: 'CYB-2024-002',
    distancePrecision: 35,
    severity: 'medium',
    longitude: -94.556725,
    latitude: 39.104532,
  },
  {
    id: 'CYB-2024-003',
    distancePrecision: 40,
    severity: 'low',
    longitude: -73.998772,
    latitude: 40.717575,
  },
  {
    id: 'CYB-2024-004',
    distancePrecision: 50,
    severity: 'high',
    longitude: -87.773124,
    latitude: 41.786535,
  },
  {
    id: 'CYB-2024-005',
    distancePrecision: 60,
    severity: 'low',
    longitude: -122.293741,
    latitude: 47.545032,
  },
];

const BubbleLayerSizeInterpolationZoom = () => {
  const [sizeInterpolation, setSizeInterpolation] = useState<'zoom' | 'fixed'>(
    'zoom'
  );

  const initialViewState = {
    longitude: -101.465989,
    latitude: 40.822381,
    zoom: 3,
  };

  return (
    <>
      <Button
        onClick={() => {
          setSizeInterpolation('zoom');
        }}
        variant="emphasized"
        disabled={sizeInterpolation === 'zoom'}
        style={{ margin: '4px 2px' }}
      >
        Size interpolation: Zoom
      </Button>
      <Button
        onClick={() => {
          setSizeInterpolation('fixed');
        }}
        variant="emphasized"
        disabled={sizeInterpolation === 'fixed'}
        style={{ margin: '4px 2px' }}
      >
        Size interpolation: Fixed
      </Button>

      <MapView initialViewState={initialViewState} height={400}>
        <BubbleLayer
          data={cyberAttacks}
          radius={(cyberAttack: CyberAttackEvent) =>
            cyberAttack.distancePrecision
          }
          sizeInterpolation={sizeInterpolation}
        />
      </MapView>
    </>
  );
};
```

```tsx
import { useState } from 'react';

import { Button } from '@dynatrace/strato-components/buttons';
import { BubbleLayer, Location, MapView } from '@dynatrace/strato-geo';

type CyberAttackEvent = {
  id: string;
  distancePrecision: number;
  severity: 'high' | 'medium' | 'low';
} & Location;

const cyberAttacks: CyberAttackEvent[] = [
  {
    id: 'CYB-2024-001',
    distancePrecision: 85,
    severity: 'high',
    longitude: -115.195615,
    latitude: 36.171462,
  },
  {
    id: 'CYB-2024-002',
    distancePrecision: 35,
    severity: 'medium',
    longitude: -94.556725,
    latitude: 39.104532,
  },
  {
    id: 'CYB-2024-003',
    distancePrecision: 40,
    severity: 'low',
    longitude: -73.998772,
    latitude: 40.717575,
  },
  {
    id: 'CYB-2024-004',
    distancePrecision: 50,
    severity: 'high',
    longitude: -87.773124,
    latitude: 41.786535,
  },
  {
    id: 'CYB-2024-005',
    distancePrecision: 60,
    severity: 'low',
    longitude: -122.293741,
    latitude: 47.545032,
  },
];

const BubbleLayerSizeInterpolationZoom = () => {
  const [sizeInterpolation, setSizeInterpolation] = useState<'zoom' | 'fixed'>(
    'zoom'
  );

  const initialViewState = {
    longitude: -101.465989,
    latitude: 40.822381,
    zoom: 3,
  };

  return (
    <>
      <Button
        onClick={() => {
          setSizeInterpolation('zoom');
        }}
        variant="emphasized"
        disabled={sizeInterpolation === 'zoom'}
        style={{ margin: '4px 2px' }}
      >
        Size interpolation: Zoom
      </Button>
      <Button
        onClick={() => {
          setSizeInterpolation('fixed');
        }}
        variant="emphasized"
        disabled={sizeInterpolation === 'fixed'}
        style={{ margin: '4px 2px' }}
      >
        Size interpolation: Fixed
      </Button>

      <MapView initialViewState={initialViewState} height={400}>
        <BubbleLayer
          data={cyberAttacks}
          radius={(cyberAttack: CyberAttackEvent) =>
            cyberAttack.distancePrecision
          }
          sizeInterpolation={sizeInterpolation}
        />
      </MapView>
    </>
  );
};
```


#### Scale and radius

The `scale` prop controls how the size of the bubbles is scaled, affecting their
visual representation on the map.

##### Linear Scaling

This is the default scaling mode, in which the size of the bubbles is scaled
linearly based on the data range provided. The size of the bubbles increases or
decreases proportionally to data values.

In this scaling mode, the value accessor has to be explicitly provided by
passing to the `radius` prop a callback that returns the value which will be
used to calculate the scale.

Additionally, when using linear scaling, you have the option to specify a
`radiusRange`, which is an array or the minimum and maximum sizes for the bubble
radius in pixels. This allows more control over the size range of bubble
displayed on the map.

```tsx
<MapView initialViewState={initialViewState} height={400}>
  <BubbleLayer
    data={cyberAttacks}
    radius={(cyberAttack: CyberAttackEvent) => cyberAttack.distancePrecision}
    radiusRange={[10, 50]}
    scale="log"
    sizeInterpolation="zoom"
  />
</MapView>
```

```tsx
<MapView initialViewState={initialViewState} height={400}>
  <BubbleLayer
    data={cyberAttacks}
    radius={(cyberAttack: CyberAttackEvent) => cyberAttack.distancePrecision}
    radiusRange={[10, 50]}
    scale="log"
    sizeInterpolation="zoom"
  />
</MapView>
```


##### Logarithmic Scaling

Alternatively, setting the `scale` prop to `'log'` applies logarithmic scaling
to the bubble sizes. Logarithmic scaling is useful for representing data that
spans several orders of magnitude, as it compresses the range of values into a
more visually manageable scale.

Similar to linear scaling, logarithmic scaling also allows for specifying a
`radiusRange` to define the minimum and maximum sizes for the bubble radius.

In this scaling mode, the `radius` prop must be callback function that
dynamically calculates the radius based on the data points.

##### No Scaling

In contrast, when the scale prop is set to `'none'`, no automatic scaling is
applied to the bubble size. A constant number must be provided for the `radius`
prop to set the size of all bubbles uniformly, or a callback function that will
be run for each data point and the returned value used as a radius. When
`radius` prop is not set, the default radius of 12px will be applied.

Be aware, that the `radiusRange` prop is not supported in `none` scaling mode
because it's not possible to derive the scaling mechanism for the provided
range.

#### Tooltip

The `BubbleLayer` component has an optional tooltip that displays additional
data point information when hovering over data points from any of the data
layers. To enable the tooltip a `BubbleLayer.Tooltip` subcomponent should be
passed inside the `BubbleLayer` component. When a `BubbleLayer.Tooltip`
subcomponent is provided without any children, the default tooltip will be used.

By default, the tooltip will display the location information of the hovered
bubble, but
it can be heavily customized.

```tsx
import {
  BubbleLayer,
  BubbleLayerTooltipData,
  Location,
  MapView,
  Tooltip,
  TooltipAtoms,
} from '@dynatrace/strato-geo';
import { AttackIcon } from '@dynatrace/strato-icons';

type CyberAttackEvent = {
  id: string;
  distancePrecision: number;
  severity: 'high' | 'medium' | 'low';
} & Location;

const cyberAttacks: CyberAttackEvent[] = [
  {
    id: 'CYB-2024-001',
    distancePrecision: 250,
    severity: 'high',
    longitude: -115.195615,
    latitude: 36.171462,
  },
  {
    id: 'CYB-2024-002',
    distancePrecision: 500,
    severity: 'medium',
    longitude: -94.556725,
    latitude: 39.104532,
  },
  {
    id: 'CYB-2024-003',
    distancePrecision: 100,
    severity: 'low',
    longitude: -73.998772,
    latitude: 40.717575,
  },
  {
    id: 'CYB-2024-004',
    distancePrecision: 50,
    severity: 'high',
    longitude: -87.773124,
    latitude: 41.786535,
  },
  {
    id: 'CYB-2024-005',
    distancePrecision: 300,
    severity: 'low',
    longitude: -122.293741,
    latitude: 47.545032,
  },
];

const BubbleLayerTooltip = () => {
  const initialViewState = {
    longitude: -101.465989,
    latitude: 40.822381,
    zoom: 2,
  };

  return (
    <MapView height={400} initialViewState={initialViewState}>
      <BubbleLayer
        data={cyberAttacks}
        radius={(cyberAttack: CyberAttackEvent) =>
          cyberAttack.distancePrecision
        }
      >
        <BubbleLayer.Tooltip>
          {(
            closestAttack: BubbleLayerTooltipData<CyberAttackEvent>,
            cyberAttacks: BubbleLayerTooltipData<CyberAttackEvent>[]
          ) => {
            return (
              <>
                <Tooltip.Header>
                  <Tooltip.Item>
                    <Tooltip.Symbol>
                      <AttackIcon />
                    </Tooltip.Symbol>
                    <Tooltip.Content>
                      <Tooltip.Text variant="secondary">
                        {closestAttack.data.id}
                      </Tooltip.Text>
                    </Tooltip.Content>
                    <Tooltip.Value>
                      <TooltipAtoms.Chip>{`${closestAttack.data.severity} severity`}</TooltipAtoms.Chip>
                    </Tooltip.Value>
                  </Tooltip.Item>
                </Tooltip.Header>
                <Tooltip.Body
                  virtualization={false}
                  style={{ width: '95%', padding: '2px 8px' }}
                >
                  {cyberAttacks.length > 0 ? (
                    cyberAttacks.map((cyberAttack, idx) => {
                      return (
                        <Tooltip.Item
                          key={`${cyberAttack.data.id}${idx}`}
                          style={{ padding: '2px 0' }}
                        >
                          <Tooltip.Content>
                            {cyberAttack.data.id}
                          </Tooltip.Content>
                          <Tooltip.Value variant="chip">
                            {`${cyberAttack.data.severity} severity`}
                          </Tooltip.Value>
                        </Tooltip.Item>
                      );
                    })
                  ) : (
                    <Tooltip.Item style={{ padding: '2px 0' }}>
                      <Tooltip.Content>No other attacks</Tooltip.Content>
                    </Tooltip.Item>
                  )}
                </Tooltip.Body>
                <Tooltip.Footer>
                  <Tooltip.Item>
                    <Tooltip.Content>Total attacks:</Tooltip.Content>
                    <Tooltip.Value variant="chip">
                      {cyberAttacks.length + 1}
                    </Tooltip.Value>
                  </Tooltip.Item>
                </Tooltip.Footer>
              </>
            );
          }}
        </BubbleLayer.Tooltip>
      </BubbleLayer>
    </MapView>
  );
};
```

```tsx
import {
  BubbleLayer,
  BubbleLayerTooltipData,
  Location,
  MapView,
  Tooltip,
  TooltipAtoms,
} from '@dynatrace/strato-geo';
import { AttackIcon } from '@dynatrace/strato-icons';

type CyberAttackEvent = {
  id: string;
  distancePrecision: number;
  severity: 'high' | 'medium' | 'low';
} & Location;

const cyberAttacks: CyberAttackEvent[] = [
  {
    id: 'CYB-2024-001',
    distancePrecision: 250,
    severity: 'high',
    longitude: -115.195615,
    latitude: 36.171462,
  },
  {
    id: 'CYB-2024-002',
    distancePrecision: 500,
    severity: 'medium',
    longitude: -94.556725,
    latitude: 39.104532,
  },
  {
    id: 'CYB-2024-003',
    distancePrecision: 100,
    severity: 'low',
    longitude: -73.998772,
    latitude: 40.717575,
  },
  {
    id: 'CYB-2024-004',
    distancePrecision: 50,
    severity: 'high',
    longitude: -87.773124,
    latitude: 41.786535,
  },
  {
    id: 'CYB-2024-005',
    distancePrecision: 300,
    severity: 'low',
    longitude: -122.293741,
    latitude: 47.545032,
  },
];

const BubbleLayerTooltip = () => {
  const initialViewState = {
    longitude: -101.465989,
    latitude: 40.822381,
    zoom: 2,
  };

  return (
    <MapView height={400} initialViewState={initialViewState}>
      <BubbleLayer
        data={cyberAttacks}
        radius={(cyberAttack: CyberAttackEvent) =>
          cyberAttack.distancePrecision
        }
      >
        <BubbleLayer.Tooltip>
          {(
            closestAttack: BubbleLayerTooltipData<CyberAttackEvent>,
            cyberAttacks: BubbleLayerTooltipData<CyberAttackEvent>[]
          ) => {
            return (
              <>
                <Tooltip.Header>
                  <Tooltip.Item>
                    <Tooltip.Symbol>
                      <AttackIcon />
                    </Tooltip.Symbol>
                    <Tooltip.Content>
                      <Tooltip.Text variant="secondary">
                        {closestAttack.data.id}
                      </Tooltip.Text>
                    </Tooltip.Content>
                    <Tooltip.Value>
                      <TooltipAtoms.Chip>{`${closestAttack.data.severity} severity`}</TooltipAtoms.Chip>
                    </Tooltip.Value>
                  </Tooltip.Item>
                </Tooltip.Header>
                <Tooltip.Body
                  virtualization={false}
                  style={{ width: '95%', padding: '2px 8px' }}
                >
                  {cyberAttacks.length > 0 ? (
                    cyberAttacks.map((cyberAttack, idx) => {
                      return (
                        <Tooltip.Item
                          key={`${cyberAttack.data.id}${idx}`}
                          style={{ padding: '2px 0' }}
                        >
                          <Tooltip.Content>
                            {cyberAttack.data.id}
                          </Tooltip.Content>
                          <Tooltip.Value variant="chip">
                            {`${cyberAttack.data.severity} severity`}
                          </Tooltip.Value>
                        </Tooltip.Item>
                      );
                    })
                  ) : (
                    <Tooltip.Item style={{ padding: '2px 0' }}>
                      <Tooltip.Content>No other attacks</Tooltip.Content>
                    </Tooltip.Item>
                  )}
                </Tooltip.Body>
                <Tooltip.Footer>
                  <Tooltip.Item>
                    <Tooltip.Content>Total attacks:</Tooltip.Content>
                    <Tooltip.Value variant="chip">
                      {cyberAttacks.length + 1}
                    </Tooltip.Value>
                  </Tooltip.Item>
                </Tooltip.Footer>
              </>
            );
          }}
        </BubbleLayer.Tooltip>
      </BubbleLayer>
    </MapView>
  );
};
```


#### Coloring

The `BubbleLayer` supports two ways of color configuration: granular
configuration using the `color` prop, or using a one of the available legend
subcomponents (e.g. `SequentialLegend`, `ThresholdLegend`, or
`CategoricalLegend`).

Note: Detailed information about coloring can be found in the `MapView`
documentation page under the `Coloring` section.

#### Granular color configuration

For a granular color customization, layer's `color` prop should be used.

```tsx
import Colors from '@dynatrace/strato-design-tokens/colors';
import { BubbleLayer, Location, MapView } from '@dynatrace/strato-geo';

type CyberAttackEvent = {
  id: string;
  distancePrecision: number;
  severity: 'high' | 'medium' | 'low';
} & Location;

const cyberAttacks: CyberAttackEvent[] = [
  {
    id: 'CYB-2024-001',
    distancePrecision: 85,
    severity: 'high',
    longitude: -115.195615,
    latitude: 36.171462,
  },
  {
    id: 'CYB-2024-002',
    distancePrecision: 35,
    severity: 'medium',
    longitude: -94.556725,
    latitude: 39.104532,
  },
  {
    id: 'CYB-2024-003',
    distancePrecision: 40,
    severity: 'low',
    longitude: -73.998772,
    latitude: 40.717575,
  },
  {
    id: 'CYB-2024-004',
    distancePrecision: 50,
    severity: 'high',
    longitude: -87.773124,
    latitude: 41.786535,
  },
  {
    id: 'CYB-2024-005',
    distancePrecision: 60,
    severity: 'low',
    longitude: -122.293741,
    latitude: 47.545032,
  },
];

const BubbleLayerCustomColor = () => {
  const initialViewState = {
    longitude: -101.465989,
    latitude: 40.822381,
    zoom: 3,
  };
  const callbackColor = (attack: CyberAttackEvent) => {
    if (attack.severity === 'low') {
      return Colors.Charts.Threshold.Good.Default;
    } else if (attack.severity === 'medium') {
      return Colors.Charts.Threshold.Warning.Default;
    } else {
      return Colors.Charts.Threshold.Bad.Default;
    }
  };

  return (
    <MapView initialViewState={initialViewState} height={400}>
      <BubbleLayer
        data={cyberAttacks}
        color={callbackColor}
        radius={(cyberAttack: CyberAttackEvent) =>
          cyberAttack.distancePrecision
        }
        sizeInterpolation="zoom"
      />
    </MapView>
  );
};
```

```tsx
import Colors from '@dynatrace/strato-design-tokens/colors';
import { BubbleLayer, Location, MapView } from '@dynatrace/strato-geo';

type CyberAttackEvent = {
  id: string;
  distancePrecision: number;
  severity: 'high' | 'medium' | 'low';
} & Location;

const cyberAttacks: CyberAttackEvent[] = [
  {
    id: 'CYB-2024-001',
    distancePrecision: 85,
    severity: 'high',
    longitude: -115.195615,
    latitude: 36.171462,
  },
  {
    id: 'CYB-2024-002',
    distancePrecision: 35,
    severity: 'medium',
    longitude: -94.556725,
    latitude: 39.104532,
  },
  {
    id: 'CYB-2024-003',
    distancePrecision: 40,
    severity: 'low',
    longitude: -73.998772,
    latitude: 40.717575,
  },
  {
    id: 'CYB-2024-004',
    distancePrecision: 50,
    severity: 'high',
    longitude: -87.773124,
    latitude: 41.786535,
  },
  {
    id: 'CYB-2024-005',
    distancePrecision: 60,
    severity: 'low',
    longitude: -122.293741,
    latitude: 47.545032,
  },
];

const BubbleLayerCustomColor = () => {
  const initialViewState = {
    longitude: -101.465989,
    latitude: 40.822381,
    zoom: 3,
  };
  const callbackColor = (attack: CyberAttackEvent) => {
    if (attack.severity === 'low') {
      return Colors.Charts.Threshold.Good.Default;
    } else if (attack.severity === 'medium') {
      return Colors.Charts.Threshold.Warning.Default;
    } else {
      return Colors.Charts.Threshold.Bad.Default;
    }
  };

  return (
    <MapView initialViewState={initialViewState} height={400}>
      <BubbleLayer
        data={cyberAttacks}
        color={callbackColor}
        radius={(cyberAttack: CyberAttackEvent) =>
          cyberAttack.distancePrecision
        }
        sizeInterpolation="zoom"
      />
    </MapView>
  );
};
```


#### Color configuration using a legend

To connect a data layer to the legend, a `color` property of the layer should be
set to `legend` string.

##### Sequential legend

```tsx
import {
  BubbleLayer,
  Location,
  MapView,
  SequentialLegend,
} from '@dynatrace/strato-geo';

type Earthquake = {
  magnitude: number;
  tsunami: number;
} & Location;

const earthquakes: Earthquake[] = [
  {
    longitude: -155.7645,
    latitude: 19.608333,
    magnitude: 1.47,
    tsunami: 0,
  },
  {
    longitude: -111.456667,
    latitude: 42.600833,
    magnitude: 1.84,
    tsunami: 0,
  },
  {
    longitude: -152.8997,
    latitude: 62.5624,
    magnitude: 1.4,
    tsunami: 0,
  },
  {
    longitude: -147.6239,
    latitude: 61.9391,
    magnitude: 2,
    tsunami: 0,
  },
  {
    longitude: -155.6845,
    latitude: 18.778833,
    magnitude: 2.06,
    tsunami: 0,
  },
  {
    longitude: -149.0205,
    latitude: 61.3011,
    magnitude: 1.7,
    tsunami: 0,
  },
  {
    longitude: -149.1141,
    latitude: 63.8125,
    magnitude: 1.6,
    tsunami: 0,
  },
  {
    longitude: -116.364,
    latitude: 33.395667,
    magnitude: 0.97,
    tsunami: 0,
  },
  {
    longitude: -118.118,
    latitude: 33.743333,
    magnitude: 1.15,
    tsunami: 0,
  },
  {
    longitude: -178.1517,
    latitude: -31.5827,
    magnitude: 5,
    tsunami: 0,
  },
  {
    longitude: -173.6834,
    latitude: 51.2465,
    magnitude: 2,
    tsunami: 0,
  },
  {
    longitude: -139.521,
    latitude: 59.9658,
    magnitude: 1.3,
    tsunami: 0,
  },
  {
    longitude: -121.7125,
    latitude: 37.351167,
    magnitude: 1.22,
    tsunami: 0,
  },
  {
    longitude: -73.1491,
    latitude: 7.5135,
    magnitude: 5.1,
    tsunami: 0,
  },
  {
    longitude: -116.354833,
    latitude: 33.961167,
    magnitude: 1.75,
    tsunami: 0,
  },
  {
    longitude: 140.5685,
    latitude: 36.9167,
    magnitude: 4.9,
    tsunami: 0,
  },
  {
    longitude: -169.8117,
    latitude: 51.8357,
    magnitude: 2.5,
    tsunami: 0,
  },
  {
    longitude: -117.119167,
    latitude: 33.9365,
    magnitude: 1,
    tsunami: 0,
  },
  {
    longitude: -153.8841,
    latitude: 57.2184,
    magnitude: 1.3,
    tsunami: 0,
  },
  {
    longitude: -150.4019,
    latitude: 63.1122,
    magnitude: 1,
    tsunami: 0,
  },
  {
    longitude: -70.2379,
    latitude: -31.7388,
    magnitude: 3.9,
    tsunami: 0,
  },
  {
    longitude: -115.605333,
    latitude: 32.8245,
    magnitude: 1.54,
    tsunami: 0,
  },
  {
    longitude: -111.4244,
    latitude: 42.5958,
    magnitude: 2.5,
    tsunami: 0,
  },
  {
    longitude: -119.12,
    latitude: 38.2855,
    magnitude: 1.3,
    tsunami: 0,
  },
  {
    longitude: -121.059667,
    latitude: 36.477833,
    magnitude: 1.21,
    tsunami: 0,
  },
];

const BubbleLayerSequentialLegendColor = () => {
  return (
    <MapView height={400}>
      <BubbleLayer
        data={earthquakes}
        color="legend"
        valueAccessor="magnitude"
        radius={({ magnitude }) => magnitude * 3}
        scale="none"
      />
      <SequentialLegend min={0} max={8} colorPalette="blue" />
    </MapView>
  );
};
```

```tsx
import {
  BubbleLayer,
  Location,
  MapView,
  SequentialLegend,
} from '@dynatrace/strato-geo';

type Earthquake = {
  magnitude: number;
  tsunami: number;
} & Location;

const earthquakes: Earthquake[] = [
  {
    longitude: -155.7645,
    latitude: 19.608333,
    magnitude: 1.47,
    tsunami: 0,
  },
  {
    longitude: -111.456667,
    latitude: 42.600833,
    magnitude: 1.84,
    tsunami: 0,
  },
  {
    longitude: -152.8997,
    latitude: 62.5624,
    magnitude: 1.4,
    tsunami: 0,
  },
  {
    longitude: -147.6239,
    latitude: 61.9391,
    magnitude: 2,
    tsunami: 0,
  },
  {
    longitude: -155.6845,
    latitude: 18.778833,
    magnitude: 2.06,
    tsunami: 0,
  },
  {
    longitude: -149.0205,
    latitude: 61.3011,
    magnitude: 1.7,
    tsunami: 0,
  },
  {
    longitude: -149.1141,
    latitude: 63.8125,
    magnitude: 1.6,
    tsunami: 0,
  },
  {
    longitude: -116.364,
    latitude: 33.395667,
    magnitude: 0.97,
    tsunami: 0,
  },
  {
    longitude: -118.118,
    latitude: 33.743333,
    magnitude: 1.15,
    tsunami: 0,
  },
  {
    longitude: -178.1517,
    latitude: -31.5827,
    magnitude: 5,
    tsunami: 0,
  },
  {
    longitude: -173.6834,
    latitude: 51.2465,
    magnitude: 2,
    tsunami: 0,
  },
  {
    longitude: -139.521,
    latitude: 59.9658,
    magnitude: 1.3,
    tsunami: 0,
  },
  {
    longitude: -121.7125,
    latitude: 37.351167,
    magnitude: 1.22,
    tsunami: 0,
  },
  {
    longitude: -73.1491,
    latitude: 7.5135,
    magnitude: 5.1,
    tsunami: 0,
  },
  {
    longitude: -116.354833,
    latitude: 33.961167,
    magnitude: 1.75,
    tsunami: 0,
  },
  {
    longitude: 140.5685,
    latitude: 36.9167,
    magnitude: 4.9,
    tsunami: 0,
  },
  {
    longitude: -169.8117,
    latitude: 51.8357,
    magnitude: 2.5,
    tsunami: 0,
  },
  {
    longitude: -117.119167,
    latitude: 33.9365,
    magnitude: 1,
    tsunami: 0,
  },
  {
    longitude: -153.8841,
    latitude: 57.2184,
    magnitude: 1.3,
    tsunami: 0,
  },
  {
    longitude: -150.4019,
    latitude: 63.1122,
    magnitude: 1,
    tsunami: 0,
  },
  {
    longitude: -70.2379,
    latitude: -31.7388,
    magnitude: 3.9,
    tsunami: 0,
  },
  {
    longitude: -115.605333,
    latitude: 32.8245,
    magnitude: 1.54,
    tsunami: 0,
  },
  {
    longitude: -111.4244,
    latitude: 42.5958,
    magnitude: 2.5,
    tsunami: 0,
  },
  {
    longitude: -119.12,
    latitude: 38.2855,
    magnitude: 1.3,
    tsunami: 0,
  },
  {
    longitude: -121.059667,
    latitude: 36.477833,
    magnitude: 1.21,
    tsunami: 0,
  },
];

const BubbleLayerSequentialLegendColor = () => {
  return (
    <MapView height={400}>
      <BubbleLayer
        data={earthquakes}
        color="legend"
        valueAccessor="magnitude"
        radius={({ magnitude }) => magnitude * 3}
        scale="none"
      />
      <SequentialLegend min={0} max={8} colorPalette="blue" />
    </MapView>
  );
};
```


##### Threshold legend

```tsx
import Colors from '@dynatrace/strato-design-tokens/colors';
import {
  BubbleLayer,
  Location,
  MapView,
  ThresholdLegend,
} from '@dynatrace/strato-geo';

type Earthquake = {
  magnitude: number;
  tsunami: number;
} & Location;

const earthquakes: Earthquake[] = [
  {
    longitude: -155.7645,
    latitude: 19.608333,
    magnitude: 1.47,
    tsunami: 0,
  },
  {
    longitude: -111.456667,
    latitude: 42.600833,
    magnitude: 1.84,
    tsunami: 0,
  },
  {
    longitude: -152.8997,
    latitude: 62.5624,
    magnitude: 1.4,
    tsunami: 0,
  },
  {
    longitude: -147.6239,
    latitude: 61.9391,
    magnitude: 2,
    tsunami: 0,
  },
  {
    longitude: -155.6845,
    latitude: 18.778833,
    magnitude: 2.06,
    tsunami: 0,
  },
  {
    longitude: -149.0205,
    latitude: 61.3011,
    magnitude: 1.7,
    tsunami: 0,
  },
  {
    longitude: -149.1141,
    latitude: 63.8125,
    magnitude: 1.6,
    tsunami: 0,
  },
  {
    longitude: -116.364,
    latitude: 33.395667,
    magnitude: 0.97,
    tsunami: 0,
  },
  {
    longitude: -118.118,
    latitude: 33.743333,
    magnitude: 1.15,
    tsunami: 0,
  },
  {
    longitude: -178.1517,
    latitude: -31.5827,
    magnitude: 5,
    tsunami: 0,
  },
  {
    longitude: -173.6834,
    latitude: 51.2465,
    magnitude: 2,
    tsunami: 0,
  },
  {
    longitude: -139.521,
    latitude: 59.9658,
    magnitude: 1.3,
    tsunami: 0,
  },
  {
    longitude: -121.7125,
    latitude: 37.351167,
    magnitude: 1.22,
    tsunami: 0,
  },
  {
    longitude: -73.1491,
    latitude: 7.5135,
    magnitude: 5.1,
    tsunami: 0,
  },
  {
    longitude: -116.354833,
    latitude: 33.961167,
    magnitude: 1.75,
    tsunami: 0,
  },
  {
    longitude: 140.5685,
    latitude: 36.9167,
    magnitude: 4.9,
    tsunami: 0,
  },
  {
    longitude: -169.8117,
    latitude: 51.8357,
    magnitude: 2.5,
    tsunami: 0,
  },
  {
    longitude: -117.119167,
    latitude: 33.9365,
    magnitude: 1,
    tsunami: 0,
  },
  {
    longitude: -153.8841,
    latitude: 57.2184,
    magnitude: 1.3,
    tsunami: 0,
  },
  {
    longitude: -150.4019,
    latitude: 63.1122,
    magnitude: 1,
    tsunami: 0,
  },
  {
    longitude: -70.2379,
    latitude: -31.7388,
    magnitude: 3.9,
    tsunami: 0,
  },
  {
    longitude: -115.605333,
    latitude: 32.8245,
    magnitude: 1.54,
    tsunami: 0,
  },
  {
    longitude: -111.4244,
    latitude: 42.5958,
    magnitude: 2.5,
    tsunami: 0,
  },
  {
    longitude: -119.12,
    latitude: 38.2855,
    magnitude: 1.3,
    tsunami: 0,
  },
  {
    longitude: -121.059667,
    latitude: 36.477833,
    magnitude: 1.21,
    tsunami: 0,
  },
];

const BubbleLayerThresholdLegendColor = () => {
  return (
    <MapView height={400}>
      <BubbleLayer
        data={earthquakes}
        color="legend"
        valueAccessor="magnitude"
        radius={({ magnitude }) => magnitude * 3}
        scale="none"
      />
      <ThresholdLegend
        ranges={[
          {
            from: 0,
            to: 1.8,
            color: Colors.Charts.Sequential.Petrol.Color09.Default,
          },
          {
            from: 1.8,
            to: 5,
            color: Colors.Charts.Sequential.Petrol.Color06.Default,
          },
          {
            from: 5,
            to: 6.5,
            color: Colors.Charts.Sequential.Petrol.Color01.Default,
          },
        ]}
      />
    </MapView>
  );
};
```

```tsx
import Colors from '@dynatrace/strato-design-tokens/colors';
import {
  BubbleLayer,
  Location,
  MapView,
  ThresholdLegend,
} from '@dynatrace/strato-geo';

type Earthquake = {
  magnitude: number;
  tsunami: number;
} & Location;

const earthquakes: Earthquake[] = [
  {
    longitude: -155.7645,
    latitude: 19.608333,
    magnitude: 1.47,
    tsunami: 0,
  },
  {
    longitude: -111.456667,
    latitude: 42.600833,
    magnitude: 1.84,
    tsunami: 0,
  },
  {
    longitude: -152.8997,
    latitude: 62.5624,
    magnitude: 1.4,
    tsunami: 0,
  },
  {
    longitude: -147.6239,
    latitude: 61.9391,
    magnitude: 2,
    tsunami: 0,
  },
  {
    longitude: -155.6845,
    latitude: 18.778833,
    magnitude: 2.06,
    tsunami: 0,
  },
  {
    longitude: -149.0205,
    latitude: 61.3011,
    magnitude: 1.7,
    tsunami: 0,
  },
  {
    longitude: -149.1141,
    latitude: 63.8125,
    magnitude: 1.6,
    tsunami: 0,
  },
  {
    longitude: -116.364,
    latitude: 33.395667,
    magnitude: 0.97,
    tsunami: 0,
  },
  {
    longitude: -118.118,
    latitude: 33.743333,
    magnitude: 1.15,
    tsunami: 0,
  },
  {
    longitude: -178.1517,
    latitude: -31.5827,
    magnitude: 5,
    tsunami: 0,
  },
  {
    longitude: -173.6834,
    latitude: 51.2465,
    magnitude: 2,
    tsunami: 0,
  },
  {
    longitude: -139.521,
    latitude: 59.9658,
    magnitude: 1.3,
    tsunami: 0,
  },
  {
    longitude: -121.7125,
    latitude: 37.351167,
    magnitude: 1.22,
    tsunami: 0,
  },
  {
    longitude: -73.1491,
    latitude: 7.5135,
    magnitude: 5.1,
    tsunami: 0,
  },
  {
    longitude: -116.354833,
    latitude: 33.961167,
    magnitude: 1.75,
    tsunami: 0,
  },
  {
    longitude: 140.5685,
    latitude: 36.9167,
    magnitude: 4.9,
    tsunami: 0,
  },
  {
    longitude: -169.8117,
    latitude: 51.8357,
    magnitude: 2.5,
    tsunami: 0,
  },
  {
    longitude: -117.119167,
    latitude: 33.9365,
    magnitude: 1,
    tsunami: 0,
  },
  {
    longitude: -153.8841,
    latitude: 57.2184,
    magnitude: 1.3,
    tsunami: 0,
  },
  {
    longitude: -150.4019,
    latitude: 63.1122,
    magnitude: 1,
    tsunami: 0,
  },
  {
    longitude: -70.2379,
    latitude: -31.7388,
    magnitude: 3.9,
    tsunami: 0,
  },
  {
    longitude: -115.605333,
    latitude: 32.8245,
    magnitude: 1.54,
    tsunami: 0,
  },
  {
    longitude: -111.4244,
    latitude: 42.5958,
    magnitude: 2.5,
    tsunami: 0,
  },
  {
    longitude: -119.12,
    latitude: 38.2855,
    magnitude: 1.3,
    tsunami: 0,
  },
  {
    longitude: -121.059667,
    latitude: 36.477833,
    magnitude: 1.21,
    tsunami: 0,
  },
];

const BubbleLayerThresholdLegendColor = () => {
  return (
    <MapView height={400}>
      <BubbleLayer
        data={earthquakes}
        color="legend"
        valueAccessor="magnitude"
        radius={({ magnitude }) => magnitude * 3}
        scale="none"
      />
      <ThresholdLegend
        ranges={[
          {
            from: 0,
            to: 1.8,
            color: Colors.Charts.Sequential.Petrol.Color09.Default,
          },
          {
            from: 1.8,
            to: 5,
            color: Colors.Charts.Sequential.Petrol.Color06.Default,
          },
          {
            from: 5,
            to: 6.5,
            color: Colors.Charts.Sequential.Petrol.Color01.Default,
          },
        ]}
      />
    </MapView>
  );
};
```


##### Categorical legend

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Size interpolation
- Scale and radius
- Tooltip
- Coloring
- Granular color configuration
- Color configuration using a legend

```tsx
import {
  BubbleLayer,
  CategoricalLegend,
  Location,
  MapView,
} from '@dynatrace/strato-geo';

type Earthquake = {
  magnitude: number;
  tsunami: number;
} & Location;

const earthquakes: Earthquake[] = [
  {
    longitude: -155.7645,
    latitude: 19.608333,
    magnitude: 1.47,
    tsunami: 0,
  },
  {
    longitude: -111.456667,
    latitude: 42.600833,
    magnitude: 1.84,
    tsunami: 0,
  },
  {
    longitude: -152.8997,
    latitude: 62.5624,
    magnitude: 1.4,
    tsunami: 0,
  },
  {
    longitude: -147.6239,
    latitude: 61.9391,
    magnitude: 2,
    tsunami: 0,
  },
  {
    longitude: -155.6845,
    latitude: 18.778833,
    magnitude: 2.06,
    tsunami: 0,
  },
  {
    longitude: -149.0205,
    latitude: 61.3011,
    magnitude: 1.7,
    tsunami: 0,
  },
  {
    longitude: -149.1141,
    latitude: 63.8125,
    magnitude: 1.6,
    tsunami: 0,
  },
  {
    longitude: -116.364,
    latitude: 33.395667,
    magnitude: 0.97,
    tsunami: 0,
  },
  {
    longitude: -118.118,
    latitude: 33.743333,
    magnitude: 1.15,
    tsunami: 0,
  },
  {
    longitude: -178.1517,
    latitude: -31.5827,
    magnitude: 5,
    tsunami: 0,
  },
  {
    longitude: -173.6834,
    latitude: 51.2465,
    magnitude: 2,
    tsunami: 0,
  },
  {
    longitude: -139.521,
    latitude: 59.9658,
    magnitude: 1.3,
    tsunami: 0,
  },
  {
    longitude: -121.7125,
    latitude: 37.351167,
    magnitude: 1.22,
    tsunami: 0,
  },
  {
    longitude: -73.1491,
    latitude: 7.5135,
    magnitude: 5.1,
    tsunami: 0,
  },
  {
    longitude: -116.354833,
    latitude: 33.961167,
    magnitude: 1.75,
    tsunami: 0,
  },
  {
    longitude: 140.5685,
    latitude: 36.9167,
    magnitude: 4.9,
    tsunami: 0,
  },
  {
    longitude: -169.8117,
    latitude: 51.8357,
    magnitude: 2.5,
    tsunami: 0,
  },
  {
    longitude: -117.119167,
    latitude: 33.9365,
    magnitude: 1,
    tsunami: 0,
  },
  {
    longitude: -153.8841,
    latitude: 57.2184,
    magnitude: 1.3,
    tsunami: 0,
  },
  {
    longitude: -150.4019,
    latitude: 63.1122,
    magnitude: 1,
    tsunami: 0,
  },
  {
    longitude: -70.2379,
    latitude: -31.7388,
    magnitude: 3.9,
    tsunami: 0,
  },
  {
    longitude: -115.605333,
    latitude: 32.8245,
    magnitude: 1.54,
    tsunami: 0,
  },
  {
    longitude: -111.4244,
    latitude: 42.5958,
    magnitude: 2.5,
    tsunami: 0,
  },
  {
    longitude: -119.12,
    latitude: 38.2855,
    magnitude: 1.3,
    tsunami: 0,
  },
  {
    longitude: -121.059667,
    latitude: 36.477833,
    magnitude: 1.21,
    tsunami: 0,
  },
];

const BubbleLayerCategoricalLegendColor = () => {
  const categories = ['Muted', 'Critical', 'High', 'Medium', 'Low'];
  const colorPalette = 'security-risk-level';

  const getStatus = (magnitude: number) =>
    categories[Math.floor(Math.random() * categories.length)];

  const categoricalData = earthquakes.map((t) => ({
    ...t,
    status: getStatus(t.magnitude),
  }));

  return (
    <MapView height={400}>
      <BubbleLayer
        data={categoricalData}
        color="legend"
        valueAccessor="status"
        radius={({ magnitude }) => magnitude * 5}
        scale="none"
      />
      <CategoricalLegend colorPalette={colorPalette} />
    </MapView>
  );
};
```

```tsx
import {
  BubbleLayer,
  CategoricalLegend,
  Location,
  MapView,
} from '@dynatrace/strato-geo';

type Earthquake = {
  magnitude: number;
  tsunami: number;
} & Location;

const earthquakes: Earthquake[] = [
  {
    longitude: -155.7645,
    latitude: 19.608333,
    magnitude: 1.47,
    tsunami: 0,
  },
  {
    longitude: -111.456667,
    latitude: 42.600833,
    magnitude: 1.84,
    tsunami: 0,
  },
  {
    longitude: -152.8997,
    latitude: 62.5624,
    magnitude: 1.4,
    tsunami: 0,
  },
  {
    longitude: -147.6239,
    latitude: 61.9391,
    magnitude: 2,
    tsunami: 0,
  },
  {
    longitude: -155.6845,
    latitude: 18.778833,
    magnitude: 2.06,
    tsunami: 0,
  },
  {
    longitude: -149.0205,
    latitude: 61.3011,
    magnitude: 1.7,
    tsunami: 0,
  },
  {
    longitude: -149.1141,
    latitude: 63.8125,
    magnitude: 1.6,
    tsunami: 0,
  },
  {
    longitude: -116.364,
    latitude: 33.395667,
    magnitude: 0.97,
    tsunami: 0,
  },
  {
    longitude: -118.118,
    latitude: 33.743333,
    magnitude: 1.15,
    tsunami: 0,
  },
  {
    longitude: -178.1517,
    latitude: -31.5827,
    magnitude: 5,
    tsunami: 0,
  },
  {
    longitude: -173.6834,
    latitude: 51.2465,
    magnitude: 2,
    tsunami: 0,
  },
  {
    longitude: -139.521,
    latitude: 59.9658,
    magnitude: 1.3,
    tsunami: 0,
  },
  {
    longitude: -121.7125,
    latitude: 37.351167,
    magnitude: 1.22,
    tsunami: 0,
  },
  {
    longitude: -73.1491,
    latitude: 7.5135,
    magnitude: 5.1,
    tsunami: 0,
  },
  {
    longitude: -116.354833,
    latitude: 33.961167,
    magnitude: 1.75,
    tsunami: 0,
  },
  {
    longitude: 140.5685,
    latitude: 36.9167,
    magnitude: 4.9,
    tsunami: 0,
  },
  {
    longitude: -169.8117,
    latitude: 51.8357,
    magnitude: 2.5,
    tsunami: 0,
  },
  {
    longitude: -117.119167,
    latitude: 33.9365,
    magnitude: 1,
    tsunami: 0,
  },
  {
    longitude: -153.8841,
    latitude: 57.2184,
    magnitude: 1.3,
    tsunami: 0,
  },
  {
    longitude: -150.4019,
    latitude: 63.1122,
    magnitude: 1,
    tsunami: 0,
  },
  {
    longitude: -70.2379,
    latitude: -31.7388,
    magnitude: 3.9,
    tsunami: 0,
  },
  {
    longitude: -115.605333,
    latitude: 32.8245,
    magnitude: 1.54,
    tsunami: 0,
  },
  {
    longitude: -111.4244,
    latitude: 42.5958,
    magnitude: 2.5,
    tsunami: 0,
  },
  {
    longitude: -119.12,
    latitude: 38.2855,
    magnitude: 1.3,
    tsunami: 0,
  },
  {
    longitude: -121.059667,
    latitude: 36.477833,
    magnitude: 1.21,
    tsunami: 0,
  },
];

const BubbleLayerCategoricalLegendColor = () => {
  const categories = ['Muted', 'Critical', 'High', 'Medium', 'Low'];
  const colorPalette = 'security-risk-level';

  const getStatus = (magnitude: number) =>
    categories[Math.floor(Math.random() * categories.length)];

  const categoricalData = earthquakes.map((t) => ({
    ...t,
    status: getStatus(t.magnitude),
  }));

  return (
    <MapView height={400}>
      <BubbleLayer
        data={categoricalData}
        color="legend"
        valueAccessor="status"
        radius={({ magnitude }) => magnitude * 5}
        scale="none"
      />
      <CategoricalLegend colorPalette={colorPalette} />
    </MapView>
  );
};
```


### Props

The `BubbleLayer` component renders data points as bubbles on a map, accepting
an array of data points with required properties like latitude and longitude. It
supports customization of bubble size using the radius prop and optional
tooltips for displaying additional information.

OverviewProperties

### BubbleLayer

#### BubbleLayerProps

##### Signature:
`export declare type BubbleLayerProps = & ( | ) & ( | );`

#### BubbleLayerBaseProps
extends |
 | Name | Type | Default | Description
 | `data` | T[] | | An array of location data items to be displayed as bubbles in the BubbleLayer
 | `sizeInterpolation?` | | | `'fixed'` | Determines the interpolation mode for bubble size.
'zoom': Bubble size changes with zoom.
'fixed': Constant bubble size regardless of zoom level.

#### LocationColorProps
 |
 | Name | Type | Default | Description
 | `color?` | | ((item: T) => ) | | Custom color to apply to the layer

#### LegendColorLayerProps
 |
 | Name | Type | Default | Description
 | `color` | | | When the color prop is set to 'legend', a value accessor is needed
 | `valueAccessor` | | | The value accessor to map data point values to legend color

#### ScaleRadiusProps
 |
 | Name | Type | Default | Description
 | `scale?` | | | `'linear'` | The way the radius is scaled.
 | `radius` | (item: T) => | | The radius property, which determines the size of the bubbles.
It requires a callback that is used as data accessor.
 | `radiusRange?` | [, ] | `[10, 100]` | It determines the min and max size for the bubble radius

#### ScaleNoneProps
 |
 | Name | Type | Default | Description
 | `scale` | | | The way to indicate that scale should not be used
 | `radius?` | | ((item: T) => ) | `12` | The radius property, which determines the size of the bubbles.
It can be a constant number or a function that calculates the radius based on the data item

#### Location
 |
 | Name | Type | Default | Description
 | `latitude` | | | The latitude coordinate of the location.
 | `longitude` | | | The longitude coordinate of the location.

### Tooltip

```tsx
import {
  BubbleLayer,
  BubbleLayerTooltipData,
  Location,
  MapView,
  Tooltip,
  TooltipAtoms,
} from '@dynatrace/strato-geo';
import { AttackIcon } from '@dynatrace/strato-icons';

type CyberAttackEvent = {
  id: string;
  distancePrecision: number;
  severity: 'high' | 'medium' | 'low';
} & Location;

const cyberAttacks: CyberAttackEvent[] = [
  {
    id: 'CYB-2024-001',
    distancePrecision: 250,
    severity: 'high',
    longitude: -115.195615,
    latitude: 36.171462,
  },
  {
    id: 'CYB-2024-002',
    distancePrecision: 500,
    severity: 'medium',
    longitude: -94.556725,
    latitude: 39.104532,
  },
  {
    id: 'CYB-2024-003',
    distancePrecision: 100,
    severity: 'low',
    longitude: -73.998772,
    latitude: 40.717575,
  },
  {
    id: 'CYB-2024-004',
    distancePrecision: 50,
    severity: 'high',
    longitude: -87.773124,
    latitude: 41.786535,
  },
  {
    id: 'CYB-2024-005',
    distancePrecision: 300,
    severity: 'low',
    longitude: -122.293741,
    latitude: 47.545032,
  },
];

const BubbleLayerTooltip = () => {
  const initialViewState = {
    longitude: -101.465989,
    latitude: 40.822381,
    zoom: 2,
  };

  return (
    <MapView height={400} initialViewState={initialViewState}>
      <BubbleLayer
        data={cyberAttacks}
        radius={(cyberAttack: CyberAttackEvent) =>
          cyberAttack.distancePrecision
        }
      >
        <BubbleLayer.Tooltip>
          {(
            closestAttack: BubbleLayerTooltipData<CyberAttackEvent>,
            cyberAttacks: BubbleLayerTooltipData<CyberAttackEvent>[]
          ) => {
            return (
              <>
                <Tooltip.Header>
                  <Tooltip.Item>
                    <Tooltip.Symbol>
                      <AttackIcon />
                    </Tooltip.Symbol>
                    <Tooltip.Content>
                      <Tooltip.Text variant="secondary">
                        {closestAttack.data.id}
                      </Tooltip.Text>
                    </Tooltip.Content>
                    <Tooltip.Value>
                      <TooltipAtoms.Chip>{`${closestAttack.data.severity} severity`}</TooltipAtoms.Chip>
                    </Tooltip.Value>
                  </Tooltip.Item>
                </Tooltip.Header>
                <Tooltip.Body
                  virtualization={false}
                  style={{ width: '95%', padding: '2px 8px' }}
                >
                  {cyberAttacks.length > 0 ? (
                    cyberAttacks.map((cyberAttack, idx) => {
                      return (
                        <Tooltip.Item
                          key={`${cyberAttack.data.id}${idx}`}
                          style={{ padding: '2px 0' }}
                        >
                          <Tooltip.Content>
                            {cyberAttack.data.id}
                          </Tooltip.Content>
                          <Tooltip.Value variant="chip">
                            {`${cyberAttack.data.severity} severity`}
                          </Tooltip.Value>
                        </Tooltip.Item>
                      );
                    })
                  ) : (
                    <Tooltip.Item style={{ padding: '2px 0' }}>
                      <Tooltip.Content>No other attacks</Tooltip.Content>
                    </Tooltip.Item>
                  )}
                </Tooltip.Body>
                <Tooltip.Footer>
                  <Tooltip.Item>
                    <Tooltip.Content>Total attacks:</Tooltip.Content>
                    <Tooltip.Value variant="chip">
                      {cyberAttacks.length + 1}
                    </Tooltip.Value>
                  </Tooltip.Item>
                </Tooltip.Footer>
              </>
            );
          }}
        </BubbleLayer.Tooltip>
      </BubbleLayer>
    </MapView>
  );
};
```

```tsx
import {
  BubbleLayer,
  BubbleLayerTooltipData,
  Location,
  MapView,
  Tooltip,
  TooltipAtoms,
} from '@dynatrace/strato-geo';
import { AttackIcon } from '@dynatrace/strato-icons';

type CyberAttackEvent = {
  id: string;
  distancePrecision: number;
  severity: 'high' | 'medium' | 'low';
} & Location;

const cyberAttacks: CyberAttackEvent[] = [
  {
    id: 'CYB-2024-001',
    distancePrecision: 250,
    severity: 'high',
    longitude: -115.195615,
    latitude: 36.171462,
  },
  {
    id: 'CYB-2024-002',
    distancePrecision: 500,
    severity: 'medium',
    longitude: -94.556725,
    latitude: 39.104532,
  },
  {
    id: 'CYB-2024-003',
    distancePrecision: 100,
    severity: 'low',
    longitude: -73.998772,
    latitude: 40.717575,
  },
  {
    id: 'CYB-2024-004',
    distancePrecision: 50,
    severity: 'high',
    longitude: -87.773124,
    latitude: 41.786535,
  },
  {
    id: 'CYB-2024-005',
    distancePrecision: 300,
    severity: 'low',
    longitude: -122.293741,
    latitude: 47.545032,
  },
];

const BubbleLayerTooltip = () => {
  const initialViewState = {
    longitude: -101.465989,
    latitude: 40.822381,
    zoom: 2,
  };

  return (
    <MapView height={400} initialViewState={initialViewState}>
      <BubbleLayer
        data={cyberAttacks}
        radius={(cyberAttack: CyberAttackEvent) =>
          cyberAttack.distancePrecision
        }
      >
        <BubbleLayer.Tooltip>
          {(
            closestAttack: BubbleLayerTooltipData<CyberAttackEvent>,
            cyberAttacks: BubbleLayerTooltipData<CyberAttackEvent>[]
          ) => {
            return (
              <>
                <Tooltip.Header>
                  <Tooltip.Item>
                    <Tooltip.Symbol>
                      <AttackIcon />
                    </Tooltip.Symbol>
                    <Tooltip.Content>
                      <Tooltip.Text variant="secondary">
                        {closestAttack.data.id}
                      </Tooltip.Text>
                    </Tooltip.Content>
                    <Tooltip.Value>
                      <TooltipAtoms.Chip>{`${closestAttack.data.severity} severity`}</TooltipAtoms.Chip>
                    </Tooltip.Value>
                  </Tooltip.Item>
                </Tooltip.Header>
                <Tooltip.Body
                  virtualization={false}
                  style={{ width: '95%', padding: '2px 8px' }}
                >
                  {cyberAttacks.length > 0 ? (
                    cyberAttacks.map((cyberAttack, idx) => {
                      return (
                        <Tooltip.Item
                          key={`${cyberAttack.data.id}${idx}`}
                          style={{ padding: '2px 0' }}
                        >
                          <Tooltip.Content>
                            {cyberAttack.data.id}
                          </Tooltip.Content>
                          <Tooltip.Value variant="chip">
                            {`${cyberAttack.data.severity} severity`}
                          </Tooltip.Value>
                        </Tooltip.Item>
                      );
                    })
                  ) : (
                    <Tooltip.Item style={{ padding: '2px 0' }}>
                      <Tooltip.Content>No other attacks</Tooltip.Content>
                    </Tooltip.Item>
                  )}
                </Tooltip.Body>
                <Tooltip.Footer>
                  <Tooltip.Item>
                    <Tooltip.Content>Total attacks:</Tooltip.Content>
                    <Tooltip.Value variant="chip">
                      {cyberAttacks.length + 1}
                    </Tooltip.Value>
                  </Tooltip.Item>
                </Tooltip.Footer>
              </>
            );
          }}
        </BubbleLayer.Tooltip>
      </BubbleLayer>
    </MapView>
  );
};
```


#### BubbleLayerTooltipData
 |
 | Name | Type | Default | Description
 | `color` | | | The hovered bubble color
 | `radius` | | | The hovered bubble radius
 | `data` | T | | The hovered bubble custom data and location

#### BubbleLayerTooltipHandler

##### Signature:
`export declare type BubbleLayerTooltipHandler = (closestDot: , dotsData: []) => | ;`

#### BubbleLayerTooltipHandlerProps
 |
 | Name | Type | Default | Description
 | `children?` | | | | The BubbleLayer tooltip handler template
 | `seriesActions?` | (location: ) => | | Series actions callback for the default tooltipStill have questions?Find answers in the Dynatrace Community
- Tooltip

---

## ChoroplethLayer

`/design/data-visualizations/geo-maps/ChoroplethLayer/`

The `ChoroplethLayer` component allows users to display divided geographical
areas or regions that are coloured in relation to a given data. It provides an
easy way to visualize how a variable varies across a geographic area or show the
level of variability within a region.

OverviewProperties

### Import

`tsx
import { ChoroplethLayer } from '@dynatrace/strato-geo';
`

### Use cases

Use the `ChoroplethLayer` subcomponent to apply color to a specific region. The
`ChoroplethLayer` subcomponent accepts an array of data entries as the `data`
prop. Each entry must contain an ISO 3166-2 region code.

You can use the `regionAccessor` prop to access the region where the color needs
to be applied. This can be either a string in the form of a value accessor or a
callback to dynamically construct the region code.

`tsx
[ { country: 'DE', color: '#f7c910', population: 84724070, }, { country: 'AU', color: '#012066', population: 26473055, }, { country: 'BR', color: '#029639', population: 218689752, },];
`

Learn more about the data format here.

```tsx
import { ChoroplethLayer, MapView } from '@dynatrace/strato-geo';

const countriesStats = [
  {
    country: 'DE',
    primary_color: '#f7c910',
    population: 84724070,
    continent: 'Europe',
    apdex: 'Excellent',
  },
  {
    country: 'AU',
    primary_color: '#012066',
    population: 26473055,
    continent: 'Oceania',
    apdex: 'Excellent',
  },
  {
    country: 'BR',
    primary_color: '#029639',
    population: 218689752,
    continent: 'South America',
    apdex: 'Unacceptable',
  },
  {
    country: 'ES',
    primary_color: '#c70219',
    population: 48196693,
    continent: 'Europe',
    apdex: 'Fair',
  },
  {
    country: 'MX',
    primary_color: '#006e49',
    population: 131135337,
    continent: 'North America',
    apdex: 'Unacceptable',
  },
  {
    country: 'CA',
    primary_color: '#d62618',
    population: 38037204,
    continent: 'North America',
    apdex: 'Excellent',
  },
  {
    country: 'AR',
    primary_color: '#6CACE4',
    population: 47327407,
    continent: 'South America',
    apdex: 'Good',
  },
  {
    country: 'VE',
    primary_color: '#FCE300',
    population: 28515829,
    continent: 'South America',
    apdex: 'Excellent',
  },
  {
    country: 'CU',
    primary_color: '#002a90',
    population: 10985974,
    continent: 'North America',
    apdex: 'Good',
  },
  {
    country: 'PR',
    primary_color: '#ee0200',
    population: 3285874,
    continent: 'North America',
    apdex: 'Excellent',
  },
  {
    country: 'UA',
    primary_color: '#0057B7',
    population: 41732779,
    continent: 'Europe',
    apdex: 'Fair',
  },
  {
    country: 'IT',
    primary_color: '#028e44',
    population: 59346717,
    continent: 'Europe',
    apdex: 'Poor',
  },
];

const ChoroplethLayerSimple = () => {
  return (
    <MapView height={400} initialViewState={{ zoom: 1 }}>
      <ChoroplethLayer data={countriesStats} regionAccessor="country" />
    </MapView>
  );
};
```

```tsx
import { ChoroplethLayer, MapView } from '@dynatrace/strato-geo';

const countriesStats = [
  {
    country: 'DE',
    primary_color: '#f7c910',
    population: 84724070,
    continent: 'Europe',
    apdex: 'Excellent',
  },
  {
    country: 'AU',
    primary_color: '#012066',
    population: 26473055,
    continent: 'Oceania',
    apdex: 'Excellent',
  },
  {
    country: 'BR',
    primary_color: '#029639',
    population: 218689752,
    continent: 'South America',
    apdex: 'Unacceptable',
  },
  {
    country: 'ES',
    primary_color: '#c70219',
    population: 48196693,
    continent: 'Europe',
    apdex: 'Fair',
  },
  {
    country: 'MX',
    primary_color: '#006e49',
    population: 131135337,
    continent: 'North America',
    apdex: 'Unacceptable',
  },
  {
    country: 'CA',
    primary_color: '#d62618',
    population: 38037204,
    continent: 'North America',
    apdex: 'Excellent',
  },
  {
    country: 'AR',
    primary_color: '#6CACE4',
    population: 47327407,
    continent: 'South America',
    apdex: 'Good',
  },
  {
    country: 'VE',
    primary_color: '#FCE300',
    population: 28515829,
    continent: 'South America',
    apdex: 'Excellent',
  },
  {
    country: 'CU',
    primary_color: '#002a90',
    population: 10985974,
    continent: 'North America',
    apdex: 'Good',
  },
  {
    country: 'PR',
    primary_color: '#ee0200',
    population: 3285874,
    continent: 'North America',
    apdex: 'Excellent',
  },
  {
    country: 'UA',
    primary_color: '#0057B7',
    population: 41732779,
    continent: 'Europe',
    apdex: 'Fair',
  },
  {
    country: 'IT',
    primary_color: '#028e44',
    population: 59346717,
    continent: 'Europe',
    apdex: 'Poor',
  },
];

const ChoroplethLayerSimple = () => {
  return (
    <MapView height={400} initialViewState={{ zoom: 1 }}>
      <ChoroplethLayer data={countriesStats} regionAccessor="country" />
    </MapView>
  );
};
```


#### Tooltip

Finally, when hovering a region in the `ChoroplethLayer`, the tooltip will
output the region `name`, the `color` and all the additional custom props inside
a `data` object.

```tsx
import Colors from '@dynatrace/strato-design-tokens/colors';
import {
  ChoroplethLayer,
  ChoroplethLayerTooltipData,
  MapView,
  Tooltip,
  TooltipAtoms,
} from '@dynatrace/strato-geo';

type CountryStats = {
  country: string;
  primary_color: string;
  population: number;
  continent: string;
  apdex: string;
  status: string;
};

const countriesStats: CountryStats[] = [
  {
    country: 'DE',
    primary_color: '#f7c910',
    population: 84_724_070,
    continent: 'Europe',
    apdex: 'Excellent',
    status: 'muted',
  },
  {
    country: 'AU',
    primary_color: '#012066',
    population: 26_473_055,
    continent: 'Oceania',
    apdex: 'Excellent',
    status: 'affected',
  },
  {
    country: 'BR',
    primary_color: '#029639',
    population: 218_689_752,
    continent: 'South America',
    apdex: 'Unacceptable',
    status: 'muted',
  },
  {
    country: 'ES',
    primary_color: '#c70219',
    population: 48_196_693,
    continent: 'Europe',
    apdex: 'Fair',
    status: 'resolved',
  },
  {
    country: 'MX',
    primary_color: '#006e49',
    population: 131_135_337,
    continent: 'North America',
    apdex: 'Unacceptable',
    status: 'muted',
  },

  {
    country: 'CA',
    primary_color: '#d62618',
    population: 38_037_204,
    continent: 'North America',
    apdex: 'Excellent',
    status: 'muted',
  },
  {
    country: 'AR',
    primary_color: '#6CACE4',
    population: 47_327_407,
    continent: 'South America',
    apdex: 'Good',
    status: 'muted',
  },
  {
    country: 'VE',
    primary_color: '#FCE300',
    population: 28_515_829,
    continent: 'South America',
    apdex: 'Excellent',
    status: 'affected',
  },
  {
    country: 'CU',
    primary_color: '#002a90',
    population: 10_985_974,
    continent: 'North America',
    apdex: 'Good',
    status: 'resolved',
  },
  {
    country: 'PR',
    primary_color: '#ee0200',
    population: 3_285_874,
    continent: 'North America',
    apdex: 'Excellent',
    status: 'muted',
  },
  {
    country: 'UA',
    primary_color: '#0057B7',
    population: 41_732_779,
    continent: 'Europe',
    apdex: 'Fair',
    status: 'resolved',
  },
  {
    country: 'IT',
    primary_color: '#028e44',
    population: 59_346_717,
    continent: 'Europe',
    apdex: 'Poor',
    status: 'affected',
  },
];

const ChoroplethLayerTooltip = () => {
  return (
    <MapView height={400} initialViewState={{ zoom: 1 }}>
      <ChoroplethLayer
        data={countriesStats}
        regionAccessor="country"
        color={Colors.Charts.Sequential.Pink.Color05.Default}
      >
        <ChoroplethLayer.Tooltip>
          {(regionData: ChoroplethLayerTooltipData<CountryStats>) => {
            const { name, color, data } = regionData;

            const { apdex } = data;

            return (
              <Tooltip.Body>
                <Tooltip.Item>
                  <Tooltip.Symbol>
                    <TooltipAtoms.SingleDataPoint color={color} />
                  </Tooltip.Symbol>
                  <Tooltip.Content>
                    <Tooltip.Text variant="secondary">{name}</Tooltip.Text>
                  </Tooltip.Content>
                  <Tooltip.Value>
                    <TooltipAtoms.Chip>{apdex}</TooltipAtoms.Chip>
                  </Tooltip.Value>
                </Tooltip.Item>
              </Tooltip.Body>
            );
          }}
        </ChoroplethLayer.Tooltip>
      </ChoroplethLayer>
    </MapView>
  );
};
```

```tsx
import Colors from '@dynatrace/strato-design-tokens/colors';
import {
  ChoroplethLayer,
  ChoroplethLayerTooltipData,
  MapView,
  Tooltip,
  TooltipAtoms,
} from '@dynatrace/strato-geo';

type CountryStats = {
  country: string;
  primary_color: string;
  population: number;
  continent: string;
  apdex: string;
  status: string;
};

const countriesStats: CountryStats[] = [
  {
    country: 'DE',
    primary_color: '#f7c910',
    population: 84_724_070,
    continent: 'Europe',
    apdex: 'Excellent',
    status: 'muted',
  },
  {
    country: 'AU',
    primary_color: '#012066',
    population: 26_473_055,
    continent: 'Oceania',
    apdex: 'Excellent',
    status: 'affected',
  },
  {
    country: 'BR',
    primary_color: '#029639',
    population: 218_689_752,
    continent: 'South America',
    apdex: 'Unacceptable',
    status: 'muted',
  },
  {
    country: 'ES',
    primary_color: '#c70219',
    population: 48_196_693,
    continent: 'Europe',
    apdex: 'Fair',
    status: 'resolved',
  },
  {
    country: 'MX',
    primary_color: '#006e49',
    population: 131_135_337,
    continent: 'North America',
    apdex: 'Unacceptable',
    status: 'muted',
  },

  {
    country: 'CA',
    primary_color: '#d62618',
    population: 38_037_204,
    continent: 'North America',
    apdex: 'Excellent',
    status: 'muted',
  },
  {
    country: 'AR',
    primary_color: '#6CACE4',
    population: 47_327_407,
    continent: 'South America',
    apdex: 'Good',
    status: 'muted',
  },
  {
    country: 'VE',
    primary_color: '#FCE300',
    population: 28_515_829,
    continent: 'South America',
    apdex: 'Excellent',
    status: 'affected',
  },
  {
    country: 'CU',
    primary_color: '#002a90',
    population: 10_985_974,
    continent: 'North America',
    apdex: 'Good',
    status: 'resolved',
  },
  {
    country: 'PR',
    primary_color: '#ee0200',
    population: 3_285_874,
    continent: 'North America',
    apdex: 'Excellent',
    status: 'muted',
  },
  {
    country: 'UA',
    primary_color: '#0057B7',
    population: 41_732_779,
    continent: 'Europe',
    apdex: 'Fair',
    status: 'resolved',
  },
  {
    country: 'IT',
    primary_color: '#028e44',
    population: 59_346_717,
    continent: 'Europe',
    apdex: 'Poor',
    status: 'affected',
  },
];

const ChoroplethLayerTooltip = () => {
  return (
    <MapView height={400} initialViewState={{ zoom: 1 }}>
      <ChoroplethLayer
        data={countriesStats}
        regionAccessor="country"
        color={Colors.Charts.Sequential.Pink.Color05.Default}
      >
        <ChoroplethLayer.Tooltip>
          {(regionData: ChoroplethLayerTooltipData<CountryStats>) => {
            const { name, color, data } = regionData;

            const { apdex } = data;

            return (
              <Tooltip.Body>
                <Tooltip.Item>
                  <Tooltip.Symbol>
                    <TooltipAtoms.SingleDataPoint color={color} />
                  </Tooltip.Symbol>
                  <Tooltip.Content>
                    <Tooltip.Text variant="secondary">{name}</Tooltip.Text>
                  </Tooltip.Content>
                  <Tooltip.Value>
                    <TooltipAtoms.Chip>{apdex}</TooltipAtoms.Chip>
                  </Tooltip.Value>
                </Tooltip.Item>
              </Tooltip.Body>
            );
          }}
        </ChoroplethLayer.Tooltip>
      </ChoroplethLayer>
    </MapView>
  );
};
```


#### Coloring

The `ChoroplethLayer` supports two ways of color configuration: granular
configuration using the `color` prop, or using a one of the available legend
subcomponents (e.g. `SequentialLegend`, `ThresholdLegend`, or
`CategoricalLegend`).

Note: Detailed information about coloring can be found in the `MapView`
documentation page under the `Coloring` section.

##### Granular color configuration

For a granular color customization, layer's `color` prop should be used.

###### Custom color applied on singular country state

This type of display can be done by providing country/state array for `include`
and `exclude` props in `BaseLayer` component

```tsx
import { ChoroplethLayer, MapView } from '@dynatrace/strato-geo';

const countriesStats = [
  {
    country: 'DE',
    primary_color: '#f7c910',
    population: 84_724_070,
    continent: 'Europe',
    apdex: 'Excellent',
  },
  {
    country: 'AU',
    primary_color: '#012066',
    population: 26_473_055,
    continent: 'Oceania',
    apdex: 'Excellent',
  },
  {
    country: 'BR',
    primary_color: '#029639',
    population: 218_689_752,
    continent: 'South America',
    apdex: 'Unacceptable',
  },
  {
    country: 'ES',
    primary_color: '#c70219',
    population: 48_196_693,
    continent: 'Europe',
    apdex: 'Fair',
  },
  {
    country: 'MX',
    primary_color: '#006e49',
    population: 131_135_337,
    continent: 'North America',
    apdex: 'Unacceptable',
  },
  {
    country: 'CA',
    primary_color: '#d62618',
    population: 38_037_204,
    continent: 'North America',
    apdex: 'Excellent',
  },
  {
    country: 'AR',
    primary_color: '#6CACE4',
    population: 47_327_407,
    continent: 'South America',
    apdex: 'Good',
  },
  {
    country: 'VE',
    primary_color: '#FCE300',
    population: 28_515_829,
    continent: 'South America',
    apdex: 'Excellent',
  },
  {
    country: 'CU',
    primary_color: '#002a90',
    population: 10_985_974,
    continent: 'North America',
    apdex: 'Good',
  },
  {
    country: 'PR',
    primary_color: '#ee0200',
    population: 3_285_874,
    continent: 'North America',
    apdex: 'Excellent',
  },
  {
    country: 'UA',
    primary_color: '#0057B7',
    population: 41_732_779,
    continent: 'Europe',
    apdex: 'Fair',
  },
  {
    country: 'IT',
    primary_color: '#028e44',
    population: 59_346_717,
    continent: 'Europe',
    apdex: 'Poor',
  },
];

const ChoroplethLayerCustomColor = () => {
  return (
    <MapView height={400} initialViewState={{ zoom: 1 }}>
      <ChoroplethLayer
        data={countriesStats}
        regionAccessor="country"
        color={(item) => item.primary_color}
      />
    </MapView>
  );
};
```

```tsx
import { ChoroplethLayer, MapView } from '@dynatrace/strato-geo';

const countriesStats = [
  {
    country: 'DE',
    primary_color: '#f7c910',
    population: 84_724_070,
    continent: 'Europe',
    apdex: 'Excellent',
  },
  {
    country: 'AU',
    primary_color: '#012066',
    population: 26_473_055,
    continent: 'Oceania',
    apdex: 'Excellent',
  },
  {
    country: 'BR',
    primary_color: '#029639',
    population: 218_689_752,
    continent: 'South America',
    apdex: 'Unacceptable',
  },
  {
    country: 'ES',
    primary_color: '#c70219',
    population: 48_196_693,
    continent: 'Europe',
    apdex: 'Fair',
  },
  {
    country: 'MX',
    primary_color: '#006e49',
    population: 131_135_337,
    continent: 'North America',
    apdex: 'Unacceptable',
  },
  {
    country: 'CA',
    primary_color: '#d62618',
    population: 38_037_204,
    continent: 'North America',
    apdex: 'Excellent',
  },
  {
    country: 'AR',
    primary_color: '#6CACE4',
    population: 47_327_407,
    continent: 'South America',
    apdex: 'Good',
  },
  {
    country: 'VE',
    primary_color: '#FCE300',
    population: 28_515_829,
    continent: 'South America',
    apdex: 'Excellent',
  },
  {
    country: 'CU',
    primary_color: '#002a90',
    population: 10_985_974,
    continent: 'North America',
    apdex: 'Good',
  },
  {
    country: 'PR',
    primary_color: '#ee0200',
    population: 3_285_874,
    continent: 'North America',
    apdex: 'Excellent',
  },
  {
    country: 'UA',
    primary_color: '#0057B7',
    population: 41_732_779,
    continent: 'Europe',
    apdex: 'Fair',
  },
  {
    country: 'IT',
    primary_color: '#028e44',
    population: 59_346_717,
    continent: 'Europe',
    apdex: 'Poor',
  },
];

const ChoroplethLayerCustomColor = () => {
  return (
    <MapView height={400} initialViewState={{ zoom: 1 }}>
      <ChoroplethLayer
        data={countriesStats}
        regionAccessor="country"
        color={(item) => item.primary_color}
      />
    </MapView>
  );
};
```


##### Coloring countries and regions

```tsx
import {
  BaseLayer,
  ChoroplethLayer,
  MapView,
  Tooltip,
  TooltipAtoms,
  ChoroplethLayerTooltipData,
} from '@dynatrace/strato-geo';

type CountryStats = {
  country: string;
  primary_color: string;
  population: number;
  continent: string;
  apdex: string;
  status: string;
};

const countriesStats = [
  {
    country: 'US-AB',
    primary_color: '#0033A0',
    population: 4_371_316,
    continent: 'North America',
    apdex: 'Good',
  },
  {
    country: 'US-MT',
    primary_color: '#003366',
    population: 1_084_225,
    continent: 'North America',
    apdex: 'Good',
  },
  {
    country: 'US-NE',
    primary_color: '#0033A0',
    population: 1_963_333,
    continent: 'North America',
    apdex: 'Good',
  },
  {
    country: 'BR-RJ',
    primary_color: '#0033A0',
    population: 17_463_349,
    continent: 'South America',
    apdex: 'Excellent',
  },
  {
    country: 'BR-MT',
    primary_color: '#028E44',
    population: 3_526_220,
    continent: 'South America',
    apdex: 'Good',
  },
  {
    country: 'BR-AM',
    primary_color: '#028E44',
    population: 4_269_995,
    continent: 'South America',
    apdex: 'Good',
  },
  {
    country: 'CA-NT',
    primary_color: '#002868',
    population: 45_605,
    continent: 'North America',
    apdex: 'Fair',
  },
  {
    country: 'CA-AB',
    primary_color: '#0033A0',
    population: 4_371_316,
    continent: 'North America',
    apdex: 'Good',
  },
  {
    country: 'AR',
    primary_color: '#75AADB',
    population: 45_376_763,
    continent: 'South America',
    apdex: 'Excellent',
  },
  {
    country: 'PT',
    primary_color: '#006600',
    population: 10_276_617,
    continent: 'Europe',
    apdex: 'Good',
  },
  {
    country: 'ES-CT',
    primary_color: '#FFCC00',
    population: 7_661_950,
    continent: 'Europe',
    apdex: 'Good',
  },
  {
    country: 'ES-MD',
    primary_color: '#B22222',
    population: 6_746_011,
    continent: 'Europe',
    apdex: 'Good',
  },
  {
    country: 'ES-PV',
    primary_color: '#006847',
    population: 2_199_711,
    continent: 'Europe',
    apdex: 'Good',
  },
  {
    country: 'ES-AN',
    primary_color: '#006847',
    population: 8_472_407,
    continent: 'Europe',
    apdex: 'Good',
  },
  {
    country: 'MX',
    primary_color: '#006847',
    population: 126_705_138,
    continent: 'North America',
    apdex: 'Good',
  },
];

const BaseLayerRegionsColored = () => {
  return (
    <MapView height={400} initialViewState={{ zoom: 1 }}>
      <ChoroplethLayer
        data={countriesStats}
        regionAccessor="country"
        color={(item) => item.primary_color}
      >
        <ChoroplethLayer.Tooltip>
          {(regionData: ChoroplethLayerTooltipData<CountryStats>) => {
            const { name, color, data } = regionData;

            const { apdex } = data;

            return (
              <Tooltip.Body>
                <Tooltip.Item>
                  <Tooltip.Symbol>
                    <TooltipAtoms.SingleDataPoint color={color} />
                  </Tooltip.Symbol>
                  <Tooltip.Content>
                    <Tooltip.Text variant="secondary">{name}</Tooltip.Text>
                  </Tooltip.Content>
                  <Tooltip.Value>
                    <TooltipAtoms.Chip>{apdex}</TooltipAtoms.Chip>
                  </Tooltip.Value>
                </Tooltip.Item>
              </Tooltip.Body>
            );
          }}
        </ChoroplethLayer.Tooltip>
      </ChoroplethLayer>
      <BaseLayer include={['*', 'US-*', 'BR-*', 'CA-*', 'ES-*']}></BaseLayer>
    </MapView>
  );
};
```

```tsx
import {
  BaseLayer,
  ChoroplethLayer,
  MapView,
  Tooltip,
  TooltipAtoms,
  ChoroplethLayerTooltipData,
} from '@dynatrace/strato-geo';

type CountryStats = {
  country: string;
  primary_color: string;
  population: number;
  continent: string;
  apdex: string;
  status: string;
};

const countriesStats = [
  {
    country: 'US-AB',
    primary_color: '#0033A0',
    population: 4_371_316,
    continent: 'North America',
    apdex: 'Good',
  },
  {
    country: 'US-MT',
    primary_color: '#003366',
    population: 1_084_225,
    continent: 'North America',
    apdex: 'Good',
  },
  {
    country: 'US-NE',
    primary_color: '#0033A0',
    population: 1_963_333,
    continent: 'North America',
    apdex: 'Good',
  },
  {
    country: 'BR-RJ',
    primary_color: '#0033A0',
    population: 17_463_349,
    continent: 'South America',
    apdex: 'Excellent',
  },
  {
    country: 'BR-MT',
    primary_color: '#028E44',
    population: 3_526_220,
    continent: 'South America',
    apdex: 'Good',
  },
  {
    country: 'BR-AM',
    primary_color: '#028E44',
    population: 4_269_995,
    continent: 'South America',
    apdex: 'Good',
  },
  {
    country: 'CA-NT',
    primary_color: '#002868',
    population: 45_605,
    continent: 'North America',
    apdex: 'Fair',
  },
  {
    country: 'CA-AB',
    primary_color: '#0033A0',
    population: 4_371_316,
    continent: 'North America',
    apdex: 'Good',
  },
  {
    country: 'AR',
    primary_color: '#75AADB',
    population: 45_376_763,
    continent: 'South America',
    apdex: 'Excellent',
  },
  {
    country: 'PT',
    primary_color: '#006600',
    population: 10_276_617,
    continent: 'Europe',
    apdex: 'Good',
  },
  {
    country: 'ES-CT',
    primary_color: '#FFCC00',
    population: 7_661_950,
    continent: 'Europe',
    apdex: 'Good',
  },
  {
    country: 'ES-MD',
    primary_color: '#B22222',
    population: 6_746_011,
    continent: 'Europe',
    apdex: 'Good',
  },
  {
    country: 'ES-PV',
    primary_color: '#006847',
    population: 2_199_711,
    continent: 'Europe',
    apdex: 'Good',
  },
  {
    country: 'ES-AN',
    primary_color: '#006847',
    population: 8_472_407,
    continent: 'Europe',
    apdex: 'Good',
  },
  {
    country: 'MX',
    primary_color: '#006847',
    population: 126_705_138,
    continent: 'North America',
    apdex: 'Good',
  },
];

const BaseLayerRegionsColored = () => {
  return (
    <MapView height={400} initialViewState={{ zoom: 1 }}>
      <ChoroplethLayer
        data={countriesStats}
        regionAccessor="country"
        color={(item) => item.primary_color}
      >
        <ChoroplethLayer.Tooltip>
          {(regionData: ChoroplethLayerTooltipData<CountryStats>) => {
            const { name, color, data } = regionData;

            const { apdex } = data;

            return (
              <Tooltip.Body>
                <Tooltip.Item>
                  <Tooltip.Symbol>
                    <TooltipAtoms.SingleDataPoint color={color} />
                  </Tooltip.Symbol>
                  <Tooltip.Content>
                    <Tooltip.Text variant="secondary">{name}</Tooltip.Text>
                  </Tooltip.Content>
                  <Tooltip.Value>
                    <TooltipAtoms.Chip>{apdex}</TooltipAtoms.Chip>
                  </Tooltip.Value>
                </Tooltip.Item>
              </Tooltip.Body>
            );
          }}
        </ChoroplethLayer.Tooltip>
      </ChoroplethLayer>
      <BaseLayer include={['*', 'US-*', 'BR-*', 'CA-*', 'ES-*']}></BaseLayer>
    </MapView>
  );
};
```


##### Color configuration using a legend

To connect a data layer to the legend, a `color` property of the layer should be
set to `legend` string.

###### Sequential legend

###### Threshold legend

###### Categorical legend

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Tooltip
- Coloring

```tsx
import {
  ChoroplethLayer,
  MapView,
  SequentialLegend,
} from '@dynatrace/strato-geo';

const countriesStats = [
  {
    country: 'DE',
    primary_color: '#f7c910',
    population: 84724070,
    continent: 'Europe',
    apdex: 'Excellent',
  },
  {
    country: 'AU',
    primary_color: '#012066',
    population: 26473055,
    continent: 'Oceania',
    apdex: 'Excellent',
  },
  {
    country: 'BR',
    primary_color: '#029639',
    population: 218689752,
    continent: 'South America',
    apdex: 'Unacceptable',
  },
  {
    country: 'ES',
    primary_color: '#c70219',
    population: 48196693,
    continent: 'Europe',
    apdex: 'Fair',
  },
  {
    country: 'MX',
    primary_color: '#006e49',
    population: 131135337,
    continent: 'North America',
    apdex: 'Unacceptable',
  },
  {
    country: 'CA',
    primary_color: '#d62618',
    population: 38037204,
    continent: 'North America',
    apdex: 'Excellent',
  },
  {
    country: 'AR',
    primary_color: '#6CACE4',
    population: 47327407,
    continent: 'South America',
    apdex: 'Good',
  },
  {
    country: 'VE',
    primary_color: '#FCE300',
    population: 28515829,
    continent: 'South America',
    apdex: 'Excellent',
  },
  {
    country: 'CU',
    primary_color: '#002a90',
    population: 10985974,
    continent: 'North America',
    apdex: 'Good',
  },
  {
    country: 'PR',
    primary_color: '#ee0200',
    population: 3285874,
    continent: 'North America',
    apdex: 'Excellent',
  },
  {
    country: 'UA',
    primary_color: '#0057B7',
    population: 41732779,
    continent: 'Europe',
    apdex: 'Fair',
  },
  {
    country: 'IT',
    primary_color: '#028e44',
    population: 59346717,
    continent: 'Europe',
    apdex: 'Poor',
  },
];

const ChoroplethLayerSequentialLegendColor = () => {
  return (
    <MapView height={400} initialViewState={{ zoom: 1 }}>
      <ChoroplethLayer
        data={countriesStats}
        regionAccessor="country"
        valueAccessor="population"
        color="legend"
      ></ChoroplethLayer>
      <SequentialLegend
        min={10_000_000}
        max={220_000_000}
        colorPalette="magenta"
      />
    </MapView>
  );
};
```

```tsx
import {
  ChoroplethLayer,
  MapView,
  SequentialLegend,
} from '@dynatrace/strato-geo';

const countriesStats = [
  {
    country: 'DE',
    primary_color: '#f7c910',
    population: 84724070,
    continent: 'Europe',
    apdex: 'Excellent',
  },
  {
    country: 'AU',
    primary_color: '#012066',
    population: 26473055,
    continent: 'Oceania',
    apdex: 'Excellent',
  },
  {
    country: 'BR',
    primary_color: '#029639',
    population: 218689752,
    continent: 'South America',
    apdex: 'Unacceptable',
  },
  {
    country: 'ES',
    primary_color: '#c70219',
    population: 48196693,
    continent: 'Europe',
    apdex: 'Fair',
  },
  {
    country: 'MX',
    primary_color: '#006e49',
    population: 131135337,
    continent: 'North America',
    apdex: 'Unacceptable',
  },
  {
    country: 'CA',
    primary_color: '#d62618',
    population: 38037204,
    continent: 'North America',
    apdex: 'Excellent',
  },
  {
    country: 'AR',
    primary_color: '#6CACE4',
    population: 47327407,
    continent: 'South America',
    apdex: 'Good',
  },
  {
    country: 'VE',
    primary_color: '#FCE300',
    population: 28515829,
    continent: 'South America',
    apdex: 'Excellent',
  },
  {
    country: 'CU',
    primary_color: '#002a90',
    population: 10985974,
    continent: 'North America',
    apdex: 'Good',
  },
  {
    country: 'PR',
    primary_color: '#ee0200',
    population: 3285874,
    continent: 'North America',
    apdex: 'Excellent',
  },
  {
    country: 'UA',
    primary_color: '#0057B7',
    population: 41732779,
    continent: 'Europe',
    apdex: 'Fair',
  },
  {
    country: 'IT',
    primary_color: '#028e44',
    population: 59346717,
    continent: 'Europe',
    apdex: 'Poor',
  },
];

const ChoroplethLayerSequentialLegendColor = () => {
  return (
    <MapView height={400} initialViewState={{ zoom: 1 }}>
      <ChoroplethLayer
        data={countriesStats}
        regionAccessor="country"
        valueAccessor="population"
        color="legend"
      ></ChoroplethLayer>
      <SequentialLegend
        min={10_000_000}
        max={220_000_000}
        colorPalette="magenta"
      />
    </MapView>
  );
};
```


### Props

The `ChoroplethLayer` component allows users to display divided geographical
areas or regions that are coloured in relation to a given data. It provides an
easy way to visualize how a variable varies across a geographic area or show the
level of variability within a region.

OverviewProperties

### ChoroplethLayer

#### ChoroplethLayerProps

##### Signature:
`export declare type ChoroplethLayerProps> = & ( | );`

#### ChoroplethLayerBaseProps
extends |
 | Name | Type | Default | Description
 | `data` | T[] | | An array of data items representing regions to be displayed in the ChoroplethLayer
 | `regionAccessor` | | ((t: T) => ) | | A string property or accessor function that specifies how to access the region identifier from the data items.
It can be a string representing the key in the data object or a function that extracts the region identifier

#### ChoroplethCustomColorProps
 |
 | Name | Type | Default | Description
 | `color?` | | ((item: T) => ) | | Color to apply to the layer

#### LegendColorLayerProps
 |
 | Name | Type | Default | Description
 | `color` | | | When the color prop is set to 'legend', a value accessor is needed
 | `valueAccessor` | | | The value accessor to map data point values to legend color

### Tooltip

```tsx
import Colors from '@dynatrace/strato-design-tokens/colors';
import {
  ChoroplethLayer,
  ChoroplethLayerTooltipData,
  MapView,
  Tooltip,
  TooltipAtoms,
} from '@dynatrace/strato-geo';

type CountryStats = {
  country: string;
  primary_color: string;
  population: number;
  continent: string;
  apdex: string;
  status: string;
};

const countriesStats: CountryStats[] = [
  {
    country: 'DE',
    primary_color: '#f7c910',
    population: 84_724_070,
    continent: 'Europe',
    apdex: 'Excellent',
    status: 'muted',
  },
  {
    country: 'AU',
    primary_color: '#012066',
    population: 26_473_055,
    continent: 'Oceania',
    apdex: 'Excellent',
    status: 'affected',
  },
  {
    country: 'BR',
    primary_color: '#029639',
    population: 218_689_752,
    continent: 'South America',
    apdex: 'Unacceptable',
    status: 'muted',
  },
  {
    country: 'ES',
    primary_color: '#c70219',
    population: 48_196_693,
    continent: 'Europe',
    apdex: 'Fair',
    status: 'resolved',
  },
  {
    country: 'MX',
    primary_color: '#006e49',
    population: 131_135_337,
    continent: 'North America',
    apdex: 'Unacceptable',
    status: 'muted',
  },

  {
    country: 'CA',
    primary_color: '#d62618',
    population: 38_037_204,
    continent: 'North America',
    apdex: 'Excellent',
    status: 'muted',
  },
  {
    country: 'AR',
    primary_color: '#6CACE4',
    population: 47_327_407,
    continent: 'South America',
    apdex: 'Good',
    status: 'muted',
  },
  {
    country: 'VE',
    primary_color: '#FCE300',
    population: 28_515_829,
    continent: 'South America',
    apdex: 'Excellent',
    status: 'affected',
  },
  {
    country: 'CU',
    primary_color: '#002a90',
    population: 10_985_974,
    continent: 'North America',
    apdex: 'Good',
    status: 'resolved',
  },
  {
    country: 'PR',
    primary_color: '#ee0200',
    population: 3_285_874,
    continent: 'North America',
    apdex: 'Excellent',
    status: 'muted',
  },
  {
    country: 'UA',
    primary_color: '#0057B7',
    population: 41_732_779,
    continent: 'Europe',
    apdex: 'Fair',
    status: 'resolved',
  },
  {
    country: 'IT',
    primary_color: '#028e44',
    population: 59_346_717,
    continent: 'Europe',
    apdex: 'Poor',
    status: 'affected',
  },
];

const ChoroplethLayerTooltip = () => {
  return (
    <MapView height={400} initialViewState={{ zoom: 1 }}>
      <ChoroplethLayer
        data={countriesStats}
        regionAccessor="country"
        color={Colors.Charts.Sequential.Pink.Color05.Default}
      >
        <ChoroplethLayer.Tooltip>
          {(regionData: ChoroplethLayerTooltipData<CountryStats>) => {
            const { name, color, data } = regionData;

            const { apdex } = data;

            return (
              <Tooltip.Body>
                <Tooltip.Item>
                  <Tooltip.Symbol>
                    <TooltipAtoms.SingleDataPoint color={color} />
                  </Tooltip.Symbol>
                  <Tooltip.Content>
                    <Tooltip.Text variant="secondary">{name}</Tooltip.Text>
                  </Tooltip.Content>
                  <Tooltip.Value>
                    <TooltipAtoms.Chip>{apdex}</TooltipAtoms.Chip>
                  </Tooltip.Value>
                </Tooltip.Item>
              </Tooltip.Body>
            );
          }}
        </ChoroplethLayer.Tooltip>
      </ChoroplethLayer>
    </MapView>
  );
};
```

```tsx
import Colors from '@dynatrace/strato-design-tokens/colors';
import {
  ChoroplethLayer,
  ChoroplethLayerTooltipData,
  MapView,
  Tooltip,
  TooltipAtoms,
} from '@dynatrace/strato-geo';

type CountryStats = {
  country: string;
  primary_color: string;
  population: number;
  continent: string;
  apdex: string;
  status: string;
};

const countriesStats: CountryStats[] = [
  {
    country: 'DE',
    primary_color: '#f7c910',
    population: 84_724_070,
    continent: 'Europe',
    apdex: 'Excellent',
    status: 'muted',
  },
  {
    country: 'AU',
    primary_color: '#012066',
    population: 26_473_055,
    continent: 'Oceania',
    apdex: 'Excellent',
    status: 'affected',
  },
  {
    country: 'BR',
    primary_color: '#029639',
    population: 218_689_752,
    continent: 'South America',
    apdex: 'Unacceptable',
    status: 'muted',
  },
  {
    country: 'ES',
    primary_color: '#c70219',
    population: 48_196_693,
    continent: 'Europe',
    apdex: 'Fair',
    status: 'resolved',
  },
  {
    country: 'MX',
    primary_color: '#006e49',
    population: 131_135_337,
    continent: 'North America',
    apdex: 'Unacceptable',
    status: 'muted',
  },

  {
    country: 'CA',
    primary_color: '#d62618',
    population: 38_037_204,
    continent: 'North America',
    apdex: 'Excellent',
    status: 'muted',
  },
  {
    country: 'AR',
    primary_color: '#6CACE4',
    population: 47_327_407,
    continent: 'South America',
    apdex: 'Good',
    status: 'muted',
  },
  {
    country: 'VE',
    primary_color: '#FCE300',
    population: 28_515_829,
    continent: 'South America',
    apdex: 'Excellent',
    status: 'affected',
  },
  {
    country: 'CU',
    primary_color: '#002a90',
    population: 10_985_974,
    continent: 'North America',
    apdex: 'Good',
    status: 'resolved',
  },
  {
    country: 'PR',
    primary_color: '#ee0200',
    population: 3_285_874,
    continent: 'North America',
    apdex: 'Excellent',
    status: 'muted',
  },
  {
    country: 'UA',
    primary_color: '#0057B7',
    population: 41_732_779,
    continent: 'Europe',
    apdex: 'Fair',
    status: 'resolved',
  },
  {
    country: 'IT',
    primary_color: '#028e44',
    population: 59_346_717,
    continent: 'Europe',
    apdex: 'Poor',
    status: 'affected',
  },
];

const ChoroplethLayerTooltip = () => {
  return (
    <MapView height={400} initialViewState={{ zoom: 1 }}>
      <ChoroplethLayer
        data={countriesStats}
        regionAccessor="country"
        color={Colors.Charts.Sequential.Pink.Color05.Default}
      >
        <ChoroplethLayer.Tooltip>
          {(regionData: ChoroplethLayerTooltipData<CountryStats>) => {
            const { name, color, data } = regionData;

            const { apdex } = data;

            return (
              <Tooltip.Body>
                <Tooltip.Item>
                  <Tooltip.Symbol>
                    <TooltipAtoms.SingleDataPoint color={color} />
                  </Tooltip.Symbol>
                  <Tooltip.Content>
                    <Tooltip.Text variant="secondary">{name}</Tooltip.Text>
                  </Tooltip.Content>
                  <Tooltip.Value>
                    <TooltipAtoms.Chip>{apdex}</TooltipAtoms.Chip>
                  </Tooltip.Value>
                </Tooltip.Item>
              </Tooltip.Body>
            );
          }}
        </ChoroplethLayer.Tooltip>
      </ChoroplethLayer>
    </MapView>
  );
};
```


#### ChoroplethLayerTooltipData
 |
 | Name | Type | Default | Description
 | `color` | | | The hovered region color
 | `name` | | | The hovered region name
 | `data` | T | | The hovered region custom data
 | `seriesActions?` | (data: ) => | | Series actions callback for the default tooltip

#### ChoroplethLayerTooltipHandler

##### Signature:
`export declare type ChoroplethLayerTooltipHandler = (regionData: ) => ;`

#### ChoroplethLayerTooltipHandlerProps
 |
 | Name | Type | Default | Description
 | `children?` | | | | The ChoroplethLayer tooltip handler template
 | `seriesActions?` | (data: ) => | | Series actions callback for the default tooltipStill have questions?Find answers in the Dynatrace Community
- Tooltip

---

## ConnectionLayer

`/design/data-visualizations/geo-maps/ConnectionLayer/`

The `ConnectionLayer` component renders connections between points on a map,
accepting an array of `Connection` data points with required properties like
latitude and longitude. It supports customization of color, thickness, direction
the connection indicators.

OverviewProperties

### Import

`tsx
import { ConnectionLayer } from '@dynatrace/strato-geo';
`

### Use cases

Use the `ConnectionLayer` to visually represent connections between points on a
world map. The `ConnectionLayer` subcomponent requires an array of `Connection`
objects as its data prop.

Each `Connection` object must contain at least one `path`, which is defined by
an array of data points. Each data point must have at least `latitude` and
`longitude`.

The `ConnectionLayer` automatically connects the points in the paths with lines.
It's commonly used to depict networks combined with geographical data, flight
connections, or any type of connection between different locations.

`tsx
[ { path: [ { name: 'Tangier', latitude: 35.76727, longitude: -5.79975, }, { name: 'Nantes', latitude: 47.218102, longitude: -1.5528, }, ], }, { path: [ { name: 'Barcelona', latitude: 41.3828939, longitude: 2.1774322, }, { name: 'Vienna', latitude: 48.2083537, longitude: 16.3725042, }, ], },];
`

Learn more about the data format here.

#### Customize connection styling

Each `ConnectionLayer` exposes some additional properties as `line` and
`connectionIndicator` to customize the layer's styling.

To alter the `color`, the `thickness`, or any of the other styles of a specific
`Connection` you can utilize the corresponding props.

It is also possible to modify the way the connection is displayed, to do this,
use the `curve` parameter, which allows two values `line` or `smooth`.

### Tooltip

The `Connection Layer` provides a tooltip that displays additional information
about the connected points, when hovering over a connection.

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Customize connection styling
- Tooltip

### Props

The `ConnectionLayer` component renders connections between points on a map,
accepting an array of `Connection` data points with required properties like
latitude and longitude. It supports customization of color, thickness, direction
the connection indicators.

OverviewProperties

### ConnectionLayer

#### ConnectionLayerProps

##### Signature:
`export declare type LayerProps = & ( | );`

#### Connection

##### Signature:
`export declare type Connection = {
 /** Array of connections */
 path: [];
};` |
 | Name | Type | Default | Description
 | `path` | [] | | Array of connections

#### Location
 |
 | Name | Type | Default | Description
 | `latitude` | | | The latitude coordinate of the location.
 | `longitude` | | | The longitude coordinate of the location.

#### CurvedLine

##### Signature:
`export declare type CurvedLine = | ;`

### Tooltip

#### ConnectionLayerTooltipData
 |
 | Name | Type | Default | Description
 | `color` | | | The hovered connection color
 | `thickness` | | | The hovered connection thickness
 | `data` | T | | The hovered connection custom data and path locations

#### ConnectionLayerTooltipHandler

##### Signature:
`export declare type ConnectionLayerTooltipHandler = (connectionData: ) => ;`

#### ConnectionLayerTooltipHandlerProps
 |
 | Name | Type | Default | Description
 | `children?` | | | | The ConnectionLayer tooltip handler template
 | `seriesActions?` | (data: ) => | | Series actions callback for the default tooltipStill have questions?Find answers in the Dynatrace Community
- Tooltip

---

## DotLayer

`/design/data-visualizations/geo-maps/DotLayer/`

The `DotLayer` component renders data points on a map, accepting an array of
data points with required properties like latitude and longitude. It provides
support for various shapes, optional features like custom background for icons,
rotation, and tooltips, along with granular color customization and integration
with legends for color configuration.

OverviewProperties

### Import

`tsx
import { DotLayer } from '@dynatrace/strato-geo';
`

### Use cases

Use the `DotLayer` component to render data points as dots or simple shapes. The
component accepts an array of data points as the data prop. Each data point must
have `latitude` and `longitude` properties as the bare minimum.

`tsx
[ { name: 'Vienna International Airport', latitude: 48.1049967, longitude: 16.5848987, }, { name: 'Barcelona El Prat Josep Tarradellas Airport', latitude: 41.2969439, longitude: 2.0790474, },];
`

Learn more about the data format here.

#### Data point shapes and sizes

The `DotLayer` component supports various shapes for the data points using the
`shape` prop. The supported shapes are `circle`, `square`, `diamondheart`,
`cross`, `star`, `triangle` and `pin`. The default shape is `pin`. The pin act
as a location marker and the tip of the pin will be placed at the location of
the datapoint, instead of the center.

The size of the shape can be adjusted using the `shapeSize` prop, which receives
a number (in pixels) as a value. The default shape size is 32 pixels.

Additionally, emojis, single character strings, and Strato icons are supported
as data point shapes.

Note: Strato icons must be imported from `@dynatrace/strato-icons` namespace.

#### Icon background

The `DotLayer` component provides an optional feature to include a background
for the rendered data points' icons. This feature enhances the visual
representation of the data points on the map.

To enable the optional icon background, use the `background` prop when defining
the `DotLayer`. The `background` prop can take a boolean, a string, or a
callback function:

- If set to `false`, the icon background feature is disabled for the `DotLayer`
and the default background is only shown on a data point hover.

- If set to `true`, the background color is visible without hovering, and the
default background color is applied.

- If a string is provided, the feature is enabled with a custom background color
specified by the CSS string or color token.

- When a callback function is provided, the function should return a string that
specifies the background color for each data point.

#### Bearing

The `DotLayer` component supports rotation of the data points using the
`bearing` prop. The `bearing` prop accepts a number or a callback that returns a
number. The bearing number can between 0 and 360. The default value is 0.

#### Tooltip

The `DotLayer` component has an optional tooltip that displays additional
information when hovering over data point.

By default, the tooltip will display the location information of the hovered
point, but
it can be heavily customized.

#### Coloring

The `DotLayer` supports two ways of color configuration: granular configuration
using the `color` prop, or using a one of the available legend subcomponents
(e.g. `SequentialLegend`, `ThresholdLegend`, or `CategoricalLegend`).

Note: Detailed information about coloring can be found in the `MapView`
documentation page under the `Coloring` section.

##### Granular color configuration

For a granular color customization, layer's `color` prop should be used.

##### Color configuration using a legend

To connect a data layer to the legend, a `color` property of the layer should be
set to `legend` string.

###### Sequential legend

###### Threshold legend

###### Categorical legend

CodeSandbox Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Data point shapes and sizes
- Icon background
- Bearing
- Tooltip
- Coloring

### Props

The `DotLayer` component renders data points on a map, accepting an array of
data points with required properties like latitude and longitude. It provides
support for various shapes, optional features like custom background for icons,
rotation, and tooltips, along with granular color customization and integration
with legends for color configuration.

OverviewProperties

### DotLayer

#### DotLayerProps

##### Signature:
`export declare type DotLayerProps = & ( | );`

#### DotLayerBaseProps
extends |
 | Name | Type | Default | Description
 | `data` | T[] | | An array of location data items to be displayed in the DotLayer
 | `shape?` | | | | `'pin'` | The shape of the dots
 | `bearing?` | | ((item: T) => ) | `0` | The bearing property, which determines the rotation angle of the dots.
It can be a constant number or a function that calculates the bearing based on the data item
 | `background?` | | | ((item: T) => ) | `false` | The background setting for the DotLayer.
As boolean, it toggles the visibility and sets a default color.
As string, it defines the background color.
 | `shapeSize?` | | `32` | The shapeSize property allows to edit the size of the shape, icon, emoji
or ReactNode passed to the shape property in pixels, minimum value is 1.

#### LocationColorProps
 |
 | Name | Type | Default | Description
 | `color?` | | ((item: T) => ) | | Custom color to apply to the layer

#### LegendColorLayerProps
 |
 | Name | Type | Default | Description
 | `color` | | | When the color prop is set to 'legend', a value accessor is needed
 | `valueAccessor` | | | The value accessor to map data point values to legend color

#### Location
 |
 | Name | Type | Default | Description
 | `latitude` | | | The latitude coordinate of the location.
 | `longitude` | | | The longitude coordinate of the location.

### Tooltip

#### DotLayerTooltipData
 |
 | Name | Type | Default | Description
 | `color` | | | The hovered dot color
 | `bearing` | | | The hovered dot bearing
 | `data` | T | | The hovered dot custom data and location

#### DotLayerTooltipHandler

##### Signature:
`export declare type DotLayerTooltipHandler = (dotData: ) => | ;`

#### DotLayerTooltipHandlerProps
 |
 | Name | Type | Default | Description
 | `children?` | | | | The DotLayer tooltip handler template
 | `seriesActions?` | (data: ) => | | Series actions callback for the default tooltipStill have questions?Find answers in the Dynatrace Community
- Tooltip

---

## MapView

`/design/data-visualizations/geo-maps/MapView/`

The `MapView` is a component that renders a map with various geospatial data
layers.

OverviewProperties

### Import

`tsx
import { MapView } from '@dynatrace/strato-geo';
`

### Use cases

The minimal representation of a `MapView` component is a base layer that
contains a world map.

The height of the `MapView` component must be set explicitly using the `height`
prop. The width of the `MapView` component will be determined by the width of
the parent container.

Learn more about the `MapView` props here.

```tsx
import { MapView } from '@dynatrace/strato-geo';

const Simple = () => {
  return <MapView height={400} />;
};
```

```tsx
import { MapView } from '@dynatrace/strato-geo';

const Simple = () => {
  return <MapView height={400} />;
};
```


#### Formatter

There are two other options in the formatter that allow for greater
customization. The first option enables you to prepend the unit to the value,
while the second option enables you to ignore the original unit and append a
custom string instead. Additionally, there is a custom formatter option
available to allow you to change the input unit to one of your choice, e.g.: if
the input unit is `bits`, you are able to switch and display the unit as
`bytes`, correctly formatted. The formatted value is applied in the tooltip and
the legend.

```tsx
import { BubbleLayer, MapView, SequentialLegend } from '@dynatrace/strato-geo';
import { units } from '@dynatrace-sdk/units';

const Formatter = () => {
  const bubbleData = [
    {
      longitude: -155.7645,
      latitude: 19.608333,
      magnitude: 1024,
    },
    {
      longitude: -100.7645,
      latitude: 30.608333,
      magnitude: 1024000,
    },
  ];

  return (
    <MapView
      formatter={{
        maximumFractionDigits: 2,
        input: units.data.kilobyte,
        output: units.data.megabyte,
      }}
    >
      <BubbleLayer
        data={bubbleData}
        color="legend"
        valueAccessor="magnitude"
        radius={({ magnitude }) => magnitude / 50}
      >
        <BubbleLayer.Tooltip />
      </BubbleLayer>
      <SequentialLegend colorPalette="orange" min={0} max={1500000} />
    </MapView>
  );
};
```

```tsx
import { BubbleLayer, MapView, SequentialLegend } from '@dynatrace/strato-geo';
import { units } from '@dynatrace-sdk/units';

const Formatter = () => {
  const bubbleData = [
    {
      longitude: -155.7645,
      latitude: 19.608333,
      magnitude: 1024,
    },
    {
      longitude: -100.7645,
      latitude: 30.608333,
      magnitude: 1024000,
    },
  ];

  return (
    <MapView
      formatter={{
        maximumFractionDigits: 2,
        input: units.data.kilobyte,
        output: units.data.megabyte,
      }}
    >
      <BubbleLayer
        data={bubbleData}
        color="legend"
        valueAccessor="magnitude"
        radius={({ magnitude }) => magnitude / 50}
      >
        <BubbleLayer.Tooltip />
      </BubbleLayer>
      <SequentialLegend colorPalette="orange" min={0} max={1500000} />
    </MapView>
  );
};
```


#### Truncation mode

The purpose of truncation is to gracefully handle extra long tooltips or legends
within data visualization components. By changing the value of this property,
you have control over where truncation is applied within charts. By default, the
truncation is applied to the `middle` value with the use of an ellipsis.
Truncation can, however be changed to instead be applied at the `start` or `end`
of data visualization component elements.

```tsx
import { BubbleLayer, CategoricalLegend, MapView } from '@dynatrace/strato-geo';

const TruncationMode = () => {
  const extraLongName =
    'Extreme Lorem ipsum dolor sit amet consectetur adipiscing elit ad inceptos Risk';
  const customColorPalette = {
    'Low Risk': 'rgba(238,208,103,0.8)',
    'Medium Risk': 'rgba(238,170,122,0.8)',
    'High Risk': 'rgba(225,109,123,0.8)',
    [extraLongName]: '#000000',
  };

  const bubbleData = [
    {
      longitude: -155.7645,
      latitude: 19.608333,
      status: extraLongName,
      magnitude: 100,
    },
  ];

  return (
    <MapView truncationMode="end">
      <BubbleLayer
        data={bubbleData}
        color="legend"
        valueAccessor="magnitude"
        radius={({ magnitude }) => magnitude * 2}
      >
        <BubbleLayer.Tooltip />
      </BubbleLayer>
      <CategoricalLegend colorPalette={customColorPalette} />
    </MapView>
  );
};
```

```tsx
import { BubbleLayer, CategoricalLegend, MapView } from '@dynatrace/strato-geo';

const TruncationMode = () => {
  const extraLongName =
    'Extreme Lorem ipsum dolor sit amet consectetur adipiscing elit ad inceptos Risk';
  const customColorPalette = {
    'Low Risk': 'rgba(238,208,103,0.8)',
    'Medium Risk': 'rgba(238,170,122,0.8)',
    'High Risk': 'rgba(225,109,123,0.8)',
    [extraLongName]: '#000000',
  };

  const bubbleData = [
    {
      longitude: -155.7645,
      latitude: 19.608333,
      status: extraLongName,
      magnitude: 100,
    },
  ];

  return (
    <MapView truncationMode="end">
      <BubbleLayer
        data={bubbleData}
        color="legend"
        valueAccessor="magnitude"
        radius={({ magnitude }) => magnitude * 2}
      >
        <BubbleLayer.Tooltip />
      </BubbleLayer>
      <CategoricalLegend colorPalette={customColorPalette} />
    </MapView>
  );
};
```


#### Controlled and uncontrolled states

The `MapView` component can be used in both controlled and uncontrolled states.
In the uncontrolled state it's possible to configure the initial longitude,
latitude and zoom level of the map using `initialViewState` prop. By default,
the map will be centered on the equator and zoomed out to show the whole world.

In the controlled state, user can attach state handlers to the `MapView`
component using the `onViewStateChange` prop, as well as dynamically change the
longitude, latitude and zoom level of the map.

```tsx
import { MapView } from '@dynatrace/strato-geo';

const Uncontrolled = () => {
  const initialViewState = {
    longitude: 2.1700581793810483,
    latitude: 41.389448379708284,
    zoom: 3,
  };

  return <MapView height={400} initialViewState={initialViewState}></MapView>;
};
```

```tsx
import { MapView } from '@dynatrace/strato-geo';

const Uncontrolled = () => {
  const initialViewState = {
    longitude: 2.1700581793810483,
    latitude: 41.389448379708284,
    zoom: 3,
  };

  return <MapView height={400} initialViewState={initialViewState}></MapView>;
};
```


#### Data layers

The `MapView` component supports rendering of data layers on the map using the
different subcomponents. Multiple data layers of the same type can be rendered.
The order of the data layers is determined by the order of the subcomponents of
the `MapView` component.

For detailed documentation about each data layer, please refer to the respective
docs pages.Still have questions?Find answers in the Dynatrace Community
- Import
- Use cases
- Formatter
- Truncation mode
- Controlled and uncontrolled states
- Data layers

### Props

The `MapView` is a component that renders a map with various geospatial data
layers.

OverviewProperties

### MapView

#### MapViewProps

##### Signature:
`export declare type MapViewProps = & ( | );`

#### MapViewBaseProps
extends`, , , ` |
 | Name | Type | Default | Description
 | `mapStyle?` | | | Styles of maplibre to be overridden
 | `onViewStateChange?` | (viewState: ) => | | Callback to listen for the changes in the ViewState
 | `loading?` | | `false` | Set whether map is loading
 | `height?` | | | `400px` | The height of the chart. If a number is passed, it will be treated as px
 | `truncationMode?` | | `'middle'` | The truncation mode to be used as start, middle or end in the long legend
labels
 | `formatter?` | | | | Map View formatter options
 | `onContextLostError?` | () => | | Callback fired when the map context is lost.
Browsers have a limit of active WebGL canvas contexts.
The map will automatically show an error state, but this callback
allows consumers to perform additional actions (e.g., analytics, custom UI).

#### MapViewControlledProps
extends

#### MapViewUncontrolledProps
extends`<>` |
 | Name | Type | Default | Description
 | `initialViewState?` | | | The initial state of the Map.

#### ViewState
 |
 | Name | Type | Default | Description
 | `longitude?` | | | Longitude at map center
 | `latitude?` | | | Latitude at map center
 | `zoom?` | | | Map zoom level

### MapView Ref

#### MapViewRef
 |
 | Name | Type | Default | Description
 | `element` | | | | The map component root element
 | `downloadData` | () => | | Downloads map raw data .
 | `zoomIn` | () => | | Performs zoom in action on the domain
 | `zoomOut` | () => | | Performs zoom out action on the domain
 | `zoomToFit` | () => | | Performs zoom to fit action on the domain
 | `reset` | () => | | Reset the domain to the default

### Sequential legend

#### SequentialLegendProps
extends |
 | Name | Type | Default | Description
 | `min?` | | | The min boundary
 | `max?` | | | The max boundary
 | `colorPalette?` | [] | | | The color palette to apply to the legend

#### BaseLegendProps

##### Signature:
`export declare type Base = ;`

#### LegendPosition

##### Signature:
`export declare type LegendPosition = (typeof )[];`

#### ColorPalette

##### Signature:
`export declare type ColorPalette = (typeof )[];`

### Threshold legend

#### ThresholdLegendProps
extends |
 | Name | Type | Default | Description
 | `ranges` | [] | | Ranges of the threshold legend

#### BaseLegendProps

##### Signature:
`export declare type Base = ;`

#### LegendPosition

##### Signature:
`export declare type LegendPosition = (typeof )[];`

#### ColorPalette

##### Signature:
`export declare type ColorPalette = (typeof )[];`

#### ColoredRange
 |
 | Name | Type | Default | Description
 | `from` | | | Range starting point
 | `to` | | | Range ending point
 | `color?` | | | The color to use in this range

### Categorical legend

#### CategoricalLegendProps
extends |
 | Name | Type | Default | Description
 | `colorPalette` | [] | | {
 [key: ]: ;
 } | | The color palette to apply to the legend

#### BaseLegendProps

##### Signature:
`export declare type Base = ;`

#### LegendPosition

##### Signature:
`export declare type LegendPosition = (typeof )[];`

#### ColorPalette

##### Signature:
`export declare type ColorPalette = (typeof )[];`

### Legend shared props

#### BaseLegendProps

##### Signature:
`export declare type Base = ;`

### Interactions

#### ChartInteractionsProps
 |
 | Name | Type | Default | Description
 | `onZoomChange?` | | | Callback called when any zoom event has been performed affecting the data timeframe

#### ZoomChangeHandler

##### Signature:
`export declare type ZoomChangeHandler = (newStart: | , newEnd: | , type: ) => ;`

### Toolbar

#### ChartToolbarProps
 |
 | Name | Type | Default | Description
 | `placement?` | | `'top-right'` | Initial placement for the toolbar

#### ToolbarPlacement

##### Signature:
`export declare type ToolbarPlacement = | | | ;`Still have questions?Find answers in the Dynatrace Community
- MapView Ref
- Sequential legend
- Threshold legend
- Categorical legend
- Legend shared props
- Interactions
- Toolbar

---

