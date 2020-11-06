from main import calcul
from PySide2 import QtWidgets


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Théoreme Pythagore")
        self.setup_ui()
        self.setup_connections()

    def setup_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.labelText = QtWidgets.QLabel("hello world")
        self.main_layout.addWidget(self.labelText)

    def setup_connections(self):
        pass

app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()
