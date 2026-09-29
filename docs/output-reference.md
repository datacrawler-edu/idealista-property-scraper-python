# Output reference

The default Dataset contains one object per unique listing delivered by the run. Optional fields remain `null` when the source does not publish them.

| Field | Type | Always present | Description |
| --- | --- | :---: | --- |
| `propertyCode` | string, integer or null | Yes | Idealista listing identifier. |
| `url` | string or null | Yes | Public listing URL. |
| `title` | string or null | No | Public listing title. |
| `country` | string or null | Yes | Market code: `es`, `pt`, `it` or `fr`. |
| `operation` | string or null | Yes | Sale or rent operation. |
| `propertyType` | string or null | No | Listing category returned by the source. |
| `price` | number or null | No | Advertised price in euros. |
| `priceByArea` | number or null | No | Advertised price per square metre. |
| `municipality`, `province`, `district`, `neighborhood` | string or null | No | Available location hierarchy. |
| `latitude`, `longitude` | number or null | No | Coordinates when published. |
| `size`, `usableArea`, `rooms`, `bedrooms`, `bathrooms` | number or null | No | Property dimensions and room counts. |
| `features` | object, array or null | No | Amenity flags returned by the source. |
| `energyCertification` | object or null | No | Energy data when full public details include it. |
| `multimedia` | object or null | No | Image, video and tour metadata and references. |
| `detailStatus` | string | Yes | `not_requested`, `fetched` or `unavailable`. |
| `sourceData` | object or null | No | Public search, detail and multimedia payload groups when available. |
| `scrapedAt` | string | Yes | UTC collection timestamp. |

## Dataset views

The Actor provides overview and details views. The overview emphasizes identifiers, operation, price, size and location. The details view adds property characteristics, amenities and energy data.

## Nullable fields

Availability varies by listing and market. A missing description, coordinate, advertiser field or media list is represented as `null` or an empty list according to the field contract; it is not an indication that the run failed.
