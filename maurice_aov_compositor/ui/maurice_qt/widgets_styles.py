"""
========================================================================================================================
Name: widgets_styles.py
Author: Mauricio Gonzalez Soto
Updated Date: 11-06-2024

Copyright (C) 2024 Mauricio Gonzalez Soto. All rights reserved.
========================================================================================================================
"""
import maurice_aov_compositor.ui.maurice_qt.widgets_attributes as widgets_attributes
import maurice_aov_compositor.utils as maurice_utils


icons = maurice_utils.get_icons()


def check_box_style() -> str:
    """QCheckBox style."""
    style = ('''
        QCheckBox {
            color: white; 
            font-size: %dpx;
        }
        
        QCheckBox:!enabled {
            color: rgb(112, 112, 112);
        }
        
        QCheckBox::indicator:checked {
            image: url(%s);
        }
        
        QCheckBox::indicator:checked:!enabled {
            image: url(%s);
        }
        
        QCheckBox::indicator:checked:hover {
            image: url(%s);
        }
        
        QCheckBox::indicator:unchecked {
            image: url(%s);
        }
        
        QCheckBox::indicator:unchecked:hover {
            image: url(%s);
        }
        
        QCheckBox::indicator {
            width: %dpx; 
            height: %dpx;
        }
        ''') % (
        widgets_attributes.font_size,
        icons['checkbox.png'],
        icons['checkbox-disabled.png'],
        icons['checkbox-checked-hover.png'],
        icons['checkbox-unchecked.png'],
        icons['checkbox-unchecked-hover.png'],
        maurice_utils.get_value_by_ppi(12, 18),
        maurice_utils.get_value_by_ppi(12, 18))

    return style


def check_button_style() -> str:
    """QCheckButton style."""
    style = ('''
        QPushButton {
            background-color: rgb(70, 70, 70); 
            border-radius: %dpx; 
            font-size: %dpx;
        }
        
        QPushButton:checked {
            background-color: rgb(45, 45, 45); 
            border: none;
        }
        
        QPushButton:hover {
            border: 2px solid %s;
        }
        ''') % (
        widgets_attributes.border_radius,
        widgets_attributes.font_size,
        widgets_attributes.color)

    return style


def combo_box_style() -> str:
    """QComboBox style."""
    style = ('''
        QComboBox {
            background-color: rgb(45, 45, 45); 
            border-radius: %dpx; 
            color: white; 
            font-size: %dpx;
            padding-left: %dpx;
        }

        QComboBox:!enabled {
            color: rgb(112, 112, 112);
        }

        QComboBox QAbstractItemView {
            color: white; 
            selection-background-color: %s;
        }

        QComboBox::drop-down {
            width: %dpx; 
            border-left-width: %dpx; 
            border-left-color: transparent;
            border-left-style: solid;
        }

        QComboBox:on {
            color: gray;
            padding-top: 0px; 
            padding-left: %dpx;
        }

        QComboBox::down-arrow {
            image: url(%s);
        }

        QComboBox::down-arrow {
            width: %dpx;
            height: %dpx;
        }
        
        QComboBox::separator {
            background-color: rgb(205, 25, 25);
            margin: 1px 0px 1px 0px;
            padding-top:120px;
            height: 100px;
        }
        ''') % (
        widgets_attributes.border_radius,
        widgets_attributes.font_size,
        maurice_utils.get_value_by_ppi(4, 7),
        widgets_attributes.color,
        maurice_utils.get_value_by_ppi(12, 18),
        maurice_utils.get_value_by_ppi(3, 5),
        maurice_utils.get_value_by_ppi(4, 7),
        icons['caret-down.png'],
        maurice_utils.get_value_by_ppi(12, 18),
        maurice_utils.get_value_by_ppi(12, 18))

    return style


def double_spin_box_style() -> str:
    """QDoubleSpinBox style."""
    style = ('''
        QDoubleSpinBox {
            background-color: rgb(45, 45, 45);
            border-radius: %dpx; 
            color: white;
            selection-background-color: %s; 
            font-size: %dpx;
        }
        
        QDoubleSpinBox:!enabled {
            color: #808080;
        }
        ''') % (
        widgets_attributes.border_radius,
        widgets_attributes.color,
        widgets_attributes.font_size)

    return style


def group_box_style() -> str:
    """QGroupBox style."""
    style = ('''
        QGroupBox {
            background-color: rgb(65, 65, 65); 
            border-radius: %dpx; 
            padding: %dpx;
        }
        ''') % (
        widgets_attributes.border_radius,
        maurice_utils.get_value_by_ppi(2, 3))

    return style


def label_style() -> str:
    """QLabel style."""
    style = ('''
    QLabel {
        color: white; 
        font-size: %dpx;
    }
                   
    QLabel:!enabled {
        color: #808080;
    }
    ''') % (
        widgets_attributes.font_size)

    return style


