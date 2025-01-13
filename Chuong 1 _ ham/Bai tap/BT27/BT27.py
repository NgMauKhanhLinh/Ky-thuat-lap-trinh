def toi_uu(s):
    return ' '.join(s.split()).title()

print("Nhập họ và tên:",end='')
a=input()
print("Số ký tự của chuỗi:",len(a))
s= toi_uu(a)

print("Chuỗi đã tối ưu:", s)
print("Số ký tự của chuỗi:",len(s))