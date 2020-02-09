from ListOfFeatures import ListOfFeatures
from Set import Set

class Model():
    def __init__(self):
        self.listoffeatures = ListOfFeatures("pierwsza")
        self.set = Set()
        self.listOfParams = ListOfFeatures("params")

    def resetmodel(self):
        self.set.set.clear()
        self.set.listofResults.clear()
        self.set.size=0

        self.listOfParams.list.clear()
        self.listoffeatures.list.clear()



