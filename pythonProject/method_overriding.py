# class Demo:
#     def add(self,a,b):
#         return a+b
#     def add(self,a,b,c=0):# using default arg we can rectify this error
#         return a+b+c
#     def add (self,*args):
#         total=0
#         for i in args:
#             total += i
#         return total
# d=Demo()
# print(d.add(2,3))
# print(d.add(2,3,4))#add() missing 1 required positional argument: 'c' , this is method overloading
# print(d.add(2,3,4,5,6,7,89,0))

class Father:
    def sleep(self):
        print(" sleeps from 10:00 PM to 6:00 AM")
    def eat(self):
        print("eating")
class Son(Father):
    # def sleep(self):
    #     print(" sleeps from 2:00 AM to 10:00 AM")
    def eat(self):
        print("eating")

f=Father()
f.sleep()
s=Son()
s.sleep()