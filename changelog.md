
# [Version 1.1] Main logic for movement, maps, and house quiz

## 2025-05-20 ##
### Added:
- Hasti + Emily: created character.py
- Hasti + Emily: created character parent class
- Emily: Created inflict_damage in character class
- Emily: Added attributes, max_health, wand, alive to character

## 2025-05-23 ##
### Added:
- Emily: Created house_quiz.py and house_quiz.txt
- Emily: Added questions into an external file, house_quiz.txt
- Emily: Made database for the house sorting

( Hasti: Main logic for movemnet and wand)

# [Version 1.2] Main Logic for character/player/opponent

## 2025-05-25 ##
### Removed:
- Emily: Removed max_health, wand in character class
- Emily: Removed inflict_damage method in character

### Added:
- Emily: Created player and opponent child classes to character
- Emily: Added take_damage method and logic to character
- Emily: added wand_type attribute to player, for them to recieve wand generated from wand module
- Emily: Created inlfict_damge methods and logic to player and opponent class
- Emily: Added list of opponents and their power ranges


# [Version 1.3] Have a working battle
## 2025-05-26 ##

### Added
- Emily: Created battle.py 
- Emily: Created a database for the battle and let the player and opponent inflict and take damge on each other
- Emily: Added the dialogs for battle
- Emily: Have the player and opponent's health be displayed during each attack under take_damge
- Emily: Added action reading when the player and opponent is about to attack on inflict_damge and print how much damage they took
- Emily: Have the oponent be randomized in the battle
- Emily: Added movement method in player class

## Fixed
- Emily: Fixed the player and opponent inflict damage method to have them attack each other in battle.py
- Emily: Fixed the player's attack so their damage range is within that of their wand
- Emily: Adjusted the power range of opponents


### Edit
- Emily:Docstringed cast_spell function in wand module 

# [Version 2.1] Have spells logic figured

## 2025-05-27 ##

### Added
Emily: Added color code into the house result dialog in house_quiz.py so when the player gets into a house, a
dialog will be displayed congratulating them into the house with the text having the house color.
Emily: Created spell_lesson.py
Emily: Added a list of spells
Emily: Created a spell class and spell_power method that returns a damage for each spells
Emily: Created a cast_spell to print out a dialog when the player casts a spell and a dialog if the player casts
an unknown spell
Emily: Added dialogs for when the player is allowed to cast spells in inflict_damage
Emily: Have the spell casting damage added to the regular damage if is used

### Changed:
Emily: Changed wand module.py to wand.py
Emily: Changed spell_lesson to spell.py

### Edited:
Emily: Let player cast a spell once their health is under 60, and let them type in the spell's name under inflcit_damge
Emily: Editted all dialogs in battle to be Hargrid like


# [Version 2.2] Have potions game made

## 2025-05-28 ##

### Added
Emily: added a healthing method for player child class
Emily: Create potion.py
Emily: Created score.py and score.txt
Emily: Created getScore and newScore functions and have the player's score be saved into an external text
file after the battle (Saves current highest score)
Emily: Player's difference in attack damge vs the opponent will be added up into their score

### Edited
Emily: Adjusted the spell damages
Emily: Adjested opponents' power ranges

## 2025-05-29 ##

### Added
Emily: Created PotionGame class
Emily: Created things_on_table and test methods and a database for the main menu of the potion game
Emily: Have the player be able to pick up ingredients from the table and store in their inventory 
Emily: Created a view_inventory method to test if the things picked up is in the inventory
Emily: Created brew_potions method and checks if player has the right ingrdients and start the brewing process

## 2025-05-30 ##

### Added 
Emily: Added the compare_score method in player class to update the higest score after every round
Emily: Have the battle database become a fuction called start battle and added voldemort to be the final boss
after defeating 1st opponent

Emily: Fixed main menu 







