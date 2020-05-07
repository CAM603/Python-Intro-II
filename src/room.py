# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

        self.items = [] if items == None else items

    def add_item(self, item):
        self.items.append(item)

    def speak_items(self):
        if len(self.items) == 0:
            print('\n There is nothing useful in this room \n')
        else:
            for item in self.items:
                print(f'\nThe room has {item.name}\n')

    def __str__(self):
        return f'Room: {self.name} Description: {self.description}'
