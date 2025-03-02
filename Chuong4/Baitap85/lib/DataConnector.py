from Chuong4.Baitap85.lib.JsonFileFactory import JsonFileFactory
from Chuong4.Baitap85.models.Asset import Asset

from Chuong4.Baitap85.models.Employee import Employee
from Chuong4.Baitap85.models.Employee_Asset import Employee_Asset





class DataConnector:
    def get_all_employee(self):
        jff = JsonFileFactory()
        filename = "../dataset/employees.Json"
        employees = jff.read_data(filename,Employee)
        return employees

    def get_all_employee_asset(self):
        jff = JsonFileFactory()
        filename = "../dataset/employee_assets.Json"
        eas = jff.read_data(filename, Employee_Asset)
        return eas

    def login(self,username,password):
        employees=self.get_all_employee()
        for e in employees:
            if e.UserName==username and e.Password==password:
                return e
        return None

    def get_all_asset(self):
        jff = JsonFileFactory()
        filename = "../dataset/assets.Json"
        assets = jff.read_data(filename, Asset)
        return assets