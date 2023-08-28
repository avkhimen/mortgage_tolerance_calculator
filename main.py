import numpy as np
import argparse
import yaml

def calculate_highest_interest_rate(available_per_month, property_term):
    # Define the maximum allowable loan amount
    max_loan_amount = available_per_month * property_term
    
    # Define a list of interest rates to test
    interest_rates = np.linspace(0, 1.0, num=1000)  # 1000 points between 0 and 1
    
    for rate in interest_rates:
        # Calculate the loan amount using the formula for loan payment
        loan_amount = (available_per_month * (1 - (1 + rate)**(-term))) / rate
        
        if loan_amount <= max_loan_amount:
            return rate * 100  # Convert to percentage

    return None  # No rate found within the limit

def main():

    with open('env.yml', 'r') as file:
        yaml_data = yaml.safe_load(file)

    parser = argparse.ArgumentParser(description="Calculate stress test interest rate")
    parser.add_argument("--territory", type=str, help="Territory name")
    parser.add_argument("--stress_test_rate", type=float, help="Stress test rate as float [0.5-1.5]")

    args = parser.parse_args()

    territory = args.territory
    stress_test_rate = args.stress_test_rate

    maximum_interest_rate = calculate_highest_interest_rate(available_per_month, property_term)
    maximum_interest_rate = 10
    print(f'Under the input conditions for {territory} the maximum calculated interest rate is {maximum_interest_rate}%')

if __name__ == '__main__':
    main()