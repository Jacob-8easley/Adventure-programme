from item import Item


class Health(Item):
    def __init__(self, name, equipable=False, quantity=1, weight=None, health=None, equip_state=False):
        super().__init__(name, equipable, quantity, weight, equip_state)
        self.health = health
