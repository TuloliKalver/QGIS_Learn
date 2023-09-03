
class Person:
    number_of_people = 0
    
    def __init__ (self,name):
        self.name = name
        Person.add_person()
    
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1
    
P1 = Person("Tim")
print(Person.number_of_people)
P2 = Person("Kim")
print(Person.number_of_people)

print(f"Inimesi kokku {Person.number_of_people_()}")