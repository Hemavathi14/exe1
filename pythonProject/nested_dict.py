# nest a dict within a dict
student_data={
    "hema":{"roll_no":10,"age":20,"course":"python"},
    "bhee":{"roll_no":23,"age":21,"course":"c++"}
}

print(student_data)
print(student_data["hema"])
print(student_data["hema"]["age"])
#adding
student_data["hema"]["phone_no"]=1234567890
print(student_data)
#deleting
del student_data["hema"]["phone_no"]
print(student_data["hema"].pop("course"))
#del didn't return anything .......pop return the value .....
print(student_data)

#nesting a list with in a dictionary
travel_data={
    "tamilnadu":["vellore","thanjavur","thiruvannamali"],
    "karnataka":["electronic city","sivaji nagar","chickpet market"]
}

print(travel_data["tamilnadu"][0])

#nesting a dict with a list
#student_data=[
 #   "hema":{"roll_no":10,"age":20,"course":"python"},
  #  "bhee":{"roll_no":23,"age":21,"course":"c++"}
#]#now it will give you a error coz it is in key:value form....

student_data=[
    {"name":"hema","roll_no":10,"age":20,"course":"python"},
    {"name":"bhee","roll_no":23,"age":21,"course":"c++"}
]#now it will give you a crt value ......

print(student_data[0]["name"])
print(student_data[0])

student_data=[
    {
        "name":"hema",
        "roll_no":10,
        "age":20,
        "course":"python"
    },
    {
        "name":"bhee",
        "roll_no":23,
        "age":21,
        "course":"c++"
    }
]#now this is more readable