import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class Startscreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(1500,900) 
        layout = QVBoxLayout(self)

        self.button = QPushButton("Go to workoutscreen", self)
        self.button.setFixedSize(200,100)
        layout.addWidget(self.button)
