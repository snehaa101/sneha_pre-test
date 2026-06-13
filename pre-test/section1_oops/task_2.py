from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(stop):
        print("Car stopped")

    def fuel_type(self):
        print("petrol")


c = Car()
c.start()
c.stop()
c.fuel_type()
