import random
import wand
import spells
import score
import threading
import time


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
            print(f"{self.name}'s current health : {self.health}")



class Player(Character):
    
    def __init__(self, name): # have potion inventory be in here from start
        Character.__init__(self, name)
        self.wand_type = wand.Wand.get_wand()
        self.players_score = 0
        self.increase_attack = False
        self.increase_damage = False
        self.potion_inventory = []

        
    def movement(self):
        pass
        #movement.player.main_menu()
        

    def choose_potion(self):
        print("\n---------------Potion Inventory---------------")
        i = 1
        for item in self.potion_inventory:
            print(f"{i}. {item}")
            i += 1
        try:
            choice = int(input("What potion do you want to use?: "))
            if 1 <= choice <= len(self.potion_inventory):
                selected = self.potion_inventory.pop(choice-1)
                if selected == 'Wiggenweld Potion':
                    print(f'\nYou have used the Wiggenweld Potion!')
                    self.healing()
                elif selected == 'Maxima Potion':
                    print(f'\nYou have used the Maxima Potion!')
                    print(f'\nYour attacks will increase by 5 damage for the next 20 seconds!')
                    self.increase_attack = True
                    self.start_countdown(20)
                elif selected == 'Thunderbrew Potion':
                    print(f'\nYou have used the Thunderbrew Potion')
                    print(f'\nYour next attack will be increased by 20 damage!')
                    self.increase_damage = True
            else:
                print("invalid")
        except ValueError:
            print("numbers only")
            return None

    def healing(self):
        self.health += 20
        print('drinking...')
        time.sleep(1)
        print('+ 5 health!')
        print('drinking...')
        time.sleep(1)
        print('+ 5 health!')
        time.sleep(0.5)
        print("You have gain 20 HP!")


    def start_countdown(self, duration):
        thread = threading.Thread(target=self.countdown, args=(duration,), daemon=True)
        thread.start()

    '''still in major progress'''

    def countdown(self, t):
        while t:
            mins, secs = divmod(t, 60) 
            timer = '{:02d}:{:02d}'.format(mins, secs) 
            print(f"\r[Maxima Boost Time left: {timer}]  ", end=" ", flush=True) 
            time.sleep(1) 
            t -= 1
        if self.increase_attack:
            self.increase_attack = False
            print("Time's up!")


    def inflict_damage(self, enemy):
        global choice
        print("\nCasting a spell... 🪄✨")
        attack = random.randint(self.wand_type.min_power, self.wand_type.max_power)
        if self.increase_attack: 
            attack += 5
        if self.increase_damage:
            time.sleep(1)
            attack += 50
            print("⚡⚡ BAMMMM THUNDERSTRIKE ⚡⚡")
            self.increase_damage = False
        if self.health <= 50:
            print('Blimey, yeh not lookin too good on health! Quick! Think back to class — cast any one of the spell yeh remember to cause more damage!')
            i = 1
            for item in spells.Spell.spell_list:
                print(f"{i}. {item}")
                i += 1
            #self.timer_on = True
            #self.start_countdown(5)
            choice = input("spell name: ").title()
            spells.Spell(choice).cast_spell()
            spell_attack = spells.Spell(choice).attack  
            total_attack = attack + spell_attack
            print(f"{enemy.name} has taken a total of {total_attack} damage")
            enemy.take_damage(total_attack)
            return total_attack
        else:
            print(f"{enemy.name} has taken {attack} damage!")
            enemy.take_damage(attack)
            return attack
    
    def compare_scores(self):
        if self.players_score > int(score.high_score):
            score.newScore(str(self.players_score))

class Oponent(Character):
    
    def __init__(self, name):
        Character.__init__(self, name)
     
    def inflict_damage(self, user):
        print(f"\n{self.name} is casting a spell... 😈🪄")
        time.sleep(2)
        if self.name == 'Luna':
            attack = random.randint(5, 10)
        if self.name == 'Draco':
            attack = random.randint(10, 15)
        if self.name == 'Peter':
            attack = random.randint(15, 20)
        if self.name == 'Bellatrix':
            attack = random.randint(20, 30)
        if self.name == 'Voldemort':
            attack = random.randint(30, 35)
        print(f"You have taken {attack} damage!")
        user.take_damage(attack)
        return attack
               







