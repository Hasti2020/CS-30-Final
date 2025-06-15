
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
- Hasti: Created the wand module
- Hasti: Made the class for wand and a list of all options with different powers and description
- Hasti: Changed the wand power from a fixed number to a randon number between a set range for each wand
- Hasti: Renamed the "wand module" name to just "wand"
- Hasti: Created Movement module
- Hasti: Added the two maps to the movement module
- Hasti: Added the movement logic in the tiles
- Hasti: Added scenarios to each some tiles of Daigon Alley map (The bank and the wand shop)

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
- Hasti: Added logic to Diagon Alley tiles(Bookstore, pet shop)
- Hasti: Added transition from Diagon Alley to Hogwars logic
- Hasti: Created a test file to run the movement logic in

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
- Hasti: Added Tabulate to the movement module
- Hasti: Added a map dislay anytime the player moves
- Hasti: Added post office, joke shop and station scenario and logic
- Hasti: Created a tabulate test file to test code
- Hasti: Created an emojy test file to test how emojies show up on the map grid

## Fixed
- Emily: Fixed the player and opponent inflict damage method to have them attack each other in battle.py
- Emily: Fixed the player's attack so their damage range is within that of their wand
- Emily: Adjusted the power range of opponents
- Hasti: Fixed the logic of nthe flow of the game (ie. first have to go to the bank to get money to be able to shop)
- Hasti: Renamed "movement" to "new movement" b\c of an error I got when we pushed and pulled
- Hasti: Fixed a bug in tile logic (wrong spelling) + changed a few descriptions

### Edit
- Emily:Docstringed cast_spell function in wand module 
- Hasti: Changed everything in new movement module to Hagrid narration


# [Version 2.1] Have spells logic figured and worked

## 2025-05-27 ##

### Added
- Emily: Added color code into the house result dialog in house_quiz.py so when the player gets into a house, a
dialog will be displayed congratulating them into the house with the text having the house color.
- Emily: Created spell_lesson.py
- Emily: Added a list of spells
- Emily: Created a spell class and spell_power method that returns a damage for each spells
- Emily: Created a cast_spell to print out a dialog when the player casts a spell and a dialog if the player casts
an unknown spell
- Emily: Added dialogs for when the player is allowed to cast spells in inflict_damage
- Emily: Got the spell casting to work for the player class, spell damage will be combined with regular damage

### Changed:
- Emily: Changed wand module.py to wand.py
- Emily: Changed spell_lesson to spell.py

### Edited:
- Emily: Let player cast a spell once their health is under 60, and let them type in the spell's name under inflcit_damge
- Emily: Editted all dialogs in battle to be Hargrid like

# [Version 2.2] Have scoring system and potion game made

## 2025-05-28 ##

### Added
- Emily: added a healthing method for player child class
- Emily: added voldemort to be the final boss after defeating 1st opponent
- Emily: pasted code from battle, character, and spell from Thonny to Visual studio (Could not download VS at home)
- Hasti: Changed everything in new movement module to Hagrid narration


### Edited
Emily: Adjusted the spell damages
Emily: Adjested opponents' power ranges
Hasti : Deleted all the quotation marks in Hagrid's lines

## 2025-05-29 ##

### Added
- Emily: Created score.py and score.txt
- Emily: Created getScore and newScore functions and have the player's score be saved into an external text
file
- Emily: Addded score to battle. Player's difference in attack damge vs the opponent will be added up into their score
- Emily: Added score system to final boss battle
- Emily: Added a score display after every attack, and a call the wand_intro
- Emily: Added the compare_score method in player class to update the higest score to the external file after every round
- Hasti: Added logic to each tile in Hogwarts
- Hasti: Improted the random library and added a random outcome for one of the tiles in Hagwarts
- Hasti:  Added the Hogwarts map display using tabulate
### Fixed
- Emily: Made the transition to the Voldemort battle be in the same while loop of the regular battle
- Hasti: Improved the transition logic form Diagon Alley to Howarts
- Hasti: Fixed errors in explore diagon tile method (missinf self.)
- Hasti: Changed if to elif in explore method
- Hasti: Moved the map tile from outside the class into the __init.__ method
- Hasti: Removed the unnecessary attributes fromt the class
- Hasti: Removed some parts of the tile logic that were no longer in use


# [Version 2.3] Have potion game be made

## 2025-05-28 ##

### Added
- Emily: Create potion.py
- Emily: Created PotionGame class

