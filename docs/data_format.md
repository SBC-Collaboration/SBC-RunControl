# Run Control Data Format
This documentation contains information for the data structures of different saved files by the Run Control software and different modules.

## Configuration file
The master configuration file is saved in `.json` format. The data structure is:
- `general`: General configuration for the run control software. This includes paths that the software uses in 
  normal operation. This information generally doesn't change across runs and different days.
  - `config_path` (`str`): Path for the master config file.
  - `log_path` (`str`): Path where the log file is saved.
  - `data_dir` (`str`)
  - `max_ev_time` (`int`, s)
  - `max_num_evs` (`int`)
- `scint`
  - `amp`
    - `ip_addr` (`str`)
    - `bias` (`float`, V)
    - `qp` (`float`, V)
  - `caen`
    - `model` (`str`)
    - `port` (`int`)
    - `connection` (`str`)
    - `evs_per_read` (`int`)
    - `rec_length` (`int`)
    - `post_trig` (`int`)
    - `trig_in` (`bool`)
    - `decimation` (`int`)
    - `overlap` (`bool`)
    - `polarity` (`str`)
    - `io_level` (`str`)
    - `ext_trig` (`str`)
    - `sw_trig` (`str`)
  - `caen_g0`, `caen_g1`, `caen_g2`, `caen_g3`
    - `enabled` (`bool`)
    - `thresdhold` (`int`)
    - `trig_mask` (`bool`, 8)
    - `acq_mask` (`bool`, 8)
    - `offsets` (`int`, 8)
- `acous`
  - `general`
    - `sample_rate` (`str`)
    - `pre_trig_len` (`int`)
    - `post_trig_len` (`int`)
    - `trig_timeout` (`int`)
    - `trig_delay` (`int`)
  - `per_channel`
    - `ch1`, `ch2`, `ch3`, `ch4`, `ch5`, `ch6`, `ch7`, `ch8`
      - `enabled` (`bool`)
      - `range` (`int`)
      - `offset` (`int`)
      - `trig` (`bool`)
      - `polarity` (`str`)
      - `threshold` (`int`)
- `cam`
  - `cam1`, `cam2`, `cam3`
    - `config_path` (`str`)
    - `data_path` (`str`)
    - `ip_addr` (`str`)
    - `mode` (`int`)
    - `trig_wait` (`float`)
    - `exposure` (`int`)
    - `buffer_len` (`int`)
    - `post_trig` (`int`)
    - `adc_threshold` (`int`)
    - `pix_threshold` (`int`)
    - `image_format` (`str`)
    - `date_format` (`str`)
    - `state_comm_pin` (`int`)
    - `trig_en_pin` (`int`)
    - `trig_latch_pin` (`int`)
    - `state_pin` (`int`)
    - `trig_pin` (`int`)
- `dio`
  - `arduinos`
    - `trigger`
      - `port` (`str`)
      - `sketch` (`str`)
    - `clock`
      - `port` (`str`)
      - `sketch` (`str`)
    - `position`
      - `port` (`str`)
      - `sketch` (`str`)

## Run data
The run data is saved in the run-data tables in the slow control SQL database. There is one line per run.


## Event data
This data is saved in the SBC binary format using `SBCBinaryFormat` library. The data structure is:
- `ev_number` (`uint32`, 3): A list of date, run number, and event number of current event. For example, for Run 
  20240101_0 Event 0, this list would be `[20240101, 0, 0]`.
- `ev_livetime` (`uint64`): Event livetime in milliseconds. This is the time from when all modules are ready to 
  when a trigger is received by the run control.
- `run_livetime` (`uint64`): Run livetime in milliseconds. This is the sum of the current and all previous events.
- `trigger_source` (`uint8`): Trigger source encoded in number. The list is:
  - `0`: Camera 1 motion detection;
  - `1`: Camera 2 motion detection;
  - `2`: Camera 3 motion detection;
  - `3`: Run control software trigger;
  - `4`: Run control timeout trigger;
  - `5`: PLC trigger, see PLC data for detail;
  - `6`: Kulite Ar trigger, high resolution trigger directly from Kulite (doesn't exist yet);
  - `7`: Kulite CF4 trigger, high resolution trigger directly from Kulite (does't exist yet);
  - `8`: External button manual trigger (doesn't exist yet);
  - `9`: Unknown.
