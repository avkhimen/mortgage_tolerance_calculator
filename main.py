import numpy as np
import argparse
import yaml

def main():

    with open('env.yml', 'r') as file:
        yaml_data = yaml.safe_load(file)

    parser = argparse.ArgumentParser(description="Calculate stress test interest rate")
    parser.add_argument("--territory", type=str, help="Territory name")
    parser.add_argument("--stress_test_rate", type=float, help="Stress test rate as float [0.5-1.5]")

    args = parser.parse_args()

    territory = args.territory
    stress_test_rate = args.stress_test_rate

    maximum_interest_rate = 10
    print(f'Under the input conditions for {territory} the maximum calculated interest rate is {maximum_interest_rate}%')

if __name__ == '__main__':
    main()