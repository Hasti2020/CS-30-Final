###############################################################################
'''
This is a short house quiz function that will assign the player into the
house that they earn the most points in, and if the quiz ends up being a tie,
the player will be assigned into the default Harry Potter house, Gryfindor.
This function would use external file to be used as the quiz.
'''
###############################################################################
# Imports and Global Variables-------------------------------------------------
import time


def house_sort(): 
    '''
    This function will generate a short house quiz that will assign the player
    into the best fitted house by seeing which house corresponds to their 
    majority answers
    '''
    print('------------HOUSE SORTING QUIZ------------')    
    quiz = open("house.txt", "r") # read the house.txt file
    line = quiz.readline()
    sorting = line.split(",") # split the lines at ','
    # Color codes using ANSI escape sequences
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    ENDC = "\033[0m" # Reset to default
    sorting_answers = []
    while sorting[0] != "End": # when position 0 of the line is not the 'end'
        print(sorting[0]) # prints the first question (line before the ,)
        print("1. " + str(sorting[1])) # prints 1st option (position 1)
        print("2. " + str(sorting[2])) # prints 2nd option (position 2)
        answer = input("Answer (1 or 2?): ")
        print("")
        if answer == "1":
            # adds the house that corresponds with the answer to the list
            sorting_answers.append(sorting[3]) 
            line = quiz.readline()
            sorting = line.split(",")
        elif answer == "2":
            sorting_answers.append(sorting[4])
            line = quiz.readline()
            sorting = line.split(",")
        else: # if players' input is not valid
            answer = input("The sorting hat is confused by your mind" 
            + "... (enter)")
    # counts the letters in the sorting_answers to find the 1 with the most
    g = sorting_answers.count(" G")    
    s = sorting_answers.count(" S")
    h = sorting_answers.count(" H")
    r = sorting_answers.count(" R")

    if g == 3: # if player has the Gs in their sorting_answers
        # player is assigned to gryffindor
        print(RED + "You are in...GRYFINDOR" + ENDC)
        print(RED + "💥 The bold, the brave, the ones who run *straight* "
            + "into 'danger yelling 'YOLO!' — hope you packed a spare "
            + "wand." + ENDC)
    elif s == 3: # if player has the Ss in their sorting_answers
        # player is assigned to slytherin
        print(GREEN + "You are in...SLYTHERIN" + ENDC)
        print(GREEN + "🐍 Ambitious, clever, and a *tiny bit* dramatic. "
            + "You’re the main character, obviously — plotting your way"
            + " to magical world domination since breakfast." + ENDC)
    elif r == 3: # if player has the Rs in their sorting_answers
        # player is assigned to ravenclaw
        print(BLUE + "You are in...RAVENCLAW" + ENDC)
        print(BLUE + "🧠 Big brain energy alert! You read *for fun* and "
              + " correct people’s grammar mid-duel. Just don’t forget "
              + "where you put your wand… again." + ENDC)
    elif h == 3: # if player has the Hs in their sorting_answers
        # player is assigned to hufflepuff
        print(YELLOW + "You are in...HUFFLEPUFF" + ENDC)
        print(YELLOW + "🌻 Sweet, loyal, and lowkey the only reason "
              + "Hogwarts hasn’t burned down. You bake cookies *and* win"
              + " duels with kindness (and maybe a frying pan)." + ENDC)
    else: # if player's result is a tie, they default to gryffindor
        print(RED + "You are in...GRYFINDOR" + ENDC)
        print(RED + "💥 The bold, the brave, the ones who run *straight* "
            + "into 'danger yelling 'YOLO!' — hope you packed a spare "
            + "wand." + ENDC)
    
    time.sleep(1) # waits 1 second to print following texts
    print("\n🎉 The great hall erupts in applause as you walk to your house"
          + " table, your new housemates cheering you on.")
    time.sleep(1)
    print("\n🧙‍♂️ Dumbledore: 'Welcome, welcome, one and all!")
    time.sleep(1)
    print("\nDumbledore: This year... things are going to get a tad more "
          + "*interesting*.'")
    time.sleep(1)
    print("Dumbledore: 'I am pleased to announce that this year, Hogwarts "
          + "will be hosting the legendary... **Diwizard Tournament!**'")
    time.sleep(1)
    print("To prepare, attend your classes, practice spells, brew potions,"
          + " and maybe read a book for once.")
    time.sleep(1)
    print("When — and *only* when — you feel ready... make your way to the "
    + "*Front Doors* and seek out Professor McGonagall.")
    time.sleep(1)
    print("Tell her you wish to enter the Diwizard Tournament.")
    time.sleep(1)
    print("But be warned — you only get one shot. So be wise, be ready, and "
    + "for Merlin’s sake, don’t challenge a basilisk with just a toad.'")
    time.sleep(1)
    print("\n🍰 Suddenly, desserts appear. The students cheer, but your " 
    + "mind is racing...")
    time.sleep(1)
    print("You're not just here for classes. You're here to prove yourself.")
    time.sleep(1)
    print("The Diwizard Tournament awaits. But first — it's time to get" 
    + " ready.")

