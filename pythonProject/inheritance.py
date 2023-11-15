class Human:
    def __init__(self,heart):
        self.num_eyes=2
        self.num_nose=1
        self.num_heart=heart
    def eat(self):
        print("i can eat")
    def work(self):
        print(" i can work")

class Male(Human):# here male is humman so he can eat and work for that we inherit the methods from super class
    # male some extra qualities so we def that here
    def __init__(self,name,heart):
        self.name=name
        super().__init__(heart)# we access the attributes of super class
    def behaviour(self):
        print("i have good behaviour")
# now the male have extra working ability we def work method here
    def work(self):
        super().work()
        print("i can code")
    def display(self):
        print(f"hi i am {self.name} i have {self.num_heart} heart")
male1=Male("krishna",1)
male1.eat()# access from super class
male1.behaviour() # it is from male class
male1.work() # override , it is print i can code only but i want super class work method also how we use it
# super() is func . it will give access of all attributes and methods of super class
print(male1.num_nose)
male1.display()
