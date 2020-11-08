from main import calcul as main_calcul
from PySide2 import QtWidgets, QtCore, QtGui


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Théoreme Pythagore")
        self.setup_ui()
        self.resize(525, 425)

    def setup_ui(self):
        self.create_widget()
        self.create_layouts()
        self.modify_widgets()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widget(self):
        self.labelUnit = QtWidgets.QLabel("Entrer l'unité des longueurs du triangle")
        self.entryUnit = QtWidgets.QLineEdit()

        self.labelNameTriangle = QtWidgets.QLabel("Entrer le nom du triangle rectangle")
        self.entryNameTriangle = QtWidgets.QLineEdit()

        self.labelRightAngle = QtWidgets.QLabel("Entrer le nom du sommet de l'angle droit")
        self.entryRightAngle = QtWidgets.QLineEdit()

        self.labelLenghtSide1 = QtWidgets.QLabel("Entrer la longueur du premier côté de l'angle droit")
        self.entryLenghtSide1 = QtWidgets.QLineEdit()

        self.labelLenghtSide2 = QtWidgets.QLabel("Entrer la longueur du deuxieme côté de l'angle droit")
        self.entryLenghtSide2 = QtWidgets.QLineEdit()

        self.btnCalcul = QtWidgets.QPushButton("calculer la longueur de l'hypothenuse")
        self.labelCalculResult = QtWidgets.QLabel("")

    def modify_widgets(self):
        self.labelCalculResult.setAlignment(QtCore.Qt.AlignHCenter)
        self.labelCalculResult.setMargin(10)

    def create_layouts(self):
        self.mainLayout = QtWidgets.QVBoxLayout(self)

        self.entryLayout = QtWidgets.QGridLayout()
        self.resultLayout = QtWidgets.QVBoxLayout()

    def add_widgets_to_layouts(self):
        self.mainLayout.addLayout(self.entryLayout)
        self.mainLayout.addLayout(self.resultLayout)

        self.entryLayout.addWidget(self.labelUnit, 0, 0, 1, 1)
        self.entryLayout.addWidget(self.entryUnit, 0, 1, 1, 1)
        self.entryLayout.addWidget(self.labelNameTriangle, 1, 0, 1, 1)
        self.entryLayout.addWidget(self.entryNameTriangle, 1, 1, 1, 1)
        self.entryLayout.addWidget(self.labelRightAngle, 2, 0, 1, 1)
        self.entryLayout.addWidget(self.entryRightAngle, 2, 1, 1, 1)
        self.entryLayout.addWidget(self.labelLenghtSide1, 3, 0, 1, 1)
        self.entryLayout.addWidget(self.entryLenghtSide1, 3, 1, 1, 1)
        self.entryLayout.addWidget(self.labelLenghtSide2, 4, 0, 1, 1)
        self.entryLayout.addWidget(self.entryLenghtSide2, 4, 1, 1, 1)

        self.resultLayout.addWidget(self.btnCalcul)
        self.resultLayout.addWidget(self.labelCalculResult)

    def setup_connections(self):
        self.btnCalcul.clicked.connect(self.calcul)

    def calcul(self):
        self.unit = self.entryUnit.text()
        self.nameTriangle = self.entryNameTriangle.text()
        self.rightAngle = self.entryRightAngle.text()
        self.lenghtSide1 = self.entryLenghtSide1.text()
        self.lenghtSide2 = self.entryLenghtSide2.text()
        self.labelCalculResult.setText(main_calcul(self.unit, self.nameTriangle, self.rightAngle, self.lenghtSide1, self.lenghtSide2))
        print(self.geometry())

    def not_units(self):
        # afficher pop up danger
        pass

    def not_digits(self):
        # afficher pop up danger
        pass


app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()
