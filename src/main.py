import csv
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_FILE = PROJECT_ROOT / "data" / "raw" / "sales_2026-09-15.csv"


def read_sales_data(file_path):
    """Read sales records from a CSV file."""
    with file_path.open(mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def validate_sales_data(sales_records):
    """Separate valid and rejected sales records."""
    valid_records = []
    rejected_records = []
    seen_transaction_ids = set()

    for record in sales_records:
        errors = []
        transaction_id = record["transaction_id"]

        if transaction_id in seen_transaction_ids:
            errors.append("Duplicate transaction ID")
        else:
            seen_transaction_ids.add(transaction_id)

        if not record["quantity"]:
            errors.append("Missing quantity")

        try:
            unit_price = float(record["unit_price"])

            if unit_price <= 0:
                errors.append("Unit price must be positive")
        except (TypeError, ValueError):
            errors.append("Invalid unit price")

        if not record["payment_method"]:
            errors.append("Missing payment method")

        if errors:
            rejected_records.append(
                {
                    "transaction_id": transaction_id,
                    "errors": errors,
                }
            )
        else:
            valid_records.append(record)

    return valid_records, rejected_records


def main():
    """Run the retail sales data pipeline."""
    sales_records = read_sales_data(RAW_DATA_FILE)
    valid_records, rejected_records = validate_sales_data(sales_records)

    print("Retail Sales Data Pipeline started successfully")
    print(f"Input file: {RAW_DATA_FILE.name}")
    print(f"Total records: {len(sales_records)}")
    print(f"Valid records: {len(valid_records)}")
    print(f"Rejected records: {len(rejected_records)}")

    for rejected_record in rejected_records:
        print(
            f"Rejected {rejected_record['transaction_id']}: "
            f"{', '.join(rejected_record['errors'])}"
        )


if __name__ == "__main__":
    main()