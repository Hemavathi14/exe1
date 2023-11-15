print("""
╦ ╦╔═╗╦  ╔═╗╔═╗╔╦╗╔═╗  ╔╦╗╔═╗  ╔═╗╔═╗╔═╗╔═╗╦ ╦╔═╗╦═╗╔╦╗  ╔═╗╔═╗╔╗╔╔═╗╦═╗╔═╗╔╦╗╔═╗╦═╗
║║║║╣ ║  ║  ║ ║║║║║╣    ║ ║ ║  ╠═╝╠═╣╚═╗╚═╗║║║║ ║╠╦╝ ║║  ║ ╦║╣ ║║║║╣ ╠╦╝╠═╣ ║ ║ ║╠╦╝
╚╩╝╚═╝╩═╝╚═╝╚═╝╩ ╩╚═╝   ╩ ╚═╝  ╩  ╩ ╩╚═╝╚═╝╚╩╝╚═╝╩╚══╩╝  ╚═╝╚═╝╝╚╝╚═╝╩╚═╩ ╩ ╩ ╚═╝╩╚═""")
print(" ")
import random
from random import sample
#list1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters=int(input('How many letters do you want.....?'))
alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghjiklmnopqrstuvwxyz'
alpha_str=sample(alphabets,letters) # ['C', 'D', 'd'],3
my_str=''
for i in alpha_str: #i=alphabets
    my_str+=''+i #CDd
sym=int(input('How many symbols do you want....?'))
symbols='!@#$%^&*()'
selected_symbol=sample(symbols,sym) #['@','&','*']
my_sym=''
for j in selected_symbol:# j= symbols
    my_sym+=''+j
numbers='0123456789'
num=int(input('how many numbers do you want..?'))
num_selected=sample(numbers,num)
num_str=''
for k in num_selected:
    num_str+=''+k
s=(my_str+my_sym+num_str)
s=''.join(random.sample(s,len(s)))
print("Your Password is :",s)





