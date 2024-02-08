class Room:
    def __init__(self,name,item=None,enemy=None):
        self.name = name
        self.exits = {}
        self.item = item
        self.enemy = enemy
        
    def get_exits(self):
        return list(self.exits.keys())
    
    def set_exits(self,direction,name):
        self.exits[direction] = name
        return self.exits[direction]

    def remove_item(self):
        item_to_remove = self.item
        self.item = None
        return item_to_remove