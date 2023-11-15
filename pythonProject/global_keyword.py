
a=10
def display():
    global a
    a=a+1 # now it will give local variable 'a' referenced before assignment so we use global keyword
    print(a) #11
display()

# def show():
#     a=11
#     def watch():
#         global a
#         a=a+1
#         print(a)
#         # now it will give local variable 'a' referenced before assignment so we use global keyword
# #NameError: name 'a' is not defined
#         # it will search the variable globally not locally
#     watch()
#
#show()