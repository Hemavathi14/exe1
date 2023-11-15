print(len("hemavathi"))
print(len("123455"))
#print(len(12345))type error give proper input , len fun cal string length only
length=len("hemavathi")
print(length)
#print("your name has "+length+"characters")
#we cant concatinate string and int values.....TypeError: can only concatenate str (not "int") to str
#the soln is convert lenth into str values
print("your name has "+str(length)+" characters")
print(type(length))
new_length=str(len("hgsdhdgd"))
print(type(new_length))
###
int()
float()
str()
###
print(10+10)
print("10"+"10")
print(int("10")+int("10"))
print(10+float("10"))
name = "hema"
#print(10+int(name))#ValueError: invalid literal for int() with base 10: 'hema'


