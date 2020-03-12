
class Room():
    def __init__(self, name, description, n=None, s=None, e=None, w=None, items=[]):
        self.name = name
        self.description = description
        self.n = n
        self.s = s
        self.e = e
        self.w = w
        self.items = items

    def __str__(self):
        return f"{self.name}"

    def connectedRooms(self):
        return f"n: {self.n}, s: {self.s}, e: {self.e}, w: {self.w}"

    def displayItemList(self):
        if len(self.items) > 1:
            output = ', '.join(map(str, self.items))
            print(f"Items in this room: {output}")
        elif len(self.items) == 1:
            print(f"Items in this room: {self.items[0]}")
