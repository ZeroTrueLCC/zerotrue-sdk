# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2025-11-04

### Changed
- Updated API endpoints to match current ZeroTrue API:
  - Text analysis: `/api/v1/analyze/text` (uses form-data)
  - URL analysis: `/api/v1/analyze/url` (uses form-data)
  - File analysis: `/api/v1/analyze/file` (was `/api/v1/checks/upload`)
  - Result retrieval: `/api/v1/result/{id}` (was `/api/v1/checks/{id}`)
- Improved HTTP client header handling:
  - Content-Type header is now set automatically only for JSON requests
  - Form-data and file uploads use automatic Content-Type detection
- Enhanced API response adaptation:
  - Automatically unwraps nested response data from `data` field
  - Converts probability values from 0-1 range to percentages (0-100)
- Updated examples to support `.env` file loading via `python-dotenv` (optional)

### Fixed
- Proper handling of API key in request body for text/URL/file checks
- Correct API key parameter passing in GET requests for result retrieval

## [1.1.1] - 2025-11-04

### Fixed
- Removed non-existent `types-httpx` dependency that caused installation failures
- Updated `httpx` to version 0.28.1 (includes built-in type hints)

### Changed
- Bumped minimum `httpx` version from 0.24.0 to 0.28.1

## [1.1.0] - 2025-11-04

### Known Issues
- Installation fails due to non-existent `types-httpx` dependency (fixed in 1.1.1)

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
- Installation fails due to non-existent `types-httpx` dependency (fixed in 1.1.1)

