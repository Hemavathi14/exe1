# same func have diff forms , for example
class Duck :
    def swim(self):
        print("I am a duck I can swim")
    def speak(self):
        print("Quack Quack")

class Dog:
    def swim(self):
        print("I am a dog I can swim")
    def speak(self):
        print("woof woof ")
class Person():
    def speak(self):
        print("blah blah blah")

def display(obj):
    obj.swim()
    obj.speak()
# python using dynamic typing - data type of the variable can change according to the input
# it does not consideer class mrthods and attributes are important , class doesn't  matter type does

d=Duck()
dog=Dog()
p=Person()
display(d)
display(dog)
display(p)# in tis obj we didn't define swim , python doesn't care for object or class if you define a method it calls otherwise don't


