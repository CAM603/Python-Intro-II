from room import Room
from player import Player
from item import Sword, Valuable

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
chamber! There is a large treasure chest towards the north..."""),
}

# Declare items
item = {
    'gladius': Sword("Gladius", "The sword is short, featuring a thick and wide blade."),
    'needle': Sword("Needle", "The sword is small, like a needle, but the blade is strong. Best for turning enemies into swiss cheese."),
    'gold': Valuable("Gold", "A large golden nugget, this is what everyone has been risking their lives for!")
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

# Add items to room
room['foyer'].add_item(item['gladius'])
room['foyer'].add_item(item['needle'])
room['treasure'].add_item(item['gold'])

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
    print('\nEnter [n] to travel north, [s] for south, [e] for east, [w] for west, [l] to look around, [i] to see your items and [q] if you wish to end the game\n')

def start():
    global name
    name = input('\nWhat is your name?: \n')
    print(f'\n{name}... travel at your own risk...HAHAHAHAHA! \n')
    
    return name

def pickup_item(item_name):
    room_list = player.current_room.items
    if not any(d.name == item_name for d in room_list):
        print(f'{item_name} is not here')
    else:
        for item in room_list:
            if item_name == item.name:
                player.add_item(item)
                player.current_room.remove_item(item)
                item.on_take()
                break
            else:
                pass

def drop_item(item_name):
    player_items = player.items
    if not any(d.name == item_name for d in player_items):
        print(f'{item_name} is not in your bag...')
    else:
        for item in player_items:
            if item_name == item.name:
                player.remove_item(item)
                player.current_room.add_item(item)
            else:
                pass

name = ''
intro()
start()
player = Player(name, room['outside'])

while True:
    
    print(f'\n{player.name} is in the {player.current_room.name}. {player.current_room.description}.\n')
    
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
                    '\nYou stubbed your toe on the treasure chest silly! It hurts but you can still walk, and the chest opened! Look inside? (y/n):\n')
                if selection == 'y':
                    player.current_room.speak_items()
                    selection = input('\nTake the treasure? (y/n): \n')
                    if selection == 'no':
                        pass
                    else:
                        pickup_item('Gold')
                else:
                    continue
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
        elif selection == 'l':
            if len(player.current_room.items) == 0:
                print(f'\n{player.name} looks around and sees nothing of use...what a waste of your time.\n')
            else:
                print(f'\n{player.name} looks around and sees: \n')
                player.current_room.speak_items()
                selection = input('\nWill you take anything from this room? [take] [name of item] or [no]: \n')
                if selection == 'no':
                    pass
                else:
                    item = selection.split(' ')
                    pickup_item(item[1])
        elif selection == 'i':
            if len(player.items) == 0:
                print('\nThere is nothing in your bag...\n')
            else:
                print(f'\n{player.name} looks in their bag and sees\n')
                player.check_items()
                selection = input(f'\nDo you want to remove any of your items? [drop] [item name] or [no] \n')
                if selection == 'no':
                    pass
                else:
                    item = selection.split(' ')
                    drop_item(item[1])
        else:
            print('Your only choices are [n] [s] [e] [w] [q] [l]')
    except AttributeError:
        print('Oh no')
