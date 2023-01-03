import ninja
import pet


doggie = pet.Dog("Fido", "Dog", ["Sit", "Play Dead", "Roll Over"], 20, 50)
kiki = pet.Cat("Kiki",)
ninja = ninja.Ninja("Da", "Goener", doggie, ["Snicky Snacks"], ["Scooby Snacks"])


ninja.feed().bathe().walk()