"""
========================================================================================================================
Name: list_widget.py
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


class QListWidget(QtWidgets.QListWidget):
    """QListWidget."""
    item_dropped = QtCore.Signal()

    def __init__(self, *args):
        """Initializes class attributes."""
        super(QListWidget, self).__init__(*args)

        # QListWidget settings.
        self.setStyleSheet(widgets_styles.list_widget_style())
        self.setFocusPolicy(QtCore.Qt.NoFocus)

    def dropEvent(self, event):
        """Executes the drop event.

            Parameters
            ----------
                event : Any
                    Drop event.
            Returns
            -------
                None
        """
        super(QListWidget, self).dropEvent(event)

        self.item_dropped.emit()
