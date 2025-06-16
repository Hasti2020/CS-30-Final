###############################################################################
# Tittle: Harry Potter: DiWizzard Tournament
# Name: Hasti and Emily
# Class: CS 30
# Assignment: CS 30 Final Project
# Version: 4.4
# Date: June 16th 2025
###############################################################################
'''
This is the main menu of our game, a game where the player will be emerged 
into the Wizarding world of Harry Potter. First they will recieve the letter
from Hogwarts. Then they will arrive to the Diagon Alley, where they will get
to collect all their school supplies, like books, wands, pets to get into the
school. When they actually get into Hogwarts, they will get to do a House Quiz
and be sorted into their house they score the most points on the quiz. In 
Hogwarts, the player would get to walk around, join different classes like
the potion and spell class, where they get to make/learn useful information
that will help them in their battle later on. Lastly, the ending is where the
player gets to enter the DiWizzard Tournament, where they will fight 3 
different randomized opponents, and if they survive, they would get to fight
with Lord Voldemort. And if they win that battle, they will be crowned the
hero of the wizaarding world!
'''
###############################################################################
# Imports and Global Variables-------------------------------------------------
import Explore as e
import character as c

def intro_story():
    '''This function will print out the dialogs at the start of the game'''
    print("\n📬 You wake up to the sound of something thumping against your"
          + " window.")
    print("It’s… an owl? With a letter tied to its leg? Weird, but okay.")
    input("\n(Press Enter to open the letter...)\n")
    print("\n────────────────────────────────────")
    print("📜 HOGWARTS SCHOOL OF WITCHCRAFT AND WIZARDRY")
    print("────────────────────────────────────")
    print("Dear Student,")
    print()
    print("We are pleased to inform you that you have been accepted at "
          + "Hogwarts School of Witchcraft and Wizardry.")
    print("Term begins soon. You will find all necessary items on the "
          + "enclosed supply list.")
    print("Your journey begins at Diagon Alley.")
    print()
    print("Sincerely,")
    print("Minerva McGonagall")
    print("Deputy Headmistress")
    print("────────────────────────────────────\n")
    print("You blink. Then blink again.")
    print("There’s another thump. This time, it’s your front door.")
    print("You open it to find a massive man with a beard so wild it could "
          + "house birds.")

    print("Hagrid: 'Yeh got yer letter then? Good. I'm Hagrid. I’ll be "
          + "helpin’ you get your school gear.'")
   

def run_game():
    '''This function will run our code from the other modules'''
    intro_story() # Calls the intro function above
    # Lets the player input their name
    player_name = input("Hagrid: 'What’s your name, then?'\n> ")
    print(f"\nAlright then, {player_name}, you’re about to begin your magical"
          + " journey. ✨")
    player_character = c.Player(player_name) # Instance of the player
    # Movement now just takes the player
    movement = e.Movement(player_character)
    movement.main_menu() # Start the main menu


run_game() # Runs the function above


