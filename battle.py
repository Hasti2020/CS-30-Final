import character
import random
import wand
import score
import time


class Battle:

    def __init__(self, player):
        self.oponent_list = ['Draco', 'Luna', 'Peter', 'Bellatrix']
        wand.Wand.get_wand()
        self.player = player

    def start_battle(self): 
        score.getScore()
        print("\n-----------------Player Info-----------------")
        print(f'Current High-score: {score.high_score}')
        print(f'Wand: {self.player.wand_type}')
        print("\n----------------Note-----------------")
        print("press 'e' to acess inventory of your potions! and enter to continue your battles!")
        print("\n------------------Main Game------------------")
        for i in range(3): # loops 3 times to create 3 different bettles
            oponent = random.choice(self.oponent_list) 
            self.oponent_list.remove(oponent) 
            target = character.Oponent(oponent)
            print(f"\nYou are now fighting against: {oponent}")
            print("\nBattle #" + str(i + 1) +" shall now begin!")
            if not self.player.alive:
                print("Better luck next time, kiddo… but don't worry — yeh got more in yeh than yeh know!")
                break
            while self.player.alive and target.alive:  
                print("press enter to continue or 'e' to access inventory:") 
                choice = input()
                if choice == 'e':
                    self.player.choose_potion()
                    continue 
                player_attack = self.player.inflict_damage(target)
                if target.alive:
                    target_attack = target.inflict_damage(self.player) 
                    difference = abs(player_attack - target_attack)
                    if player_attack > target_attack:
                        print(f"\nDifference in attack damage: {difference}")
                        self.player.players_score += difference
                        print(f"score: {self.player.players_score}")
            if self.player.alive:
                print(f'\nCongrats {self.player.name}, you have defeated {oponent}!')
        
        if self.player.alive:
            time.sleep(1)
            print("\nWell done, yeh did it! Survived and won the battle — knew yeh had it in yeh all along!")
            print(f"But oh no, {self.player.name}! Blimey —  Lord Voldemort just appeared on the battlefield! Use every bit of strength yeh got left — this is the fight over yer life!")
            time.sleep(2)
            oponent = 'Voldemort'
            boss = character.Oponent('Voldemort')
            while self.player.alive and boss.alive:
                print("press enter to continue or 'e' to access inventory:") 
                choice = input()
                if choice == 'e':
                    self.player.choose_potion()
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
                self.player.compare_scores()
            else:
                print("Better luck next time, kiddo… but don't worry — yeh got more in yeh than yeh know!")
            input('enter to continue: ')


    






    





