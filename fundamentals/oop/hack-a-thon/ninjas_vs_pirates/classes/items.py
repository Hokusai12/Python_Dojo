class Item:
    def __init__(self, name, use):
        self.name = name
        self.use = use

def use_potion(user):
    user.health += 10
    print("Healed for 10 hp!")


