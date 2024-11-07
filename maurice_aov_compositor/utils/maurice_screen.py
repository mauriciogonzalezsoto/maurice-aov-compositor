"""
========================================================================================================================
Name: maurice_screen.py
Author: Mauricio Gonzalez Soto
Updated Date: 11-06-2024

Copyright (C) 2024 Mauricio Gonzalez Soto. All rights reserved.
========================================================================================================================
"""
from ctypes import windll
from typing import Union

import maurice_aov_compositor as maurice


def get_ppi() -> int:
    """Gets the PPI of the screen."""
    user32 = windll.user32
    user32.SetProcessDPIAware()
    pix_per_inch = windll.gdi32.GetDeviceCaps(user32.GetDC(0), 88)

    return pix_per_inch


def get_value_by_ppi(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Gets the value by PPI."""
    value = a if maurice.PPI < 144 else b

    return value
