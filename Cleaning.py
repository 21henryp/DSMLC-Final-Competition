import pandas as pd
from openpyxl import load_workbook as lwb

# -------------------------------------------------------------
def dropStyles(df: pd.DataFrame, workbook):
  for i in range(len(df.index)):
    for j in range(len(df.columns)):
      cell = workbook.cell(i+1,j+1) #workbook not filtered 
  
  # print(cell.value)
  # print(cell.row)
  # print(df.iloc[cell.row - 1])

# -------------------------------------------------------------
dataset = ".\DSMLC Final Competition 2024 Dataset.xlsx"
workbook = lwb(dataset, data_only=True).active
df = pd.read_excel(dataset)

# drop dulicates
df = df.drop_duplicates()
# dataframe with countries only
country_df = df.dropna(subset="Code")

dropStyles(country_df, workbook)
# print(country_df.iloc[len(country_df.index) - 1])

# print(country_df.duplicated(subset="Country").value_counts())
