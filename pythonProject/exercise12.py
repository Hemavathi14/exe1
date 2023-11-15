
import random
names=input("enter your names seperated with whitespace:")
names_splitted=names.split(' ')
print(names_splitted)
length=len(names_splitted)
#who=random.choice(names_splitted)
#print(who,"will pay the bill") # im done this only
choice=random.randint(0,length-1)
choice_picked=names_splitted[choice]
print(choice_picked,"will pay the bill")

names=['hema','hemavathi']
length=len(names)
print(names[length-1])