def line_edit_style() -> str:
    """QLineEdit style."""
    style = ('''
        QLineEdit {
            background-color: rgb(45, 45, 45); 
            border-radius: %dpx; 
            color: white;
            selection-background-color: %s; 
            font-size: %dpx; 
            padding-left: 4px;
        }
        
        QLineEdit:!enabled {
            color: rgb(128, 128, 128);
        }
        ''') % (
        widgets_attributes.border_radius,
        widgets_attributes.color,
        widgets_attributes.font_size)

    return style


def list_widget_style() -> str:
    """QListWidget style."""
    style = ('''
        QListWidget {
            border: 2px solid rgb(43, 43, 43); 
            border-radius: %dpx;
            font-size: %dpx;
        }
        
        QListWidget::item {
            color: white; 
        }
        
        QListWidget::item:selected {
            background: %s; 
            border: 2px solid %s; 
            border-radius: %dpx;
            color: black; 
            padding-left: -2px; 
            padding-top: 0px;
        }
        ''' + scroll_area_style()) % (
        widgets_attributes.border_radius,
        widgets_attributes.font_size,
        widgets_attributes.color,
        widgets_attributes.color,
        widgets_attributes.border_radius)

    return style


def menu_bar_style() -> str:
    """QMenuBar style."""
    style = ('''
        QMenuBar {
            background-color: rgb(45, 45, 45); 
            font-size: %dpx;
            padding: 1px 1px 1px %dpx;
            icon-size: %dpx;
        }
        
        QMenuBar::item {
            border-radius: 5px; 
            padding: 3px 3px 3px 3px;
        }
        
        QMenuBar::item:selected {
            background-color: %s;
        }
        
        QMenu {
            background-color: rgb(40, 40, 40);
        }
        
        QMenu::indicator {
            background-color: rgb(40, 40, 40);
            height: 27px;
            width: 36px;
            padding: -1px -1px 2px 0px;
        }
        
        QMenu::indicator:non-exclusive:checked {
            image: url(%s);
            padding: -1px -1px 2px 0px;
        }
        
        QMenu::indicator:non-exclusive:unchecked {
            image: url(%s);
        }
        
        QMenu::item {
            border-radius: 5px; 
            padding: 3px 50px 3px 15px;
            background-color: rgb(45, 45, 45);
            color: white;
            font-size: %dpx;
            margin: 1px 0px 1px 0px;
            min-width: %dpx;
            min-height: %dpx;
        }
        
        QMenu::item:selected {
            background-color: %s;
        }
        
        QMenu::icon {
            subcontrol-origin: padding;
            subcontrol-position: left center;
            background-color: rgb(40, 40, 40);
            padding: 6px
        }
        
        QMenu::right-arrow {
            image: url(%s);
            width: 24px; 
            height: 24px;
        }
        
        QMenu::separator {
            height: 1px;
            background-color: white;
            margin: 1px 0px 1px 0px;
            margin-left: auto;
        }
        ''') % (
        widgets_attributes.font_size,
        maurice_utils.get_value_by_ppi(-2, -4),
        maurice_utils.get_value_by_ppi(16, 24),
        widgets_attributes.color,
        icons['checkbox.png'],
        icons['checkbox-unchecked.png'],
        widgets_attributes.font_size,
        maurice_utils.get_value_by_ppi(80, 120),
        maurice_utils.get_value_by_ppi(16, 24),
        widgets_attributes.color,
        icons['caret-right.png'])

    return style


def progress_bar_style() -> str:
    """QProgressBar style."""
    style = ('''
        QProgressBar {
            border-radius: 5px; 
            text-align: center; 
            color: white;
        }
        
        QProgressBar::chunk {
            background: %s; 
            border-radius: 5px;
        }
        ''') % (
        widgets_attributes.color)

    return style


def push_button_style() -> str:
    """QPushButton style."""
    style = ('''
        QPushButton {
            background-color: rgb(45, 45, 45); 
            border-radius: %dpx; 
            color: white; 
            font-size: %dpx;
        }
        
        QPushButton:!enabled {
            color: rgb(128, 128, 128);
        }
        
        QPushButton:pressed {
            background-color: rgb(70, 70, 70);
            border: none;
        }
        
        QPushButton:hover {
            border: 2px solid %s;
        }
        
        QToolTip {
            background-color: rgb(45, 45, 45);
            color: white; 
            border: 1px solid %s; 
        }
        ''') % (
        widgets_attributes.border_radius,
        widgets_attributes.font_size,
        widgets_attributes.color,
        widgets_attributes.color)

    return style


