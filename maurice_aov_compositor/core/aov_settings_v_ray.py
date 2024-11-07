"""
========================================================================================================================
Name: aov_settings_v_ray.py
Author: Mauricio Gonzalez Soto
Updated Date: 11-06-2024

Copyright (C) 2024 Mauricio Gonzalez Soto. All rights reserved.
========================================================================================================================
"""
from maurice_aov_compositor.core.aov_settings import AOVSettings


class AOVSettingsVRay(AOVSettings):
    """AVO settings V-Ray."""
    AOVS = {
        'atmospheric_effects': ['Atmosphere', 'atmosphere'],
        'background': ['Background', 'background'],
        'caustics': ['Caustics', 'caustics'],
        'diffuse': ['Diffuse', 'diffuse'],
        'gi': ['GI', 'GI'],
        'lighting': ['Lighting', 'lighting'],
        'raw_gi': ['Raw GI', 'rawGI'],
        'raw_lighting': ['Raw Lighting', 'rawLight'],
        'raw_reflection': ['Raw Reflection', 'rawReflection'],
        'raw_refraction': ['Raw Refraction', 'rawRefraction'],
        'reflection': ['Reflection', 'reflect'],
        'reflection_filter': ['Reflection Filter', 'reflectionFilter'],
        'refraction': ['Refraction', 'refract'],
        'refraction_filter': ['Refraction Filter', 'refractionFilter'],
        'sss': ['SSS', 'SSS'],
        'self_illumination': ['Self-Illumination', 'selfIllum'],
        'specular': ['Specular', 'specular']
    }

    STANDARD_KEYS = (
        'atmospheric_effects',
        'background',
        'caustics',
        'gi',
        'lighting',
        'reflection',
        'refraction',
        'sss',
        'self_illumination',
        'specular'
    )

    ADVANCED_KEYS = (
        'atmospheric_effects',
        'background',
        'caustics',
        'diffuse',
        'raw_gi',
        'raw_lighting',
        'raw_reflection',
        'raw_refraction',
        'reflection_filter',
        'refraction_filter',
        'sss',
        'self_illumination',
        'specular'
    )

    def __init__(self):
        """Initializes class attributes."""
        super(AOVSettingsVRay, self).__init__()
