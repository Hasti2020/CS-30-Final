import character
import random

oponent_list = ['Draco', 'Luna', 'Peter', 'Bellatrix']
oponent = random.choice(oponent_list) 
player = character.Player('Harry') # player = character.Player('{player_name}')
target = character.Oponent(oponent)


while player.alive and target.alive:
    player.inflict_damage(target)
    if target.alive:
        target.inflict_damage(player)  
    choice = input('enter to continue: ')


if not player.alive:
    print("Better luck next time, kiddo… but don't worry — yeh got more in yeh than yeh know!")
else:
    print("\nWell done, yeh did it! Survived and won the battle — knew yeh had it in yeh all along!")
    print(f"But oh no, {player.name}! Blimey —  Lord Voldemort just appeared on the battlefield! Use every bit of strength yeh got left — this is the fight over yer life!")
    oponent = 'Voldemort'
    boss = character.Oponent('Voldemort')
    enter_final_battle = input('enter to continue: ')
    while player.alive and boss.alive:
        player.inflict_damage(boss)
        if boss.alive:
            boss.inflict_damage(player)
    if player.alive:
        print("Yeh won. Yeh a true hero of the wizarding world {player.name}!")
    else:
        print("Better luck next time, kiddo… but don't worry — yeh got more in yeh than yeh know!")
    choice = input('enter to continue: ')


    






    





