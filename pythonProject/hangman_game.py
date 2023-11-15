print("Welcome to Hangman Game!!\n let's play !! " )
import random
import hangman_stages
word_list1=['apple','orange','banana','mosambi','dog','cat','lion','tiger','elephant','mango','avocado','graphes','kiwi','watermelon',
       'fig','melon','papaya','lime','bear','horse','deer','rabbit','panda']
lives=6
word=random.choice(word_list1)
#print(word)
length=len(word)
display=[]
for i in range(length):       #for letter in word: another mtd
    display+='_'                #list2+='_'
print('You have only 6 lives so try to guess the word in 6 attempts! Good luck!!')
print(display)
game_over=False
while not game_over:
    guessed_letter=input('Guess a letter:').lower()
    for position in range(length):# 0 1 2 3 4
        letter=word[position]
        if letter in guessed_letter:
            display[position]=guessed_letter
    print(display)
    if guessed_letter not in word:
        lives-=1
        if lives == 0:
            game_over=True
            print('you lose!!')
    if '_' not in display:
        game_over=True
        print("you win!!")
    print(hangman_stages.stages[lives])
















#blanks=print("'_'",end=" ")
    #blanks=print("'_'")
    #blanks.split( )
