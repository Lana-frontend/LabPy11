from model import rating
from model.child import Child
from model.drill import Drill
from model.fix import Fix
from model.hammer import Hammer
from model.rating import Rating
from model.screws import Screws
from model.type import Type


class RepairInstrumentsManager:
    def __init__(self, repair_list):
        self.repair_list = repair_list

    def sort_repair_by_price(self, reverse):
        return sorted(self.repair_list, key=lambda repairInstruments: repairInstruments.price, reverse=reverse)

    def sort_repair_by_width(self, reverse):
        return sorted(self.repair_list, key=lambda repairInstruments: repairInstruments.producer, reverse=reverse)

    def find_repair_by_rating(self, rating):
        return list(filter(lambda repairInstruments: repairInstruments.rating == rating, self.repair_list))




hammer = Hammer(230, Rating.MEDIUM, Fix.DOOR, 0, "tree" ,  20)
screws = Screws(10, Rating.LOW, Fix.DOOR, 0,  20)
drill = Drill(20, Rating.HIGH, Fix.DOOR, 5, Type.ELECTRONIC, 220)
child = Child(20, Rating.HIGH, Fix.DOOR, 5, "Velykodnyi", "Black")

repair = [screws, drill, hammer, child]
manager = RepairInstrumentsManager(repair)
print(manager.sort_repair_by_price(False))
print("\n")
print(manager.sort_repair_by_width(True))
print("\n")
print(manager.find_repair_by_rating(rating.Rating.LOW))