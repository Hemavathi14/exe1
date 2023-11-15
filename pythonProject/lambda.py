# normal program
def add_ten(num):
    return num+10
print((add_ten(6)))

product=lambda a,b,c:a*b*c
print(product(5,4,6))

square=lambda a,b: "yes" if a == b else "no"
print(square([1,2,3],[1,2,3]))
#(item code,item name , item price)
items=[(1234,"cactus plant",200),(5678,"book",359),(7890,"phone",23000),(2345,"watch",500),(3467,"chudi",1000)]#list of tuple
items.sort()
print(items)# defaultly it sorted with 1st one
items.sort(key=lambda item:item[1])
print(items)#sorting with name
items.sort(key=lambda item:item[2])
print(items)#sorting with price
items.sort(key=lambda item:item[1], reverse=True)
print(items)#ascending order

items=((1234,"cactus plant",200),(5678,"book",359),(7890,"phone",23000),(2345,"watch",500),(3467,"chudi",1000))#tuple of tuples
#items.sort()#this is meththod , inga items . sort so item ah dha sort paannum nu theryum but sorted func anga namma dha kudukkanum
print(items)#AttributeError: 'tuple' object has no attribute 'sort' tuple is immutable so we cant change the order directly
print(sorted(items))
print(items)# it doesn't affect the original tuple
print(sorted(items,key=lambda item:item[1]))
print(items)
