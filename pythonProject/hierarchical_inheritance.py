class A():
    def __init__(self):
        self.num_eyes=2
    def work(self):
        print("i can work")
class B(A): # inherit from class a
    def eat(self):
        print("i can eat")
class C(A):# inherit from class a
    def __init__(self,name):
        self.name=name
        A.__init__(self)

    def sleep(self):

        print("i can sleep")

c1=C("hema")
print(c1.sleep())
print(c1.num_eyes)