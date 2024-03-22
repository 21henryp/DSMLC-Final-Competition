import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sc
import numpy as np

# -------------------------------------------------------------

# Subsets creation
dataset = "./dataset.csv"
df = pd.read_csv(dataset)

# Data organized by Year
df_by_years = {}
for i in range(2000,2020):
  df_by_years.setdefault(i, df.query("Year == " + str(i)))

# Compute average/sample mean of all countries by each year for every category
x = 0                                                                                 # Categories
mean_categories_by_years = [[0 for z in range(20)] for z in range(2)]                 # Store mean values of 7.1.1 and 12.2.2 of all countries by years
var_categories_by_years = [[0 for z in range(20)] for z in range(2)]                  # Store variance values of 7.1.1 and 12.2.2 of all countries by years
sd_categories_by_years = [[0 for z in range(20)] for z in range(2)]                   # Store standard deviation values of 7.1.1 and 12.2.2 of all countries by years
n_obs = len(df)/20                                                                    # Store number of observations
z = 0
for i in df.columns:
  if (z < 3):
    z += 1
    continue
  x += 1
  if (x == 3):
    break
  y = 0                                                                               # Years
  for j in range(2000,2020):
    y += 1
    mean_categories_by_years[x-1][y-1] = df_by_years.get(j)[i].mean(numeric_only=True)
    var_categories_by_years[x-1][y-1] = df_by_years.get(j)[i].var(numeric_only=True)
    sd_categories_by_years[x-1][y-1] = df_by_years.get(j)[i].std(numeric_only=True)

# Contain years from 2000-2019
years = [year for year in range(2000,2020)]

df = pd.DataFrame(mean_categories_by_years, index=["7.1.1", "12.2.2"], columns=years)
ratios_mean = []
# Compute ratio of mean from each category for every year
# ratio = sample mean 7.1.1 / sample mean 12.2.2
for i in years:
  mean_7 = df[i].loc["7.1.1"]
  mean_12 = df[i].loc["12.2.2"]
  ratios_mean.append(df[i].loc["7.1.1"]/df[i].loc["12.2.2"])
  
# T-test computing t-values and p-values of 2 sample means using scipy
obs = pd.DataFrame(sc.ttest_ind_from_stats(mean1=df.iloc[0], mean2=df.iloc[1], 
                                           std1=var_categories_by_years[0], std2=var_categories_by_years[1], 
                                           nobs1=n_obs, nobs2=n_obs, equal_var=False),
                                           index=["T-value", "P-value"], columns=years)

df = pd.DataFrame(ratios_mean, index=years, columns=["ratio"])
print(obs)

stderr = []
for i in range(20):
  stderr.append(np.sqrt((var_categories_by_years[0][i]/n_obs) + (var_categories_by_years[1][i]/n_obs)))

t_value = []
for i in range(20):
  t_value.append((mean_categories_by_years[0][i] - mean_categories_by_years[1][i]) / stderr[i])
print(pd.DataFrame(t_value))

dfreedom = n_obs + n_obs - 2
print(mean_categories_by_years)

# print(sc.linregress(years, mean_categories_by_years[0]))
# pd.set_option("display.max_rows", 200)

# plt.scatter(years,mean_categories_by_years[0])
# plt.xticks(years)
# plt.xlabel("Year")
# plt.ylabel(str(df.columns[3]))
# plt.grid(visible=True)
# plt.show()