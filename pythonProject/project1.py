import logo_art
#print("welcome to the Game ")
print(logo_art.logo3)
print("\n 0 for Rock \n 1 for Paper \n 2 for Scissors\n")

user_choice=int(input("Enter your choice (0/1/2):"))
import random
computer_choice=random.randint(0,2)
print("Computer Choice:",computer_choice)
if computer_choice==2 and user_choice==0:
    print('you Win')
elif computer_choice==0 and user_choice==2:
    print('you Lose')
elif computer_choice>user_choice:
    print('you Lose')
elif computer_choice<user_choice:
    print('you Win')
elif computer_choice==user_choice:
    print("Match draw")
else:
    print('wrong input')

