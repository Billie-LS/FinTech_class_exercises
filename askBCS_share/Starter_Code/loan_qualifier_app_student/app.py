# -*- coding: utf-8 -*-
"""Loan Qualifier Application.

This is a command line application to match applicants with qualifying loans.

Example:
    $ python app.py
"""
import sys
import fire
import questionary
from pathlib import Path

from qualifier.utils.fileio import load_csv

from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)

from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value


def load_bank_data():
    """Ask for the file path to the latest banking data and load the CSV file.

    Returns:
        The bank data from the data rate sheet CSV file.
    """

    csvpath = questionary.text(
        "Enter a file path to a rate-sheet (.csv):").ask()
    csvpath = Path(csvpath)
    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}")

    return load_csv(csvpath)


def get_applicant_info():
    """Prompt dialog to get the applicant's financial information.

    Returns:
        Returns the applicant's financial information.
    """

    credit_score = questionary.text("What's your credit score?").ask()
    debt = questionary.text(
        "What's your current amount of monthly debt?").ask()
    income = questionary.text("What's your total monthly income?").ask()
    loan_amount = questionary.text("What's your desired loan amount?").ask()
    home_value = questionary.text("What's your home value?").ask()

    credit_score = int(credit_score)
    debt = float(debt)
    income = float(income)
    loan_amount = float(loan_amount)
    home_value = float(home_value)

    return credit_score, debt, income, loan_amount, home_value


# changed loan to loan_amount
def find_qualifying_loans(bank_data, credit_score, debt, income, loan_amount, home_value):
    """Determine which loans the user qualifies for.

    Loan qualification criteria is based on:
        - Credit Score
        - Loan Size
        - Debit to Income ratio (calculated)
        - Loan to Value ratio (calculated)

    Args:
        bank_data (list): A list of bank data.
        credit_score (int): The applicant's current credit score.
        debt (float): The applicant's total monthly debt payments.
        income (float): The applicant's total monthly income.
        # changed loan to loan_amount
        loan_amount (float): The total loan amount applied for.
        home_value (float): The estimated home value.

    Returns:
        A list of the banks willing to underwrite the loan.

    """

    # Calculate the monthly debt ratio
    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
    print(f"The monthly debt to income ratio is {monthly_debt_ratio:.02f}")

    # Calculate loan to value ratio
    # changed loan to loan_amount
    loan_to_value_ratio = calculate_loan_to_value_ratio(
        loan_amount, home_value)
    print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.")

    # Run qualification filters
    # changed loan to loan_amount
    bank_data_filtered = filter_max_loan_size(loan_amount, bank_data)
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    bank_data_filtered = filter_debt_to_income(
        monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = filter_loan_to_value(
        loan_to_value_ratio, bank_data_filtered)

    print(f"Found {len(bank_data_filtered)} qualifying loans")

    return bank_data_filtered


def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.
    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    # YOUR CODE HERE!
    output_path = Path('qualifying_loans.csv')
    header = ['Lender', 'Max Loan Amount', 'Max LTV',
              'Max DTI', 'Min Credit Score', 'Interest Rate']
    if len(qualifying_loans) > 0:
        save_value = questionary.confirm(
            'Would you like to save your qualifying bank loans? enter 1 for yes or 0 for no').ask()
        if save_value == True:
            with open(output_path, 'r+', newline='') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=',')
                csvwriter.writerow(header)
                for loan in qualifying_loans:
                    csvwriter.writerow(loan)
            print("Your qualifying loans have now been saved.")
        else:
            print("Your qualifying loans were not saved.")

    # save_location = questionary.text("Enter a file path/name to save the qualifying loans (.csv):").ask()


def run():
    """The main function for running the script."""

    # Load the latest Bank data
    bank_data = load_bank_data()

    # Get the applicant's information
    credit_score, debt, income, loan_amount, home_value = get_applicant_info()

    # Find qualifying loans
    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )

    # Save qualifying loans
    save_qualifying_loans(qualifying_loans)


if __name__ == "__main__":
    fire.Fire(run)

# run via - python app.py
# at prompt for CSV file path, enter - ./data/daily_rate_sheet.csv


"""thoughts, ideas, suggestions
# A
start code for csv file
qualifying_loans = []
qualifying_loans = find_qualifying_loans(
    bank_data, credit_score, debt, income, loan_amount, home_value)
header = ['Lender', 'Max Loan Amount', 'Max LTV',
          'Max DTI', 'Min Credit Score', 'Interest Rate']
output_path = Path('qualifying_loans.csv')


    with open(output_path, 'r+', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(header)
        for row in qualifying_loans:
            csvwriter.writerow(row.values())


# B
if len(qualifying_loans) == 0:
           output_path = Path(f"results/unqualified_loans/{name.lower()}")
           save_csv(output_path, qualifying_loans)
       else:
           output_path = Path(f"results/qualified_loans/{name.lower()}")
           save_csv(output_path, qualifying_loans) 
# C
def saveCsv(df,filepath, filename):
    df.to_csv(os.path.join(filepath,filename))

saveCsv(df,filepath='/home/ashleyubuntu/Documents',filename='df.csv')
"""
