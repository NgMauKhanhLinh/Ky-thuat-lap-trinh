from Chuong4.Baitap85.lib.JsonFileFactory import JsonFileFactory
from Chuong4.Baitap85.models.Employee import Employee

jff=JsonFileFactory()
filename="../dataset/employees.Json"
employees=jff.read_data(filename,Employee)
print("Danh sach Employee sau khi doc file:")
for e in employees:
    print(e)