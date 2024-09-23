import csv


def remove_test_entries(rows: list[dict]) -> list[dict]:
    """
    Remove entries where the 'Name' or 'Email' fields contain the word 'test' (case-insensitive).

    :param rows: List of rows from the CSV file.
    :return: List of rows without 'test' in 'Name' or 'Email'.
    """
    cleaned_rows = []
    for row in rows:
        name = row.get("Name", "").lower()
        email = row.get("Email", "").lower()
        # Check if 'test' is in 'Name' or 'Email' fields
        if "test" not in name and "test" not in email:
            cleaned_rows.append(row)
    return cleaned_rows


def dedupe_csv(rows: list[dict]) -> list[dict]:
    """
    Remove duplicates based on phone number or email.

    :param rows: List of rows from the CSV file.
    :return: List of unique rows based on email or phone number.
    """
    unique_emails = {}
    unique_phones = {}
    deduped_rows = []

    for row in rows:
        email = row.get("Email")
        phone = row.get("Phone Number")
        # Check for uniqueness based on email or phone number
        if email not in unique_emails and phone not in unique_phones:
            unique_emails[email] = row
            unique_phones[phone] = row
            deduped_rows.append(row)

    return deduped_rows


def clean_csv(file_path: str) -> str:
    """
    Clean the CSV by removing test entries and duplicates, and write to a new CSV.

    :param file_path: The path to the original CSV file.
    :return: The path to the cleaned and deduped CSV file.
    """
    output_file_path = f"cleaned_deduped_{file_path}"

    # Open the file with utf-8-sig encoding to handle and remove BOM
    with open(file_path, mode="r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        rows = list(reader)

    # Apply cleaning functions
    rows = remove_test_entries(rows)
    rows = dedupe_csv(rows)

    # Open the output file with utf-8-sig encoding to ensure BOM is handled correctly
    with open(output_file_path, mode="w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    return output_file_path


def get_total_leads_from_csv(file_path: str) -> int:
    """
    Read a CSV file and return the total lead count as an integer.

    :param file_path: The path to the CSV file.
    :return: The total number of leads.
    """
    total_leads: int = 0
    with open(file_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_leads += 1
    return total_leads


def calculate_lead_metrics(
    total_leads: int, total_spend: float
) -> tuple[float, int, float]:
    """
    Calculate and return the total spend, total leads, and cost per lead.

    :param total_leads: The number of leads generated.
    :param total_spend: The total amount of money spent.
    :return: A tuple containing total spend, total leads, and cost per lead.
    """
    cost_per_lead = total_spend / total_leads if total_leads != 0 else 0.0
    return total_spend, total_leads, cost_per_lead


if __name__ == "__main__":
    # Example usage for cleaning CSV and getting total leads from cleaned CSV
    file_path: str = "test copy.csv"
    cleaned_file_path: str = clean_csv(file_path)
    total_leads: int = get_total_leads_from_csv(cleaned_file_path)
    print(f"Total Leads from cleaned file: {total_leads}")

    # Example usage for calculate_lead_metrics
    total_spend: float
    cost_per_lead: float

    total_spend, total_leads, cost_per_lead = calculate_lead_metrics(
        total_leads, 911.26
    )

    print(
        f"Total Spend: {total_spend}, Total Leads: {total_leads}, Cost per Lead: {cost_per_lead}"
    )
