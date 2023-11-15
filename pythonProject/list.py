num=[1,2,3,4,5,6,7,8,8,-9]
names=['hema','bheee','hemavathi']
mix_list=[1,'shhdgjs',True,10.10]
print(num,names,mix_list)
#we can access list by index,,,,,
print(num[4])
print(num[0:4])#this is list slicing [0:4] it will print full list
print(num[0:])
print(num[1:4]) #here 1 is index and 4 is  length
print(num[-3])#negative index also applicable it's starts from backward it starts from -1
print(num[:])# bydefault it assumes value
print(num[:4])
print(num[0:5:1])#it will jump 1st element
print(num[0:5:2])#it will jump 2nd element  skip the 1st element
print(num[0:5:3])# that 5 indicates end it doesn't print after the values
print(num[0::3])# now it has noo end
#sorting
num.sort()#you have to start first and then print otherwise it will give you none
print(num)
print(num.sort())
num.reverse()
print(num)
print(max(num))
print(min(num))
#we can't apply sort for mix list
#append - at the end of the list we can add one element at a time
num.append(56)
print(num)
#if we want to add ai specific index use insert we can add 2 arg also
num.insert(2,78)
print(num)
#extend is atdd at the end of the list ......here we can addd more than one element at a time
num.extend([56,78,90])
#insert
num[7]=790
num[1:4]=[67,89,890]
num.remove(4)
print(num)
#pop means remove the last elemennt
print(num.pop())
print(num.pop(6))