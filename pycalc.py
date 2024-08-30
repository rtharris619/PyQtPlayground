import sys
from functools import partial

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

ERROR_MSG = "ERROR"
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


def evaluate_expression(expression: str):
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG
    return result


class Calc:
    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connect_signals_and_slots()

    def _calculate_result(self):
        result = self._evaluate(expression=self._view.display_text())
        self._view.set_display_text(result)

    def _build_expression(self, sub_expression):
        if self._view.display_text() == ERROR_MSG:
            self._view.clear_display()
        expression = self._view.display_text() + sub_expression
        self._view.set_display_text(expression)

    def _connect_signals_and_slots(self):
        for key_symbol, button in self._view.button_map.items():
            if key_symbol not in {"=", "C"}:
                button.clicked.connect(
                    partial(self._build_expression, key_symbol)
                )
        self._view.button_map["="].clicked.connect(self._calculate_result)
        self._view.display.returnPressed.connect(self._calculate_result)
        self._view.button_map["C"].clicked.connect(self._view.clear_display)


def main():
    app = QApplication([])
    window = CalcWindow()
    window.show()

    Calc(model=evaluate_expression, view=window)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
