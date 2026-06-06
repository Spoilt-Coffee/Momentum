import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from frontend.ui.dashboard import Dashboard
from frontend.ui.fitness import Fitness

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1025, 901)
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        self.setWindowTitle("Momentum")

        self.dashboard = Dashboard()
        self.fitness = Fitness()

        self.stacked_widget.addWidget(self.dashboard)
        self.stacked_widget.addWidget(self.fitness)

        # Connect button clicks to switch screens
        self.fitness.button.clicked.connect(
            lambda: self.stacked_widget.setCurrentWidget(self.dashboard)
        )
        self.dashboard.button.clicked.connect(
            lambda: self.stacked_widget.setCurrentWidget(self.fitness)
        )

if __name__ == "__main__":
    """Entry point for the application."""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.move(100, 100)
    window.show()
    app.exec()
