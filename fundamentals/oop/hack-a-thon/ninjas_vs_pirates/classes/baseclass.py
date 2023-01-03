import random

class BaseClass:
    npc_actions = ["ATTACK", "USE ITEM", "REST"]


    def __init__(self, name, strength, health):
        self.name = name
        self.strength = strength
        self.max_strength = strength
        self.health = health

    def show_stats(self):
        print(f"Name: {self.name}\nStrength: {self.strength}\nHealth: {self.health}\nInventory: ")
        for item in self.items:
            print(item.name)

    def attack(self, victim):
        victim.health -= self.strength
        print(f"{self.name} is attacking {victim.name} for {self.strength} damage!")
        self.strength -= 2

    def rest(self):
        if self.strength + 5 > self.max_strength:
            self.strength = self.max_strength
        else:
            self.strength += 5

    def npc_use_item(self):
        index = random.randint(0, len(self.items) - 1) if len(self.items) > 1 else 0
        print("Using this index:", index)
        self.items[index].use(self)
        del self.items[index]
        if len(self.items) == 0:
            BaseClass.npc_actions.remove("USE ITEM")


    def use_item(self):
        if len(self.items) == 0:
            print("Seems like you're inventory is empty!")

        else:
            print("Inventory: ", end="")
            for item in self.items:
                print(item.name, end=", ")
            print("\n")

            item_input = input("What item would you like to use?")
            item_used = False

            while not item_used:
                for item in self.items:
                    if item_input.upper() == item.name:
                        item.use(self)
                        self.items.remove(item)
                        item_used = True
                        break
                    else:
                        item_input = input("You don't seem to have that item. Try another one!")

