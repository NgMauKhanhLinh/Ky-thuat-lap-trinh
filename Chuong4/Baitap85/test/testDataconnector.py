from Chuong4.Baitap85.lib.DataConnector import DataConnector


dc=DataConnector()
#Lay toan bo nhan vien:
employees=dc.get_all_employee()
print("Danh sach nhan vien:")
for e in employees:
    print(e)
assets= get_all_asset()
print("Danh sach tai san:")
for a in assets:
    print(a)
aes=dc.get_all_employee_asset()
print("Danh sach phan cong tai san:")
for ae in aes:
    print(ae)
#test chuc nang dang nhap he thong
uid="teo"
pwd="123"
emp=dc.login(uid,pwd)
if emp!=None:
    print("Dang nhap thanh cong")
else:
    print("Dang nhap that bai")