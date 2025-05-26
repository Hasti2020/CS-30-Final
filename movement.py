import wand as w

class Movement:

    def __init__(self, name, location, have_money, have_wand):
        self.name = name
        self.location = location
        self.money = have_money
        self.have_wand = have_wand
    
    def __str__(self):
        return f"{self.name}"
    
    def move(self):
        print("Which direction do you wanna go? (north, south, east, west)")
        direction = input("Choice: ").lower()
        # Move based on user input
        if direction == "west":
            if self.location['col'] > 0:
                self.location['col'] -= 1
                print("You moved west.")
                print(f"Now you are in {diagon_alley[self.location['row']][self.location['col']]}. ")
            else:
                print("You can't move west.")
                self.move()
        elif direction == "east":
            if self.location['col'] < 2:  # There's only 3 columns (0, 1, 2)
                self.location['col'] += 1
                print("You moved east.")
                print(f"Now you are in {diagon_alley[self.location['row']][self.location['col']]}. ")
            else:
                print("You can't move east.")
                self.move()
        elif direction == "south":
            if self.location['row'] < 2:  # There's only 3 rows (0, 1, 2)
                self.location['row'] += 1
                print("You moved south.")
                print(f"Now you are in {diagon_alley[self.location['row']][self.location['col']]}. ")
            else:
                print("You can't move south.")
                self.move()
        elif direction == "north":
            if self.location['row'] > 0:
                self.location['row'] -= 1
                print("You moved north.")
                print(f"Now you are in {diagon_alley[self.location['row']][self.location['col']]}. ")
            else:
                print("You can't move north.")
                self.move()
        else:
            print("Invalid direction! Please choose north, south, east or west.")
            self.move()
        self.explore_diagon_tile()

        if diagon_alley[self.location['row']][self.location['col']] == "Train station":
            print(f"You're in the {diagon_alley[self.location['row']][self.location['col']]}")
            print("You can choose to stay in daigon alley or you can choose to go to Hagwrats!")
            decision = input("Choice (stay/go): ")
    
    def explore_diagon_tile(self):
        current_tile = diagon_alley[self.location['row']][self.location['col']]
        
        if current_tile == "Gringotts Wizarding Bank":
            print("You can collect your money from you account.")
            print(input("Enter your name and password to access your vault: "))
            print("Vault opened!"+
                  "\nWow you have more than enough!!")
            self.money = True
            print("Now you can go shopping.")

        if current_tile == "Ollivanders wand shop":
            if self.money == False:
                print("You didn't get your money yet! Go to the bank first.")
            else:
                print("You should get your wand {player_name}!")
                print("Olivander talking...")
                w.Wand.get_wand()
                self.have_wand = True
        self.move()


    def main_menu(self):
        # Display the current location based on player coordinates
        print(f"You are currently in the {diagon_alley[self.location['row']][self.location['col']]} of Diagon Alley.")
        print("Do you want to explore? (yes/no)")
        explore = input("choice: ")
        if explore.lower() == "yes":
            self.move()
        elif explore.lower() == "no":
            print("Bye.")
        else:
            print("Invalid choice! Please choose yes or no.")
            self.main_menu()
    



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

player_name = input("Enter name: ")
player = Movement(player_name, {'row': 0, 'col': 0}, False, False)
Movement.main_menu(player)


