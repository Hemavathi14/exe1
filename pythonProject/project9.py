menu={
    "latte":{
        "ingredians":{

            "coffee_powder": 25,
            "creamy_milk": 150,
            "hot_water" : 200,
            "sugar" : 100
        },
        "cost":200
    },
    "cappucino":{
        "ingredians":{
            "coffee_powder": 50,
            "creamy_milk": 200,
            "hot_water" : 100,
            "sugar" : 100

        },
        "cost":150
    },
    "espresso":{
        "ingredians": {
        "coffee_powder": 50,
        "hot_water": 100
        },
        "cost": 100
    },
    "coffee":{
        "ingredians":{
            "milk": 100,
            "coffee_powder": 50,
            "sugar":50
        },
        "cost":50
    }
}

choice_list={
    "coffee":50,
    "espresso":100,
    "cappucino":150,
    "latte":200
}
profit=0
resources={
    "milk": 500,
    "coffee_powder": 500,
    "creamy_milk": 500,
    "hot_water" : 1000,
    "sugar" : 500
}

print("****************************************")
print("COFFEE VENDING MACHINE")
print("****************************************")
print("******COST DETAILS******\nlatte=200Rs\ncappucino=150Rs\nespresso=100Rs\ncoffee=50Rs\n************************")
print("Enter 'off' for off the machine\nEnter 'resource' for check the Resources")
def check_resources(order_ingredians):
    for item in  order_ingredians:#'ingredians': {'milk': 100, 'coffee_powder': 50, 'sugar': 50}
        if order_ingredians[item]>resources[item]:
            print(f"sorry there is not enough {item}")
            return False
    return True
def process_coins():
    print("please insert coins:")
    coins_5=int(input("How many 5Rs.coins ?? "))*5
    coins_10=int(input("How many 10Rs.coins ?? "))*10
    coins_20=int(input("How many 20Rs.coins ?? "))*20
    paid_amount=coins_5+coins_10+coins_20
    return paid_amount

def is_payment_successful(money_received,coffee_cost):
    if money_received>=coffee_cost:
        global profit
        profit += coffee_cost
        change=money_received-coffee_cost
        print(f"Here is your Rs{change} in change")
        return True
    else:
        print("sorry that's not enough money. Money refunded")
        return False
def make_coffee(coffee_name,coffee_ingredians):
    for item in coffee_ingredians:#{'milk': 100, 'coffee_powder': 50, 'sugar': 50
        resources[item] -=coffee_ingredians[item]
    print(f"Here is your {coffee_name} ☕....Enjoy ")


is_on=True
while is_on:
    choice=input("what would you like (latte/espresso/cappucino/coffee):").lower()
    if choice=='off':
        is_on=False
    elif choice=='resources':
        print(f"hot water={resources['hot_water']}ml")
        print(f"milk={resources['milk']}ml")
        print(f"creamy milk={resources['creamy_milk']}ml")
        print(f"coffee powder={resources['coffee_powder']}gm")
        print(f"sugar={resources['sugar']}ml")
    else:
        coffee_type=menu[choice]#latte
        #print(coffee_type)
        if check_resources(coffee_type["ingredians"]):#fn
            payment=process_coins()
            if is_payment_successful(payment,coffee_type["cost"]):# user paid amount,150
                make_coffee(choice,coffee_type["ingredians"])#coffee,{'milk': 100, 'coffee_powder': 50, 'sugar': 50}

