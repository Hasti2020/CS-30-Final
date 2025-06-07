import Explore as e
import wand as w
import potion as p
import spells as s
import house_quiz as h
import random as r

def intro_story():
    print("\n📬 You wake up to the sound of something thumping against your window.")
    print("It’s… an owl? With a letter tied to its leg? Weird, but okay.")
    input("\n(Press Enter to open the letter...)\n")
    print("\n────────────────────────────────────")
    print("📜 HOGWARTS SCHOOL OF WITCHCRAFT AND WIZARDRY")
    print("────────────────────────────────────")
    print("Dear Student,")
    print()
    print("We are pleased to inform you that you have been accepted at Hogwarts School of Witchcraft and Wizardry.")
    print("Term begins soon. You will find all necessary items on the enclosed supply list.")
    print("Your journey begins at Diagon Alley.")
    print()
    print("Sincerely,")
    print("Minerva McGonagall")
    print("Deputy Headmistress")
    print("────────────────────────────────────\n")
    print("You blink. Then blink again.")
    print("There’s another thump. This time, it’s your front door.")
    print("You open it to find a massive man with a beard so wild it could house birds.")

    print("Hagrid: 'Yeh got yer letter then? Good. I'm Hagrid. I’ll be helpin’ you get your school gear.'")
   



def run_game():
    intro_story()
    player_name = input("Hagrid: 'What’s your name, then?'\n> ")
    print(f"\nAlright then, {player_name}, you’re about to begin your magical journey. ✨")
    player = e.Movement(player_name, {'row': 0, 'col': 0})
    player.move()  # or whatever the main movement method is

run_game()