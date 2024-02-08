
class CommandControl:

    def __init__(self):
        self.valid_commands = ["Help", "Move", "Search",
                               "Pickup", "Attack", "Equip", "Quit", "Exits"]

    def execute_command(self, command, callback=None):

        direction = ["N", "E", "S", "W"]
        if command[0] == "Help":
            print(f"Valid command are {self.valid_commands}")
            print("To move player type Move N,E,S or W")
        if command[0] == "Move":
            if len(command) <= 1:
                print(
                    "Please enter which direction you would like to move after the command.")

            elif command[1] in direction:
                callback(command[1])

            else:
                print(
                    f"The command needs to be in the list of valid cammands {self.valid_commands}")

        if command[0] == "Search":
            if len(command) <= 1:
                print(
                    "Specify whether you would like to search the room or your library.")

            elif command[1] not in ["Room", "Library"]:
                print(f"Can only search library or room")
            else:
                print(f"You search the {command[1]}")
                callback(command[1])

        if command[0] == "Pickup":
            if len(command) <= 1:
                print("please enter an item to pickup")
            else:
                callback(command[1])

        if command[0] == "Attack":
            callback()
        if command[0] == "Equip":
            if len(command) <= 1:
                print("please enter which weapon to equip")
            else:
                callback(command[1])

        if command[0] == "Eat":
            if len(command) <= 1:
                print("Please enter an item to eat")
            else:
                callback(command[1])

        if command[0] == "Exits":
            callback()

        if command[0] == "Quit":
            print(
                f"command entered was {command}.\n Thankyou for playing Dragon Slayers.")

        if command[0] not in self.valid_commands:
            print(f"please ensure input is from {self.valid_commands}.")
