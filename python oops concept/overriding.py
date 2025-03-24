class Parent:
    def show(self):
        print("This is the parent class")

class Child(Parent):
    def show(self):
        print("This is the child class")

obj = Child()
obj.show()  # Output: This is the child class
