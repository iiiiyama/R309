import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        root = QWidget()
        root.resize(400, 300)

        grid = QVBoxLayout()
        widget.setLayout(grid)

        self.__lab = QLabel("Saisir votre nom")
        self.__text = QLineEdit("")
        self.__rep = QLabel("")
        ok = QPushButton("Ok")
        quit = QPushButton("Quitter")

        grid.addWidget(self.__lab)
        grid.addWidget(self.__text)
        grid.addWidget(ok)
        grid.addWidget(self.__rep)

        grid.addWidget(quit)

        ok.clicked.connect(self.__actionOk)
        quit.clicked.connect(self.__actionQuitter)
        self.setWindowTitle("welcome")

    def __actionOk(self):
        self.__rep.setText(f"bonjour {self.__text.text()}")


    def __actionQuitter(self):
        QCoreApplication.exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()