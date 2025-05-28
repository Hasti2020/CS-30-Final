import wand as w

class Movement:

    def __init__(self, name, location, have_money, have_wand, have_book):
        self.name = name
        self.location = location
        self.have_money = have_money
        self.have_wand = have_wand
        self.have_book = have_book
    
    def __str__(self):
        return f"{self.name}"
    
    def move(self):
        self.explore_diagon_tile()
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
            self.have_money = True
            print("Now you can go shopping.")

        if current_tile == "Ollivanders wand shop":
            if not self.have_money:
                print("You didn't get your money yet! Go to the bank first.")
            else:
                print(f"You should get your wand {self.name}!")
                print("Olivander talking...")
                w.Wand.wand_intro()
                self.have_wand = True

        if current_tile == "Bookstore":
            if not self.have_money:
                print("You didn't get your money yet! Go to the bank first.")
            else:
                print(f"You can get your books from here {self.name}.")
                self.have_book = True

        if current_tile == "Pet shop":
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



    def main_menu(self):
        print(f"Welcome to Diagon Alley, {self.name}!")

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
player = Movement(player_name, {'row': 0, 'col': 0}, False, False, False)
player.main_menu()



