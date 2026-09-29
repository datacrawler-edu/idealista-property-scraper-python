# Input reference

The Actor accepts one JSON object. `locations` is required; the other fields have public defaults or are optional filters.

| Field | Type | Required | Example | Description |
| --- | --- | :---: | --- | --- |
| `country` | string | No | `"es"` | Market: `es` Spain, `pt` Portugal, `it` Italy or `fr` France. Default: `es`. |
| `locations` | string array | Yes | `["Madrid"]` | One to 20 place names. Each location is resolved before searching. |
| `operation` | string | No | `"sale"` | `sale` or `rent`. Default: `sale`. |
| `propertyType` | string | No | `"homes"` | `homes`, `offices`, `premises`, `garages`, `bedrooms`, `storageRooms`, `lands`, `buildings` or `newDevelopments`. Default: `homes`. |
| `minPrice` | integer | No | `100000` | Optional minimum advertised price in euros. Range: 0–1,000,000,000. |
| `maxPrice` | integer | No | `300000` | Optional maximum advertised price in euros. Range: 0–1,000,000,000. |
| `bedrooms` | integer | No | `2` | Optional minimum bedrooms. Range: 0–10. |
| `maxItems` | integer | No | `30` | Maximum unique listings across the run. Range: 30–5,000. Default: 30. |

## Validation and limits

- `locations` must contain at least one non-empty string and no more than 20 entries.
- Each location name is limited to 120 characters.
- `country`, `operation` and `propertyType` must use one of the documented values.
- `maxItems` applies to the complete run, not separately to every location.
- Request pacing and temporary recovery are managed by the hosted Actor; they are not user inputs.
