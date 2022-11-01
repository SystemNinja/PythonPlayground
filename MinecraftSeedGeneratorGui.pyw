import random
import string
import sys

from PySide6 import QtCore, QtWidgets, QtGui

class SeedGenerator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__() # this one is only useful when dealing with methods
        self.label = QtWidgets.QLabel("To generate seed click on this --> ")
        self.label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.button = QtWidgets.QPushButton("Generate Seed")
        # self.checkbox1 = QtWidgets.QCheckBox("Test1")
        # self.checkbox2 = QtWidgets.QCheckBox("Test2")

        # self.layout2 = QtWidgets.QHBoxLayout(self)
        # self.layout2.addWidget(self.checkbox1)
        # self.layout2.addWidget(self.checkbox2)

        self.layout1 = QtWidgets.QVBoxLayout(self)
        self.layout1.addWidget(self.label)
        self.layout1.addWidget(self.button)

        self.button.clicked.connect(self.generate)

    # @QtCore.Slot() # If having multiple methods, not fully sure of the use yet
    def generate(self):
        seed_length = random.randint(6, 66)
        alphabet = string.ascii_letters + string.digits
        result = str(random.choices(alphabet, k=seed_length)).replace("[", "").replace("]", "").replace(",","").replace(" ", "").replace("'", "")
        self.label.setText(result)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = SeedGenerator()
    widget.setWindowTitle("Minecraft Seed Generator")
    widget.setFixedSize(700,150)
    widget.show()

    sys.exit(app.exec())
