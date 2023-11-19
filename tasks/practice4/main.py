import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtGui import QPalette, QColor
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

        # Настройка стилей кнопок
        self.set_button_style()

    def set_button_style(self):
        buttons = self.findChildren(QPushButton)
        for button in buttons:
            button.setFixedSize(50, 50)
            button.setStyleSheet("""
                QPushButton {
                    background-color: #F0F0F0;
                    border: 1px solid #CCCCCC;
                    border-radius: 5px;
                    font-size: 16px;
                }

                QPushButton:hover {
                    background-color: #E0E0E0;
                }

                QPushButton:pressed {
                    background-color: #D0D0D0;
                }
            """)

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


    palette = QPalette()
    palette.setColor(QPalette.Button, QColor("#F0F0F0"))
    palette.setColor(QPalette.ButtonText, QColor("#000000"))
    palette.setColor(QPalette.Base, QColor("#F0F0F0"))
    app.setPalette(palette)

    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
