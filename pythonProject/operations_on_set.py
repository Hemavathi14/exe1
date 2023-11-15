set1={1,3,4,5,6,7,8,9}
set2={1,3,4,5,6,7,8,9}
set3={3,45,78,90,23,4}
"""
print(set1.union(set2,set3))# in method the argument may be tuple
print(set1 | set2 | set3)#this is the operator to perform union. in operator the argument only a set
# multiple sets we can perform in union
#set2.union(set1)
print(set1.union((1,3,4,78,9))) # first it converts tuple into set and then its perform union
set1.update([5.0,78])
set1 |= set2 # update operator
print(set1.intersection(set2))
print(set1.intersection(set2,set3))
print(set1 & set2)
print(set1.intersection([1,3,56]))
#print(set1&set2&set3)
set1.intersection_update(set2)
print(set1)
#difference
print(set1.difference(set2))
print(set1-set2)
print(set1.difference(set2,set3))
set2.difference_update(set1,set3)
print(set1)
print(set1.difference([1.4,6,7,89,9]))
print(set1.symmetric_difference(set2))
print(set1^set2^set3)
set2.symmetric_difference_update(set1)
print(set2)
set2.symmetric_difference_update(('34','333'))
print(set2)
"""
#disjoint,subset,superset
print(set1.isdisjoint(set2))
print(set1.issuperset(set2))
print(set1.issubset([1,3,6,7]))
print(set1<=set1)
print(set1>=set2)
#del set2#it will delete the set
#print(set2)
set2.clear()#  it will delete the set elements
print(set2)