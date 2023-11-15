
def add_new_student(Name,Roll_no,Age,Course):
    new_entry={}
    new_entry["name"] = name
    new_entry["roll_no"] =roll_no
    new_entry["age"] = age
    new_entry["course"] =course
    print(new_entry)

    student_data = [
        {
            "name": "hema",
            "roll_no": 10,
            "age": 20,
            "course": "python"
        },
        {
            "name": "bhee",
            "roll_no": 23,
            "age": 21,
            "course": "c++"
        }
    ]
    student_data.append(new_entry)
    print(student_data)
name=input("enter a name:")
roll_no=int(input("enter your roll no:"))
age=int(input("enter your age:"))
course=input("enter your course:")
add_new_student(Name=name,Roll_no=roll_no,Age=age,Course=course)

#wow i am doneeeeeeeeee eeeee