import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QtCalc")
        self.buildInterface()
        self.show()

    def buildInterface(self):
        calclayout = QVBoxLayout()
        buttGrid = QGridLayout()

        button1 = QPushButton("1")
        button2 = QPushButton("2")
        button3 = QPushButton("3")
        button4 = QPushButton("4")
        button5 = QPushButton("5")
        button6 = QPushButton("6")
        button7 = QPushButton("7")
        button8 = QPushButton("8")
        button9 = QPushButton("9")
        button0 = QPushButton("0")
        buttonP = QPushButton(".")

        buttonAdd = QPushButton("+")
        buttonSub = QPushButton("-")
        buttonDiv = QPushButton("/")
        buttonMul = QPushButton("X")
        buttonCalc = QPushButton("=")

        buttGrid.addWidget(button1, 0, 0)
        buttGrid.addWidget(button2, 0, 1)
        buttGrid.addWidget(button3, 0, 2)
        buttGrid.addWidget(buttonAdd, 0, 3)
        buttGrid.addWidget(button4, 1, 0)
        buttGrid.addWidget(button5, 1, 1)
        buttGrid.addWidget(button6, 1, 2)
        buttGrid.addWidget(buttonSub, 1, 3)
        buttGrid.addWidget(button7, 2, 0)
        buttGrid.addWidget(button8, 2, 1)
        buttGrid.addWidget(button9, 2, 2)
        buttGrid.addWidget(buttonMul, 2, 3)
        buttGrid.addWidget(button0, 3, 0)
        buttGrid.addWidget(buttonP, 3, 1)
        buttGrid.addWidget(buttonCalc, 3, 2)
        buttGrid.addWidget(buttonDiv, 3, 3)
        
        disp = QLineEdit()
        disp.setReadOnly(True)

        calclayout.addWidget(disp)
        calclayout.addLayout(buttGrid)

        self.setLayout(calclayout)

        # self.show()

if(__name__ == "__main__"):
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec())