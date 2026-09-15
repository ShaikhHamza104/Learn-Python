"""
capstone/fetcher.py

Milestone 1: Fetcher class for the currency exchange-rate capstone project.

Wraps calls to the Frankfurter API (https://www.frankfurter.app), which
requires no API key or signup. Handles the same failure modes covered in
chapter_20_apis_and_data - timeouts, connection errors, and bad HTTP
status codes - so a single bad request never crashes the whole app.
"""

import logging

import requests

logging.basicConfig(
    filename="capstone.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

BASE_URL = "https://api.frankfurter.app"


class FetchError(Exception):
    """Raised when the Frankfurter API can't be reached or returns bad data."""
    pass


class ExchangeRateFetcher:
    """Fetches exchange-rate data from the Frankfurter API."""

    def __init__(self, base_currency="USD", timeout=5):
        self.base_currency = base_currency
        self.timeout = timeout

    def get_latest(self, target_currency):
        """
        Fetch the latest exchange rate from self.base_currency to
        target_currency.

        Returns a dict like:
            {"date": "2026-09-15", "base": "USD", "target": "INR",
             "rate": 83.12}

        Raises FetchError if the request fails for any reason.
        """
        url = f"{BASE_URL}/latest"
        params = {"from": self.base_currency, "to": target_currency}
        return self._get(url, params, target_currency)

    def get_history(self, target_currency, start_date, end_date):
        """
        Fetch daily exchange rates between start_date and end_date
        (both "YYYY-MM-DD" strings).

        Returns a list of dicts, one per day:
            [{"date": "2026-09-01", "base": "USD", "target": "INR",
              "rate": 83.05}, ...]

        Raises FetchError if the request fails for any reason.
        """
        url = f"{BASE_URL}/{start_date}..{end_date}"
        params = {"from": self.base_currency, "to": target_currency}
        data = self._get(url, params, target_currency, is_history=True)
        return data

    def _get(self, url, params, target_currency, is_history=False):
        """Shared request + error handling for both endpoints above."""
        try:
            response = requests.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            rates = data.get("rates") or {}

            if is_history:
                if not rates:
                    raise FetchError(
                        f"No historical data found for "
                        f"{self.base_currency}->{target_currency}. "
                        f"Check that both currency codes are valid."
                    )
                records = []
                for date, day_rates in sorted(rates.items()):
                    if target_currency not in day_rates:
                        raise FetchError(
                            f"'{target_currency}' is not a currency "
                            f"code the API recognizes."
                        )
                    records.append({
                        "date": date,
                        "base": self.base_currency,
                        "target": target_currency,
                        "rate": day_rates[target_currency],
                    })
                logging.info(
                    f"Fetched {len(records)} historical records for "
                    f"{self.base_currency}->{target_currency}"
                )
                return records

            if target_currency not in rates:
                raise FetchError(
                    f"'{target_currency}' is not a currency code the "
                    f"API recognizes."
                )
            rate = rates[target_currency]
            logging.info(
                f"Fetched {self.base_currency}->{target_currency}: {rate}"
            )
            return {
                "date": data["date"],
                "base": self.base_currency,
                "target": target_currency,
                "rate": rate,
            }

        except requests.exceptions.Timeout:
            logging.error("Request timed out while calling the API")
            raise FetchError("The request timed out. Try again shortly.")

        except requests.exceptions.ConnectionError:
            logging.error("Could not connect to the Frankfurter API")
            raise FetchError(
                "Could not connect - check your internet connection."
            )

        except requests.exceptions.HTTPError as e:
            logging.error(f"Bad response from API: {e}")
            raise FetchError(f"The API returned an error: {e}")

        except requests.exceptions.RequestException as e:
            logging.error(f"Network request error: {e}")
            raise FetchError(
                f"A network error occurred while reaching the API: {e}"
            )

        except (KeyError, ValueError, TypeError) as e:
            logging.error(f"Unexpected response format: {e}")
            raise FetchError(
                "Received an unexpected response format from the API."
            )


if __name__ == "__main__":
    fetcher = ExchangeRateFetcher(base_currency="USD")

    try:
        latest = fetcher.get_latest("INR")
        print("Latest rate:", latest)

        history = fetcher.get_history("INR", "2026-09-01", "2026-09-10")
        print(f"\nFetched {len(history)} historical records:")
        for record in history:
            print(" ", record)

    except FetchError as e:
        print("Error:", e)