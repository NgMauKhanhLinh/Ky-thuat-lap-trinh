from Chuong4.jsonfile_oop.employee import Employee


class mydump:
    @staticmethod
    def gen_sample_employees():
        employees=[]
        employees.append(Employee("e1","Tèo","teo@gmail.com"))
        employees.append(Employee("e2", "Tí", "ti@gmail.com"))
        employees.append(Employee("e3", "Bin", "bin@gmail.com"))
        employees.append(Employee("e4", "Bo", "bo@gmail.com"))
        employees.append(Employee("e5", "Tủn", "tun@gmail.com"))
        return employees