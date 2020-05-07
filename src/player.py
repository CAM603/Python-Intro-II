# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, items=None):
        self.name = name
        self.current_room = current_room

        # if items = None:
        #     self.items = []
        # else:
        #     self.items = items
        self.items = [] if items == None else items

    def change_room(self, room):
        self.current_room = room
    
    def add_item(self, item):
        self.items.append(item)
