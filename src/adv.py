import code

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

# Make a new player object that is currently in the 'outside' room.
p = Player("Zelda", "outside")
print(p)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Need validation for if direction is available, if not throw an error
# If invalid input, throw an error
# Update p.current_room each time
# Return a string with current room name and description
n = f'The current room is {room[p.current_room].n_to.name} - {room[p.current_room].n_to.description}'
s = f'Moved South to {room[p.current_room].s_to.name} - {room[p.current_room].s_to.description}'
e = f'Moved East to {room[p.current_room].e_to.name} - {room[p.current_room].e_to.description}'
w = f'Moved West to {room[p.current_room].w_to.name} - {room[p.current_room].w_to.description}'
q = f'Thanks for playing!'

def adventure_repl():
    room_description = room[p.current_room].description
    banner = f'The current room is {p.current_room} - {room_description}\nExplore the map by moving North(n), South(s), East(e), or West(w)\nTo exit the game, enter q'
    code.interact(banner=banner, local=globals(), exitmsg='Thanks for playing!')

adventure_repl()
# move_rooms()