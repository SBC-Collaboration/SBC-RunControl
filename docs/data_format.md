# Data Formats
This documentation contains information for the data structures of different saved files by the Run Control software and different modules.

## Main configuration
The master configuration file is saved in `.json` format. It contains configuration for run control itself and also all modules, including SiPM amps, CAEN, GaGe, cameras, arduinos, NI USB, and SQL. When run control starts, it will read the file from the main run control folder, and populate the fields in the settings window. After editing in the setting window, applying will update the config dictionary, and saving will update the dictionary and update the local file. Loading from a file will overwrite only the fields available in the file. 
At the start of a run, a copy of the config dictionay to the run_config dictionary, which will be used as the reference config for all modules during the entire run. If some changes are made in the settings window during a run, it will only change the config dictionary, and not the run_config dictionary. A json copy of the run config is saved to the run data folder. 
The data structure is:
- **general**: General configuration for the run control software. This includes paths that the software uses in 
  normal operation. This information generally doesn't change across runs and different days.
  - **config_path** (`str`): Path to the master config json file.
  - **log_path** (`str`): Path to the log file.
  - **data_dir** (`str`): Main directory where all of the data is saved.
  - **max_ev_time** (`int`, s): Max time an event can last. After the maximum is reached, a software trigger is sent from run control.
  - **max_num_evs** (`int`): Max number of events that a run can have. If the max number is reached, then the run will end, instead of starting a new event.
  - **sql**: SQL configurations
    - **hostname** (`str`): Host name of SQL server
    - **port** (`int`): Port used by SQL server
    - **user** (`str`): User name for SQL connection
    - **token** (`str`): Environment variable of the password used for SQL connection
    - **database** (`str`): Name of database to which the data is saved
    - **run_table** (`str`): Name of the table in the database that the information for the run is saved to
    - **event_table** (`str`): Name of the table in the database that the event data is saved to.
  - **pressure**: Pressure profiles for the run.
    - **mode**: The selection mode of pressure profiles for events in a run. If `random`, then a profile is chosen randomly among enabled ones. If `cycle`, then it will cycle through all enabled ones in order.
    - **profile1**, **profile2**, **profile3**, **profile4**, **profile5**, **profile6**: Six slots for pressure profiles to choose from.
      - **enabled** (`bool`): Whether this profile is enabled to be used in the run.
      - **setpoint** (`float`, bara): Pressure set point if it only uses one, and lower pressure set point if it oscillates between two values.
      - **setpoint_high** (`float`, bara): Higher pressure set point if it oscillates between two values. If only one setpoint is needed, just set this value to number smaller than `setpoint`, preferably 0.
      - **slope** (`float`, bar/s): The speed of expansion at the start of the event.
      - **period** (`float`, s): The period of oscillation between the low and high pressure set points.
