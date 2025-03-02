import xlsxwriter as xr
class ListStudent:
    def __init__(self):
        self.students=[]
    def add_student(self, st):
        self.students.append(st)
    def add_students(self,arr):
        self.students.extend(arr)
    def print_all_students(self):
        for st in self.students:
            print(st)
    def export_excel(self,filename):
        workbook = xr.Workbook(filename)
        worksheet = workbook.add_worksheet()

        # Modify column width
        worksheet.set_column('A:A', 5)
        worksheet.set_column('B:B', 20)
        worksheet.set_column('C:C', 15)

        bold = workbook.add_format({'bold': True})

        # Add header
        worksheet.write('A1', 'Student Id', bold)
        worksheet.write('B1', 'Student Name', bold)
        worksheet.write('C1', 'Student GPA', bold)
        cell_format_st_failed=workbook.add_format()
        cell_format_st_failed.set_font_color('red')
        cell_format_st_failed.set_bg_color('yellow')
        for i in range (len(self.students)):
            index=i+2
            st=self.students[i]
            if float(st.gpa)<5:
                worksheet.write(f'A{index}',st.id,cell_format_st_failed)
                worksheet.write(f'B{index}', st.name, cell_format_st_failed)
                worksheet.write(f'C{index}', st.gpa, cell_format_st_failed)
            else:
                worksheet.write(f'A{index}',st.id)
                worksheet.write(f'B{index}', st.name)
                worksheet.write(f'C{index}', st.gpa)
        workbook.close()








