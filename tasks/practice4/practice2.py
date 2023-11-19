import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFormLayout, QSlider, \
    QLineEdit, QPushButton, QRadioButton, QGroupBox, QComboBox, QMessageBox, QTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)

        form_layout = QFormLayout()

        self.height_slider = QSlider()
        self.height_slider.setMinimum(140)
        self.height_slider.setMaximum(230)
        self.height_slider.setTickInterval(10)
        self.height_slider.setTickPosition(QSlider.TicksAbove)
        self.height_slider.setValue(140)
        form_layout.addRow(QLabel("Рост"), self.height_slider)

        self.weight_slider = QSlider()
        self.weight_slider.setMinimum(35)
        self.weight_slider.setMaximum(200)
        self.weight_slider.setTickInterval(5)
        self.weight_slider.setTickPosition(QSlider.TicksAbove)
        self.weight_slider.setValue(35)
        form_layout.addRow(QLabel("Вес"), self.weight_slider)

        self.gender_group = QGroupBox("Пол")
        gender_layout = QHBoxLayout()
        self.male_radio = QRadioButton("М")
        self.female_radio = QRadioButton("Ж")
        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)
        self.gender_group.setLayout(gender_layout)
        form_layout.addRow(self.gender_group)

        self.age_edit = QLineEdit()
        form_layout.addRow(QLabel("Возраст"), self.age_edit)

        self.name_edit = QLineEdit()
        form_layout.addRow(QLabel("Имя"), self.name_edit)

        self.surname_edit = QLineEdit()
        form_layout.addRow(QLabel("Фамилия"), self.surname_edit)

        self.patronymic_edit = QLineEdit()
        form_layout.addRow(QLabel("Отчество"), self.patronymic_edit)

        self.profession_combo = QComboBox()
        self.profession_combo.addItems(["Программист", "Менеджер", "Учитель"])
        form_layout.addRow(QLabel("Род деятельности"), self.profession_combo)

        self.marital_status_group = QGroupBox("Семейное положение")
        marital_status_layout = QHBoxLayout()
        self.single_radio = QRadioButton("Свободен/на")
        self.in_relationship_radio = QRadioButton("В отношениях")
        marital_status_layout.addWidget(self.single_radio)
        marital_status_layout.addWidget(self.in_relationship_radio)
        self.marital_status_group.setLayout(marital_status_layout)
        form_layout.addRow(self.marital_status_group)

        save_button = QPushButton("Сохранить")
        save_button.clicked.connect(self.save_data)
        form_layout.addRow(save_button)

        layout.addLayout(form_layout)
        self.setLayout(layout)

    def save_data(self):
        data = {}
        data["Рост"] = self.height_slider.value()
        data["Вес"] = self.weight_slider.value()
        data["Пол"] = "М" if self.male_radio.isChecked() else "Ж"
        data["Возраст"] = self.age_edit.text()
        data["Имя"] = self.name_edit.text()
        data["Фамилия"] = self.surname_edit.text()
        data["Отчество"] = self.patronymic_edit.text()
        data["Род деятельности"] = self.profession_combo.currentText()
        data["Семейное положение"] = "Свободен/на" if self.single_radio.isChecked() else "В отношениях"

        with open("data.txt", "w") as file:

            for key, value in data.items():
                file.write(f"{key}: {value}\n")

        QMessageBox.information(self, "Успех", "Данные сохранены в файл data.txt")

class SecondWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Окно для просмотра файла")
        self.setGeometry(100, 100, 400, 300)

        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.load_data()

    def load_data(self):
        try:
            with open("data.txt", "r") as file:
                data = file.read()
                self.text_edit.setText(data)
        except FileNotFoundError:
            self.text_edit.setText("Файл не найден")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    second_window = SecondWindow()
    second_window.show()

    sys.exit(app.exec_())
