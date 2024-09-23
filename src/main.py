import csv


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
    # Example usage for get_total_leads_from_csv
    file_path = "test.csv"
    total_leads = get_total_leads_from_csv(file_path)
    print(f"Total Leads: {total_leads}")

    # Example usage for calculate_lead_metrics
    total_spend, total_leads, cost_per_lead = calculate_lead_metrics(total_leads, 911.26)
    print(
        f"Total Spend: {total_spend}, Total Leads: {total_leads}, Cost per Lead: {cost_per_lead}"
    )
