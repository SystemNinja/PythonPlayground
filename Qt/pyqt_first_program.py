"""
https://doc.qt.io/qtforpython/?hsCtaTracking=464a02ec-f9fd-40ba-aa60-8ec24b6a0016%7Cd3b1d1a7-49c6-4f79-91b8-2a4d35c64ac2
Demonstration of the PyQt library
https://doc.qt.io/qtforpython/quickstart.html

@CtCore.Slot()
Explanation: https://www.tutorialspoint.com/pyqt/pyqt_signals_and_slots.htm
"""
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me.")
        self.text = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    # @QtCore.Slot() # I have no fucking idea what this does...
    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800,600)
    widget.show()

    sys.exit(app.exec())