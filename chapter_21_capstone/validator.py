"""
capstone/validator.py

Milestone 2: Validate raw exchange-rate records fetched by fetcher.py
before they're allowed anywhere near storage or analysis.

Uses the same "validate at the door" pattern from
chapter_22_pydantic/04_pydantic_for_data_science.py - build a Pydantic
model describing what a valid record looks like, then run every raw
dict through it, keeping the clean ones and logging the rejects.
"""

import logging
from datetime import date as date_type

from pydantic import BaseModel, Field, TypeAdapter, ValidationError

logging.basicConfig(
    filename="capstone.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class ExchangeRateRecord(BaseModel):
    """One validated exchange-rate observation."""

    date: date_type
    base: str = Field(min_length=3, max_length=3)
    target: str = Field(min_length=3, max_length=3)
    rate: float = Field(gt=0)


def validate_records(raw_records):
    """
    Validate a list of raw dicts (as returned by
    ExchangeRateFetcher.get_history) against ExchangeRateRecord.

    Returns (clean_records, rejected) where:
      - clean_records is a list of validated ExchangeRateRecord objects
      - rejected is a list of (raw_dict, error) tuples for bad rows
    """
    clean_records = []
    rejected = []

    for raw in raw_records:
        try:
            record = ExchangeRateRecord(**raw)
            clean_records.append(record)
        except ValidationError as e:
            logging.error(f"Rejected record {raw}: {e.error_count()} error(s)")
            rejected.append((raw, e))

    logging.info(
        f"Validated {len(clean_records)} records, rejected {len(rejected)}"
    )
    return clean_records, rejected


def validate_single(raw_record):
    """
    Validate a single raw dict (as returned by
    ExchangeRateFetcher.get_latest).

    Raises ValidationError if the record is invalid.
    """
    return ExchangeRateRecord(**raw_record)


# A TypeAdapter lets you validate a whole list in one line, without
# writing your own loop - useful once you trust the data source more.
ExchangeRateRecordList = TypeAdapter(list[ExchangeRateRecord])


if __name__ == "__main__":
    # A few fake records to prove validation actually rejects bad data.
    # This does NOT call the real API - it's just a quick self-test.
    sample_records = [
        {"date": "2026-09-01", "base": "USD", "target": "INR", "rate": 94.95},
        {"date": "2026-09-02", "base": "USD", "target": "INR", "rate": 94.97},
        # bad: base currency code too short
        {"date": "2026-09-03", "base": "US", "target": "INR", "rate": 94.49},
        # bad: negative rate
        {"date": "2026-09-04", "base": "USD", "target": "INR", "rate": -1},
        # bad: not a real date
        {"date": "not-a-date", "base": "USD", "target": "INR", "rate": 95.0},
    ]

    clean, bad = validate_records(sample_records)

    print(f"\nValid records: {len(clean)}")
    for record in clean:
        print(" -", record)

    print(f"\nRejected records: {len(bad)}")
    for raw, error in bad:
        print(" -", raw, "->", error.error_count(), "error(s)")
