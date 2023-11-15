height=int(input("what is your height??.....in feet"))
bill=0
if(height>3):
    print("you can ride")
    age=int(input("enter your age"))
    if age<12:
        bill=150
        print("ticket price is rs150")
    elif age<18:
        bill=250
        print("ticket price is rs250")
    else:
        bill=500
        print("ticket price is rs500")
    want_photo=input("if you want photo say(Y/N)")
    if (want_photo=="Y" or want_photo=="y"):
        print(f'your ticket price is {bill+50}')

else:
    print("yoou can't ride")
print("bye")
