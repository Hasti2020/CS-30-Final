A checklist created for every element of the program that needs alpha testing.
(you can use your development plan and changelog to help you generate a list) 
Summary of the results of the alpha testing, along with a list of fixes to be made.

# Alpha Testing Checklist:
- Exception Handling in the potion, battle, and character modules
- Maxima Potion timer and player's input overlap
- Stacking Maxima Potion
- High Score storing
- Stopping the game once player dies
- Increase attacks (Do they really work?)
- Dialogs (Make sure no grammar error, spelling mistakes, and on themed)
- Format on the console for the battle
- Power levels adjustments

# Alpha Test Results!:
- Stacking Maxima Potion ended up messing up the timer, the game does not 
know which to print on the screen so it keeps glitching.
- When player dies in the regular battle, there was no SystemExit() yet so it returns
them to hogwarts
- All dialogs were good and some were the game system speaking so it makes sense that
it does not sound like Hagrid or the characters.
- The high score stores!!
- Exception Handling messgaes were good
- Battle console looks a little confusing
- The increase_attack and damage works
- Maxima potion timer seem a bit to long
- Thunderbrew potion damage is somehow at 50?
- Spells are too powerful

# Fixes needed to be made:
- Have the time.sleep() be get rid of during the battles due to confusions in Beta testing
- Have the player not stack Maxima or Thunderbrew potions (If self.player.increase_attack is True then dont let them take more)
- Add raise SystemExit() to the death scene of regular battle
- Solve overlap of spells and timer by letting the player just choose the corresponding number
- Make the console easier to read for battle
- Maybe have the battle stats be printed after every spell attacks?
- Adjust timer of maxima potion from 20 to 15 or 10
- Adjust thunderbrew damage to 20
- Adjust some of the spells' powers or have their health be lower to use it
- Rename increase_attack and damage 
- Have the ingredients invenotry merge with the potion inventory and call it inventory