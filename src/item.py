PURPLE = "\033[1;35;40m"
YELLOW = "\033[1;33;40m"


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f"\n{PURPLE}You have picked up a {self}\n")

    def __str__(self):
        return f"{PURPLE}{self.name}. {self.description}"


class Sword(Item):
    category = "sword"

    def __init__(self, name, description):
        super().__init__(name, description)

    def __str__(self):
        return f"{self.category}, named {self.name}. {self.description}"


class Valuable(Item):
    category = "valuable"

    def __init__(self, name, description):
        super().__init__(name, description)

    def __str__(self):
        return f"{YELLOW}{self.description}"
