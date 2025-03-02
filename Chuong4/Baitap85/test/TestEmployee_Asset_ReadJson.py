

from Chuong4.Baitap85.lib.JsonFileFactory import JsonFileFactory
from Chuong4.Baitap85.models.Employee_Asset import Employee_Asset
from Chuong4.Baitap85.test.TestEmployee_Asset_WriteJson import eas

jff=JsonFileFactory()
filename="../dataset/employee_assets.Json"
employees=jff.read_data(filename,Employee_Asset)
for ea in eas:
    print(ea)