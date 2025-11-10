# Changelog

## [Run Control v0.4.5](https://github.com/SBC-Collaboration/SBC-RunControl/releases/tag/v0.4.5) (2025-11-10)
### Added
- Added error handling for camera thread. 
- Added timeout for acoustic module.
### Changed
- Improved SiPM biasing speed for each event.
- Renamed Modbus module to PLC.
- Updated documentation to reflect changes in data formats.
- Improved logging to be more clear.
### Fixed 
- Stop run button is no longer checked at start of new run.
- CAEN plotting will use decimation for time-axis.
- Bugfix for CAEN decimation.

## [Run Control v0.4.4](https://github.com/SBC-Collaboration/SBC-RunControl/releases/tag/v0.4.4) (2025-11-06)
### Added
- Version number display on main window.
### Changed
- Changed some of digiscope config options.
- SiPM voltage set or readback errors will now cause a warning only and not an error.
### Fixed
- If SiPM Amp command execution fails, it will retry until it succeeds. 

## [Run Control v0.4.3](https://github.com/SBC-Collaboration/SBC-RunControl/releases/tag/v0.4.3) (2025-11-05)
### Added
- Digiscope module.
### Changed
- Added timeout for stop event of acoustic driver.

## [Run Control v0.4.2](https://github.com/SBC-Collaboration/SBC-RunControl/releases/tag/v0.4.2) (2025-11-04)
### Added
- Access to new PLC variables `LED1_OUT_PRE`, `LED1_OUT_POST`, `LED_POST_TIME`, `PCYCLE_PSET_LOW`, `PCYCLE_PSET_HIGH`, `PCYCLE_PSET_RAMP1`, `PCYCLE_PSET_RAMPDOWN`, `PCYCLE_PSET_RAMPUP`. Changes to UI, binary file writer and SQL table to reflect the changes. 
### Changed
- Updates to acoustic driver to simplify data saving steps. 

## [Run Control v0.4.1](https://github.com/SBC-Collaboration/SBC-RunControl/releases/tag/v0.4.1) (2025-10-16)
### Changed
- Improved SiPM amp module error handling when `dactest`, `adctest` or `iv_cmd.py` throws an error. 
- Now when biasing SiPM, it will perform at least the number of iterations and keep performing correction until the readback is within tolerance.

## [Run Control v0.4.0](https://github.com/SBC-Collaboration/SBC-RunControl/releases/tag/v0.4.0) (2025-10-09)
### Added
- Added the guardian module, which can handle error messages from any other modules. It can currently log and send alarms on Slack. In the future, it will handle automatic retries when appropriate. There is a checkbox for enabling/disabling the slack alarms.
- Added a gain setting for arducam.
- Added a Python script to take camera time lapse videos.
- Added a new button to choose whether to turn off position sensor during an event.
- Added a new button to take SiPM IV curves when not in a run.
- Added more sources and source positions in the default list. The source names of existing sources at MINOS now loosely follow Fermilab source ID.
### Changed
- Stop Run button is "checked" and not "disabled" when pressed. The user can uncheck the button to continue the run after the end of the event.
- SiPM unbiasing now happens at the end of run, not events now. Bias is still recorded at the start of every event.

## [Run Control v0.3.3](https://github.com/SBC-Collaboration/SBC-RunControl/releases/tag/v0.3.3) (2025-08-20)
### Changed
- Modbus module will wait for cameras to finish for an event before turning off LED control voltages.
- Update documentation on PLC modbus settings.

## [Run Control v0.3.2](https://github.com/SBC-Collaboration/SBC-RunControl/releases/tag/v0.3.2) (2025-08-20)
### Added
- Conda lockfile of a working environment, in case newer package version breaks things.
- Added more documentation on readthedocs
### Changed
- Check SQL tables in addition to local data folder when picking a new run number.
- Update README and badges.
### Fixed
- Removed unused dependencies.

## [Run Control v0.3.1](https://github.com/SBC-Collaboration/SBC-RunControl/releases/tag/v0.3.1) (2025-07-18)
### Added
- Added the Guardian module responsible for everything related to error handling.
- Added a feedback loop when setting SiPM amp biases so the readback real voltage matches the target voltage.
### Fixed
- Fixed the bug that SiPM are not biased at start of event.
- Updated SiPM Amp class docstrings.

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
