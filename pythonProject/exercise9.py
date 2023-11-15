print("Welcome to Hema's Pizza")
print("Ordering details")
print("\n 1.small pizza=100rs \n 2.Medium pizza=200rs \n 3.large pizza=300rs \n pepporoni for Small pizza =30rs \n pepporoni for "
      "medium or large pizza =50rs \n extra cheese for any size pizza =20rs")

size=input("which size of pizza you want? (s/m/l) ")
bill=0

if size=='s' or size == 'S':
    bill+=100
    print(f"you have to pay rs{bill}")
elif size=="m" or size=="M":
    bill+=200
    print(f"you have to pay rs{bill}")
else:
    bill+=300
    print(f"you have to pay rs{bill}")
add_pepperoni=input("do you want pepperoni?? (y/N)")
if add_pepperoni == "y" or add_pepperoni == "Y" :
    if size == 's' or size == 'S':
        bill+=30
        print(f"now your price is {bill}")
    else:
        bill+=50
        print(f"now your price is {bill}")
add_cheese=input("do you want cheese??(y/N)")
if add_cheese=="y" or add_cheese=="Y":
    bill+=20
    print(f"your final price is {bill}")
print(" thankyou for ordering")