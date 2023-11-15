import logo_art
import random
import project8_data
import os

print(logo_art.logo2)
score=0
def account_info(account):
    name=account["name"]
    description=account["description"]
    country=account["country"]
    return f"{name},{description},{country}"

def check_answer(guess,count_1,count_2):
    if count_1<count_2:
        if guess==1:
            return False
        else:
            return True
    else:
        if guess==1:
            return True
        else:
            return False
account_2=random.choice(project8_data.data)
end=True
while end:
    account_1=account_2
    account_2=random.choice(project8_data.data)
    while account_1==account_2:
        account_2 = random.choice(project8_data.data)
    print(f"compare1:{account_info(account_1)}")
    print(logo_art.logo1)
    print(f"compare2:{account_info(account_2)}")
    guess= int(input("who has more followers? Type '1' or '2':"))
    follower_count_1=account_1["follower_count"]
    follower_count_2=account_2["follower_count"]
    is_correct=check_answer(guess,follower_count_1,follower_count_2)
    os.system("cls")
    print(logo_art.logo2)

    if is_correct == True: # is_correct this also crt
        score+=1
        print(f"You are right ..... your score is {score}")
    else:
        print(f"ohh you are wrong.....your final score is {score}")
        end=False


