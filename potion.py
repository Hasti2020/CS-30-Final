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
        self.potion_inventory = []

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
        
    '''for testing purposes'''
    def view_inventory(self):
        i = 1
        for item in self.inventory:
            print(f"{i}. {item}")
            i += 1
    
    def brew_potion(self):
        brew = False
        print("brewing...")
        time.sleep(1)
        print("brewing...")
        time.sleep(1)
        print("almost done!")
        time.sleep(1)
        for potion, required_items in self.potions.items():
                if all(item in self.inventory for item in required_items):
                        for item in required_items:
                            self.inventory.remove(item)
                        print(f'you have brewed {potion}')
                        self.potion_inventory.append(potion)
                        brew = True
        if not brew:
            print("you do not have enough inredients to brew any potions!")

    def potions_made(self):
        return self.potion_inventory
 

def start_potion_game():
    game = PotionGame()
    print("welcome to the potion making game!")
    while True:     
        test = input("q or w: ")
        if test == 'q':
            game.things_on_table() 
        elif test == 'w':
            game.view_inventory()
        elif test == 'e':
            game.brew_potion()
        elif test == 'p':
            print(game.potions_made())
        elif test == 't':
            return game.potions_made()  

