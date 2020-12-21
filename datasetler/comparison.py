import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
dataset_turkey = pd.read_excel("TurkeyData3.xls",header=0)
# #print(dataset_turkey.head(10))

labels = ['Q1', 'Q2', 'Q3']
men_means = dataset_turkey['ECOMSA'][-3:]
women_means = dataset_turkey["ECOMSA"][-7:-4]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects2 = ax.bar(x + width/2, men_means, width, label='2020')
rects1 = ax.bar(x - width/2, women_means, width, label='2019')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('E-ticaret hacim')
ax.set_title('2019-2020 Karşılaştırma')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()