import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from task_db import Users, Bank, Account

engine = create_engine('sqlite:///banks.db')
Session = sessionmaker(bind=engine)
session = Session()


def check_all_user():
    users = session.query(Users)
    for i in users:
        print(i)


while True:
    choise = input("Choose what you want to do:\n1.Add user\n2.Check user account\n3.Check user account info\n4.Add "
                   "money or remove money from account.\n5.Show all users.\n")
    if choise == '1':
        name = input("Write user name:")
        surname = input("Write surname name:")
        personal_code = input("Write personal code name:")
        phone_number = input("Write phone number name:")
        user_rel = Users(name, surname, personal_code, phone_number)
        bank_name = input("Write bank name:")
        bank_address = input("Write bank address:")
        bank_code = input("Write bank code:")
        swift_code = input("Write swift code:")
        bank_rel = Bank(bank_name, bank_address, bank_code, swift_code)
        account_number = input("Write account number")
        balance = input("Write balance")
        account = Account(account_number, balance)
        account.users.append(user_rel)
        account.bank.append(bank_rel)
        session.add(account)
        session.commit()
    elif choise == '2':
        check_all_user()
    elif choise == '3':
        account = session.query(Account).get(1)
        for bank in account.bank:
            print(bank.name, bank.accounts)
