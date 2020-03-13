import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class Player:
    def __init__(self, currentRoom, inventory=[]):
        self.currentRoom = currentRoom
        self.inventory = inventory

    def move(self, cmd):
        if cmd == 'n' and self.currentRoom.n != None:
            self.currentRoom = self.currentRoom.n
        elif cmd == 's' and self.currentRoom.s != None:
            self.currentRoom = self.currentRoom.s
        elif cmd == 'e' and self.currentRoom.e != None:
            self.currentRoom = self.currentRoom.e
        elif cmd == 'w' and self.currentRoom.w != None:
            self.currentRoom = self.currentRoom.w
        elif cmd == 'inventory' or cmd == 'i':
            self.displayInventory()
        else:
            clear()
            print("Invalid choice!\n")
            return

    def displayInventory(self):
        clear()
        if len(self.inventory) <= 0:
            print("You have nothing in your inventory\n")
        else:
            output = ', '.join(map(str, self.inventory))
            print(f"Inventory: {output}\n")

    def getItem(self, item):
        self.inventory.append(item)

    def dropItem(self, item):
        self.inventory.remove(item)
