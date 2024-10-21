class Car:
    def __init__(self,model,year,brand):
        self.model = model
        self.year = year
        self.brand = brand 

    def much(self):
        print(f"{self.year} is the day {self.brand} was created")


Car1 = Car("Corolla",1996,"Toyota")

Car1.much()