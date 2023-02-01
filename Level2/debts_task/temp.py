import debt_task
import pandas as pd
import numpy as np

df = pd.DataFrame()
df_cols = ['Amount returning part', 'Amount left', 'Accrued interest', 'Total amount due']
if __name__ == '__main__':
    while True:
        user = input(
            "Choose what you want to do: \n1. Add debt info \n2. Show debt info\n3. Show debt schedule\n4. End "
            "program.:\n")
        if user == '1':
            if df.empty:
                amount_of_debt = int(input('Add amount of debt '))
                interest_of_debt = int(input('Add interest of debt '))
                period_of_debt = int(input('Add period of debt '))
                df = pd.DataFrame(columns=[df_cols], index=range(1, period_of_debt))
                # df.set_index(period_of_debt)
            else:
                amount_of_debt = int(input('Add amount of debt you want to return'))
                interest_of_debt = debt.interest
                period_of_debt = debt.period
                df.loc[len(df.index)] = [amount_of_debt, interest_of_debt, period_of_debt]
                # interest_of_debt = int(input('Add interest of debt '))
                # period_of_debt = int(input('Add period of debt '))
            debt = debt_task.Debts(amount_of_debt, period_of_debt, interest_of_debt)
        elif user == '2':
            sum_of_interest = (debt.amount * debt.interest / 100) / 12
            payable_amount = (debt.amount / debt.period) + sum_of_interest
            print(debt.debt_info(sum_of_interest, payable_amount))
        elif user == '3':
            print(df)
        elif user == '4':
            break
        else:
            print("You need to choose correctly from 1 - 4")

# table_merged = pd.DataFrame([items, new_group, new_group],
#                             ['Indicator', 'Genre', 'Value']).transpose()
