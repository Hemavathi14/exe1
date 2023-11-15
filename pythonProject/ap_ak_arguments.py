"""
def add(*numbers):# now it will become a tuple here y tuple means tuples are immutable
    c=0
    print(numbers[2])
    for i in numbers:
        c=c+i
    print(c)

add(1,2,3,45,67,7,89)


def add(*numbers,name):# now it will become a tuple here y tuple means tuples are immutable
    c=0
    print(numbers)
    #for i in numbers:
    #    c=c+i
    #print(c)

add(1,2,3,45,67,7,89,"hema") #now it will give you TypeError: add() missing 1 required keyword-only argument: 'name'
# it fully consider as a tuple
def add(*numbers,name):# now it will become a tuple here y tuple means tuples are immutable
    c=0
    print(numbers)
    print(name)
    for i in numbers:
        c=c+i
    print(c)

add(1,2,3,45,67,7,89,name="hema")

def add(a,*numbers):
    c=0
    print(numbers)# now the one is assign to a and the sum is 7 so first better write normal arg then ap and ak args
    for i in numbers:
        c=c+i
    print(c)

add(1,2,3)
"""

# **kwargs
def info_person(**kwargs):# it will be in dictionary here dictionary havong key and value pair so 2 things we want to access
    for key,value in kwargs.items():
        print(key,value)
info_person(name="hema",age=30,dept="eee")
info_person(name="hema",dept="eee")

