import sys
from functools import partial

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class Window(QWidget):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Signals and Slots")

        self.layout = QVBoxLayout()

        self.button = QPushButton("Greet")
        self.button.clicked.connect(partial(self.greet, "Ryan"))

        self.layout.addWidget(self.button)

        self.msg_label = QLabel("")
        self.layout.addWidget(self.msg_label)

        self.setLayout(self.layout)

    def greet(self, name):
        if self.msg_label.text():
            self.msg_label.setText("")
        else:
            self.msg_label.setText(f"Hello, {name}")


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
    