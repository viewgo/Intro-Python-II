class Room():
    def __init__(self, name, description, n=None, s=None, e=None, w=None):
        self.name = name
        self.description = description
        self.n = n
        self.s = s
        self.e = e
        self.w = w

    def __str__(self):
        return f"{self.name}"

    def connectedRooms(self):
        return f"n: {self.n}, s: {self.s}, e: {self.e}, w: {self.w}"

    
