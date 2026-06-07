"""
main
====

Application entry point. Constructs the :class:`MainWindow` and starts
the PyQt6 event loop.
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QHBoxLayout
from frontend.ui.dashboard import Dashboard
from frontend.ui.fitness import Fitness
from frontend.ui.sidebar import Sidebar


class MainWindow(QMainWindow):
    """Top-level application window.

    Arranges the :class:`~frontend.ui.sidebar.Sidebar` and a
    :class:`~PyQt6.QtWidgets.QStackedWidget` content area side by side
    inside a central widget.

    :ivar sidebar_widget: The navigation sidebar.
    :vartype sidebar_widget: Sidebar
    :ivar content_widget: Stacked widget that holds the individual page panels.
    :vartype content_widget: QStackedWidget
    :ivar dashboard: The dashboard page panel.
    :vartype dashboard: Dashboard
    :ivar fitness: The fitness page panel.
    :vartype fitness: Fitness
    """

    def __init__(self):
        """Initialise the main window, create and arrange child widgets."""
        super().__init__()
        self.setFixedSize(1025, 901)
        self.setWindowTitle("Momentum")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QHBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.sidebar_widget = Sidebar()
        # Puts all the buttons into a list to cycle through in update_button_colours()
        self.nav_buttons = [
            self.sidebar_widget.dashboard_button,
            self.sidebar_widget.fitness_button
        ]

        self.content_widget = QStackedWidget()

        self.sidebar_widget.setObjectName("sidebar_widget")
        self.content_widget.setObjectName("content_widget")

        layout.addWidget(self.sidebar_widget)
        layout.addWidget(self.content_widget)
        layout.setStretchFactor(self.sidebar_widget, 1)
        layout.setStretchFactor(self.content_widget, 4)

        self.dashboard = Dashboard()
        self.fitness = Fitness()

        self.content_widget.addWidget(self.dashboard)
        self.content_widget.addWidget(self.fitness)

        # Connect sidebar buttons to switch screens
        self.sidebar_widget.dashboard_button.clicked.connect(
            lambda: self.switch_screen(self.dashboard, self.sidebar_widget.dashboard_button)
        )
        self.sidebar_widget.fitness_button.clicked.connect(
            lambda: self.switch_screen(self.fitness, self.sidebar_widget.fitness_button)  
        )

    def switch_screen(self, target_screen, clicked_button):
        self.content_widget.setCurrentWidget(target_screen)
        for button in self.nav_buttons:
            button.setProperty("active", False)
            button.style().unpolish(button)
            button.style().polish(button)
        clicked_button.setProperty("active", True)
        clicked_button.style().unpolish(clicked_button)
        clicked_button.style().polish(clicked_button)

def load_stylesheet(app):
    """Load and apply the QSS stylesheet to the application.

    :param app: The running QApplication instance.
    :type app: QApplication
    """
    with open("style.qss", "r") as file:
        app.setStyleSheet(file.read())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    load_stylesheet(app)
    window = MainWindow()
    window.move(100, 100)
    window.show()
    app.exec()
