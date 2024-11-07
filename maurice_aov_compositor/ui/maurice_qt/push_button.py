"""
========================================================================================================================
Name: push_button.py
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

import maurice_aov_compositor.ui.maurice_qt.widgets_attributes as widgets_attributes
import maurice_aov_compositor.ui.maurice_qt.widgets_styles as widgets_styles


class QPushButton(QtWidgets.QPushButton):
    """QPushButton."""
    ICON_SIZE = widgets_attributes.push_button_icon_size
    ICON_SMALL_SIZE = widgets_attributes.push_button_icon_small_size

    clicked_and_alt = QtCore.Signal()
    clicked_and_ctrl = QtCore.Signal()

    POP_UP_WINDOW = None

    def __init__(self, *args):
        """Initializes class attributes."""
        super(QPushButton, self).__init__(*args)

        # QPushButton class variables.
        self.pop_up_window = None

        # QPushButton settings.
        self.setFixedHeight(widgets_attributes.push_button_height)
        self.setIconSize(QtCore.QSize(QPushButton.ICON_SIZE[0], QPushButton.ICON_SIZE[1]))
        self.setStyleSheet(widgets_styles.push_button_style())

    def set_small_push_button_size(self) -> None:
        """Sets small push button size."""
        self.setFixedSize(
            widgets_attributes.push_button_small_height,
            widgets_attributes.push_button_small_height)
        self.setIconSize(QtCore.QSize(QPushButton.ICON_SMALL_SIZE[0], QPushButton.ICON_SMALL_SIZE[1]))

    def set_transparent_background(self) -> None:
        """Sets transparent background."""
        self.setStyleSheet('''
            QPushButton {
                background-color: transparent;
                border: 0px;} 
            QPushButton:hover {
                border: 0px;}
                
            QToolTip {
            background-color: rgb(45, 45, 45);
            color: white; 
            border: 1px solid %s;}
            ''' % widgets_attributes.color)

    def set_yellow_background(self) -> None:
        """Sets yellow background."""
        self.setStyleSheet(widgets_styles.push_button_style() + 'QPushButton {background-color: #d7801a;}')

    def setCheckable(self, checkable):
        """Sets checkable."""
        if checkable:
            self.setStyleSheet(widgets_styles.check_button_style())

        super(QPushButton, self).setCheckable(checkable)

    def setToolTip(self, lmb: str, alt_lmb: str = '', ctrl_lmb: str = '', title: str = ''):
        """Sets tool tip."""
        alt_lmb = alt_lmb.capitalize()
        ctrl_lmb = ctrl_lmb.capitalize()
        lmb = lmb.capitalize()

        if alt_lmb:
            alt_lmb = f'<br><br><b>Alt + LMB:</b> {alt_lmb}'

        if ctrl_lmb:
            ctrl_lmb = f'<br><br><b>Ctrl + LMB:</b> {ctrl_lmb}'

        title = title.title() if title else lmb.title()

        super(QPushButton, self).setToolTip(f'<b>{title}</b><br><br><b>LMB:</b> {lmb}{alt_lmb}{ctrl_lmb}')
