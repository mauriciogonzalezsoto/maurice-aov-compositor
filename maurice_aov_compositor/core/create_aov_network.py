"""
========================================================================================================================
Name: create_aov_network.py
Author: Mauricio Gonzalez Soto
Updated Date: 11-06-2024

Copyright (C) 2024 Mauricio Gonzalez Soto. All rights reserved.
========================================================================================================================
"""
import nuke

from pathlib import Path
import os


class CreateAOVNetwork(object):
    """Create AOV network."""

    def __init__(self):
        """Initializes class attributes."""
        self.aovs_settings = {}

    def create_standard_network_from_multi_files(self) -> None:
        """Creates a standard network from multiple files."""
        files_paths = self.get_files_paths()

        if not files_paths:
            return

        last_merge_node = None
        x_pos = 0
        y_pos = 0

        for i, file_path in enumerate(files_paths):
            file_path, aov = file_path

            read_node = self.create_read_node(file_path=file_path)

            if i == 0:
                x_pos = read_node.xpos()
                y_pos = read_node.ypos()

            x_pos += 150

            read_node['xpos'].setValue(x_pos)
            read_node['ypos'].setValue(y_pos)

            shuffle_node = self.create_shuffle_node(aov='rgba', input_a=read_node, label=aov)
            shuffle_node['xpos'].setValue(x_pos)
            shuffle_node['ypos'].setValue(y_pos + 150)

            if i > 0:
                merge_node = self.create_merge_node(input_a=shuffle_node, input_b=last_merge_node)
                merge_node['xpos'].setValue(x_pos)
                merge_node['ypos'].setValue(y_pos + 300)
            else:
                dot_node_l = self.create_dot_node(input_a=shuffle_node)
                dot_node_l['xpos'].setValue(self.get_x_pos_center(node_a=shuffle_node, node_b=dot_node_l))
                dot_node_l['ypos'].setValue(y_pos + 303)

                merge_node = dot_node_l

            last_merge_node = merge_node

    def create_v_ray_advanced_network_from_single_file(self) -> None:
        """Creates a V-Ray advanced network from a single."""
        read_node = self.get_read_node()

        if not read_node:
            return

    def create_standard_network_from_single_file(self) -> None:
        """Creates a standard network from single a file."""
        read_node = self.get_read_node()

        if not read_node:
            return

        aovs = set()

        for channel in read_node.channels():
            channel_split = channel.split('.')

            if channel_split[1] in ['red', 'green', 'blue']:
                if channel_split[0] in self.aovs_settings.values():
                    aovs.add(channel_split[0])

        last_dot_node = read_node
        last_merge_node = None

        for i, aov in enumerate(sorted(list(aovs))):
            new_y_pos = read_node.ypos() + 125

            dot_node = self.create_dot_node(input_a=last_dot_node)
            dot_node['xpos'].setValue(self.get_x_pos_center(node_a=read_node, node_b=dot_node) + (150 * i))
            dot_node['ypos'].setValue(new_y_pos)

            shuffle_node = self.create_shuffle_node(aov=aov, input_a=dot_node, label=aov)
            shuffle_node['xpos'].setValue(self.get_x_pos_center(node_a=read_node, node_b=shuffle_node) + (150 * i))
            shuffle_node['ypos'].setValue(new_y_pos + 50)

            if i > 0:
                merge_node = self.create_merge_node(input_a=shuffle_node, input_b=last_merge_node)
                merge_node['xpos'].setValue(self.get_x_pos_center(node_a=read_node, node_b=merge_node) + (150 * i))
                merge_node['ypos'].setValue(new_y_pos + 200)
            else:
                dot_node_l = self.create_dot_node(input_a=shuffle_node)
                dot_node_l['xpos'].setValue(self.get_x_pos_center(node_a=shuffle_node, node_b=dot_node_l))
                dot_node_l['ypos'].setValue(new_y_pos + 203)

                merge_node = dot_node_l

            last_dot_node = dot_node
            last_merge_node = merge_node

    @staticmethod
    def create_dot_node(input_a) -> nuke.Node:
        """Creates a dot node."""
        dot_node = nuke.createNode('Dot')
        dot_node.setInput(0, input_a)
        dot_node.setSelected(False)

        return dot_node

    @staticmethod
    def create_merge_node(input_a: nuke.Node, input_b: nuke.Node) -> nuke.Node:
        """Create a merge node."""
        merge_node = nuke.createNode('Merge')
        merge_node.knob('operation').setValue('plus')
        merge_node.setInput(0, input_a)
        merge_node.setInput(1, input_b)
        merge_node.setSelected(False)

        return merge_node

    @staticmethod
    def create_read_node(file_path: str) -> nuke.Node:
        """Creates a read node."""
        read_node = nuke.createNode('Read')
        read_node.knob('file').setValue(file_path)
        read_node.setSelected(False)

        return read_node

    @staticmethod
    def create_shuffle_node(aov: str, input_a: nuke.Node, label: str) -> nuke.Node:
        """Creates a shuffle node."""
        shuffle_node = nuke.createNode('Shuffle2')
        shuffle_node.knob('in1').setValue(aov)
        shuffle_node.knob('label').setValue(label)
        shuffle_node.setInput(0, input_a)
        shuffle_node.setSelected(False)

        return shuffle_node

    def get_files_paths(self) -> list:
        """Gets the files paths."""
        target_file_path = nuke.getFilename('Select file', '*.exr')

        if not target_file_path:
            return []

        folder_path = os.path.dirname(target_file_path)
        files_names = os.listdir(folder_path)
        base_name = '.'.join(Path(target_file_path).stem.split('.')[:-1])

        files_paths = []

        for file_name in files_names:
            path = Path(file_name)

            if path.suffix == '.exr':
                file_name_split = path.stem.split('.')

                if len(file_name_split) > 1:
                    file_base_name = '.'.join(file_name_split[:-1])
                    aov_name = file_name_split[-1]

                    if file_base_name == base_name and aov_name in self.aovs_settings.values():
                        files_paths.append((f'{folder_path}/{file_name}', aov_name))

        return files_paths

    def get_read_node(self) -> nuke.Node | None:
        """Gets the read node."""
        read_node = nuke.selectedNodes('Read')

        if not read_node:
            file_path = nuke.getFilename('Select file', '*.exr')

            if not file_path:
                return

            read_node = self.create_read_node(file_path=file_path)
        else:
            read_node = read_node[-1]

        return read_node

    @staticmethod
    def get_x_pos_center(node_a: nuke.Node, node_b: nuke.Node) -> float:
        """Gets the X pos center."""
        return node_a.xpos() + (node_a.screenWidth() / 2) - (node_b.screenWidth() / 2)

    def set_aovs_settings(self, aovs: dict) -> None:
        """Sets AOVs settings."""
        self.aovs_settings = aovs
