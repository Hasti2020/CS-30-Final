
###############################################################################
'''
This module handles the spell part of the game. It includes all the famous 
Harry Potter spells, figures out how strong each one is, and prints out 
messages when spells are cast. While also includes a fun little spell lesson
with Flitwick to have the players know which spells to casts during the
battle. time.sleep() is to show the texts slowly to the console
'''
###############################################################################
# Imports and Global Variables-------------------------------------------------
import time


class Spell:
    '''
    This class will handle the power ranges of the spells and returns its
    damage to the player's attacks in the character module.
    '''

    # List of all the spells
    spell_list = [
        'Sectumsempra',
        'Lumos',
        'Avada Kedavra',
        'Disillusionment',
        'Cruciatus' 
        ]
    

    def __init__(self, name):
        '''Initializes the spells'''
        self.name = name # Initializes the spell name
        self.attack = self.spell_power()


    def __str__(self):
        return f"{self.name}" 
    

    def spell_power(self):
        '''
        This method will return the damage of the coresponding spells
        to the attack object of the class
        '''
        if self.name == 'Sectumsempra':
            return 20
        if self.name == 'Lumos':
            return 1
        if self.name == 'Avada Kedavra':
            return 25
        if self.name == 'Disillusionment':
            return 5
        if self.name == 'Cruciatus':
            return 10
        if self.name == 'Expelliarmus':
            return 15
        if self.name == 'Stupefy':
            return 10

        
    def cast_spell(self):
        '''This method will chack and handle the spell casting process'''
        # Makes sure the spell in within the list
        if self.name in Spell.spell_list: 
            # Prints out the spell name and also its damage
            print(f"\nYou have casted {self.name}, which contributes"
                  + f" {self.attack} damage")


def spell_lesson():
    '''
    This function will print out all the dialogs of the spell lesson
    with professor Flitwick'''
    print("--------You have entered professor Flitwick's spells lessons"
          + "--------")
    time.sleep(1) 
    print("Flitwick: Hello students, today we will be learning about the"
          + " most famous spells in the wizzarding world! ✨✨" )
    time.sleep(1)
    print("\nFlitwick: Need a bit of light? Lumos ✨! A flick of the "
          + " wand, and a glowing tip to guide your way in the dark!")
    print("Flitwick: It can only create 1 DMG in a battle though...")
    time.sleep(2)
    print("\nFlitwick: Become nearly invisible! Disillusionment Charm ✨!"
          + " Excellent for sneaking — just don’t trip over your own feet!")
    print("Flitwick: It can only create 5 DMG tho...")
    time.sleep(2)
    print("\nFlitwick: Dark magic... Sectumsempra ✨ causes deep wounds, "
          + ". Use it only if you must.")
    print("Flitwick: This dangerous spell can cause a massive 20 DMG...")
    time.sleep(2)
    print("\nFlitwick: The Cruciatus. It causes unbearable pain. Unforgivable."
          + " Illegal. This is not a spell to take lightly.")
    print("Flitwick: This spell can cause 10 DMG...")
    time.sleep(2)
    print("\nFlitwick: The Killing Curse. Avada Kedavra. This spell is pure "
          + "evil — never to be used!")
    print("Flitwick: This spell can cause 25 DMG...")
    time.sleep(2)
    print("\nYou: Ugh, this is too boring, I will sneak out now!")
    time.sleep(2)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)






