from Chuong4.excel_file_oop.student import Student


class MyDump:
    @staticmethod
    def gen_students_dataset():
        students=[]
        students.append(Student("ST1","Tèo","10"))
        students.append(Student("ST2","Ty","4"))
        students.append(Student("ST3", "Bin", "7.5"))
        students.append(Student("ST4", "Bo", "8"))
        students.append(Student("ST5", "Tun", "3"))
        return students
