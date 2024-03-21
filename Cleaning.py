import pandas as pd
import numpy as np
import re
# -------------------------------------------------------------
dataset = "./DSMLC Final Competition 2024 Dataset.xlsx"
df = pd.read_excel(dataset)

# drop dulicates
df = df.drop_duplicates()

# convert file type to csv
dataset = "./dataset.csv"
df.to_csv(dataset)
df = pd.read_csv(dataset)

# Import population.csv
dataset2 = "./population.csv"
popdf = pd.read_csv(dataset2)

# dataframe with countries (on its own) only
df = df.dropna(subset="Code")
df = df.drop(df.columns[0], axis=1)
# get rid of "()" along with its annotations
df["Country"] = df["Country"].replace(regex=r'(.+?)\s\(.*\)', value=r'\1')
# get rid of column titles' annotations
colName = []
for i in df.columns:
  colName.append(re.split(r"\s", i)[0])

df.columns = colName

# duplicates = {}
# list = ['.A', '.a', '.b', '.c','.d','.e','.f','.g','.h']
# index = 0
# for i in colName:
#   if i in duplicates:
#     df.columns.values[index-1] = duplicates.setdefault(i, i) + list[::-1].pop()
#     list.remove(list[0])
#     df.columns.values[index] = duplicates.setdefault(i, i) + list[::-1].pop()
#   else:
#     df.columns.values[index] = duplicates.setdefault(i, i)
#   index += 1

# dataframe with sdg 7.1.1 and 12.2.2 only
df = df.drop(df.columns[15:], axis=1)
df = df.drop(df.columns[4:14], axis=1)

# Remove for missing data
arr = np.where(df.isnull())
for i,j in zip(arr[0], arr[1]):
  df = df.drop(i, axis=0)

# Remove data with value 0 from sdg 12.2.2
arr = df.query("`12.2.2` == 0")["Country"].unique()
for i in arr:
  df.drop(df[df["Country"] == i].index, inplace=True)

# Remove countries that aren't ranged from 2000-2019
unique_countries = df['Country'].unique()
arr = []
for country in unique_countries:
  years_for_country = df[df['Country'] == country]['Year'].unique()
  if len(years_for_country) != 20 or min(years_for_country) != 2000 or max(years_for_country) != 2019:
    arr.append(country)

for i in arr:
  df.drop(df[df["Country"] == i].index, inplace=True)

df.drop(df[df["Country"] == "World"].index, inplace=True)

# Rename Entity to Country
popdf.columns.values[0] = "Country"

# Merge population to current df
df2_filtered = popdf[popdf["Country"].isin(unique_countries)]
df2_filtered = df2_filtered[(df2_filtered["Year"] >= 2000) & (df2_filtered["Year"] <= 2019)]
df = pd.merge(df, df2_filtered[["Country", "Year", "Population (historical estimates)"]], on=["Country", "Year"], how="left")

# Renamed column
df.columns.values[5] = re.split(r"\s", df.columns[5])[0]

print(df)

df.to_csv(dataset, index=False)
