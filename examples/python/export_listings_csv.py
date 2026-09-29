"""Run the hosted Idealista Actor and export useful fields to CSV."""

from __future__ import annotations

import csv
import json
import os
from pathlib import Path

from apify_client import ApifyClient


ACTOR_ID = "datascraperes/idealista-property-search-scraper"
ROOT = Path(__file__).resolve().parents[2]
INPUT_PATH = ROOT / "data" / "sample-input.json"
OUTPUT_PATH = ROOT / "data" / "exported-idealista-listings.csv"
FIELDS = [
    "propertyCode",
    "url",
    "country",
    "operation",
    "propertyType",
    "price",
    "size",
    "rooms",
    "bedrooms",
    "bathrooms",
    "municipality",
    "province",
    "detailStatus",
]


def main() -> None:
    token = os.environ.get("APIFY_API_TOKEN")
    if not token:
        raise SystemExit("Set APIFY_API_TOKEN before running this example.")

    run_input = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    client = ApifyClient(token)
    run = client.actor(ACTOR_ID).call(run_input=run_input)
    items = client.dataset(run["defaultDatasetId"]).iterate_items()

    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        for item in items:
            writer.writerow(item)

    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
