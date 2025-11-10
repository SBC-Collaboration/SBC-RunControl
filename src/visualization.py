import pyqtgraph as pg
from PySide6.QtCore import QObject
from sbcbinaryformat import Streamer
import os
import logging

class CAENPlotManager(QObject):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.container = main.ui.caen_plot_container
        self.main_config = main.config_class.run_config
        self.plots = []
        self.curves = []
        self.event_label = None
        # one pen for each channel in a group
        self.pen_colors = ["green", "red", "blue", "orange", "violet", "brown", "pink", "gray"]
        self.pens = [pg.mkPen(color=c, width=2) for c in self.pen_colors]

        self.logger = logging.getLogger("rc")
        
    def setup_plot(self):
        """
        Set up the CAEN plot widgets. It will create the plot and text items for each plot, and set up basic properties.
        """
        # plot and text items for each plot
        self.container.ci.layout.setSpacing(0)
        self.container.clear()
        self.container.setBackground("w")
        y_label = self.container.addLabel("Amplitude (ADC)", 
                    color='k', row=0, col=0, angle=-90, rowspan=4, anchor=(0,0.5))
        self.event_label = pg.TextItem(text="Event: 0", color='k', anchor=(0, 0))
        self.event_label.setParentItem(y_label)
        self.event_label.setPos(0, 1)
        self.container.ci.layout.setColumnFixedWidth(0, 8)
        self.container.ci.layout.setColumnStretchFactor(1, 4)
        self.container.ci.layout.setColumnFixedWidth(2, 10)
        self.container.ci.layout.setColumnFixedWidth(3, 10)
        
        for i in range(4):
            p = self.container.addPlot(row=i, col=1)
            self.plots.append(p)
            p.showGrid(x=True, y=True)
            p.getViewBox().setBackgroundColor("w")
            p.enableAutoRange('xy', True)
            border_pen = pg.mkPen(color='black', width=2)
            p.getViewBox().border = border_pen
            legend = p.addLegend()
            legend.scene().removeItem(legend)
            legend_layout = self.container.addLayout(row=(i//2)*2, col=2+(i%2), rowspan=2)
            legend_layout.layout.setSpacing(0)
            legend_layout.addItem(legend, 0, 0)

            # Do different things for each subplot
            if i == 0:
                p.setTitle(f"CAEN Waveforms", color='k')
                axis = p.getAxis('bottom')
                axis.setStyle(tickLength=0, showValues=False)
            elif i in [1, 2]:
                p.setXLink(self.plots[0])
                axis = p.getAxis('bottom')
                axis.setStyle(tickLength=0, showValues=False)
            elif i == 3:
                p.setXLink(self.plots[0])
                p.setLabel('bottom', "Time (us)", color='k')
            else:
                raise ValueError("Invalid CAEN plot index")

            # create curves for each channel
            curves = []
            for j in range(8):
                c = p.plot(x=[], y=[], pen=self.pens[j], name=f"Ch{i*8+j}")
                curves.append(c)
            self.curves.append(curves)


    def update_plot(self, data):
        """
        Update the CAEN plot widgets every time data is retrieved
        """
        self.event_label.setText(f"Event: {data['EventCounter'][-1]:,}")
        self.main_config = self.main.config_class.run_config
        configs = self.main_config["caen"]

        for i in range(len(self.plots)):
            curves = self.curves[i]
            # frequency is 62.5MHz
            tick = 0.016 * configs["global"]["decimation"]  # us
            time_axis = [i*tick for i in range(data["Waveforms"].shape[2])]
            for j in range(8):
                if not configs[f"group{i}"]["enabled"] or \
                    not configs[f"group{i}"]["acq_mask"][j] or \
                    not configs[f"group{i}"]["plot_mask"][j]:
                    curves[j].setData(x=[], y=[])
                else:
                    ind = self._get_ch_index(data["AcquisitionMask"], 8*i+j)
                    wfs = data['Waveforms'][-1][ind]
                    curves[j].setData(x=time_axis, y=wfs)
        

    @staticmethod
    def _get_ch_index(mask, ch):
        """
        Get the index of the channel in list using mask
        Count number of 1s in all bits lower than the desired bit
        """
        lower_mask = (1 << ch) - 1
        return bin(mask & lower_mask).count("1")


class AcousPlotManager(QObject):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.plot = self.main.ui.acous_plot
        self.main_config = self.main.config_class.run_config
        self.curves = []
        self.text = None
        self.pens = []
        self.logger = logging.getLogger("rc")

    def setup_plot(self):
        """
        Set up the Acous plot widgets. It will create the plot and text items for each plot, and set up basic properties.
        """
        self.text = pg.TextItem("", anchor=(0, 1), color='k')
        self.pens = [pg.mkPen(color=c, width=2) for c in ["green", "red", "blue", "orange","violet","brown","pink","gray"]] 

        # setup some basic plot properties
        self.plot.setBackground("w")
        self.plot.showGrid(x=True, y=True)
        self.plot.setTitle(f"Acous Waveforms", color='k')
        self.plot.setLabel('left', "Amplitude (ADC)", color='k')
        self.plot.setLabel('bottom', "Time (us)", color='k')
        self.plot.addLegend()

        # setup text counter
        self.text.setParentItem(self.plot.getViewBox())
        self.text.setPos(0, 1)

        # create curves for each channel
        for i in range(8):
            c = self.plot.plot(x=[], y=[], pen=self.pens[i], name=f"Ch{i+1}")
            self.curves.append(c)

    def update_plot(self):
        """
        Update the acous plot widgets every time data is retrieved
        """
        acous_configs = self.main_config["acous"]
        if not acous_configs["enabled"]:
            return
        
        try:
            data = Streamer(os.path.join(self.main.current_path, "acoustics.sbc")).to_dict()
        except FileNotFoundError:
            self.logger.warning("AcousPlotter: Acoustics data file not found.")
            return
        sample_rate = self.main.acous_worker.sample_rate_conversion[acous_configs["sample_rate"]]/1e6
        time_axis = [i/sample_rate for i in range(data["Waveforms"].shape[2])]
        for i in range(8):
            if not acous_configs[f"ch{i+1}"]["plot"]:
                self.curves[i].setData(x=[], y=[])
            else:
                self.curves[i].setData(x=time_axis, y=data['Waveforms'][-1][i])