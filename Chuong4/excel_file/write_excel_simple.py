import xlsxwriter as xr

workbook = xr.Workbook("Products.xlsx")
worksheet = workbook.add_worksheet()

# Modify column width
worksheet.set_column('A:A', 5)
worksheet.set_column('B:B', 20)
worksheet.set_column('C:C', 15)

bold = workbook.add_format({'bold': True})

# Add header
worksheet.write('A1', 'Id', bold)
worksheet.write('B1', 'Name', bold)
worksheet.write('C1', 'Price', bold)

# Add first row
worksheet.write('A2', '1')
worksheet.write('B2', 'Heineken')
worksheet.write('C2', '19000')

# Add second row
worksheet.write('A3', '2')
worksheet.write('B3', 'Tiger')
worksheet.write('C3', '18000')

# Insert image
worksheet.insert_image('B5', 'beer.png')

workbook.close()


