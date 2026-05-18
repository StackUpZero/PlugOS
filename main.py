cash = 100
reputation = 0
day = 1

running = True

while running:
    choice = input("Choose: ")
    
    if choice == "i":
        print(cash)
        print(reputation)
        print(day)
    
    if choice == "quit":
        running = False