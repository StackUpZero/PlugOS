##########
# Imports
##########

import random

############
# Inventory
############

cash = 100
reputation = 0
day = 1
weed = 0
weed_buy_price = 20
weed_sell_price = 25
running = True

############
# Functions
############

# Show Stats
def show_stats():
    print()
    print(f"Cash: £{cash}")
    print(f"Reputation: {reputation}")
    print(f"Day: {day}")
    print(f"Weed: {weed}")
    print(f"Weed buy price: £{weed_buy_price}")
    print(f"Weed sell price: £{weed_sell_price}")
    print()
     
# Show Menu
def show_menu():
    print("1. Show Stats")
    print("2. Do small job")
    print("3. Buy Weed")
    print("4. Sell Weed")
    print("q. Quit")
    print()
    print("Current Market")
    print(f"Weed sell price: £{weed_sell_price}")
    print(f"Weed buy price: £{weed_buy_price}")
    print()
   
# Update Prices
def update_prices():
    global weed_buy_price, weed_sell_price
    weed_buy_price = random.randint(15,30)
    weed_sell_price = random.randint(15,30)
 
# Do small job
def do_small_job():
    global cash, reputation, day
    print()
    print("You did a small Job!")
    cash += 25
    reputation += 1
    day += 1
    update_prices()
    print()

# Get Amount
def get_amount(question):
    amount = input(question)

    try:
        amount = int(amount)
    except ValueError:
        print()
        print("Please enter a valid number.")
        print()
        return None

    return amount
       
# Buy Weed
def buy_weed():
    global cash, weed, day

    amount = get_amount("How many Weed do you want to buy? ")

    if amount is None:
        return

    total_cost = weed_buy_price * amount

    if amount <= 0:
        print()
        print("Amount must be at least 1.")
        print()

    elif cash >= total_cost:
        cash -= total_cost
        weed += amount
        day += 1
        print()
        print(f"You bought {amount} Weed for £{total_cost}.")
        print(f"Your current cash is £{cash}.")
        print()
        update_prices()

    else:
        print()
        print("You do not have enough cash!")
        print()  
        
# Sell Weed
def sell_weed():
    global cash, weed, day

    amount = get_amount("How much Weed do you want to sell? ")

    if amount is None:
        return

    total_earned = weed_sell_price * amount

    if amount <= 0:
        print()
        print("Must be selling more than 0!")
        print()

    elif weed >= amount:
        weed -= amount
        cash += total_earned
        day += 1
        print()
        print(f"You sold {amount} Weed for £{total_earned}!")
        print(f"Your current cash is £{cash}.")
        print()
        update_prices()

    else:
        print()
        print("You do not have enough Weed.")
        print()
        
def check_game_over():
    global running
    if cash >= 500:
        print("You Won!")
        running = False
                        
############
# Game Loop
############

while running:
    show_menu()
    choice = input("Choose: ")
    
    if choice == "1":
        show_stats()

    elif choice == "2":
        do_small_job()
        
    elif choice == "3":
        buy_weed()
    
    elif choice == "4":
        sell_weed()
    
    elif choice == "q":
        print("Quit")
        running = False
        
    else:
        print("Invalid choice")
        print()
        
    check_game_over()
