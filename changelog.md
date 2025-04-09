# Changelog

## [Unreleased]

## [0.1.0] - 2023-07-12

### Added
- Logging functionality to the STT (Speech-to-Text) module
  - Added logging for initialization, audio processing, and speech recognition
  - Added error handling with appropriate log messages
- Logging functionality to the TTS (Text-to-Speech) module
  - Added logging for initialization, text processing, and file saving
  - Added error handling with appropriate log messages
- Centralized logging configuration in main.py
  - Configured logging to output to both console and file
  - Set up consistent log format with timestamp, module name, and log level
  - Added logging for request handling and processing flow
- Created changelog.md file to track project changes

### Changed
- Enhanced error handling in STT and TTS modules with proper exception logging
- Improved request processing flow in main.py with detailed logging

### Fixed
- No specific fixes in this release