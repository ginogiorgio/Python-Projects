# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    # Parent method
    def make_sound(self):
        pass  # Placeholder method, to be overridden by child classes

# Child class 1
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    # Polymorphic method overriding parent method
    def make_sound(self):
        return "Woof!"

# Child class 2
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    # Polymorphic method overriding parent method
    def make_sound(self):
        return "Meow!"

# Create instances of child classes
dog = Dog("Buddy", "Labrador")
cat = Cat("Whiskers", "White")

# Demonstrate polymorphism by calling the same method on different objects
print(dog.name + " says: " + dog.make_sound())  # Dog instance calling make_sound()
print(cat.name + " says: " + cat.make_sound())  # Cat instance calling make_sound()
