# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-11-04

### Fixed
- Removed non-existent `types-httpx` dependency that caused installation failures
- Updated `httpx` to version 0.28.1 (includes built-in type hints)

### Changed
- Bumped minimum `httpx` version from 0.24.0 to 0.28.1

## [1.0.0] - 2025-11-04

### Added
- Initial release of ZeroTrue Python SDK
- Support for text and URL checks
- File upload support (from path, buffer, or bytes)
- Automatic retry logic with exponential backoff
- Rate limit handling
- Idempotency support
- Type hints for all functions
- Comprehensive error handling
- Auto-polling for check results

### Known Issues
- Installation fails due to non-existent `types-httpx` dependency (fixed in 1.1.0)

