# FAQ

## Can I run this Actor without Python or code?

Yes. Open the [hosted Actor](https://apify.com/datascraperes/idealista-property-search-scraper?fpr=edudata), enter the required values in the **Input** tab, click **Start** and inspect or export the results from the **Dataset** tab. See [`docs/no-code-guide.md`](no-code-guide.md).

## Can I test this Actor with Apify's free plan?

Apify's Free plan currently includes **$5 in monthly prepaid usage** for the Apify Store or your own Actors. It can cover a small test while credit is available, but it is not unlimited free usage. Unused credit expires at the end of the billing cycle. Check the [current Apify pricing](https://apify.com/pricing?fpr=edudata) for current terms.

## How do I search several cities in one run?

Put up to 20 place names in the `locations` array. The Actor resolves each place against the source suggestions and applies `maxItems` to the total unique listings across all requested locations.

## Which markets and property types are supported?

The markets are Spain (`es`), Portugal (`pt`), Italy (`it`) and France (`fr`). Property types include homes, offices, premises, garages, bedrooms, storage rooms, lands, buildings and new developments.

## What does Full + multimedia mean?

The hosted Actor returns a normalized listing with public detail enrichment and multimedia metadata when available. Image, video and tour values are references; media files are not bundled into the Dataset. The public integration repository does not expose the Actor implementation or its source credentials.

## Why can a listing have null fields?

Public fields vary by listing and market. A missing description, coordinate, advertiser field, energy value or media list is returned as `null` or an empty list according to the output contract.

## How is pricing calculated?

One `result` event represents one successful unique listing saved to the default Dataset. Failed, duplicate and undelivered listings are not charged. Current tiered prices are listed on the [Actor page](https://apify.com/datascraperes/idealista-property-search-scraper?fpr=edudata).
