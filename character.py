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
        else: 
            print(f"{self.name}, current health : {self.health}")

class Player(Character):
    
    def __init__(self, name):
        Character.__init__(self, name)
        self.wand_type = wand.Wand.get_wand()

    def movement(self):
        pass

    def inflict_damage(self, enemy):
        print("\nCasting a spell...")
        attack = random.randint(self.wand_type.min_power, self.wand_type.max_power)
        print(f"{enemy.name} has taken {attack} damage")
        enemy.take_damage(attack)

        
       
class Oponent(Character):
    
    def __init__(self, name):
        Character.__init__(self, name)
     
    def inflict_damage(self, user):
        print(f"{self.name} is casting a spell...")
        if self.name == 'Luna':
            attack = random.randint(0, 5)
        if self.name == 'Draco':
            attack = random.randint(5, 10)
        if self.name == 'Peter':
            attack = random.randint(15, 25)
        if self.name == 'Bellatrix':
            attack = random.randint(20, 30)
        if self.name == 'Voldemort':
            attack = random.randint(30, 40)
        print(f"you have taken {attack} damage")
        user.take_damage(attack)

               









