import sys
from PyQt6.QtWidgets import (
    QApplication, QLabel, QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QGridLayout, QFormLayout, QLineEdit
)


def hello_world():
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("PyQt App")
    window.setGeometry(100, 100, 280, 80)
    helloMsg = QLabel("<h1>Hello World!</h1>", parent=window)
    helloMsg.move(60, 15)

    window.show()
    sys.exit(app.exec())


def horizontal_layout():
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("QHBoxLayout")

    layout = QHBoxLayout()
    layout.addWidget(QPushButton("Left"))
    layout.addWidget(QPushButton("Center"))
    layout.addWidget(QPushButton("Right"))
    window.setLayout(layout)

    window.show()
    sys.exit(app.exec())


def vertical_layout():
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("QVBoxLayout")

    layout = QVBoxLayout()
    layout.addWidget(QPushButton("Top"))
    layout.addWidget(QPushButton("Center"))
    layout.addWidget(QPushButton("Bottom"))
    window.setLayout(layout)

    window.show()
    sys.exit(app.exec())


def grid_layout():
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("QGridLayout")

    layout = QGridLayout()
    layout.addWidget(QPushButton("Button (0, 0)"), 0, 0)
    layout.addWidget(QPushButton("Button (0, 1)"), 0, 1)
    layout.addWidget(QPushButton("Button (0, 2)"), 0, 2)
    layout.addWidget(QPushButton("Button (1, 0)"), 1, 0)
    layout.addWidget(QPushButton("Button (1, 1)"), 1, 1)
    layout.addWidget(QPushButton("Button (1, 2)"), 1, 2)
    layout.addWidget(QPushButton("Button (2, 0)"), 2, 0)
    layout.addWidget(QPushButton("Button (2, 1) + 2 col-span"), 2, 1, 1, 2)

    window.setLayout(layout)

    window.show()
    sys.exit(app.exec())


def form_layout():
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("QFormLayout")

    layout = QFormLayout()
    layout.addRow("Name:", QLineEdit())
    layout.addRow("Age:", QLineEdit())
    layout.addRow("Job:", QLineEdit())
    layout.addRow("Hobbies:", QLineEdit())
    window.setLayout(layout)

    window.show()
    sys.exit(app.exec())


form_layout()

# https://realpython.com/python-pyqt-gui-calculator/#dialogs
