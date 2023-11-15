class University:
    def __init__(self):
        self.univ_name="Anna University"
    def show_details(self):
        print(f" This is {self.univ_name} ")
class Course(University):
    def __init__(self):
        self.course="Engineering"
    def show_details(self):
        print(f" This is {self.univ_name} and course is {self.course} ")
class Branch(University):
    def __init__(self):
        self.branch_name="EEE"
    def show_details(self):
        print(f" This is {self.univ_name}  and the branch is {self.branch_name}")
class Student(Course,Branch):
    def __init__(self,name):
        self.name=name
        University.__init__(self)
    def show_details(self):
        print(f"My name is {self.name}")
        Course.show_details(self)
        Branch.show_details(self)
class Faculty(Branch):
    def __init__(self,Fac_name):
        self.Fac_name=Fac_name
    def show_details(self):
        Branch.show_details(self)
        print(f" faculty name:{self.Fac_name}")

student1=Student("hemA")
#print(student1.show_details())
faculty1=Faculty("hema")
faculty1.show_details()

