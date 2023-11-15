#default argument
def greet(name,dept):
    print(f"hi {name}")
    print(f"you are from {dept} department")

greet("hema","eee")# these are positional argument we are not specified which parameter is associated with which value
#we are passing two values it will accept two values....1st position value assign to 1st position arguments
greet("ee","hema")# now it will return nonsense output

#keyword argument
def greet(name,dept):
    print(f"hi {name}")
    print(f"you are from {dept} department?")
greet(dept="eee",name="hema")
greet(name="hema",dept="eee")#now we can change the order it is not affected the order
# in the same fuction call we use poitional + keywrd arg
greet("hema",dept="ee")
#greet(dept="ee","hema") now it will give you error it is manditory positional arg come first after keyword arg

#default parameter
def greet(name,subject,dept="ee"):
    print(f"hi {name}")
    print(f"would you teach {subject}")
    print(f"you are from {dept} department?")
greet("hema","c") # it will take the default value  here dept is default argument and name and subject is known default
#argument this is what required arg ." The default arg should be provided after the known arg
greet("hema","python","cs")# it will override the default value

# arbitrary arg
# sometimes i add 2 num sometimes i add 3 ........if the no of arg vary every time i call the func,so i cannot fix the values  here we can probide variable length arg
# how you provide arbitrary func - use * sign and one variable name
def addition(*numbers):
    c=0
    for i in numbers:
        c=c+i
    print(f"your addition is {c} ")
addition(10,20)
addition(10,20,78,45,789,90)
# here we use only one * this is arbitrary positional argument


