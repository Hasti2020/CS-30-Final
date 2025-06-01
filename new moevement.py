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
            print("- Hagrid: Alright, now which way do you wanna go? (north, south, east, west)")
            direction = input("Yer choice, mate: ").lower()
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
                print("Hagrid: Blimey, that's not a direction! Try again, yeah?")
            if moved:
                print(f"Hagrid: Good on ya! You moved {direction}.")
                print(f"Hagrid: You're now standin' in {diagon_alley[self.location['row']][self.location['col']]}, nice an' safe.")
                break
            else:
                print(f"Hagrid: Ya can't go {direction} from here, try another way.")
        self.explore_diagon_tile()
        self.display_diagon_map()

    
    def explore_diagon_tile(self):
        current_tile = diagon_alley[self.location['row']][self.location['col']]

        if current_tile == "Gringotts Wizarding Bank":
            if not self.have_money:
                print("Hagrid: Right, time to fetch yer galleons from yer vault!")
                print(input("Enter yer name an' password to get access, now: "))
                print("Hagrid: Vaults open! You've got plenty o' gold to spend.")
                self.have_money = True
                print("Hagrid: Now ya can go on and buy what ya need.")
            else:
                print("Hagrid: You've already taken yer money, no need t' come back here.")


        elif current_tile == "Ollivanders wand shop":
            if not self.have_wand:
                if not self.have_money:
                    print("Hagrid: Ya can't get a wand without yer money, mate! Go see Gringotts first.")
                else:
                    print(f"Hagrid: This here's the wand shop, {self.name}. Yer wand's waitin' for ya.")
                    print("Ollivander says...")  # Calling wand_intro from your wand module
                    w.Wand.get_wand()
                    w.Wand.wand_intro()
                    self.have_wand = True
            else:
                print("Hagrid: You’ve already got yerself a wand, good on ya!")

        elif current_tile == "Bookstore":
            if not self.have_book:
                if not self.have_money:
                    print("Hagrid: No books without coins, I’m afraid. Head to the bank!")
                else:
                    print(f"Hagrid: Grab yer spell books here, {self.name}, and be ready for Hogwarts!")
                    self.have_book = True
            else:
                print("Hagrid: Yer books are already in yer bag, no need to buy more.")


        elif current_tile == "Pet shop":
            if self.have_pet == False:
                if not self.have_money:
                    print("Hagrid: Ya havent got no money for a pet yet. Off to the bank!")
                else:
                    print(f"Hagrid: Pick a magical companion, {self.name};\n1-Cat \n2-Toad \n3-Owl")
                    while True:
                        pet = input("Choose yer pet, (Enter the corresponding number): ")
                        if pet == "1":
                            print("Hagrid: A fine choice, a cat. Good luck with her!")
                            break
                        elif pet == "2":
                            print("Hagrid: Toads are great for beginners, youll do fine!")
                            break
                        elif pet == "3":
                            print("Hagrid: Owls are loyal friends, good pick!")
                            break
                        else:
                            print("Hagrid: Oi! Pick 1, 2, or 3, no funny business.")
                    self.have_pet = True
            else:
                print("Hagrid: You already got a pet. Take good care of it, yeah?")


        elif current_tile == "The leaky cauldron":
            print("Hagrid: Ah, The Leaky Cauldron. Want to rest yer bones or listen for some news? (rest/news/leave)")
            choice = input("What'll it be? ").lower()
            if choice == "rest":
                print("Hagrid: Nothing beats a warm meal and butterbeer to set ya right.")
            elif choice == "news":
                print("Hagrid: Heard tell of a secret room in Hogwarts... keep yer eyes open.")
            else:
                print("Hagrid: Alright, off ya go then!")


        if current_tile == "Post Office":
            print("Hagrid: You are in the Post Office. Fancy sendin' a magical letter? (yes/no)  ")
            choice = input("Say yes or no, mate: ").lower()
            if choice == "yes":
                print("Who’s the lucky recipient? (e.g., Dumbledore, friend, etc.)")
                recipient = input("Recipient: ")
                print(f"You sent a letter to {recipient}. Owls flap away into the sky!")
            else:
                print("Hagrid: 'No worries, maybe next time.'")


        elif current_tile == "Weasleys' Wizard Wheezes (joke shop)":
            print("Hagrid: Welcome to the wildest joke shop in Diagon Alley!")
            if self.have_money:
                print("Hagrid: You can get one o' these fun items: 1-Extendable Ear, 2-Trick Wand, 3-Skiving Snackbox")
                choice = input("What would you like? (1/2/3): ")
                if choice == "1":
                    print("Hagrid: You bought an Extendable Ear! Great for sneakin' on folks.")
                elif choice == "2":
                    print("Hagrid: Careful with that wand—it sparks real good!")
                elif choice == "3":
                    print("Hagrid: That snackboxll get ya outta class, if yare clever enough.")
                else:
                    print("Hagrid: That ain’t a proper choice, try again.")
            else:
                print("George: Sorry, no galleons, no giggles! Get some money first.")

        elif current_tile == "Train station":
            print(f"Hagrid: You're at the {current_tile}.")
            print("Hagrid: You can either stay in Diagon Alley or head off to Hogwarts, yeh? What'll it be?")
            decision = input("Stay or go, mate? (stay, go) ").lower()
            if decision == "stay":
                print("Alrighty let's go explore more!") ## make it Hagrid-yy
            elif decision == "go":
                if not self.have_book:
                    print("Youre not done with your list yet! Go get your books.")
                elif not self.have_pet:
                    print("Youre not done with your list yet! Go get your pet")
                elif not self.have_wand:
                    print("Youre not done with your list yet! Go get your wand.")
                else:
                    print("Yay, go get your trian. choo choo")
                

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
        print("Hagrid: Here's where yeh are on the Diagon Alley map:\n")
        print(tabulate(display_grid, tablefmt="fancy_grid"))


    def main_menu(self):
            print(f"Hagrid: Welcome to Diagon Alley, {self.name}! Ready for a magical day?")
            self.explore_diagon_tile()

            while True:
                print(f"\nHagrid: Right now, yeh're at the {diagon_alley[self.location['row']][self.location['col']]}.")
                print("Hagrid: Want to explore a bit more? (yes/no)")
                explore = input("Say yes or no: ").lower()

                if explore == "yes":
                    self.move()
                elif explore == "no":
                    print("Hagrid: Alright then, take care out there, {0}!'. Farewell!'".format(self.name))
                    break
                else:
                    print("Hagrid: Come on now, just say yes or no.")



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

player_name = input("What's yer name, young wizard? ")
player = Movement(player_name, {'row': 0, 'col': 0}, False, False, False, False)
player.main_menu()