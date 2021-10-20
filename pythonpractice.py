from typing import AsyncGenerator


class Dog: 
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def get_name(self):
            return self.name

        def get_age(self):
            return self.age

        def set_age(self, age):
            self.age= age


d1 = Dog("Harry",10)
d1.set_age(20)
print(d1.get_age())
