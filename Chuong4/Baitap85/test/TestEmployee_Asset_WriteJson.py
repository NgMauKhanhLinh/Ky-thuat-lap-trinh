from Chuong4.Baitap85.lib.JsonFileFactory import JsonFileFactory
from Chuong4.Baitap85.models.Employee_Asset import Employee_Asset

eas=[]
eas.append(Employee_Asset("E1","AS1","MAIN"))
eas.append(Employee_Asset("E2","AS2","MAIN"))
eas.append(Employee_Asset("E3","AS3","MAIN"))
eas.append(Employee_Asset("E4","AS4","MAIN"))
eas.append(Employee_Asset("E5","AS5","MAIN"))
eas.append(Employee_Asset("E6","AS6","MAIN"))
eas.append(Employee_Asset("E1","AS1","MAIN"))
eas.append(Employee_Asset("E2","AS2","MAIN"))
print("Danh sach phan cong quan ly tai san:")
for ea in eas:
    print(ea)
jff=JsonFileFactory()
filename="../dataset/employee_assets.Json"
jff.write_data(eas,filename)