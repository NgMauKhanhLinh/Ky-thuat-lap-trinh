class ListEmployee:
    def __init__(self):
        self.employees=[]
    def print_all_employees(self):
        for emp in self.employees:
            print(emp)
    def add_employees(self,arr):
        self.employees.extend(arr)