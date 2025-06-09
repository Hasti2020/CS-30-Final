'''import potion
import battle


def main():
    while True:
        choice = input('a or s: ')
        if choice == 's':
            potion.start_potion_game()
        elif choice == 'a':
            battle.start_battle()
main()
'''
import Explore as e
import wand as w
import potion as p
import spells as s
import house_quiz as h
import random as r
import character as c

def run_game():
    player_name = input("Hagrid: 'What’s your name, then?'\n> ")
    print(f"\nAlright then, {player_name}, you’re about to begin your magical journey. ✨")
    player_character = c.Player(player_name)
    player = e.Movement(player_name, player_character, {'row': 0, 'col': 0})
    player.current_map = player.hogwarts_map
    player.at_hogwarts = True
    player.location = {'row': 1, 'col': 0}  
    player.move()  

run_game()
