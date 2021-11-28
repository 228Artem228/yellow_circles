import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor
from random import randint


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Кнопка', self)
        self.setGeometry(100, 100, 1500, 900)
        self.setWindowTitle('Первая программа')
        self.btn.resize(150, 150)
        self.btn.move(1300, 1)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_okr(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_okr(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        i = randint(0, 750)
        qp.drawEllipse(200, 150, i, i)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
