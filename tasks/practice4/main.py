import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtCore import Qt


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.layout = QVBoxLayout()

        self.result_field = QLineEdit()
        self.result_field.returnPressed.connect(self.calculate)
        self.layout.addWidget(self.result_field)

        buttons_layout = QGridLayout()

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        row, col = 0, 0
        for button in buttons:
            button_obj = QPushButton(button)
            button_obj.clicked.connect(self.button_clicked)
            buttons_layout.addWidget(button_obj, row, col)

            col += 1
            if col > 3:
                col = 0
                row += 1

        self.layout.addLayout(buttons_layout)
        self.setLayout(self.layout)

    def button_clicked(self):
        button = self.sender()
        current_text = self.result_field.text()

        if button.text() == "=":
            self.calculate()
        else:
            self.result_field.setText(current_text + button.text())

    def calculate(self):
        current_text = self.result_field.text()
        try:
            result = eval(current_text)
            self.result_field.setText(str(result))
        except:
            self.result_field.setText("Error")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
