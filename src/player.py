class Player:
    def __init__(self, currentRoom, inventory=[]):
        self.currentRoom = currentRoom
        self.inventory = inventory

    def move(self, newRoom):
        if newRoom == 'n' and self.currentRoom.n != None:
            self.currentRoom = self.currentRoom.n
        elif newRoom == 's' and self.currentRoom.s != None:
            self.currentRoom = self.currentRoom.s
        elif newRoom == 'e' and self.currentRoom.e != None:
            self.currentRoom = self.currentRoom.e
        elif newRoom == 'w' and self.currentRoom.w != None:
            self.currentRoom = self.currentRoom.w
        else:
            print("\nInvalid choice!")
        return
