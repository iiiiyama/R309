import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QLineEdit, QComboBox, QPushButton, QGridLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        grid = QGridLayout()

        widget.setLayout(grid)

        self.__lab1 = QLabel("température")
        self.__text = QLineEdit("")
        self.__lab2 = QLabel("°C")
        self.__conv = QComboBox()
        self.__conv.addItems(["°C -> K", "K -> °C"])
        conver = QPushButton("Convertir")
        self.__conv.currentIndexChanged.connect(self.__selectionchange)
        self.__lab3 = QLabel("conversion")
        self.__lab4 = QLabel("K")
        grid.addWidget(self.__lab1, 0, 0)
        grid.addWidget(self.__text, 0, 1)
        grid.addWidget(self.__lab2, 0, 2)
        grid.addWidget(conver, 1, 1)
        grid.addWidget(self.__conv, 1, 3)
        grid.addWidget(self.__lab3, 2, 0)
        grid.addWidget(self.__lab4, 2, 3)

        #aide = QPushButton("?")
        #textaide = "permet de convertir un nombre soit des Kelvins vers Celsius ou Celsius vers Kelvin "
        #aide.show(textaide)


    def __selectionchange(self):

        if self.__conv.currentIndexChanged:
            self.__lab2.setText("K")
            self.__lab4.setText("°C")
        else:
            self.__lab4.setText("K")
            self.__lab2.setText("°C")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()