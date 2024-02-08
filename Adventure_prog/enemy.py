import random

class Enemy:
    def __init__ (self, name, health=None, attack=None, dead=False):
        self.name = name
        self.health = health 
        self.attack = attack 
        self.dead = dead
         
    def get_attack_value(self):
        return -(self.attack + random.randint(0,5))
    
    def get_health(self):
        return self.health
    
    def update_health(self,health_value):
        self.health += health_value
        return self.health
        
    def get_name(self):
        return self.name