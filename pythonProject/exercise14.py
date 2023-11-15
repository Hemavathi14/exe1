heights=input('enter the heightssplitted by comma')
heights_splitted=heights.split(',')
print(heights_splitted)
count = 0
for height in heights_splitted:
    count+=1
print(count)
for i in range(0,count):
    heights_splitted[i]=int(heights_splitted[i])
print(heights_splitted)
sum=0
for j in heights_splitted:
    sum=sum+j
avg=sum//count
print(avg)
#finally done it