thislist=["apple","banana","kiwi","orange","pineapple","mango","grapes"]
thislist1=list(("apple","banana","kiwi","orange","pineapple","mango","grapes"))#list constructor
"""
print(thislist[-4:-1])
thislist[1:3]=["blackcurrant","watermelon"]#here replacing index 1 and 2 values
thislist[1:2]=["blackcurrant","watermelon"]#here replacing index 1 with 2 values
print(thislist)
if "banana" in thislist:
    print("true")
#insert and replacing are different
thislist1.insert(2,"mosambi")
print(thislist1)
thislist.append("cherry")
print(thislist)
thislist.extend(thislist1)
print(thislist)
thislist.remove("apple")
print(thislist)
thislist1.pop(2)
print(thislist1)
del thislist1[2:5]
print(thislist1)
thislist1.clear()
print(thislist1)
"""
list1=[]
length=len(thislist)
print(length)
for i in range(length):
    list1.append("meow")
print(list1)
