from model.repairInstruments import RepairInstruments
from model.rating import Rating
from model.fix import Fix


class Screws(RepairInstruments, object):
    def __init__(self, price=0, rating=Rating.LOW, fix=Fix.DOOR, producer=0, size = 0):
        super(Screws, self).__init__(price, rating, fix, producer)
        self.size = size

    def __str__(self):
        return ('The price = {0} $, Rating Instruments {1} , Fix {2},'
                + 'it\'s produced by {3} , Size screws {4}  \n').format(self.price,
                                                     self.rating,
                                                     self.fix,
                                                     self.producer,
                                                     self.size)

    def __repr__(self):
        return self.__str__()