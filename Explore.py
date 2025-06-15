###############################################################################
# Title: Wnad Module
# Name/s: Hasti, Emily
# Class: CS 30
# Assignment: Capstone project
##############################################################################
'''
This module defines a Wand class and provides functionality to randomly assign a wand 
to a user, simulating a magical wand selection process similar to fantasy worlds.
'''
##############################################################################
# Imports and Global Variables------------------------------------------------
import wand as w
from tabulate import tabulate
import random as r
import potion as p
import spells as s
import house_quiz as h
import battle as b


class Movement:

    def __init__(self, player):
        self.player = player
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

    def __str__(self):
        return f"{self.player.name}"

    def move(self):
        while True:
            print("- Hagrid: Alright, now which way do you wanna go? (north, south, east, west)")
            direction = input("Yer choice, mate: ").lower()
            moved = False
            old_location = self.player.location.copy()

            if direction == "west":
                if self.player.location['col'] > 0:
                    self.player.location['col'] -= 1
                    moved = True
            elif direction == "east":
                if self.player.location['col'] < len(self.current_map[0]) - 1:
                    self.player.location['col'] += 1
                    moved = True
            elif direction == "south":
                if self.player.location['row'] < len(self.current_map) - 1:
                    self.player.location['row'] += 1
                    moved = True
            elif direction == "north":
                if self.player.location['row'] > 0:
                    self.player.location['row'] -= 1
                    moved = True
            else:
                print("Hagrid: Blimey, that's not a direction! Try again, yeah?")

            if moved:
                print(f"Hagrid: Good on ya! You moved {direction}.")
            else:
                print(f"Hagrid: Ya can't go {direction} from here, try another way.")

            if self.player.at_hogwarts:
                self.explore_hogwarts_tile()
            else:
                self.explore_diagon_tile()
            self.display_map()

    def explore_diagon_tile(self):
        current_tile = self.diagon_alley_map[self.player.location['row']][self.player.location['col']]

        if current_tile == "Gringotts Wizarding Bank":
            if not self.player.have_money:
                print("Hagrid: Right, time to fetch yer galleons from yer vault!")
                print(input("Enter yer name an' password to get access, now: "))
                print("Hagrid: Vaults open! You've got plenty o' gold to spend.")
                self.player.have_money = True
                print("Hagrid: Now ya can go on and buy what ya need.")
            else:
                print("Hagrid: You've already taken yer money, no need t' come back here.")

        elif current_tile == "Ollivanders wand shop":
            if not self.player.have_wand:
                if not self.player.have_money:
                    print("Hagrid: Ya can't get a wand without yer money, mate! Go see Gringotts first.")
                else:
                    print(f"Hagrid: This here's the wand shop, {self.player.name}. Yer wand's waitin' for ya.")
                    print("Ollivander says...")
                    w.Wand.get_wand()
                    w.Wand.wand_intro()
                    self.player.have_wand = True
            else:
                print("Hagrid: You’ve already got yerself a wand, good on ya!")

        elif current_tile == "Bookstore":
            if not self.player.have_book:
                if not self.player.have_money:
                    print("Hagrid: No books without coins, I’m afraid. Head to the bank!")
                else:
                    print(f"Hagrid: Grab yer spell books here, {self.player.name}, and be ready for Hogwarts!")
                    self.player.have_book = True
            else:
                print("Hagrid: Yer books are already in yer bag, no need to buy more.")

        elif current_tile == "Pet shop":
            if not self.player.have_pet:
                if not self.player.have_money:
                    print("Hagrid: Ya havent got no money for a pet yet. Off to the bank!")
                else:
                    print(f"Hagrid: Pick a magical companion, {self.player.name};\n1-Cat \n2-Toad \n3-Owl")
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
                    self.player.have_pet = True
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
                recipient = input("Recipient: ")
                print(f"You sent a letter to {recipient}. Owls flap away into the sky!")
            else:
                print("Hagrid: 'No worries, maybe next time.'")

        elif current_tile == "Weasleys' Wizard Wheezes (joke shop)":
            print("Hagrid: Welcome to the wildest joke shop in Diagon Alley!")
            if self.player.have_money:
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
                print("Alrighty let's go explore more!")
            elif decision == "go":
                if not self.player.have_book:
                    print("Youre not done with your list yet! Go get your books.")
                elif not self.player.have_pet:
                    print("Youre not done with your list yet! Go get your pet")
                elif not self.player.have_wand:
                    print("Youre not done with your list yet! Go get your wand.")
                else:
                    print("Hagrid: Brilliant! Let’s get yeh to Hogwarts. Choo choo!")
                    self.current_map = self.hogwarts_map
                    self.player.location = {'row': 0, 'col': 0}
                    self.player.at_hogwarts = True
                    self.explore_hogwarts_tile()

    def explore_hogwarts_tile(self):
        current_tile = self.hogwarts_map[self.player.location['row']][self.player.location['col']]

        if current_tile == "Dining Hall":
            if not self.player.sorted:
                print("Hagrid: Ahh, the Great Hall! Time for yeh to be sorted into yer house.")
                self.player.sorted = True
                h.house_sort()
            else:
                print("Hagrid: Welcome to the Dining Hall. Fancy a feast or just sittin' with the students? (feast/sit/leave)")
                choice = input("Yer pick: ").lower()
                if choice == "feast":
                    print("Hagrid: You had a grand feast! Yer energy’s full. You’ll feel stronger in battles now.")
                    self.player.energy_boost = True
                elif choice == "sit":
                    print("Hagrid: You sat with a group of friendly witches and wizards. Nice way to make friends!")
                else:
                    print("Hagrid: Alright then, movin on.")

        elif current_tile == "Library":
            print("Hagrid: Shhh... It's the library. Want to read a magical book? (yes/no)")
            if input("Your choice: ").lower() == "yes":
                print("Hagrid: You found a dusty book on magical creatures. You've learned a new spell: *Stupefy!*")
                s.Spell.spell_list.append('Stupefy')
            else:
                print("Hagrid: Fair enough, not everyone’s a bookworm.")

        elif current_tile == "Dorms":
            print("Hagrid: Yer dorm’s cozy and warm. Wanna take a nap or decorate yer space? (nap/decorate/leave)")
            action = input("What'll it be? ").lower()
            if action == "nap":
                print("Hagrid: You took a quick nap. Energy restored!")
                self.player.energy_boost = True
            elif action == "decorate":
                print("Hagrid: You added fairy lights and posters! Yer dorm feels more like home.")
            else:
                print("Hagrid: Alright, outta here then.")

        elif current_tile == "Potion Class":
            # Checks if the player has entered potion class yet
            if not self.player.enter_potion_class:
                print("You're in Potions class. Professor Snape eyes you.")
                # Pass the player into the potion game
                mini_game = p.PotionGame(self.player)
                # Stores the object in the potion game to the player to access later
                self.player.potion_game = mini_game
                # Starts the potion mini game
                mini_game.start_potion_game()
                self.player.enter_potion_class = True
            else:
                print("Hagrid: Yeh just walked passed professor Snape's class!")

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
            # Checks if the player has gone to the spell lesson yet
            if not self.player.enter_spell_class:
                # Allow player to go into the lesson
                s.spell_lesson()
                self.player.enter_spell_class = True
            else: # Prevents player from coming into spell lesson again
                print("Hagrid: Yeh just walked pass professor Flitwick's spells class!")

        elif current_tile == "Room of Requirement":
            print("Hagrid: You have entered the Room of Requirement! What do you wish for?")
            print("Options: 'knowledge' or 'secret?'")
            wish = input("Your wish: ").lower()
            if wish == "knowledge":
                print("Hagrid: A rare spellbook appears. You learned *Expelliarmus!*")
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
                # Have the player be passed into the battle
                tournament = b.Battle(self.player)
                # Starts the battle/tournament
                tournament.start_battle()
            else:
                print("\nMcGonagall: 'A wise decision. There’s no shame in preparation. Come back when you’re truly ready.'")
                print("She vanishes into the shadows like a dramatic Scottish ninja.")

    def display_map(self):
        display_grid = []
        for i, row in enumerate(self.current_map):
            display_row = []
            for j, tile in enumerate(row):
                if self.player.location['row'] == i and self.player.location['col'] == j:
                    display_row.append(f"{tile} \U0001f600")
                else:
                    display_row.append(tile)
            display_grid.append(display_row)

        if self.current_map == self.diagon_alley_map:
            print("Hagrid: Here's where yeh are on the Diagon Alley map:\n")
        elif self.current_map == self.hogwarts_map:
            print("Hagrid: Here's where yeh are in Hogwarts:\n")
        else:
            print("You're somewhere mysterious...\n")

        print(tabulate(display_grid, tablefmt="fancy_grid"))

    def main_menu(self):
        print(f"Hagrid: Welcome to Diagon Alley, {self.player.name}! Ready for a magical day?")
        self.explore_diagon_tile()

        while True:
            print(f"\nHagrid: Right now, yeh're at the {self.current_map[self.player.location['row']][self.player.location['col']]}")
            print("Hagrid: Want to explore a bit more? (yes/no)")
            explore = input("Say yes or no: ").lower()

            if explore == "yes":
                self.move()
            elif explore == "no":
                print("Hagrid: Alright then, take care out there, {0}!'. Farewell!'".format(self.player.name))
                break
            else:
                print("Hagrid: Come on now, just say yes or no.")


'''
player_name = input("What's yer name, young wizard? ")
player = Movement(player_name, {'row': 0, 'col': 0})
player.main_menu()
'''