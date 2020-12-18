import pandas as pd

# create dataset
df = pd.DataFrame({'dates': [2011,2012,2013,2014,2015,2016,2017,2018,2019],
                   'score': [45104.57, 60265.08, 69114.95, 82732.12, 110673, 137252, 197325.5, 271517.7, 368394.7]})

import matplotlib.pyplot as plt

plt.scatter(df.dates, df.score)
plt.title('Hours studied vs. Exam Score')
plt.xlabel('Hours')
plt.ylabel('Score')
plt.show()

df.boxplot(column=['score'])
import statsmodels.api as sm

#define response variable
y = df['score']

#define explanatory variable
x = df[['dates']]

#add constant to predictor variables
x = sm.add_constant(x)

#fit linear regression model
model = sm.OLS(y, x).fit()

#view model summary
print(model.summary())
#define figure size
fig = plt.figure(figsize=(12,8))

#produce residual plots
fig = sm.graphics.plot_regress_exog(model, 'dates', fig=fig)

#define residuals
res = model.resid

#create Q-Q plot
fig = sm.qqplot(res, fit=True, line="45")
plt.show()