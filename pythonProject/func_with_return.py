def add(a,b):
    c=a+b
    #print(c)
    return c #it will return to the caller if i am printing add(5,4)
    return # ntg will print here
    return d
print(add(5,4))# we can use return as retun with value and return without value it will return none with value will return the value
d=add(5,3)
print(d)

# title case
def formatted_string(f_name,l_name):
    a = f_name.title()
    b = l_name.title()
    print(a,b)
    return a,b
formatted_string("hema","BHEEE")#ouput will be Hema Bhee