## 2025-05-30 ##

### Added 
- Emily: Created things_on_table and test methods and a database for the main menu of the potion game
- Emily: Have the player be able to pick up ingredients from the table and store in their inventory 
- Emily: Created a view_inventory method to test if the things picked up is in the inventory
- Emily: Created brew_potions method and checks if player has the right ingrdients and start the brewing process
- Emily: Have items be removed from table and inventory and potions be added to inventory

### Fixed
- Emily: Fixed main menu database for potion game to avoid input error



# [Version 2.4] Connect potion inventory to game

## 2025-05-30 ##

### Added
- Emily: Allow the player's potions to be stored in potion_inventory
- Emily: Created test_main_game and a menu database to test out the battle and potion game quicker

### Changed
- Emily: Turned the battle database into a function 


## 2025-05-31 ##
### Added
- Emily: Allow player to know which wand they currently have before the battle
- Emily: Allow player to view their potion invenotry during the battle, both in the regular and boss battle
- Emily: Have potion's inventory be accessed in the player class by making it an object to the player class


## 2025-05-30 ##
### Added
- Emily: Created a healing, inventory, countdown, and start_countdown method in player class
- Emily: Allowed players to choose the potions they have and got the Wiggenweld potion to work by healing the player
- Emily: Have the timer be printed on the console when player chooses the Maxima potion
- Emily: Have the player's damage be increased by 5 DMG during the 30s countdown range




# [Version 3.1] Polishing Game

## 2025-06-02
### Changes
- Emily: Adjusted countdown of Maxima potion to 15s
- Emily: Added time.sleep() in between dialogs during battle so the console don't print out the actions all at once
- Emily: Turned the database of the house quiz into a function
- Emily: Added Stupefy to the list of spells

### Fixed
- Emily: Fixed how the main battle menu look in the console
- Emily: Have the player know what wand they have, score, and potions
- Emily: Organized the while loop in battle, let ending dialog print when the player die
- Emily: Have the regular battle loop through 3 times with different opponents

## 2025-06-02
### Added
- Emily: Added more dialog and action narration for the battle game
- Emily: Connected movement module with house_quiz module
- Emily: Added more dialogs to the potion game

### Changes
- Emily: Have the timer displayed on console be printed on the line below the battle dialogs

### Fixed
- Emily: Fix how the main battle menu look in the console, added notes/instructions for players for which keys they type in
- Emily: Fix how the potion main menu look like on the console

 ## 2025-06-03
 ### Chnaged
 - Hasti: Set location to be the location of the player instead of Flase at the begining of the game

### Added
- Hasti: Added logic to track the map the player is in and set that to "current map"
- Hasti: Added logic to end the game when the player doesn't want to explore anymore

## 2025-06-04

### Added
- Emily: Allow the players to access the Thunderbrew potion during the battle and allow them to cause 50 damage on their next attack
- Emily: Have the players' health displayed with their score after every attack

## 2025-06-05

### Added
- Emily: Added view_recipe method to potion game for players to view the potions recipes during the game

## 2025-06-05

### Fixed
- Emily: Allow players to see all their potions at the start of the battle

### Changes
- Emily: Adjust time.sleep() length in between the dialogs in the potion game



# [Version 3.2] Connecting battle + potion + spells to movement 

## 2025-06-05

### Added
- Emily: Connected battle and potion modules to movement module
- Emily: Added a message that allows players to know they brewed the potions with the wrong ingredients in the potion game
- Emily: Added a list of spells for the player to use by typing its name during the battle when their health is low
- Emily: Give a 5s timer for player to type the spell if they want to use it in the battle (Ended up scratching out the idea due to timer and input overlap)
- Emily: Added dialog to the spell lessons
- Hastil: Imported house quiz, battle, potion, spells modules
- Hasti: For each tile of the maps, added the corresponding module and called the methods
- Hasti: Added the house sort quiz to the dining hall tile for the players first visit
- Hasti: 

### Change
- Emily: Have the user recieve 2 potions instead of 1 after brewing
- Emily: Have the brewing dialog be in the for loop for it too print before each type of potion is brewed
- Emily: Have the spell_list be in the spell class instead of being outside
- Hasti: Changed hallway tile to spell class and class to potion class tile
- Hasti:  Changed the logic for hallway and class tile to go with the new spell and potion class story line
- Hasti: Doc stringed the test main gamae . py b/c it was interfering with the other files

