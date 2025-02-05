from PyQt6.QtWidgets import QMainWindow, QApplication, QGridLayout, QPushButton, QSpacerItem, QSizePolicy, QWidget


class UI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Git and Random Circles')
        self.setBaseSize(500, 350)
        self.layout = QGridLayout()

        self.spacer_top = QSpacerItem(
            20, 100, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.button = QPushButton('Нажми меня')
        self.spacer_bottom = QSpacerItem(
            20, 100, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.layout.addItem(self.spacer_top, 0, 0)
        self.layout.addWidget(self.button, 1, 0)
        self.layout.addItem(self.spacer_bottom, 2, 0)

        # Устанавливаем макет для центрального виджета
        central_widget = self.centralWidget()
        if central_widget is None:
            central_widget = QWidget()
            self.setCentralWidget(central_widget)
        central_widget.setLayout(self.layout)
