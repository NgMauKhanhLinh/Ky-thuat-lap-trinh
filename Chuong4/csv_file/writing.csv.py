import csv

with open('new_employee.csv', mode='w',encoding='utf-8') as f:
    employee_writer = csv.writer(f, delimiter=',', quotechar='"')
    employee_writer.writerow(['Id', 'Name', 'Dob'])
    employee_writer.writerow(['1', 'Tú Linh', '02/02/2002'])
    employee_writer.writerow(['2', 'Nam Giao', '03/04/2000'])
    employee_writer.writerow(['3', 'Huỳnh Anh', '05/11/2001'])