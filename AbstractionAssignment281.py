from abc import ABC, abstractmethod  # Importing ABC (Abstract Base Class) and abstractmethod decorator


class Shape(ABC):  # Abstract class Shape
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):  # Abstract method area
        pass

    def display_color(self):  # Regular method to display the color
        print(f"This shape is {self.color}")


class Rectangle(Shape):  # Child class Rectangle inheriting from Shape
    def __init__(self, color, width, height):
        super().__init__(color)  # Calling the parent class constructor
        self.width = width
        self.height = height

    def area(self):  # Implementation of the abstract method area
        return self.width * self.height


# Creating objects
my_rectangle = Rectangle("blue", 5, 10)
my_rectangle.display_color()  # Output: This shape is blue
print("Area of Rectangle:", my_rectangle.area())  # Output: Area of Rectangle: 50
