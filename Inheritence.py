class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
    def speak(self):
        print("I don't know what to say!")

class Dog(Pet):
    def __init__(self, name, age, color):
        super().__init__(name,age)
        self.color = color
    def speak(self):
        print("Bark")

   
class Cat(Pet):
    def __init__(self, name, age, character):
        super().__init__(name,age)
        self.character = character
    def speak(self):
        print("Meow")

p = Pet("Harry", 10)
p.show()
p.speak()
c = Cat("Potter", 5, "arrogant")
c.speak()
print(c.character)
print(c.name)
c.show()
d = Dog("Puppy", 8, "Black")
d.speak()
print(d.color)
print(d.name)