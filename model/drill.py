from model.repairInstruments import RepairInstruments
from model.rating import Rating
from model.fix import Fix
from model.type import Type


class Drill(RepairInstruments, object):
    def __init__(self, price=0, rating=Rating.LOW, fix=Fix.DOOR, producer=0, type=Type.ELECTRONIC, power=0):
        super(Drill, self).__init__(price, rating, fix, producer)
        self.power = power
        self.type = type

    def __str__(self):
        return ('The price = {0} $, Rating Instruments {1} , Fix {2},'
                + 'it\'s produced by {3} , Type drill {4} , Power drill {5} \n').format(self.price,
                                                     self.rating,
                                                     self.fix,
                                                     self.type,
                                                     self.power,
                                                     self.producer)

    def __repr__(self):
        return self.__str__()
