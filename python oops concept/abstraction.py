from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract class
    @abstractmethod
    def make_sound(self):
        pass  # Abstract method

class Cat(Animal):
    def make_sound(self):
        print("Cat meows")

cat = Cat()
cat.make_sound()  # Output: Cat meows
