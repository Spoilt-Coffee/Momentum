import sys

from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton

class Fitness(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  # Remove outer margins
        layout.setSpacing(0)  # Remove space between widgets

        # Create sidebar and main content widgets
        sidebar_widget = QWidget()
        main_content_widget = QWidget()
        
        sidebar_widget.setStyleSheet("background-color: rgb(40, 41, 64);")
        main_content_widget.setStyleSheet("background-color: rgb(30, 30, 51);")

        # Set up sidebar layout
        sidebar_layout = QVBoxLayout(sidebar_widget)
        self.button = QPushButton("Dashboard", self)
        self.button.setFixedSize(200, 100)
        sidebar_layout.addWidget(self.button)

        # Add both widgets to main layout with stretch factors
        layout.addWidget(sidebar_widget)
        layout.addWidget(main_content_widget)
        layout.setStretchFactor(sidebar_widget, 1)   # 20% of space
        layout.setStretchFactor(main_content_widget, 4)  # 80% of space
