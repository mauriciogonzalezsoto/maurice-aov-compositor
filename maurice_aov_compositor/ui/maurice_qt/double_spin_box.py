"""
========================================================================================================================
Name: double_spin_box.py
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


class QDoubleSpinBox(QtWidgets.QDoubleSpinBox):
    """QDoubleSpinBox."""

    def __init__(self, *args):
        """Initializes class attributes."""
        super(QDoubleSpinBox, self).__init__(*args)

        # QDoubleSpinBox settings.
        self.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.setFixedSize(widgets_attributes.width, widgets_attributes.height)
        self.setStyleSheet(widgets_styles.double_spin_box_style())

    def contextMenuEvent(self, event):
        """Context menu event."""
        event.ignore()