- **scint**: Scintillation related settings, including SiPM amplifiers and CAEN digitizer.
  - **amp1**, **amp2**, **amp3**
    - **enabled** (`bool`): Whether this amplifier is enabled.
    - **ip_addr** (`str`): Local IP address of this amplifier's nanopi.
    - **bias** (`float`, V): Reverse bias voltage for SiPMs. This is the `HVout` variable in the documentation. Positive number means reverse bias. 
    - **qp** (`float`, V): Charge pump voltage, defaults to 70V. This sets the upper limit of `HVout`.
    - **iv_enabled** (`bool`): Whether to perform IV curve measurements automatically.
    - **iv_data_dir** (`str`): Directory on the nanopi to save the IV measurement results.
    - **iv_rc_dir** (`str`): Directory on the run control where data is saved.
    - **iv_interval** (`float`, hours): If an IV curve measurement within this interval already exists at the satart or end of a run, no IV curve measurement will be performed.
    - **iv_start** (`float`, V): Start (lower) voltage of measurement.
    - **iv_stop** (`float`, V): End (higher) voltage of measurement.
    - **iv_step** (`float`, V): Voltage step of measurement.
    - **ch_offset** (`float`, V): Voltage offset for each channel.
  - **caen**: General config for CAEN digitizer.
    - **enabled** (`bool`): Whether this module in run control is enabled. If disabled, nothing will be done.
    - **data_path** (`str`): Path on the DAQ PC that the data of the current event should be saved to. This can be a symbolic link.
    - **model** (`str`): Model of digitizer (DT5740 for Fermilab chamber).
    - **link** (`int`): COM port of digitizer. If this is the first CAEN digitizer, it will be 0. If not, increment from there.
    - **connection** (`str`): Connection type: USB or PCIe.
    - **evs_per_read** (`int`): Maximum number of events per read from digitizer to PC memory. If number of events on digitizer is fewer, than all events will be transferred.
    - **rec_length** (`int`): Record length for each buffer, or number of samples in a waveform. The actual record length may be the closest multiple of 3.
    - **post_trig** (`int`): Percentage of samples after the trigger. 0% means trigger is at the end of waveform.
    - **trig_in_as_gate** (`bool`): If `true`, the TRIG-IN port on the digitizer will serve as gate for triggering in all other channels. This means that only if the TRIG-IN is true will the data channel triggering be enabled. If `false`, the TRIG-IN will serve as an additional channel of trigger, which may be useful when doing LED calibration.
    - **decimation** (`int`): Decimation factor for acquisition. This can be n=\[0..7\], and the sampling frequency is f = 62.5 MHz/s / (2 ^ n).
    - **overlap_en** (`bool`): Whether overlapping triggers are enabled. Overlapping triggers are triggers that appear inside the acquisition window of another trigger.
    - **polarity** (`str`): Trigger polarity. Rising of falling edge.
    - **majority_level** (`int`): How many groups need to generate concurrent triggers for a global trigger to be generated. A `majority_level` of 0 means any channel from 1 group or more will be accepted. 
    - **majority_window** (`int`, 8 ns): The concurrent triggers need to be with in this many clock cycles of each other to count. The internal clock frequency is 125 MHz, so each cycle is 8 ns.
    - **clock_source** (`str`): Where the reference clock comes from. Could be "Internal" or "External". Internal clock is at 125 MHz.
    - **acq_mode** (`str`): How the acquisition can be enabled or disabled. Can be "SW CTRL", "TRG-IN CTRL", or "GPI CTRL". 
    - **io_level** (`str`): Selects IO level for TRIG-IN, GPO, and GPI ports. Can be NIM or TTL.
    - **ext_trig** (`str`): Mode of external trigger if `trig_in_as_gate` not enabled. Can be `disabled`, `extout only`, `acq only` or `extout+acq`. This sets if the external trigger is used to generate acquisition trigger, or trigger output, or both, or neither.
    - **sw_trig** (`str`): Mode of software trigger, with the same set of options as previous.
    - **ch_trig** (`str`): Mode of channel self trigger, with the same set of options as previous.
  - **caen_g0**, **caen_g1**, **caen_g2**, **caen_g3**: Per-group config for CAEN digitizer.
    - **enabled** (`bool`): Whether this entire group is enabled.
    - **offset** (`int`): 16-bit offset value for entire group for 2Vpp \[0..65535\].
    - **range** (`str`): Voltage range of this group. DT5740 can only be "2 Vpp".
    - **thresdhold** (`int`): Triggering threshold for this group. 12 bit value corresponding to 2Vpp \[0..4095\].
    - **trig_mask** (`bool`, 8): Specifies if each individual channel participates in triggering.
    - **acq_mask** (`bool`, 8): Specifies if data from individual channel is saved.
    - **ch-offset** (`int`, 8): 8-bit per-channel offset on top of group offset. \[0..255\] added to the 16-bit offset.
- **acous**
  - **enabled** (`bool`): Whether this module is enabled. If not, everything will be skipped.
  - **data_dir** (`str`): Director on the DAQ PC that the acoustics data for this event should be saved to.
  - **driver_path** (`str`)
  - **mode** (`str`)
  - **sample_rate** (`str`)
  - **pre_trig_len** (`int`)
  - **post_trig_len** (`int`)
  - **trig_timeout** (`int`)
  - **trig_delay** (`int`)
  - **ch1**, **ch2**, **ch3**, **ch4**, **ch5**, **ch6**, **ch7**, **ch8**
    - **enabled** (`bool`)
    - **range** (`int`)
    - **offset** (`int`)
    - **impedance** (`str`)
    - **coupling** (`str`)
    - **trig** (`bool`)
    - **polarity** (`str`)
    - **threshold** (`int`)
  - **ext**
    - **range** (`int`)
    - **trig** (`bool`)
    - **polarity** (`str`)
    - **threshold** (`int`)
