###############################################################################
'''
This module manages the battle system where the player fights enemies 
using spells, potions, and wands. It handles battle flow, player and opponent 
health and damage, score updates, and user interactions during battles.
The Battle class showcases encounters with opponents, with random battles 
and the final boss fight with Voldemort. It also uses external modules 
for character stats, spells, potions, wands, and scoring.
'''
###############################################################################
# Imports and Global Variables-------------------------------------------------
import character
import random
import wand as w
import score as s
import time


class Battle:
    """ Controls the battle sequences between the player and opponents """


    def __init__(self, player):
        '''Initializes the battle with the player and opponets'''
        self.oponent_list = ['Draco', 'Luna', 'Peter', 'Bellatrix']
        w.Wand.get_wand()
        s.getScore()
        self.player = player


    def battle_stat(self):
        '''
        This method is to print out the player's performance after 
        they finish a battle
        '''
        print('\n---------------STATS---------------')
        print(f"Score: {self.player.players_score}")
        print(f"Health: {self.player.health}")
        self.player.compare_scores() # compares with high score


    def start_battle(self): 
        print("\n-----------------Player Info-----------------")
        # Displays highscore and the wand the user has
        print(f'Current High-score: {s.high_score}')
        print(f'Wand: {self.player.wand_type}')
        print("\n----------------Note-----------------")
        print("press 'e' to acess inventory of your potions! ")
        print("press enter or any other keys to continue your battles " 
              + "and action!")
        print("\n--------------WARNING---------------")
        print("Only click enter once you have the option to, in order to "
              + "avoid the battle from moving too quickly!")
        print("\n------------------Main Game------------------")
        for i in range(3): # Loops 3 times to create 3 different bettles
            # Chooses a random opponent from the list
            oponent = random.choice(self.oponent_list) 
            # Removes opponent from the list
            self.oponent_list.remove(oponent) 
            target = character.Oponent(oponent)
            print(f"\n{oponent} is approaching...")
            print("\nOh no! Battle #" + str(i + 1) +" is starting!")
            print('...')
            time.sleep(3)
            # Makes sure both enemy and user are alive to continue with battle
            while self.player.alive and target.alive:  
                print("press enter to continue or 'e' to access inventory:") 
                choice = input('> ')
                # Lets player choose potion by accessing it from potion module
                if choice == 'e':
                    self.player.potion_game.choose_potion()
                    continue 
                # Let player inflict damage on the enemy
                player_attack = self.player.inflict_damage(target)
                if target.alive: # Checks if the player is still alive
                    # Let enemy inflict damage in the player
                    target_attack = target.inflict_damage(self.player) 
                    difference = abs(player_attack - target_attack)
                    if player_attack > target_attack:
                        # Shows difference in attack and adding it to the score
                        print(f"\nDifference in attack damage: {difference}")
                        self.player.players_score += difference
                        print(f"score: {self.player.players_score}")
                if not self.player.alive: # Chacks if player is dead
                    print("Hagrid: Oh no, kiddo, stand up! ")
                    time.sleep(2)
                    print("Seems like the enemy has won... don't worry — yeh "
                          + "got more in yeh than yeh know!")
                    time.sleep(2)
                    self.battle_stat() # Gives them their performance stat
                    raise SystemExit
            if self.player.alive:
                print(f'\nCongrats {self.player.name}, you have defeated '
                      + f'{oponent}!')
                time.sleep(2)
                self.battle_stat()
        if self.player.alive: 
            time.sleep(1)
            print("\nWell done, yeh did it! Survived and won the battle — "
                  + "knew yeh had it in yeh all along!")
            print(f"\nBut oh no, {self.player.name}! Blimey —  Lord Voldemort"
                  + " just appeared on the battlefield! Use every bit of "
                  + "strength yeh got left — this is the fight over yer life!")
            time.sleep(2)
            oponent = 'Voldemort' # Have the opponent be Voldemort
            boss = character.Oponent('Voldemort')
            while self.player.alive and boss.alive:
                print("press enter to continue or 'e' to access inventory:") 
                choice = input('> ')
                if choice == 'e':
                    self.player.potion_game.choose_potion()
                    continue 
                player_attack = self.player.inflict_damage(boss)
                if boss.alive:
                    boss_attack = boss.inflict_damage(self.player)
                    difference = abs(player_attack - boss_attack) 
                    if player_attack > boss_attack:
                        print(f"Difference in attack damage: {difference}")
                        self.player.players_score += difference
                        print(f"score: {self.player.players_score}")
            if self.player.alive:
                print(f"Yeh won. Yeh a true hero of the wizarding world"
                      + f"{self.player.name}!")
                time.sleep(2)
                print('')
                self.battle_stat()
                raise SystemExit()
            else:
                print("Hagrid: Better luck next time, kiddo… but don't worry"
                      + " — yeh got more in yeh than yeh know!")
                time.sleep(2)
                self.battle_stat()
                raise SystemExit
    


    






    





