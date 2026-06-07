"""
frontend.ui.fitness
===================

Contains the :class:`Fitness` panel.
"""

from PyQt6.QtWidgets import QVBoxLayout, QPushButton
from frontend.ui.base import Panel


class Fitness(Panel):
    """Fitness tracking panel.

    Displays fitness-related content and controls within the application's
    content area.
    """

    def __init__(self):
        """Initialise the fitness panel."""
        super().__init__()
