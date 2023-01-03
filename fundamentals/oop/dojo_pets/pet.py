class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
        return self
    
    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print("Undefined")
        return self


class Dog(Pet):
    def __init__(self, name, breed, tricks, health, energy):
        super().__init__(name, "Dog", tricks, health, energy)
        self.breed = breed

    def noise(self):
        print("Ruff!")
        return self

class Cat(Pet):
    def __init__(self, name, breed, tricks, health, energy):
        super().__init__(name, "Cat", tricks, health, energy)
        self.breed = breed

    def noise(self):
        print("Meow.")
        return self