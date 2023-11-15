def func1(a,b):
    c=a+b
    print(c)

output3=func1(5,6)
print(output3) #now it will return none coz in every func they return mplicitely to caller func

def func2(x):
    output2=x+1
    return output2

def func1(a,b):
    c=a+b
    return c

output=func1(5,6)
output2=func2(output)
print(output2)