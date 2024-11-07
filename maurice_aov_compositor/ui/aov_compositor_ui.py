"""
========================================================================================================================
Name: aov_compositor_ui.py
Author: Mauricio Gonzalez Soto
Updated Date: 11-06-2024

Copyright (C) 2024 Mauricio Gonzalez Soto. All rights reserved.
========================================================================================================================
"""
try:
    from PySide6 import QtWidgets
    from PySide6 import QtCore
    from PySide6 import QtGui
except ImportError:
    from PySide2 import QtWidgets
    from PySide2 import QtCore
    from PySide2 import QtGui

import os

from maurice_aov_compositor.core.aov_settings_redshift import AOVSettingsRedshift
from maurice_aov_compositor.core.aov_settings_arnold import AOVSettingsArnold
from maurice_aov_compositor.core.aov_settings_v_ray import AOVSettingsVRay
from maurice_aov_compositor.core.create_aov_network import CreateAOVNetwork
import maurice_aov_compositor.ui.maurice_qt as maurice_qt
import maurice_aov_compositor.utils as maurice_utils
import maurice_aov_compositor as maurice

    
class AOVCompositorUI(maurice_qt.QDialogNuke):
    """AOV compositor UI."""
    WINDOW_HEIGHT = 400
    WINDOW_NAME = maurice.AOV_COMPOSITOR_WINDOW_NAME
    WINDOW_TITLE = maurice.AOV_COMPOSITOR
    WINDOW_WIDTH = 600

    CONFIG_PATH = os.path.join(maurice_utils.get_data_folder_path(), f'{WINDOW_NAME}.ini')

    ARNOLD = 'Arnold'
    REDSHIFT = 'Redshift'
    V_RAY = 'V-Ray'

    STANDARD = 'Standard'
    ADVANCED = 'Advanced'

    @classmethod
    def show_window(cls) -> None:
        """Shows the window."""
        if not cls.window_instance:
            cls.window_instance = AOVCompositorUI()

        super(AOVCompositorUI, cls).show_window()

    def __init__(self):
        """Initializes class attributes."""
        # Settings class variables.
        self.render_engine_combo_box = None
        self.from_single_file_radio_button = None
        self.from_separate_files_radio_button = None
        self.create_aov_network_push_button = None

        # AOV compositor class variables.
        self.render_compositing_operations_combo_box = None

        # Arnold compositor class variables.
        self.arnold_aov_compositor_group_box = None
        self.arnold_aov_compositor_widget = None
        self.arnold_background_widget = None
        self.arnold_coat_widget = None
        self.arnold_diffuse_widget = None
        self.arnold_direct_widget = None
        self.arnold_emission_widget = None
        self.arnold_indirect_widget = None
        self.arnold_sss_widget = None
        self.arnold_specular_widget = None
        self.arnold_transmission_widget = None
        self.arnold_volume_widget = None
        
        # V-Ray compositor class variables.
        self.v_ray_aov_compositor_group_box = None
        self.v_ray_aov_compositor_widget = None
        self.v_ray_atmosphere_widget = None
        self.v_ray_background_widget = None
        self.v_ray_caustics_widget = None
        self.v_ray_diffuse_widget = None
        self.v_ray_gi_widget = None
        self.v_ray_lighting_widget = None
        self.v_ray_raw_gi_widget = None
        self.v_ray_raw_lighting_widget = None
        self.v_ray_raw_reflection_widget = None
        self.v_ray_raw_refraction_widget = None
        self.v_ray_reflection_widget = None
        self.v_ray_reflection_filter_widget = None
        self.v_ray_refraction_widget = None
        self.v_ray_refraction_filter_widget = None
        self.v_ray_sss_widget = None
        self.v_ray_self_illumination_widget = None
        self.v_ray_specular_widget = None

        # Arnold settings.
        self.arnold_aov_settings = AOVSettingsArnold()
        self.arnold_aovs = self.arnold_aov_settings.get_aovs()
        self.arnold_advanced_mode = self.arnold_aov_settings.get_advanced()
        self.arnold_standard_mode = self.arnold_aov_settings.get_standard()
        
        # Redshift settings.
        self.redshift_aov_settings = AOVSettingsRedshift()
        self.redshift_aovs = self.redshift_aov_settings.get_aovs()
        self.redshift_advanced_mode = self.redshift_aov_settings.get_advanced()
        self.redshift_standard_mode = self.redshift_aov_settings.get_standard()

        # V-Ray settings.
        self.v_ray_aov_settings = AOVSettingsVRay()
        self.v_ray_aovs = self.v_ray_aov_settings.get_aovs()
        self.v_ray_advanced_mode = self.v_ray_aov_settings.get_advanced()
        self.v_ray_standard_mode = self.v_ray_aov_settings.get_standard()
        
        super(AOVCompositorUI, self).__init__()

        # QDialog settings.
        self.setMinimumHeight(self.WINDOW_HEIGHT)
        self.setMinimumWidth(self.WINDOW_WIDTH)

        self.render_compositing_operations_current_text_changed_combo_box()

    def create_widgets(self) -> None:
        """Creates the widgets."""
        # ==============================================================================================================
        # Settings.
        # ==============================================================================================================
        # Render engine QComboBox.
        self.render_engine_combo_box = maurice_qt.QComboBox(fixed_size=False)
        self.render_engine_combo_box.addItems([
            AOVCompositorUI.ARNOLD,
            AOVCompositorUI.REDSHIFT,
            AOVCompositorUI.V_RAY])

        # From single file QRadioButton.
        self.from_single_file_radio_button = maurice_qt.QRadioButton('From Single File')
        self.from_single_file_radio_button.setChecked(True)

        # From separate files QRadioButton.
        self.from_separate_files_radio_button = maurice_qt.QRadioButton('From Separate Files')

        # Create aov network QPushButton.
        self.create_aov_network_push_button = maurice_qt.QPushButton('Create AOV Network')
        self.create_aov_network_push_button.setIcon(QtGui.QIcon(self.icons['chart-tree.png']))
        self.create_aov_network_push_button.setToolTip(lmb='Create Image Network')
        self.create_aov_network_push_button.set_yellow_background()

        # ==============================================================================================================
        # AOV compositor.
        # ==============================================================================================================
        # Render compositing operations QComboBox.
        self.render_compositing_operations_combo_box = maurice_qt.QComboBox(fixed_size=False)
        self.render_compositing_operations_combo_box.addItems([
            AOVCompositorUI.STANDARD,
            AOVCompositorUI.ADVANCED])

        # ==============================================================================================================
        # Arnold AOV compositor.
        # ==============================================================================================================
        # Arnold background widget.
        self.arnold_background_widget = AOVSettingsWidget()
        self.arnold_background_widget.set_aov_name(self.arnold_aovs['background'][0])
        self.arnold_background_widget.set_aov_suffix(self.arnold_aovs['background'][1])

        # Arnold coat widget.
        self.arnold_coat_widget = AOVSettingsWidget()
        self.arnold_coat_widget.set_aov_name(self.arnold_aovs['coat'][0])
        self.arnold_coat_widget.set_aov_suffix(self.arnold_aovs['coat'][1])

        # Arnold diffuse widget.
        self.arnold_diffuse_widget = AOVSettingsWidget()
        self.arnold_diffuse_widget.set_aov_name(self.arnold_aovs['diffuse'][0])
        self.arnold_diffuse_widget.set_aov_suffix(self.arnold_aovs['diffuse'][1])

        # Arnold direct widget.
        self.arnold_direct_widget = AOVSettingsWidget()
        self.arnold_direct_widget.set_aov_name(self.arnold_aovs['direct'][0])
        self.arnold_direct_widget.set_aov_suffix(self.arnold_aovs['direct'][1])

        # Arnold emission widget.
        self.arnold_emission_widget = AOVSettingsWidget()
        self.arnold_emission_widget.set_aov_name(self.arnold_aovs['emission'][0])
        self.arnold_emission_widget.set_aov_suffix(self.arnold_aovs['emission'][1])

        # Arnold indirect widget.
        self.arnold_indirect_widget = AOVSettingsWidget()
        self.arnold_indirect_widget.set_aov_name(self.arnold_aovs['indirect'][0])
        self.arnold_indirect_widget.set_aov_suffix(self.arnold_aovs['indirect'][1])

        # Arnold SSS widget.
        self.arnold_sss_widget = AOVSettingsWidget()
        self.arnold_sss_widget.set_aov_name(self.arnold_aovs['sss'][0])
        self.arnold_sss_widget.set_aov_suffix(self.arnold_aovs['sss'][1])

        # Arnold specular widget.
        self.arnold_specular_widget = AOVSettingsWidget()
        self.arnold_specular_widget.set_aov_name(self.arnold_aovs['specular'][0])
        self.arnold_specular_widget.set_aov_suffix(self.arnold_aovs['specular'][1])

        # Arnold transmission widget.
        self.arnold_transmission_widget = AOVSettingsWidget()
        self.arnold_transmission_widget.set_aov_name(self.arnold_aovs['transmission'][0])
        self.arnold_transmission_widget.set_aov_suffix(self.arnold_aovs['transmission'][1])

        # Arnold volume widget.
        self.arnold_volume_widget = AOVSettingsWidget()
        self.arnold_volume_widget.set_aov_name(self.arnold_aovs['volume'][0])
        self.arnold_volume_widget.set_aov_suffix(self.arnold_aovs['volume'][1])

        # ==============================================================================================================
        # V-Ray AOV compositor.
        # ==============================================================================================================
        # V-Ray atmosphere widget.
        self.v_ray_atmosphere_widget = AOVSettingsWidget()
        self.v_ray_atmosphere_widget.set_aov_name(self.v_ray_aovs['atmospheric_effects'][0])
        self.v_ray_atmosphere_widget.set_aov_suffix(self.v_ray_aovs['atmospheric_effects'][1])

        # V-Ray background widget.
        self.v_ray_background_widget = AOVSettingsWidget()
        self.v_ray_background_widget.set_aov_name(self.v_ray_aovs['background'][0])
        self.v_ray_background_widget.set_aov_suffix(self.v_ray_aovs['background'][1])

        # V-Ray caustics widget.
        self.v_ray_caustics_widget = AOVSettingsWidget()
        self.v_ray_caustics_widget.set_aov_name(self.v_ray_aovs['caustics'][0])
        self.v_ray_caustics_widget.set_aov_suffix(self.v_ray_aovs['caustics'][1])

        # V-Ray diffuse widget.
        self.v_ray_diffuse_widget = AOVSettingsWidget()
        self.v_ray_diffuse_widget.set_aov_name(self.v_ray_aovs['diffuse'][0])
        self.v_ray_diffuse_widget.set_aov_suffix(self.v_ray_aovs['diffuse'][1])

        # V-Ray GI widget.
        self.v_ray_gi_widget = AOVSettingsWidget()
        self.v_ray_gi_widget.set_aov_name(self.v_ray_aovs['gi'][0])
        self.v_ray_gi_widget.set_aov_suffix(self.v_ray_aovs['gi'][1])

        # V-Ray lighting widget.
        self.v_ray_lighting_widget = AOVSettingsWidget()
        self.v_ray_lighting_widget.set_aov_name(self.v_ray_aovs['lighting'][0])
        self.v_ray_lighting_widget.set_aov_suffix(self.v_ray_aovs['lighting'][1])

        # V-Ray raw GI widget.
        self.v_ray_raw_gi_widget = AOVSettingsWidget()
        self.v_ray_raw_gi_widget.set_aov_name(self.v_ray_aovs['raw_gi'][0])
        self.v_ray_raw_gi_widget.set_aov_suffix(self.v_ray_aovs['raw_gi'][1])

        # V-Ray raw lighting widget.
        self.v_ray_raw_lighting_widget = AOVSettingsWidget()
        self.v_ray_raw_lighting_widget.set_aov_name(self.v_ray_aovs['raw_lighting'][0])
        self.v_ray_raw_lighting_widget.set_aov_suffix(self.v_ray_aovs['raw_lighting'][1])

        # V-Ray raws reflection widget.
        self.v_ray_raw_reflection_widget = AOVSettingsWidget()
        self.v_ray_raw_reflection_widget.set_aov_name(self.v_ray_aovs['raw_reflection'][0])
        self.v_ray_raw_reflection_widget.set_aov_suffix(self.v_ray_aovs['raw_reflection'][1])

        # V-Ray raw refraction widget.
        self.v_ray_raw_refraction_widget = AOVSettingsWidget()
        self.v_ray_raw_refraction_widget.set_aov_name(self.v_ray_aovs['raw_refraction'][0])
        self.v_ray_raw_refraction_widget.set_aov_suffix(self.v_ray_aovs['raw_refraction'][1])

        # V-Ray reflection widget.
        self.v_ray_reflection_widget = AOVSettingsWidget()
        self.v_ray_reflection_widget.set_aov_name(self.v_ray_aovs['reflection'][0])
        self.v_ray_reflection_widget.set_aov_suffix(self.v_ray_aovs['reflection'][1])

        # V-Ray reflection filter widget.
        self.v_ray_reflection_filter_widget = AOVSettingsWidget()
        self.v_ray_reflection_filter_widget.set_aov_name(self.v_ray_aovs['reflection_filter'][0])
        self.v_ray_reflection_filter_widget.set_aov_suffix(self.v_ray_aovs['reflection_filter'][1])

        # V-Ray refraction widget.
        self.v_ray_refraction_widget = AOVSettingsWidget()
        self.v_ray_refraction_widget.set_aov_name(self.v_ray_aovs['refraction'][0])
        self.v_ray_refraction_widget.set_aov_suffix(self.v_ray_aovs['refraction'][1])

        # V-Ray refraction filter widget.
        self.v_ray_refraction_filter_widget = AOVSettingsWidget()
        self.v_ray_refraction_filter_widget.set_aov_name(self.v_ray_aovs['refraction_filter'][0])
        self.v_ray_refraction_filter_widget.set_aov_suffix(self.v_ray_aovs['refraction_filter'][1])

        # V-Ray SSS widget.
        self.v_ray_sss_widget = AOVSettingsWidget()
        self.v_ray_sss_widget.set_aov_name(self.v_ray_aovs['sss'][0])
        self.v_ray_sss_widget.set_aov_suffix(self.v_ray_aovs['sss'][1])

        # V-Ray self illumination widget.
        self.v_ray_self_illumination_widget = AOVSettingsWidget()
        self.v_ray_self_illumination_widget.set_aov_name(self.v_ray_aovs['self_illumination'][0])
        self.v_ray_self_illumination_widget.set_aov_suffix(self.v_ray_aovs['self_illumination'][1])

        # V-Ray specular widget.
        self.v_ray_specular_widget = AOVSettingsWidget()
        self.v_ray_specular_widget.set_aov_name(self.v_ray_aovs['specular'][0])
        self.v_ray_specular_widget.set_aov_suffix(self.v_ray_aovs['specular'][1])

    def create_layouts(self) -> None:
        """Creates the layout."""
        # ==============================================================================================================
        # Settings.
        # ==============================================================================================================
        # Main QSplitter.
        main_splitter = QtWidgets.QSplitter()
        self.main_layout.addWidget(main_splitter)

        # Settings QWidget.
        settings_widget = QtWidgets.QWidget()
        main_splitter.addWidget(settings_widget)

        # Settings main QVBoxLayout.
        settings_main_v_box_layout = maurice_qt.QVBoxLayout()
        settings_main_v_box_layout.addWidget(self.render_engine_combo_box)
        settings_widget.setLayout(settings_main_v_box_layout)

        # Settings file QGroupbox.
        settings_file_group_box = maurice_qt.QGroupBox()
        settings_main_v_box_layout.addWidget(settings_file_group_box)

        # Settings file QFormLayout.
        settings_file_form_layout = maurice_qt.QFormLayout()
        settings_file_form_layout.addWidget(self.from_single_file_radio_button)
        settings_file_form_layout.addWidget(self.from_separate_files_radio_button)
        settings_file_form_layout.setContentsMargins(80, 0, 0, 0)
        settings_file_group_box.setLayout(settings_file_form_layout)

        settings_main_v_box_layout.addStretch()
        settings_main_v_box_layout.addWidget(self.create_aov_network_push_button)

        # ==============================================================================================================
        # AOV compositor.
        # ==============================================================================================================
        # AOV compositor QWidget.
        aov_compositor_widget = QtWidgets.QWidget()
        main_splitter.addWidget(aov_compositor_widget)

        # AOV compositor QVBoxLayout.
        aov_compositor_v_box_layout = maurice_qt.QVBoxLayout()
        aov_compositor_v_box_layout.addWidget(self.render_compositing_operations_combo_box)
        aov_compositor_widget.setLayout(aov_compositor_v_box_layout)

        # ==============================================================================================================
        # Arnold AOV compositor.
        # ==============================================================================================================
        # Arnold AOV compositor QGroupBox.
        self.arnold_aov_compositor_group_box = QtWidgets.QGroupBox()
        self.arnold_aov_compositor_group_box.setStyleSheet('''
            QGroupBox {
                background-color: rgb(35, 35, 35); 
                border-radius: %dpx;
                padding: %dpx;}
                ''' % (
            maurice_qt.widgets_attributes.border_radius,
            4))
        aov_compositor_v_box_layout.addWidget(self.arnold_aov_compositor_group_box)

        # Arnold AOV compositor QVBoxKLayout.
        arnold_aov_compositor_v_box_layout = maurice_qt.QVBoxLayout()
        self.arnold_aov_compositor_group_box.setLayout(arnold_aov_compositor_v_box_layout)

        # Arnold AOV compositor QScrollArea.
        arnold_aov_compositor_scroll_area = maurice_qt.QScrollArea()
        arnold_aov_compositor_v_box_layout.addWidget(arnold_aov_compositor_scroll_area)

        # Arnold AOV compositor QWidget.
        self.arnold_aov_compositor_widget = QtWidgets.QWidget()
        self.arnold_aov_compositor_widget.setProperty('localStyle', True)
        self.arnold_aov_compositor_widget.setStyleSheet(
            'QWidget[localStyle="true"] {background-color: rgb(35, 35, 35);}')
        arnold_aov_compositor_scroll_area.setWidget(self.arnold_aov_compositor_widget)

        # Arnold AOV compositor items QVBoxKLayout.
        arnold_aov_compositor_items_v_box_layout = maurice_qt.QVBoxLayout()
        arnold_aov_compositor_items_v_box_layout.addWidget(self.arnold_background_widget)
        arnold_aov_compositor_items_v_box_layout.addWidget(self.arnold_coat_widget)
        arnold_aov_compositor_items_v_box_layout.addWidget(self.arnold_diffuse_widget)
        arnold_aov_compositor_items_v_box_layout.addWidget(self.arnold_direct_widget)
        arnold_aov_compositor_items_v_box_layout.addWidget(self.arnold_emission_widget)
        arnold_aov_compositor_items_v_box_layout.addWidget(self.arnold_indirect_widget)
        arnold_aov_compositor_items_v_box_layout.addWidget(self.arnold_sss_widget)
        arnold_aov_compositor_items_v_box_layout.addWidget(self.arnold_specular_widget)
        arnold_aov_compositor_items_v_box_layout.addWidget(self.arnold_transmission_widget)
        arnold_aov_compositor_items_v_box_layout.addWidget(self.arnold_volume_widget)
        arnold_aov_compositor_items_v_box_layout.setAlignment(QtCore.Qt.AlignTop)
        self.arnold_aov_compositor_widget.setLayout(arnold_aov_compositor_items_v_box_layout)

        # ==============================================================================================================
        # V-Ray AOV compositor.
        # ==============================================================================================================
        # V-Ray AOV compositor QGroupBox.
        self.v_ray_aov_compositor_group_box = QtWidgets.QGroupBox()
        self.v_ray_aov_compositor_group_box.setStyleSheet('''
            QGroupBox {
                background-color: rgb(35, 35, 35); 
                border-radius: %dpx;
                padding: %dpx;}
                ''' % (
            maurice_qt.widgets_attributes.border_radius,
            4))
        self.v_ray_aov_compositor_group_box.setVisible(False)
        aov_compositor_v_box_layout.addWidget(self.v_ray_aov_compositor_group_box)

        # V-Ray AOV compositor QVBoxKLayout.
        v_ray_aov_compositor_v_box_layout = maurice_qt.QVBoxLayout()
        self.v_ray_aov_compositor_group_box.setLayout(v_ray_aov_compositor_v_box_layout)

        # V-Ray AOV compositor QScrollArea.
        v_ray_aov_compositor_scroll_area = maurice_qt.QScrollArea()
        v_ray_aov_compositor_v_box_layout.addWidget(v_ray_aov_compositor_scroll_area)

        # V-Ray AOV compositor QWidget.
        self.v_ray_aov_compositor_widget = QtWidgets.QWidget()
        self.v_ray_aov_compositor_widget.setProperty('localStyle', True)
        self.v_ray_aov_compositor_widget.setStyleSheet(
            'QWidget[localStyle="true"] {background-color: rgb(35, 35, 35);}')
        v_ray_aov_compositor_scroll_area.setWidget(self.v_ray_aov_compositor_widget)

        # V-Ray AOV compositor items QVBoxKLayout.
        v_ray_aov_compositor_items_v_box_layout = maurice_qt.QVBoxLayout()
        v_ray_aov_compositor_items_v_box_layout.addWidget(self.v_ray_atmosphere_widget)
        v_ray_aov_compositor_items_v_box_layout.addWidget(self.v_ray_background_widget)
        v_ray_aov_compositor_items_v_box_layout.addWidget(self.v_ray_caustics_widget)
        v_ray_aov_compositor_items_v_box_layout.addWidget(self.v_ray_diffuse_widget)
        v_ray_aov_compositor_items_v_box_layout.addWidget(self.v_ray_gi_widget)
        v_ray_aov_compositor_items_v_box_layout.addWidget(self.v_ray_lighting_widget)
        v_ray_aov_compositor_items_v_box_layout.addWidget(self.v_ray_raw_gi_widget)
        v_ray_aov_compositor_items_v_box_layout.addWidget(self.v_ray_raw_lighting_widget)
        v_ray_aov_compositor_items_v_box_layout.addWidget(self.v_ray_raw_reflection_widget)
        v_ray_aov_compositor_items_v_box_layout.addWidget(self.v_ray_raw_refraction_widget)
        v_ray_aov_compositor_items_v_box_layout.addWidget(self.v_ray_reflection_widget)
        v_ray_aov_compositor_items_v_box_layout.addWidget(self.v_ray_reflection_filter_widget)
        v_ray_aov_compositor_items_v_box_layout.addWidget(self.v_ray_refraction_widget)
        v_ray_aov_compositor_items_v_box_layout.addWidget(self.v_ray_refraction_filter_widget)
        v_ray_aov_compositor_items_v_box_layout.addWidget(self.v_ray_sss_widget)
        v_ray_aov_compositor_items_v_box_layout.addWidget(self.v_ray_self_illumination_widget)
        v_ray_aov_compositor_items_v_box_layout.addWidget(self.v_ray_specular_widget)
        v_ray_aov_compositor_items_v_box_layout.setAlignment(QtCore.Qt.AlignTop)
        self.v_ray_aov_compositor_widget.setLayout(v_ray_aov_compositor_items_v_box_layout)

        main_splitter.setCollapsible(0, False)
        main_splitter.setCollapsible(1, False)
        main_splitter.setStretchFactor(1, 1)

    def create_connections(self) -> None:
        """Creates the connections."""
        self.render_engine_combo_box.currentTextChanged.connect(self.render_engine_current_text_changed_combo_box)
        self.create_aov_network_push_button.clicked.connect(self.create_aov_network_clicked_push_button)

        self.render_compositing_operations_combo_box.currentTextChanged.connect(
            self.render_compositing_operations_current_text_changed_combo_box)

    def load_settings(self) -> None:
        """Loads the settings."""
        pass

    def render_engine_current_text_changed_combo_box(self) -> None:
        """"""
        render_engine = self.render_engine_combo_box.currentText()

        self.arnold_aov_compositor_group_box.setVisible(render_engine == AOVCompositorUI.ARNOLD)
        self.v_ray_aov_compositor_group_box.setVisible(render_engine == AOVCompositorUI.V_RAY)

        self.render_compositing_operations_current_text_changed_combo_box()

    def render_compositing_operations_current_text_changed_combo_box(self) -> None:
        """"""
        render_engine = self.render_engine_combo_box.currentText()

        aov_compositor_widget = None
        standard_mode = None
        advanced_mode = None

        if render_engine == AOVCompositorUI.ARNOLD:
            aov_compositor_widget = self.arnold_aov_compositor_widget
            standard_mode = self.arnold_standard_mode
            advanced_mode = self.arnold_advanced_mode
        elif render_engine == AOVCompositorUI.REDSHIFT:
            aov_compositor_widget = None
            standard_mode = None
            advanced_mode = None
        elif render_engine == AOVCompositorUI.V_RAY:
            aov_compositor_widget = self.v_ray_aov_compositor_widget
            standard_mode = self.v_ray_standard_mode
            advanced_mode = self.v_ray_advanced_mode

        if aov_compositor_widget:
            self.display_aov_compositor_widgets(
                aov_compositor_widget=aov_compositor_widget,
                advanced_mode=advanced_mode,
                standard_mode=standard_mode)

    def create_aov_network_clicked_push_button(self) -> None:
        """"""
        render_engine = self.render_engine_combo_box.currentText()

        if render_engine == AOVCompositorUI.ARNOLD:
            self.arnold_create_image_network()
        elif render_engine == AOVCompositorUI.REDSHIFT:
            self.redshift_create_image_network()
        elif render_engine == AOVCompositorUI.V_RAY:
            self.v_ray_create_image_network()

    def display_aov_compositor_widgets(self, aov_compositor_widget: QtWidgets.QWidget, advanced_mode: dict,
                                       standard_mode: dict) -> None:
        """Displays the AOV compositor widgets."""
        render_compositing_operation = self.render_compositing_operations_combo_box.currentText()

        for aov_widget in aov_compositor_widget.children():
            if isinstance(aov_widget, AOVSettingsWidget):
                aov_name = aov_widget.get_aov_name()

                aov_widget.setVisible(False)

                if AOVCompositorUI.STANDARD == render_compositing_operation:
                    for value in standard_mode.values():
                        if aov_name == value[0]:
                            aov_widget.setVisible(True)
                elif AOVCompositorUI.ADVANCED == render_compositing_operation:
                    for value in advanced_mode.values():
                        if aov_name == value[0]:
                            aov_widget.setVisible(True)

    def get_current_aovs_settings(self, aov_compositor_widget: QtWidgets.QWidget, advanced_mode: dict,
                                  standard_mode: dict) -> dict:
        """Gets current AOVs settings."""
        render_compositing_operation = self.render_compositing_operations_combo_box.currentText()
        aovs = {}

        for aov_widget in aov_compositor_widget.children():
            if isinstance(aov_widget, AOVSettingsWidget):
                aov_name = aov_widget.get_aov_name()
                aov_suffix = aov_widget.get_aov_suffix()

                if AOVCompositorUI.STANDARD == render_compositing_operation:
                    for key, value in standard_mode.items():
                        if aov_name == value[0]:
                            aovs[key] = aov_suffix
                elif AOVCompositorUI.ADVANCED == render_compositing_operation:
                    for key, value in advanced_mode.items():
                        if aov_name == value[0]:
                            aovs[key] = aov_suffix

        return aovs

    def arnold_create_image_network(self) -> None:
        """Arnold creates the image network."""
        aovs = self.get_current_aovs_settings(
            aov_compositor_widget=self.arnold_aov_compositor_widget,
            advanced_mode=self.arnold_advanced_mode,
            standard_mode=self.arnold_standard_mode)

        aov_network = CreateAOVNetwork()
        aov_network.set_aovs_settings(aovs=aovs)

        if self.from_single_file_radio_button.isChecked():
            aov_network.create_standard_network_from_single_file()
        elif self.from_separate_files_radio_button.isChecked():
            aov_network.create_standard_network_from_multi_files()

    def redshift_create_image_network(self) -> None:
        """Redshift creates the image network."""
        # render_compositing_operation = self.render_compositing_operations_combo_box.currentText()
        # aovs = {}

        print('TODO: Redshift create image network.')

    def v_ray_create_image_network(self) -> None:
        """V-Ray creates the image network."""
        render_compositing_operation = self.render_compositing_operations_combo_box.currentText()
        aovs = self.get_current_aovs_settings(
            aov_compositor_widget=self.v_ray_aov_compositor_widget,
            advanced_mode=self.v_ray_advanced_mode,
            standard_mode=self.v_ray_standard_mode)

        aov_network = CreateAOVNetwork()
        aov_network.set_aovs_settings(aovs=aovs)

        if self.from_single_file_radio_button.isChecked():
            if AOVCompositorUI.STANDARD == render_compositing_operation:
                aov_network.create_standard_network_from_single_file()
            elif AOVCompositorUI.ADVANCED == render_compositing_operation:
                print('TODO: V-Ray Advanced Single File.')
        elif self.from_separate_files_radio_button.isChecked():
            if AOVCompositorUI.STANDARD == render_compositing_operation:
                aov_network.create_standard_network_from_multi_files()
            elif AOVCompositorUI.ADVANCED == render_compositing_operation:
                print('TODO: V-Ray Advanced Multi Files.')

    def showEvent(self, event):
        """Shows event."""
        super(AOVCompositorUI, self).showEvent(event)


