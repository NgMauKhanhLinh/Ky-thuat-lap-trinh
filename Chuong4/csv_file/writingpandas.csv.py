import pandas
df = pandas.read_csv('employee.csv', index_col="Id")
df.to_csv('another_employee.csv')

