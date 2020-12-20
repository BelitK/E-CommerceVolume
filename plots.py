import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

# american ecommerce data
dataset_A = pd.read_excel("ecomretailfixed.xls")
dataset_turkey = pd.read_excel("TurkeyData3.xlsx")

date_A = dataset_A["observation_date"]
ecomsa_A = dataset_A["ECOMSA"]
to_tl = []
for price in ecomsa_A:
    to_tl.append(price * 7.84)

# Türkiye ecommerse data
date_E = dataset_turkey["observation_date"]
ecomsa_E = dataset_turkey["ECOMSA"]


plt.style.use('seaborn-darkgrid')
#plt.plot(date_A,to_tl,label="Amerika",marker=3)
plt.plot(date_A,ecomsa_A,label="Amerika",marker=3)
plt.plot(date_E,ecomsa_E,label="Türkiye",marker=2)

plt.title("Türkiye ve Amerika E-Ticaret Piyasa Hacmi Karşılaştırması (TRY)")
plt.xlabel("Tarihler")
plt.ylabel("Milyar (TRY)")

plt.legend()
plt.show()
#plt.savefig('Matplotlib_save_plot.png')

turkey_2018 = dataset_turkey["ECOMSA"][28:32]
total_2018=0
for price in turkey_2018:
    total_2018 += price


turkey_2019 = dataset_turkey["ECOMSA"][32:36]
total_2019=0
for price2 in turkey_2019:
    total_2019 += price2
df = pd.DataFrame([[total_2018,2018],[total_2019,2019]],columns=list("AB"))




labels = df["B"]
values = df["A"]


fig = go.Figure(data=[go.Pie(labels=labels, values=values,title="Türkiye 2018-2019 E-Ticaret Hacmi\b", textinfo='label+percent',
                             insidetextorientation='radial'
                            )])
fig.show()
