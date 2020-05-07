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
# print(cam.current_room)
# print(f'Player {cam.name} is in {cam.current_room.name}')
# cam.change_room(cam.current_room.n_to)
# print(cam.current_room)
# print(f'Player {cam.name} is in {cam.current_room.name}')
# cam.change_room(cam.current_room.e_to)
# print(cam.current_room)
# print(f'Player {cam.name} is in {cam.current_room.name}')


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

def intro():
    print('\nHello brave warrior, welcome to the game...\n')
    print('\nEnter [n] to travel north, [s] for south, [e] for east, [w] for west and [q] if you wish to end the game\n')

def start():
    global name
    name = input('\nWhat is your name?: \n')
    print(f'\n{name}... travel at your own risk...HAHAHAHAHA! \n')
    
    return name


name = ''
intro()
start()
player = Player(name, room['outside'])

while True:
    print(
        f'\nPlayer {player.name} is in the {player.current_room.name}. {player.current_room.description}\n')
    selection = input('\nWhich direction will you travel? [n] [s] [e] [w] [q]: \n')
    if selection == 'q':
        print("Quitting...")
        break

    try:
        if selection == 'n':
            if player.current_room.name == 'Grand Overlook':
                selection = input(
                    '\nYou fell off the cliff silly! If you stay here, you are sure to succumb to your wounds...climb back up? (y/n):\n')
                if selection == 'y':
                    continue
                else:
                    break
            elif player.current_room.name == 'Treasure Chamber':
                selection = input(
                    '\nYou stubbed your toe on the treasure chest silly! It hurts but you can still walk, will you continue? (y/n):\n')
                if selection == 'y':
                    continue
                else:
                    break
            else:
                player.change_room(player.current_room.n_to)
        elif selection == 's':
            if player.current_room.name == 'Outside Cave Entrance':
                selection = input(
                    '\nThe cave is to the north! Are you trying to go home already? (y/n):\n')
                if selection == 'y':
                    break
                else:
                    continue
            else:
                player.change_room(player.current_room.s_to)
        elif selection == 'e':
            if player.current_room.name == 'Outside Cave Entrance':
                selection = input(
                    '\nThe cave is to the north! Are you trying to go home already? (y/n):\n')
                if selection == 'y':
                    break
                else:
                    continue
            elif player.current_room.name == 'Narrow Passage' or player.current_room.name == 'Treasure Chamber' or player.current_room.name == 'Grand Overlook':
                selection = input(
                    '\nYou ran into a wall! Your nose is bleeding but you can still continue, will you? (y/n):\n')
                if selection == 'y':
                    continue
                else:
                    break
            else:
                player.change_room(player.current_room.e_to)
        elif selection == 'w':
            if player.current_room.name == 'Outside Cave Entrance':
                selection = input(
                    '\nThe cave is to the north! Are you trying to go home already? (y/n):\n')
                if selection == 'y':
                    break
                else:
                    continue
            elif player.current_room.name == 'Narrow Passage' or player.current_room.name == 'Treasure Chamber' or player.current_room.name == 'Foyer' or player.current_room.name == 'Grand Overlook':
                selection = input(
                    '\nYou ran into a wall! Your nose is bleeding but you can still continue, will you? (y/n):\n')
                if selection == 'y':
                    continue
                else:
                    break
            else:
                player.change_room(player.current_room.w_to)
        else:
            print('Your only choices are [n] [s] [e] [w] [q]')
    except AttributeError:
        print('Oh no')
