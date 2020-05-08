class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def on_take(self):
        print(f'\nYou have picked up {self.name}\n')

    def __str__(self):
        return f'{self.name}. {self.description}'

class Sword(Item):
    category = 'sword'
    def __init__(self, name, description):
        super().__init__(name, description)

    def __str__(self):
        return f'{self.category}, named {self.name}. {self.description}'

class Valuable(Item):
    category = 'valuable'
    def __init__(self, name, description):
        super().__init__(name, description)

    def __str__(self):
        return f'{self.name}. {self.description}'