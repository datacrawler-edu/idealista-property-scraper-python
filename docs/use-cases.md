# Use cases

## Build a city-level property inventory

Use one or more locations with `propertyType: "homes"` and a suitable `maxItems` value.

```json
{
  "country": "es",
  "locations": ["Madrid", "Málaga"],
  "operation": "sale",
  "propertyType": "homes",
  "maxItems": 100
}
```

Inspect `propertyCode`, `url`, `price`, the location fields and `detailStatus`. Export the Dataset as JSON for downstream processing or CSV for spreadsheet review.

## Compare sale and rent supply

Run the same locations twice, changing `operation` between `sale` and `rent`. Keep the location, property type and item limit consistent so the two Dataset exports can be compared.

```json
{
  "country": "pt",
  "locations": ["Lisboa", "Porto"],
  "operation": "rent",
  "propertyType": "homes",
  "maxItems": 60
}
```

Compare `price`, `size`, `rooms`, `bedrooms`, `municipality` and `scrapedAt`. The Actor deduplicates listings within each run; comparisons across separate runs should account for changing source inventory.

## Export a filtered research set

Use `minPrice`, `maxPrice` and `bedrooms` to narrow a run before exporting it.

```json
{
  "country": "it",
  "locations": ["Milano"],
  "operation": "sale",
  "propertyType": "homes",
  "minPrice": 150000,
  "maxPrice": 400000,
  "bedrooms": 2,
  "maxItems": 30
}
```

Use `export_listings_csv.py` to produce a flat CSV with the most useful columns. Keep `url` and `propertyCode` with every row so records can be traced back to the public listing.
