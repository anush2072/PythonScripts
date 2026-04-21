'''
* By using a personal loan to pay off part of the mortgage, you reduce the mortgage principal. 
* This means less money is left to charge interest on, so you pay less interest overall during the mortgage's 30 years.
* Even though the personal loan has a slightly higher interest rate, it's for a shorter time (4 years), 
so the total interest on it is much smaller than what you'd save on the mortgage.
In short: Smaller mortgage principal = less interest over 30 years.
"""
This script calculates the total interest paid on a mortgage over 30 years and compares it to a scenario where a personal loan is used to pay off part of the mortgage principal.

The script performs the following steps:
1. Defines the parameters for the mortgage and personal loan.
2. Implements a helper function to calculate the monthly payment and total interest for a given loan.
3. Calculates the total interest for the mortgage-only scenario.
4. Calculates the total interest for the scenario where a personal loan is used to reduce the mortgage principal.
5. Combines the total interest from the personal loan and the reduced mortgage.
6. Prints the total interest for both scenarios and the interest savings achieved by using the personal loan.

Parameters:
- mortgage_balance: Initial mortgage amount.
- mortgage_rate: Annual mortgage interest rate.
- mortgage_term_years: Mortgage term in years.
- personal_loan_amount: Personal loan amount.
- personal_loan_rate: Annual personal loan interest rate.
- personal_loan_term_years: Personal loan term in years.

Functions:
- loan_calculator(principal, annual_rate, term_years): Calculates the monthly payment and total interest for a loan.

Outputs:
- Total interest paid for the mortgage-only scenario.
- Total interest paid for the combined personal loan and reduced mortgage scenario.
- Interest savings achieved by using the personal loan.
"""
'''
# Define parameters for the calculation
mortgage_balance = 176250  # Initial mortgage amount
mortgage_rate = 6.5 / 100  # Annual mortgage interest rate
mortgage_term_years = 30  # Mortgage term in years

personal_loan_amount = 40000  # Personal loan amount
personal_loan_rate = 9.99 / 100  # Annual personal loan interest rate
personal_loan_term_years = 4  # Personal loan term in years

# Helper function to calculate monthly payment and total interest for a loan
def loan_calculator(principal, annual_rate, term_years):
    monthly_rate = annual_rate / 12
    months = term_years * 12
    monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    total_interest = monthly_payment * months - principal
    return monthly_payment, total_interest

# Calculate for the mortgage only scenario
mortgage_monthly_payment, mortgage_total_interest = loan_calculator(
    mortgage_balance, mortgage_rate, mortgage_term_years
)

# Calculate for the split scenario
personal_loan_monthly_payment, personal_loan_total_interest = loan_calculator(
    personal_loan_amount, personal_loan_rate, personal_loan_term_years
)

reduced_mortgage_balance = mortgage_balance - personal_loan_amount
reduced_mortgage_monthly_payment, reduced_mortgage_total_interest = loan_calculator(
    reduced_mortgage_balance, mortgage_rate, mortgage_term_years
)

# Combine total interest for the split scenario
split_total_interest = personal_loan_total_interest + reduced_mortgage_total_interest

print(f"Mortgage only: You will pay approximately ${mortgage_total_interest:,.2f} in interest over 30 years")
print(f"Mortgage + Personal Loan: You will pay approximately ${split_total_interest:,.2f} in combined interest (personal loan + reduced mortgage)")
print(f"  - Personal Loan Interest: ${personal_loan_total_interest:,.2f}")
print(f"  - Reduced Mortgage Interest: ${reduced_mortgage_total_interest:,.2f}")

# Print monthly payments
print(f"Monthly payment for mortgage only: ${mortgage_monthly_payment:,.2f}")
print(f"Monthly payment for personal loan: ${personal_loan_monthly_payment:,.2f}")
print(f"Monthly payment for reduced mortgage: ${reduced_mortgage_monthly_payment:,.2f}")

# Print conclusion
interest_savings = mortgage_total_interest - split_total_interest
print(f"Conclusion: Taking the personal loan to reduce the mortgage principal results in about ${interest_savings:,.2f} less interest overall.")
