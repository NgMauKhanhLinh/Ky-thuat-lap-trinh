import columns
import matplotlib.pyplot as plt # cách 1
import pandas as pd
import rows

# from matplotlib import pyplot as plt  # cách 2


#slide 87
# thiết lập thông số cấu hình chung cho biểu đồ
# plt.rcParams['savefig.dpi'] = 200
# plt.rcParams['legend.fontsize'] = 'large'
# plt.rcParams['figure.titlesize'] = 'medium'
# plt.rcParams["legend.loc"] = 'best'
plt.rcParams['figure.figsize'] = (10,8)
plt.rcParams['figure.dpi'] = 200
plt.rcParams['font.size'] = 13


#slide 88
#Biểu đồ đường
df = pd.read_csv('./Data/NetProfit.csv')
dat = df[['Year', 'VIC']]
print(dat)

plt.plot('Year', 'VIC', data=dat)
plt.show()


#slide 89
#Biểu đồ đường
df = pd.read_csv('./data/NetProfit.csv')
print(df)
plt.plot('Year', 'VNM', data=df)
plt.plot('Year', 'PNJ', data=df)
plt.plot('Year', 'VCB', data=df)
plt.plot('Year', 'VIC', data=df)
plt.show()

#slide 90
#Biểu đồ đường
plt.plot('Year', 'VNM', data=df, color='b', linestyle='-', marker='o')
plt.plot('Year', 'PNJ', data=df, color='g', linestyle='--', marker='s')
plt.plot('Year', 'VCB', data=df, color='#FF0000', linestyle=':', marker='+')
plt.plot('Year', 'VIC', data=df, color='orange', linestyle='-.', marker='*')
plt.title("Lợi nhuận của VNM, PNJ, VCB, VIC từ 2010 đến 2020", fontweight='bold')
plt.xlabel("Năm", fontweight='bold')
plt.ylabel("Lợi nhuận", fontweight='bold')
plt.legend()
plt.show()

#slide 91
#biểu đồ cột
df = pd.read_csv('./Data/PVD_Asset.csv')
print(df)

plt.bar('Year', 'Liabilities', data=df)
plt.title("Nợ của PVD qua các năm")
plt.xlabel("Năm")
plt.ylabel("Nợ")
plt.show()


#slide 92
#biểu đồ cột
df = pd.read_csv('./Data/PVD_Asset.csv')
print(df)

plt.barh('Year', 'Equity', data=df)
plt.title("Vốn của PVD qua các năm")
plt.xlabel("Vốn")
plt.ylabel("Năm")
plt.show()



#slide 93
#biểu đồ cột
plt.bar('Year', 'Liabilities', data=df, color='orange', label="Nợ")
plt.bar('Year', 'Equity', data=df, bottom='Liabilities', color='darkgreen', label="Vốn")
plt.title("Tài sản của PVD từ 2010-2020")
plt.xlabel("Năm")
plt.ylabel("Tỷ đồng")
plt.legend()
plt.show()



#slide 94
#biểu đồ phân tán
df = pd.read_csv('./Data/Income.csv')
print(df)

plt.scatter('Income', 'Expenditure', data=df, color='darkgreen')
plt.xlabel('Thu nhập', fontweight='bold')
plt.ylabel('Chi tiêu', fontweight='bold')
plt.show()

#slide 95
#biểu đồ phân tán
colors = np.random.rand(df.shape[0]) # Random màu ngẫu nhiên
area = df['Income'].values * 50 # Kích thước điểm dữ liệu
plt.scatter('Income', 'Expenditure', data=df, c=colors, s=area,alpha=0.8)
plt.xlabel('Thu nhập', fontweight='bold')
plt.ylabel('Chi tiêu', fontweight='bold')
plt.show()


#slide 96
#biểu đồ tần suất
dat = np.random.normal(12, 2, 400)
plt.hist(dat, color='darkgreen', edgecolor='orange')
plt.xlabel('Lương')
plt.ylabel('Tần suất')
plt.show()


#slide 97
#biểu đồ tròn
lbls = ['Chuyển nhượng BĐS', 'Cho thuê BĐS', 'DV khách sạn', 'Bệnh viện', 'Giáo dục', 'Sản xuất', 'Hoạt động khác']
income = [71.576, 6.788, 4.869, 2.675, 2.244, 18.007, 4.304]
explode = [0.1, 0.1, 0.2, 0.2, 0.1, 0.1, 0.2]
plt.pie(income, labels= lbls, explode=explode, autopct='%1.1f%%', pctdistance=1.1, labeldistance=1.2)
plt.title('Cơ cấu doanh thu VinGroup - 2020', fontweight='bold')
# plt.legend(loc='upper right')
plt.show()


#slide 99
#biểu đồ boxplot
dat = pd.read_csv('./Data/Salary_of_Developer.csv')
print(dat)
plt.boxplot(dat)
plt.ylabel("Lương (triệu đồng)")
plt.title("Boxplot thể hiện phân bổ mức lương Lập trình viên")
plt.show()

#slide 100
#biểu đồ boxplot
orange_square = dict(markerfacecolor='orange', marker='s')
plt.boxplot(dat, notch=True, flierprops=orange_square, vert=False)
plt.xlabel("Lương (triệu đồng)")
plt.title("Boxplot thể hiện phân bổ mức lương Lập trình viên")
plt.show()


#slide 101
#biểu đồ kết hợp
plt.subplot(rows, columns, index)






