###############################################################################
'''
This module is in charge of the part in the game where the player battles 
enemies using spells, potions, and wands. It handles character health, damage, 
timers, and score updates. Classes include Player and Opponent, with support 
from external modules like spells, potions, and wand.
'''
###############################################################################
# Imports and Global Variables-------------------------------------------------
import random
import wand as w
import spells as s
import potion as p
import score 
import threading
import time


class Character:
    '''Represents a character in the game.'''


    def __init__(self, name):
        ''' Initializes character '''
        self.name = name
        self.health = 100 # Sets both player and opponent's health to 100
        self.alive = True # Sets noth as alive 
   

    def __str__(self):
        return f"{self.name}"
   

    def take_damage(self, damage):
        # Takes the amount of damage each taken and subtract it by the health
        self.health -= damage
        if self.health <= 0:
            self.alive = False # Sets player/opponent to dead
            self.health = 0 # Have health not go to a negative number
        else:
            print('--------------------------------')
            # Prints health of the player/opponent
            print(f"[{self.name}] current health : {self.health}")


class Player(Character):
    """Represents player in the game."""
   

    def __init__(self, name): 
        ''' Initializes player '''
        Character.__init__(self, name) # Takes attributes from character
        self.wand_type = w.Wand.get_wand() # Stores the wand given
        self.players_score = 0 
        self.maxima_increase = False # Have increase attacks not be activated
        self.thunderbrew_increase = False
        self.inventory = [] 
        # Lets player have access to the potion game
        self.potion_game = p.PotionGame(self) 
        self.have_money = False
        self.have_wand = False
        self.have_book = False
        self.have_pet = False
        self.at_hogwarts = False
        self.sorted = False
        self.location = {'row': 0, 'col': 0} # Set player's coordinates to 0,0
        self.enter_potion_class = False
        self.enter_spell_class = False
             
           
    def healing(self):
        ''' Heals player '''
        self.health += 20 
        print('drinking...')
        time.sleep(1)
        print('+ 5 health!')
        print('drinking...')
        time.sleep(1)
        print('+ 5 health!')
        time.sleep(0.5)
        print("You have gain 20 HP!")


    def start_countdown(self, length):
        '''
        In order for timer to not freeze the whole game, threading needs
        to be used to run the method sperately in the background in my
        game. Or else the game will wait for the timer to go out before
        the game continues on.
        '''
        thread = threading.Thread(target=self.countdown, args=(length,),
                                  daemon=True)
        # chooses my countdown method to be played in the background, 
        # and takes in my coutdown argument of 15s, letting my timer
        # to be played in the background without freezing the game
        # daemon will stop the threading once the game ends
        thread.start()


    def countdown(self, t):
        '''
        This is the method for the Maxima Potion's timer to
        be displayed on the console.
        '''
        while t: # while my time is counting down
            mins, secs = divmod(t, 60) 
            # takes the time and try doing the quotient division with 60
            # 15 fits in 60 0 times, so there is 0 minutes, and 15s is left
            timer = '{:02d}:{:02d}'.format(mins, secs)
            # if the number is only 1 digit, add a 0 in front to make it 2 
            # and formats the timer into 00:15, with just whole numbers
            print(f"\r[Maxima Boost Time left: {timer}]  ", end=" ",
                   flush=True)
            # prints the timer format,and keep printing at the same spot
            # and also immediately display it on the screen 
            time.sleep(1)
            t -= 1 # time argument keeps counting down
        self.maxima_increase = False # deactivate increase attack
        print("Time's up!")


    def inflict_damage(self, enemy):
        '''
        This is a method for inflicting damage on the enemy of 
        the player
        '''
        global spell_input
        print()
        print("\nYou are casting a spell... 🪄✨")
        # Have attack be from the wand's power range
        attack = random.randint(self.wand_type.min_power, 
                                self.wand_type.max_power)
        if self.maxima_increase: # checks if the player uses Maxima Potion
            attack += 5 # Add exta 5 attack damage
        # Checks if the player uses Thunderbrew Potion
        if self.thunderbrew_increase:
            attack += 20 # Add exta 20 attack damage
            print("⚡⚡ BAMMMM THUNDERSTRIKE ⚡⚡")
            self.thunderbrew_increase = False
        # Checks if the player health is less than 40, they cast a spell
        if self.health <= 40: 
            print('\nBlimey, cast any one of the spell yeh remember to '
                  + 'cause more damage!')
            i = 1
            # Prints out the spell list from Spell class in spell module
            for item in s.Spell.spell_list:
                print(f"{i}. {item}")
                i += 1
            try:
                print("Spell Name: ")
                # Have input correspond the Python position rule
                spell_input = int(input("> ")) - 1 
                # Checks if the input is within list's range
                if 0 <= spell_input < len(s.Spell.spell_list):
                    spell_name = s.Spell.spell_list[spell_input]
                    spell = s.Spell(spell_name)
                    spell.cast_spell()
                else: # checks if the input is invalid
                    print("That was not a spell!")
                    # Creates 0 damage
                    spell_attack = 0
                # Have attack equal the chosen spell's power
                spell_attack = spell.attack
                # Add the spell damage to the wand damage
                total_attack = attack + spell_attack
                print(f"{enemy.name} has taken a total of {total_attack}"
                      + " damage")
                # Have the enemy take on the attacks
                enemy.take_damage(total_attack)
                return total_attack
            except ValueError: # Checks if the player's input is not an integer
                print("\nYou have casted an unknown spell which contributes"
                      + " 0 damage")
                spell_attack = 0 
                total_attack = attack + spell_attack
                print(f"{enemy.name} has taken a total of {total_attack}"
                      + " damage")
                enemy.take_damage(total_attack)
                return total_attack
        else: # Gives regular attacks
            print(f"{enemy.name} has taken {attack} damage!")
            enemy.take_damage(attack)
            return attack


    def compare_scores(self):
        '''
        This method will compare the player's score after the battle to
        their highest score
        '''
        if self.players_score > int(score.high_score):
            # Have the new high score overwrite the old one
            score.newScore(str(self.players_score))


class Oponent(Character):
    """Represents opponent in the game."""
   

    def __init__(self, name):
        '''
        Initializes opponent by taking attributes from
        the Character class
        '''
        Character.__init__(self, name)
     

    def inflict_damage(self, user):
        '''
        This is a method for inflicting damage on the player of 
        the enemy
        '''
        print()
        print(f"\n{self.name} is casting a spell... 😈🪄")
        # checks if the opponent is the following characters
        if self.name == 'Luna':
            # Randomizes the attacks
            attack = random.randint(5, 10)
        if self.name == 'Draco':
            attack = random.randint(10, 15)
        if self.name == 'Peter':
            attack = random.randint(15, 20)
        if self.name == 'Bellatrix':
            attack = random.randint(20, 25)
        if self.name == 'Voldemort':
            attack = random.randint(25, 30)
        print(f"You have taken {attack} damage!")
        # Have the player take on the attack
        user.take_damage(attack)
        return attack
               

















