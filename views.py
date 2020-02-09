from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout, QLabel, QListWidget, QLineEdit
import sys

from models import Model


class StartWindow(QWidget):
    def __init__(self, model=None):
        super().__init__()  # zwraca klase rodzica i wywoluje jego konstruktor
        self.model = model
        self.interface()

    def interface(self):

        #1-liniowe pola edycyjne
        self.featuresEdt = QLineEdit()
        self.featuresEdt.setText("1")
        self.sizeSetEdt = QLineEdit()
        self.sizeSetEdt.setText("10")
        self.paramsEdt = QLineEdit()
        self.paramsEdt.setText("1")

        # przyciski
        self.addFeaturesBtn = QPushButton("&AddFeatures", self)
        self.createSetBtn = QPushButton("&Create", self)
        self.addParamsBtn = QPushButton("Add&Params", self)
        self.findParams = QPushButton("&FindParams", self)
        self.resetBtn = QPushButton("&Reset", self)

        self.addFeaturesBtn.clicked.connect(self.addFeaturesClick)
        self.createSetBtn.clicked.connect(self.createSetClick)
        self.addParamsBtn.clicked.connect(self.addParamsClick)
        self.findParams.clicked.connect(self.findParamsClick)
        self.resetBtn.clicked.connect(self.resetClick)

        # etykiety
        self.featuresLabel = QLabel("Features: ", self)
        self.setLabel = QLabel("Set: ", self)
        self.paramsLabel = QLabel("Params: ", self)
        self.matchingLabel = QLabel("Maching: ", self)

        # ListWidget
        self.featuresListWidget = QListWidget()
        self.setWidget = QListWidget()
        self.paramsListWidget = QListWidget()
        self.findParamsListWidget = QListWidget()

        # uklad tabelaryczny:
        self.tab_layout = QGridLayout()

        self.tab_layout.addWidget(self.featuresEdt, 0, 0)
        self.tab_layout.addWidget(self.sizeSetEdt, 0, 1)
        self.tab_layout.addWidget(self.paramsEdt, 0, 2)
        self.tab_layout.addWidget(self.resetBtn, 0, 3)

        self.tab_layout.addWidget(self.addFeaturesBtn, 1, 0)
        self.tab_layout.addWidget(self.createSetBtn, 1, 1)
        self.tab_layout.addWidget(self.addParamsBtn, 1, 2)
        self.tab_layout.addWidget(self.findParams, 1, 3)

        self.tab_layout.addWidget(self.featuresLabel, 2, 0)
        self.tab_layout.addWidget(self.setLabel, 2, 1)
        self.tab_layout.addWidget(self.paramsLabel, 2, 2)
        self.tab_layout.addWidget(self.matchingLabel, 2, 3)

        self.tab_layout.addWidget(self.featuresListWidget, 3, 0)
        self.tab_layout.addWidget(self.setWidget, 3, 1)
        self.tab_layout.addWidget(self.paramsListWidget, 3, 2)
        self.tab_layout.addWidget(self.findParamsListWidget, 3, 3)



        # przypisanie utworzonego ukladu do okna

        self.setLayout(self.tab_layout)

        self.showMaximized()
        self.setWindowTitle("Projekt - dopasowanie zbiorow")
        self.show()


    def addFeaturesClick(self):
        self.model.listoffeatures.addToList(self.featuresEdt.text())
        #print(self.model.listoffeatures.list)
        l=len(self.model.listoffeatures.list)-1
        self.featuresListWidget.insertItem(l, self.model.listoffeatures.list[-1])


    def createSetClick(self):
        self.setWidget.clear()
        self.model.set.createSet(int(self.sizeSetEdt.text()), model.listoffeatures.list)
        print(model.set.set)
        for a in model.set.set:
            self.setWidget.addItem(str(a))


    def addParamsClick(self):

        self.model.listOfParams.addToList(self.paramsEdt.text())
        # print(self.model.listoffeatures.list)
        l = len(self.model.listOfParams.list) - 1
        self.paramsListWidget.insertItem(l, self.model.listOfParams.list[-1])
        print(self.model.listOfParams.list)

    def findParamsClick(self):
        self.model.set.findParams(self.model.listOfParams.list)
        for i, a in enumerate(self.model.set.listofResults):
            self.findParamsListWidget.insertItem(i, str(a))

    def resetClick(self):
        self.model.resetmodel()
        self.clearLayout(self.tab_layout)

    def clearLayout(self, layout):
        self.featuresListWidget.clear()
        self.setWidget.clear()
        self.paramsListWidget.clear()
        self.findParamsListWidget.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = Model()
    window = StartWindow(model)
    window.show()
    app.exit(app.exec_())
