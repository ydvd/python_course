from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Page(QWidget):
    def __init__(self, parent=None):
        super(Page, self).__init__(parent)

        mylabel = QLabel("this is a label")
        layout = QVBoxLayout()

        layout.addWidget(mylabel)

        mainLayout = QGridLayout()
        mainLayout.addLayout(layout, 0, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("qt app")

if __name__ == "__main__":
    import sys
    
    app = QApplication(sys.argv)
    window = Page()
    window.show()

    sys.exit(app.exec_())