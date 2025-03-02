from Chuong4.Baitap85.lib.JsonFileFactory import JsonFileFactory
from Chuong4.jsonfile_oop.employee import Employee
from Chuong4.jsonfile_oop.listemployee import ListEmployee

le=ListEmployee()
jff=JsonFileFactory()
arr=jff.read_data("employees.json",Employee)
le.add_employees(arr)
print("List of Employees after Deserializing:")
le.print_all_employees()