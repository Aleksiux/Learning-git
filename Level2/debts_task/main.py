import debt_task
import pandas as pd
import numpy as np

df = pd.DataFrame(columns=
                  ['Months', 'Returning', 'Left', 'Interest',
                   'Total'])

if __name__ == '__main__':
    list_of_payload = []
    list_of_interest = []
    list_of_total = []
    list_of_returning = []
    while True:
        user = input(
            "Choose what you want to do: \n1. Add debt info \n2. Show debt info\n3. Show debt schedule\n4. End "
            "program.:\n")
        if user == '1':
            amount_of_debt = int(input('Add amount of debt '))
            interest_of_debt = int(input('Add interest of debt '))
            period_of_debt = int(input('Add period of debt '))
            debt = debt_task.Debts(amount_of_debt, period_of_debt, interest_of_debt)
            part_of_amount = amount_of_debt / period_of_debt
            number = amount_of_debt
            while True:
                if number > 0:
                    interest_cal = (number * debt.interest / 100) / 12
                    list_of_returning.append(round(part_of_amount, 2))
                    total = part_of_amount + interest_cal
                    number = number - part_of_amount
                    list_of_interest.append(round(interest_cal, 2))
                    list_of_payload.append(int(number))
                    list_of_total.append(round(total, 2))
                else:
                    break
            df = df.assign(Months=range(1, int(period_of_debt + 1)), Returning=list_of_returning, Left=list_of_payload,
                           Interest=list_of_interest,
                           Total=list_of_total)
            df.set_index('Months', inplace=True)
        elif user == '2':
            sum_of_interest = (debt.amount * debt.interest / 100) / 12
            payable_amount = (debt.amount / debt.period) + sum_of_interest
            print(debt.debt_info(sum_of_interest, payable_amount))
        elif user == '3':
            df.to_csv('table.csv')
            csv_total_last_row = ['Total', debt.amount, '', sum(list_of_interest), sum(list_of_total)]
            debt_task.append_dict_as_row('table.csv', csv_total_last_row)
            open_csv = pd.read_csv('table.csv').fillna(' ')
            open_csv = open_csv.set_index('Months')
            print(open_csv)
        elif user == '4':
            break
        else:
            print("You need to choose correctly from 1 - 4")
