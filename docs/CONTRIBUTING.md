# Contributing to pingping

Thank you for your interest in contributing to pingping! This document provides guidelines and instructions for contributing to the project.

## Prerequisites

Before you begin, ensure you have the following tools installed:

### Required Tools

- **[uv](https://github.com/astral-sh/uv)** - Fast Python package installer and resolver
  ```bash
  # Install uv (macOS/Linux)
  curl -LsSf https://astral.sh/uv/install.sh | sh
  
  # Or using pip
  pip install uv
  ```

- **Git** - Version control system
- **Python 3.9+** - The project requires Python 3.9 or higher

## Development Setup

### 1. Fork and Clone the Repository

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/pingping.git
cd pingping
```

### 2. Create a Virtual Environment with uv

uv automatically manages virtual environments. Simply sync the project:

```bash
# This will create a virtual environment and install all dependencies
uv sync --all-extras
```

The virtual environment will be created in `.venv/` directory.

### 3. Install Development Dependencies

Development dependencies are already included when you use `--all-extras`:

- **pytest** - Testing framework
- **pytest-cov** - Coverage plugin for pytest
- **ruff** - Fast Python linter
- **black** - Code formatter
- **testiq** - Test quality analysis tool

## Development Workflow

### Running Tests

```bash
# Run all tests with coverage
uv run pytest

# Run tests with verbose output
uv run pytest -v

# Run specific test file
uv run pytest tests/test_ping.py

# Run specific test
uv run pytest tests/test_ping.py::TestPing::test_ping_en
```

### Code Quality Checks

#### Linting with Ruff

```bash
# Check for linting issues
uv run ruff check .

# Auto-fix linting issues
uv run ruff check . --fix
```

#### Code Formatting with Black

```bash
# Check if code is formatted
uv run black --check .

# Format code
uv run black .
```

#### Run All Quality Checks

```bash
# Lint, format, and test in one go
uv run ruff check . --fix && uv run black . && uv run pytest
```

### Test Quality Analysis with TestIQ

TestIQ helps identify duplicate and redundant tests:

#### Generate Coverage Data

```bash
# Generate TestIQ coverage data
uv run pytest --testiq-output=testiq_coverage.json
```

#### Analyze Test Duplicates

```bash
# Analyze for duplicate tests
uv run testiq analyze testiq_coverage.json

# Get test quality score
uv run testiq quality-score testiq_coverage.json

# Run demo to see how it works
uv run testiq demo
```

#### View HTML Coverage Report

```bash
# Generate HTML coverage report
uv run pytest --cov=pingping --cov-report=html

# Open the report in your browser
open htmlcov/index.html
```

#### Generate TestIQ HTML Report

```bash
# Generate TestIQ HTML report with duplicate test analysis
uv run testiq analyze testiq_coverage.json --format html --output testiq_report.html

# Open the report in your browser
open testiq_report.html
```

### Making Changes

1. **Create a new branch** for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** and ensure they follow the project's coding standards

3. **Run tests and quality checks**:
   ```bash
   uv run ruff check . --fix
   uv run black .
   uv run pytest
   ```

4. **Commit your changes** with a clear commit message:
   ```bash
   git add .
   git commit -m "Add: brief description of your changes"
   ```

5. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request** on GitHub

## Commit Message Guidelines

Use clear and descriptive commit messages:

- `Add: new feature or functionality`
- `Fix: bug fix`
- `Update: updates to existing features`
- `Refactor: code refactoring`
- `Docs: documentation changes`
- `Test: test-related changes`

## Code Style Guidelines

- Follow PEP 8 style guide (enforced by ruff and black)
- Line length: 100 characters
- Use type hints where appropriate
- Write descriptive docstrings for functions and classes
- Keep functions focused and concise

## Testing Guidelines

- Write tests for new features
- Ensure all tests pass before submitting PR
- Maintain or improve code coverage
- Use descriptive test names
- Test both success and failure cases

## Adding New Language Support

To add support for a new language's ping output:

1. Create a JSON file in `data/` directory (e.g., `ping_german.json`)
2. Add sample ping outputs in the new language
3. Add corresponding test in `tests/test_ping.py`
4. Run tests to verify parsing works correctly

## Getting Help

- Open an issue on GitHub for bugs or feature requests
- Check existing issues and pull requests first
- Ask questions in issue discussions

## License

By contributing to pingping, you agree that your contributions will be licensed under the MIT License.
