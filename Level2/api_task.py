import datetime
import json

import requests


def get_rate(from_currency, to_currency):
    amount = 46290
    dict_currency = requests.get(f'https://api.frankfurter.app/currencies')
    currency = json.loads(dict_currency.text)
    params = {
        ('amount', amount),
        ('from', from_currency),
        ('to', to_currency),
    }
    if from_currency in currency and to_currency in currency:
        request = requests.get(f'https://api.frankfurter.app/latest?', params=params)
        dictionary = json.loads(request.text)
        print(f"{amount} {from_currency} is {dictionary['rates'][to_currency]} {to_currency}")
    else:
        print(f"There is no such a currency. {from_currency} or {to_currency}")


# get_rate('USD', 'EUR')


def currency_pair_analysis(from_currency, to_currency, from_date, to_date):
    amount = 1
    params = {
        ('amount', amount),
        ('from', from_currency),
        ('to', to_currency),
    }

    request = requests.get(f"https://api.frankfurter.app/{from_date}..{to_date}", params=params)
    dictionary = json.loads(request.text)
    print(f'In currency group {from_currency}-{to_currency}, period from {from_date} to {to_date}')
    list_of_items = []
    for key, val in dictionary['rates'].items():
        result = key, val[to_currency]
        list_of_items.append(result)
    min_result = min(list_of_items, key=lambda x: x[1])
    max_result = max(list_of_items, key=lambda x: x[1])
    print(f'Lowest currency rate was {min_result[0]}, {min_result[1]}')
    print(f'Highest currency rate was {max_result[0]}, {max_result[1]}')


# currency_pair_analysis('EUR', 'GBP', '2023-01-01', '2023-01-16')


def horoscope(sign):
    params = (
        ('sign', sign),
        ('day', 'tomorrow'),
    )
    request = requests.post('https://aztro.sameerkumar.website/', params=params)
    dictionary = request.json()
    print(
        f"Sign - {sign} | Todays date: {dictionary['current_date']} "
        f"| What's waiting for you: \n{dictionary['description']}")

# horoscope('Virgo')
