class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak()
animal=Animal()
animal.speak()
