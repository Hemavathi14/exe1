set1={1,45,69,True,'hema',78.100}
set2={}# this is dictionary  if you want to create a empty set
set3=set()
print(set2)
print(type(set1))
print(type(set2))
print(len(set1))
set1.add(67)
set1.remove(78.1)
set1.discard(1) #the difference between remove and discard is if you remove which does not present in the set it will return
#the error in remove but in discard it doesn't show error it will print set values
print(set1)
#set1.clear()#it will clear the all the values
print(set1.pop())#it will remove any random item on the set and it will return the value also
print(set1.add((13,45,78)))
#we cant add list because it is mutable 

