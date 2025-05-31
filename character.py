import random
import wand
import spells
import score
import potion

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
    
    def __init__(self, name, potions = None):
        Character.__init__(self, name)
        self.wand_type = wand.Wand.get_wand()
        self.players_score = 0
        if potions:
            self.potion_inventory = potions
        else:
            self.potion_inventory = []
        

    def movement(self):
        pass
        #movement.player.main_menu()

    def heal(self, user):
        for item in self.potions:
            if item == 'Wiggenweld Potion':
                user.health += 20
                print('You have regained 20 health!')

    def inventory(self):
        i = 1
        for item in self.potion_inventory:
            print(f"{i}. {item}")
            i += 1
        try:
            choice = int(input("What potion do you want to use?: "))
            if 1 <= choice <= len(self.potion_inventory):
                selected = self.potion_inventory[choice-1]
                self.potion_inventory.pop(choice-1)
                return selected
            
        except ValueError:
            print("numbers only")
            return None




    def inflict_damage(self, enemy):
        global choice
        print("\nCasting a spell...")
        attack = random.randint(self.wand_type.min_power, self.wand_type.max_power)
        if self.health <= 60:
            print('Blimey, yeh not lookin too good on health! Quick! Think back to class — cast any spell yeh remember to cause more damage!')
            choice = input("spell name: ").title()
            spells.Spell(choice).cast_spell()
            spell_attack = spells.Spell(choice).attack    
            total_attack = attack + spell_attack
            print(f"{enemy.name} has taken a total of {total_attack} damage")
            enemy.take_damage(total_attack)
            return total_attack
        else:
            print(f"{enemy.name} has taken {attack} damage")
            enemy.take_damage(attack)
            return attack
    
    def compare_scores(self):
        if self.players_score > int(score.high_score):
            score.newScore(str(self.players_score))

class Oponent(Character):
    
    def __init__(self, name):
        Character.__init__(self, name)
     
    def inflict_damage(self, user):
        print(f"\n{self.name} is casting a spell...")
        if self.name == 'Luna':
            attack = random.randint(0, 5)
        if self.name == 'Draco':
            attack = random.randint(5, 10)
        if self.name == 'Peter':
            attack = random.randint(10, 15)
        if self.name == 'Bellatrix':
            attack = random.randint(10, 20)
        if self.name == 'Voldemort':
            attack = random.randint(15, 20)
        print(f"you have taken {attack} damage")
        user.take_damage(attack)
        return attack
               











