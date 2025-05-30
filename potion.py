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

    def things_on_table(self):
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

    def test(self):
        print(self.ingredients)
        print(self.inventory)
        
game = PotionGame()
while True:        
    test = input("q or w: ")
    if test == 'q':
        print(game.things_on_table()) 
    elif test == 'w':
        print(game.test())
      

