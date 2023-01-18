import sys
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.text_label = QLabel("---")
        label = QLabel("Name: ")
        self.name_input = QLineEdit()
        button = QPushButton("Set name")
        button.clicked.connect(self.alterName)


        hori = QHBoxLayout()
        # hori.addStretch(1)
        hori.addWidget(label)
        hori.addWidget(self.name_input)

        verti = QVBoxLayout()
        verti.addWidget(self.text_label)
        verti.addLayout(hori)
        verti.addWidget(button)
        verti.addStretch()

        self.setLayout(verti)
        # self.setWindowTitle("horizontal layout")
        self.setWindowTitle("Nothing has been clicked")
        self.show()

    def alterName(self): 
        self.text_label.setText(self.name_input.text())
        self.setWindowTitle(self.name_input.text() + "'s window")

    # def clickedButton(self):
    #     print( "Button click" )
    #     self.setWindowTitle("can i do this?")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())