### Fixed
- Emily: Have all potions made in the potion game be stored in the player once the battle starts
- Hasti: Improved the logic for the tiles when the player enters them for the second time (ie. You've already been here...)

### Removed 
- Emily: Removed spell typing timer in player class' inflicted_damage method

## 2025-06-07
### Added
- Emily: Connected spell lesson module into movement module


# [Version 3.3] Connecting battle + potion to movement 

## 2025-06-7
### Added
- Hasti: Created main.py to make the main menu database for the game
- Hasti + Emily: Connected the main.py module with all the modules


# [Version 4.1] Fixing bugs

## 2025-06-7
### Added
- Hasti: Added text to the house sorting module and added a story line
- Hasti: Added the game goal for the player from Dumbldore's narration
- Hasti: Added sleep timer so that the text types out more natural

### Changes
- Emily: Have the brewing dialog be outside the for loop for the players to not wait too long to recieve their potions (if they brew all at once)
- Emily: Turned start_battle function into a class
- Hasti: Changed Spell_Lesson() function to spell_lesson()
- Emily: Changed inventory method in player class to choose_potion
- Hasti: Renamed the module "new movement" to "Explore" b/c it was handeling much more than just movement

### Fixed
- Emily: Have the wand not be randomized again every time the player's wand name is printed
- Emily: Fixed dialogs in potion game
- Emily: Have all potions made in the potion game be stored as the player's attribute once the battle starts (Bug occured again after making battle into a class)
- Hasti: Connected battle to one of the tiles in the Explore module (front doors)
- Hasti: Gave the player the option to choose to battle when they get to front door
- Hasti: In house quiz module, moved import random from inside the class to the first line
- Hasti: Added timer for the wand module to reveal the wand smoother

## 2025-06-8
### Fixed
- Emily: fixed player's potion invenotry storing logic, attributes into objects for player class

### Change
- Emily: made potion inventory attribute in player class to an object
- Emily: move potion_invenotry from potion module to be just in player
- Emily: Adjusted thurderbrew potion strength and time limit for maxima potion


# [Version 4.2] Polishing Game before Beta Test

## 2025-06-8

### Added
- Emily: added more dialogs to spell lesson, talked about the spells and their power damage
- Emily: Added system exit to when the player dies or game ends 
- Hasti: Deleted all the attributes that related to the player from Explore to character module
- Hasti: Initialized all of them in character class under player
- Hasti: Edited all the lines where said attributes were mentined and calling them back in character (ie. self.have_money --> self.player.have_money)
- Hasti: Moved all the imported libraries and modules from inside the class to outside
- Hasti: Made the necesarry changes to the way movement was called in main game since all the attributes were moved to charcter module under the child class player
- Hasti: Debugged and fixed the lines that I missed the first time I went through

## 2025-06-9

### Changes
- Emily: Moved choose_potion from player class into potion module


# [Version 4.3] Polishing Game + Fixing Bugs found after Beta and Alpha test


## 2025-06-12

### Changes
- Emily: Added more instructions for the potion game, stating that you are supposed to get 2 potions
of each after every brew
- Emily: Got rid of time.sleep() in the battles entirely to prevent players from spamming the enter
button and getting alot of texts at once
- Emily: Changed spell casting from typing to choosing the corresponding number to make it easier and
engaging.
- Emily: Changed ingredients of Maxima potion 'Leech Juice' to 'Lemon Juice' to not match with Thunderbrew's 
ingredients.
- Emily: Removed brackets from potion recipe when it is being printed
- Added a battle status method to be called at the end of the battles

## 2025-06-13

### Fixes
- Emily: Prevented people from stacking Maxima Potion to avoid glitching of the timer
- Emily: Also prevented people from stacking Thunderbrew potion
- Emily: Made Stupefy spell added to the spell_list only if the player read the book
in the library and learnt the spell
- Emily: Added raise system exit when player died during the regular battle

### Changes
- Emily: Adjusted the power levels of the spells, enemies, and potions


# [Version 4.4] Pep 8 and final polishing

## 2025-06-13

### Added
- Emily: Added comments and pep 8

## 2025-06-14

### Added:
- Emily: Allow the player to quit during the battles
- Emily: Added Pep 8 and comments 

### Changes
- Emily: Have the ingredients inventory merge with the potion inventory and call it inventory

## 2025-06-15

### Added:
- Hasti: Added pep 8 and comments to the wand module

