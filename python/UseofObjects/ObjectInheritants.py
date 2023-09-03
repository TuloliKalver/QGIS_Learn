
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"i am {self.name} and i am {self.age} years old")


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name,age)
        self.color = color
    def speak(self):
        print("Bark") 
    def show(self):
        print(f"i am {self.name} and i am {self.age} years old and i am {self.color}" )



class Dog(Pet):
    def speak(self):
        print("Meow")
                

p = Pet("Snoopy", 2)
p.show()
c = Cat("Poopy", 15, "Brown")
c.show()
d = Dog("Noopy",19)
d.speak()