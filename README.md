# mortgage_tolerance_calculator
This script calculates the maximum interest rate that Canadians can afford based on inputs such as average monthly salary, average debt, average prices of certain goods like phone plans, and average food costs

## How the script works

The script reads inputs from the env.yml file that dictates the average values for each territory.

The input into the script is the territory and the stress test rate. The stress test rate is a number close to 1, which acts as a multiplier for certain payments, like phone plan, miscelaneous, and car loan expenses.

## Using the script

To use:
1. Install requirements with `$ pip install -r requirements.txt`.
2. Make sure the values for your territory in `env.yml` file are correct.
3. Run with `$ python main.py --territory <territory name> --stress_test_rate <stress_test_rate>` or adjust the values in `run.sh` file and run with `$ sh run.sh`.

# License

Use as you like, at your own risk. Not suitable for financial advice. 