"""
========================================================================================================================
Name: message_box_question.py
Author: Mauricio Gonzalez Soto
Updated Date: 11-06-2024

Copyright (C) 2024 Mauricio Gonzalez Soto. All rights reserved.
========================================================================================================================
"""
try:
    from PySide6 import QtCore
    from PySide6 import QtGui
except ImportError:
    from PySide2 import QtCore
    from PySide2 import QtGui

from maurice_aov_compositor.ui.maurice_qt.divider_label import QDividerLabel
from maurice_aov_compositor.ui.maurice_qt.h_box_layout import QHBoxLayout
from maurice_aov_compositor.ui.maurice_qt.v_box_layout import QVBoxLayout
from maurice_aov_compositor.ui.maurice_qt.push_button import QPushButton
from maurice_aov_compositor.ui.maurice_qt.group_box import QGroupBox
from maurice_aov_compositor.ui.maurice_qt.dialog import QDialog
from maurice_aov_compositor.ui.maurice_qt.label import QLabel


class QMessageBoxQuestion(QDialog):
    """QMessageBoxQuestion."""
    WINDOW_HEIGHT = 25
    WINDOW_NAME = 'QMessageBoxQuestion'
    WINDOW_TITLE = 'QMessageBoxQuestion'

    MENU_BAR = False

    yes = QtCore.Signal()
    no = QtCore.Signal()

    def __init__(self, question: str, title: str):
        """Initializes class attributes."""
        # QInputDialog class variables.
        self.title = title if title else self.WINDOW_TITLE

        # Question class variables.
        self.question_label = None
        self.question = question
        self.divider_label = None
        self.yes_push_button = None
        self.no_push_button = None

        super(QMessageBoxQuestion, self).__init__()

        # QDialog settings.
        self.setFixedWidth(self.WINDOW_WIDTH)
        self.setMaximumHeight(self.WINDOW_HEIGHT)
        self.setModal(True)
        self.setWindowIcon(QtGui.QIcon(self.icons['interrogation-black.png']))
        self.setWindowTitle(self.title)

    def create_widgets(self) -> None:
        """Creates the widgets."""
        # ==============================================================================================================
        # Question.
        # ==============================================================================================================
        # Question QLabel.
        self.question_label = QLabel(self.question)
        self.question_label.setAlignment(QtCore.Qt.AlignHCenter)

        # q_divider_label.
        self.divider_label = QDividerLabel()
        
        # Yes QPushButton.
        self.yes_push_button = QPushButton('Yes')
        self.yes_push_button.setToolTip(lmb='Yes')
        
        # No QPushButton.
        self.no_push_button = QPushButton('No')
        self.no_push_button.setToolTip(lmb='No')
        self.no_push_button.set_yellow_background()

    def create_layouts(self) -> None:
        """Creates the layouts."""
        # ==============================================================================================================
        # Question.
        # ==============================================================================================================
        # Question QGroupBox.
        question_group_box = QGroupBox()
        self.main_layout.addWidget(question_group_box)

        # Question QVBoxLayout.
        question_v_box_layout = QVBoxLayout()
        question_v_box_layout.addWidget(self.question_label)
        question_group_box.setLayout(question_v_box_layout)

        # Buttons QHBoxLayout.
        buttons_h_box_layout = QHBoxLayout()
        buttons_h_box_layout.addWidget(self.yes_push_button)
        buttons_h_box_layout.addWidget(self.no_push_button)
        self.main_layout.addWidget(self.divider_label)
        self.main_layout.addLayout(buttons_h_box_layout)

    def create_connections(self) -> None:
        """Creates the connections."""
        # ==============================================================================================================
        # Question.
        # ==============================================================================================================
        self.yes_push_button.clicked.connect(self.accept)
        self.no_push_button.clicked.connect(self.reject)
