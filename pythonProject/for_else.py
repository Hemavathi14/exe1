"""
tuple1=(3,6,7,8,90,678)
for i in tuple1:
    print(i)
else:
    print('else block')
"""
tuple1=(3,6,7,8,90,678)
for i in tuple1:
    if i%11==0:
        print(i)
    #else:
        #print("not divisible by 11")#in this if else  block it prints the else statement 6 times rather than this we use
        #for else block
else:
    print("not divisible by 11")