
from command_parse import CommandControl
from player import Player
from room import Room
from item import Item
from enemy import Enemy
from weapon import Weapon
from health import Health


class Game:
    def __init__(self):
        self.player = Player()
        village = Room(name="village")
        castle = Room(name="castle")
        tower = Room(name="tower")
        bridge = Room(name="Bridge")
        blacksmith = Room(name="Blacksmith")
        forest = Room(name="Forest")
        self.gate = Room(name="Gate")
        swamp = Room(name="Swamp")

        village.set_exits("N", castle)
        village.set_exits("S", tower)
        village.set_exits("E", bridge)
        village.set_exits("W", blacksmith)
        castle.set_exits("S", village)
        tower.set_exits("N", village)
        tower.set_exits("W", swamp)
        bridge.set_exits("W", village)
        blacksmith.set_exits("E", village)
        self.gate.set_exits("S", forest)
        forest.set_exits("N", self.gate)
        castle.set_exits("W", forest)
        forest.set_exits("E", castle)
        swamp.set_exits("E", tower)

        boots = Item("Boots", equipable=True, weight=10)
        key = Item("Key", equipable=True, weight=3)
        ring = Weapon("Ring", equipable=True, weight=2, power=10)
        lock = Item("Lock")
        sword = Weapon("Sword", equipable=True, weight=25, power=5,)
        mushroom = Health("Mushroom", equipable=True,
                          quantity=1, weight=2, health=5)

        village.item = mushroom
        castle.item = key
        tower.item = ring
        self.gate.item = lock
        bridge.item = mushroom
        blacksmith.item = sword
        forest.item = mushroom
        swamp.item = mushroom

        bridge.enemy = Enemy("Troll", health=15, attack=1)
        forest.enemy = Enemy("Bear", health=25, attack=3)
        tower.enemy = Enemy("Skeleton", health=5, attack=1)
        self.gate.enemy = Enemy("Dragon", health=50, attack=5)

        self.current_room = village

        self.commands = CommandControl()

    def move_handler(self, move):
        if move not in self.current_room.exits:
            print(
                f"\nThis is not a valid exit the exits are {list(self.current_room.exits.keys())}.")
        else:
            self.current_room = self.current_room.exits[move]
            if self.current_room.enemy != None:
                print(
                    f"\nYou have come across {self.current_room.enemy.name}.")

    def search_handler(self, search):
        if search == "Room":
            if self.current_room.enemy:
                print(
                    f"\nThis {self.current_room.enemy.name} needs to be dealt with first before room can be searched.")
            elif self.current_room.item:
                print(f"you find {self.current_room.item.name}")
            else:
                print(f"{self.current_room.name} is empty")

        elif search == "Library":
            if len(self.player.library) == 0:
                print("library is empty")
            else:
                print(list(self.player.library.keys()))

    def pickup_handler(self, pickup):
        if pickup != self.current_room.item.name:
            print(f"{pickup} does not exist here")
        elif not self.current_room.item.equipable:
            print(f"cant pickup the {pickup}")
        else:
            library_item = self.current_room.remove_item()
            self.player.add_to_library(library_item)

    def ai_attack_handler(self):
        damage = self.current_room.enemy.get_attack_value()
        self.player.update_health(damage)
        if self.player.health < 0:
            print("You're Dead")
        else:
            print("You are being attacked\n")

    def attack_handler(self):

        if self.current_room.enemy == None:
            print("There are no enemies to attack")
        else:
            print(f"enemy Health: {self.current_room.enemy.get_health()}")
            attack_value = self.player.attack()
            if attack_value == 0:
                print("You don't have a weapon equiped")
            else:
                self.current_room.enemy.update_health(attack_value)
                print(
                    f"Attacking with {self.player.get_weapon()},\
                        You dealt {attack_value} damage to enemy.",
                    "\nEnemy Health: ", self.current_room.enemy.get_health()
                )
                if self.current_room.enemy.get_health() < 1:
                    print("You have defeated your foe congratulations")
                    self.current_room.enemy = None

                elif self.current_room.enemy.get_health() > 0:
                    print(
                        f"No time for resting yet\n{self.current_room.enemy.get_name()} is still attacking.")

    def equip_weapon(self, weapon):
        self.player.equip_weapon(weapon)
        if not self.player.weapon:
            print(f"No weapon {weapon}")
        else:
            print(
                f"You set {self.player.weapon.name} as weapon its attack power is {self.player.weapon.power}.")

    def eat_food(self, health):
        self.player.eat_food(health)
        if not self.player.food:
            print(f"No Food {health} to eat")
        else:
            print(
                f"You eat {health} and increase your health from {self.player.health} to {self.player.health + self.player.food.health}")

    def print_exits(self):
        print(self.current_room.get_exits())

    def check_game_ended(self):
        if self.player.health < 1:
            return False
        if not self.gate.enemy:
            print("You have beaten the dragon!")
            return False
        return True

    def play(self):
        not_complete = True
        name = "Janice"
        print(
            f"welcome to slay the dragon!\n\nGI {name} wakes up to her family gone with note left on the table in the side of her house.\n\n")
        print(
            f"The note reads '{name} help the realm is in danger, please explore and find out what you can to defeat the trecherous Elder Dragon!\n\n")
        print(f"{name} get up and prepare to head out on there adventure.\n\nType help to see a list of available commands.\n\n")

        while not_complete:
            not_complete = self.check_game_ended()
            print("\nMy inventory:", list(self.player.library.keys()), "\n")
            print("My health:", self.player.health, "\n")

            user_input = input(f"You are in {self.current_room.name}\n>>>")
            user_input = user_input.title()
            command = user_input.split(" ")

            if command[0] == "Move":
                self.commands.execute_command(command, self.move_handler)
            elif command[0] == "Search":
                self.commands.execute_command(command, self.search_handler)
            elif command[0] == "Pickup":
                self.commands.execute_command(command, self.pickup_handler)
            elif command[0] == "Attack":
                self.commands.execute_command(command, self.attack_handler)
            elif command[0] == "Equip":
                self.commands.execute_command(command, self.equip_weapon)
            elif command[0] == "Eat":
                self.commands.execute_command(command, self.eat_food)
            elif command[0] == "Help":
                self.commands.execute_command(command)
            elif command[0] == "Exits":
                self.commands.execute_command(command, self.print_exits)
            else:
                self.commands.execute_command(command)

            if self.current_room.enemy != None:
                self.ai_attack_handler()
            not_complete = self.check_game_ended()

            if command[0] == "Quit":
                self.commands.execute_command(command)
                not_complete = False
