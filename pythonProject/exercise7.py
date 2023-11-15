weight= int(input("enter your weight in kg:"))
height=float(input("enter your height in m:"))
bmi=(weight)/(height**2)
bmi=round(bmi,2)
print(bmi)
if bmi<16:
    print(" underweight-verythin")
elif bmi<16.9:
    print(" underweight-moderatethin")
elif bmi<18.5:
    print(" underweight-mildthin")
elif bmi<25:
    print("normal")
elif bmi<30:
    print("obse")
else:
    print("enter correct values")