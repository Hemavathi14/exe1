python_questions = {
    "1.What is the correct way to declare a variable in Python?": {
        "options": {
            "A": "variable = 42",
            "B": "var 42 = variable",
            "C": "42 = variable",
            "D": "Variable = 42",
        },
        "answer": "A"
    },
    "2.How do you comment multiple lines in Python?": {
        "options": {
            "A": "# This is a comment",
            "B": "''' This is a comment '''",
            "C": "/* This is a comment */",
            "D": "// This is a comment",
        },
        "answer": "B"
    },
    "3.What is the output of 'print(3 * 'abc')'?": {
        "options": {
            "A": "abcabc",
            "B": "9",
            "C": "TypeError",
            "D": "abcabcabc",
        },
        "answer": "D"
    },
    "4.Which data type is used to store a sequence of characters in Python?": {
        "options": {
            "A": "int",
            "B": "str",
            "C": "list",
            "D": "tuple",
        },
        "answer": "B"
    },
    "5.How can you check the length of a list named 'my_list'?": {
        "options": {
            "A": "length(my_list)",
            "B": "count(my_list)",
            "C": "len(my_list)",
            "D": "size(my_list)",
        },
        "answer": "C"
    },
    "6.Which of the following is not a valid data type in Python?": {
        "options": {
            "A": "int",
            "B": "float",
            "C": "boolean",
            "D": "character",
        },
        "answer": "D"
    },
    "7.What is the result of '5 // 2' in Python?": {
        "options": {
            "A": "2.5",
            "B": "2",
            "C": "2.0",
            "D": "2.5 (as a float)",
        },
        "answer": "B"
    },
    "8.Which keyword is used to exit a loop prematurely in Python?": {
        "options": {
            "A": "break",
            "B": "exit",
            "C": "stop",
            "D": "return",
        },
        "answer": "A"
    },
    "9.What is the purpose of 'elif' in an 'if-elif-else' statement?": {
        "options": {
            "A": "It signifies the end of the conditional statement",
            "B": "It is used for exception handling",
            "C": "It is an alternative to 'else'",
            "D": "It allows you to check multiple conditions sequentially",
        },
        "answer": "D"
    },
    "10.Which method is used to remove an item from a list in Python?": {
        "options": {
            "A": "delete()",
            "B": "remove()",
            "C": "discard()",
            "D": "pop()",
        },
        "answer": "B"
    }
}
import math
print("*****************************************")
print("WELCOME TO MY QUIZ GAME")
print("*****************************************")
# To access the questions and answers, you can iterate through the dictionary:
score=0
qn_count=1
length=len(python_questions)
while length:
    for question, data in python_questions.items(): #data-{'options': {'A': 'delete()', 'B': 'remove()', 'C': 'discard()', 'D': 'pop()'}, 'answer': 'B'}
        print(question)
        options = data["options"]
        #print(options)#{'A': 'delete()', 'B': 'remove()', 'C': 'discard()', 'D': 'pop()'}
        for option, answer in options.items():
            print(f"{option}) {answer}")
        user_choice = input("Enter your choice(A/B/C/D):").upper()
        if user_choice == data['answer']:
            score += 1
            print("Correct Answer")
            print(f"Your Current Score is {score}/{qn_count} ")
            # print(f"Correct Answer: {data['answer']}\n")
        else:
            print("Incorrect Answer")
            print(f"The correct Answer is :{data['answer']}")
            print(f"Your Current Score is {score}/{qn_count} ")
        length -= 1
        qn_count += 1
    percentage= (score/ (qn_count-1))*100
    print(f"Your Percentage is {math.ceil(percentage)}%")
