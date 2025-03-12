import numpy as np
import pandas as pd

#slide37
#series
ser = pd.Series([1, 2, 3, 4, 5])
print(ser)

arr_price = np.array([70.2, 29.1, 12.8, 38.4])
arr_symbol = np.array(["FPT", "VNM", "VCB", "MBB" ])
ser = pd.Series(arr_price, index=arr_symbol)
print (ser)


dic = {"FPT":70.2, "VNM":29.1, "VCB":12.8, "MBB":38.4}
ser = pd.Series(dic)
print(ser)

#slide38
#truy xuat
print(ser['VNM'])
print(ser[2])
print(ser[1:])
print(ser[['FPT', 'VNM']])

#slide39
print(ser.size)
print(len(ser))
print(ser.values)
print(ser.index)
print(ser.axes)


#slide40
#truy xuat

dic = {"FPT":70.2, "VNM":29.1, "VCB":12.8, "MBB":38.4}
ser = pd.Series(dic)
print(ser)

print(ser.head(3))
print(ser.tail(2))

#slide41
#truy xuat
print(ser.mean())
print(ser.std())
print(ser.describe())

#slide42
#cap nhat
ser ["FPT"] = 82
ser[2] = 105
print(ser)

#slide43
#xoa phan tu
print(ser.drop(ser.index[[0, 2]]))
print(ser.drop(["VCB" , "MBB"]))


#slide44
#TINH TOAN SO HOC
print(ser + 2)
print(ser.map(lambda x: x*2))

#slide45
#data frame
list_sample =[["PNJ", 180.4, 184.9 ], ["VPB", 28.4, 29.1], ["TCB", 204.5, 240.6], ["VJA", 240.6, 502.5]]
df = pd.DataFrame(list_sample, columns=["Name", "Open", "Close"])
print(df)

#slide46
#doc du lieu tu file .csv/ .xlsx
df = pd.read_csv("Data/employee.csv")
print(df)

#slide47
df = pd.read_excel("Data/Sales.xlsx")
print(df)

#slide48
df= pd.read_csv("Data/TCB_2018_2020.csv")
print(df)

#slide49
df= pd.read_csv("Data/TCB_2018_2020.csv", index_col=0)
print(df.head())

#slide50
df= pd.read_csv("Data/TCB_2018_2020.csv", index_col=0)
print(df[df["Close"]>100])

#slide51
print(df[["High", "Low"]].tail())

#slide52
df= pd.read_csv("Data/TCB_2018_2020.csv", header= None)
print(df[[0, 2, 3]].tail())

#slide53
df= pd.read_csv("Data/TCB_2018_2020.csv", index_col=0)
print(df.loc["2020-06-15"])

#slide54
df= pd.read_csv("Data/TCB_2018_2020.csv", index_col=0)
print(df.loc[['2019-06-10', '2020-06-10']])

#slide55
df= pd.read_csv("Data/TCB_2018_2020.csv", index_col=0)
print(df.iloc[0])


#slide56
df= pd.read_csv("Data/TCB_2018_2020.csv", index_col=0)
print(df.iloc[0, 2])

#slide57
df= pd.read_csv("Data/TCB_2018_2020.csv", index_col=0)
print(df.iloc[35:41])

#slide58
df= pd.read_csv("Data/TCB_2018_2020.csv", index_col=0)
print(df.loc["2019-08-20", "Close"])
print(df.loc["2020-12-25", "Open"])

#slide59
df= pd.read_csv("Data/TCB_2018_2020.csv", index_col=0)
print(df.iloc[4, 0])

print(df.iloc[648:, :])