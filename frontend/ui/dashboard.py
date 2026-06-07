"""
frontend.ui.dashboard
=====================

Contains the :class:`Dashboard` panel.
"""

from PyQt6.QtWidgets import QVBoxLayout, QPushButton
from frontend.ui.base import Panel


class Dashboard(Panel):
    """Main dashboard panel.

    Serves as the default content view displayed in the application's
    content area on startup.
    """

    def __init__(self):
        """Initialise the dashboard panel."""
        super().__init__()

        layout = QVBoxLayout(self)
        self.temp_button = QPushButton("TEST! THIS IS DASHBOARD", self)
        layout.addWidget(self.temp_button)
