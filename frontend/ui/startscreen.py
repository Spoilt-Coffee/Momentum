"""
Start screen module for the Momentum application.

This module contains the dashboard screen that serves as the main entry point
for the application.
"""

import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton


class Startscreen(QWidget):
    """
    Dashboard screen for the application.

    Displays the main dashboard with widgets showing information from
    various modules (workouts, finances, etc.).

    :param parent: Parent widget, defaults to None
    :type parent: QWidget, optional
    """

    def __init__(self):
        """Initialize the start screen with dashboard layout."""
        super().__init__()

        self.setFixedSize(1500, 900)
        layout = QVBoxLayout(self)

        self.button = QPushButton("Go to workoutscreen", self)
        self.button.setFixedSize(200, 100)
        layout.addWidget(self.button)
