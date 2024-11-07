"""
========================================================================================================================
Name: label.py
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


class QLabel(QtWidgets.QLabel):
    """QLabel."""

    def __init__(self, *args):
        """Initializes class attributes."""
        super(QLabel, self).__init__(*args)

        # QLabel settings.
        self.setAlignment(QtCore.Qt.AlignVCenter)
        self.setStyleSheet(widgets_styles.label_style())
