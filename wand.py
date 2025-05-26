import random

class Wand:

    def __init__(self, name: str, core: str, min_power: int, max_power: int):
        self.name = name
        self.core = core
        self.max_power = max_power
        self.min_power = min_power

    def __str__(self):
        return f"{self.name}"
    '''
    def cast_spell(self):
        return random.randint(self.min_power, self.max_power)
    '''
    def get_wand():
        random_wand = random.choice(wand_options)
        #print(f"The wand has spoken... You have been chosen by {random_wand}!")
       #print(f"Your wand has a {random_wand.core};  and casts spells with power between {random_wand.min_power} and {random_wand.max_power}.")
        return random_wand
        
wand_options = [Wand("Duststick", "Rabbit Fur", 0, 10),
                Wand("Ashlight", "Unicorn Hair", 5, 15),
                Wand("Dragonshade", "Dragon Heartstring", 10, 20),
                Wand("Phoenixbane", "Phoenix Feather", 15, 25),
                Wand("Elder Echo", "Basilisk Horn", 20, 30)]


Wand.get_wand()


