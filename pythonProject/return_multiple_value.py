
import statistics
def mean_median_mode(list_1):
 #return statistics.mean(list_1),statistics.median(list_1),statistics.mode(list_1) # now it will return output as tuple
 return [statistics.mean(list_1), statistics.median(list_1), statistics.mode(list_1)]#now it will return as list
 #whatever you write after retuern statement it won't be executed.......
 print("end of function.....")

result=(mean_median_mode([3,4,45,3,2,1,89]))
print(result)
a,b,c=(mean_median_mode([3,4,45,3,2,1,89]))
print(f"The mean is{a}\n Median is {b}\nMode is {c}")

# we can use multiple return statement in single func in single return statement we can give multiple values
def add(a,b):
    if a==0 & b==0:
        return "you entered both values are zero" #we can give here statements also
    else:
        return a+b

var1=int(input("Enter the first variable\n"))
var2=int(input("Enter the second variable\n"))
result=add(var1,var2)
print(result)

def title_case(f_name,l_name):
    empty_str=""
    if f_name=="" and l_name=="":
        return "you entered nothing"
    else:
        formatted_fname=f_name.title()
        formatted_lname=l_name.title()
        return formatted_fname,formatted_lname

first_name=input("Enter your first name")
last_name=input("Enter your first name")
result=(title_case(f_name=first_name,l_name=last_name))
print(result)