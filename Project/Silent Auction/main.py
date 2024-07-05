import os
import img
# Function to clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Dictionary to hold bidder names and their respective bids
bids = {}

# Function to find and print the highest bid
def find_highest_bidder():
    highest_bid = 0
    winner = ""
    for bidder in bids:
        if bids[bidder] > highest_bid:
            highest_bid = bids[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

# Display the auction logo
print(img.logo)

# Main loop to accept bids
auction_running = True
while auction_running:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bids[name] = bid
    more_bidders = input("Is there any other bidder? Type 'yes' or 'no': ").lower()
    
    # Clear the console
    clear_console()
    
    if more_bidders == "no":
        find_highest_bidder()
        auction_running = False
