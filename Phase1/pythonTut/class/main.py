class Dog:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def bark(self):
        return f"{self.name} says: {self.sound}"


d1 = Dog("Mark", "bhaau")
d2 = Dog("Kukur", "woof woof!")
print(d1.bark())
print(d2.bark())
