import pandas as pd
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

# dataframe with countries (on its own) only
df = df.dropna(subset="Code")
df = df.drop(df.columns[0], axis=1)
# get rid of "()" along with its annotations
df["Country"] = df["Country"].replace(regex=r'(.+?)\s\(.*\)', value=r'\1')
# get rid of column titles' annotations
colName = []
for i in df.columns:
  colName.append(re.split(r"\s", i)[0])

duplicates = {}
list = ['.A', '.a', '.b', '.c','.d','.e','.f','.g','.h']
index = 0
for i in colName:
  if i in duplicates:
    df.columns.values[index-1] = duplicates.setdefault(i, i) + list[::-1].pop()
    list.remove(list[0])
    df.columns.values[index] = duplicates.setdefault(i, i) + list[::-1].pop()
  else:
    df.columns.values[index] = duplicates.setdefault(i, i)
  index += 1

df.to_csv(dataset)

# --------------------------------------- #
# pd.set_option('display.max_rows', 4500)
# print(df)
# print(country_df.duplicated(subset="Country").value_counts())
