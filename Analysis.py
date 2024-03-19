import scipy.stats as sc
import pandas as pd

# Subsets creation
dataset = "./dataset.csv"
df = pd.read_csv(dataset)

for i in range(2000,2020):
  print(df.query("Year == " + str(i)))

