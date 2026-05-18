cash = 100
reputation = 0
day = 1
weed = 0
weed_price = 20
running = True

while running:
    print("1. Check stats\n2. Do small job\n3. Buy 1 Weed\nq. Quit")
    choice = input("Choose: ")
    
    if choice == "1":
        print()
        print("Cash:", cash)
        print("Reputation:", reputation)
        print("Day:", day)
        print("Weed:", weed)
        print()

    elif choice =="2":
        print()
        print("You did a small Job!")
        cash += 25
        reputation += 1
        day += 1
        print()
        
    elif choice == "3":
        if cash >= weed_price:
            print()
            cash -= weed_price
            weed += 1
            print("Item Brought\n+1 Weed")
            print()
        else:
            print()
            print("You do not have enough cash.")
            print()
            
    elif choice == "q":
        print("Quit")
        running = False
        
    else:
        print("Invalid choice")
        print()