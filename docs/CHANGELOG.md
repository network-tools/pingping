# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.5] - 2026-01-16

### Added
- Modern Python tooling support (uv, ruff, black)
- `pyproject.toml` for project configuration
- TestIQ integration for test quality analysis
- `.python-version` file for uv compatibility
- Comprehensive contributing guidelines in `docs/CONTRIBUTING.md`
- This changelog

### Changed
- **BREAKING**: Dropped Python 2.7 support
- Minimum Python version is now 3.9+
- Migrated from `setup.py` to `pyproject.toml` build system
- Updated CI/CD to use uv for dependency management
- Replaced flake8 with ruff for linting
- Added black for code formatting
- Updated GitHub Actions workflows to use modern practices
- Publish workflow now uses PyPI Trusted Publishers (OIDC) instead of API tokens
- Updated test matrix to focus on Python 3.12
- Code formatting improvements (line length: 100)

### Removed
- Python 2.7 testing and support
- `setup.py` (replaced by pyproject.toml)
- `requirements.txt`, `requirements_dev.txt`, `requirements_dev27.txt`
- `tox.ini` (CI/CD handles testing)
- `Pipfile` and `Pipfile.lock`
- `MANIFEST.in` (handled by hatchling)
- `.github/workflows/pytest-python2.yml`
- Legacy Python 2 compatibility code

### Fixed
- Ruff linting errors:
  - Replaced `map()` with generator expression
  - Fixed mutable default argument in `_set_time()`
  - Removed outdated Python 2 version check
  - Fixed variable shadowing in tests
  - Removed unused imports

### Development
- Added pre-commit quality checks support
- Improved development workflow documentation
- Added HTML coverage report generation
- Integrated TestIQ for identifying duplicate tests

## [1.3.4] - Previous Release

### Features
- Multi-linguistic ping output parsing support
- TCP ping support
- Support for English, Spanish, French, Afrikaans, Telugu, and Hindi
- JSON output format
- Command-line interface

---

For older versions, please see the git history.
