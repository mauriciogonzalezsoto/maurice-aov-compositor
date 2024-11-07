"""
========================================================================================================================
Name: dialog.py
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

import logging
import os

import maurice_aov_compositor.ui.maurice_qt.widgets_attributes as widgets_attributes
import maurice_aov_compositor.ui.maurice_qt.widgets_styles as widgets_styles
import maurice_aov_compositor.utils as maurice_utils


logger = logging.getLogger(__name__)


class QDialog(QtWidgets.QDialog):
    """QDialog."""
    WINDOW_HEIGHT = maurice_utils.get_value_by_ppi(30, 50)
    WINDOW_NAME = 'QDialog'
    WINDOW_TITLE = 'QDialog'
    WINDOW_WIDTH = maurice_utils.get_value_by_ppi(316, 400)

    MENU_BAR = True
    EDIT_MENU = True
    RESET_SETTINGS_BUTTON = True
    SAVE_SETTINGS_BUTTON = True
    PREFERENCES_BUTTON = False
    ON_TOP_BOTTOM = True
    COLLAPSE_BUTTON = True
    EXPAND_BUTTON = True

    VERTICAL_MAIN_LAYOUT = True

    CONFIG_PATH = ''

    window_instance = None

    @classmethod
    def show_window(cls) -> None:
        """Shows the window."""
        if not cls.window_instance:
            cls.window_instance = QDialog()

        if cls.window_instance.isHidden():
            cls.window_instance.show()
        else:
            cls.window_instance.raise_()
            cls.window_instance.activateWindow()

    def __init__(self, parent: QtWidgets.QWidget = None):
        """Initializes class attributes"""
        super(QDialog, self).__init__(parent)

        # Files path class variables.
        self.icons = maurice_utils.get_icons()
        self.images = maurice_utils.get_images()

        # UI class variables.
        self.geometry = None
        self.main_layout = None

        # QMenuBar class variables.
        self.on_top_bottom_action = None
        self.is_on_top = False

        # QDialog settings.
        palette = self.palette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(60, 60, 60))

        self.setAutoFillBackground(True)
        self.setObjectName(self.WINDOW_NAME)
        self.setPalette(palette)
        self.setWindowTitle(self.WINDOW_TITLE)

        if os.name == 'nt':
            self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        elif os.name == 'posix':
            self.setWindowFlags(QtCore.Qt.Tool)

        # Main layout.
        if self.VERTICAL_MAIN_LAYOUT:
            self.main_layout = QtWidgets.QVBoxLayout(self)
        else:
            self.main_layout = QtWidgets.QHBoxLayout(self)

        self.main_layout.setContentsMargins(2, 2, 2, 2)
        self.main_layout.setObjectName('mainLayout')
        self.main_layout.setSpacing(2)

        # Creates the widgets.
        if self.MENU_BAR:
            self.create_menu_bar()

        self.create_actions()
        self.create_widgets()
        self.create_layouts()
        self.create_shortcuts()
        self.create_connections()

        # Loads settings.
        if self.CONFIG_PATH:
            self.load_settings()

    def create_menu_bar(self) -> None:
        """Creates the menu bar."""
        # Main QMenuBar.
        main_menu_bar = QtWidgets.QMenuBar()
        main_menu_bar.setFixedHeight(widgets_attributes.menu_bar_height)
        main_menu_bar.setStyleSheet(widgets_styles.menu_bar_style())
        self.main_layout.setMenuBar(main_menu_bar)

        # Main menu.
        main_menu = main_menu_bar.addMenu('Edit')
        main_menu.setIcon(QtGui.QIcon(self.icons['menu-burger.png']))

        if self.EDIT_MENU:
            edit_menu = main_menu.addMenu('Edit')

            if self.SAVE_SETTINGS_BUTTON:
                save_settings_action = edit_menu.addAction('Save Settings', self.save_settings)
                save_settings_action.setIcon(QtGui.QIcon(self.icons['disk.png']))

            if self.RESET_SETTINGS_BUTTON:
                reset_settings_action = edit_menu.addAction('Reset Settings', self.reset_settings)
                reset_settings_action.setIcon(QtGui.QIcon(self.icons['refresh.png']))

            if self.PREFERENCES_BUTTON:
                edit_menu.addSeparator()

                preferences_action = edit_menu.addAction('Preferences', self.show_preferences)
                preferences_action.setIcon(QtGui.QIcon(self.icons['settings.png']))

        if self.ON_TOP_BOTTOM:
            mode_menu = main_menu.addMenu('Mode')

            self.on_top_bottom_action = mode_menu.addAction('On Top', self.on_top_bottom)
            self.on_top_bottom_action.setIcon(QtGui.QIcon(self.icons['arrow-alt-to-top.png']))

        # Help menu.
        help_menu = main_menu.addMenu('Help')

        about_action = help_menu.addAction('About', self.show_about)
        about_action.setIcon(QtGui.QIcon(self.icons['info.png']))

        # Right QMenuBar.
        right_menu_bar = QtWidgets.QMenuBar(main_menu_bar)
        right_menu_bar.setStyleSheet('QMenuBar {padding: 0px 0px 0px %dpx;}' % (maurice_utils.get_value_by_ppi(3, 5)))
        main_menu_bar.setCornerWidget(right_menu_bar, corner=QtCore.Qt.Corner.TopRightCorner)

        if self.COLLAPSE_BUTTON:
            collapse_action = right_menu_bar.addAction('Collapse', self.collapse_frame_layouts)
            collapse_action.setIcon(QtGui.QIcon(self.icons['angle-up.png']))

        if self.EXPAND_BUTTON:
            expand_action = right_menu_bar.addAction('Expand', self.expand_frame_layouts)
            expand_action.setIcon(QtGui.QIcon(self.icons['angle-down.png']))

    def create_shortcuts(self) -> None:
        """Creates the shortcuts."""
        pass

    def create_actions(self) -> None:
        """Creates the actions."""
        pass

    def create_widgets(self) -> None:
        """Creates the widgets."""
        logger.info('Override this method: create_widgets.')

    def create_layouts(self) -> None:
        """Creates the layouts."""
        logger.info('Override this method: create_layouts.')

    def create_connections(self) -> None:
        """Creates the connections."""
        pass

    def reset_settings(self) -> None:
        """Resets the settings."""
        logger.info('Override this method: reset_settings.')

    def save_settings(self) -> None:
        """Saves the settings."""
        logger.info('Override this method: save_settings.')

    @staticmethod
    def show_preferences() -> None:
        """Shows the preferences."""
        logger.info('Override this method: preferences.')

    def on_top_bottom(self) -> None:
        """Sets the window on the top or bottom."""
        window_size = self.size()

        if self.is_on_top:
            self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint, False)
            self.show()

            self.on_top_bottom_action.setIcon(QtGui.QIcon(self.icons['arrow-alt-to-top.png']))

            self.is_on_top = False
        else:
            self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint, True)
            self.show()

            self.on_top_bottom_action.setIcon(QtGui.QIcon(self.icons['arrow-alt-to-top-yellow.png']))

            self.is_on_top = True

        self.resize(window_size)

    def show_about(self) -> None:
        """Shows the QAbout."""
        logger.info('Override this method: show_about.')

    def collapse_frame_layouts(self) -> None:
        """Collapses the QFrameLayouts of the UI."""
        logger.info('Override this method: collapse_frame_layouts.')

    def expand_frame_layouts(self) -> None:
        """Expands the QFrameLayouts of the UI."""
        logger.info('Override this method: expand_frame_layouts.')

    def load_settings(self) -> None:
        """Loads the settings."""
        logger.info('Override this method: load_settings.')

    def block_all_signals(self, widget: any = None) -> None:
        """Blocks all signals."""
        if not widget:
            widget = self

        widget.blockSignals(True)

        if hasattr(widget, 'children'):
            for child in widget.children():
                if hasattr(child, 'blockSignals'):
                    child.blockSignals(True)
                self.block_all_signals(child)

    def unblock_all_signals(self, widget: any = None) -> None:
        """Unblocks all signals."""
        if not widget:
            widget = self

        widget.blockSignals(False)

        if hasattr(widget, 'children'):
            for child in widget.children():
                if hasattr(child, 'blockSignals'):
                    child.blockSignals(False)
                self.unblock_all_signals(child)

    def closeEvent(self, event):
        """Close event."""
        if isinstance(self, QDialog):
            super(QDialog, self).closeEvent(event)

            self.geometry = self.saveGeometry()

    def showEvent(self, event):
        """Show event."""
        super(QDialog, self).showEvent(event)

        if self.geometry:
            self.restoreGeometry(self.geometry)
