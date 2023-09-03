class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.dog_name = dog_name
        self.dog_age = dog_age
        self.dog = dog
    
    
    def get_dog_data(self):
        return(self.dog_name,self.dog_age)

    def get_name(self):
        return(self.name)     
    
    def get_age(self):
        return(self.age)
    def get_dog(self):
        return()
    
d=Dog("Tim",21)
print(d.get_name())
d2=Dog("Bell", 14)
print(d2.get_age())

dog_name = ["Bill","Snoopy"]
dog_age = [21,34]

a=Dog(dog_name,dog_age)
print(a.get_dog_data())