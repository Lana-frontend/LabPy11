from model.rating import Rating
from model.fix import Fix


class RepairInstruments:

    def __init__(self, price=0, rating=Rating.LOW, fix=Fix.DOOR, producer=0):
        self.price = price
        self.producer = producer
        self.rating = rating
        self.fix = fix

    def __str__(self):
        return ('The price = {0} $, Rating Instruments {1} , Fix {2},'
                + 'it\'s produced by {3} \n').format(self.price,
                                                     self.rating,
                                                     self.fix,
                                                     self.producer)

    def __repr__(self):
        return self.__str__()
