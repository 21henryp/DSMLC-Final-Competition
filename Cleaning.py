import pandas as pd

dataset = "D:\School\Winter 2024\DSMLC Competition\DSMLC Final Competition 2024 Dataset.xlsx"
df = pd.read_excel(dataset)

# drop dulicates
df = df.drop_duplicates()
# dataframe with countries only
country_df = df.dropna(subset="Code")


print(country_df)