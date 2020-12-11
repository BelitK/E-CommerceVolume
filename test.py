import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()
dataset = pd.read_excel("ecomretailfixed.xls")
date = dataset["observation_date"]
ecomsa = dataset["ECOMSA"]
sns.displot(dataset)
plt.show()
# sns.barplot(x=date,y=ecomsa)
# plt.show()
plt.savefig('saved_figure.jpg')
print(date)