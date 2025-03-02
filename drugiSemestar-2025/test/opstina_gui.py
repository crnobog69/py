import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QGroupBox,
)


class OpstinaProzor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Проверa карактера")
        self.setGeometry(100, 100, 600, 500)  # x, y

        # Main widget and layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        input_group = QGroupBox("Унос реченице")
        input_layout = QVBoxLayout()

        self.recenica_input = QLineEdit()
        input_layout.addWidget(QLabel("Унесите реченицу:"))
        input_layout.addWidget(self.recenica_input)

        input_group.setLayout(input_layout)
        main_layout.addWidget(input_group)

        buttons_group = QGroupBox("Опције провере")
        buttons_layout = QVBoxLayout()

        self.btn_ime_datoteke = QPushButton(
            "Провери за ИМЕ ДАТОТЕКЕ (лимит: 20 карактера)"
        )
        self.btn_tekuci_racun = QPushButton(
            "Провери за БРОЈ ТЕКУЋЕГ РАЧУНА (лимит: 18 карактера)"
        )
        self.btn_jmbg = QPushButton(
            "Провери за ЈЕДИНСТВЕНИ МАТИЧНИ БРОЈ ГРАЂАНА (лимит: 13 карактера)"
        )
        self.btn_plata = QPushButton("Провери за ПЛАТА (лимит: 23 карактера)")
        self.btn_ukupno = QPushButton("Провери УКУПНО (лимит: 136 карактера)")

        self.btn_ime_datoteke.clicked.connect(
            lambda: self.proveri_limit(20, "ИМЕ ДАТОТЕКЕ")
        )
        self.btn_tekuci_racun.clicked.connect(
            lambda: self.proveri_limit(18, "БРОЈ ТЕКУЋЕГ РАЧУНА")
        )
        self.btn_jmbg.clicked.connect(
            lambda: self.proveri_limit(13, "ЈЕДИНСТВЕНИ МАТИЧНИ БРОЈ ГРАЂАНА")
        )
        self.btn_plata.clicked.connect(lambda: self.proveri_limit(23, "ПЛАТА"))
        self.btn_ukupno.clicked.connect(lambda: self.proveri_limit(136, "УКУПНО"))

        buttons_layout.addWidget(self.btn_ime_datoteke)
        buttons_layout.addWidget(self.btn_tekuci_racun)
        buttons_layout.addWidget(self.btn_jmbg)
        buttons_layout.addWidget(self.btn_plata)
        buttons_layout.addWidget(self.btn_ukupno)

        buttons_group.setLayout(buttons_layout)
        main_layout.addWidget(buttons_group)

        result_group = QGroupBox("Резултат провере")
        result_layout = QVBoxLayout()

        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        result_layout.addWidget(self.result_text)

        result_group.setLayout(result_layout)
        main_layout.addWidget(result_group)

    def proveri_limit(self, limit, naslov):
        """Proverava broj karaktera u recenici u odnosu na limit i prikazuje rezultat."""
        recenica = self.recenica_input.text()
        broj_karaktera = len(recenica)
        preostalo = limit - broj_karaktera

        result = f"{'-' * 40}\n"
        result += f"{naslov:^40}\n\n"
        result += f'Унета реченица: "{recenica}"\n'
        result += f"Број карактера: {broj_karaktera}\n"

        if broj_karaktera <= limit:
            result += f"Преостало до лимита: {preostalo} карактера\n"
        else:
            result += f"Прекорачење лимита за: {abs(preostalo)} карактера\n"

        result += f"{'-' * 40}"

        self.result_text.setText(result)


def main():
    app = QApplication(sys.argv)
    window = OpstinaProzor()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
