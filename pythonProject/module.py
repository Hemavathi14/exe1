#print(help("modules")) # it shows how many modules present in your laptop
#print(help("random")) #it shows what are func is in that module
# modules are used to increase the reusability of the code , manage the files and time saving
# two types of modules are there 1. builtin 2.user defined
# we can use modules by import key word
#import my_module
from my_module import operators as op # we can import specific func also
# we are importing the module totally (variables , func, etc)
#print(my_module.a)
op(45,7) # if we import seperate func no need to use modulename . that func we can directly use that name
# we can import more than one func also
# from my_module import a,operators,area_of_square
from my_module import * #it will import all func , vaiables
print(a)
# if the module name is big we use as keyword abd give a simple name
a,b=6,5
print(a+b)
print("a from my_module",a) # this time we want to access that a it is a bug so we use my_module.a method this is the crt way 



