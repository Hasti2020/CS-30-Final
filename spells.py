
import character
import time
'''
for item in spell_list:
    print(item)
choice = input("spell name: ")
'''
class Spell:
    spell_list = ['Sectumsempra',
          'Lumos',
          'Avada Kedavra',
          'Disillusionment',
          'Cruciatus', 
          'Expelliarmus']
    
    def __init__(self, name):
        self.name = name
        self.attack = self.spell_power()

    def __str__(self):
        return f"{self.name}"
    
    def spell_power(self):
        if self.name == 'Sectumsempra':
            return 25
        if self.name == 'Lumos':
            return 1
        if self.name == 'Avada Kedavra':
            return 20
        if self.name == 'Disillusionment':
            return 5
        if self.name == 'Cruciatus':
            return 10
        if self.name == 'Expelliarmus':
            return 15
        if self.name == 'Stupefy':
            return 10
        else:
            return 0
        
    def cast_spell(self):
        if character.choice in Spell.spell_list:
            print(f"\nYou have casted {self.name}, which contributes {self.attack} damage")
        else:
            print(f"\nYou have casted an unknown spell, {self.name}, which contributes {self.attack} damage")

def spell_lesson():
    print("--------You have entered professor Flitwick's spells lessons--------")
    time.sleep(1)
    print("Flitwick: Hello students, today we will be learning about the most famous spells in the wizzarding world! ✨✨" )
    time.sleep(1)
    print("Flitwick: Need a bit of light? Lumos ✨! A flick of the wand, and voilà — a glowing tip to guide your way in the dark!")
    print("Flitwick: It can only create 1 DMG in a battle though...")
    time.sleep(2)
    print("Flitwick: Become nearly invisible! Disillusionment Charm ✨! Excellent for sneaking — just don’t trip over your own feet!")
    print("Flitwick: Only 5 DMG tho...")
    time.sleep(2)
    print("Flitwick: Dark magic... Sectumsempra ✨ causes deep, slashing wounds. Use it only if you must — and be prepared for the consequences")
    print("Flitwick: This dangerous spell can cause a massive 25 DMG...")
    time.sleep(2)
    print("Flitwick: The Cruciatus.It causes unbearable pain. Unforgivable. Illegal. And deeply disturbing. This is not a spell to take lightly")
    print("Flitwick: This spell can cause 10 DMG...")
    time.sleep(2)
    print("Flitwick: The Killing Curse. Avada Kedavra. This spell is pure evil — never to be used")
    print("Flitwick: This spell can cause 20 DMG...")
    time.sleep(2)
    print("You: Ugh, this is too boring, I will sneak out now")
    time.sleep(2)
    ...
    time.sleep(1)
    ...
    time.sleep(1)

'''
Spell(character.choice).cast_spell()
Spell(character.choice)
'''




