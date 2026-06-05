"""
Main application module for Momentum.

This module initializes the PyQt6 application, creates the main window,
and manages screen switching between the start screen and workout screen.
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from frontend.ui.startscreen import Startscreen
from frontend.ui.workoutscreen import Workoutscreen


class MainWindow(QMainWindow):
    """
    Main application window that manages screen navigation.

    Uses a QStackedWidget to switch between different screens (dashboard,
    workout tracker, etc.).

    :param parent: Parent widget, defaults to None
    :type parent: QWidget, optional
    """

    def __init__(self):
        """Initialize the main window and set up screens."""
        super().__init__()
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        self.setWindowTitle("Momentum")

        self.start_screen = Startscreen()
        self.workout_screen = Workoutscreen()

        self.stacked_widget.addWidget(self.start_screen)
        self.stacked_widget.addWidget(self.workout_screen)

        # Connect button clicks to switch screens
        self.start_screen.button.clicked.connect(
            lambda: self.stacked_widget.setCurrentWidget(self.workout_screen)
        )
        self.workout_screen.button.clicked.connect(
            lambda: self.stacked_widget.setCurrentWidget(self.start_screen)
        )


if __name__ == "__main__":
    """Entry point for the application."""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.move(100, 100)
    window.show()
    app.exec()
