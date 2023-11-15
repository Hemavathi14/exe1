class Student:
    def __init__(self,name,rollno,age):
        self.name=name # public instance of variable
        self._rollno=rollno # protected instance variable , prefix with _
        self.__age=age # private instance variable prefix with __
    def __display(self): # this method also private
        print(f"Hi myself {self.name} from student class with roll no {self._rollno}")
    def displayPrivateData(self):
        self.__display()
    def rollno(self):
        print(self._rollno)
class Branch(Student):
    pass

s1=Student("hema",19,20)
print(s1.name)
# s1.name="bhee" # we can modify iit
# s1._rollno=45
# print(s1.__age)
# s1.display()
# def showdata(): # public func use the protected attributes python does not provide strict restriction ,it is flexible
#     b1=Branch("bhee",56)# not use protected outside avoid ....
#     print(b1._rollno)
#     b1.display()
# showdata()
s1.displayPrivateData() # now it will print because it is in the class

#we can access private attributes and methods using name mangling
# for that use dir method
print(dir(Student))#mangling is for private things, it will shoe the all valid attribute
print(s1._Student__display) # now we can access from outsise of the