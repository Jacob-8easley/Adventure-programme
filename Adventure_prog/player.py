from health import Health
from weapon import Weapon


class Player:
    def __init__(self):
        self.health = 100
        self.library = {}
        self.weapon = None
        self.food = None

    def update_health(self, health_value):
        self.health += health_value
        return self.health

    def attack(self):
        if not self.weapon:
            print("You have no weapon! run away and find one!")
            return 0
        return -self.weapon.power

    def get_weapon(self):
        if not self.weapon:
            print("No weapon equipped")
            return
        return self.weapon.name

    def add_to_library(self, item):
        self.library[item.name] = item
        return item

    def remove_from_library(self, name):
        self.library = {piece: self.library[piece]
                        for piece in self.library if piece != name}

    def equip_weapon(self, name):
        if name not in self.library.keys():
            print("Weapon not in library")
            return
        if not isinstance(self.library[name], Weapon):
            print("Item must be a weapon")
            return
        if self.weapon:
            self.add_to_library(self.weapon)
        self.weapon = self.library[name]
        self.remove_from_library(name)
        return self.weapon.name

    def eat_food(self, name):
        if name not in self.library.keys():
            print("Item not on library")
            return
        if not isinstance(self.library[name], Health):
            print("Item must be a health bonus")
        else:
            self.health += self.library[name].health
            return
        self.remove_from_library(name)
        return self.health
