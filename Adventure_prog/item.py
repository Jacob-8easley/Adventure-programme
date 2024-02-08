
class Item:
    
    def __init__(self,name, equipable=False,quantity=1,weight=None, equip_state=False):
        self.name = name
        self.quantity = quantity
        self.weight = weight
        self.equipable = equipable
        self.equip_state = equip_state
        
    def set_equiped(self):
        self.equip_state = True
        return self.equip_state
    
    def set_unequipped(self):
        self.equip_state = False
        return self.equip_state