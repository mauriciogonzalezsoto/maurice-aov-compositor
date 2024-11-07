"""
========================================================================================================================
Name: widgets_attributes.py
Author: Mauricio Gonzalez Soto
Updated Date: 11-06-2024

Copyright (C) 2024 Mauricio Gonzalez Soto. All rights reserved.
========================================================================================================================
"""
import maurice_aov_compositor.utils as maurice_utils

border_radius = maurice_utils.get_value_by_ppi(4, 6)
color = '#d7801a'
font_size = maurice_utils.get_value_by_ppi(11, 15)
spacing = maurice_utils.get_value_by_ppi(2, 3)
height = maurice_utils.get_value_by_ppi(20, 30)
width = maurice_utils.get_value_by_ppi(100, 126)

# QFrameLayout.
frame_layout_background_border_radius = maurice_utils.get_value_by_ppi(5, 7.5)
frame_layout_height = height
frame_layout_title_margin = maurice_utils.get_value_by_ppi(3, 5)

# QListWidget.
list_widget_icon_size = maurice_utils.get_value_by_ppi(14, 25), maurice_utils.get_value_by_ppi(14, 25)

# QMenuBar.
menu_bar_height = maurice_utils.get_value_by_ppi(24, 32)
menu_bar_icon_size = maurice_utils.get_value_by_ppi(16, 24), maurice_utils.get_value_by_ppi(16, 24)

# QPushButton.
push_button_height = maurice_utils.get_value_by_ppi(26, 40)
push_button_icon_size = maurice_utils.get_value_by_ppi(16, 24), maurice_utils.get_value_by_ppi(16, 24)
push_button_small_height = height
push_button_icon_small_size = maurice_utils.get_value_by_ppi(12, 24), maurice_utils.get_value_by_ppi(12, 24)
