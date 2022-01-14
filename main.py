import sys

from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog


class Example(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.initUI()

    def initUI(self) -> None:
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event) -> None:
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def paint(self) -> None:
        self.do_paint = True
        self.repaint()

    def draw(self, qp) -> None:
        count = randint(2, 6)
        p = QPen(QColor(255, 255, 0), 2)
        qp.setPen(p)
        for i in range(count):
            d = randint(30, 200)
            x = randint(d + 5, self.width() - d - 5)
            y = randint(d + 5, self.height() - d - 5)
            qp.drawEllipse(x, y, d / 2, d / 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
