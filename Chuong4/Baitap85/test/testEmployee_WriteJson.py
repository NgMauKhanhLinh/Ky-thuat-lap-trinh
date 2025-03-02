from Chuong4.Baitap85.lib.JsonFileFactory import JsonFileFactory
from Chuong4.Baitap85.models.Employee import Employee


employees=[]
employees.append(Employee("E1","Teo","teo","123"))
employees.append(Employee("E2","Ti","ti","234"))
employees.append(Employee("E3","Bin","bin","456"))
employees.append(Employee("E4","Bo","bo","182"))
employees.append(Employee("E5","Bun","bun","912"))
print("Danh sach Employee:")
for e in employees:
    print(e)
jff=JsonFileFactory()
filename="../dataset/employees.Json"
jff.write_data(employees,filename)