var_1=1234567899#any long value we can take ,it will print
#there is no range limit is only the memory of the system
var_2=10.1
print(type(var_2))
print(var_1)
print(var_1+var_2)
var3=0o123#prefix is octal it print equivalent decimal value
print(var3)
print(type(var3))
name="hemavathi"
name2="balaraman"
print(type(name))
print(name[1+2])
print(name+name2)
#i wanna print like this "hema's "lectures"
# one way print("hema's ""lectures")
# another way single code and double code having special meaning in python so if you skip this special
# -meaning, we can do the task before the codes use backslash to skip the special meaning
print("hema\'s \n \"lectures\"") #\n means new line
print("hema\'s \\n \"lectures\"")#\\n it will skip the special meaning
print(5*"hema\'s \n \"lectures\"")
var=True #here we dont use small t if we use it will show name error
print(var)
print(type(var))
a=1
b=2
var_1=(a>b)
print(var_1)