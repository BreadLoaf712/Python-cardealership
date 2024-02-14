from Car import Car

class Dealership:
    def __init__(self):
        self.inventory = []

    def add_car(self, car):
        self.inventory.append(car)

    def display_inventory(self):
        result = "Dealership Inventory:\n"
        for car in self.inventory:
            result += car.display_info() + "\n"
        return result
