class Animal:
    def __init__(self,name,family,feeding_habit,habitat):
        self.name = name
        self.famiy = family
        self.feeding_habit = feeding_habit
        self.habitat = habitat

    def animal_sound(self):
        print(f"{self.name} makes a bleaing sound ")
    def sleep(self):
        print(f" The {self.name} is sleeping")
    def eat(self):
        print(f"{self.name} eats vegs")

Animal_one = Animal("Goat","Bovidae","Milk","savanna")
Animal_two = Animal("Lion","Felidae","carnivorous","Savannas")
Animal_three = Animal("Cat","Felidae","carnivorous","open forest")
Animal_four = Animal("Horse","Equidae","hoofed","open grasslands")


print(f"{Animal_one.animal_sound}")

