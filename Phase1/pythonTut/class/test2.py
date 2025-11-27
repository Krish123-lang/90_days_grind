class Person:
    def __init__(self, name, age):
        self.name=name
        self._age=age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value<0:
            raise ValueError('Age cannot be negative!')
        self._age = value
        
    def greet(self):
        return f"Hello, {self.name}! You're {self._age} years old!"
    
p1=Person('Krishna', 23)
p1.age=-2 #remove the negative sign (-) to avoid error. this avoids entering negative age in the program!
print(p1.greet())