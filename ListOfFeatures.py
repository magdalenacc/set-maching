
class ListOfFeatures:
    def __init__(self, name):
        self.name = name
        self.list = []

    def addToList(self, feature):
        self.list.append(feature)
        