- **cam**
  - **cam1**, **cam2**, **cam3**
    - **enabled** (`bool`): Whether this camera is enabled. If not, this camera will be skipped.
    - **rc_config_path**: Path of config file in the run control system.
    - **config_path** (`str`): Path of the config file in camera's raspberry pi system.
    - **data_path** (`str`): Data Path for the current event on the camera pi (mounted directory). For the main config file, this will be the mounted directory of the master data file. For the config file saved on camera for each event, it will be that path joined with run and event id.
    - **ip_addr** (`str`): IP address of camera raspberry pi. This should be in the local subnet.
    - **mode** (`int`): Mode of the camera, which determines the resolution, pixel format, and trigger mode. Useful 
      modes for this camera is mode 5 (1280x800, self trigger) and mode 11 (1280x800, external trigger)
    - **trig_wait** (`float`, s): Time after event start before the `trig_en` signal is sent by the run control. This 
      variable is used only by run control and not the RPi.
    - **exposure** (`int`): The exposure time of camera module. This number is in units of 7.7us.
    - **buffer_len** (`int`): Number of images to keep in the ring buffer.
    - **post_trig** (`int`): Number of images to take after a trigger is received.
    - **adc_threshold** (`int`): The threshold of adc value change between two consecutive images before the pixel is 
      counted as different. The image is taken in 8bit.
    - **pix_threshold** (`int`): The threshold of number of pixels that need to be different between two consecutive 
      images before the trigger condition is satisfied.
    - **image_format** (`str`): The format in which the image is saved. For example it can be "bmp", "png", or "jpg".
    - **date_format** (`str`)
    - **state_comm_pin** (`int`): The pin number on the raspberry pi for the state_comm pin. This is the BCM pin 
      number (GPIOx) and not the physical pin number.
    - **trig_en_pin** (`int`): The pin at which the trigger enable signal is received.
    - **trig_latch_pin** (`int`): The pin at which the trigger latch signal from the trigger arduino is received.
    - **state_pin** (`int`): The output pin for state communication back to run control.
    - **trig_pin** (`int`): The output pin when the trigger condition is satisfied to trigger arduino.
- **dio**: All settings related to the digital input/output box.
  - **trigger**: Trigger fan-in/fan-out arduino.
    - **port** (`str`): Serial port that this arduino is connected to. A custom informational name should be assigned based on the port on the USB hub.
    - **sketch** (`str`): Location of the sketch folder for this arduino.
    - **loop** (`int`, us): How long each loop of the code should take. If arduino cannot complete the tasks within that time, it will print warning to serial and lower the `on_time` pin. 
    - **reset** (`int`): Reset pin. Resets all trigger latch pins back to low.
    - **or** (`int`): Logic OR (non-latching) pin.
    - **on_time** (`int`): On-time pin showing whether all operations completed within designated clock cycle (100 us).
    - **heartbeat** (`int`): Heartbeat pin, oscillates between high and low each clock cycle.
    - **trig1**, **trig2**, **trig3**, **trig4**, **trig5**, **trig6**, **trig7**, **trig8**, **trig9**, **trig10**, **trig11**, **trig12**, **trig13**, **trig14**, **trig15**, **trig16**
      - **enabled** (`bool`): Whether this channel is enabled. If not, trigger in to this channel will not be counted in the global latching.
      - **name** (`str`): Name for this pin for information.
      - **compressions** (`str`): Whether this trigger causes fast or slow compression in the PLC.
      - **in** (`int`): Trigger in pin.
      - **first_fault** (`int`): First fault pin.
  - **clock**: Clock arduino for syncing LED, camera, and CAEN.
    - **port** (`str`): Serial port for this device.
    - **sketch** (`str`): Location of sketch folder.
    - **loop** (`int`, us): How long each loop of the code should take. If arduino cannot complete the tasks within that time, it will print warning to serial and lower the `on_time` pin. 
    - **wave1**, **wave2**, **wave3**, **wave4**, **wave5**, **wave6**, **wave7**, **wave8**, **wave9**, **wave10**, **wave11**, **wave12**, **wave13**, **wave14**, **wave15**, **wave16**
      - **enabled** (`bool`): If not enabled, this channel will always be low.
      - **name** (`str`): Name of channel for information.
      - **gated** (`bool`): Whether this channel is controlled by the trigger gate signal from trigger arduino. If true, this channel will only be active when the gate pin is high from trigger arduino.
      - **period** (`int`): Period of this wave, in units of `loop`.
      - **phase** (`int`): Phase of the wave in units of `loop`.
      - **duty** (`int`): Duty cycle of the wave, in units of percent.
      - **polarity** (`bool`): If positive, then the wave will first be high and be low. Vice versa for polarity.
  - **position**: Position arduino for measuring the location of the bellow.
    - **port** (`str`): Serial port for this device.
    - **sketch** (`str`): Location of sketch folder.
    - **mac_addr** (`str`): MAC address for Modbus setting. This can be any value, as long as it's unique in the subnet. Using the value printed on the Ethernet shield.
    - **ip_addr** (`str`): Local static IP address in the subnet.
    - **gateway** (`str`)
    - **subnet** (`str`)

