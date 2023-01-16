import sys
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QLabel



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        label = QLabel("This is a label")
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hori = QHBoxLayout()
        hori.addStretch(1)
        hori.addWidget(okButton)
        hori.addWidget(cancelButton)

        verti = QVBoxLayout()
        verti.addWidget(label)
        verti.addStretch()
        verti.addLayout(hori)

        self.setLayout(verti)
        self.setWindowTitle("horizontal layout")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())