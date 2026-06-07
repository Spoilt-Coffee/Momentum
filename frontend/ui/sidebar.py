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

    The ``active`` boolean property on each button is toggled by
    :meth:`~main.MainWindow.switch_screen` and drives QSS pseudo-state
    styling to highlight the currently selected view.

    :ivar dashboard_button: Button that navigates to the Dashboard view.
        Initialised with ``active=True`` as the default screen on startup.
    :vartype dashboard_button: QPushButton
    :ivar fitness_button: Button that navigates to the Fitness view.
    :vartype fitness_button: QPushButton
    """

    def __init__(self):
        """Initialise the sidebar, configure layout spacing, and create navigation buttons.

        Sets ``active=True`` on the dashboard button so it appears selected
        on startup without requiring an explicit :meth:`~main.MainWindow.switch_screen` call.
        """
        super().__init__()

        nav_button_layout = QVBoxLayout(self)
        nav_button_layout.setSpacing(30)
        nav_button_layout.addSpacing(20)

        self.dashboard_button = QPushButton("DASHBOARD", self)
        self.fitness_button = QPushButton("FITNESS", self)

        self.dashboard_button.setMinimumSize(50, 30)
        self.fitness_button.setMinimumSize(50, 30)

        self.dashboard_button.setProperty("active", True)
        self.fitness_button.setProperty("active", False)


        nav_button_layout.addWidget(self.dashboard_button)
        nav_button_layout.addWidget(self.fitness_button)
        nav_button_layout.addStretch()