class AOVSettingsWidget(QtWidgets.QWidget):
    """AOV settings widget."""
    edit_texture_clicked = QtCore.Signal()

    def __init__(self):
        """Initializes class attributes."""
        super(AOVSettingsWidget, self).__init__()

        # Files path class variables.
        self.icons = maurice_utils.get_icons()

        # Main layout.
        self.main_layout = maurice_qt.QVBoxLayout()
        self.setLayout(self.main_layout)

        # Header class variables.
        self.aov_name_label = None
        self.aov_suffix_line_edit = None

        # Creates the widgets.
        self.create_widgets()
        self.create_layout()

    def create_widgets(self) -> None:
        """Creates the widgets."""
        # ==============================================================================================================
        # Header.
        # ==============================================================================================================
        # AOV type QFont.
        aov_type_font = QtGui.QFont()
        aov_type_font.setBold(True)

        # AOV name QLabel.
        self.aov_name_label = maurice_qt.QLabel()
        self.aov_name_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.aov_name_label.setContentsMargins(0, 0, 0, 0)
        self.aov_name_label.setFixedWidth(125)
        self.aov_name_label.setFont(aov_type_font)

        # AOV suffix QLineEdit.
        self.aov_suffix_line_edit = maurice_qt.QLineEdit()

    def create_layout(self) -> None:
        """Creates the layouts."""
        # ==============================================================================================================
        # Header.
        # ==============================================================================================================
        # Header QGroupBox.
        header_group_box = QtWidgets.QGroupBox()
        header_group_box.setStyleSheet('''
            QGroupBox {
                background-color: rgb(45, 45, 45); 
                border-radius: %dpx;
                padding: %dpx;}''' % (
            maurice_qt.widgets_attributes.border_radius,
            maurice_qt.widgets_attributes.spacing))
        self.main_layout.addWidget(header_group_box)

        # Header QHBoxLayout.
        header_h_box_layout = maurice_qt.QHBoxLayout()
        header_h_box_layout.addWidget(self.aov_name_label)
        header_h_box_layout.addWidget(self.aov_suffix_line_edit)
        header_group_box.setLayout(header_h_box_layout)

    def get_aov_name(self) -> str:
        """Gets the AOV name."""
        return self.aov_name_label.text()

    def get_aov_suffix(self) -> str:
        """Gets the AOV suffix."""
        return self.aov_suffix_line_edit.text()

    def set_aov_name(self, aov_name: str) -> None:
        """Sets the AOV name."""
        self.aov_name_label.setText(aov_name)

    def set_aov_suffix(self, aov_suffix: str) -> None:
        """Sets the AOV suffix."""
        self.aov_suffix_line_edit.setText(aov_suffix)
