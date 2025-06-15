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

import random # to assign a random wand
import time # To add the factor of time to make the convo more engaging

random_wand = None  # set it to none before the player gets their wand

# Function--------------------------------------------------------------------
class Wand:
    def __init__(self, name: str, core: str, min_power: int, max_power: int):
        self.name = name
        self.core = core
        self.max_power = max_power
        self.min_power = min_power

    def __str__(self):
        return f"{self.name}"

    #def cast_spell(self):
        #return random.randint(self.min_power, self.max_power)

    def get_wand():
        global random_wand
        if random_wand == None:
            random_wand = random.choice(wand_options)
        return random_wand

    def wand_intro():
        print(f"The wand has spoken... You have been chosen by {random_wand}!")
        time.sleep(1)
        print("...........")
        time.sleep(2)
        print(f"Your wand has a {random_wand.core};  and casts spells with power between {random_wand.min_power} and {random_wand.max_power}.")
        
        
wand_options = [Wand("Duststick", "Rabbit Fur", 0, 10),
                Wand("Ashlight", "Unicorn Hair", 5, 15),
                Wand("Dragonshade", "Dragon Heartstring", 10, 20),
                Wand("Phoenixbane", "Phoenix Feather", 15, 25),
                Wand("Elder Echo", "Basilisk Horn", 20, 30)]


# Main------------------------------------------------------------------------
#Usage exmpale:
#Wand.get_wand()


