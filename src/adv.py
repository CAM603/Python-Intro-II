from room import Room
from player import Player
from item import Sword, Valuable
import random

# Declare some colors
GREEN = "\033[0;32;40m"
GREEN2 = "\033[1;32;40m"
RED = "\033[1;31;40m"
BLUE = "\033[0;34;40m"

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! There is a large treasure chest towards the north...""",
    ),
}

# Declare items
item = {
    "gladius": Sword(
        "Gladius", "The sword is short, featuring a thick and wide blade."
    ),
    "needle": Sword(
        "Needle",
        "The sword is small, like a needle, but the blade is strong. Best for turning enemies into swiss cheese.",
    ),
    "gold": Valuable(
        "Gold",
        "large golden nugget, this is what everyone has been risking their lives for!",
    ),
}

# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

# Add items to room
room["foyer"].add_item(item["gladius"])
room["foyer"].add_item(item["needle"])
room["treasure"].add_item(item["gold"])

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
    print(GREEN + "\nHello brave warrior, welcome to the game!\n")
    print("Your goal is to find the long lost nugget")
    print(
        "Many have lost their lives trying to find it.\nTheir remains still litter the cave..."
    )
    commands()
    print("\nType [h] anytime to see your commands\n")


def commands():
    print("\n---------------------------")
    print("Your Commands:")
    print("[n] travel north")
    print("[s] travel south")
    print("[e] travel east")
    print("[w] travel west")
    print("[l] look around")
    print("[i] check your items")
    print("[q] end the game")
    print("---------------------------\n")


def start():
    global name
    name = input(GREEN2 + "\nWhat is your name?: \n")
    print(f"\n{GREEN}{name}... travel at your own risk...{RED}H A H A H A H A H A! \n")

    return name


def random_fail():
    num = random.randrange(0, 5)

    possibilities = [
        f"\n{RED}You ran into a wall! Your nose is bleeding but you can still continue, will you? (y/n):\n",
        f"\n{RED}🕸 🕸 🕸 🕸 🕸 🕸\nYou walked into a spider web!\n🕸 🕸 🕸 🕸 🕸 🕸\nYou didn't see any spiders but now You're itchy everywhere. 🕷\n Continue? (y/n):\n",
        f"\n{RED}You set off a trap and rocks bury the path ahead.\nCan't go that way anymore. Continue? (y/n):\n",
        f"\n{RED}Whoa! A dead body! 💀 Probably shouldn't go that way...Are you tough enough to continue? (y/n):\n",
        f"\n{RED}🦇🦇🦇🦇🦇\n 🦇🦇🦇🦇🦇\n Looks like a dead end full of bats! One of them pooped on you. Continue? (y/n):\n",
    ]
    return possibilities[num]


def pickup_item(item_name):
    room_list = player.current_room.items
    if not any(d.name == item_name for d in room_list):
        print(f"{BLUE}{item_name} is not here")
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
        print(f"{BLUE}{item_name} is not in your bag...")
    else:
        for item in player_items:
            if item_name == item.name:
                player.remove_item(item)
                player.current_room.add_item(item)
            else:
                pass


name = ""
intro()
start()
player = Player(name, room["outside"])

while True:

    print(
        f"\n{GREEN}{player.name} is in the {player.current_room.name}. {player.current_room.description}.\n"
    )

    selection = input(
        GREEN2 + "\nWhich direction will you travel? [n] [s] [e] [w] [q]: \n"
    )

    if selection == "q":
        print(RED + "Quitting...")
        break

    try:
        if selection == "n":
            if player.current_room.name == "Grand Overlook":
                selection = input(
                    RED
                    + "\nYou fell off the cliff silly!\n If you stay here, you are sure to succumb to your wounds...climb back up? (y/n): \n"
                )
                if selection == "y":
                    pass
                else:
                    break
            elif player.current_room.name == "Treasure Chamber":
                selection = input(
                    "\nYou stubbed your toe on the treasure chest silly! It hurts but you can still walk, and the chest opened! Look inside? (y/n):\n"
                )
                if selection == "y":
                    player.current_room.speak_items()
                    selection = input(GREEN2 + "\nTake the treasure? (y/n): \n")
                    if selection == "y":
                        pickup_item("Gold")
                    else:
                        pass
                else:
                    continue
            else:
                player.change_room(player.current_room.n_to)
        elif selection == "s":
            if player.current_room.name == "Outside Cave Entrance":
                selection = input(
                    RED
                    + "\nThe cave is to the north! Are you trying to go home already? (y/n):\n"
                )
                if selection == "y":
                    break
                else:
                    continue
            else:
                player.change_room(player.current_room.s_to)
        elif selection == "e":
            if player.current_room.name == "Outside Cave Entrance":
                selection = input(
                    RED
                    + "\nThe cave is to the north! Are you trying to go home already? (y/n):\n"
                )
                if selection == "y":
                    break
                else:
                    continue
            elif (
                player.current_room.name == "Narrow Passage"
                or player.current_room.name == "Treasure Chamber"
                or player.current_room.name == "Grand Overlook"
            ):
                selection = input(random_fail())
                if selection == "y":
                    continue
                else:
                    break
            else:
                player.change_room(player.current_room.e_to)
        elif selection == "w":
            if player.current_room.name == "Outside Cave Entrance":
                selection = input(
                    RED
                    + "\nThe cave is to the north! Are you trying to go home already? (y/n):\n"
                )
                if selection == "y":
                    break
                else:
                    continue
            elif (
                player.current_room.name == "Narrow Passage"
                or player.current_room.name == "Treasure Chamber"
                or player.current_room.name == "Foyer"
                or player.current_room.name == "Grand Overlook"
            ):
                selection = input(random_fail())
                if selection == "y":
                    continue
                else:
                    break
            else:
                player.change_room(player.current_room.w_to)
        elif selection == "l":
            if len(player.current_room.items) == 0:
                print(
                    f"\n{BLUE}{player.name} looks around and sees nothing of use...what a waste of your time.\n"
                )
            elif player.current_room.name == "Treasure Chamber":
                print(BLUE + "\nThere is a large treasure chest towards the north...\n")
            else:
                print(f"\n{BLUE}{player.name} looks around and sees: \n")
                player.current_room.speak_items()
                selection = input(
                    GREEN2
                    + "\nWill you take anything from this room? [take] [name of item] or [no]: \n"
                )
                if selection == "no":
                    pass
                else:
                    item = selection.split(" ")
                    pickup_item(item[1])
        elif selection == "i":
            if len(player.items) == 0:
                print(BLUE + "\nThere is nothing in your bag...\n")
            else:
                print(f"\n{BLUE}{player.name} looks in their bag and sees\n")
                player.check_items()
                selection = input(
                    f"\n{GREEN2}Do you want to remove any of your items? [drop] [item name] or [no] \n"
                )
                if selection == "no":
                    pass
                else:
                    item = selection.split(" ")
                    drop_item(item[1])
        elif selection == "h":
            commands()
        else:
            print(GREEN2 + "Your only choices are [n] [s] [e] [w] [q] [l]")
    except AttributeError:
        print(RED + "Oh no")
