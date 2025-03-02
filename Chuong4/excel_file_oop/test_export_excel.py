from Chuong4.excel_file_oop.liststudent import ListStudent
from Chuong4.excel_file_oop.mydump import MyDump

ls=ListStudent()
arr=MyDump.gen_students_dataset()
ls.add_students(arr)
print("List of Gen Students:")
ls.print_all_students()

#export to excel
filename="student.xlsx"
ls.export_excel(filename)