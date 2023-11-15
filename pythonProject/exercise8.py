year=int(input("enter the year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("this is leap year")
        else:
            print("not a leap year")
    else:
        print("this is  a leap year")
else:
    print("not a leap year")
    # i am done but this logic new for me