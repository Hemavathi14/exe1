def multiply(*numbers):# now it will become a tuple here y tuple means tuples are immutable
    c=1
    print(numbers[2])
    for i in numbers:
        c=c*i
    print(c)

multiply(1,2,3)

import math
def paint_calc(height,width,cover):
    area=h*w
    no_of_cans=area/7
    final_value=math.ceil(no_of_cans)
    print(final_value)
h=int(input("enter the height of the wall in meter:"))
w=int(input("enter the width of the wall in meter:"))
coverage=7

paint_calc(height=h,width=w,cover=coverage)


#no_of_cans(height=int(input("enter the height")),width=int(input("enter the height")))

