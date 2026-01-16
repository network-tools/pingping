# Multi Linguistic Ping (pingping)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://github.com/network-tools/pingping/actions/workflows/pytest.yml/badge.svg)](https://github.com/network-tools/pingping)
[![codecov](https://codecov.io/gh/network-tools/pingping/branch/master/graph/badge.svg?token=jNB6BX5az1)](https://codecov.io/gh/network-tools/pingping)
[![Downloads](https://pepy.tech/badge/pingping)](https://pepy.tech/project/pingping)
[![GitHub issues open](https://img.shields.io/github/issues/network-tools/pingping.svg?)](https://github.com/network-tools/pingping/issues)

- [Introduction](#introduction)
- [Docs](#docs)
- [Commands](#commands)
- [Pre-requisites](#pre-requisites)
- [Installation and Downloads](#installation-and-downloads)
- [FAQ](#faq)
- [Other Resources](#other-resources)
- [Bug Tracker and Support](#bug-tracker-and-support)
- [Unit-Tests](#unit-tests)
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

pingping supports **Python 3.8+**. The OS should not matter.

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

- pingping project unit tests are running at [GitHub Actions](https://github.com/network-tools/pingping/actions) via pytest for Python 3.8+.

- The current build status is:

   [![Build Status](https://github.com/network-tools/pingping/actions/workflows/pytest.yml/badge.svg)](https://github.com/network-tools/pingping)

## Development

This project uses modern Python tooling:

- **[uv](https://github.com/astral-sh/uv)** - Fast Python package installer and resolver
- **[ruff](https://github.com/astral-sh/ruff)** - Fast Python linter
- **[black](https://github.com/psf/black)** - Code formatter
- **[pytest](https://pytest.org/)** - Testing framework

To set up a development environment:

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone and set up the project
git clone https://github.com/network-tools/pingping.git
cd pingping
uv sync --all-extras

# Run tests
uv run pytest

# Run linter
uv run ruff check .

# Format code
uv run black .
```

## License and Copyright

- pingping is licensed [MIT](http://opensource.org/licenses/mit-license.php) *2019*

   [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Author and Thanks

pingping was developed by [Kiran Kumar Kotari](https://github.com/kirankotari)
