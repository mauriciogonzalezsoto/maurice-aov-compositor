"""
========================================================================================================================
Name: aov_settings.py
Author: Mauricio Gonzalez Soto
Updated Date: 11-06-2024

Copyright (C) 2024 Mauricio Gonzalez Soto. All rights reserved.
========================================================================================================================
"""


class AOVSettings(object):
    """AVO settings."""
    AOVS = {}
    ADVANCED_KEYS = ()
    STANDARD_KEYS = ()

    def __init__(self):
        """Initializes class attributes."""
        self.standard_settings = None
        self.advanced_settings = None

    def get_aovs(self) -> dict:
        """Gets the AOVs settings."""
        return self.AOVS

    def get_advanced(self) -> dict:
        """Gets the advanced settings."""
        self.advanced_settings = {key: self.AOVS[key] for key in self.ADVANCED_KEYS}

        return self.advanced_settings

    def get_standard(self) -> dict:
        """Gets the standard settings."""
        self.standard_settings = {key: self.AOVS[key] for key in self.STANDARD_KEYS}

        return self.standard_settings
