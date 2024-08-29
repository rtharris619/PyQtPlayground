import sys
from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
)


class Window(QDialog):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("QDialog")

        dialog_layout = QVBoxLayout()
        form_layout = QFormLayout()

        form_layout.addRow("Name:", QLineEdit())
        form_layout.addRow("Age:", QLineEdit())
        form_layout.addRow("Job:", QLineEdit())
        form_layout.addRow("Hobbies:", QLineEdit())
        dialog_layout.addLayout(form_layout)

        buttons = QDialogButtonBox()
        buttons.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel |
            QDialogButtonBox.StandardButton.Ok
        )
        dialog_layout.addWidget(buttons)
        self.setLayout(dialog_layout)


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
