class Car:
    def __init__(self, brand, model):  # Constructor (called when an object is created)
        self.brand = brand  # Attribute
        self.model = model  # Attribute

    def display(self):  # Method
        print(f"Car: {self.brand} {self.model}")

# Creating objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

car1.display()  # Output: Car: Toyota Corolla
car2.display()  # Output: Car: Honda Civic
