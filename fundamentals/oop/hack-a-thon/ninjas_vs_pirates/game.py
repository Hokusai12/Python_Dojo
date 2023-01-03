from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

role = input("Would you like to be a ninja or a pirate? The pirate is stronger, but the ninja has special shurikens that have a chance to deal x2 damage(Ninja/Pirate): ")
while True:
    if role.upper() == "NINJA" or role.upper() == "PIRATE":
        role = role.upper()
        print(f"Oh so you're a {role} eh? I like it! But ready yourself, they're coming!")
        break
    else:
        role = input("I didn't quite get that, would you make sure you put ninja or pirate: ")

while michelangelo.health > 0 and jack_sparrow.health > 0:

    if role == "PIRATE":
        action = input("What would you like to do? (Attack/Use Item/Rest/Stats): ")

        if action.upper() == "ATTACK":
            jack_sparrow.attack(michelangelo)
        elif action.upper() == "USE ITEM":
            jack_sparrow.use_item()
        elif action.upper() == "REST":
            jack_sparrow.rest()
        elif action.upper() == "STATS":
            jack_sparrow.show_stats()
            print("")
            michelangelo.show_stats()
            continue
        elif action.upper() == "EXIT":
            break


        #Gives the ninja a random action
        michelangelo.npc_actions(jack_sparrow)


    elif role == "NINJA":
        action = input("What would you like to do? (Attack/Use Item/Rest/Stats): ")

        if action.upper() == "ATTACK":
            michelangelo.attack(jack_sparrow)
        elif action.upper() == "USE ITEM":
            michelangelo.use_item()
        elif action.upper() == "REST":
            michelangelo.rest()
        elif action.upper() == "STATS":
            jack_sparrow.show_stats()
            michelangelo.show_stats()
            continue
        elif action.upper() == "EXIT":
            break

        jack_sparrow.npc_action(michelangelo)



print("Jack Sparrow" if jack_sparrow.health <= 0 else "Michelangelo", "died!")
print("END STATS")
jack_sparrow.show_stats()
michelangelo.show_stats()