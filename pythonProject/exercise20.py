student_marks={
    "hema":95,
    "madhav":85,
    "aishu":75,
    "rahuk":65,
    "aniket":99,
    "prem":34,
    "ram":56,
    "sham":49
}
student_grades={}
for student in student_marks:#hema
    i=student_marks[student]#95
    if i >= 91:
        student_grades[student]="A+"
    elif i >=81 and i<=90:
        student_grades[student] ="A"
    elif i >=71 and i<=80:
        student_grades[student] ="B+"
    elif  i >=61 and i<=70:
        student_grades[student] ="B"
    elif  i >=51 and i<=60:
        student_grades[student] ="C"
    elif  i >=41 and i<=50:
        student_grades[student] = "D"
    else:
        student_grades[student] = "F"


print(student_grades)
# finally done


