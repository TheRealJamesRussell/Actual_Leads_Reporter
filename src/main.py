import csv
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import click

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


def calculate_cost_per_lead(total_leads: int, total_spend: float) -> float:
    """
    Calculate and return the cost per lead.

    :param total_leads: The number of leads generated.
    :param total_spend: The total amount of money spent.
    :return: The cost per lead.
    """
    cost_per_lead = total_spend / total_leads if total_leads != 0 else 0.0
    return cost_per_lead


@click.command()
@click.option("-c","--csv-path", type=click.Path(exists=True), required=True, help="Path to the CSV file.")
@click.option("-s","--spend", type=float, required=True, help="Total amount of money spent.")
def main(csv_path: str, spend: float):
    """
    CLI tool to process a CSV file, clean it, and calculate cost per lead. 
    Use the --file-path flag to specify the path to the CSV file and the --total-spend flag to specify the total spend amount.
    """
    try:
        # Clean the CSV file by removing test entries and deduping, and get the path to the cleaned file
        cleaned_file_path: str = clean_csv(csv_path)

        # Get the total number of leads from the cleaned CSV file
        total_leads: int = get_total_leads_from_csv(cleaned_file_path)
        click.echo(f"Total Leads from cleaned file: {total_leads}")

        # Calculate the cost per lead
        cost_per_lead: float = calculate_cost_per_lead(total_leads, spend)

        # Print the total spend, total leads, and cost per lead
        click.echo(
            f"Total Spend: {spend}, Total Leads: {total_leads}, Cost per Lead: {cost_per_lead}"
        )
    except FileNotFoundError:
        click.echo(f"Error: The file {csv_path} was not found.", err=True)

if __name__ == '__main__':
    main()


if __name__ == "__main__":
    main()
