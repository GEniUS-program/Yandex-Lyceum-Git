import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QRect
from PyQt6 import uic


class CircleWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self = uic.load_ui.loadUi(
            "Git and yellow circles\\UI.ui", baseinstance=self)
        self.circles = []

        self.button.clicked.connect(self.add_circle)

    def add_circle(self):
        diameter = random.randint(20, min(self.width(), self.height()))
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)

        self.circles.append((x, y, diameter))

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(255, 255, 0))

        for x, y, diameter in self.circles:
            painter.drawEllipse(QRect(x, y, diameter, diameter))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircleWidget()
    window.show()
    sys.exit(app.exec())
