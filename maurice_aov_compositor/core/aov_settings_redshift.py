"""
========================================================================================================================
Name: aov_settings_redshift.py
Author: Mauricio Gonzalez Soto
Updated Date: 11-06-2024

Copyright (C) 2024 Mauricio Gonzalez Soto. All rights reserved.
========================================================================================================================
"""
from maurice_aov_compositor.core.aov_settings import AOVSettings


class AOVSettingsRedshift(AOVSettings):
    """AVO settings Redshift."""
    AOVS = {}
    ADVANCED_KEYS = ()
    STANDARD_KEYS = ()

    def __init__(self):
        """Initializes class attributes."""
        super(AOVSettingsRedshift, self).__init__()
