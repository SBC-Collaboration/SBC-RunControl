# Changelog

## [latest]
### Added
- Add PLC / modbus module. This enables communication between run control and PLC. It can start and stop pressure cycle, set pressure setpoint, start and stop PLC taking high resolution data.
- Create a run_info.sbc that matches the RunData SQL table for each run, and populate the event_info.sbc to match the EventData SQL table.
- Add run exit code and event exit code in SQL tables. Specific definitions to come later.
- Add changelog.
- Add lock file so that only one instance of run control runs at a time.
- Create a symlink for current run folder in data directory, in addition to the current event folder.
- Main log file is renamed rc.log, and is rotated daily.
### Changed
- Simplify enable boxes in settings window general tab.
### Fixed
- Define fast compress pin as output pin in trigger Arduino code.
- Switch the trigger and trigger latch pins in NIUSB config, because the pin may be malfunctioning as output.

## [[v0.0.2]](https://github.com/SBC-Collaboration/SBC-RunControl/releases/tag/v0.0.2) - 2025-05-21
### Added
- Saving version number of red_caen, niusb_6501, and sbc_binary_format.
- Remove dependencies from dependencies folder. Install instead using pip from github.
- Added CAEN / GaGe driver install scripts to `init.sh`. Created new `root_init.sh` to handle the parts that needs root privileges. The script also prompts for SQL token and saves to a file with proper permission.
- Add event pressure display in main window.
### Changed
- Use `git submodule` to handle dependencies that cannot be installed using pip, instead of `git subtree`.
- Change the structure of config file. Specifically where PLC and pressure configs are organized.
### Fixed
- Update documentation and bug fixes.

## [[v0.0.1]](https://github.com/SBC-Collaboration/SBC-RunControl/releases/tag/v0.0.1) - 2025-04-25
First versioned release of run control.
