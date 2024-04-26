from abc import ABC, abstractmethod

class AbstractVehicle(ABC):
    def _init_(self, color, num_tyres, gears):
        self.color = color
        self.num_tyres = num_tyres
        self.gears = gears

    @abstractmethod
    def display_details(self):
        pass