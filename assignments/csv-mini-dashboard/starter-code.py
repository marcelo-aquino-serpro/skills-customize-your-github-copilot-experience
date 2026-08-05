"""Starter code: CSV Mini Dashboard

Goal: load data, compute 3 indicators, and create 2 charts.
"""

import pandas as pd
import matplotlib.pyplot as plt


def load_data(path: str) -> pd.DataFrame:
    """Load CSV data into a DataFrame."""
    return pd.read_csv(path)


def show_basic_info(df: pd.DataFrame) -> None:
    """Print first rows and basic structure details."""
    print("First 5 rows:")
    print(df.head())
    print("\nShape:", df.shape)
    print("\nColumns:", list(df.columns))
    print("\nData types:")
    print(df.dtypes)


def calculate_indicators(df: pd.DataFrame) -> dict:
    """Return core dashboard indicators."""
    total_revenue = df["revenue"].sum()
    avg_revenue = df["revenue"].mean()
    top_category = (
        df.groupby("category", as_index=False)["revenue"].sum()
        .sort_values("revenue", ascending=False)
        .iloc[0]["category"]
    )

    return {
        "total_revenue": total_revenue,
        "avg_revenue": avg_revenue,
        "top_category": top_category,
    }


def plot_revenue_by_category(df: pd.DataFrame) -> None:
    """Create and save a revenue-by-category bar chart."""
    grouped = df.groupby("category", as_index=False)["revenue"].sum()

    plt.figure(figsize=(8, 5))
    plt.bar(grouped["category"], grouped["revenue"])
    plt.title("Revenue by Category")
    plt.xlabel("Category")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig("revenue_by_category.png")
    plt.close()


def plot_order_value_distribution(df: pd.DataFrame) -> None:
    """Create and save a histogram of order values."""
    plt.figure(figsize=(8, 5))
    plt.hist(df["revenue"], bins=8)
    plt.title("Order Value Distribution")
    plt.xlabel("Revenue")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("order_value_distribution.png")
    plt.close()


def print_insights(indicators: dict) -> None:
    """Print short insights based on computed metrics."""
    print("\nInsights:")
    print(f"- Total revenue is {indicators['total_revenue']:.2f}.")
    print(f"- Average revenue per sale is {indicators['avg_revenue']:.2f}.")
    print(f"- The top category by revenue is {indicators['top_category']}.")


def main() -> None:
    df = load_data("sales_data.csv")
    show_basic_info(df)

    indicators = calculate_indicators(df)
    print("\nIndicators:")
    print(indicators)

    plot_revenue_by_category(df)
    plot_order_value_distribution(df)
    print_insights(indicators)


if __name__ == "__main__":
    main()
