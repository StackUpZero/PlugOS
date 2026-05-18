
cash = 100
reputation = 0
day = 1
weed = 0
weed_buy_price = 20
weed_sell_price = 25
running = True

while running:
    print("1. Check stats\n2. Do small job\n3. Buy 1 Weed\n4. Sell 1 Weed\nq. Quit")
    choice = input("Choose: ")
    
    if choice == "1":
        print()
        print(f"Cash: £{cash}")
        print(f"Reputation:{reputation}")
        print(f"Day:{day}")
        print(f"Weed:{weed}")
        print()

    elif choice == "2":
        print()
        print("You did a small Job!")
        cash += 25
        reputation += 1
        day += 1
        print()
        
    elif choice == "3":
        if cash >= weed_buy_price:
            print()
            cash -= weed_buy_price
            weed += 1
            print("Item Brought\n+1 Weed")
            print()
        else:
            print()
            print("You do not have enough cash.")
            print()
    
    elif choice == "4":
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
            
    
    
    
    elif choice == "q":
        print("Quit")
        running = False
        
    else:
        print("Invalid choice")
        print()