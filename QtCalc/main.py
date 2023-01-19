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

        self.disp = QLineEdit()
        self.disp.setReadOnly(True)
        self.disp.setAlignment(Qt.AlignmentFlag(2))

        buttNames = [1, 2, 3, "+", 4, 5, 6, "-", 7, 8, 9, "*", 0, ".", "=", "/"]
        buttons = []

        row = 0
        col = 0

        for buttName in buttNames:
            # Create button
            b = QPushButton(str(buttName))

            # Connect a function
            if buttName != "=":
                print(str(buttName), "created", b.text())
                b.clicked.connect(lambda: self.addChar(b, buttName))
            else:
                b.clicked.connect(self.calculate)

            b.click()

            # Add to list of buttons (though not needed anymore?)
            buttons.append(b)

            # Place buttons on a grid
            if col > 3:
                col = 0
                row += 1

            buttGrid.addWidget(b, row, col)

            col += 1

        # for butt in buttons:
            # butt.click()
            # butt.clicked.connect(lambda: self.addChar(butt, butt.text()))
            # butt.click()


        # button1 = QPushButton("1")
        # button2 = QPushButton("2")
        # button3 = QPushButton("3")
        # button4 = QPushButton("4")
        # button5 = QPushButton("5")
        # button6 = QPushButton("6")
        # button7 = QPushButton("7")
        # button8 = QPushButton("8")
        # button9 = QPushButton("9")
        # button0 = QPushButton("0")
        # buttonP = QPushButton(".")

        # button1.clicked.connect(lambda: self.addChar(button1))

        # buttonAdd = QPushButton("+")
        # buttonSub = QPushButton("-")
        # buttonDiv = QPushButton("/")
        # buttonMul = QPushButton("X")
        # buttonCalc = QPushButton("=")

        # buttGrid.addWidget(button1, 0, 0)
        # buttGrid.addWidget(button2, 0, 1)
        # buttGrid.addWidget(button3, 0, 2)
        # buttGrid.addWidget(buttonAdd, 0, 3)
        # buttGrid.addWidget(button4, 1, 0)
        # buttGrid.addWidget(button5, 1, 1)
        # buttGrid.addWidget(button6, 1, 2)
        # buttGrid.addWidget(buttonSub, 1, 3)
        # buttGrid.addWidget(button7, 2, 0)
        # buttGrid.addWidget(button8, 2, 1)
        # buttGrid.addWidget(button9, 2, 2)
        # buttGrid.addWidget(buttonMul, 2, 3)
        # buttGrid.addWidget(button0, 3, 0)
        # buttGrid.addWidget(buttonP, 3, 1)
        # buttGrid.addWidget(buttonCalc, 3, 2)
        # buttGrid.addWidget(buttonDiv, 3, 3)
        
        calclayout.addWidget(self.disp)
        calclayout.addLayout(buttGrid)

        self.setLayout(calclayout)

        # self.show()

    def addChar(self, clickedbutton, buttonText):
        self.disp.setText(str(self.disp.text()) + str(clickedbutton.text()))
    
    def calculate(self):
        print("Should calculate: ", self.disp.text())




if(__name__ == "__main__"):
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec())