import numpy as np
import argparse
import yaml

def calculate_home_price(monthly_payment, term, interest_rate):
    # Convert annual interest rate to monthly interest rate
    monthly_interest_rate = (interest_rate / 12) / 100
    
    # Calculate loan amount using the formula for loan payment
    loan_amount = (monthly_payment * (1 - (1 + monthly_interest_rate)**(-term))) / monthly_interest_rate
    
    return loan_amount

def calculate_highest_interest_rate(available_per_month, property_term):
    # Define the maximum allowable loan amount
    max_loan_amount = available_per_month * property_term
    
    # Define a list of interest rates to test
    interest_rates = np.linspace(0, 1.0, num=1000)  # 1000 points between 0 and 1
    
    for rate in interest_rates:

        if rate < 1e-10:  # A very small positive value instead of zero
            continue

        # Calculate the loan amount using the formula for loan payment
        loan_amount = (available_per_month * (1 - (1 + rate)**(-property_term))) / rate
        
        if loan_amount <= max_loan_amount:
            return rate * 100  # Convert to percentage

    return None  # No rate found within the limit

def calculate_cash_available_per_month(data, stress_test_rate):

    #available_per_month = salary_per_month - expenses_per_month
    #salary_per_momth = number_of_adults * annual_wage * tax_rate / 12
    #expenses_per_month = total_expenses_adults + total_expenses_kids + total_expenses_shared
    #total_expenses_shared = 
    #total_expenses_kids = 
    #total_expenses_adults = total_personal_expenses_adults + total_housing_costs_without_mortgage
    #total_personal_expenses_adults = 
    #total_housing_costs = 

    total_housing_costs_without_mortgage = data['average_property_price'] * (data['property_tax_rate'] 
                                                                             + data['property_insurance_rate'])/12
    total_personal_expenses_adults = data['number_of_adults_in_family'] * sum(data['Individual_adults'].values()) * stress_test_rate
    total_expenses_adults = total_housing_costs_without_mortgage + total_personal_expenses_adults * stress_test_rate
    total_expenses_kids = data['number_of_kids_in_family'] * sum(data['Individual_kids'].values()) * stress_test_rate
    total_expenses_shared = sum(data['Shared'].values()) * stress_test_rate
    expenses_per_month = total_expenses_adults + total_expenses_kids + total_expenses_shared
    salary_per_month = data['number_of_adults_in_family'] * data['annual_wage'] * data['tax_rate'] / 12

    available_per_month = salary_per_month - expenses_per_month

    #available_per_month = 1000
    return available_per_month

def main():

    with open('env.yml', 'r') as file:
        yaml_data = yaml.safe_load(file)

    parser = argparse.ArgumentParser(description="Calculate stress test interest rate")
    parser.add_argument("--territory", type=str, help="Territory name")
    parser.add_argument("--stress_test_rate", type=float, help="Stress test rate as float [0.5-1.5]")

    args = parser.parse_args()

    territory = args.territory
    stress_test_rate = args.stress_test_rate

    data = yaml_data[territory]

    available_per_month = calculate_cash_available_per_month(data, stress_test_rate)

    property_term = data['property_term']

    maximum_interest_rate = calculate_highest_interest_rate(available_per_month, property_term)

    maximum_home_price = calculate_home_price(available_per_month, property_term, maximum_interest_rate)

    #maximum_interest_rate = 10
    print(f'Under the input conditions for {territory} the disposable income per month is {available_per_month}$')
    print(f'Under the input conditions for {territory} the maximum calculated interest rate is {maximum_interest_rate}%')
    print(f'This also implies the maximum allowable home price of {maximum_home_price}')

if __name__ == '__main__':
    main()