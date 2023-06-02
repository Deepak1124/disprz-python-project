# Create animal base class with attribute and related methods then create sub concrete subclass 
# using animal eg of subclass: cow, horse, dog


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def make_sound(self):
        print(f"{self.name} is making a sound.")


class Cow(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def moo(self):
        print("Moo!")


class Horse(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def whinny(self):
        print("Neigh!")


class Dog(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def bark(self):
        print("Woof!")


cow = Cow("Meee", "cow")
horse = Horse("Boom", "horse")
dog = Dog("Dany", "dog")

cow.moo()
horse.whinny()
dog.bark()

cow.make_sound()