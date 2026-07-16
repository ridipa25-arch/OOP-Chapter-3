class Vehicle:
    def move(self):
        print("Vehicle is moving.")

class Car(Vehicle):
    def move(self):          
        print("Car is driving.")

c = Car()
c.move()