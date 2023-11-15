#greatest num

numbers=input('enter the numbers splitted by comma:') # input as string
numbers_splitted=numbers.split(',')
print(numbers_splitted) # input converted into list
count = 0
for height in numbers_splitted:
    count+=1
print(count)
for i in range(0,count):
   numbers_splitted[i]=int(numbers_splitted[i]) # list of str converted into list of int
print(numbers_splitted)
maximum_number=numbers_splitted[0] #
for numbers in numbers_splitted:
    if numbers>maximum_number:
        maximum_number=numbers
print(maximum_number)

# i dont know the lolgic so i watch the vedio and done it