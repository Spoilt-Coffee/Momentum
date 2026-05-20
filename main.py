import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from frontend.ui.startscreen import Startscreen
from frontend.ui.workoutscreen import Workoutscreen

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        self.setWindowTitle("Momentum")
        
        self.start_screen = Startscreen()
        self.workout_screen = Workoutscreen()
        
        self.stacked_widget.addWidget(self.start_screen)
        self.stacked_widget.addWidget(self.workout_screen)
        
        # Connect button clicks
        self.start_screen.button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.workout_screen))
        self.workout_screen.button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.start_screen))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.move(100, 100)   
    window.show()
    app.exec()
