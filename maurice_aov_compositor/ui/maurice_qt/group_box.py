"""
========================================================================================================================
Name: group_box.py
Author: Mauricio Gonzalez Soto
Updated Date: 11-06-2024

Copyright (C) 2024 Mauricio Gonzalez Soto. All rights reserved.
========================================================================================================================
"""
try:
    from PySide6 import QtWidgets
except ImportError:
    from PySide2 import QtWidgets

import maurice_aov_compositor.ui.maurice_qt.widgets_styles as widgets_styles


class QGroupBox(QtWidgets.QGroupBox):
    """QGroupBox."""

    def __init__(self, *args):
        """Initializes class attributes."""
        super(QGroupBox, self).__init__(*args)

        # QGroupBox settings.
        self.setStyleSheet(widgets_styles.group_box_style())
