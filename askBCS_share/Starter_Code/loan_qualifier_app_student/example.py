# coding: utf-8

import csv                # importing csv library
import statistics         # alternative for use with 'averages' via statistics.mean()
""" import pathlib            # importing pathlib library - potentially redundant, but boot-suspenders style """
from pathlib import Path  # importing 'Path' tool from pathlib

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""
loan_costs = [500, 600, 200, 1000, 450]   # ~ simple list

# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list
number_of_loans = len(loan_costs)
# use f-string to use variable to input the value, number of loans is integer and not monetary value
print(f'The total number of loans is {number_of_loans}')

# What is the total amount of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans
sum_of_loans = sum(loan_costs)
# use f-string to use variable to input the value, specify fixed 2 decimal places = The sum of all loans is $2750.00
print(f'The sum of all loans is ${sum_of_loans:.2f}')

# alternate syntax within f-string using round() and specify up to 2 decimal = The sum of all loans is $2750
print(f'The sum of all loans is ${round(sum_of_loans, 2)}')

# What is the average loan amount from the list?
# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount
average_loan_price = sum_of_loans / number_of_loans
# use f-string to use variable to input the value, specify fixed 2 decimal places = The average loan cost is $550.00
print(f'The average loan cost is ${average_loan_price:.2f}')

# alternate syntax using import statistics, statistics.mean()
average_loan_price = statistics.mean(loan_costs)
# use f-string to use variable to input the value, round() with possible 2 decimal places = The average loan cost is $550
print(f'The average loan cost is ${round(average_loan_price, 2)}')

"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, 
follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""

# Given the following loan data, you will need to calculate the present value for the loan
# present value formula = future_value / (1 + Discount_Rate) ** time   # where time = years and discount_Rate = ~'annual_hurdle_rate'
# future value formula = present_value * (1 + Discount_Rate) ** time

# adjusting for 'monthly precision' ->  present_value = future_value / (1 + discount_Rate / 12) ** remaining_months
# adjusting for 'monthly precision' ->  future_value = present_value * (1 + discount_Rate / 12) ** remaining_months
# provided in instructions, discount rate = 20% = 0.20

# A 'bullet' is a one-time lump-sum repayment of an outstanding loan made by the borrower
# A bullet transaction = loan requires the principal balance to be paid in full when it matures

