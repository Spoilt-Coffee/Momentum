import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from database.db_connection import init_database

class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Page2")
        self.setMinimumSize(1200, 800)
        self.setStyleSheet("background-color: red;")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Momentum")
        self.setMinimumSize(1200, 800)
        self.setStyleSheet("background-color: rgb(32, 35, 52);")

        self.secondwindow = AnotherWindow()

        central = QWidget()
        layout = QVBoxLayout(central)

        self.button = QPushButton("Start")
        self.button.clicked.connect(self.show_new_window)

        layout.addWidget(self.button)
        self.setCentralWidget(central)

    def show_new_window(self, _):
        self.secondwindow.show()

if __name__ == "__main__":
    init_database()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())