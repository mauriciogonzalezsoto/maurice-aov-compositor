"""
========================================================================================================================
Name: input_dialog.py
Author: Mauricio Gonzalez Soto
Updated Date: 11-06-2024

Copyright (C) 2024 Mauricio Gonzalez Soto. All rights reserved.
========================================================================================================================
"""
try:
    from PySide6 import QtGui
except ImportError:
    from PySide2 import QtGui

from maurice_aov_compositor.ui.maurice_qt.divider_label import QDividerLabel
from maurice_aov_compositor.ui.maurice_qt.h_box_layout import QHBoxLayout
from maurice_aov_compositor.ui.maurice_qt.push_button import QPushButton
from maurice_aov_compositor.ui.maurice_qt.v_box_layout import QVBoxLayout
from maurice_aov_compositor.ui.maurice_qt.group_box import QGroupBox
from maurice_aov_compositor.ui.maurice_qt.line_edit import QLineEdit
from maurice_aov_compositor.ui.maurice_qt.dialog import QDialog


class QInputDialog(QDialog):
    """QInputDialog."""
    WINDOW_NAME = 'QInputDialog'
    WINDOW_TITLE = 'QInputDialog'

    MENU_BAR = False

    def __init__(self, title):
        """Initializes class attributes."""
        # QInputDialog class variables.
        self.title = title

        # Input class variables.
        self.input_line_edit = None
        self.divider_label = None
        self.ok_push_button = None
        self.cancel_push_button = None

        super(QInputDialog, self).__init__()

        # QDialog settings.
        self.setFixedWidth(self.WINDOW_WIDTH)
        self.setMaximumHeight(self.WINDOW_HEIGHT)
        self.setModal(True)
        self.setWindowIcon(QtGui.QIcon(self.icons['input-text-black.png']))
        self.setWindowTitle(self.title)

    def create_widgets(self) -> None:
        """Creates the widgets."""
        # ==============================================================================================================
        # Input.
        # ==============================================================================================================
        # Input line edit.
        self.input_line_edit = QLineEdit()

        # QDividerLabel.
        self.divider_label = QDividerLabel()

        # Ok push button.
        self.ok_push_button = QPushButton('OK')
        self.ok_push_button.setIcon(QtGui.QIcon(self.icons['check.png']))
        self.ok_push_button.setToolTip(lmb='Ok')
        self.ok_push_button.set_yellow_background()

        # Cancel push button.
        self.cancel_push_button = QPushButton('Cancel')
        self.cancel_push_button.setIcon(QtGui.QIcon(self.icons['x.png']))
        self.cancel_push_button.setToolTip(lmb='Cancel')

    def create_layouts(self) -> None:
        """Creates the layouts."""
        # ==============================================================================================================
        # Input.
        # ==============================================================================================================
        # Input QGroupBox.
        input_group_box = QGroupBox()
        self.main_layout.addWidget(input_group_box)

        # Input QVBoxLayout.
        input_v_box_layout = QVBoxLayout()
        input_v_box_layout.addWidget(self.input_line_edit)
        input_group_box.setLayout(input_v_box_layout)

        # Buttons QHBoxLayout.
        buttons_h_box_layout = QHBoxLayout()
        buttons_h_box_layout.addWidget(self.ok_push_button)
        buttons_h_box_layout.addWidget(self.cancel_push_button)
        self.main_layout.addWidget(self.divider_label)
        self.main_layout.addLayout(buttons_h_box_layout)

    def create_connections(self) -> None:
        """Creates the connections."""
        # ==============================================================================================================
        # Input.
        # ==============================================================================================================
        self.input_line_edit.returnPressed.connect(self.accept)
        self.ok_push_button.clicked.connect(self.accept)
        self.cancel_push_button.clicked.connect(self.reject)

    def get_text(self) -> str:
        """Gets the text."""
        return self.input_line_edit.text()
