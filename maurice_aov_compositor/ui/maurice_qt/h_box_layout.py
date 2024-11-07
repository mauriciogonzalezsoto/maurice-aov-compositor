"""
========================================================================================================================
Name: h_box_layout.py
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


class QHBoxLayout(QtWidgets.QHBoxLayout):
    """QHBoxLayout."""

    def __init__(self, *args):
        """Initializes class attributes."""
        super(QHBoxLayout, self).__init__(*args)

        # QHBoxLayout settings.
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(widgets_attributes.spacing)
