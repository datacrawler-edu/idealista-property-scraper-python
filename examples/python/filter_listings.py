"""Run a filtered Idealista search and print matching listing summaries."""

from __future__ import annotations

import os

from apify_client import ApifyClient


ACTOR_ID = "datascraperes/idealista-property-search-scraper"
RUN_INPUT = {
    "country": "es",
    "locations": ["Madrid"],
    "operation": "sale",
    "propertyType": "homes",
    "minPrice": 150000,
    "maxPrice": 400000,
    "bedrooms": 2,
    "maxItems": 30,
}


def main() -> None:
    token = os.environ.get("APIFY_API_TOKEN")
    if not token:
        raise SystemExit("Set APIFY_API_TOKEN before running this example.")

    client = ApifyClient(token)
    run = client.actor(ACTOR_ID).call(run_input=RUN_INPUT)
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        print(
            item.get("propertyCode"),
            item.get("price"),
            item.get("municipality"),
            item.get("url"),
            sep=" | ",
        )


if __name__ == "__main__":
    main()
