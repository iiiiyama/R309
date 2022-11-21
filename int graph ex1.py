import sys
from PyQt5.QtWidgets import QApplication, QWidget

def __init__(self):
    super().__init__()
    widget = QWidget()
    self.setCentralWidget(widget)
    grid = QGridLayout()
    widget.setLayout(grid)
    app = QApplication(sys.argv)
    root = QWidget()
    root.resize(300, 200)
    root.setWindowTitle("exercice 1")
    root.show()
    grid = QGridLayout()
    root.setLayout(grid)









if __name__ == '__main__':
sys.exit(app.exec_())