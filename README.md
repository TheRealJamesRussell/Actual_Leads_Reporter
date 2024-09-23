# Actual Leads Reporter
This is a CLI-based Lead Reporter that processes a CSV of leads. It performs the following tasks:
- Checks and removes duplicates
- Checks and removes any lead entries with "test" in it
- Calculates the total spend and provides an accurate cost per lead

## Installation

### To install the project for normal use, run:
1. Ensure you have `pipx` installed:
   ```
   python3 -m pip install --user pipx
   python3 -m pipx ensurepath
   ```
2. Install the project using `pipx`:
   ```
   pipx install actual-leads-reporter
   ```

### To install the project for development, run:
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/actual-leads-reporter.git
   cd actual-leads-reporter
   ```
2. Install the project in editable mode with development tools:
   ```
   pip install -e .[dev]
   ```