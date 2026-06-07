import sys
from PyQt6.QtWidgets import QApplication, QWidget, QStackedWidget, QHBoxLayout, QVBoxLayout, QPushButton
from frontend.ui.dashboard import Dashboard
from frontend.ui.fitness import Fitness

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1025, 901)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  # Remove outer margins
        layout.setSpacing(0)  # Remove space between widgets

        # Create sidebar and main content widgets
        self.sidebar_widget = QWidget()
        self.content_widget = QStackedWidget()
        
        self.sidebar_widget.setObjectName("sidebar_widget")
        self.content_widget.setObjectName("content_widget")

        layout.addWidget(self.sidebar_widget)
        layout.addWidget(self.content_widget)
        layout.setStretchFactor(self.sidebar_widget, 1)
        layout.setStretchFactor(self.content_widget, 4)
        
        self.setWindowTitle("Momentum")

        self.dashboard = Dashboard()
        self.fitness = Fitness()

        self.content_widget.addWidget(self.dashboard)
        self.content_widget.addWidget(self.fitness)

        self.dashboard_button = QPushButton("dashboard", self)
        self.fitness_button = QPushButton("Fitness", self)

        self.dashboard_button.setObjectName("sidebar_button")
        self.fitness_button.setObjectName("sidebar_button")

        self.dashboard_button.setMinimumSize(50,30)
        self.fitness_button.setMinimumSize(50,30)

        sidebar_layout = QVBoxLayout(self.sidebar_widget)
        sidebar_layout.addWidget(self.dashboard_button)
        sidebar_layout.addWidget(self.fitness_button)


def load_stylesheet(app):
    with open("style.qss", "r") as file:
        app.setStyleSheet(file.read())

if __name__ == "__main__":
    """Entry point for the application."""
    app = QApplication(sys.argv)
    load_stylesheet(app)
    window = MainWindow()
    window.move(100, 100)
    window.show()
    app.exec()
