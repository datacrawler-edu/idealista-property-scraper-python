# Run Idealista Property Listings Scraper without code

You can use the hosted Actor from the Apify web interface without installing a package or writing a script.

## Step-by-step

1. Open [Idealista Property Listings Scraper on Apify](https://apify.com/datascraperes/idealista-property-search-scraper?fpr=edudata).
2. Select the **Input** tab.
3. Enter one or more city, province or area names in **Locations**.
4. Review **Country**, **Operation**, **Property type**, optional price or bedroom filters and **Maximum listings**.
5. Click **Start**.
6. When the run finishes, open the **Dataset** output and export JSON or CSV.

## First test

Start with the example in [`data/sample-input.json`](../data/sample-input.json). It requests up to 30 unique sale listings for Madrid and is small enough to inspect before a larger run.

## Use the monthly free usage credit

Apify's Free plan currently includes **$5 in monthly prepaid usage** for the Apify Store or your own Actors, and no credit card is required to start. Use a small input first so you can inspect the result while credit is available. The credit is not unlimited, and unused credit expires at the end of the billing cycle.

See the [current Apify pricing](https://apify.com/pricing?fpr=edudata) for current platform terms.

## What to check in the output

The Dataset should contain one row per unique listing delivered. Check `propertyCode`, `url`, `price`, `municipality` and `detailStatus`. When detail enrichment is available, `detailStatus` is `fetched`; a value of `unavailable` means the listing was returned but optional public detail data was not available.

The `multimedia` field contains media metadata and references when published by the listing. It does not guarantee that every listing has photos, videos or tours.

## Larger runs

You can request up to 5,000 unique listings in one run and up to 20 locations. The maximum applies to the complete run. Listings are deduplicated across locations, so the delivered count can be lower when the source has fewer matching listings.

Billing is one event per successful unique listing saved to the default Dataset. Review the current price on the [Actor page](https://apify.com/datascraperes/idealista-property-search-scraper?fpr=edudata) before sending a large request.
