import numpy as np
import numpy_financial as npf
import argparse
import yaml

def calculate_interest_rate(data,monthly_payment, property_term):
    '''Calculates interest rate from term, payment, and mortage amount'''
    return npf.rate(property_term*12, -monthly_payment, data['average_property_price'] * 0.8, 0) * 12 * 100 # Assume 20% downpayment on a home

def calculate_cash_available_per_month(data, stress_test_rate): 
    '''Calclates available disposable income per month'''
    total_housing_costs_without_mortgage = data['average_property_price'] * (data['property_tax_rate'] 
                                                                             + data['property_insurance_rate'])/12
    total_personal_expenses_adults = data['number_of_adults_in_family'] * sum(data['Individual_adults'].values()) * stress_test_rate
    total_expenses_adults = total_housing_costs_without_mortgage + total_personal_expenses_adults * stress_test_rate
    total_expenses_kids = data['number_of_kids_in_family'] * sum(data['Individual_kids'].values()) * stress_test_rate
    total_expenses_shared = sum(data['Shared'].values()) * stress_test_rate
    expenses_per_month = total_expenses_adults + total_expenses_kids + total_expenses_shared
    salary_per_month = data['number_of_adults_in_family'] * data['annual_wage'] * data['tax_rate'] / 12

    available_per_month = salary_per_month - expenses_per_month

    return available_per_month

def main():

    # Import yaml data
    with open('env.yml', 'r') as file:
        yaml_data = yaml.safe_load(file)

    parser = argparse.ArgumentParser(description="Calculate stress test interest rate")
    parser.add_argument("--territory", type=str, help="Territory name")
    parser.add_argument("--stress_test_rate", type=float, help="Stress test rate as float [0.5-1.5]")
    args = parser.parse_args()
    
    # Get args
    territory = args.territory
    stress_test_rate = args.stress_test_rate

    # Get data for territory
    data = yaml_data[territory]

    # Calc available cash per month
    available_per_month = int(calculate_cash_available_per_month(data, stress_test_rate))

    # Get term
    property_term = data['property_term']

    # Calc interest rate
    interest_rate = round(calculate_interest_rate(data, available_per_month, property_term),2)

    # Report results
    print(f'For {territory} the disposable income per month is {available_per_month}$')
    print(f'For {territory} the calculated maximum interest rate is {interest_rate}%')

if __name__ == '__main__':
    main()