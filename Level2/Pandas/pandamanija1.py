import pandas as pd
import numpy as np

dfas = pd.read_csv('test.csv', encoding='utf-8')
print(dfas[:5])
df = dfas.set_index('Miestas')

print(df.loc['Marijampolė']["1923"])
print('-' * 100)
print(df["1897"][:5])
print('-' * 100)
print(df[['2019', '1970', '1923']][:10])
print('-' * 100)
print(df.shape)
print('-' * 100)
df['nr'] = range(1, df.shape[0] + 1)
print(df)
print('-' * 100)
print(df[29:39])
print('-' * 100)
df.drop('nr', axis=1, inplace=True)
print(df)
print('-' * 100)
print(df[df['1959'] <= 0])
print('-' * 100)
bool_city = df['1897'] > df['2019']
print(df[bool_city])
print('-' * 100)
bool_city_more = df['2011'] < df['2019']
print(df[bool_city_more][['2019', '2011']])
print('-' * 100)
bool_city_dec = (df['2019'] < df['2011']) & (df['2001'] < df['1989']) & (df['1979'] < df['1970']) & (
        df['1959'] < df['1923']) & (df['1923'] < df['1897'])
print(df[bool_city_dec])
print('-' * 100)


result = ((df['2019'] * 100) / df['1989']) - 100

print(f'{result.idxmax()} {int(result.max())}%')
print(f'{result.idxmin()} {int(result.min())}%')
print('-' * 100)
# print(df.reset_index())
