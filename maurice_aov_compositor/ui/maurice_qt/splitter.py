"""
========================================================================================================================
Name: splitter.py
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


class QSplitter(QtWidgets.QSplitter):
    """QSplitter."""

    def __init__(self, *args):
        """Initializes class attributes."""
        super(QSplitter, self).__init__(*args)

        # QSplitter settings.
        self.setStyleSheet(widgets_styles.splitter_style())
