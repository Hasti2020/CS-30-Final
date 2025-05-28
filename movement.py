import wand as w
from tabulate import tabulate

class Movement:

    def __init__(self, name, location, have_money, have_wand, have_book, have_pet):
        self.name = name
        self.location = location
        self.have_money = have_money
        self.have_wand = have_wand
        self.have_book = have_book
        self.have_pet = have_pet
    
    def __str__(self):
        return f"{self.name}"
    
    def move(self):
        #self.explore_diagon_tile()
        while True:
            print("Which direction do you wanna go? (north, south, east, west)")
            direction = input("Choice: ").lower()
            moved = False
            if direction == "west":
                if self.location['col'] > 0:
                    self.location['col'] -= 1
                    moved = True
            elif direction == "east":
                if self.location['col'] < 2:
                    self.location['col'] += 1
                    moved = True
            elif direction == "south":
                if self.location['row'] < 2:
                    self.location['row'] += 1
                    moved = True
            elif direction == "north":
                if self.location['row'] > 0:
                    self.location['row'] -= 1
                    moved = True
            else:
                print("Invalid direction!")
            if moved:
                print(f"You moved {direction}.")
                print(f"Now you are in {diagon_alley[self.location['row']][self.location['col']]}.")
                break
            else:
                print(f"You can't move {direction}. Try a different direction.")
        self.explore_diagon_tile()
        self.display_diagon_map()


        if diagon_alley[self.location['row']][self.location['col']] == "Train station":
            print(f"You're in the {diagon_alley[self.location['row']][self.location['col']]}")
            print("You can choose to stay in daigon alley or you can choose to go to Hagwrats!")
            decision = input("Choice (stay/go): ")
            # Add logic
    

    def explore_diagon_tile(self):
        current_tile = diagon_alley[self.location['row']][self.location['col']]

        if current_tile == "Gringotts Wizarding Bank":
            if self.have_money == False:
                print("You can collect your money from you account.")
                print(input("Enter your name and password to access your vault: "))
                print("Vault opened!"+
                    "\nWow you have more than enough!!")
                self.have_money = True
                print("Now you can go shopping.")
            else:
                print("You already took your money!")


        if current_tile == "Ollivanders wand shop":
            if self.have_wand == False:
                if not self.have_money:
                    print("You didn't get your money yet! Go to the bank first.")
                elif self.have_wand == True:
                    print("You already got your wand.")
                else:
                    print(f"You should get your wand {self.name}!")
                    print("Olivander talking...")
                    w.Wand.wand_intro()
                    self.have_wand = True
            else:
                print("You already have a wand!")


        if current_tile == "Bookstore":
            if self.have_book ==  False:
                if not self.have_money:
                    print("You didn't get your money yet! Go to the bank first.")
                else:
                    print(f"You can get your books from here {self.name}.")
                    self.have_book = True
            else:
                print("You already have got your books!")


        if current_tile == "Pet shop":
            if self.have_pet == False:
                if not self.have_money:
                    print("You didn't get your money yet! Go to the bank first.")
                else:
                    print(f"You can pick a pet {self.name}:\n1-Cat \n2-Toad \n3-Owl")
                    while True:
                        pet = input("What do you wanna get? (Enter the corresponding number): ")
                        if pet == "1":
                            print("You got a cat.")
                            break
                        elif pet == "2":
                            print("You got a toad.")
                            break
                        elif pet == "3":
                            print("You got an owl.")
                            break
                        else:
                            print("Invalid input! Please enter 1, 2, or 3.")
                    self.have_pet = True
            else:
                print("You already got a pet!")


        if current_tile == "The leaky Cauldren":
            print("You’re in the cozy Leaky Cauldron. Do you want to rest or listen for news? (rest/news/leave)")
            choice = input("Choice: ").lower()
            if choice == "rest":
                print("You enjoy a warm meal and butterbeer. You feel refreshed!")
            elif choice == "news":
                print("You overhear someone talking about a secret room in Hogwarts...")
            else:
                print("You leave the Leaky Cauldron.")


        if current_tile == "Post Office":
            print("You are in the Post Office. Do you want to send a magical letter? (yes/no)")
            choice = input("Choice: ").lower()
            if choice == "yes":
                print("Who do you want to write to? (e.g., Dumbledore, friend, etc.)")
                recipient = input("Recipient: ")
                print(f"You sent a letter to {recipient}. Owls flap away into the sky!")
            else:
                print("You decide not to send a letter.")


        if current_tile == "Weasleys' Wizard Wheezes (joke shop)":
            print("You’ve entered the wildest shop in Diagon Alley!")
            if self.have_money:
                print("You can buy a fun item:\n1-Extendable Ear\n2-Trick Wand\n3-Skiving Snackbox")
                choice = input("What would you like? (1/2/3): ")
                if choice == "1":
                    print("You bought an Extendable Ear! You might overhear secrets later.")
                elif choice == "2":
                    print("The wand explodes in sparks! Everyone laughs. Classic.")
                elif choice == "3":
                    print("You feel a bit sick... now you can skip class if needed!")
                else:
                    print("That’s not an option.")
            else:
                print("Fred: Sorry, no galleons, no giggles! Get some money first.")


    def display_diagon_map(self):
        display_grid = []
        for i, row in enumerate(diagon_alley):
            display_row = []
            for j, tile in enumerate(row):
                if self.location['row'] == i and self.location['col'] == j:
                    # Highlight current location
                    display_row.append(f"{tile}\U0001f600")
                else:
                    display_row.append(tile)
            display_grid.append(display_row)

        print("\nYour current position on the Diagon Alley map:\n")
        print(tabulate(display_grid, tablefmt="fancy_grid"))


    def main_menu(self):
            print(f"Welcome to Diagon Alley, {self.name}!")
            self.explore_diagon_tile()

            while True:
                print(f"\nYou are currently in the {diagon_alley[self.location['row']][self.location['col']]}.")
                print("Do you want to explore? (yes/no)")
                explore = input("Choice: ").lower()

                if explore == "yes":
                    self.move()
                elif explore == "no":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice! Please choose yes or no.")


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
player = Movement(player_name, {'row': 0, 'col': 0}, False, False, False, False)
player.main_menu()



