import pandas as pd
import numpy as np

top_left = pd.read_csv('top1-25-1.csv')
top_right = pd.read_csv('top1-25-2.csv')
bottom_left = pd.read_csv('top26-50-1.csv')
bottom_right = pd.read_csv('top26-50-2.csv')

merged_data = pd.concat([bottom_left, bottom_right])
merged_data2 = pd.concat([top_left, top_right])
concate_data = pd.concat([merged_data2, merged_data])
print(concate_data)
