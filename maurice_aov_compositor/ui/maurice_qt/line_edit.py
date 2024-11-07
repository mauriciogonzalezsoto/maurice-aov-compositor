"""
========================================================================================================================
Name: line_edit.py
Author: Mauricio Gonzalez Soto
Updated Date: 11-06-2024

Copyright (C) 2024 Mauricio Gonzalez Soto. All rights reserved.
========================================================================================================================
"""
try:
    from PySide6 import QtWidgets
except ImportError:
    from PySide2 import QtWidgets

import maurice_aov_compositor.ui.maurice_qt.widgets_attributes as widgets_attributes
import maurice_aov_compositor.ui.maurice_qt.widgets_styles as widgets_styles


class QLineEdit(QtWidgets.QLineEdit):
    """QLineEdit."""

    def __init__(self, *args):
        """Initializes class attributes."""
        super(QLineEdit, self).__init__(*args)

        # QLineEdit settings.
        self.setFixedHeight(widgets_attributes.height)
        self.setStyleSheet(widgets_styles.line_edit_style())

    def contextMenuEvent(self, event):
        """Context menu event."""
        event.ignore()
