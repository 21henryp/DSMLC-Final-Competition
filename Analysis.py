import scipy.stats as sc
import pandas as pd
import matplotlib.pyplot as plt
# -------------------------------------------------------------

# Subsets creation
dataset = "./dataset.csv"
df = pd.read_csv(dataset)
df = df.drop(df.columns[0], axis=1)

# Data organized by Year
df_by_years = {}
for i in range(2000,2020):
  df_by_years.setdefault(i, df.query("Year == " + str(i)))

# Compute average of all countries by each year for every category
x = 0 # Categories
mean_categories_by_years = [[0 for z in range(20)] for z in range(21)]
z = 0
for i in df.columns:
  if (z < 3):
    z += 1
    continue
  x += 1
  y = 0 # Years
  for j in range(2000,2020):
    y += 1
    mean_categories_by_years[x-1][y-1] = df_by_years.get(j)[i].mean(numeric_only=True)

years = [year for year in range(2000,2020)]
# for i in range(x):
#   print(sc.linregress(years, mean_categories_by_years[i]))

# print(mean_categories_by_years[0])
# print(sc.linregress(years, mean_categories_by_years[0]))
plt.scatter(years,mean_categories_by_years[0])
plt.xticks(years)
plt.xlabel("Year")
plt.ylabel(str(df.columns[3]))
plt.grid(visible=True)
plt.show()