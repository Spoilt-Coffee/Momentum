"""
frontend.ui.sidebar
===================

Contains the :class:`Sidebar` navigation panel.
"""

from PyQt6.QtWidgets import QVBoxLayout, QPushButton
from frontend.ui.base import Panel


class Sidebar(Panel):
    """Navigation sidebar panel.

    Displays navigation buttons that allow the user to switch between
    the different views in the application's content area.

    :ivar dashboard_button: Button that navigates to the Dashboard view.
    :vartype dashboard_button: QPushButton
    :ivar fitness_button: Button that navigates to the Fitness view.
    :vartype fitness_button: QPushButton
    """

    def __init__(self):
        """Initialise the sidebar and create navigation buttons."""
        super().__init__()

        nav_button_layout = QVBoxLayout(self)
        nav_button_layout.setSpacing(20)
        nav_button_layout.addSpacing(20)

        self.dashboard_button = QPushButton("dashboard", self)
        self.fitness_button = QPushButton("Fitness", self)

        self.dashboard_button.setObjectName("sidebar_button")
        self.fitness_button.setObjectName("sidebar_button")

        self.dashboard_button.setMinimumSize(50, 30)
        self.fitness_button.setMinimumSize(50, 30)

        nav_button_layout.addWidget(self.dashboard_button)
        nav_button_layout.addWidget(self.fitness_button)
        nav_button_layout.addStretch()
