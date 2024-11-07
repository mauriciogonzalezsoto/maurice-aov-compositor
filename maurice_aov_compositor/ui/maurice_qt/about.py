"""
========================================================================================================================
Name: about.py
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

import webbrowser
import datetime

from maurice_aov_compositor.ui.maurice_qt.divider_label import QDividerLabel
from maurice_aov_compositor.ui.maurice_qt.push_button import QPushButton
from maurice_aov_compositor.ui.maurice_qt.h_box_layout import QHBoxLayout
from maurice_aov_compositor.ui.maurice_qt.v_box_layout import QVBoxLayout
from maurice_aov_compositor.ui.maurice_qt.group_box import QGroupBox
from maurice_aov_compositor.ui.maurice_qt.dialog import QDialog
from maurice_aov_compositor.ui.maurice_qt.label import QLabel
import maurice_aov_compositor.utils as maurice_utils
import maurice_aov_compositor as maurice


class QAbout(QDialog):
    """QAbout."""
    WINDOW_NAME = 'QAbout'
    WINDOW_TITLE = 'About Maurice'
    WINDOW_WIDTH = maurice_utils.get_value_by_ppi(230, 350)

    MENU_BAR = False

    ICON_SIZE = maurice_utils.get_value_by_ppi(20, 30)

    def __init__(self, parent: QtWidgets.QWidget, image_path: str, tool_name: str, tool_version: int):
        """ Initializes class attributes."""
        # About class variables.
        self.image_path = image_path
        self.tool_name = tool_name
        self.tool_version = tool_version
        self.image_label = None
        self.window_icon_label = None
        self.window_label = None
        self.author_icon_label = None
        self.author_label = None
        self.email_icon_label = None
        self.email_label = None
        self.copyright_label = None
        self.divider_label = None
        self.open_art_station_push_button = None
        self.open_github_push_button = None

        super(QAbout, self).__init__(parent)

        # QDialog settings.
        self.setFixedWidth(self.WINDOW_WIDTH)
        self.setMaximumHeight(self.WINDOW_HEIGHT)
        self.setModal(True)
        self.setWindowIcon(QtGui.QIcon(self.icons['info-black.png']))

    def create_widgets(self) -> None:
        """Creates the widgets."""
        # ==============================================================================================================
        # About.
        # ==============================================================================================================
        # Toolkit QImage. #########Warning scale not working on lower resolutions
        toolkit_image = QtGui.QImage(self.image_path)
        toolkit_image = toolkit_image.scaled(
            maurice_utils.get_value_by_ppi(223, 334),
            maurice_utils.get_value_by_ppi(126, 188),
            QtCore.Qt.IgnoreAspectRatio,
            QtCore.Qt.SmoothTransformation)

        # Toolkit QPixmap.
        toolkit_pixmap = QtGui.QPixmap()
        toolkit_pixmap.convertFromImage(toolkit_image)

        # Toolkit QLabel.
        self.image_label = QtWidgets.QLabel()
        self.image_label.setAlignment(QtCore.Qt.AlignVCenter)
        self.image_label.setAlignment(QtCore.Qt.AlignHCenter)
        self.image_label.setPixmap(toolkit_pixmap)

        # Window QImage.
        window_image = QtGui.QImage(self.icons['browser.png'])
        window_image = window_image.scaled(
            QAbout.ICON_SIZE,
            QAbout.ICON_SIZE,
            QtCore.Qt.IgnoreAspectRatio,
            QtCore.Qt.SmoothTransformation)

        # Window QPixmap.
        window_pixmap = QtGui.QPixmap()
        window_pixmap.convertFromImage(window_image)

        # Window icon QLabel.
        self.window_icon_label = QtWidgets.QLabel()
        self.window_icon_label.setMaximumSize(40, 40)
        self.window_icon_label.setPixmap(window_pixmap)

        # Window QLabel.
        self.window_label = QLabel(f'{self.tool_name} {self.tool_version}')

        # Author QImage.
        author_image = QtGui.QImage(self.icons['user.png'])
        author_image = author_image.scaled(
            QAbout.ICON_SIZE,
            QAbout.ICON_SIZE,
            QtCore.Qt.IgnoreAspectRatio,
            QtCore.Qt.SmoothTransformation)

        # Author QPixmap.
        author_pixmap = QtGui.QPixmap()
        author_pixmap.convertFromImage(author_image)

        # Author icon QLabel.
        self.author_icon_label = QtWidgets.QLabel()
        self.author_icon_label.setMaximumSize(40, 40)
        self.author_icon_label.setPixmap(author_pixmap)

        # Author QLabel.
        self.author_label = QLabel(maurice.AUTHOR)

        # Email QImage.
        email_image = QtGui.QImage(self.icons['envelope.png'])
        email_image = email_image.scaled(
            QAbout.ICON_SIZE,
            QAbout.ICON_SIZE,
            QtCore.Qt.IgnoreAspectRatio,
            QtCore.Qt.SmoothTransformation)

        # Email QPixmap.
        email_pixmap = QtGui.QPixmap()
        email_pixmap.convertFromImage(email_image)

        # Email icon QLabel.
        self.email_icon_label = QtWidgets.QLabel()
        self.email_icon_label.setMaximumSize(40, 40)
        self.email_icon_label.setPixmap(email_pixmap)

        # email QLabel.
        self.email_label = QLabel('mauricio.gonzalez.soto@outlook.com')

        # Copyright QLabel.
        self.copyright_label = QLabel(
            f'Copyright © 2024-{datetime.date.today().strftime("%Y")} Maurice.\nAll rights reserved.')
        self.copyright_label.setAlignment(QtCore.Qt.AlignHCenter)

        # QDividerLabel.
        self.divider_label = QDividerLabel()

        # Open ArtStation QPushButton.
        self.open_art_station_push_button = QPushButton('ArtStation')
        self.open_art_station_push_button.setIcon(QtGui.QIcon(self.icons['artstation.png']))
        self.open_art_station_push_button.setToolTip(lmb='Open ArtStation')

        # Open Github QPushButton.
        self.open_github_push_button = QPushButton('Github')
        self.open_github_push_button.setIcon(QtGui.QIcon(self.icons['github.png']))
        self.open_github_push_button.setToolTip(lmb='Open Github')

    def create_layouts(self) -> None:
        """Creates the layouts."""
        # ==============================================================================================================
        # About.
        # ==============================================================================================================
        # Image QGroupBox.
        image_group_box = QGroupBox()
        self.main_layout.addWidget(image_group_box)

        # Image QVBoxLayout.
        image_v_box_layout = QVBoxLayout()
        image_v_box_layout.addWidget(self.image_label)
        image_group_box.setLayout(image_v_box_layout)

        # Window QGroupBox.
        window_group_box = QGroupBox()
        self.main_layout.addWidget(window_group_box)

        # Window QHBoxLayout.
        window_h_box_layout = QHBoxLayout()
        window_h_box_layout.addWidget(self.window_icon_label)
        window_h_box_layout.addWidget(self.window_label)
        window_group_box.setLayout(window_h_box_layout)

        # Author QGroupBox.
        author_group_box = QGroupBox()
        self.main_layout.addWidget(author_group_box)

        # Author QHBoxLayout.
        author_h_box_layout = QHBoxLayout()
        author_h_box_layout.addWidget(self.author_icon_label)
        author_h_box_layout.addWidget(self.author_label)
        author_group_box.setLayout(author_h_box_layout)

        # Email QGroupBox.
        email_group_box = QGroupBox()
        self.main_layout.addWidget(email_group_box)

        # Email QHBoxLayout.
        email_h_box_layout = QHBoxLayout()
        email_h_box_layout.addWidget(self.email_icon_label)
        email_h_box_layout.addWidget(self.email_label)
        email_group_box.setLayout(email_h_box_layout)

        # Copyright QGroupBox.
        copyright_group_box = QGroupBox()
        self.main_layout.addWidget(copyright_group_box)

        # Copyright QVBoxLayout.
        copyright_v_box_layout = QVBoxLayout()
        copyright_v_box_layout.addWidget(self.copyright_label)
        copyright_group_box.setLayout(copyright_v_box_layout)

        # About buttons QVBoxLayout.
        about_buttons_v_box_layout = QVBoxLayout()
        about_buttons_v_box_layout.addWidget(self.divider_label)
        self.main_layout.addLayout(about_buttons_v_box_layout)

        # About buttons QHBoxLayout.
        about_buttons_h_box_layout = QHBoxLayout()
        about_buttons_h_box_layout.addWidget(self.open_art_station_push_button)
        about_buttons_h_box_layout.addWidget(self.open_github_push_button)
        about_buttons_v_box_layout.addLayout(about_buttons_h_box_layout)

    def create_connections(self) -> None:
        """Creates the connections."""
        # ==============================================================================================================
        # About.
        # ==============================================================================================================
        self.open_art_station_push_button.clicked.connect(self.open_art_station_clicked_push_button)
        self.open_github_push_button.clicked.connect(self.open_github_clicked_push_button)

    @staticmethod
    def open_art_station_clicked_push_button() -> None:
        """Executes the signal 'clicked' of the 'open Artstation' push button."""
        webbrowser.open('https://www.artstation.com/mauriciogonzalezsoto')

    @staticmethod
    def open_github_clicked_push_button() -> None:
        """Executes the signal 'clicked' of the 'open Github' push button."""
        webbrowser.open('https://github.com/mauriciogonzalezsoto')
