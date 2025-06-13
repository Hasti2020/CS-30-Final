import random
import wand
import spells
import score
import threading
import time
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
            self.health = 0
        else:
            print(f"[{self.name}] current health : {self.health}")


class Player(Character):
   
    def __init__(self, name): # have potion inventory be in here from start
        Character.__init__(self, name)
        self.wand_type = wand.Wand.get_wand()
        self.players_score = 0
        self.maxima_increase = False
        self.thunderbrew_increase = False
        self.potion_inventory = ['Maxima Potion', 'Thunderbrew Potion']
        self.potion_game = potion.PotionGame(self)
        self.have_money = False
        self.have_wand = False
        self.have_book = False
        self.have_pet = False
        self.at_hogwarts = False
        self.sorted = False
        self.location = {'row': 0, 'col': 0}
        self.enter_potion_class = False
        self.enter_spell_class = False
             
           
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


    def start_countdown(self, length):
        '''
        In order for timer to not freeze the whole game, threading needs
        to be used to run the method sperately in the background in my
        game. Or else the game will wait for the timer to go out before
        the game continues on.
        '''
        thread = threading.Thread(target=self.countdown, args=(length,), daemon=True)
        # chooses my countdown method to be played in the background, 
        # and takes in my coutdown argument of 15s, letting my timer
        # to be played in the background without freezing the game
        # daemon will stop the threading once the game ends
        thread.start()


    def countdown(self, t):
        '''
        This is the method for the Maxima Potion's timer to
        be displayed on the console.
        '''
        while t: # while my time is counting down
            mins, secs = divmod(t, 60) 
            # takes my time argument and try doing the quotient division with 60
            # 15 fits in 60 0 times, so there is 0 minutes, and 15s is left
            timer = '{:02d}:{:02d}'.format(mins, secs)
            # if the number is only 1 digit, add a zero in front to make it 2 digits
            # and formats the timer into 00:15, with just whole numbers
            print(f"\r[Maxima Boost Time left: {timer}]  ", end=" ", flush=True)
            # prints the timer format, and let it keep printing at the same spot
            # and also immediately display it on the screen (end just adds a space)
            time.sleep(1)
            t -= 1 # time argument keeps counting down
        if self.maxima_increase:
            self.maxima_increase = False
            print("Time's up!")


    def inflict_damage(self, enemy):
        global spell_input
        print("\nCasting a spell... 🪄✨")
        #time.sleep(1.5)
        attack = random.randint(self.wand_type.min_power, self.wand_type.max_power)
        if self.maxima_increase:
            attack += 5
        if self.thunderbrew_increase:
            attack += 20
            print("⚡⚡ BAMMMM THUNDERSTRIKE ⚡⚡")
            self.thunderbrew_increase = False
        if self.health <= 40: # if the player health is less than 40, they cast a spell
            print('\nBlimey, cast any one of the spell yeh remember to cause more damage!')
            print('Type it CORRECTLLY!!')
            i = 1
            for item in spells.Spell.spell_list:
                print(f"{i}. {item}")
                i += 1
            try:
                print("Spell Name: ")
                spell_input = int(input("> ")) - 1
                if 0 <= spell_input < len(spells.Spell.spell_list):
                    spell_name = spells.Spell.spell_list[spell_input]
                    spell = spells.Spell(spell_name)
                    spell.cast_spell()
                else:
                    print("Invalid spell number, defaulting to unknown spell")
                    spell_attack = 0
                spell_attack = spell.attack
                total_attack = attack + spell_attack
                print(f"{enemy.name} has taken a total of {total_attack} damage")
                enemy.take_damage(total_attack)
                return total_attack
            except ValueError:
                print("\nYou have casted an unknown spell which contributes 0 damage")
                spell_attack = 0
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
        #time.sleep(2)
        if self.name == 'Luna':
            attack = random.randint(5, 10)
        if self.name == 'Draco':
            attack = random.randint(10, 15)
        if self.name == 'Peter':
            attack = random.randint(15, 20)
        if self.name == 'Bellatrix':
            attack = random.randint(20, 25)
        if self.name == 'Voldemort':
            attack = random.randint(25, 30)
        print(f"You have taken {attack} damage!")
        user.take_damage(attack)
        return attack
               

















