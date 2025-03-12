import pandas as pd

#tải dữ lệu lên
df = pd.read_csv("../Data/TCB_2018_2020.csv")


# 1. Xuất toàn bộ dữ liệu TCB ra màn hình
print("\n1. Toàn bộ dữ liệu TCB:\n")
print(df)

# 2. Lọc ra dữ liệu với điều kiện Close < x và Close > y
x = float(input("\nNhập giá trị x (Close < x): "))
y = float(input("Nhập giá trị y (Close > y): "))

filtered_df = df[(df["Close"] < x) | (df["Close"] > y)]
print("\n2. Dữ liệu sau khi lọc Close < x hoặc Close > y:\n", filtered_df)

# 3. Lọc dữ liệu lấy các cột Date, High, Low và lọc Low từ x đến y
low_x = float(input("\nNhập giá trị x cho Low: "))
low_y = float(input("Nhập giá trị y cho Low: "))

filtered_low_df = df[(df["Low"] >= low_x) & (df["Low"] <= low_y)][["Date", "High", "Low"]]
print("\n3. Dữ liệu lọc theo Low từ x đến y:\n", filtered_low_df)

# 4. Nhập vào một ngày cụ thể để xem thông tin chi tiết
date_input = input("\nNhập ngày cần tra cứu (YYYY-MM-DD): ")

if date_input in df["Date"].values:
    print("\n4. Dữ liệu ngày giao dịch:", df[df["Date"] == date_input])
else:
    print("\nKhông tìm thấy dữ liệu cho ngày này.")

# 5. Nhập vào một danh sách ngày để lọc dữ liệu
date_list = input("\nNhập danh sách ngày (cách nhau bởi dấu phẩy): ").split(',')
filtered_dates_df = df[df["Date"].isin(date_list)]
print("\n5. Dữ liệu lọc theo danh sách ngày:\n", filtered_dates_df)
