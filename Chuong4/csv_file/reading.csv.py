import csv
with open('employee.csv', newline='',encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    for row in reader:
        print(' - '.join(row))
        # print(row[0] + ' * ' + row[1] + ' * ' + row[2] + ' * ' + row[3])

