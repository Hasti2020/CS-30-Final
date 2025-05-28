
spells = ['Alohomora',
          'Lumos',
          'Avada Kedavra',
          'Disillusionment',
          'Cruciatus', 
]

for item in spells:
    print(item)
choice = input("spell name: ")

class Spell:

    def __init__(self, name):
        self.name = name
        self.attack = self.spell_power()

    def __str__(self):
        return f"{self.name}"
    
    def spell_power(self):
        if self.name == 'Lumos':
            return 5
    
    def cast_spell(self):
        print(f"You have casted {self.name}, which has an attack damage of {self.attack}")

Spell(choice).cast_spell()


