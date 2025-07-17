# Changelog

## [Latest]
### Added
- Added the Guardian module responsible for everything related to error handling.
### Fixed
- Fixed the bug that SiPM are not biased at start of event.

## [Run Control v0.3.0](https://github.com/SBC-Collaboration/SBC-RunControl/releases/tag/v0.3.0) (2025-07-15)
### Added
- SiPM Amp module now queries the amplifier for HV and QP voltages and per-channel offsets at the start and end of each event. This data is saved into `sipm_amp.sbc`. 
- Added a button to manually force upload arduino sketch without comparing to archived sketch. 
### Changed
- Moved config file to `~/.config/runcontrol/config.json`. Now in the project folder there doesn't need to be a `config.json`. When loading config into settings window, if a field is non existent, a default value will be used instead of throwing an error. This should make adding fields to the config file easier.
- GaGe driver has now new fields `PreTrigLen` and `PostTrigLen` in seconds that controls how much data to save before and after the bubble trigger in Ch1 of the digitizer.
- Renamed **Depth** and **Segment Size** fields in the GaGe driver config to `depth` and `segment_size`. Now the `pre_trig_len` and `post_trig_len` are used for our workaround triggering after retrieving all the data. Those lengths are in seconds.
- Renamed `Waveform` to `Waveforms` in acoustics data.
### Fixed
- Minor bug fix for PLC LED control voltage code.
- Fix acoustic plotting in run control.
- When first connecting to NIUSB, if resource is busy, try freeing the USB device and try again.

## [Run Control v0.2.2](https://github.com/SBC-Collaboration/SBC-RunControl/releases/tag/v0.2.2) (2025-07-08)
### Added
- Turn off position arduino UTI chips at runs, and turn on at end of runs. (Need to find a better time for that to happen to record pressure cycle).
### Fixed
- Use `git describe --tags` to get the correct run control version, instead of `setuptools_scm.get_version`.
- Fix an off-by-one error in SQL RunData table number of events field.
- Update SiPM amp config at start of run.

## [Run Control v0.2.1](https://github.com/SBC-Collaboration/SBC-RunControl/releases/tag/v0.2.1) (2025-07-06)
### Fixed
- Fix the SiPM amplifier PATH not loaded when using paramiko.

## [Run Control v0.2.0](https://github.com/SBC-Collaboration/SBC-RunControl/releases/tag/v0.2.0) (2025-07-03)
### Added
- Add LED current control via PLC modbus.
- Add a page of documentation on git workflow.
### Changed
- Acoustic data now has all only one row of ndarray per trigger, instead of one row per sample.
- Change the name of acoustic file to use only the provided name, no suffix.
- Change a few file paths to be interpreted relative to main run control directory, and not current working directory.
- Acoustic driver will save 10s of data per trigger, instead of 100ms. (Need to parametrize this at some point).
- Move status lights to the bottom area out of the tabs.
- Consolidate CAEN plots into subplots. Moved legends to the side.
- Moved CAEN and acoustic plotting into their own classes.
### Fixed
- Fix the issue that camera imdaq program not getting killed at the end of run.
- Fix CAEN module seg fault and errors when in external or self trigger mode.
- Added a check so that stop event only runs once per event. (Need to add similar checks for other states).
- Fix sync of CAEN per group plot checkbox and individual channel boxes.

## [Run Control v0.1.0](https://github.com/SBC-Collaboration/SBC-RunControl/releases/tag/v0.1.0) (2025-06-11)
### Added
- Add PLC / modbus module. This enables communication between run control and PLC. It can start and stop pressure cycle, set pressure setpoint, start and stop PLC taking high resolution data.
- Implement autorun. If autorun box is checked and the previous run didn't end by pressing the "STOP RUN" button, a new run will automatically start. 
- Create a run_info.sbc that matches the RunData SQL table for each run, and populate the event_info.sbc to match the EventData SQL table.
- Add run exit code and event exit code in SQL tables. Specific definitions to come later.
- Save run control version number in run info and SQL RunData table.
- Add active modules in SQL and run info file.
- Change init script to create a `~/.config/runcontrol/` and save the SMB and SQL tokens there. 
- Add changelog.
- Add lock file so that only one instance of run control runs at a time.
- Create a symlink for current run folder in data directory, in addition to the current event folder.
### Changed
- Change piezo file format. Now it has "range", "offset", and "waveforms" columns.
- Fix all status lights. The status are idle, working, active, disabled, or error.
- Simplify enable boxes in settings window general tab.
- Main log file is renamed rc.log, and is rotated daily.
### Fixed
- Define fast compress pin as output pin in trigger Arduino code.
- Switch the trigger and trigger latch pins in NIUSB config, because the pin may be malfunctioning as output.
- Improve terminating workers and threads when closing run contorl.

## [Run Control v0.0.2](https://github.com/SBC-Collaboration/SBC-RunControl/releases/tag/v0.0.2) (2025-05-21)
### Added
- Saving version number of red_caen, nius- **rc_ver** (`VARCHAR(100)`): b_6501, and sbc_binary_format.
- Remove dependencies from dependencies folder. Install instead using pip from github.
- Added CAEN / GaGe driver install scripts to `init.sh`. Created new `root_init.sh` to handle the parts that needs root privileges. The script also prompts for SQL token and saves to a file with proper permission.
- Add event pressure display in main window.
### Changed
- Use `git submodule` to handle dependencies that cannot be installed using pip, instead of `git subtree`.
- Change the structure of config file. Specifically where PLC and pressure configs are organized.
### Fixed
- Update documentation and bug fixes.

## [Run Control v0.0.1](https://github.com/SBC-Collaboration/SBC-RunControl/releases/tag/v0.0.1) (2025-04-25)
First versioned release of run control.
