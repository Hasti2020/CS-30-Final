import wand as w
from tabulate import tabulate
import random as r
import potion as p
import spells as s
import house_quiz as h
import battle as b


class Movement:

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.have_money = False
        self.have_wand = False
        self.have_book = False
        self.have_pet = False
        self.at_hogwarts = False
        self.sorted = False

        self.diagon_alley_map = [
            ["Entrance", "Gringotts Wizarding Bank", "Ollivanders wand shop"],
            ["Bookstore", "Pet shop", "The leaky cauldron"],
            ["Weasleys' Wizard Wheezes (joke shop)", "Post Office", "Train station"]
        ]
        self.hogwarts_map = [
            ["Dining Hall", "Library", "Dorms"],
            ["Potion Class", "Hagrid's Cabin", "Secret path"],
            ["Spell Class", "Room of Requirement", "Front doors"]
        ]
        self.current_map = self.diagon_alley_map
        self.location = {'row': 0, 'col': 0}
    
    def __str__(self):
        return f"{self.name}"
    
    def move(self):
        while True:
            print("- Hagrid: Alright, now which way do you wanna go? (north, south, east, west)")
            direction = input("Yer choice, mate: ").lower()
            moved = False
            old_location = self.location.copy()

            if direction == "west":
                if self.location['col'] > 0:
                    self.location['col'] -= 1
                    moved = True
            elif direction == "east":
                if self.location['col'] < len(self.current_map[0]) - 1:
                    self.location['col'] += 1
                    moved = True
            elif direction == "south":
                if self.location['row'] < len(self.current_map) - 1:
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
            else:
                print(f"Hagrid: Ya can't go {direction} from here, try another way.")

            # Now always explore and display the current tile
            if self.at_hogwarts:
                self.explore_hogwarts_tile()
            else:
                self.explore_diagon_tile()
            self.display_map()

            #if moved:
                #break  # Only break after all logic is processed

    
    def explore_diagon_tile(self):
        current_tile = self.diagon_alley_map[self.location['row']][self.location['col']]

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
            if not self.have_pet:
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


        elif current_tile == "Post Office":
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
                    print("Hagrid: Brilliant! Let’s get yeh to Hogwarts. Choo choo!")
                    self.current_map = self.hogwarts_map
                    self.location = {'row': 0, 'col': 0}
                    self.at_hogwarts = True
                    self.explore_hogwarts_tile()
                
                
    def explore_hogwarts_tile(self):
        current_tile = self.hogwarts_map[self.location['row']][self.location['col']]

        if current_tile == "Dining Hall":
            if not self.sorted:
                    print("Hagrid: Ahh, the Great Hall! Time for yeh to be sorted into yer house.")
                    self.sorted = True
                    h.house_sort()
            else:
                print("Hagrid: Welcome to the Dining Hall. Fancy a feast or just sittin' with the students? (feast/sit/leave)")
                choice = input("Yer pick: ").lower()
                if choice == "feast":
                    print("Hagrid: You had a grand feast! Yer energy’s full. You’ll feel stronger in battles now.")
                    self.energy_boost = True  # You can use this in future battle logic
                elif choice == "sit":
                    print("Hagrid: You sat with a group of friendly witches and wizards. Nice way to make friends!")
                else:
                    print("Hagrid: Alright then, movin on.")

        elif current_tile == "Library":
            print("Hagrid: Shhh... It's the library. Want to read a magical book? (yes/no)")
            if input("Your choice: ").lower() == "yes":
                print("Hagrid: You found a dusty book on magical creatures. You've learned a new spell: *Stupefy!*")
                # Tell Emily to add this to the list of spells
            else:
                print("Hagrid: Fair enough, not everyone’s a bookworm.")


        elif current_tile == "Dorms":
            print("Hagrid: Yer dorm’s cozy and warm. Wanna take a nap or decorate yer space? (nap/decorate/leave)")
            action = input("What'll it be? ").lower()
            if action == "nap":
                print("Hagrid: You took a quick nap. Energy restored!")
                self.energy_boost = True
            elif action == "decorate":
                print("Hagrid: You added fairy lights and posters! Yer dorm feels more like home.")
            else:
                print("Hagrid: Alright, outta here then.")


        elif current_tile == "Potion Class":
            print("You're in Potions class. Professor Snape eyes you.")
            my_potions = p.start_potion_game()

        elif current_tile == "Hagrid's Cabin":
            print("Hagrid: Hey! You found my cabin. Want to help me feed a baby dragon? (yes/no)")
            if input("Yes or no? ").lower() == "yes":
                print("Hagrid: Thanks, mate! The dragon really likes ya.")
            else:
                print("Hagrid: No worries. That lil’ rascal bites anyway.")


        elif current_tile == "Secret path":
            print("Hagrid: Oi, you’ve stumbled on a secret path. Want to sneak through it? Could be risky. (sneak/leave)")
            choice = input("What's yer move? ").lower()
            if choice == "sneak":
                luck = r.randint(1, 2)
                if luck == 1:
                    print("Hagrid: Whoa! You found a hidden chest and gained 10 Galleons!")
                else:
                    print("Hagrid: Uh-oh! A trick stair. You lost some time and had to crawl out.")
            else:
                print("Hagrid: Smart one, not all paths are worth the risk.")

        elif current_tile == "Spell Class":
            s.spell_lesson()

        elif current_tile == "Room of Requirement":
            print("Hagrid: You have entered the Room of Requirement! What do you wish for?")
            print("Options: 'knowledge' or 'secret?/'")
            wish = input("Your wish: ").lower()
            if wish == "knowledge":
                print("Hagrid: A rare spellbook appears. You learned *Expelliarmus!*")
                # Add this to the spells list
            elif wish == "secret":
                print("Hagrid: The room whispers... 'There's a traitor at Hogwarts.'")
            else:
                print("Hagrid: The room didn’t understand ya. Try again next time.")

        elif current_tile == "Front doors":
            print("\nProfessor McGonagall: 'Well? Have you come to throw your name into the Diwizard Tournament?'")
            choice = input("Do you want to enter the tournament? (yes/no): ").strip().lower()
            if choice == "yes":
                print("\nMcGonagall: 'Very well. I hope you’ve been studying, practicing, and not just petting hippogriffs.'")
                print("She pulls out a long scroll and scribbles your name down.")
                print("McGonagall: 'The first battle will be start soon. Prepare yourself — there’s no turning back now.'")
                b.Battle(self.name, my_potions).start_battle()
            else:
                print("\nMcGonagall: 'A wise decision. There’s no shame in preparation. Come back when you’re truly ready.'")
                print("She vanishes into the shadows like a dramatic Scottish ninja.")

    def display_map(self):
        display_grid = []
        # Use the current map (e.g., self.current_map)
        for i, row in enumerate(self.current_map):
            display_row = []
            for j, tile in enumerate(row):
                if self.location['row'] == i and self.location['col'] == j:
                    # Highlight current location with emoji
                    display_row.append(f"{tile} \U0001f600")
                else:
                    display_row.append(tile)
            display_grid.append(display_row)

        # Dynamic title based on map name
        if self.current_map == self.diagon_alley_map:
            print("Hagrid: Here's where yeh are on the Diagon Alley map:\n")
        elif self.current_map == self.hogwarts_map:
            print("Hagrid: Here's where yeh are in Hogwarts:\n")
        else:
            print("You're somewhere mysterious...\n")

        # Print the map
        print(tabulate(display_grid, tablefmt="fancy_grid"))



    def main_menu(self):
            print(f"Hagrid: Welcome to Diagon Alley, {self.name}! Ready for a magical day?")
            self.explore_diagon_tile()

            while True:
                print(f"\nHagrid: Right now, yeh're at the {self.current_map[self.location['row']][self.location['col']]}.")
                print("Hagrid: Want to explore a bit more? (yes/no)")
                explore = input("Say yes or no: ").lower()

                if explore == "yes":
                    self.move()
                elif explore == "no":
                    print("Hagrid: Alright then, take care out there, {0}!'. Farewell!'".format(self.name))
                    # Do something better instead of sudden end!
                    break
                else:
                    print("Hagrid: Come on now, just say yes or no.")


'''
player_name = input("What's yer name, young wizard? ")
player = Movement(player_name, {'row': 0, 'col': 0})
player.main_menu()
'''