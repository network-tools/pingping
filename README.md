# Multi Linguistic Ping (pingping)

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/version-1.3.5-blue.svg)](https://github.com/network-tools/pingping)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Test Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)](https://github.com/network-tools/pingping)
[![Tests](https://img.shields.io/badge/tests-35%2F35%20passing-brightgreen.svg)](tests/)
[![Build Status](https://github.com/network-tools/pingping/actions/workflows/ci.yml/badge.svg)](https://github.com/network-tools/pingping/actions)
[![Downloads](https://pepy.tech/badge/pingping)](https://pepy.tech/project/pingping)

## Table of Contents

- [Introduction](#introduction)
- [Docs](#docs)
- [Commands](#commands)
- [Pre-requisites](#pre-requisites)
- [Installation and Downloads](#installation-and-downloads)
- [FAQ](#faq)
- [Other Resources](#other-resources)
- [Bug Tracker and Support](#bug-tracker-and-support)
- [Unit Tests](#unit-tests)
- [Development](#development)
- [Contributing](#contributing)
- [Changelog](#changelog)
- [License and Copyright](#license-and-copyright)
- [Author and Thanks](#author-and-thanks)

## Introduction

pingping is a special library which understands multi linguistic of ping output and translated the result to machine understandable format. i.e. Json

pingping is a vendor independent library where you can parse any language ping output

pingping support tcping which works on transport layer i.e. Ping on proxy server, here ping refers to seding packets via tcp protocol to check the connectivity.

## Docs

**How to use pingping?**

- Command Line  
  Type `pingping <ip-address>` or `pingping <ip-address> --web`. For more help type `pingping -h`

- Python  
  It's very simple, create an object of __Ping__ and call __ping method with ip address__. Internally it calls system ping command and captures the needed result.

**How to run ping command?**

```python
# cli
pingping 192.168.1.1
pingping 1.1.1.1

# python code
obj = Ping()
print(obj.ping('192.168.1.1'))
print(obj.ping('1.1.1.1'))

# python tcping ping 
obj = Ping(command='tcping', layer=4, timeout=3)
print(obj.ping('192.168.1.1'))
print(obj.ping('1.1.1.1'))

```

It returns Json output and easy to understand by the keys of it.

```json
{"ip": "192.168.1.1", "loss_percentage": 100.0}
{"ip": "1.1.1.1", "loss_percentage": 0.0, "min": 55.669, "avg": 78.198, "max": 130.778, "time_in": "ms"}
```

**How to capture result from ping output?**

I am having ping result how to analise the output of it.

```python
Ping.fetch_ping_data(ping_output) # it's a class method.
```

It automatically identifies the ip address and important details from it. It doesn't have any language barier.

```json
{"ip": "1.1.1.1", "loss_percentage": 0.0, "min": 55.669, "avg": 78.198, "max": 130.778, "time_in": "ms"}
```

## Commands

```
Usage pingping  <ip-address>
                -c | --count <Number>
                -l4 | --web | --tcp | --http (ping over proxy)
                -h | --help
```

## Pre-requisites

pingping supports **Python 3.9+**. The OS should not matter.

- shconfparser is used to capture the data.

## Installation and Downloads

The best way to get pingping is with pip or uv:

```bash
pip install pingping
```

Or using uv:

```bash
uv pip install pingping
```

If you're interested in the source, you can always pull from the github repo:

```bash
git clone https://github.com/network-tools/pingping.git
cd pingping
uv sync --all-extras  # Install with dev dependencies
```

## FAQ

- **Question:** What Python versions does pingping support?  
 **Answer:** pingping requires Python 3.8 or higher. All releases are tested against Python 3.8, 3.9, 3.10, 3.11, and 3.12.

## Other Resources

- [Python3 documentation](https://docs.python.org/3/) is a good way to learn python
- Python [GeeksforGeeks](https://www.geeksforgeeks.org/python-programming-language/)
- [JSON](http://json.org/)

## Bug Tracker and Support

- Please report any suggestions, bug reports, or annoyances with pingping through the [Github bug tracker](https://github.com/network-tools/pingping/issues). If you're having problems with general python issues, consider searching for a solution on [Stack Overflow](https://stackoverflow.com/search?q=).
- If you can't find a solution for your problem or need more help, you can [ask a question](https://stackoverflow.com/questions/ask).
- You can also ask on the [Stack Exchange Network Engineering](https://networkengineering.stackexchange.com/) site.

## Unit Tests

- pingping project unit tests are running at [GitHub Actions](https://github.com/network-tools/pingping/actions) via pytest for Python 3.9+.

- The current build status is:

   [![Build Status](https://github.com/network-tools/pingping/actions/workflows/pytest.yml/badge.svg)](https://github.com/network-tools/pingping)

## Development

This project uses modern Python tooling:

- **[uv](https://github.com/astral-sh/uv)** - Fast Python package installer and resolver
- **[ruff](https://github.com/astral-sh/ruff)** - Fast Python linter
- **[black](https://github.com/psf/black)** - Code formatter
- **[pytest](https://pytest.org/)** - Testing framework
- **[testiq](https://github.com/ivanmkc/testiq)** - Test quality analysis tool

### Quick Start

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone and set up the project
git clone https://github.com/network-tools/pingping.git
cd pingping

# Install dependencies
make install

# Run tests
make test

# Run all quality checks (linter, formatter, tests)
make all
```

### Makefile Commands

The project includes a Makefile for common development tasks:

```bash
make help          # Show all available commands
# Run testiq analysis (using Makefile)
make testiq

# Get test quality score
make testiq-score

# Generate HTML report
make testiq-html
open testiq_report.html
```

Or use commands directly:

```bash
# Generate coverage data for TestIQ
uv run pytest --testiq-output=testiq_coverage.json

# Analyze for duplicate tests (skip similarity with threshold 1.0)
uv run testiq analyze testiq_coverage.json --threshold 1.0

# Get test quality score
uv run testiq quality-score testiq_coverage.jsonn all CI checks locally
```

### Test Quality Analysis

Analyze test quality and find duplicates using TestIQ:

```bash
# Generate coverage data for TestIQ
uv run pytest --testiq-output=testiq_coverage.json

# Analyze for duplicate tests (skip similarity with threshold 1.0)
uv run testiq analyze testiq_coverage.json --threshold 1.0

# Get test quality score
uv run testiq quality-score testiq_coverage.json

# Generate HTML report with test duplicates analysis
uv run testiq analyze testiq_coverage.json --threshold 1.0 --format html --output testiq_report.html
open testiq_report.html
```

## Contributing

We welcome contributions! Please see our [Contributing Guide](docs/CONTRIBUTING.md) for detailed information on:

- Setting up your development environment
- Running tests and quality checks
- Code style guidelines
- Submitting pull requests

## Changelog

See [CHANGELOG.md](docs/CHANGELOG.md) for a detailed history of changes to this project.

## License and Copyright

- pingping is licensed [MIT](http://opensource.org/licenses/mit-license.php) *2019*

   [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Author and Thanks

pingping was developed by [Kiran Kumar Kotari](https://github.com/kirankotari)
