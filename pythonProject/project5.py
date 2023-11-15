


import os
from time import sleep
def find_winner(bidder_details):
    # key_max=max(zip(auction_dict.keys(),auction_dict.values()))[1]
    # key_value=max(zip(auction_dict.keys(),auction_dict.values()))[0]
    # print(f"The winner is {key_value},and the price is {key_max}")

    highest_bid=0
    winner=""
    for bidder in auction_dict:
        bidding_price=auction_dict[bidder]
        #int(bidding_price)
        if bidding_price>highest_bid:
            highest_bid=bidding_price
            winner=bidder
    print(f" Here is the List of all the bidders:{auction_dict}")
    print(f"The winner is {winner.upper()} with a bid price {highest_bid}")

print("*****************WELCOOME TO SILENT AUCTION PROGRAM********************")

wanna_end=False
auction_dict = {}
while not wanna_end:
    name = input("Enter your Name:")
    bid = int(input("What is your Bid?:"))
    auction_dict[name] = bid
    #print(auction_dict)
    many_bidder=input("Are there any other bidders? type 'yes' or 'no':").lower()
    if many_bidder=="yes":
        os.system('cls')
        wanna_end=False
    elif many_bidder=='no':
        wanna_end=True
        find_winner(auction_dict)

    else:
        print("wrong input")



