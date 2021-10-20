class Person:
    no_of_people = 0
    def __init__(self,name):
        self.name = name
        
    @classmethod
    def nop(cls):
        return cls.no_of_people
      

print(Person.nop())
print(Person.nop())

