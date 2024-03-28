# Run Control Data Structures
This documentation contains information for the data structures of different saved files by the Run Control software and different modules.

## Configuration file
The master configuration file is saved in `.json` format. The data structure is:
- `general`: General configuration for the run control software. This includes paths that the software uses in 
  normal operation. This information generally doesn't change across runs and different days.
  - `config_path`
  - `log_path`
  - `data_dir`
- `run`: Information specific to this run.
  - `source`
  - `pressure_setpoint` (psia)
  - `max_ev_time` (s)
  - `max_num_evs`
- `scint`
  - `amp`
    - `ip_addr`
    - `bias` (V)
    - `qp` (V)
  - `caen`
    - `model`
    - `port`
    - `connection`
    - `evs_per_read`
    - `rec_length`
    - `post_trig`
    - `trig_in`
    - `decimation`
    - `overlap`
    - `polarity`
    - `io_level`
    - `ext_trig`
    - `sw_trig`

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
