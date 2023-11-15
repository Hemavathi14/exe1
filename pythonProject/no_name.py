"""
service=int(input("how many year service you are? "))
salary=int(input("enter your salary"))
if service>=5:
    bonus=salary*.05
    amount=salary+bonus
    print(f"you got bonus{bonus}")
    print(f"your salary is {amount}")
else:
    print(f"your salary is {salary}")
#finding square
length=int(input("enter the length.."))
breadth=int(input("enter the breadth.."))
if length==breadth:
    print ("it is square")
else:
    print("not a square")
# printing grades
mark=int(input("enter your marks "))
if mark<25:
    print("grade f")
elif mark<50:
    print("grade d")
elif mark<60:
    print("grade c")
elif mark<80:
    print("grade b")
else:
    print("grade a")
    """
number=input("enter 4 digit number")
print(number[3],number[2],number[1],number[0])