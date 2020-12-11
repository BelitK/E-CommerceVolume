
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


#american ecommerce data
dataset_A = pd.read_excel("ecomretailfixed.xls")
dataset_metal = pd.read_excel("External_Data.xls")
date_A = dataset_A["observation_date"]
ecomsa_A = dataset_A["ECOMSA"]
#europe ecommerse data
dataset_E = pd.read_csv("isoc_ec_eseln2.tsv",sep='\t')
date_E = dataset_A["observation_date"]
ecomsa_E = dataset_A["ECOMSA"]


# plt.plot(date_A,ecomsa_A)
# plt.show()
plt.plot(date_E,ecomsa_E)
plt.show()
print(dataset_metal)


