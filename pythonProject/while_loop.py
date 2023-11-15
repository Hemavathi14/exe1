"""
count=1
while count<6:
    count+=1
    print(count)
    if count==3:
        break
else:
    print('out from loop')

count=5
while count>0: count-=1;print(count)
else:
    print('out from loop')

number=int(input('enter a number (-1 to quit)'))
while number!=-1:
    print(number)
    number = int(input('enter a number (-1 to quit)'))
else:
    print('out from loop')
print('byeeee')
#-1 is the special sentinel value
while True:
    print(count)
    count+=1
    if count==5:
        break
else:
    print('in else block')
print('out from loop')
"""
number=int(input('enter a number (0 to quit):'))
count=0
while number!=0:
    count+=number
    number = int(input('enter a number (0 to quit):'))
print(count)