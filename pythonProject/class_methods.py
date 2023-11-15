class Instructor:
    followers=0
    def __init__(self,name,address): #attributes
        self.name=name # here we can give any name in the place of self.    but afte equal we give attribte same as it is
        self.address=address
    def display(self,sub_name):#defining a method
        print("hi "+self.name + " i am teach "+sub_name)
      # self.name is a attribute so we use like that
    def update_followers(self,follower_name):
        self.followers += 1

instructor1=Instructor("hema","vellore")
print(instructor1.name)
instructor1.display("python")# calling a method
instructor1.update_followers("bhee")
print(instructor1.followers)