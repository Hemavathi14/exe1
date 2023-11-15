import os

print("***************** CALCULATOR ********************")
print("")
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return (a/b)

operation_dict={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}
def calculator():
    n1 = int(input("Enter a First Number:"))
    continue_func = True
    while continue_func:
        for symbol in operation_dict:
            operator = symbol
            print(operator)
        operator = input("Pick an Operator:")

        n2 = int(input("Enter a Next Number:"))
        user_wish = operation_dict[operator]
        output = user_wish(n1, n2)
        print(f"{n1}{operator}{n2}={output}")
        user_choice = input(
            f"enter 'y' to continue with {output} or 'n' to start a new calculation or 'x' to exit:").lower()
        if user_choice == 'y':
            os.system("cls")
            n1 = output
        elif user_choice == 'n':
            continue_func = False
            calculator()

        elif user_choice == 'x':
            continue_func = False


calculator()


