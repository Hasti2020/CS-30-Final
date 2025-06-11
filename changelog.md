
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




# [Version 2.1] Have spells logic figured and worked

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
Emily: Got the spell casting to work for the player class, spell damage will be combined with regular damage

### Changed:
Emily: Changed wand module.py to wand.py
Emily: Changed spell_lesson to spell.py

### Edited:
Emily: Let player cast a spell once their health is under 60, and let them type in the spell's name under inflcit_damge
Emily: Editted all dialogs in battle to be Hargrid like



# [Version 2.2] Have scoring system and potion game made

## 2025-05-28 ##

### Added
Emily: added a healthing method for player child class
Emily: added voldemort to be the final boss after defeating 1st opponent
Emily: pasted code from battle, character, and spell from Thonny to Visual studio (Could not download VS at home)

### Edited
Emily: Adjusted the spell damages
Emily: Adjested opponents' power ranges

## 2025-05-29 ##

### Added
Emily: Created score.py and score.txt
Emily: Created getScore and newScore functions and have the player's score be saved into an external text
file
Emily: Addded score to battle. Player's difference in attack damge vs the opponent will be added up into their score
Emily: Added score system to final boss battle
Emily: Added a score display after every attack, and a call the wand_intro
Emily: Added the compare_score method in player class to update the higest score to the external file after every round

### Fixed
Emily: Made the transition to the Voldemort battle be in the same while loop of the regular battle


# [Version 2.3] Have potion game be made

## 2025-05-28 ##

### Added
Emily: Create potion.py
Emily: Created PotionGame class

## 2025-05-30 ##

### Added 
Emily: Created things_on_table and test methods and a database for the main menu of the potion game
Emily: Have the player be able to pick up ingredients from the table and store in their inventory 
Emily: Created a view_inventory method to test if the things picked up is in the inventory
Emily: Created brew_potions method and checks if player has the right ingrdients and start the brewing process
Emily: Have items be removed from table and inventory and potions be added to inventory

### Fixed
Emily: Fixed main menu database for potion game to avoid input error



# [Version 2.4] Connect potion inventory to game

## 2025-05-30 ##

### Added
Emily: Allow the player's potions to be stored in potion_inventory
Emily: Created test_main_game and a menu database to test out the battle and potion game quicker

### Changed
Emily: Turned the battle database into a function 


## 2025-05-31 ##
### Added
Emily: Allow player to know which wand they currently have before the battle
Emily: Allow player to view their potion invenotry during the battle, both in the regular and boss battle
Emily: Have potion's inventory be accessed in the player class by making it an object to the player class


## 2025-05-30 ##
### Added
Emily: Created a healing, inventory, countdown, and start_countdown method in player class
Emily: Allowed players to choose the potions they have and got the Wiggenweld potion to work by healing the player
Emily: Have the timer be printed on the console when player chooses the Maxima potion
Emily: Have the player's damage be increased by 5 DMG during the 30s countdown range




# [Version 3.1] Polishing Game

## 2025-06-02
### Changes
Emily: Adjusted countdown of Maxima potion to 15s
Emily: Added time.sleep() in between dialogs during battle so the console don't print out the actions all at once
Emily: Turned the database of the house quiz into a function
Emily: Added Stupefy to the list of spells

### Fixed
Emily: Fixed how the main battle menu look in the console
Emily: Have the player know what wand they have, score, and potions
Emily: Organized the while loop in battle, let ending dialog print when the player die
Emily: Have the regular battle loop through 3 times with different opponents

## 2025-06-02
### Added
Emily: Added more dialog and action narration for the battle game
Emily: Connected movement module with house_quiz module
Emily: Added more dialogs to the potion game

### Changes
Emily: Have the timer displayed on console be printed on the line below the battle dialogs

### Fixed
Emily: Fix how the main battle menu look in the console, added notes/instructions for players for which keys they type in
Emily: Fix how the potion main menu look like on the console

## 2025-06-04

### Added
Emily: Allow the players to access the Thunderbrew potion during the battle and allow them to cause 50 damage on their next attack
Emily: Have the players' health displayed with their score after every attack

## 2025-06-05

### Added
Emily: Added view_recipe method to potion game for players to view the potions recipes during the game

## 2025-06-05

### Fixed
Emily: Allow players to see all their potions at the start of the battle

### Changes
Emily: Adjust time.sleep() length in between the dialogs in the potion game



# [Version 3.2] Connecting battle + potion + spells to movement 

## 2025-06-05

### Added
Emily: Connected battle and potion modules to movement module
Emily: Added a message that allows players to know they brewed the potions with the wrong ingredients in the potion game
Emily: Added a list of spells for the player to use by typing its name during the battle when their health is low
Emily: Give a 5s timer for player to type the spell if they want to use it in the battle (Ended up scratching out the idea due to timer and input overlap)
Emily: Added dialog to the spell lessons

### Change
Emily: Have the user recieve 2 potions instead of 1 after brewing
Emily: Have the brewing dialog be in the for loop for it too print before each type of potion is brewed
Emily: Have the spell_list be in the spell class instead of being outside

### Fixed
Emily: Have all potions made in the potion game be stored in the player once the battle starts

### Removed 
Emily: Removed spell typing timer in player class' inflicted_damage method

## 2025-06-07
### Added
Emily: Connected spell lesson module into movement module


# [Version 3.3] Connecting battle + potion to movement 

## 2025-06-7
### Added
Hasti: Created main.py to make the main menu database for the game
Hasti + Emily: Connected the main.py module with all the modules


# [Version 4.1] Fixing bugs

## 2025-06-7
### Changes
Emily: Have the brewing dialog be outside the for loop for the players to not wait too long to recieve their potions (if they brew all at once)
Emily: Turned start_battle function into a class
Emily: Changed Spell_Lesson() function to spell_lesson()
Emily: Changed inventory method in player class to choose_potion

### Fixed
Emily: Have the wand not be randomized again every time the player's wand name is printed
Emily: Fixed dialogs in potion game
Emily: Have all potions made in the potion game be stored as the player's attribute once the battle starts (Bug occured again after making battle into a class)

## 2025-06-8
### Fixed
Emily: fixed player's potion invenotry storing logic, attributes into objects for player class

### Change
Emily: made potion inventory attribute in player class to an object
Emily: move potion_invenotry from potion module to be just in player
Emily: Adjusted thurderbrew potion strength and time limit for maxima potion


# [Version 4.2] Polishing Game

## 2025-06-8

### Added
Emily: added more dialogs to spell lesson, talked about the spells and their power damage
Emily: Added system exit to when the player dies or game ends

## 2025-06-9

### Changes
- Emily: Moved choose_potion from player class into potion module







