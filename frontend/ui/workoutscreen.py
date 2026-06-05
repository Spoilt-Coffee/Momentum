"""
Workout screen module for the Momentum application.

This module contains the workout tracking screen where users can log
and view their workout routines.
"""

import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton


class Workoutscreen(QWidget):
    """
    Workout tracking screen.

    Allows users to log exercises, sets, reps, and weights for their
    workout routines.

    :param parent: Parent widget, defaults to None
    :type parent: QWidget, optional
    """

    def __init__(self):
        """Initialize the workout screen with tracking interface."""
        super().__init__()

        self.setFixedSize(1500, 900)
        layout = QVBoxLayout(self)

        self.button = QPushButton("Go to Startscreen", self)
        self.button.setFixedSize(200, 100)
        layout.addWidget(self.button)
