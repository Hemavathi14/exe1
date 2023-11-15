class Student:
    def __init__(self,name,rollno,age):
        self.name=name # public instance of variable
        self._rollno=rollno # protected instance variable , prefix with _
        self.__age=age # private instance variable prefix with __
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age>35:
            print("invalid")
        else:
            self.__age=age
    # def __display(self): # this method also private
    #     print(f"Hi myself {self.name} from student class with roll no {self._rollno}")
    # def displayPrivateData(self):
    #     self.__display()
# class Branch(Student):
#     def show(self):
#         print(f"My rollno is {self._rollno}"
s1=Student("hema",19,20)
print(s1.get_age())
s1.set_age(23)
print(s1.get_age())

# print(s1.name)
# print(dir(Student))
# s1._Student__display()#mangling mthd

#get and set mtd to implement complete encapsulation in python . we can access private data using this mtd
# get is used to access the private mtd and set mtd is used to modify it