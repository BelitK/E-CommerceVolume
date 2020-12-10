import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

data = pd.read_excel("ecomretailfixed.xls")
date = data["observation_date"]
ecomsa = data["ECOMSA"]


plt.plot(date)

print(data,ecomsa)