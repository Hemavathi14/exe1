# to create a file
#f1=open("file_1.txt","x") #x is to create a file ,if we run again it will give you a error, FileExistsError: [Errno 17] File exists: 'file_1.txt' becoz this file nmae already exists
f1=open("file_1.txt","r") #it points begining of the file
f1=open("file_1.txt")# by default it is in read mode
data=f1.read()
print(data)
f1.close()
# write mtd
# f2=open("file2.txt","r+")
# print(f2.tell())
# #f2.write("welcome you all ")
# #print(f2.read()) # error
# #read and write mode r+
# #f2=open("file2.txt","r+")
# f2.write(" Hi i am hema ")
# print(f2.tell())
# print(f2.read())
f2=open("file2.txt","w+")
print(f2.tell())
f2.write(" hello you are a brilliant girl you look awesome ")
print(f2.tell())
f2.write("hii hema")
f2.seek(0)#moving file pointer to begining
data=f2.read()
print(data)#it shows nothing in the console bcoz the file pointer is in the end ...
print(f2.tell())

# write means it will erase the previous witten once
#in append mode it will not erase a previous one it will append to it

# f3=open("file_3.txt","a") #only append
# f3.write(" happy birthday to youuu")
#print(f3.read())# it is not readable
f3=open("C:\Users\elcot\Desktop.txt","rb") # a+ - both append and readable
#f3.write("YOU ARE A STRONG GIRL ")
#f3.seek(0)
print(f3.read())




