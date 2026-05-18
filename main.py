cash = 100
reputation = 0
day = 1

running = True

while running:
    print("1. Check stats\n2. Do small job\n3. Quit")
    choice = input("Choose: ")
    
    if choice == "1":
        print("Cash:", cash)
        print("Reputation:", reputation)
        print("Day:", day)
        print()

    elif choice =="2":
        print("You did a small Job!")
        cash += 25
        reputation += 1
        day += 1
        print()
        
    elif choice == "3":
        print("Quit")
        running = False
        
    else:
        print("Invalid choice")
        print()