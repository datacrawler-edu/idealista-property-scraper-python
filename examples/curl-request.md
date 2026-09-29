# cURL request

Replace `YOUR_APIFY_TOKEN` with an Apify API token and edit the JSON input if needed. Do not commit the token.

```bash
curl --request POST \
  "https://api.apify.com/v2/acts/datascraperes~idealista-property-search-scraper/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN" \
  --header "Content-Type: application/json" \
  --data @data/sample-input.json
```

The endpoint waits for the run to finish and returns the default Dataset items. For long-running jobs, use the asynchronous run endpoint and read the Dataset after completion.
