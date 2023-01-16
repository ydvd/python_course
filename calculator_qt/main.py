import sys
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        label = QLabel("Name: ")
        name_input = QLineEdit()
        button = QPushButton("Set name")

        hori = QHBoxLayout()
        # hori.addStretch(1)
        hori.addWidget(label)
        hori.addWidget(name_input)

        verti = QVBoxLayout()
        verti.addLayout(hori)
        verti.addWidget(button)
        verti.addStretch()

        self.setLayout(verti)
        self.setWindowTitle("horizontal layout")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())