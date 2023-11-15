

try: # give doubtful code in try block
    num=int(input("Enter Numerator:"))
    den = int(input("Enter Denominator:"))
    result= num/den

except ZeroDivisionError as e:
    print(e)
    print("You Cannot divide by Zero..")
except ValueError as e:
    print(e)
    print("Enter numbers Only..")
except Exception as e : # if error occurs in try block it comes to except block
# for every error it comes to except block don't give like that give specific exceptions
    print(e)
    print("Some Error Occurs")
#  as e  is used for catch the error message we can print the  exact error msg
else:
    print(result) # else block is execute there is no error only ,if error occurs this block doesn't execute

finally:
    print(" always execute ") # this block executes always , if error occure or don't
 #try to avoid error on getting input from user .
