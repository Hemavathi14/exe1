# love calculator
her_name = input(" enter her name.....")
her_name = her_name.lower()
him_name = input(" enter him name.....")
him_name = him_name.lower()
name = him_name + her_name
t = (name.count('t'))
u = (name.count('u'))
e = (name.count('e'))
r = (name.count('r'))
l = (name.count('l'))
o = (name.count('o'))
v = (name.count('v'))
e = (name.count('e'))
n1 = (t + u + r + e)
n2 = (l + o + v + e)
percentage = str(n1) + str(n2)
print(f"percentage is {percentage}% ")
if percentage < "10" or percentage > '90':
    print(f"you are score is{percentage}\n you go together like a blast")
elif percentage >= '40' and percentage <= '50':
    print(f"you are score is{percentage} you are alright together ")
else:
    print(f" you are score is {percentage}")

# wowwwwwwwwww i'm done