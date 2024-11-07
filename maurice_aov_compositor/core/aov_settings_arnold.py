"""
========================================================================================================================
Name: aov_settings_arnold.py
Author: Mauricio Gonzalez Soto
Updated Date: 11-06-2024

Copyright (C) 2024 Mauricio Gonzalez Soto. All rights reserved.
========================================================================================================================
"""
from maurice_aov_compositor.core.aov_settings import AOVSettings


class AOVSettingsArnold(AOVSettings):
    """AVO settings Arnold."""
    AOVS = {
        'background': ['Background', 'background'],
        'coat': ['Coat', 'coat'],
        'diffuse': ['Diffuse', 'diffuse'],
        'direct': ['Direct', 'direct'],
        'emission': ['Emission', 'emission'],
        'indirect': ['Indirect', 'indirect'],
        'specular': ['Specular', 'specular'],
        'sss': ['SSS', 'sss'],
        'transmission': ['Transmission', 'transmission'],
        'volume': ['Volume', 'volume']
    }

    STANDARD_KEYS = (
        'direct',
        'indirect',
        'emission',
        'background'
    )

    ADVANCED_KEYS = (
        'diffuse',
        'specular',
        'coat',
        'transmission',
        'sss',
        'volume',
        'emission',
        'background'
    )

    def __init__(self):
        """Initializes class attributes."""
        super(AOVSettingsArnold, self).__init__()
