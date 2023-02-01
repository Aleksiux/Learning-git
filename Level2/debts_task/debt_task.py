from csv import writer


class Debts:
    def __init__(self, amount, period, interest):
        self.amount = amount
        self.period = period
        self.interest = interest

    def __str__(self):
        return f'Amount: {self.amount} | Period of time {self.period} months | Debt interest: {self.interest}%'

    def debt_info(self, sum_of_interest, payable_amount):
        return f'Amount: {self.amount} | ' \
               f'Period of time: {self.period} ' \
               f'years | Debt interest: {self.interest}%\n' \
               f'Sum of interest: {sum_of_interest:.2f}%\n' \
               f'Interest payable amount: {payable_amount:.2f}' \



def append_dict_as_row(file_name, list_of_elem):
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)