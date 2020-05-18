# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, items=None):
        self.name = name
        self.current_room = current_room

        self.items = [] if items == None else items

    def check_items(self):
        if len(self.items) == 0:
            print("\n nothing in the bag \n")
        else:
            for item in self.items:
                print(f"\nA {item}\n")

    def change_room(self, room):
        self.current_room = room

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
