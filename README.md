# Multi Linguistic Ping (pingping)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://github.com/network-tools/pingping/actions/workflows/pytest.yml/badge.svg)](https://github.com/network-tools/pingping)
[![Build Status](https://github.com/network-tools/pingping/actions/workflows/pytest-python2.yml/badge.svg)](https://github.com/network-tools/pingping)
[![codecov](https://codecov.io/gh/network-tools/pingping/branch/master/graph/badge.svg?token=jNB6BX5az1)](https://codecov.io/gh/network-tools/pingping)
[![Downloads](https://pepy.tech/badge/pingping)](https://pepy.tech/project/pingping)
[![GitHub issues open](https://img.shields.io/github/issues/network-tools/pingping.svg?)](https://github.com/network-tools/pingping/issues)
[![Known Vulnerabilities](https://snyk.io/test/github/network-tools/pingping/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/network-tools/pingping?targetFile=requirements.txt)

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

pingping supports both trains of **python** `2.7+ and 3.1+`, the OS should not matter.

- shconfparser is used to captured the data.

## Installation and Downloads

The best way to get pingping is with setuptools or pip. If you already have setuptools, you can install as usual:

`python -m pip install pingping`

Otherwise download it from PyPi, extract it and run the `setup.py` script

`python setup.py install`

If you're Interested in the source, you can always pull from the github repo:

- From github `git clone https://github.com/network-tools/pingping.git`

## FAQ

- **Question:** I want to use pingping with Python3, is that safe?  
 **Answer:** As long as you're using python 3.3 or higher, it's safe. I tested every release against python 3.1+, however python 3.1 and 3.2 not running in continuous integration test.  

- **Question:** I want to use pingping with Python2, is that safe?  
 **Answer:** As long as you're using python 2.7 or higher, it's safe. I tested against python 2.7.

## Other Resources

- [Python3 documentation](https://docs.python.org/3/) is a good way to learn python
- Python [GeeksforGeeks](https://www.geeksforgeeks.org/python-programming-language/)
- [JSON](http://json.org/)

## Bug Tracker and Support

- Please report any suggestions, bug reports, or annoyances with pingping through the [Github bug tracker](https://github.com/network-tools/pingping/issues). If you're having problems with general python issues, consider searching for a solution on [Stack Overflow](https://stackoverflow.com/search?q=).
- If you can't find a solution for your problem or need more help, you can [ask a question](https://stackoverflow.com/questions/ask).
- You can also ask on the [Stack Exchange Network Engineering](https://networkengineering.stackexchange.com/) site.

## Unit Tests

- pingping project unit tests are running at [GitHub Actions](https://github.com/network-tools/pingping/actions) via pytest for Python [2.7](https://github.com/network-tools/pingping/actions/workflows/pytest-python2.yml) and [3.x](https://github.com/network-tools/pingping/actions/workflows/pytest.yml).

- The current build status is:

   [![Build Status](https://github.com/network-tools/pingping/actions/workflows/pytest.yml/badge.svg)](https://github.com/network-tools/pingping)
   [![Build Status](https://github.com/network-tools/pingping/actions/workflows/pytest-python2.yml/badge.svg)](https://github.com/network-tools/pingping)

## License and Copyright

- pingping is licensed [MIT](http://opensource.org/licenses/mit-license.php) *2019*

   [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Author and Thanks

pingping was developed by [Kiran Kumar Kotari](https://github.com/kirankotari)
