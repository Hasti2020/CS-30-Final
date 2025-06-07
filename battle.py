
def start_battle():
    import character
    import random
    import wand
    import score
    import time
    oponent_list = ['Draco', 'Luna', 'Peter', 'Bellatrix']
    player = character.Player({player.name}, False, False) 
    score.getScore()
    print("\n-----------------Player Info-----------------")
    print(f'Current High-score: {score.high_score}')
    print(f'Wand: {wand.Wand.get_wand()}')
    print("\n----------------Note-----------------")
    print("press 'e' to acess inventory of your potions! and enter to continue your battles!")
    print("\n------------------Main Game------------------")
    for i in range(3): # loops 3 times to create 3 different bettles
        oponent = random.choice(oponent_list) 
        oponent_list.remove(oponent) 
        target = character.Oponent(oponent)
        print(f"\nYou are now fighting against: {oponent}")
        print("\nBattle #" + str(i + 1) +" shall now begin!")
        if not player.alive:
            print("Better luck next time, kiddo… but don't worry — yeh got more in yeh than yeh know!")
            break
        while player.alive and target.alive:   
            choice = input()
            if choice == 'e':
                player.inventory()
                continue 
            player_attack = player.inflict_damage(target)
            if target.alive:
                target_attack = target.inflict_damage(player) 
                difference = abs(player_attack - target_attack)
                if player_attack > target_attack:
                    print(f"\nDifference in attack damage: {difference}")
                    player.players_score += difference
                    print(f"score: {player.players_score}")
                    print(f"health: {player.health}")
        if player.alive:
            print(f'\nCongrats {player.name}, you have defeated {oponent}!')
    
    if player.alive:
        print("\nWell done, yeh did it! Survived and won the battle — knew yeh had it in yeh all along!")
        print(f"But oh no, {player.name}! Blimey —  Lord Voldemort just appeared on the battlefield! Use every bit of strength yeh got left — this is the fight over yer life!")
        oponent = 'Voldemort'
        boss = character.Oponent('Voldemort')
        while player.alive and boss.alive:
            player_attack = player.inflict_damage(boss)
            if boss.alive:
                boss_attack = boss.inflict_damage(player)
                difference = abs(player_attack - boss_attack) 
                if player_attack > boss_attack:
                    print(f"Difference in attack damage: {difference}")
                    player.players_score += difference
                    print(f"score: {player.players_score}")
        if player.alive:
            print(f"Yeh won. Yeh a true hero of the wizarding world {player.name}!")
            player.compare_scores()
        else:
            print("Better luck next time, kiddo… but don't worry — yeh got more in yeh than yeh know!")
        input('enter to continue: ')


    






    





