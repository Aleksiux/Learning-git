import pandas as pd
import numpy as np
from collections import ChainMap

top_left = pd.read_csv('top1-25-1.csv')
top_right = pd.read_csv('top1-25-2.csv')
bottom_left = pd.read_csv('top26-50-1.csv')
bottom_right = pd.read_csv('top26-50-2.csv')
data_right_bottom = bottom_right.reset_index()
data_right_bottom.drop(columns='index', inplace=True)
merged_data_bottom = pd.concat([bottom_left, data_right_bottom], axis=1)
merged_data_top = pd.merge(top_left, top_right, on=['Track.Name', 'Popularity'])
concate_data = pd.concat([merged_data_top, merged_data_bottom])
concate_data.index = concate_data.index + 1
grouped_by_genre = concate_data.groupby(['Genre'])
bool_energy = grouped_by_genre.count()
# print(bool_energy[bool_energy['Energy'] > 3]['Energy'])

list_of_dict = []
pop_group = grouped_by_genre.mean()['Popularity']
# print(pop_group.idxmax(), pop_group.max())
# print(pop_group.idxmin(), pop_group.min())
# popularity = {'Genre': 'val'}
# for index, row in grouped_by_genre['Popularity']:
#     result = row.sum() / row.describe().loc['count']
#     popularity = {index: result}
#     list_of_dict.append(popularity)
# pop_dict = dict(ChainMap(*list_of_dict))
items = concate_data.columns.tolist()[3:]
# list_of_i = []
new_group = grouped_by_genre.mean()[items].max()
new_group_idx = grouped_by_genre.mean()[items].idxmax()
# table1 = pd.DataFrame(new_group)
# table2 = pd.DataFrame(new_group_idx)
table_merged = pd.DataFrame([items, new_group, new_group],
                            ['Indicator', 'Genre', 'Value']).transpose()
# table_merged.reset_index(inplace=True)
# table_merged.columns = ['Indicator', 'Genre', 'Value']
# print(table_merged)
list_of_i=[]
for i in items:
    for index, row in grouped_by_genre[i]:
        result = row.max() / row.describe().loc['count']
        popularity = {i: {index: result}}
        list_of_i.append(popularity)


# print(f'{max(pop_dict, key=pop_dict.get)} {max(pop_dict.values())}')
# print(f'{min(pop_dict, key=pop_dict.get)} {min(pop_dict.values())}')
# print(concate_data[concate_data.isnull().any(axis=1)].to_string())

# concate_data['Genre'].fillna('pop', inplace=True)
# print(concate_data['Genre'])
concate_data['Popularity'].fillna(concate_data['Popularity'].mean(), inplace=True)
print(concate_data.to_string())




# --------------------------- STASIO --------------------#


# import pandas as pd
#
# # 1 uzduotis
# top_left = pd.read_csv('top1-25-1.csv')
# top_right = pd.read_csv('top1-25-2.csv')
# bottom_left = pd.read_csv('top26-50-1.csv')
# bottom_right = pd.read_csv('top26-50-2.csv')
# data_bottom = pd.concat([bottom_left, bottom_right], axis=1)
# data_top = pd.merge(top_left, top_right, on=['Track.Name', 'Popularity'])
# data = pd.concat([data_top, data_bottom], sort=False)
#
#
# # 2 uzduotis
# data['#'] = list(range(1, 51))
# data.set_index('#', inplace=True)
# # print(data.to_string())
# # 3 uzduotis
# grouped = data.groupby('Genre')
#
# # 4 uzduotis
# newdf = grouped.count()
# # print(newdf[newdf['Energy']>3]['Energy'])
# # 5 uzduotis
# most_popular_genre = grouped.mean()['Popularity'].idxmax()
# most_popular_score = grouped.mean()['Popularity'].max()
# least_popular_genre = grouped.mean()['Popularity'].idxmin()
# least_popular_score = grouped.mean()['Popularity'].min()
# # print(most_popular_genre, most_popular_score)
# # print(least_popular_genre, least_popular_score)
# # 6 uzduotis
# indikatoriai = data.columns.tolist()[3:]
# zanrai = grouped.mean()[indikatoriai].idxmax()
# skaiciai = grouped.mean()[indikatoriai].max()
# result = pd.DataFrame([indikatoriai, zanrai, skaiciai],
#                       ['Indikatorius', 'Žanras', 'Balai']).transpose()
# # print(result.to_string())
# # 7 uzduotis
# print(data.info())
# with_NaN = data[data['Genre'].isnull() | data['Popularity'].isnull()]
# print(with_NaN.to_string())
#
# # 8 uzduotis
# data['Genre'].fillna('poop', inplace=True)
#
# # 9 uzduotis
# data['Popularity'].fillna(data['Popularity'].mean(), inplace=True)
# print(data.to_string())
