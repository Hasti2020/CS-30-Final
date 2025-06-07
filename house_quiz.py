def house_sort():     
    import random
    quiz = open("house.txt", "r")
    line = quiz.readline()
    sorting = line.split(",")
    # Color codes using ANSI escape sequences
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    ENDC = "\033[0m"  # Reset to default

    house_list = []

    while sorting[0] != "End":
        print(sorting[0])
        print("1. " + str(sorting[1]))
        print("2. " + str(sorting[2]))
        answer = input("Answer (1 or 2?): ")
        print("")
        if answer == "1":
            house_list.append(sorting[3])
            line = quiz.readline()
            sorting = line.split(",")
        elif answer == "2":
            house_list.append(sorting[4])
            line = quiz.readline()
            sorting = line.split(",")
        else:
            answer = input("Try again (enter)")
        
    #print(house_list) # delete when game is done
    g = house_list.count(" G")    
    s = house_list.count(" S")
    h = house_list.count(" H")
    r = house_list.count(" R")

    if g == 3:
        print(RED + "You are in...GRYFINDOR" + ENDC)
        print(RED + "💥 The bold, the brave, the ones who run *straight* into danger yelling 'YOLO!' — hope you packed a spare wand." + ENDC)
    elif s == 3:
        print(GREEN + "You are in...SLYTHERIN" + ENDC)
        print(GREEN + "🐍 Ambitious, clever, and a *tiny bit* dramatic. You’re the main character, obviously — plotting your way to magical world domination since breakfast." + ENDC)
    elif r == 3:
        print(BLUE + "You are in...RAVENCLAW" + ENDC)
        print(BLUE + "🧠 Big brain energy alert! You read *for fun* and correct people’s grammar mid-duel. Just don’t forget where you put your wand… again." + ENDC)
    elif h == 3:
        print(YELLOW + "You are in...HUFFLEPUFF" + ENDC)
        print(YELLOW + "🌻 Sweet, loyal, and lowkey the only reason Hogwarts hasn’t burned down. You bake cookies *and* win duels with kindness (and maybe a frying pan)." + ENDC)
    else:
        print(RED + "You are in...GRYFINDOR" + ENDC)
    print("\n🎉 The great hall erupts in applause as you walk to your house table, your new housemates cheering you on.")
    print("\n🧙‍♂️ Dumbledore: 'Welcome, welcome, one and all!")
    print("Dumbledore: This year... things are going to get a tad more *interesting*.'")
    print("Dumbledore: 'I am pleased to announce that this year, Hogwarts will be hosting the legendary... **Diwizard Tournament!**'")
    print("To prepare, attend your classes, practice spells, brew potions, and maybe read a book for once.")
    print("When — and *only* when — you feel ready... make your way to the *Front Doors* and seek out Professor McGonagall.")
    print("Tell her you wish to enter the Diwizard Tournament.")
    print("But be warned — you only get one shot. So be wise, be ready, and for Merlin’s sake, don’t challenge a basilisk with just a toad.'")
    print("\n🍰 Suddenly, desserts appear. The students cheer, but your mind is racing...")
    print("You're not just here for classes. You're here to prove yourself.")
    print("The Diwizard Tournament awaits. But first — it's time to get ready.")
