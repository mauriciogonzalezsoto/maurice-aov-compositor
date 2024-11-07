"""
========================================================================================================================
Name: divider_label.py
Author: Mauricio Gonzalez Soto
Updated Date: 11-06-2024

Copyright (C) 2024 Mauricio Gonzalez Soto. All rights reserved.
========================================================================================================================
"""
try:
    from PySide6 import QtWidgets
except ImportError:
    from PySide2 import QtWidgets

import maurice_aov_compositor.utils as maurice_utils


class QDividerLabel(QtWidgets.QLabel):
    """QDividerLabel."""

    def __init__(self, *args):
        """Initializes class attributes."""
        super(QDividerLabel, self).__init__(*args)

        # QLabel settings.
        self.setFixedHeight(maurice_utils.get_value_by_ppi(4, 6))
        self.setFrameStyle(QtWidgets.QFrame.HLine | QtWidgets.QFrame.Plain)
        self.setLineWidth(maurice_utils.get_value_by_ppi(2, 3))
