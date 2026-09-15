"""
capstone/main.py

Milestone 5: The CLI entry point that ties the whole capstone pipeline
together - fetch -> validate -> store -> analyze.

This file deliberately does NOT put the menu loop inside __init__ (a
mistake worth avoiding - it means CapstoneApp() would immediately start
prompting for input the moment you create the object, which makes the
class impossible to test or reuse). Instead, __init__ only sets up
state, and run() is called explicitly to start the interactive loop.
"""

import logging
from datetime import datetime

from pydantic import ValidationError

from analyzer import ExchangeRateAnalyzer
from fetcher import ExchangeRateFetcher, FetchError
from storage import ExchangeRateRepository
from validator import validate_records, validate_single

logging.basicConfig(
    filename="capstone.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

MENU_TEXT = """
=== Currency Exchange Rate Toolkit ===
1. Fetch latest rate
2. Fetch historical data (date range) and store it
3. View stored data
4. Analyze stored data
5. Exit
"""


def is_valid_currency_code(code: str) -> bool:
    """
    A cheap sanity check before hitting the API at all - real currency
    codes are always exactly 3 letters (USD, INR, EUR). This won't
    catch every invalid code (fetcher.py still checks against the
    API's actual response), but it catches empty input and obvious
    typos immediately, without wasting a network call.
    """
    return len(code) == 3 and code.isalpha()


def is_valid_date(date_str: str) -> bool:
    """
    Check that a string is a real calendar date in YYYY-MM-DD format,
    using Python's own date parser rather than a regex - this catches
    both wrong formats (e.g. "2026-15-9") and impossible dates
    (e.g. "2026-02-30") in one line.
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


class CapstoneApp:
    """Wires together the fetcher, validator, storage, and analyzer."""

    def __init__(self, base_currency="USD"):
        self.fetcher = ExchangeRateFetcher(base_currency=base_currency)
        self.repo = ExchangeRateRepository()

    def run(self):
        """Start the interactive menu loop - call this to use the app."""
        print("Welcome to the Currency Exchange Rate Toolkit!")

        while True:
            print(MENU_TEXT)
            choice = input("Select an option (1-5): ").strip()

            if choice == "1":
                self.fetch_latest()
            elif choice == "2":
                self.fetch_history()
            elif choice == "3":
                self.view_stored_data()
            elif choice == "4":
                self.analyze_data()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid option - please choose 1-5.")

    def fetch_latest(self):
        """Fetch, validate, and store today's latest rate for a currency."""
        target = input("Target currency code (e.g. INR): ").strip().upper()

        if not is_valid_currency_code(target):
            print(
                "Please enter a 3-letter currency code, e.g. INR, "
                "EUR, GBP."
            )
            return

        if target == self.fetcher.base_currency:
            print(
                f"Target currency can't be the same as the base "
                f"currency ({self.fetcher.base_currency}) - "
                f"converting a currency to itself isn't meaningful."
            )
            return

        try:
            raw = self.fetcher.get_latest(target)
        except FetchError as e:
            print(f"Could not fetch data: {e}")
            return

        try:
            record = validate_single(raw)
        except ValidationError as e:
            print(
                f"Fetched data failed validation "
                f"({e.error_count()} error(s)) - not saved."
            )
            logging.error(f"Validation failed for latest rate: {raw}")
            return

        self.repo.save_one(record)
        print(
            f"Saved: {record.date} {record.base}->{record.target} "
            f"= {record.rate}"
        )

    def fetch_history(self):
        """Fetch, validate, and store a date range of historical rates."""
        target = input("Target currency code (e.g. INR): ").strip().upper()
        start_date = input("Start date (YYYY-MM-DD): ").strip()
        end_date = input("End date (YYYY-MM-DD): ").strip()

        if not is_valid_currency_code(target):
            print(
                "Please enter a 3-letter currency code, e.g. INR, "
                "EUR, GBP."
            )
            return

        if not is_valid_date(start_date) or not is_valid_date(end_date):
            print(
                "Please enter both dates in YYYY-MM-DD format, "
                "e.g. 2026-09-15."
            )
            return

        if start_date > end_date:
            print("Start date cannot be after end date.")
            return

        if target == self.fetcher.base_currency:
            print(
                f"Target currency can't be the same as the base "
                f"currency ({self.fetcher.base_currency}) - "
                f"converting a currency to itself isn't meaningful."
            )
            return

        try:
            raw_records = self.fetcher.get_history(
                target, start_date, end_date
            )
        except FetchError as e:
            print(f"Could not fetch data: {e}")
            return

        if not raw_records:
            print("No data returned for that range - check your dates.")
            return

        clean, rejected = validate_records(raw_records)

        if clean:
            self.repo.save_many(clean)

        print(
            f"Saved {len(clean)} record(s). "
            f"Rejected {len(rejected)} record(s)."
        )

    def view_stored_data(self):
        """Print everything currently stored, optionally filtered."""
        prompt = "Filter by target currency (leave blank for all): "
        target = input(prompt).strip().upper()

        records = self.repo.load_all(target=target or None)

        if not records:
            print("No data stored yet - try fetching some first.")
            return

        print(f"\n{len(records)} record(s) stored:")
        for r in records:
            print(f"  {r['date']}  {r['base']}->{r['target']} = {r['rate']}")

    def analyze_data(self):
        """Run the Pandas analysis on whatever's currently stored."""
        prompt = "Target currency to analyze (e.g. INR): "
        target = input(prompt).strip().upper()

        if not is_valid_currency_code(target):
            print(
                "Please enter a 3-letter currency code, e.g. INR, "
                "EUR, GBP."
            )
            return

        if target == self.fetcher.base_currency:
            print(
                f"Target currency can't be the same as the base "
                f"currency ({self.fetcher.base_currency})."
            )
            return

        df = self.repo.load_as_dataframe(
            base=self.fetcher.base_currency, target=target
        )

        try:
            analyzer = ExchangeRateAnalyzer(df)
        except ValueError as e:
            print(e)
            return

        summary = analyzer.summary()
        print("\n--- Summary ---")
        for key, value in summary.items():
            print(f"  {key}: {value}")

        biggest_move = analyzer.biggest_single_day_move()
        if biggest_move:
            print("\n--- Biggest single-day move ---")
            print(
                f"  {biggest_move['date']}: rate {biggest_move['rate']} "
                f"(change {biggest_move['change']:+.4f})"
            )

        print("\n--- Last 5 days, with 3-day rolling average ---")
        rolling = analyzer.rolling_average(window=3)
        cols = ["date", "rate", "rolling_avg_3"]
        print(rolling[cols].tail(5).to_string(index=False))


if __name__ == "__main__":
    app = CapstoneApp(base_currency="USD")
    app.run()
