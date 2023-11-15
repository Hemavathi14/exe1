
count=1
while count<=10:
    print(count)
    count+=1
    if count==4:
        break
    print('hi')
print('out from loop')

list1=['hi','hello','welcome']
names=['krish','ram','madhav']
for item in list1:
    for name in names:
        print(item,name)
        if item=='hello' and name=='ram':
            break
    print('out from inner loop')
print('out from outer loop')43q dvh'
# count=1
# while count<=10:
#     print(count)
#     count+=1 # after 3 the count becomes 4 so iy doesn't print hi
#     if count==4:
#         continue
#     print('hi')
# print('out from loop')
#
# for i in range(1,11):
#     if i==7:
#         continue
#     else:
#         print(i)
#
# for i in range(1,11):
#     pass