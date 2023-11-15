class Human():
    def __init__(self,heart):
        self.num_eyes=2
        self.heart=heart
    def eat(self):
        print("i can eat")
class Male(Human):
    def __init__(self,name):
        self.name=name
    def work(self):
        print(" i can work")
class Boy(Male):
    def __init__(self,language,heart,name):
        Human.__init__(self,heart)
        Male.__init__(self,name)
        self.language=language


    def sleep(self):
        print("i can sleep")
    def work(self):
        Male.work(self) # self indicates boy1 we can use boy1 instead of self
        super().work() # it alsoo access the same
        print("i can code")


boy1=Boy("python",1,"heman")
boy1.work()
print(boy1.num_eyes)
print(boy1.heart)























# class Programmer(Boy):
#     def prog(self):
#         print(" i can program")

# prog_1=Programmer()
# prog_1.sleep()
