"""
========================================================================================================================
Name: combo_box.py
Author: Mauricio Gonzalez Soto
Updated Date: 11-06-2024

Copyright (C) 2024 Mauricio Gonzalez Soto. All rights reserved.
========================================================================================================================
"""
try:
    from PySide6 import QtWidgets
    from PySide6 import QtCore
    from PySide6 import QtGui
except ImportError:
    from PySide2 import QtWidgets
    from PySide2 import QtCore
    from PySide2 import QtGui

import maurice_aov_compositor.ui.maurice_qt.widgets_attributes as widgets_attributes
import maurice_aov_compositor.ui.maurice_qt.widgets_styles as widgets_styles


class QComboBox(QtWidgets.QComboBox):
    """QComboBox."""

    def __init__(self, fixed_size: bool = True):
        """Initializes class attributes."""
        super(QComboBox, self).__init__()

        # QComboBox class variables.
        self.last_text = ''
        self.wheel_event = True

        # QComboBox settings.
        if fixed_size:
            self.setFixedWidth(widgets_attributes.width)

        self.setFixedHeight(widgets_attributes.height)
        self.setStyleSheet(widgets_styles.combo_box_style())

        # QStandardItemModel.
        self.standard_item_model = QtGui.QStandardItemModel()
        self.setModel(self.standard_item_model)
        self.setItemDelegate(QSeparatorStyledItemDelegate())

    def add_separator(self) -> None:
        """Adds a separator."""
        separator_standard_item = QtGui.QStandardItem()
        separator_standard_item.setData('mgSeparator', QtCore.Qt.UserRole)
        separator_standard_item.setEnabled(False)
        separator_standard_item.setSizeHint(QtCore.QSize(0, 10))
        self.standard_item_model.appendRow(separator_standard_item)

    def items_text(self) -> list:
        """Gets the items text."""
        return [self.itemText(i) for i in range(self.count())]

    @property
    def last_text_selected(self) -> str:
        """Gets the last text selected."""
        return self.last_text

    def set_wheel_event(self, wheel_event: bool) -> None:
        """Sets the wheel event."""
        self.wheel_event = wheel_event

    def keyPressEvent(self, event):
        """Key press event."""
        pass

    def mousePressEvent(self, event):
        """Mouse press event."""
        super(QComboBox, self).mousePressEvent(event)
        self.last_text = self.currentText()

    def wheelEvent(self, event):
        """Wheel event."""
        if self.wheel_event:
            super(QComboBox, self).wheelEvent(event)


class QSeparatorStyledItemDelegate(QtWidgets.QStyledItemDelegate):
    """QSeparatorStyledItemDelegate."""

    def paint(self, painter, option, index):
        """Paint."""
        if index.data(QtCore.Qt.UserRole) == 'mgSeparator':
            pen = QtGui.QPen(QtGui.QColor(255, 255, 255))
            pen.setWidth(1)
            painter.setPen(pen)

            separator_rect = option.rect
            y_center = separator_rect.center().y()
            start = separator_rect.bottomLeft()
            end = separator_rect.bottomRight()
            start.setY(y_center)
            end.setY(y_center)
            start.setX(start.x())
            end.setX(end.x())

            painter.drawLine(start, end)
        else:
            super(QSeparatorStyledItemDelegate, self).paint(painter, option, index)
