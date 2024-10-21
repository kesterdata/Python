class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def sound(self):
        print(f"{self.name} is making a moew sound")

    def eat(self):
        print(f"{self.name} drinks milk")

class Cat(Animal):
    def __init__(self, name, species,family):
        super().__init__(name, species)
        self.family = family

    def sound(self):
        print(f"{self.name} makes a boo sound")
    
    def eat(self):
        print(f"{self.name} eats peanut")

Cat1 = Cat("Bill","Mammal","Ray")
Cat2 = Animal("Ray","Mammal")


print(Cat1.family)
    