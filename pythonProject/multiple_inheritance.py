class Human():
    def __init__(self,heart):
        self.num_eyes=2
        self.num_nose=1
        self.heart=heart
    def eat(self):
        print(" i can eat")
    def work(self):
        print(" i can work")
class Male():
    def __init__(self,name):
        self.name=name
    def behaviour(self):
        print(" i have good behaviour")
    def work(self):
        print("i can code")

class Boy(Human,Male):
    def __init__(self,language,name,heart):
        self.language=language
        Male.__init__(self,name)
        Human.__init__(self,heart)
    def work(self):
        print(" i can test")
    def sleep(self):
        print(" i can sleep ")
    def display(self):
        print(f" my name is {self.name} and i am doing {self.language} course and i have {self.heart} heart")

boy1= Boy("python","bhee","1")
boy1.behaviour()
boy1.work() # now it will print (i can work ) now Boy(Human,Male), it is matter if human class first it takes that method
# if you give male first it takes male method ( work method present in both classes)
Male.work(boy1) # now it will print male method
# mro is the method resolution order
print(Boy.mro())
print(boy1.num_eyes)
boy1.display()