cash = 100
reputation = 0
day = 1

running = True

while running:
    choice = input("Choose: ")
    
    if choice == "1":
        print("Cash:", cash)
        print("Reputation:", reputation)
        print("Day:", day)

    elif choice == "2":
        print("Quit")
        running = False
    else:
        print("Invalid choice")