class User: #class must be in pascal naming
    #def __init__(self):

        users=0   # class variable , we can access the class variable with class name
        pwd=None
        def __init__(self,user_name,pwd): #constructor
            self.user_name=user_name #instance variable , within a constructor wee called it as instance variable
            self.pwd=pwd# we can access the instance variable using object name
            User.users += 1
        def register(self):
            print("Registering....."+self.user_name)
        def login(self):
            print("logging inn........"+self.user_name)








































































# instructor_1=Instructor()
# print(type(instructor_1))
# instructor_1.name="hema"#attribute
# instructor_1.address="india"
# #print(name) now it is syntax error
# print(instructor_1.name)
# instructor_2=Instructor()
# instructor_1.name="ema"#attribute
# instructor_1.address="india"
# print(instructor_2.name) #this way is not easy

# class CarDesign:
#     pass
# Audi=CarDesign()
# BMW=CarDesign()