#1st we have to import the class
from oop_concept_class_obj import User
user1=User("hema","6576hghb")#object
user2=User("bhee","657hfghv")
user3=User("hgvn","68njhn")

user1.register()
user2.login()
print(user1.pwd)
print(user2.user_name)
print(User.users)#we can access the class variable with class name
# sometimes it acts like wired , we can access or change using object but we have to avoid iit
user1.users=10
print(user1.users) #10
print(User.users)#3