class Student:
    def __init__(self,id=None,name=None,gpa=None):
        self.id=id
        self.name=name
        self.gpa=gpa
    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.gpa}"
