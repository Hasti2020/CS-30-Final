import character
import random
import wand
import score
import time


class Battle:

    def __init__(self, player):
        self.oponent_list = ['Draco', 'Luna', 'Peter', 'Bellatrix']
        wand.Wand.get_wand()
        score.getScore()
        self.player = player

    def battle_stat(self):
        print('---------------STATS---------------')
        print(f"Score: {self.player.players_score}")
        print(f"Health: {self.player.health}")
        self.player.compare_scores()

    def start_battle(self): 
        print("\n-----------------Player Info-----------------")
        print(f'Current High-score: {score.high_score}')
        print(f'Wand: {self.player.wand_type}')
        print("\n----------------Note-----------------")
        print("press 'e' to acess inventory of your potions! ")
        print("press enter or any other keys to continue your battles and action!")
        print("\n--------------WARNING---------------")
        print("Dialogs in the battle will be printed with wait times in between like this...")
        print("Only click enter once you have the option to, in order to avoid the battle from moving too quickly!")
        print("\n------------------Main Game------------------")
        for i in range(3): # loops 3 times to create 3 different bettles
            oponent = random.choice(self.oponent_list) 
            self.oponent_list.remove(oponent) 
            target = character.Oponent(oponent)
            print(f"\n{oponent} is approaching...")
            print("\nOh no! Battle #" + str(i + 1) +" is starting!")
            print('...')
            time.sleep(3)
            while self.player.alive and target.alive:  
                print("press enter to continue or 'e' to access inventory:") 
                choice = input('> ')
                if choice == 'e':
                    self.player.potion_game.choose_potion()
                    continue 
                player_attack = self.player.inflict_damage(target)
                if target.alive:
                    target_attack = target.inflict_damage(self.player) 
                    difference = abs(player_attack - target_attack)
                    if player_attack > target_attack:
                        print(f"\nDifference in attack damage: {difference}")
                        self.player.players_score += difference
                        print(f"score: {self.player.players_score}")
                if not self.player.alive:
                    print("Hagrid: Oh no, kiddo, stand up! Seems like the enemy has won... don't worry — yeh got more in yeh than yeh know!")
                    time.sleep(2)
                    self.battle_stat()
                    raise SystemExit
            if self.player.alive:
                print(f'\nCongrats {self.player.name}, you have defeated {oponent}!')
                time.sleep(2)
                self.battle_stat()
                
        
        if self.player.alive:
            time.sleep(1)
            print("\nWell done, yeh did it! Survived and won the battle — knew yeh had it in yeh all along!")
            print(f"\nBut oh no, {self.player.name}! Blimey —  Lord Voldemort just appeared on the battlefield! Use every bit of strength yeh got left — this is the fight over yer life!")
            time.sleep(2)
            oponent = 'Voldemort'
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
                print(f"Yeh won. Yeh a true hero of the wizarding world {self.player.name}!")
                time.sleep(2)
                self.battle_stat()
            else:
                print("Hagrid: Better luck next time, kiddo… but don't worry — yeh got more in yeh than yeh know!")
                time.sleep(2)
                self.battle_stat()
                raise SystemExit
    


    






    





