diagon_alley = [
    ["Entrance", "Gringotts Wizarding Bank", "Ollivanders wand shop"],
    ["Bookstore", "Pet shop", "The leaky cauldron"],
    ["Weasleys' Wizard Wheezes (joke shop)", "Post Office", "Train station"]
]

hogwarts = [
    ["Dining Hall", "Library", "Dorms"],
    ["class", "Hagrid's Cabin", "Secret path"],
    ["Hallway", "Room of Requirement", "Front doors"]
]

# player starting position
player_location = {'row': 0, 'col': 0}

def movement():
    print("Which direction do you wanna go? (north, south, east, west)")
    direction = input("Choice: ").lower()
    # Move based on user input
    if direction == "west":
        if player_location['col'] > 0:
            player_location['col'] -= 1
            print("You moved west.")
            print(f"Now you are in {diagon_alley[player_location['row']][player_location['col']]}. ")
        else:
            print("You can't move west.")
    elif direction == "east":
        if player_location['col'] < 2:  # There's only 3 columns (0, 1, 2)
            player_location['col'] += 1
            print("You moved east.")
            print(f"Now you are in {diagon_alley[player_location['row']][player_location['col']]}. ")
        else:
            print("You can't move east.")
    elif direction == "south":
        if player_location['row'] < 2:  # There's only 3 rows (0, 1, 2)
            player_location['row'] += 1
            print("You moved south.")
            print(f"Now you are in {diagon_alley[player_location['row']][player_location['col']]}. ")
        else:
            print("You can't move south.")
    elif direction == "north":
        if player_location['row'] > 0:
            player_location['row'] -= 1
            print("You moved north.")
            print(f"Now you are in {diagon_alley[player_location['row']][player_location['col']]}. ")
        else:
            print("You can't move north.")
    else:
        print("Invalid direction! Please choose north, south, east or west.")
        movement()
    if diagon_alley[player_location['row']][player_location['col']] == "Train station":
        print(f"You're in the {diagon_alley[player_location['row']][player_location['col']]}")
        print("You can choose to stay in daigon alley or you can choose to go to Hagwrats!")
        decision = input("Choice (stay/go): ")
        
def main_menu():
    # Display the current location based on player coordinates
    print(f"You are currently in the {diagon_alley[player_location['row']][player_location['col']]} of Diagon Alley.")
    print("Do you want to explore? (yes/no)")
    explore = input("choice: ")
    if explore.lower() == "yes":
        movement()
    elif explore.lower() == "no":
        print("Bye.")
    else:
        print("Invalid choice! Please choose yes or no.")
        main_menu()

# Start the game loop
main_menu()


