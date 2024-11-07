"""
========================================================================================================================
Name: form_layout.py
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
from maurice_aov_compositor.ui.maurice_qt.label import QLabel


class QFormLayout(QtWidgets.QFormLayout):
    """QFormLayout."""

    def __init__(self, *args):
        """Initializes class attributes."""
        super(QFormLayout, self).__init__(*args)

        # QFormLayout settings.
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(widgets_attributes.spacing)

    def add_row(self, label_text: str, filed: any):
        """Adds a row."""
        self.addRow(QLabel(label_text), filed)
