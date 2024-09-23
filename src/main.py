def calculate_lead_metrics(total_leads: int, total_spend: float) -> tuple[float, int, float]:
    """
    Calculate and return the total spend, total leads, and cost per lead.

    :param total_leads: The number of leads generated.
    :param total_spend: The total amount of money spent.
    :return: A tuple containing total spend, total leads, and cost per lead.
    """
    cost_per_lead = total_spend / total_leads if total_leads != 0 else 0.0
    return total_spend, total_leads, cost_per_lead

if __name__ == "__main__":
    # Example usage
    total_spend, total_leads, cost_per_lead = calculate_lead_metrics(5, 500.0)
    print(f"Total Spend: {total_spend}, Total Leads: {total_leads}, Cost per Lead: {cost_per_lead}")