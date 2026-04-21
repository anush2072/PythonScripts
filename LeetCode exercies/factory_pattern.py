from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def getType(self) -> str:
        pass

class Car(Vehicle):
    def getType(self) -> str:
        return "Car"

class Bike(Vehicle):
    def getType(self) -> str:
        return "Bike"

class Truck(Vehicle):
    def getType(self) -> str:
        return "Truck"

class VehicleFactory(ABC):
    @abstractmethod
    def createVehicle(self) -> Vehicle:
        pass

class CarFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
        return Car()
class BikeFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
        return Bike()
class TruckFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
        return Truck()


carFactory = CarFactory()
truckFactory = TruckFactory()
bikeFactory = BikeFactory()

myCar = carFactory.createVehicle()
myTruck = truckFactory.createVehicle()
myBike = bikeFactory.createVehicle()

print(myCar.getType())   # "Car"
print(myTruck.getType()) # "Truck"
print(myBike.getType())  # "Bike"

'''
=== INTERVIEW FOLLOWUP QUESTIONS ===
1. How would you modify this pattern to support dynamic vehicle creation based on configuration files or user input?
2. What if you need to add a new vehicle type without modifying the existing factory code?

=== REAL WORLD APPLICATION ===
Game Development: Used in game engines to create different types of game objects (characters, weapons, items) based on player actions or game events, enabling flexible object instantiation without coupling game logic to specific classes.

=== TIME AND SPACE COMPLEXITY ===
Time Complexity: O(1) for object creation
- Factory method calls are constant time operations
- Object instantiation depends on constructor complexity
- No loops or recursive operations

Space Complexity: O(1) per object created
- Each factory instance: O(1)
- Created objects: O(k) where k = number of objects
- Factory pattern itself adds minimal overhead
'''