###############################################################################
'''
This module handles the potion brewing part and choosing potion part of the 
game. Player will pick ingredients, brew potions, and use them to help in 
battles. The Wiggenwelf potion can heal you, Maxima boosts your attack, 
and Thunderbrew gives a big damage strike. It includes inventory management, 
recipes, and a little story with Snape guiding you. Also the 
time.sleep() is to show the texts slowly to the console
'''
###############################################################################
# Imports and Global Variables-------------------------------------------------
import time


class PotionGame:
    '''Controls/Starting the potion game, potion brewing and choosing potion'''

    def __init__(self, player):
        '''Initializes the potions and ingredients for the player'''
        self.player = player
        # Ingredients for the potions
        self.ingredients = [
            'Horklump Juice', 
            'Dittany Leaves', 
            'Lemon Juice', 
            'Spider Fang', 
            'Leech Juice', 
            'Stench of the Dead'
        ]
        # Ingredients needed for each potion
        self.potions = {
            'Wiggenweld Potion': ['Horklump Juice', 'Dittany Leaves'],
            'Maxima Potion': ['Lemon Juice', 'Spider Fang'],
            'Thunderbrew Potion': ['Leech Juice', 'Stench of the Dead']
        }


    def things_on_table(self):
        '''
        This method would let the player chooses their ingredients on
        the table and bring it to their brewing station.
        '''
        global choice
        print("---------THINGS ON YOUR TABLE---------")
        i = 1
        # Prints out a list of items on the table
        for item in self.ingredients:
            print(f"{i}. {item}")
            i += 1
        try:
            choice = int(input("What do you want to grab to the brewing "
                               + "station?: "))
            # Checks if the player's choice is within the list
            if 1 <= choice <= len(self.ingredients):
                # Makes sure the coresponding number match with the python rule
                selected = self.ingredients[choice-1]
                # Removes the item on the table
                self.player.inventory.append(selected)
                # Adds the item into player's inventory
                self.ingredients.pop(choice-1)
                return selected
        # Makes sure to not crash the program if player did not enter a number
        except ValueError: 
            print("You did not collected anything....")
            return None

    
    def view_recipe(self):
        '''This method would print out all the potions recipes'''
        print("\n---------POTIONS RECIPE---------")
        for key, value in self.potions.items():
            # Makes sure there are no brackets from the list
            print(f"- {key}: {', '.join(value)}")


    def choose_potion(self):
        '''
        This method allow the player to choose the potions from their 
        inventory during their battles, and activate some healing,
        and increase in damage from the player
        '''
        print("\n---------------Your Inventory---------------")
        i = 1
        # Prints out all the items from the player's inventory for the battle
        for item in self.player.inventory:
            print(f"{i}. {item}")
            i += 1
        try:
            choice = int(input("What potion do you want to use?: "))
            # Checks if the choice is within range of the list
            if 1 <= choice <= len(self.player.inventory):
                selected = self.player.inventory.pop(choice-1)
                # Checks if the player chooses Wiggenweld potion
                if selected == 'Wiggenweld Potion':
                    print(f'\nYou have used the Wiggenweld Potion!')
                    # Activate the healing method from player
                    self.player.healing()
                # Checks if the player have not already use the Maxima potion 
                # to avoid stacking
                if selected == 'Maxima Potion' and \
                not self.player.maxima_increase:
                    print(f'\nYou have used the Maxima Potion!')
                    print(f'\nYour attacks will increase by 5 damage for the'
                          + f' next 20 seconds!')
                    # Have the player's attacks increase by 5 DMG
                    self.player.maxima_increase = True
                    # Have the timer begins
                    self.player.start_countdown(15)
                # Prevents player from stacking Maxima potion  
                elif selected == 'Maxima Potion' and \
                    self.player.maxima_increase:
                    print('You are already currently using the Maxima potion'
                          + ' already!')
                # Checks if the player have not already use the Thunderbrew 
                # potion to avoid stacking
                if selected == 'Thunderbrew Potion' and \
                    not self.player.thunderbrew_increase:
                    print(f'\nYou have used the Thunderbrew Potion')
                    print(f'\nYour next attack will be increased by '
                          + f'20 damage!')
                    self.player.thunderbrew_increase = True
                # Prevents player from stacking Thunderbrew potion  
                elif selected == 'Thunderbrew Potion' and \
                    self.player.thunderbrew_increase:
                    print('You already equipped the Thunderbrew'
                    '+ potion!')
                else:
                    print("That was not even a potion!")
            else:
                print("You do not have that potion!")
        # Makes sure to not crash game if the input was not an integer
        except ValueError: 
            print("You do not have that potion!")
            return None
    

    def brew_potion(self):
        '''This method will allow and handle the potion brewing process'''
        brew = False # Tracks if the player has brew a potion
        print("brewing...")
        time.sleep(1)
        print("brewing...")
        time.sleep(1)
        print("almost done!")
        time.sleep(1)
        # Makes sure the items in the player's inventory matches with the
        # ingredients needed to make the potions
        for potion, required_items in self.potions.items():
                if all(item in self.player.inventory 
                       for item in required_items):
                        for item in required_items:
                            # Removes the ingredients
                            self.player.inventory.remove(item)
                            # puts in loop to get 2 potions
                            print(f'+ you have brewed a {potion}') 
                            # Adds the brewed potion to inventory
                            self.player.inventory.append(potion)
                            # Let the game know a potion was brewed
                            brew = True
        if not brew: # Checks if the player has failed to brew a potion
            print(f'you have brewed no potion...')
            print("Snape: Looks like someone did not follow the recipes"
                  + " correctly...")
            time.sleep(1)


    def view_inventory(self):
        '''
        This method allows for the player to check their inventory 
        during the potion game only
        '''
        print("\n---------INVENTORY---------")
        i = 1
        for item in self.player.inventory:
            print(f"{i}. {item}")
            i += 1


    def start_potion_game(self):
        '''
        This method will handle the main menu of the potion game and includes dialogs
        at the start of the potion game, followed by instructions from Snape. 
        '''
        print("\n--------You have entered professor Snape's potion class--------")
        time.sleep(1)
        print("\nSnape: Well, well, look who is late on their very first day"
              + "...")
        time.sleep(1)
        print("Snape: So as I was saying, we will be learning 3 types of potions"
              + " in this class")
        time.sleep(2)
        print("Snape: Pay attention as I explain the abilities of the potions as"
              + " it might come in handy soon...")
        time.sleep(1)
        print("\nSnape: Let's first take a look at the 'Wiggenweld Potion'...")
        print("Snape: This potion has the ability to grant you with an extra 10"
              + " HP in your battles.")
        time.sleep(2)
        print("\nSnape: Moving on to the 'Maxima Potion'...")
        print("Snape: This potion has the ability to grant you with an extra 5 "
              + "attack damage for 15 seconds.")
        time.sleep(2)
        print("\nSnape: Next, the 'Thunderbrew Potion'...")
        print("Snape: This potion will grant you the ability to strike your"
              + " enemy with 20 total attack damage.")
        time.sleep(2)
        print("\nSnape: Now, you guys would be making these potions for "
              + "yourselves,...")
        print("Snape: Look at the recipes and brew the ingredients needed to "
              + "make your potions.")
        time.sleep(2)
        print("\nSnape: With each time you successfully brew, you will brew 2 "
              + "of the same potion...")
        input("press enter to continue: ")
        while True: # Prints out main menu database for the potion game
            print("\n-------------OPTIONS-------------")
            print("1. Take ingredients from your table")
            print("2. Brew your ingredients")
            print("3. View Potions Inventory")
            print("4. Potions Recipe")
            print("5. Exit")
            choice = input("what do you intend to do?: ")
            try:    
                # Lets player see/get their things from the table
                if choice == '1':
                    self.things_on_table()
                # Lets player brew their ingredients
                elif choice == '2':
                    self.brew_potion()
                # Lets player check their inventory 
                elif choice == '3':
                    self.view_inventory()
                # Lets the player check the recipe book
                elif choice == '4':
                    self.view_recipe()
                # Lets player exit the class and updates player's potions
                elif choice == '5':
                    return self.player.inventory
                else: # If the player chooses something out of range
                    print("Snape: What are you trying to do there?")   
            except ValueError: # If the player did not type a number
                print("Snape: What are you trying to do there?")
                time.sleep(1)
