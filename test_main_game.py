import potion
import battle

potions = []

def main():
    while True:
        choice = input('a or s: ')
        if choice == 's':
            potions = potion.start_potion_game()
        elif choice == 'a':
            battle.start_battle(potions)
main()