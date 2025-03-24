class Bird:
    def sound(self):
        print("Birds chirp")

class Duck(Bird):
    def sound(self):
        print("Ducks quack")

bird = Bird()
bird.sound()  # Output: Birds chirp

duck = Duck()
duck.sound()  # Output: Ducks quack
