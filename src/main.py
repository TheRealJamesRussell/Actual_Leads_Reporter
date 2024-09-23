import csv
from collections import defaultdict


def remove_test_entries(file_path: str) -> str:
    """
    Remove entries where the 'Name' or 'Email' fields contain the word 'test' (case-insensitive), and write to a new CSV.

    :param file_path: The path to the original CSV file.
    :return: The path to the cleaned CSV file.
    """
    output_file_path = f"cleaned_{file_path}"

    # Open the file with utf-8-sig encoding to handle and remove BOM
    with open(file_path, mode="r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        rows_to_write = []

        for row in reader:
            name = row.get("Name", "").lower()
            email = row.get("Email", "").lower()
            # Check if 'test' is in 'Name' or 'Email' fields
            if "test" not in name and "test" not in email:
                rows_to_write.append(row)

    # Open the output file with utf-8-sig encoding to ensure BOM is handled correctly
    with open(output_file_path, mode="w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        # Write rows that do not contain 'test' in 'Name' or 'Email'
        for row in rows_to_write:
            writer.writerow(row)

    return output_file_path


def dedupe_csv(file_path: str) -> str:
    """
    Remove duplicates based on phone number or email, and write to a new CSV.

    :param file_path: The path to the original CSV file.
    :return: The path to the deduped CSV file.
    """
    unique_emails = {}
    unique_phones = {}
    output_file_path = f"deduped_{file_path}"

    # Open the file with utf-8-sig encoding to handle and remove BOM
    with open(file_path, mode="r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        for row in reader:
            email = row.get("Email")
            phone = row.get("Phone Number")
            # Check for uniqueness based on email or phone number
            if email not in unique_emails and phone not in unique_phones:
                unique_emails[email] = row
                unique_phones[phone] = row

    # Open the output file with utf-8-sig encoding to ensure BOM is handled correctly
    with open(output_file_path, mode="w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        # Write unique entries based on email
        for entry in unique_emails.values():
            writer.writerow(entry)

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
    # Example usage for removing test entries, deduping, and getting total leads from deduped CSV
    file_path: str = "test copy.csv"
    cleaned_file_path: str = remove_test_entries(file_path)
    deduped_file_path: str = dedupe_csv(cleaned_file_path)
    total_leads: int = get_total_leads_from_csv(deduped_file_path)
    print(f"Total Leads from deduped file: {total_leads}")

    # Example usage for calculate_lead_metrics
    total_spend: float
    total_leads: int
    cost_per_lead: float

    total_spend, total_leads, cost_per_lead = calculate_lead_metrics(
        total_leads, 911.26
    )

    print(
        f"Total Spend: {total_spend}, Total Leads: {total_leads}, Cost per Lead: {cost_per_lead}"
    )
