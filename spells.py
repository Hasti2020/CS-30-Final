
import character2
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
            return 0
        if self.name == 'Avada Kedavra':
            return 20
        if self.name == 'Disillusionment':
            return 5
        if self.name == 'Cruciatus':
            return 10
        if self.name == 'Expelliarmus':
            return 15
        else:
            print("This is not a spell")
    
    def cast_spell(self):
        print(f"You have casted {self.name}, which has an attack damage of {self.attack}")
'''
Spell(character.choice).cast_spell()
Spell(character.choice)
'''


