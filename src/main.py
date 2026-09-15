import csv
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_FILE = PROJECT_ROOT / "data" / "raw" / "sales_2026-09-15.csv"


def read_sales_data(file_path):
    """Read sales records from a CSV file."""
    with file_path.open(mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def main():
    """Run the retail sales data pipeline."""
    sales_records = read_sales_data(RAW_DATA_FILE)

    print("Retail Sales Data Pipeline started successfully")
    print(f"Input file: {RAW_DATA_FILE.name}")
    print(f"Records read: {len(sales_records)}")


if __name__ == "__main__":
    main()