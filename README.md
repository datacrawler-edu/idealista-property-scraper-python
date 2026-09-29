# Idealista property scraper with Python, JavaScript and cURL

Run **Idealista Property Listings Scraper | Sale & Rent** from Apify's web interface without writing code, or integrate it with Python, JavaScript or cURL to get structured **property listings with public details and multimedia metadata**.

This repository contains working request examples, sanitized sample input, sample output and CSV data so you can understand the result format before starting a live request.

[Open Idealista Property Listings Scraper on Apify](https://apify.com/datascraperes/idealista-property-search-scraper?fpr=edudata)

## What this repository helps you do

- Search sale or rental listings across Spain, Portugal, Italy and France.
- Compare property supply across several locations in one run.
- Filter by property type, price range and minimum bedrooms.
- Export deduplicated listing records to JSON or CSV for analysis.

## Example result

The repository includes a sanitized example in [`data/sample-output.json`](data/sample-output.json) and a tabular version in [`data/sample-output.csv`](data/sample-output.csv).

```json
{
  "propertyCode": "example-idealista-001",
  "title": "Two-bedroom apartment near the city centre",
  "country": "es",
  "operation": "sale",
  "price": 285000,
  "municipality": "Madrid",
  "size": 82,
  "bedrooms": 2,
  "detailStatus": "fetched",
  "multimedia": {"images": [], "videos": []},
  "scrapedAt": "2026-09-29T12:00:00Z"
}
```

## Run without code

You can run the hosted Actor directly from the Apify web interface. This is the simplest option if you do not need to write a program.

1. Open [Idealista Property Listings Scraper on Apify](https://apify.com/datascraperes/idealista-property-search-scraper?fpr=edudata).
2. In the **Input** tab, enter one or more place names in **Locations**.
3. Choose the country, sale or rent, property type and any optional price or bedroom filters.
4. Set **Maximum listings** and click **Start**.
5. Open the **Dataset** output and export it as JSON or CSV.

Use [`docs/no-code-guide.md`](docs/no-code-guide.md) for the field-by-field walkthrough and [`data/sample-input.json`](data/sample-input.json) for a first test input.

## Try it with Apify's free plan

Apify's Free plan includes **$5 in monthly prepaid usage** that can be spent in the Apify Store or on your own Actors. No credit card is required to start. This can cover a small first test while credit is available; it is not unlimited free usage.

Unused credits expire at the end of the billing cycle and do not roll over. Check the [current Apify pricing](https://apify.com/pricing?fpr=edudata) before running a larger batch.

## Quick start for developers

### Python

#### 1. Install the client

```bash
pip install apify-client
```

#### 2. Set your Apify token

```bash
export APIFY_API_TOKEN="your-token"
```

On Windows PowerShell:

```powershell
$env:APIFY_API_TOKEN = "your-token"
```

#### 3. Run the example

```bash
python examples/python/idealista_listings.py
```

The example reads [`data/sample-input.json`](data/sample-input.json), starts the hosted Actor and prints the returned Dataset items.

## Input example

```json
{
  "country": "es",
  "locations": ["Madrid", "Málaga"],
  "operation": "sale",
  "propertyType": "homes",
  "maxPrice": 300000,
  "maxItems": 30
}
```

See the complete field guide in [`docs/input-reference.md`](docs/input-reference.md).

## Request examples

### cURL

See [`examples/curl-request.md`](examples/curl-request.md) for a synchronous API request.

### Python

See [`examples/python/idealista_listings.py`](examples/python/idealista_listings.py) for a basic run and [`examples/python/export_listings_csv.py`](examples/python/export_listings_csv.py) for CSV export.

### JavaScript

See [`examples/javascript/request.mjs`](examples/javascript/request.mjs).

All examples use the hosted Apify Actor. They do not expose a proxy, bypass access controls or require the Actor source code locally.

## Output fields

The most useful Dataset fields are:

| Field | Meaning |
| --- | --- |
| `propertyCode` and `url` | Stable listing identifier and public listing URL. |
| `title`, `description`, `price` | Public listing content and advertised price. |
| `country`, `operation`, `propertyType` | Market, sale/rent operation and listing category. |
| `municipality`, `province`, `district`, `neighborhood` | Available location hierarchy. |
| `size`, `rooms`, `bedrooms`, `bathrooms` | Advertised property dimensions and room counts. |
| `multimedia` | Available image, video and tour metadata as references. |
| `detailStatus` | Whether public detail enrichment was fetched, unavailable or not requested. |
| `scrapedAt` | UTC timestamp for the collected record. |

See [`docs/output-reference.md`](docs/output-reference.md) for the complete output contract.

## Common use cases

Read [`docs/use-cases.md`](docs/use-cases.md) for complete examples covering:

- City-level property inventory.
- Sale-versus-rent market comparisons.
- Price-filtered exports for research or lead analysis.

## How to collect Idealista property listings with Python

Use [`examples/python/idealista_listings.py`](examples/python/idealista_listings.py) with an Apify token. The script starts the hosted Actor and iterates over the default Dataset without requiring the Actor source code.

## How to export Idealista listings to CSV

Use [`examples/python/export_listings_csv.py`](examples/python/export_listings_csv.py), or export the completed Dataset as CSV from the Apify interface. The example writes a flat file containing the most useful listing and location columns.

## FAQ

See [`docs/faq.md`](docs/faq.md) for questions derived from the actual Actor behavior.

## Limits and pricing

The Actor accepts 1–20 locations and a maximum of 30–5,000 unique listings per run. Supported markets are Spain (`es`), Portugal (`pt`), Italy (`it`) and France (`fr`). Optional filters include price, operation, property type and minimum bedrooms.

Billing uses one `result` event for each successful unique listing saved to the default Dataset. Failed, duplicate and undelivered listings are not charged. The current tiered prices are $0.001500 per listing at FREE, $0.001350 at BRONZE, $0.001200 at SILVER, and $0.001125 at GOLD, PLATINUM and DIAMOND. Check the [Actor page](https://apify.com/datascraperes/idealista-property-search-scraper?fpr=edudata) for current pricing.

## Hosted version

Use the hosted version when you need repeatable execution, batching, scheduling, API access or Dataset storage without managing the scraping infrastructure yourself. It can be run from the web interface or called programmatically:

[Open Idealista Property Listings Scraper on Apify](https://apify.com/datascraperes/idealista-property-search-scraper?fpr=edudata)

## Responsible use

Use the returned data lawfully and respect the terms, access rules, privacy obligations and intellectual-property rights that apply to your use case. Never commit API tokens or other credentials to this repository.

## Support

For a problem with the examples, [open a GitHub issue](https://github.com/datacrawler-edu/idealista-property-scraper-python/issues) with the command, sanitized input and error message. For an execution problem, include the Apify run ID but never include your token.

## License

This repository is released under the MIT License.
