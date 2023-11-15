tuple1=(1,34,-90,"hema",True,5,78,90,100)
tuple3=(23,78,90) # it will take it as integer
# while accesing index we use square brackets
print(tuple1[4])
print(tuple1[-2])
print(type(tuple1[4])) #now the type is boolean
print(type(tuple1))#now the type is tuple
print(tuple1[1:7:3])
#nesting of tuple
tuple2=(tuple1,tuple3)
print(len(tuple2))
print(tuple2)
print(tuple2[1])
print(min(tuple3))
print(max(tuple3))
print(tuple1.count(78))
#we can access index
print(tuple1.index(90))
#if i want to convert a list to tuple
list1=[1,2,34,5,6,89]
print(tuple(list1))
tuple7=(10,)*5
print(tuple7)