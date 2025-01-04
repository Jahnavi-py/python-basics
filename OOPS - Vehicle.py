#.Implement a class Vehicle with subclasses Car and Bike. Override a method to display vehicle type.
class Vehicle:
    def __init__(self, model_name):
        self.model_name = model_name
    def display_vehicle_type(self):
        raise NotImplementedError("Subclass must implement abstract method")
class Car(Vehicle):
    def display_vehicle_type(self):
        print(f"{self.model_name} is car model")
class Bike(Vehicle):
    def display_vehicle_type(self):
        print(f"{self.model_name} is bike model")
car = Car("KIA")
car.display_vehicle_type()
bike = Bike("Royal Enflied")
bike.display_vehicle_type()