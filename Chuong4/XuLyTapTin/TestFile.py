from XuLyFile import *

masp = input("nhập mã sản phẩm: ")
tensp = input("nhập tên sản phẩm: ")
dongia = float(input("nhập giá sản phẩm: "))

line = masp + ";" + tensp + ";" + str(dongia)

LuuFile("database.txt", line)