## Run Data
The run data is saved in the `RunData` tables in the slow control SQL database. There is one line per run.
- **ID** (`BIGINT UNSIGNED`, `NOT NULL`, `PRIMARY KEY`, `AUTO-INCREMENT`): Auto-generated unique integer ID.
- **run_ID** (`VARCHAR(100)`, `NOT NULL`, `UNIQUE KEY`): Run ID generated by run control software, like "20240101_0".
- **num_events** (`INT UNSIGNED`, `NOT NULL`): Number of events in the run.
- **run_livetime** (`TIME(3)`, `NOT NULL`): Total livetime of the run, with ms precision.
- **comment** (`TEXT`): Any comments entered by the user during the run.
- **active_datastreams** (`SET('imaging', 'scintillation', 'acoustics')`, `NOT NULL`): A list of active data streams 
  for the run. It can have zero, one, or multiple entries, from the predetermined list. If it has zero elements, it is saved as an empty string, and not NULL.
- **pset_mode** (`ENUM('random', 'sequential')`, `NOT NULL`): Mode of pressure setpoint in this run. If `random`, then run control will choose randomly from the list. If `sequential`, then run control will cycle through the pressure setpoints in the list in order.
- **pset** (`FLOAT`, `NOT NULL`): Pressure set point of the run. If the run is doing pressure ramping, then the higher setpoint of the ramp
- **start_time** (`TIMESTAMP(3)`, `NOT NULL`): UTC timestamp of when the run starts, with ms precision
- **end_time** (`TIMESTAMP(3)`, `NOT NULL`): UTC timestamp of when the run ends, with ms precision
- **source1_ID** (`VARCHAR(100)`): Name of source 1
- **source1_location** (`VARCHAR(100)`): Location of source 1
- **source2_ID** (`VARCHAR(100)`): Name of source 2
- **source2_location** (`VARCHAR(100)`): Location of source 2
- **source3_ID** (`VARCHAR(100)`): Name of source 3
- **source3_location** (`VARCHAR(100)`): Location of source 3
- **config** (`JSON`): Saves the master config file in addition to the data folder. Should enable some SQL query using config info.
- More columns will be added when analysis module is running, like the last data reduction version performed and the date, etc.

## Event Data
The event data is saved in the `EventData` tables in the slow control SQL database. There is one line per event.
- **ID** (`INT UNSIGNED`, `NOT NULL`, `PRIMARY KEY`, `AUTO-INCREMENT`): Auto-generated unique integer ID.
- **run_ID** (`VARCHAR(100)`, `NOT NULL`, `MULTIPLE KEY (1)`): Run ID generated by run control software, like "20240101_0". Run_ID and event_ID combined is a unique key for the event.
- **event_ID** (`INT UNSIGNED`, `NOT NULL`, `MULTIPLE KEY (2)`): Integer event ID starting from 0 in the run. 
- **event_livetime** (`TIME(3)`, `NOT NULL`): Run control livetime for this event.
- **cum_livetime** (`TIME(3)`, `NOT NULL`): Cumulative livetime of the run at the end of the event.
- **pset** (`FLOAT`, `NOT NULL`): Pressure set point for this event, in units of bara. If `pset_hi` exists, then this is the lower of the two set points.
- **pset_hi** (`FLOAT`): Higher pressure set point, in units of bara. If this number is lower than `pset` or is `NULL`, then there is only one set point.
- **pset_slope** (`FLOAT`, `NOT NULL`): Slope of expansion from compressed state to the higher pressure set point, in units of bar/s.
- **pset_period** (`FLOAT`): Period of oscillation between higher and lower set points. In units of seconds.
- **start_time** (`TIMESTAMP(3)`): Timestamp of the event start.
- **stop_time** (`TIMESTAMP(3)`): Timestamp of the event stop.
- **trigger_source** (`VARCHAR(100)`, `NOT NULL`): Name of trigger's first fault.

## Event info
This data is saved in the SBC binary format using `SBCBinaryFormat` library. The data structure is:
- **ev_number** (`uint32`, 3): A list of date, run number, and event number of current event. For example, for Run 
  20240101_0 Event 0, this list would be `[20240101, 0, 0]`.
- **ev_livetime** (`uint64`): Event livetime in milliseconds. This is the time from when all modules are ready to 
  when a trigger is received by the run control.
- **run_livetime** (`uint64`): Run livetime in milliseconds. This is the sum of the current and all previous events.
- **pset** (`float`): Pressure setpoint for this event. In case of pressure ramping or random sampling, the pressure setpoint could be different for each event. 
- **trigger_source** (`str`): Trigger first fault source. This trigger is the one that causes the global trigger latch.
