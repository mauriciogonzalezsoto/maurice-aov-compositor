"""
========================================================================================================================
Name: scroll_area.py
Author: Mauricio Gonzalez Soto
Updated Date: 11-06-2024

Copyright (C) 2024 Mauricio Gonzalez Soto. All rights reserved.
========================================================================================================================
"""
try:
    from PySide6 import QtWidgets
    from PySide6 import QtCore
except ImportError:
    from PySide2 import QtWidgets
    from PySide2 import QtCore

import maurice_aov_compositor.ui.maurice_qt.widgets_styles as widgets_styles


class QScrollArea(QtWidgets.QScrollArea):
    """QScrollArea."""

    def __init__(self, *args):
        """Initializes class attributes."""
        super(QScrollArea, self).__init__(*args)

        # QScrollBar settings.
        self.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.setStyleSheet(widgets_styles.scroll_area_style())
        self.setWidgetResizable(True)
