"""the max loan size filter will filter the bank list by comparing the loan applicant's loan amount to the banks' maximum loan size"""


def filter_max_loan_size(loan_amount, bank_list):
    loan_size_approval_list = []

    for bank in bank_list:
        if loan_amount <= int(bank[1]):
            loan_size_approval_list.append(bank)
    return loan_size_approval_list
