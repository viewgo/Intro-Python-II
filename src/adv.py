from room import Room
from player import Player
from item import Item
import os

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

room['outside'].items = [
    Item("Key", "It's a key"), Item("Rock", "It's a rock")]
room['foyer'].items = [Item("Gold", "A bag of 100 gold pieces")]

print(room['outside'].items)


movement_options = ["n", "s", "e", "w", "i", "inventory", "q"]
action_options = ["take", "drop"]


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def displayMessages():
    print(f"Location: {player.currentRoom.name}")
    print(f"{player.currentRoom.description}")
    player.currentRoom.displayItemList()


def getUserChoice():

    return input(
        "\nMove in a cardinal direction. Enter `q` to quit.\nEnter your movement: ")


def gameActions(input):
    # what kind of action (split string)
    split = input.split(" ")

    # if it's two words => action
    if len(split) == 2:
        action = split[0]
        item = split[1].capitalize()

        if action == action_options[0]:  # take
            foundItem = False
            for i in player.currentRoom.items:
                if i.name == item:
                    player.getItem(i)
                    player.currentRoom.removeItem(i)
                    foundItem = True
            if foundItem == False:
                clear()
                print(f"There's no {item} here.\n")

        elif action == action_options[1]:
            foundItem = False
            for i in player.inventory:
                if i.name == item:
                    player.dropItem(i)
                    player.currentRoom.addItem(i)
                    foundItem = True
            if foundItem == False:
                clear()
                print(f"There's no {item} in your inventory.\n")

        else:
            clear()
            print("Invalid choice!\n")

    elif len(split) == 1:
        if input in movement_options:
            player.move(input)
        else:
            clear()
            print("Invalid choice!\n")

    else:
        clear()
        print("Invalid choice!\n")


def quit():
    exit()


# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

# Start of Game
clear()
displayMessages()

# First user choice
user_choice = getUserChoice()

# Game loop
while user_choice != "q":
    gameActions(user_choice)
    displayMessages()
    user_choice = getUserChoice()
    clear()


# Quit if loop exits
quit()
