import wand
import character
player = character.Player('Harry')
target = character.Oponent(character.oponent)


while player.alive and target.alive:
    player.inflict_damage(target)
    if target.alive:
        target.inflict_damage(player)
    choice = input('enter to continue: ')
    
if player.alive: 
    print("\nCongrats you survived and won the battle")
else:
    print("\nBetter Luck next time.")





    



