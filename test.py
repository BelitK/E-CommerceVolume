import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# american ecommerce data
dataset_A = pd.read_excel("ecomretailfixed.xls")
dataset_turkey = pd.read_excel("TurkeyData.xlsx")

date_A = dataset_A["observation_date"]
ecomsa_A = dataset_A["ECOMSA"]
to_tl = []
for price in ecomsa_A:
    to_tl.append(price * 7.84)

# europe ecommerse data
date_E = dataset_turkey["observation_date"]
ecomsa_E = dataset_turkey["ECOMSA"]
print(ecomsa_E)

plt.plot(date_A,to_tl)
plt.plot(date_E,ecomsa_E)
plt.title("E-commerce between usa and turkey (TRY)")
plt.xlabel("Dates")
plt.ylabel("Billions")
plt.show()
plt.savefig('Matplotlib_save_plot.png')
print(dataset_turkey)
print(to_tl)