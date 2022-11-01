"""
PyQt ref:
https://doc.qt.io/qtforpython/contents.html
PyQt modules
https://doc.qt.io/qtforpython/api.html
"""

import json
import random
import sys
import os

import pyperclip  # Library for copy/pasting text to clipboard
from PySide6 import QtCore, QtWidgets, QtGui

class PassGen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # configure label
        self.label = QtWidgets.QLabel("Click button to generate password -->")
        # Allow label text to be selected
        # Flag responsible for this TextSelectableByMouse
        # Documentation is confusing as fuck
        self.label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        # configure button
        self.button = QtWidgets.QPushButton("Generate Password")
        # Create layout that will place widgets horizontally
        self.layout = QtWidgets.QHBoxLayout(self)

        # Add gui elements using layout defined above
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        # When button is clicked execute method
        self.button.clicked.connect(self.generate_password)

    def generate_password(self):
        cwd = os.getcwd() # get current working directory
        cwd1 = sys.path[0]
        # word_list = json.load(open(cwd+"\words_dictionary.json")) 
        word_list = json.load(open(str(cwd1)+"/words_dictionary.json"))
        # all words are listed as keys with value 1
        # convert dict obtained from JSON to list which allows iteration using numbers
        words = list(word_list)
        symbols = ['!', '@', '#', '$']
        # Take random word from JSON file
        # Word range can begin at 13, first 12 words can be skipped as they are meaningless
        word = random.randint(13, len(words) - 1)
        # get random number
        number = str(random.randint(0, 99))
        # Capitalize first letter of the word and combine it with random number and a symbol
        result = words[word].capitalize() + number + symbols[random.randint(0, len(symbols) - 1)]
        # Copy result to clipboard
        pyperclip.copy(result)
        # Update label value
        self.label.setText(result)
        # print(result)
        # print(len(result))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = PassGen()
    # set window title
    widget.setWindowTitle("Password Generator")
    widget.show()

    sys.exit(app.exec())
