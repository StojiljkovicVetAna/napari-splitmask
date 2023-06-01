from typing import TYPE_CHECKING

from qtpy.QtWidgets import QPushButton, QWidget, QSpinBox, QVBoxLayout, QComboBox, QLabel, QFileDialog

import matplotlib.pyplot as plt
import numpy as np
import skimage.io
from pathlib import Path

import matplotlib

from tifffile.tifffile import imwrite


from splitmask import splitmask

from napari_guitils.gui_structures import TabSet

from napari.layers import Labels, Points, Image

from .baseplot import DataPlotter

from microfilm.dataset import MultipageTIFF, Nparray

from cmap import Colormap


if TYPE_CHECKING:
    import napari


class SplitmaskforNapari(QWidget):
    
    def __init__(self, napari_viewer):
        super().__init__()
        self.viewer = napari_viewer

        self.colormap = Colormap('glasbey:glasbey')
        self.napari_cm = self.colormap.to_napari()
        self.matplotlib_cm = self.colormap.to_matplotlib()

        self.napari_cm = {i: self.matplotlib_cm(i) for i in range(256)}
        self.napari_cm[0]=[0,0,0,0]
        
        
        self.btn_ROI = QPushButton('Add ROI')
        self.btn_ROI_label = QLabel('1. Add a point of interest:')

        self.drop_layers = QComboBox()
        self.drop_layers_label = QLabel('2. Select the point or label layer from which the mask will be generated:')
    
        self.tabs = TabSet(['Radial sector', 'Angular sector', 'Circular sector'])
        self.tabs_label = QLabel('3. Generate a sector of the desired geometry using the tabs:')

        # Radial sector
        self.spin_sector_width = QSpinBox()
        self.spin_sector_width.setRange(1,100)
        self.spin_sector_width.setValue(5)
        self.spin_sector_width_label = QLabel('Sector width')

        self.spin_num_sector = QSpinBox()
        self.spin_num_sector.setRange(1,100)
        self.spin_num_sector.setValue(5)
        self.spin_num_sector_label = QLabel('Number of sectors')

        self.btn_radial = QPushButton("Generate radial sector!")
    
        # Angular sector
        self.spin_angular_width = QSpinBox()
        self.spin_angular_width.setRange(1,360)
        self.spin_angular_width.setValue(45)
        self.spin_angular_width_label = QLabel('Angle width')

        self.spin_max_rad = QSpinBox()
        self.spin_max_rad.setRange(1,100)
        self.spin_max_rad.setValue(20)
        self.spin_max_rad_label = QLabel('Sector radius')
        
        self.btn_angular = QPushButton('Generate angular sector!')

        # Circular sector
        self.spin_circle_width = QSpinBox()
        self.spin_circle_width.setRange(1,360)
        self.spin_circle_width.setValue(45)
        self.spin_circle_width_label = QLabel('Circle angle')

        self.spin_circle_rad = QSpinBox()
        self.spin_circle_rad.setRange(1,100)
        self.spin_circle_rad.setValue(20)
        self.spin_circle_rad_label = QLabel('Circle radius')

        self.spin_ring_width = QSpinBox()
        self.spin_ring_width.setRange(1,100)
        self.spin_ring_width.setValue(10)
        self.spin_ring_width_label = QLabel('Ring width')

        self.btn_circle = QPushButton('Generate circular sector!') 



        self.drop_channel = QComboBox()
        self.drop_channel_label = QLabel('4. Select the channel to analyze:')

        self.drop_sector = QComboBox()
        self.drop_sector_label = QLabel('5. Select the sector mask to apply:')

        self.btn_plot_int = QPushButton('6. Compute plot')
        self.intensity_plot = DataPlotter(self.viewer)

        self.btn_export_plot = QPushButton('7. Save plot data')

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.btn_ROI_label)
        self.layout().addWidget(self.btn_ROI)
        self.layout().addWidget(self.drop_layers_label)
        self.layout().addWidget(self.drop_layers)
        self.layout().addWidget(self.tabs_label)
        self.layout().addWidget(self.tabs)
        self.tabs.add_named_tab('Radial sector', self.spin_sector_width_label)
        self.tabs.add_named_tab('Radial sector', self.spin_sector_width)
        self.tabs.add_named_tab('Radial sector', self.spin_num_sector_label)
        self.tabs.add_named_tab('Radial sector', self.spin_num_sector)
        self.tabs.add_named_tab('Radial sector', self.btn_radial)
        self.tabs.add_named_tab('Angular sector', self.spin_angular_width_label)
        self.tabs.add_named_tab('Angular sector', self.spin_angular_width)
        self.tabs.add_named_tab('Angular sector', self.spin_max_rad_label)
        self.tabs.add_named_tab('Angular sector', self.spin_max_rad)
        self.tabs.add_named_tab('Angular sector', self.btn_angular)
        self.tabs.add_named_tab('Circular sector', self.spin_circle_width_label)
        self.tabs.add_named_tab('Circular sector', self.spin_circle_width)
        self.tabs.add_named_tab('Circular sector', self.spin_circle_rad_label)
        self.tabs.add_named_tab('Circular sector', self.spin_circle_rad)
        self.tabs.add_named_tab('Circular sector', self.spin_ring_width_label)
        self.tabs.add_named_tab('Circular sector', self.spin_ring_width)
        self.tabs.add_named_tab('Circular sector', self.btn_circle)

        self.layout().addWidget(self.drop_channel_label)
        self.layout().addWidget(self.drop_channel)
        self.layout().addWidget(self.drop_sector_label)
        self.layout().addWidget(self.drop_sector)
        self.layout().addWidget(self.btn_plot_int)
        self.layout().addWidget(self.btn_export_plot)

        

        self._add_connections()
        
    def _add_connections(self):

        self.btn_ROI.clicked.connect(self._ROI_click)
        self.viewer.layers.events.inserted.connect(self._update_drop)
        self.viewer.layers.events.removed.connect(self._update_drop)
        self.spin_sector_width.valueChanged.connect(self._on_click_radial)
        self.spin_num_sector.valueChanged.connect(self._on_click_radial)
        self.btn_radial.clicked.connect(self._on_click_radial)
        self.spin_angular_width.valueChanged.connect(self._on_click_angular)
        self.spin_max_rad.valueChanged.connect(self._on_click_angular)
        self.btn_angular.clicked.connect(self._on_click_angular)
        self.spin_circle_width.valueChanged.connect(self._on_click_circular)
        self.spin_circle_rad.valueChanged.connect(self._on_click_circular)
        self.spin_ring_width.valueChanged.connect(self._on_click_circular)
        self.btn_circle.clicked.connect(self._on_click_circular)

        self.btn_plot_int.clicked.connect(self._on_plot)
        self.btn_export_plot.clicked.connect(self._export_plot)
        

    
    def _ROI_click(self):
        
        self.viewer.add_points(size=5, 
                               name='point of interest')
        
        
    def _update_drop(self):

        label_points_layers=[]
        for x in self.viewer.layers:
            if isinstance(x, Labels) and 'mask' not in x.name:
                label_points_layers.append(x.name)
            elif isinstance(x, Points):
                label_points_layers.append(x.name)
                
        channel_layers=[]
        for x in self.viewer.layers:
            if isinstance(x, Image):
                channel_layers.append(x.name)

        label_layers=[]
        for x in self.viewer.layers:
            if isinstance(x, Labels) and 'mask' in x.name:
                label_layers.append(x.name)

        self.drop_layers.clear()
        self.drop_layers.addItems(label_points_layers)
        self.drop_channel.clear()
        self.drop_channel.addItems(channel_layers)
        self.drop_sector.clear()
        self.drop_sector.addItems(label_layers)

    def _on_click_radial(self):

        data = self.viewer.layers[0].data

        if isinstance(self.viewer.layers[self.drop_layers.currentText()], Labels):
            roi = self.viewer.layers[self.drop_layers.currentText()].data
            cm = splitmask.get_roi_cm(roi_im=roi)
        elif isinstance(self.viewer.layers[self.drop_layers.currentText()], Points):
            cm = self.viewer.layers[self.drop_layers.currentText()].data
        else:
            raise('Not the correct layer')


        self.radius_labels = splitmask.create_concentric_mask(center=cm, im_dims=data.shape[-2::],    
                                                 sector_width=self.spin_sector_width.value(), 
                                                 num_sectors=self.spin_num_sector.value())
        if "radial_mask" in self.viewer.layers:
            self.viewer.layers["radial_mask"].data=self.radius_labels[0]
        else: 
            self.viewer.add_labels(self.radius_labels[0], name="radial_mask", num_colors=256, color=self.napari_cm)
        self.viewer.layers["radial_mask"].refresh()


    def _on_click_angular(self):

        data = self.viewer.layers[0].data

        if isinstance(self.viewer.layers[self.drop_layers.currentText()], Labels):
            roi = self.viewer.layers[self.drop_layers.currentText()].data
            cm = splitmask.get_roi_cm(roi_im=roi)
        elif isinstance(self.viewer.layers[self.drop_layers.currentText()], Points):
            cm = self.viewer.layers[self.drop_layers.currentText()].data
        else:
            raise('Not the correct layer')
       
        self.sector_labels = splitmask.create_sector_mask(center=cm, im_dims=data.shape[-2::],
                                                     angular_width=self.spin_angular_width.value(),
                                                     max_rad=self.spin_max_rad.value())
        if "angular_mask" in self.viewer.layers:
            self.viewer.layers['angular_mask'].data=self.sector_labels[0]
        else:
            self.viewer.add_labels(self.sector_labels[0], name='angular_mask', num_colors=256, color=self.napari_cm)
        self.viewer.layers['angular_mask'].refresh()

    
    def _on_click_circular(self):

        data = self.viewer.layers[0].data

        if isinstance(self.viewer.layers[self.drop_layers.currentText()], Labels):
            roi = self.viewer.layers[self.drop_layers.currentText()].data
            cm = splitmask.get_roi_cm(roi_im=roi)
        elif isinstance(self.viewer.layers[self.drop_layers.currentText()], Points):
            cm = self.viewer.layers[self.drop_layers.currentText()].data
        else:
            raise('Not the correct layer')
        
        self.circular_labels = splitmask.create_sector_mask(center=cm, im_dims=data.shape[-2::],
                                                     angular_width=self.spin_circle_width.value(),
                                                     max_rad=self.spin_circle_rad.value(),
                                                     ring_width=self.spin_ring_width.value())
        
        if "circular_mask" in self.viewer.layers:
            self.viewer.layers['circular_mask'].data=self.circular_labels[0]
        else:
            self.viewer.add_labels(self.circular_labels[0], name='circular_mask', num_colors=256, color=self.napari_cm)
        self.viewer.layers['circular_mask'].refresh()



    def _on_plot(self):

        C_data = self.viewer.layers[self.drop_channel.currentText()].data
        sector_mask = self.viewer.layers[self.drop_sector.currentText()].data[np.newaxis, :]   
    
        npdata = Nparray(C_data[np.newaxis,:])

        channels = npdata.channel_name
        
        self.signal_radius = splitmask.measure_intensities(
                     npdata, channels=channels, 
                     im_labels = sector_mask)
        
        data = self.signal_radius.sel(channel=0, roi=0)

        self.intensity_plot.axes.clear()

        for i in range(data.shape[1]):
            self.intensity_plot.axes.plot(data[:,i], color=self.matplotlib_cm(i+1))
                                
        self.intensity_plot.canvas.figure.canvas.draw()

        self.intensity_plot.show()

    def _export_plot(self):

        sector_mask = self.viewer.layers[self.drop_sector.currentText()].data

        self.export_folder = Path(str(QFileDialog.getExistingDirectory(self, "Select Directory")))

        self.signal_radius.name = 'intensity'
        df = self.signal_radius.to_dataframe().reset_index()
        df.to_csv(self.export_folder.joinpath('export_plot_data.csv'), index=False)

        self.intensity_plot.axes.savefig(self.export_folder.joinpath('export_plot.png'))
        self.viewer.screenshot(self.export_folder.joinpath('export_screenshot.png'))

        imwrite(self.export_folder.joinpath('export_'+self.drop_sector.currentText()+'.tiff'), sector_mask)   