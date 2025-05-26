import random
import wand 
class Character:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.alive = True
    
    def __str__(self):
        return f"{self.name}"
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.alive = False
            print(f"-Hagrid saying youre dead-")
        else: 
            print(f"{self.name} took damage. Current health = {self.health}")

class Player(Character):
    
    def __init__(self, name, wand_type):
        super.__init__(name)
        self.wand_type = wand.Wand(min_power, max_power)
        
    def inflict_damage(self, hero):
        print("Casting a spell...")
        attack = wand.cast_spell(self)
        print(f"the enemy has taken {attack} damage")
        enemy.take_damage(attack)
        
       
class Oponent(Player):
    
    def __init__(self, name):
        super.__init__(name)
     
    def inflict_damage(self, enemy):
        if oponent == 'Luna':
            attack = random.randint(0, 10)
        elif oponent == 'Draco':
            attack == random.randint(10, 20)
        elif oponent == 'Peter':
        
    
 
oponent_list = ['Draco', 'Luna', 'Peter', 'Bellatrix', 'Cedric']
oponent = random.randint(oponent_list)
                








