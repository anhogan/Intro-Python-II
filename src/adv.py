import code

from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [("Sword", "A pointy object")]),

    'foyer':    Room("Foyer", 
                    "Dim light filters in from the south. Dusty passages run north and east.",
                    [("Egg", "Don't drop it!")]),

    'overlook': Room("Grand Overlook", 
                    "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.",
                    [("Phone", "Find the password, find the help")]),

    'narrow':   Room("Narrow Passage", 
                    "The narrow passage bends here from west to north. The smell of gold permeates the air.",
                    [("Water Bottle", "Hydration is a necessary evil")]),

    'treasure': Room("Treasure Chamber", 
                    "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.",
                    [("Key", "What could this be for?")]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# If item doesn't exist return an error
# If verb doesn't match an action, return an error (list, like directions > get, take, or drop)
# Get / take > look in current room to see if item is available, if yes, add to player's item list and remove from Room list ... if not, print error
directions = ['n', 's', 'e', 'w']
item_actions = ['get', 'take', 'drop']

p = Player("Amanda", room['outside'])

print(f'Welcome {p.name}!\nExplore the map by moving North(n), South(s), East(e), or West(w)\nTo exit the game, enter q\n')
print(f'You are in the {p.current_room.name} - {p.current_room.description}\n')
print(f'{p.current_room.print_items()}')

while True:
    selection = input('Where to? ').lower().split(' ')

    if len(selection) > 2 or len(selection) < 1:
        print("Please enter a one or two word input for the game. To get a list of valid commands, type 'help' or 'h")
    elif len(selection) == 2:
        if selection[0] in item_actions:
            print('Success')
        else: 
            print("Please enter a valid action for the item. To get a list of valid commands, type 'help' or 'h")
    else:
        if selection[0] == 'q' or selection[0] == 'quit':
            print(f'Thanks for playing {p.name}!') 
            break

        if selection[0] == 'h' or selection[0] == 'help':
            print("Valid game commands:\n'n' - Move North\n's' - Move South\n'e' - Move East\n'w' - Move West\n'i' or 'inventory' - Get a list of your current items\n'get' or 'take' - Pick up an item\n'drop' - Drop an item\n'q' or 'quit' - Exit Game\n")
            continue

        if selection[0] == 'i' or selection[0] == 'inventory':
            p.print_items()
            continue

        if selection[0] in directions:
            try:
                p.move_room(selection[0])
                print(f'You are in the {p.current_room.name} - {p.current_room.description}\n')
                print(f'{p.current_room.print_items()}')
            except AttributeError:
                print('No room there, try another direction')
        else:
            print('Movement not allowed! Please enter a direction (n, s, e, w) to move around the map')