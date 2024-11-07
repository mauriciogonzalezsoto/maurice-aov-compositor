"""
========================================================================================================================
Name: maurice_paths.py
Author: Mauricio Gonzalez Soto
Updated Date: 11-05-2024

Copyright (C) 2024 Mauricio Gonzalez Soto. All rights reserved.
========================================================================================================================
"""
from pathlib import Path
from glob import glob
import os


def get_data_folder_path() -> str:
    """Gets the data folder path."""
    data_folder_path = os.path.join(get_root_path(), 'data')

    return data_folder_path


def get_files_in_folder(path: str) -> dict:
    """Gets files in folder."""
    files = {}

    for file_path in glob(os.path.join(path, '*')):
        file_path = file_path.replace('\\', '/')
        files[os.path.basename(file_path)] = file_path

    return files


def get_icons() -> dict:
    """Gets the icons."""
    icons = get_files_in_folder(get_icons_folder_path())

    return icons


def get_icons_folder_path() -> str:
    """Gets the icons folder path."""
    icons_folder_path = os.path.join(get_root_path(), 'icons')

    return icons_folder_path


def get_images() -> dict:
    """Gets the images."""
    images = get_files_in_folder(get_images_folder_path())

    return images


def get_images_folder_path() -> str:
    """Gets the images path."""
    images_folder_path = os.path.join(get_root_path(), 'images')

    return images_folder_path


def get_root_path() -> str:
    """Gets the root path."""
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    return root_path


def is_image(path: str) -> bool:
    """Checks if the path is an image."""
    if os.path.isfile(path):
        if Path(path).suffix in ['.exr', '.gif', '.hdr', '.jpg', '.jpeg', '.png', '.tif', '.tiff']:
            return True

    return False
