import time


class PotionGame:
    def __init__(self):
        self.ingredients = ['Horklump Juice', 'Dittany Leaves', 'Leech Juice', 'Spider Fang', 'Leech Juice', 'Stench of the Dead']
        self.potions = {
            'Wiggenweld Potion': ['Horklump Juice', 'Dittany Leaves'],
            'Maxima Potion': ['Leech Juice', 'Spider Fang'],
            'Thunderbrew Potion': ['Leech Juice', 'Stench of the Dead']
        }
        self.inventory = []
        self.potion_inventory = ['Wiggenweld Potion', 'Maxima Potion', 'Thunderbrew Potion']

    def things_on_table(self):
        global choice
        print("---------THINGS ON YOUR TABLE---------")
        i = 1
        for item in self.ingredients:
            print(f"{i}. {item}")
            i += 1
        try:
            choice = int(input("What do you want to grab to the brewing station?: "))
            if 1 <= choice <= len(self.ingredients):
                selected = self.ingredients[choice-1]
                self.inventory.append(selected)
                self.ingredients.pop(choice-1)
                return selected
            
        except ValueError:
            print("numbers only")
            return None
    
    def view_recipe(self):
        print("\n---------POTIONS RECIPE---------")
        for key, value in self.potions.items():
            print(f"- {key}: {value}")
        
    '''for testing purposes'''
    def view_inventory(self):
        i = 1
        for item in self.inventory:
            print(f"{i}. {item}")
            i += 1
    
    def brew_potion(self):
        brew = False
        for potion, required_items in self.potions.items():
                if all(item in self.inventory for item in required_items):
                        for item in required_items:
                            self.inventory.remove(item)
                            print("brewing...")
                            time.sleep(1)
                            print("brewing...")
                            time.sleep(1)
                            print("almost done!")
                            time.sleep(1)
                            print(f'you have brewed 2x {potion}')
                            time.sleep(2)
                            self.potion_inventory.append(potion)
                            self.potion_inventory.append(potion)
                            brew = True
        if not brew:
            print("you do not have enough inredients to brew any potions!")
            time.sleep(1)

    def potions_made(self):
        print("\n---------INVENTORY---------")
        i = 1
        for item in self.potion_inventory:
            print(f"{i}. {item}")
            i += 1

def start_potion_game():
    game = PotionGame()
    print("--------You have entered professor Snape's potion class--------")
    time.sleep(1)
    print("\nSnape: Well, well, look who is late on their very first day...")
    time.sleep(1)
    print("Snape: So as I was saying, we will be learning 3 types of potions in this class")
    time.sleep(2)
    print("Snape: Pay attention as I explain the abilities of the potions as it might come in handy soon...")
    time.sleep(1)
    print("\nSnape: Let's first take a look at the 'Wiggenweld Potion'...")
    print("Snape: This potion has the ability to grant you with an extra 20 HP in your battles.")
    time.sleep(2)
    print("\nSnape: Moving on to the 'Maxima Potion'...")
    print("Snape: This potion has the ability to grant you with an extra 10 attack damage for 20 seconds.")
    time.sleep(2)
    print("\nSnape: Next, the 'Thunderbrew Potion'...")
    print("Snape: This potion will grant you the ability to strike your enemy with 50 total attack damage.")
    time.sleep(2)
    print("\nSnape: Now, you guys would be making these potions for yourselves,...")
    print("Snape: Look at the recipes and brew the ingredients needed to make your potions.")
    input("press enter to continue: ")
    while True:
        print("\n-------------OPTIONS-------------")
        print("1. Take ingredients from your table")
        print("2. Brew your ingredients")
        print("3. View Potions Inventory")
        print("4. Potions Recipe")
        print("5. Exit")
        choice = input("what do you intend to do?: ")
        try:    
            if choice == '1':
                game.things_on_table()
            elif choice == '2':
                game.brew_potion()
            elif choice == '3':
                game.potions_made()
            elif choice == '4':
                game.view_recipe()
            elif choice == '5':
                return game.potions_made()  
        except ValueError:
            print("invalid choice!")
            time.sleep(1)

