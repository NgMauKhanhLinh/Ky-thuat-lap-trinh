from Chuong4.Baitap85.lib.JsonFileFactory import JsonFileFactory
from Chuong4.jsonfile_oop.listemployee import ListEmployee
from Chuong4.jsonfile_oop.mydump import mydump

le=ListEmployee()
arr_emp_dump=mydump.gen_sample_employees()
le.add_employees(arr_emp_dump)
print("List of employees before serialize (to Json):")
le.print_all_employees()
jff=JsonFileFactory()
jff.write_data(le.employees,"employees.json")