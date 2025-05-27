import character
import random
oponent_list = ['Draco', 'Luna', 'Peter', 'Bellatrix']
oponent = random.choice(oponent_list) 
player = character.Player('Harry')
target = character.Oponent(oponent)


while player.alive and target.alive:
    player.inflict_damage(target)
    if target.alive:
        target.inflict_damage(player)
    choice = input('enter to continue: ')


if not player.alive:
    print("better luck next time kiddo")
else:
    print("\nCongrats you survived and won the battle")
    print(f"But oh no {player.name}! Lord Voldemort just appeared on the battlefield! Use all the stength you have left to battle him!")
    oponent = 'Voldemort'
    boss = character.Oponent('Voldemort')
    while player.alive and boss.alive:
        player.inflict_damage(boss)
        if boss.alive:
            boss.inflict_damage(player)
    if player.alive:
        print("you won")
    else:
        print("u lost")
    choice = input('enter to continue: ')


    






    



