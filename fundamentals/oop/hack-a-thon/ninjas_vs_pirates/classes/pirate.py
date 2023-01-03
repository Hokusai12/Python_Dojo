import classes.items as items
import classes.baseclass as baseclass
import random

class Pirate(baseclass.BaseClass):

    def __init__( self , name ):
        super().__init__(name, 15, 100)
        self.items = []
        self.items.append(items.Item("HEALTH POTION", items.use_potion))


    def npc_action(self, opponent):
        action = random.randint(0, len(baseclass.BaseClass.npc_actions) - 1)
        print(baseclass.BaseClass.npc_actions[action])
        if baseclass.BaseClass.npc_actions[action] == "ATTACK":
            self.attack(opponent)
        elif baseclass.BaseClass.npc_actions[action] == "USE ITEM":
            self.npc_use_item()
        elif baseclass.BaseClass.npc_actions[action] == "REST":
            self.rest()