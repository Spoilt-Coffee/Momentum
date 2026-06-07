"""
frontend.ui.base
================

Provides the :class:`Panel` base class shared by all full-panel widgets.
"""

from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt


class Panel(QWidget):
    """Base class for all full-panel widgets (e.g. Sidebar, Dashboard, Fitness).

    Enables ``WA_StyledBackground`` so QSS ``background-color`` rules are
    applied correctly. Plain :class:`~PyQt6.QtWidgets.QWidget` subclasses are
    transparent by default and ignore stylesheet background rules without this
    attribute.

    :param parent: Optional parent widget.
    :type parent: QWidget or None
    """

    def __init__(self, parent=None):
        """Initialise the panel and enable styled background painting.

        :param parent: Optional parent widget.
        :type parent: QWidget or None
        """
        super().__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