def radio_button_style() -> str:
    """QRadioButton style."""
    style = ('''
        QRadioButton {
            color: white; 
            font-size: %dpx;
        }
                
        QRadioButton:!enabled {
            color: rgb(128, 128, 128);
        }
        
        QRadioButton::indicator:checked {
            image: url(%s);
        }
        
        QRadioButton::indicator:checked:!enabled {
            image: url(%s);
        }
        
        QRadioButton::indicator:checked:hover {
            image: url(%s);
        }
        
        QRadioButton::indicator:unchecked {
            image: url(%s);
        }
        
        QRadioButton::indicator:unchecked:!enabled {
            image: url(%s);
        }
        
        QRadioButton::indicator:unchecked:hover {
            image: url(%s);
        }
        
        QRadioButton::indicator {
            width: %dpx; 
            height: %dpx;
        }
        ''') % (
        widgets_attributes.font_size,
        icons['radio-button.png'],
        icons['radio-button-disabled.png'],
        icons['radio-button-checked-hover.png'],
        icons['radio-button-unchecked.png'],
        icons['radio-button-unchecked-disabled.png'],
        icons['radio-button-unchecked-hover.png'],
        maurice_utils.get_value_by_ppi(12, 18),
        maurice_utils.get_value_by_ppi(12, 18))

    return style


def scroll_area_style() -> str:
    """QScrollArea style."""
    scroll_area = ('''        
        QScrollArea {
            background-color: rgb(55, 55, 55);
            border: none;
        }

        QScrollBar:vertical {
            border: none;
            background-color: transparent;
            width: 18px;
            margin: 0px 0px 0px 2px;
        }
        
        QScrollBar::handle:vertical {
            background: rgb(43, 43, 43);
            min-height: 20px;
            border-radius: 6px;
        }
        
        QScrollBar::add-line:vertical {
            background: none;
            height: 10px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }
        
        QScrollBar::sub-line:vertical {
            background: none;
            height: 10px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }
        ''')

    return scroll_area


def spin_box_style() -> str:
    """QSpinBox style."""
    style = ('''
        QSpinBox {
            background-color: rgb(45, 45, 45);
            border-radius: %dpx;
            color: white;
            selection-background-color: %s; 
            font-size: %dpx;
        }
        
        QSpinBox:!enabled {
            color: rgb(128, 128, 128);
        }
        ''') % (
        widgets_attributes.border_radius,
        widgets_attributes.color,
        widgets_attributes.font_size)

    return style


def splitter_style() -> str:
    """QSplitter style."""
    style = ('''
        QSplitter::handle {
            background-color: transparent; 
            margin: %dpx;
        }
        ''') % (
        maurice_utils.get_value_by_ppi(-2, -4))

    return style


def tab_widget_style() -> str:
    """QTabWidget style."""
    style = ('''
        QTabWidget::pane {
            border: 0px;
            border-top: 2px solid #2b2b2b;
        }
        
        QTabBar::tab {
            background-color: #2b2b2b;
            color: rgb(43, 43, 43);
            border: none;
            border-radius: 4px;
            padding: 4px 6px 2px 6px;
            margin-right: 3px;
            margin-bottom: 1px;
        }
        
        QTabBar::tab:only-one {
            padding: 100px 10px 100px 10px;
        }
        
        QTabBar::tab:selected {
            background-color: rgb(45, 45, 45);
            color: white;
        }
        
        QTabBar::tab:!selected {
            background-color: rgb(70, 70, 70);
            color: white;
        }
        
        QTabBar::tab:first {
            margin-left: 0;
        }
        
        QTabBar::tab:last {
            margin-right: 0;
        }
        ''')

    return style


def tree_widget_style() -> str:
    """QTreeWidget style."""
    style = ('''
        QTreeWidget {
            border: 2px solid rgb(43, 43, 43); 
            border-radius: %dpx;
        }
        
        QTreeWidget::item:selected {
            background: %s; 
            border: 2px solid %s; 
            border-radius: %dpx;  
            color: black; 
            padding-left: -2px; 
            padding-top: 0px;
        }
        
        QTreeView::branch {
            background-color: rgb(43, 43, 43);
        }
        
        QTreeView::branch:open {
            image: url(%s);
        }
        
        QTreeView::branch:closed:has-children {
            image: url(%s);
        }
        
        QToolTip {
            background-color: rgb(45, 45, 45);
            color: white; 
            border: 1px solid %s; 
        }
        ''' + scroll_area_style()) % (
        widgets_attributes.border_radius,
        widgets_attributes.color,
        widgets_attributes.color,
        widgets_attributes.border_radius,
        icons['caret-down.png'],
        icons['caret-right.png'],
        widgets_attributes.color)

    return style


def widget_style() -> str:
    """QWidget style."""
    style = ('''
        QWidget[localStyle="true"] {
            background-color: rgb(60, 60, 60);
        }
        ''')

    return style
