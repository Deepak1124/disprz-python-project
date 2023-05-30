# Create animal base class with attribute and related methods then create sub concrete subclass using animal eg of subclass: cow, horse, dog

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"The {self.name} makes the sound: {self.sound}")

    def move(self):
        print(f"The {self.name} is moving.")

    def eat(self, food):
        print(f"The {self.name} is eating {food}.")


class Cow(Animal):
    def __init__(self):
        super().__init__("Cow", "Moo")


class Horse(Animal):
    def __init__(self):
        super().__init__("Horse", "Neigh")

    def gallop(self):
        print(f"The {self.name} is galloping.")


class Dog(Animal):
    def __init__(self):
        super().__init__("Dog", "Woof")

    def bark(self):
        print(f"The {self.name} is barking.")


cow = Cow()
horse = Horse()
dog = Dog()

# Invoking parent class methods
cow.speak()      
horse.speak()    
dog.speak()     

cow.move()  
horse.eat("grass")
dog.eat("bones")

# Invoke methods specific to each subclass
horse.gallop()
dog.bark()
