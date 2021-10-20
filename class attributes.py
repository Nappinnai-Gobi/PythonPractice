from os import name


class Person:
    no_of_people = 0
    def __init__(self, name):
         self.name = name
         Person.no_of_people += 1

print(Person.no_of_people)

p1 = Person("Nikhil")
print(p1.no_of_people)
p2 = Person("Veshu")
print(p2.no_of_people)

