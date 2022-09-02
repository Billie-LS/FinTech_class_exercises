"""this script contains a variety of financial calculator
functions needed to determine loan qualifications"""

# As a lender,
# I want to calculate the monthly debt-to-income ratio
# so that we can assess the ability to pay of the borrower


def calculate_monthly_debt_ratio(monthly_debt_payment, monthly_income):
    """calculates for user the borrowers monthly debt ratio"""
    monthly_debt_ratio = int(monthly_debt_payment) / int(monthly_income)
    return monthly_debt_ratio


# As a lender,
# I want to calculate the loan-to-value ratio
# so that we can evaluate the risk of lending money to the borrower
def calculate_loan_to_value_ratio(loan_amount, home_value):
    """calculates for user the loan to value (LTV) ratio"""
    loan_to_value_ratio = int(loan_amount) / int(home_value)
    return loan_to_value_ratio
