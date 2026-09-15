"""
capstone/analyzer.py

Milestone 4: Analyze stored exchange-rate data using Pandas.

Takes the DataFrame produced by storage.py's load_as_dataframe() and
turns it into real, human-readable insights - not just raw numbers.
"""

import logging

import pandas as pd

logging.basicConfig(
    filename="capstone.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class ExchangeRateAnalyzer:
    """Computes summary statistics and trends from exchange-rate data."""

    def __init__(self, df: pd.DataFrame):
        """
        df must have columns: date, base, target, rate.

        The date column is converted to a real datetime and the rows
        are sorted chronologically, since every calculation below
        depends on the data being in the correct order.
        """
        if df.empty:
            raise ValueError(
                "Cannot analyze an empty DataFrame - "
                "fetch and store some data first."
            )

        self.df = df.copy()
        self.df["date"] = pd.to_datetime(self.df["date"])
        self.df = self.df.sort_values("date").reset_index(drop=True)

        if "base" in self.df.columns and self.df["base"].nunique() > 1:
            raise ValueError(
                "Cannot analyze data containing multiple base currencies."
            )
        if "target" in self.df.columns and self.df["target"].nunique() > 1:
            raise ValueError(
                "Cannot analyze data containing multiple target currencies."
            )
        if self.df["date"].duplicated().any():
            raise ValueError(
                "Cannot analyze data containing duplicate date entries."
            )

    def summary(self):
        """
        Returns a dict of headline stats: min, max, mean rate, and
        which dates the min/max occurred on.
        """
        min_row = self.df.loc[self.df["rate"].idxmin()]
        max_row = self.df.loc[self.df["rate"].idxmax()]

        return {
            "num_records": len(self.df),
            "start_date": self.df["date"].min().date(),
            "end_date": self.df["date"].max().date(),
            "min_rate": min_row["rate"],
            "min_rate_date": min_row["date"].date(),
            "max_rate": max_row["rate"],
            "max_rate_date": max_row["date"].date(),
            "mean_rate": round(self.df["rate"].mean(), 4),
        }

    def daily_change(self):
        """
        Adds a 'change' column (day-over-day difference in rate) and
        a 'pct_change' column (that difference as a percentage).
        Returns the DataFrame with these two new columns.
        """
        result = self.df.copy()
        result["change"] = result["rate"].diff()
        result["pct_change"] = result["rate"].pct_change() * 100
        return result

    def rolling_average(self, window=3):
        """
        Adds a column with the rolling average rate over the given
        window size (in number of records). Useful for smoothing out
        day-to-day noise to see the underlying trend.
        """
        result = self.df.copy()
        result[f"rolling_avg_{window}"] = (
            result["rate"].rolling(window=window, min_periods=1).mean()
        )
        return result

    def biggest_single_day_move(self):
        """
        Returns the single day with the largest absolute change in
        rate compared to the previous day, or None if there isn't
        enough data to compare.
        """
        changes = self.daily_change()
        changes = changes.dropna(subset=["change"])
        if changes.empty:
            return None

        biggest = changes.loc[changes["change"].abs().idxmax()]
        return {
            "date": biggest["date"].date(),
            "rate": biggest["rate"],
            "change": round(biggest["change"], 4),
        }


if __name__ == "__main__":
    # Self-test using sample data run through validator + storage, so
    # this file can be tested without calling the real API.
    from storage import ExchangeRateRepository
    from validator import validate_records

    sample_records = [
        {"date": "2026-09-01", "base": "USD", "target": "INR", "rate": 94.95},
        {"date": "2026-09-02", "base": "USD", "target": "INR", "rate": 94.97},
        {"date": "2026-09-03", "base": "USD", "target": "INR", "rate": 94.49},
        {"date": "2026-09-04", "base": "USD", "target": "INR", "rate": 94.49},
        {"date": "2026-09-07", "base": "USD", "target": "INR", "rate": 94.49},
        {"date": "2026-09-08", "base": "USD", "target": "INR", "rate": 94.83},
        {"date": "2026-09-09", "base": "USD", "target": "INR", "rate": 95.11},
        {"date": "2026-09-10", "base": "USD", "target": "INR", "rate": 95.44},
    ]

    clean, _ = validate_records(sample_records)

    repo = ExchangeRateRepository(db_path="test_capstone.duckdb")
    repo.save_many(clean)

    df = repo.load_as_dataframe(base="USD", target="INR")
    analyzer = ExchangeRateAnalyzer(df)

    print("Summary:")
    for key, value in analyzer.summary().items():
        print(f"  {key}: {value}")

    print("\nDaily change:")
    print(analyzer.daily_change()[["date", "rate", "change", "pct_change"]])

    print("\n3-day rolling average:")
    rolling_3 = analyzer.rolling_average(window=3)
    print(rolling_3[["date", "rate", "rolling_avg_3"]])

    print("\nBiggest single-day move:")
    print(analyzer.biggest_single_day_move())
