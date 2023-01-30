import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

mpg = sns.load_dataset('mpg')
sns.set_style('darkgrid')
print(mpg.head().to_string())
# sns.displot(mpg['acceleration'], kde=False)
# sns.displot(mpg['displacement'])
# sns.countplot(x=mpg['cylinders'], palette='inferno')
# sns.countplot(x=mpg['model_year'], palette='Set2')
# sns.countplot(data=mpg, x='origin')
# sns.barplot(data=mpg, x='origin', y='displacement', ci=False)
# sns.scatterplot(data=mpg, x='displacement', y='acceleration', hue='origin', size='cylinders')
# sns.pairplot(data=mpg, hue='origin')
# sns.catplot(data=mpg,x='origin', y='mpg', kind='box')
# corel = mpg.corr()
# sns.heatmap(corel, annot=True, cmap="crest")
# grid = sns.FacetGrid(mpg, col='origin')
# grid.map(sns.scatterplot, 'acceleration', 'cylinders')
plt.show()
