import pandas as pd

# -------------------------------------------------------------


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
# get rid of "() along with its annotations"
df["Country"] = df["Country"].replace(regex=r'(.+?)\s\(.*\)', value=r'\1')
df.to_csv(dataset)

# --------------------------------------- #
pd.set_option('display.max_rows', 4500)
print(df)
# print(country_df.duplicated(subset="Country").value_counts())
