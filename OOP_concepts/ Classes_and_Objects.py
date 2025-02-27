class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0
        
    def accelerating(self):
        print("accelerating")
        
my_car = Car()
my_car.accelerating()