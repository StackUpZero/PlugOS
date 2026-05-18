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
    print()
     
# Show Menu
def show_menu():
    print("1. Show Stats")
    print("2. Do small job")
    print("3. Buy 1 Weed")
    print("4. Sell 1 Weed")
    print("q. Quit")
    
# Do small job
def do_small_job():
    global cash, reputation, day
    print()
    print("You did a small Job!")
    cash += 25
    reputation += 1
    day += 1
    print()


# Buy 1 Weed
def buy_weed():
    global cash, day, weed
    if cash >= weed_buy_price:
        print()
        cash -= weed_buy_price
        weed += 1
        print("Item Bought\n+1 Weed")
        print()
    else:
        print()
        print("You do not have enough cash.")
        print()
            
# Sell 1 Weed
def sell_weed():
    global cash, weed
    if weed > 0:
        weed -= 1
        cash += weed_sell_price
        day += 1
        print()
        print(f"You sold 1 Weed for £{weed_sell_price}.")
        print(f"You currently have £{cash}.")
        print()
    else:
        print()
        print("You do not have enough Weed.")
        print()
            

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
        
        
