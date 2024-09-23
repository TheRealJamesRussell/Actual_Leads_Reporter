# Actual Leads Reporter
This is a CLI-based Lead Reporter that processes a CSV of leads. It performs the following tasks:
- Checks and removes duplicates
- Checks and removes any lead entries with "test" in it
- Calculates the total spend and provides an accurate cost per lead

## Installation

### To install the project for normal use, run:
1. Ensure you have `pipx` installed:
   ```sh
   python3 -m pip install --user pipx
   python3 -m pipx ensurepath
   ```
2. Install the project using `pipx`:
   ```sh
   pipx install actual-leads-reporter
   ```

### To install the project for development, run:
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/actual-leads-reporter.git
   cd actual-leads-reporter
   ```
2. Install the project in editable mode with development tools:
   ```sh
   pip install -e .[dev]
   ```

## Usage

To use the CLI tool, run the following command:
```sh
leads <path_to_csv_file>
```

### Example
```sh
leads leads.csv
```

This will:
1. Clean the CSV file by removing test entries and duplicates.
2. Calculate the total number of leads.
3. Calculate the cost per lead based on a predefined total spend of $911.26.
4. Output the total spend, total leads, and cost per lead.

### Output
The CLI will output:
- Total Leads from cleaned file
- Total Spend
- Total Leads
- Cost per Lead