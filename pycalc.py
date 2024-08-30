import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

WINDOW_SIZE = 235
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 40


class CalcWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.general_layout = QVBoxLayout()
        central_widget = QWidget(self)
        central_widget.setLayout(self.general_layout)
        self.setCentralWidget(central_widget)

        self._create_display()
        self._create_buttons()

    def _create_display(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.general_layout.addWidget(self.display)

    def _create_buttons(self):
        self.button_map = {}
        buttons_layout = QGridLayout()
        keyboard = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", "00", ".", "+", "="],
        ]

        for row, keys in enumerate(keyboard):
            for col, key in enumerate(keys):
                self.button_map[key] = QPushButton(key)
                self.button_map[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                buttons_layout.addWidget(self.button_map[key], row, col)

        self.general_layout.addLayout(buttons_layout)

    def set_display_text(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def display_text(self):
        return self.display.text()

    def clear_display(self):
        self.display.setText("")


def main():
    app = QApplication([])
    window = CalcWindow()
    window.show()

    window.set_display_text("100")

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
