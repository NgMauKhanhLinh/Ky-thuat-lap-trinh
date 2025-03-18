import numpy as np
import pandas as pd
import seaborn as sns


#slide 104
# thiết lập thông số cấu hình chung cho biểu đồ
import seaborn as sns
from matplotlib import pyplot as plt
from seaborn import relplot

sns.set(style='darkgrid') # Thiết lập style cho biểu đồ
import ssl
# Cấu hình ssl cho phép tải dữ liệu mẫu thông qua thư viện
ssl._create_default_https_context = ssl._create_unverified_context

# Show sample datasets
sample_datasets = sns.get_dataset_names()
print(sample_datasets)


#slide 105
#biểu đồ với biến liên tục
# replot()
tips = sns.load_dataset("tips")
print(tips.head())

sns.relplot(x='total_bill', y='tip', data=tips)

#slide 106
#biểu đồ với biến liên tục
# replot()
sns.relplot(x='total_bill', y='tip', data=tips, hue='smoker')


#slide 107
#biểu đồ với biến liên tục
# replot()
sns.relplot(x='total_bill', y='tip', data=tips, hue='smoker', style='sex')

#slide 108
#biểu đồ với biến liên tục
# replot()
sns.relplot(x='total_bill', y='tip', data=tips, hue='smoker', style='sex', size='size')

#slide 109
#biểu đồ với biến liên tục
# replot()
dat = pd.read_csv('./Data/Income.csv')
print(dat)
sns.relplot(x='Income', y='Expenditure', data=dat, kind='scatter')



#slide 110
#biểu đồ với biến liên tục
# scatterplot()
#relplot() với
kind='scatter'


#slide 111
#biểu đồ với biến liên tục
# scatterplot()
#relplot() với
kind='line'


#slide 112
#biểu đồ với biến phân loại
# catplot()

    #phân tán
        #stripplot() → catplot() với kind='strip'
        #swarmplot() → catplot() với kind='swarm'

    #phân phối:
        # boxplot() → catplot() với kind='box'
        # violinplot() → catplot() với kind='violin'
        # boxenplot() → catplot() với kind='boxen'

    #Ước tính:
        # pointplot() → catplot() với kind='point'
        # barplot() → catplot() với kind='bar'



#slide 113
#biểu đồ với biến phân loại
# catplot()
df = pd.read_csv('./Data/Housing.csv')
# chọn 500 dòng ngẫu nhiên từ df
dat = df.sample(500)   # df: {DataFrame: (20640, 10)}
sns.catplot(x='ocean_proximity', y='median_house_value',data=dat)  # dat: {DataFrame: (500, 10)}


#slide 114
#biểu đồ với biến phân loại
# catplot()
df = pd.read_csv('./Data/Housing.csv')
# chọn 500 dòng ngẫu nhiên từ df
dat = df.sample(500)
sns.catplot(x='ocean_proximity', y='median_house_value', data=dat, kind='box')


#slide 115
#biểu đồ với biến phân loại
# catplot()
df = pd.read_csv('./Data/Housing.csv')
# chọn 500 dòng ngẫu nhiên từ df
dat = df.sample(500)
sns.catplot(x='ocean_proximity', y='median_house_value', data=dat, kind='point')


#slide 116
#biểu đồ phân phối (tần suất)
# displot()
np.random.seed(10) #random với giá trị không đổi
dat = np.random.normal(12, 2, 400)

#trường hợp 1:
sns.displot(dat)
plt.xlabel('Salary')

# trường hợp 2:
sns.displot(dat)
plt.xlabel('Salary')

#slide 117
#biểu đồ hồi quy
# regplot()
df = pd.read_csv('./Data/Income.csv')
sns.regplot(x='Income', y='Expenditure', data=df)


#slide 118
#biểu đồ nhiệt
# heatmap()
flights_long = sns.load_dataset('flights')
flights = flights_long.pivot('month', 'year', 'passengers')
#slide 119
#biểu đồ nhiệt
# heatmap()
sns.heatmap(flights, annot=True, fmt='d', linewidths=.5)

#slide 120
#biểu đồ kết hợp
# jointplot()
df = pd.read_csv('./Data/Income.csv')
sns.jointplot(x='Income', y='Expenditure', data=df, color='orange')


#slide 121
#biểu đồ kết hợp
# pairplot()
df = pd.read_csv('./Data/Income.csv')
sns.pairplot(df[['Income','Expenditure']])

