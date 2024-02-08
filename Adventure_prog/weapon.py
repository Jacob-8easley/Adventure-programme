from item import Item

class Weapon(Item):
    def __init__(self, name, equipable=False, quantity=1, weight=None, power=None, equip_state=False):
        super().__init__(name, equipable, quantity, weight, equip_state)
        self.power = power
    
        
    