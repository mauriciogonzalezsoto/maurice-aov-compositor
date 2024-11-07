"""
========================================================================================================================
Name: spin_box.py
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


class QSpinBox(QtWidgets.QSpinBox):
    """QSpinBox."""

    def __init__(self, *args):
        """Initializes class attributes."""
        super(QSpinBox, self).__init__(*args)

        # QSpinBox settings.
        self.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.setFixedSize(widgets_attributes.width, widgets_attributes.height)
        self.setStyleSheet(widgets_styles.spin_box_style())

    def contextMenuEvent(self, event):
        """Context menu event."""
        event.ignore()
