
===
# Story line
We will create a Harry Potter themed game where the students would at first get to choose their wand, pets, potion and enter the triwizard tournament in Hogwarts. Where they will be fighting with randomized oponents, and would win if they sucessfuly defeated all their oponents and remain alive in the end with the highest score.
Flow of the game:
- Hagrid invites player to Hogwarts
- They'll first to go Daiogon Alley where they will be able to pick a wand, a pet and school supplies
- They'll then go to Hagwarts
- They'll be assigned a house based on a short quiz
- They'll have the option to attend classes (potions, charms, transfiguratuon)
- Class quiz with questions to earn bonus points
- There will be hidden hints in those classes that can help in future battles
- They'll be invited to join the ? tournament at their own risk
- Nice to have: They'll have to retrieve a Dragon egg (for bonus points)\
- Three battles with random apponants and if they survive,
- They'll face the final boss aka Voldemort who showed up
The player has been chosen to enter the upcoming triWizzard tournament.  First, they would get to choose their wand, pets, potion, and enter the Triwizard Tournament in Hogwarts. With every duel, their goal is to survive, deal damage, and score points. They would win by defeating all enemies, staying alive, and getting the highest score.

# Need To Have List:
Character Module:
- list of all opponents with different strengths and they will be assigned randomly to the players. (random library)
- The opponents will be their own child classes, with the player being a parent classes
- Where the parent class would have a take_damage function, maybe heal
- The player classes would be the child to that parent class, containing fuctions like inflict_damage.
- The oppenent will be the child of the player class also having the same function as it. 

Wand Module:
- Each wand would be in a list and have a different power range, and each attack would be a random value within that range.

Game Module:
- Contains the final battle
- 2 different locations that we can move around, hogwarts and diagon alley.
- save result of their battles in an external file for each player. 
- Hagrid will be the narrator and helper. 
- Save high score
- The goal is not to die and get the high score

# Nice To Have List:  
- the player gets to go around the forbidden forest and survive all the obstacles there.
- Riddle game to get more scores
- house sort
- changes font color to the house color
- Navigate in a maze to find the dragon egg


>>>>>>> 2c10f6cbb016b1df949c196e024ea85b1cacd634

