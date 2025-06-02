
import character

spell_list = ['Sectumsempra',
          'Lumos',
          'Avada Kedavra',
          'Disillusionment',
          'Cruciatus', 
          'Expelliarmus',
]
'''
for item in spell_list:
    print(item)
choice = input("spell name: ")
'''
class Spell:

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
        if character.choice in spell_list:
            print(f"\nYou have casted {self.name}, which contributes {self.attack} damage")
        else:
            print(f"\nYou have casted an unknown spell, {self.name}, which contributes {self.attack} damage")
'''
Spell(character.choice).cast_spell()
Spell(character.choice)
'''



