import potion
import battle


def main():
    potions = ['Thunderbrew Potion']
    while True:
        choice = input('a or s: ')
        if choice == 's':
            potions = potion.start_potion_game()
        elif choice == 'a':
            battle.start_battle(potions)
main()