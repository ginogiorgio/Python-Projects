class Vehicle:
    def __init__(self, make, model, year):
        self._make = make  # Protected attribute
        self._model = model  # Protected attribute
        self._year = year  # Protected attribute
        self.__odometer_reading = 0  # Private attribute

    def get_make(self):
        """Get the make of the vehicle."""
        return self._make

    def get_model(self):
        """Get the model of the vehicle."""
        return self._model

    def get_year(self):
        """Get the year of the vehicle."""
        return self._year

    def get_odometer_reading(self):
        """Get the odometer reading of the vehicle."""
        return self.__odometer_reading

    def _set_odometer_reading(self, mileage):
        """Set the odometer reading of the vehicle."""
        if mileage >= self.__odometer_reading:
            self.__odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def drive(self, miles):
        """Simulate driving the vehicle."""
        self.__odometer_reading += miles


# Create an object of the Vehicle class
my_car = Vehicle("Toyota", "Camry", 2022)

# Accessing protected attributes
print("Make:", my_car.get_make())  # Output: Make: Toyota
print("Model:", my_car.get_model())  # Output: Model: Camry
print("Year:", my_car.get_year())  # Output: Year: 2022

# Accessing and modifying private attribute indirectly through a method
print("Odometer Reading:", my_car.get_odometer_reading())  # Output: Odometer Reading: 0
my_car.drive(100)
print("Odometer Reading:", my_car.get_odometer_reading())  # Output: Odometer Reading: 100
