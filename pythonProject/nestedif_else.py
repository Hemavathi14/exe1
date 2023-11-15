#nested if
""""
a=34
if a%2==0:
    print("even")
    if(a>30):
        print(">30")
print ("bye")
#nested if else
height=int(input("what is your height??.....in feet"))

if(height>3):
    print("you can ride")
    age=int(input("enter your age"))
    if age<18:
        print("pay rs 250")
    else:
        print("pay rs500 ")
else:
    print("yoou can't ride")
print("bye")
"""
if(height>3):
    print("you can ride")
    age=int(input("enter your age"))
    if age<11:
        print("pay rs 150")
    if age<19:
        print("pay rs 250")
    if age < 35:
        print("pay rs 350")
    else:
        print("pay rs500 ")
else:
    print("yoou can't ride")
print("bye")