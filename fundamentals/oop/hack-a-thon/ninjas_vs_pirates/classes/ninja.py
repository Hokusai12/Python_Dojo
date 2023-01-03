import classes.items as items
import classes.baseclass as baseclass
import random

class Ninja(baseclass.BaseClass):
    
    def __init__( self , name ):
        super().__init__(name, 10, 100)
        self.items = []
        self.items.append(items.Item("HEALTH POTION", items.use_potion))

    def get_weapon(self):
        if random.randint(0, 100) > 75:
            return "SHURIKEN"
        else:
            return "WAKIZAGI"

    def attack(self, victim, weapon=0):
        if weapon != "SHURIKEN" and weapon != "WAKIZAGI":
            weapon = input("Which weapon would you like to use? (Shuriken/Wakizagi): ")

            while True:
                if weapon.upper() != "SHURIKEN" and weapon.upper() != "WAKIZAGI":
                    weapon = input("That's not a weapon you have. Choose one of the listed weapons: ")
                else: 
                    break
        
        if weapon.upper() == "SHURIKEN":
            if(random.randint(0, 100) > 75):
                victim.health -= self.strength * 2
                print(f"Attacked twice! Dealt {self.strength * 2} damage!")
                self.strength -= 2
            else:
                victim.health -= self.strength
                print(f"Attacked once! Dealt {self.strength} damage!")
                self.strength -= 2
        elif weapon.upper() == "WAKIZAGI":
            victim.health -= self.strength
            print(f"Attacked once! Dealt {self.strength} damage!")
            self.strength -= 2



        def npc_action(self, victim):
            action = random.randint(0, len(baseclass.BaseClass.npc_actions) - 1)
            print(baseclass.BaseClass.npc_actions[action])
            if baseclass.BaseClass.npc_actions[action] == "ATTACK":
                newweapon = self.get_weapon()
                print(newweapon)
                self.attack(victim, newweapon)
            elif baseclass.BaseClass.npc_actions[action] == "USE ITEM":
                self.npc_use_item()
            elif baseclass.BaseClass.npc_actions[action] == "REST":
                self.rest()
