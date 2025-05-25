import random

class Wand:

    def __init__(self, name: str, core: str, max_power: int, min_power: int):
        self.name = name
        self.core = core
        self.max_power = max_power
        self.min_power = min_power

    def __str__(self):
        return f"{self.name}"
    
    def cast_spell(self):
        return random.randint(self.min_power, self.max_power)
    
wand_options = [Wand("Duststick", "Rabbit Fur", 0, 10),
                Wand("Ashlight", "Unicorn Hair", 5, 15),
                Wand("Dragonshade", "Dragon Heartstring", 10, 20),
                Wand("Phoenixbane", "Phoenix Feather", 15, 25),
                Wand("Elder Echo", "Basilisk Horn", 20, 30)]