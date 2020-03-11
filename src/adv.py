from room import Room
from player import Player

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together
room['outside'].n = room['foyer']
room['foyer'].s = room['outside']
room['foyer'].n = room['overlook']
room['foyer'].e = room['narrow']
room['overlook'].s = room['foyer']
room['narrow'].w = room['foyer']
room['narrow'].n = room['treasure']
room['treasure'].s = room['narrow']


choice_options = ["n", "s", "e", "w", "q"]


def displayMessages():
    print("\n-------------------------------")
    print(f"Location: {player.currentRoom.name}")
    print(f"{player.currentRoom.description}")
    print(player.currentRoom.connectedRooms())


def getUserChoice():
    choice = input(
        "\nMove in a cardinal direction. Enter `q` to quit.\nEnter your movement: ")
    if choice in choice_options:
        return choice
    else:
        print("\nInvalid choice!")
        return


def changeRoom(newRoom):
    if newRoom == 'n' and player.currentRoom.n != None:
        player.currentRoom = player.currentRoom.n
    elif newRoom == 's' and player.currentRoom.s != None:
        player.currentRoom = player.currentRoom.s
    elif newRoom == 'e' and player.currentRoom.e != None:
        player.currentRoom = player.currentRoom.e
    elif newRoom == 'w' and player.currentRoom.w != None:
        player.currentRoom = player.currentRoom.w
    else:
        print("\nInvalid choice!")
        return


def quit():
    exit()


# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

# Start of Game
displayMessages()

# First user choice
user_choice = getUserChoice()

# Game loop
while user_choice != "q":
    changeRoom(user_choice)
    displayMessages()
    user_choice = getUserChoice()

# Quit if loop exits
quit()
