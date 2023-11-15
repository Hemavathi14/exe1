
a=15 #global variable it is declared globally

def display():
    a=11
    def show():
        #a=10 # local variable we can access it with in the func only
        print(a) #if we can't declare local variable a is assign to global value it print 15
    show()# a nested func call with in the func otherwise it is a error
display()
print(a) #if we cant declare global variable it will be error

# in c c++ there is a block scope it is used in for while if ifelse conditions.........in python there is no block scope

a,b=7.7,8
if a>b:
    c=a+b
print(c)