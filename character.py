class Character:

    def __init__(self, name: str, wand: str, health: int):
        self.name = name
        self.wand = wand
        self.health = health
        self.max_health = health
        self.alive = True
    
    def __str__(self):
        return f""
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.alive = False
            print(f"-Hagrid saying youre dead-")
        else: 
            print(f"{self.name} took damage. Current health = {self.health}")
