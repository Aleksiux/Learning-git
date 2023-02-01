import pandas as pd
import numpy as np
from xlsxwriter import Workbook
from sqlalchemy import create_engine

# url = 'https://work.studentnews.eu/s/3695/75547-European-countries-the-table-language-population-capital-currency' \
#       '-phone-code-internet-code.htm '
# data = pd.read_html(url)

# -------------------SQL------------------------
# engine = create_engine('sqlite:///data.db')
# data[1].to_sql('countries', con=engine, index=False)
# data_sql = pd.read_sql('countries', con=engine)
# print(data_sql.to_string())
#
# -------------------CSV------------------------
# data[1].to_csv('countries.csv', index=False)
# data_csv = pd.read_csv('countries.csv')
# print(data_csv.to_string())

# -------------------EXL------------------------
# data[1].to_excel('countries.xlsx', engine='xlsxwriter')
# data_excel = pd.read_excel('countries.xlsx')
# print(data_excel.to_string())


# -------------------FIRE------------------------
fire = pd.read_csv('fire.csv')

# -----------4.-----------
# print(len(fire['cause'].unique()))
# -----------5.-----------
# print(fire['cause'].value_counts())
# -----------6.-----------
# print(fire['year'].value_counts().idxmax())
# -----------7.-----------
# print((fire['deaths'] > 0).sum())
# -----------8.-----------
# group_by_year = fire.sort_values(['year'], ascending=False)
# print(group_by_year.to_string())
# -----------9.-----------
# month = {'January': 1,
#          'February': 2,
#          'March': 3,
#          'April': 4,
#          'May': 5,
#          'June': 6,
#          'July': 7,
#          'August': 8,
#          'September': 9,
#          'October': 10,
#          'November': 11,
#          'December': 12}
#


# def change_month(month):
#     men = {1: 'January',
#              2: 'February',
#              3: 'March',
#              4: 'April',
#              5: 'May',
#              6: 'June',
#              7: 'July',
#              8: 'August',
#              9: 'September',
#              10: 'October',
#              11: 'November',
#              12: 'December'}
#     for key, val in men.items():
#         if month == val:
#             return key
#
#
# fire['month'] = fire['month'].apply(change_month)
# print(fire.to_string())
# fire.replace({'month': month}, inplace=True)
# print(fire.to_string())
# ----------10.-----------
# url = 'https://lt.wikipedia.org/wiki/S%C4%85ra%C5%A1as:Lietuvos_miestai_pagal_gyventojus'
# data = pd.read_html(url, encoding='utf-8')
# df = pd.DataFrame(data[0])
# df.set_index('Miestas', inplace=True)
# df.columns = df.columns.str.replace('\xa0m.', '')
# to_int = df.columns.tolist()[1:-1]
# cities = df.iloc[:, 1:-1]
# cities[to_int] = cities[to_int].astype(str)
# for i in to_int:
#     cities[i] = cities[i].str.extract(pat='(\d+)', expand=False)
# cities[to_int] = cities[to_int].fillna(0).astype(np.int64)
# print(cities.info())
