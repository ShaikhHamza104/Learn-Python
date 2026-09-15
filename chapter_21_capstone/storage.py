"""
capstone/storage.py

Milestone 3: Persist validated exchange-rate records to DuckDB so data
survives between runs, instead of being fetched fresh every single time.

DuckDB is an embedded analytical database (like SQLite, but built for
analytics) with a SQL dialect close to Postgres - a natural fit for a
project that's ultimately about analyzing data with Pandas.

Works directly with ExchangeRateRecord objects from validator.py - by
this point in the pipeline, only clean, validated data reaches storage.
"""

import logging
from pathlib import Path

import duckdb

logging.basicConfig(
    filename="capstone.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

DB_FILE = Path("capstone.duckdb")


class ExchangeRateRepository:
    """Handles all DuckDB reads and writes for exchange-rate records."""

    def __init__(self, db_path=DB_FILE):
        self.db_path = str(db_path)
        self._create_table()

    def _connect(self):
        """Open a fresh connection for this operation."""
        return duckdb.connect(self.db_path)

    def _create_table(self):
        """Create the table on first run - safe to call every time."""
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS exchange_rates (
                    date DATE NOT NULL,
                    base VARCHAR NOT NULL,
                    target VARCHAR NOT NULL,
                    rate DOUBLE NOT NULL,
                    PRIMARY KEY (date, base, target)
                )
                """
            )

    def save_many(self, records):
        """
        Save a list of validated ExchangeRateRecord objects.

        Uses INSERT OR REPLACE so re-fetching the same date/pair just
        updates the rate instead of creating duplicate rows.
        """
        if not records:
            return

        with self._connect() as conn:
            conn.executemany(
                """
                INSERT OR REPLACE INTO exchange_rates
                    (date, base, target, rate)
                VALUES (?, ?, ?, ?)
                """,
                [(str(r.date), r.base, r.target, r.rate) for r in records],
            )
        logging.info(f"Saved {len(records)} records to {self.db_path}")

    def save_one(self, record):
        """Save a single validated ExchangeRateRecord object."""
        self.save_many([record])

    def load_all(self, base=None, target=None):
        """
        Load stored records, optionally filtered by currency pair.

        Returns a list of plain dicts - the data is already trusted
        since it only ever got into the table via save_many().
        """
        query = "SELECT date, base, target, rate FROM exchange_rates"
        conditions = []
        params = []

        if base:
            conditions.append("base = ?")
            params.append(base)
        if target:
            conditions.append("target = ?")
            params.append(target)
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        query += " ORDER BY date"

        with self._connect() as conn:
            rows = conn.execute(query, params).fetchall()

        records = [
            {
                "date": str(row[0]),
                "base": row[1],
                "target": row[2],
                "rate": row[3],
            }
            for row in rows
        ]
        logging.info(f"Loaded {len(records)} records from {self.db_path}")
        return records

    def load_as_dataframe(self, base=None, target=None):
        """
        Load stored records directly as a Pandas DataFrame.

        DuckDB can hand back a DataFrame natively, without you looping
        over rows yourself - this is the method Milestone 4 will use.
        """
        query = "SELECT date, base, target, rate FROM exchange_rates"
        conditions = []
        params = []

        if base:
            conditions.append("base = ?")
            params.append(base)
        if target:
            conditions.append("target = ?")
            params.append(target)
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        query += " ORDER BY date"

        with self._connect() as conn:
            df = conn.execute(query, params).df()

        logging.info(f"Loaded {len(df)} records into a DataFrame")
        return df


if __name__ == "__main__":
    # Quick self-test using a few sample records run through validator.py.
    # This does NOT call the real API.
    from validator import validate_records

    sample_records = [
        {"date": "2026-09-01", "base": "USD", "target": "INR", "rate": 94.95},
        {"date": "2026-09-02", "base": "USD", "target": "INR", "rate": 94.97},
        {"date": "2026-09-03", "base": "USD", "target": "INR", "rate": 94.49},
    ]

    clean, _ = validate_records(sample_records)

    repo = ExchangeRateRepository(db_path="test_capstone.duckdb")
    repo.save_many(clean)

    print("Stored records:")
    for row in repo.load_all(base="USD", target="INR"):
        print(" -", row)

    print("\nRunning save_many again with the SAME data to prove")
    print("INSERT OR REPLACE doesn't create duplicate rows...")
    repo.save_many(clean)
    print(f"Row count is still: {len(repo.load_all())}")

    print("\nLoading straight into a Pandas DataFrame:")
    print(repo.load_as_dataframe())