loan = {                                    # dictionary
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# 1000 = present_value * (1 + 0.20 / 12)** remaining_months


# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.
# .get() returns the value of the key, 'future_value' and assigns to variable future_value
future_value = loan.get('future_value')
# .get() returns the value of the key, 'remaining_months' and assigns to variable remaining_months
remaining_months = loan.get('remaining_months')

# simple print value of variable, future_value to output = 1000
print(future_value)
# simple print value of variable, remaining_months to output = 9
print(remaining_months)

# f-string using round() to print value of variable and specify up to 2 decimal = the future value is $1000
print(f'the future value is ${round(future_value, 2)}')
# use f-string to print value of variable, remaining_months to output = the remaining months are 9
print(f'the remaining months are {remaining_months}')

# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + discount_rate/12) ** remaining_months

annual_discount_rate = 0.20
hurdle_rate = annual_discount_rate
# 'monthly precision' present value formula which uses variables future_value, hurdle_rate, and remaining_months whose values have been retrieved from dictionary using get()
present_value = future_value / (1 + hurdle_rate / 12) ** remaining_months
# prints to output
print(f'the fair value is ${present_value:.2f}')


# alternative approach to number 2 -> using functions for potential larger scale, repetitive operations
# add key:value pair for hurdle_rate to dictionary
# use get() to obtain assign value from dictionary to variable hurdle_rate
# use variable preesent_value

# define a THREE parameter function, present_value_fxn(1, 2, 3) that-
#           accepts the parameters/argumets using variables future_value, annual_discount_rate, and remaining_months; the values of which have obtain per previous
#           calculates the present value of the loan in the dictionary using the previously declared variable, present_value with value equals the present value formula
#                     enables change between yearly vs monthly precision without enterring the body of function
#           prints to output using f-string, the result of present value calculation = the fair value is $861.77
#           returns the calculation result making assignment to variable an option....
def present_value_fxn(future_value, annual_discount_rate, remaining_months):
    # variable, present_value has global scope previously defined as the 'monthly precision' present value formula
    present_value_calc = present_value
    print(
        f'directly from the function - the fair value is ${present_value_calc:.2f}')
    return present_value_calc


# define a TWO parameter function, present_value_fxn_a(1, 2) that-
#           accepts the parameters/argumets using variables loan and annual_discount_rate; the values of which have obtain per previous
#           calculates the present value of the loan in the dictionary using the previously declared variable, present_value with value equals the present value formula
#           prints to output using f-string, the result of present value calculation = the fair value is $861.77
#           returns the calculation result making assignment to variable an option....
def present_value_fxn_a(loan, annual_discount_rate):
    future_value = loan.get('future_value')
    remaining_months = loan.get('remaining_months')
    present_value_calc = present_value
    print(
        f'directly from the function - the fair value is ${present_value_calc:.2f}')
    return present_value_calc


#  define a ONE parameter function, present_value_fxn_b() that-
#           accepts the variable assigned to the loan dictionary, loan
#           utilizes get() in order to obtain the values for keys future_value, hurdle_rate, and remaining_months
#           calculates the present value of the loan in the dictionary using the previously declared variable, present_value with value equals the present value formula
#           prints to output using f-string, the result of present value calculation = the fair value is $861.77
#           returns the calculation result making assignment to variable an option....

# adds key:value pair of 'hurdle_rate': 0.20 into dictionary, thus adding discount rate as a characteristic of the overall loan parmeters
loan['hurdle_rate'] = annual_discount_rate


def present_value_fxn_b(loan):
    future_value = loan.get('future_value')
    hurdle_rate = loan.get('hurdle_rate')
    remaining_months = loan.get('remaining_months')
    present_value_calc = present_value
    print(
        f'directly from the function - the fair value is ${present_value_calc:.2f}')
    return present_value_calc


# define a ONE parameter function, present_value_fxn_c() that-
#           accepts the variable assigned to the loan dictionary, loan
#           utilizes get() in order to obtain the values for keys future_value, hurdle_rate, and remaining_months
#           calculates, within the body of the function, the present value of the loan in the dictionary
#           prints to output using f-string, the result of present value calculation = the fair value is $861.77
#           returns the calculation result making assignment to variable an option....

def present_value_fxn_c(loan):
    future_value = loan.get('future_value')
    hurdle_rate = loan.get('hurdle_rate')
    remaining_months = loan.get('remaining_months')
    # moving the 'monthly precision' present value formula into the body of the function
    present_value_calc = future_value / \
        (1 + hurdle_rate / 12) ** remaining_months
    print(
        f'directly from the function - the fair value is ${present_value_calc:.2f}')
    return present_value_calc


# use the alternate approaches, i.e. use/'call' the functions
# THREE parameter function call
# value returned out of the function is assigned to variable present_value
present_value = present_value_fxn(
    future_value, annual_discount_rate, remaining_months)
# outside of function, prints to output using f-string, the result of present_value_fxn calculations = the fair value is $861.77
print(f'function call print - the fair value is ${present_value:.2f}')

# TWO parameter function call
# value returned out of the function is assigned to variable present_value
present_value = present_value_fxn_a(loan, annual_discount_rate)
# outside of function, prints to output using f-string, the result of present_value_fxn_a calculations = the fair value is $861.77
print(f'a_function call print - the fair value is ${present_value:.2f}')

#  ONE parameter function call operation - accesses the present value formula via the previously declared variable present_value
# value returned out of the function is assigned to variable present_value
present_value = present_value_fxn_b(loan)
# outside of function, prints to output using f-string, the result of present_value_fxn_b calculations = the fair value is $861.77
print(f'b_function call print - the fair value is ${present_value:.2f}')

#  ONE parameter function call operation - has the formula for present value within body of function
# value returned out of the function is assigned to variable present_value
present_value = present_value_fxn_c(loan)
# outside of function, prints to output using f-string, the result of present_value_fxn_c calculations = the fair value is $861.77
print(f'c_function call print - the fair value is ${present_value:.2f}')


# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

# primary or main conditional if that compares present_value to the result (i.e. value) when value for key 'loan_price" is accessed in dictionary.
if present_value >= loan['loan_price']:
    # action to be performed if True
    print('the loan is worth at least the cost to buy it')
    # if True, a nested if/else conditional that provides specific value to consider when determining 'fair value'
    if present_value > loan['loan_price']:
        print(f'the estimated value of the loan is ${present_value:.2f}')
    else:
        print('the estimated value of the loan is equal to its cost')
else:                                                                        # action to be performed if False
    print('the loan is too expensive and not worth the price')

"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}
# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#                HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months
#    The function should return the `present_value` for the loan.

# define a function, present_value_fxn() that-
#           accepts the parameters/argumets using three variables- future_value, hurdle_rate, and remaining_months ; values as assigned per notation above
#           calculates the present value of the loan in the dictionary using monthly precision present value formula
#           returns the present value calculation and assigns within function to present_value


def a_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / \
        (1 + annual_discount_rate/12) ** remaining_months
    return present_value


# define an alternate function, b_present_value() that-
#           accepts two parameters- values assigned to the keys of entire loan dictionary new_loan and annual_discount_rate; value as assigned per notation above
#           utilizes get() in order to obtain the values for keys future_value and remaining_months
#           calculates the present value of the loan in the dictionary
#           prints to output using f-string, the result of present value calculation = the fair value is 861.77
#           returns the calculation result making assignment to variable an option....

def b_present_value(new_loan, annual_discount_rate):
    future_value = new_loan.get('future_value')
    remaining_months = new_loan.get('remaining_months')
    present_value = future_value / \
        (1 + annual_discount_rate/12) ** remaining_months
    return present_value


# define an alternate function, b_present_value() that-
#           accepts a single parameters- entire loan dictionary new_loan
#           utilizes get() in order to obtain the values for keys future_value, annual_discount_rate, and remaining_months
#           calculates the present value of the loan in the dictionary
#           prints to output using f-string, the result of present value calculation = the fair value is 861.77
#           returns the calculation result making assignment to variable an option....


def c_present_value(new_loan):
    future_value = new_loan.get('future_value')
    remaining_months = new_loan.get('remaining_months')
    annual_discount_rate = new_loan.get('annual_discount_rate')
    present_value = future_value / \
        (1 + annual_discount_rate/12) ** remaining_months
    return present_value

# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.

# assigning values to variables for proscribed THREE parameters; future_value, remaining_months, and annual_discount_rate


# variable annual_discount_rate declared with provided value
annual_discount_rate = 0.20
# variable future_value declared and assigned value via get() function on library new_loan
future_value = new_loan.get('future_value')
# variable remaining_months declared and assigned value via get() function on library new_loan
remaining_months = new_loan.get('remaining_months')

# using 'DRY' principle - 'use the function' = 'call the function' , using the function proscribed by instructions = a_present_value(future_value, remaining_months, annual_discount_rate)
# set variable, present_value_a = the return of the caled THREE paramter/argument function written above
present_value_a = a_present_value(
    future_value, remaining_months, annual_discount_rate)
# print to output th value of present_value obtained from calling the three paramter/argument function written above
print(
    f'with 3 parameter function, the present value is ${present_value_a:.2f}')


#        using the first alternate version of function = b_present_value(new_loan, annual_discount_rate)
# set variable, present_value_b = the return of the called TWO parameter/argument function written above
present_value_b = b_present_value(new_loan, annual_discount_rate)
# print to output the value of present_value_b obtained from calling the TWO paramter/argument function written above
print(
    f'with 2 parameter function, the present value is ${present_value_b:.2f}')


#        using the second alternate version of function = c_present_value(new_loan)
# generate new key:value pair in dictionay utilizing variable annual_discount_rate with provided value
new_loan['annual_discount_rate'] = annual_discount_rate

# set variable, present_value_c = the return of the called SINGLE parameter/argument function written above
present_value_c = c_present_value(new_loan)
# print to output th value of present_value_c obtained from calling the ONE paramter/argument function written above
print(
    f'with 1 parameter function, the present value is ${present_value_c:.2f}')


"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
    b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# @TODO: Create an empty list called `inexpensive_loans`
inexpensive_loans = []

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for cheapies in loans:
    if cheapies['loan_price'] <= 500:
        inexpensive_loans.append(cheapies)

# @TODO: Print the `inexpensive_loans` list
print(inexpensive_loans)

"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""
# Set the output header
header = ["loan_price", "remaining_months",             # header is a ~ simple list of string values
          "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")             # generate object path

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
# YOUR CODE HERE!

# opening the output path in 'read" AND 'writeable' mode
# ‘r+’	Read+Write - open a file for both reading and writing
# newline... for 'special' per textbook/class canvas
# delimeter=',' is specified for this exercise, but unnecessary as is default.
with open(output_path, 'r+', newline='') as csvfile:
    # designating/making 'writer'
    csvwriter = csv.writer(csvfile, delimiter=',')
    # using writer to write header 'row'
    csvwriter.writerow(header)
    # iterate through the list of inexpensive loans temp assign values to variable 'row'
    for row in inexpensive_loans:
        # at each pass through, i.e. iteration writer adds/writes data values to rows in csv file
        csvwriter.writerow(row.values())
