from model.rating import Rating
from model.repairInstruments import RepairInstruments
from model.fix import Fix

class Child (RepairInstruments , object):
    def __init__(self, price=0, rating=Rating.LOW, fix=Fix.DOOR, producer=0, name = "NoName" , color = "NoColor"):
            super(Child, self).__init__(price, rating, fix, producer)
            self.name = name
            self.color = color

            def __str__(self):
                return ('The price = {0} $, Rating Instruments {1} , Fix {2},'
                        + 'it\'s produced by {3} , name child {4} , color child {5} \n').format(
                    self.price,

                    self.rating,
                    self.fix,
                    self.producer,
                    self.name,
                    self.color)

            def __repr__(self):
                return self.__str__()
