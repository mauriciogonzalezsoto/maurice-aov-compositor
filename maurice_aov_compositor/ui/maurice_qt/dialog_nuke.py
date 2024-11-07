"""
========================================================================================================================
Name: dialog_nuke.py
Author: Mauricio Gonzalez Soto
Updated Date: 11-06-2024

Copyright (C) 2024 Mauricio Gonzalez Soto. All rights reserved.
========================================================================================================================
"""
try:
    from shiboken6 import wrapInstance
    from PySide6 import QtWidgets
    from PySide6 import QtCore
    from PySide6 import QtGui
except ImportError:
    from shiboken2 import wrapInstance
    from PySide2 import QtWidgets
    from PySide2 import QtCore
    from PySide2 import QtGui


from maurice_aov_compositor.ui.maurice_qt.dialog import QDialog


def nuke_main_window() -> QtWidgets.QWidget | None:
    """Gets the Nuke main window widget as a Python object."""
    app = QtWidgets.QApplication.instance()

    for widget in app.topLevelWidgets():
        if widget.metaObject().className() == 'Foundry::UI::DockMainWindow':
            return widget

    return


class QDialogNuke(QDialog):
    """QDialog Nuke."""
    def __init__(self, parent: QtWidgets.QWidget = nuke_main_window()):
        super(QDialogNuke, self).__init__(parent)
