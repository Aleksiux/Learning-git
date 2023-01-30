import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
sns.set_style('dark')
sns.barplot(x='sex', y='total_bill', data=tips, hue='day', estimator=sum, ci=False, palette='inferno')
sns.despine()

plt.show()
