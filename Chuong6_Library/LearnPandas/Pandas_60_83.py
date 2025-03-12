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
print(df.groupby('Group'))
#print(df.groupby('Group').mean())
#print(df.groupby('Group').sum())
#print(df.groupby('Group').count())


#slide66
df = pd.read_csv("Data/SampleData2.csv")
df1 = df[['Symbol', 'Price', 'Group']]
df2 = df[['Symbol', 'PE', 'Group']]
print(df1)
print(df2)


#slide67
df_concat = pd.concat([df1, df2])
print(df_concat)


#slide68
df_concat = pd.concat([df1, df2], join='inner')
print(df_concat)

#slide69
df_concat = pd.concat([df1, df2], axis=1)
print(df_concat)

#slide70
# df_append = df1.append(df2)
# print(df_append)

#slide71
df_merge = pd.merge(df1, df2)
print(df_merge)

#slide72
df = pd.read_csv("Data/SampleData2.csv")
df1 = df[['Symbol', 'Price', 'Group']]
df1=df1.drop(df1.index[3])  #xóa FPT
df2 = df[['Symbol', 'PE', 'Group']]
print(df1)
print(df2)

#slide73
df_merge = pd.merge(df1, df2)
print(df_merge)
df_merge = pd.merge(df1, df2, how='outer')
print(df_merge)

#slide74
df = pd.read_csv("Data/SampleData_NaN.csv")
print(df)

#slide75
df = pd.read_csv("Data/SampleData_NaN.csv")
print(df.isnull())

#slide76
df = pd.read_csv("Data/SampleData_NaN.csv")
print(df.isnull().any())
print(df.isnull().values.any())

#slide77
df = pd.read_csv("Data/SampleData_NaN.csv")
print(df.isnull().sum())
print(df.isnull().sum().sum())

#slide78
df = pd.read_csv("Data/SampleData_NaN.csv")
df_delete_na_by_row = df.dropna(axis=0)
print(df_delete_na_by_row)

#slide79
df = pd.read_csv("Data/SampleData_NaN.csv")
df_delete_na_by_row = df.dropna(axis=1)
print(df_delete_na_by_row)

#slide80
#fill giá trị 100 cho phần tử rỗng
df = pd.read_csv("Data/SampleData_NaN.csv")
df_fill_na_100 = df.fillna(100)
print(df_fill_na_100)

#slide81
df = pd.read_csv("Data/SampleData_NaN.csv")
#fill phần tử rỗng với giá trị liền kề phía dưới
df_fill_na_bfill = df.fillna(method='bfill')
print(df_fill_na_bfill)

#slide82
df = pd.read_csv("Data/SampleData_NaN.csv")
#fill phần tử rỗng với giá trị liền kề phía trên
df_fill_na_ffill = df.fillna(method='ffill')
print(df_fill_na_ffill)

#slide83
df = pd.read_csv("Data/SampleData_NaN.csv")
#fill phần tử rỗng với giá trị liền kề phía trên
df_fill_na_interpolate = df.interpolate()
print(df_fill_na_interpolate)