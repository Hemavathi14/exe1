# print(1+2)
# print("1"+"2")
# print(int.__add__(4,6))# it is already defined , when we pass 2 int then this mtd is called
# print(str.__add__("1","5"))#when we pass 2 str then this mtd is called
# # now we want to add the complex number how it is possible
# class ComplexNumber:
#     def __init__(self,r,i):
#         self.real=r
#         self.imaginary=i
#     def __add__(self, other):# self means c1 obj other means c2 obj
#         return f"{self.real + other.real} + {self.imaginary + other.imaginary}i"
#
# c1=ComplexNumber(1,2)
# c2=ComplexNumber(4,5)
# print(c1+c2)# it gives you error bcoz ide doesn't know what to do now the operator is overloaded ,to overcome this use special method
# # whenever  this  you write the + is this add method will call, in that method we are define our own func

class Person:
    def __init__(self,name,age):
        self.n=name
        self.a=age

    def __gt__(self, other):# we can use comparison operator also for lessthan - lt
        if self.a > other.a:
            print(f"{self.n} will pay the bill")
        else:
            print(f"{other.n} will pay the bill")

p1=Person("hema",22)
p2=Person("bhee",19)
p1>p2
