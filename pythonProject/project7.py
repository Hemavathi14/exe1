import random
import logo_art
def guess_word(num,lives):

        while lives:
            print(f"you have {lives} lives remaining to guess the number.....!")
            guessed_num=int(input("Make a guess:"))

            if guessed_num>num:
                print("Your Guess is too high")
                lives-=1
                print("Guess again")
            elif guessed_num<num:
                print("Your Guess is too low")
                lives -= 1
                print("Guess again")
            elif num==guessed_num:
                print("Your Guess is correct")
                lives=False
                break
        else:
            print("Oh Noo.....Out of lives")

level_dict={
    "easy":10,
    "hard":5
}
lives=0
print(logo_art.logo)
print("Let me think a number between 1 to 50")
level=input("Choose level of difficulty..........Type 'easy' or 'hard'\n").lower()
number=random.randint(1,51)
# print(number)
lives=level_dict[level]
#print(lives)
guess_word(number,lives)