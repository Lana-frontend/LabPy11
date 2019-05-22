from model.repairInstruments import RepairInstruments
from model.rating import Rating
from model.fix import Fix


class Hammer(RepairInstruments, object):
    def __init__(self, price=0, rating=Rating.LOW, fix=Fix.DOOR, producer=0, handleMaterial = "NULL", weight = 0):
        super(Hammer, self).__init__(price, rating, fix, producer)
        self.handleMaterial = handleMaterial
        self.weight = weight

    def __str__(self):
        return ('The price = {0} $, Rating Instruments {1} , Fix {2},'
                + 'it\'s produced by {3} , Handle material hammer {4} , weight hammer {5} \n').format(self.price,

                                                     self.rating,
                                                     self.fix,
                                                     self.producer,
                                                     self.handleMaterial,
                                                     self.weight)

    def __repr__(self):
        return self.__str__()