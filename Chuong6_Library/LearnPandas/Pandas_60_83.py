import numpy as np
import pandas as pd

#slide60
df = pd.read_csv("Data/SampleData.csv", index_col=0)
print(df)

#slide61
df = pd.read_csv("Data/SampleData.csv", index_col=0)
print(df)
df["Usd"] = df["Price"]/22
print(df)

#slide62
df = pd.read_csv("Data/SampleData.csv")
print(df)
df.loc[df.shape[0]] = ["VCB", 117.6, 25.8]
print(df)

#slide63
sales_2020 = pd.DataFrame({'sales': [450, 503, 5037, 793]}, index =['Mar', 'Jun', 'Feb', "Apr"])
print(sales_2020)
print(sales_2020.sort_index())

#slide64
sales_2020 = pd.DataFrame({'sales': [450, 503, 5037, 793]}, index =['Mar', 'Jun', 'Feb', "Apr"])
print(sales_2020)
sales_2021 = pd.DataFrame({'sales': [5432, 348, 376, 762]}, index =['Mar', 'Jun', 'Feb', "Apr"])
print(sales_2020.reindex(sales_2021.index))

#slide65
df = pd.read_csv("Data/SampleData2.csv")
print(df)
print(df.groupby('Group').mean())
#print(df.groupby('Group').sum())
#print(df.groupby('Group').count())
