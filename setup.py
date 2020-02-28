from setuptools import setup, find_packages
from os import path
from io import open

try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

here = path.abspath(path.dirname(__file__))
install_reqs = parse_requirements('requirements.txt', session='hack')
reqs = [str(ir.req) for ir in install_reqs]

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
	long_description = f.read()

setup(
	name='pingping',
	version='1.2.1',
	description="pingping is a special library which understands multi linguistic of ping output and translated the result to machine understandable format.",
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	url = 'https://github.com/network-tools/pingping',
	author = 'Kiran Kumar Kotari',
	author_email='kirankotari@live.com',
	entry_points={
          'console_scripts': [
              'pingping = pingping.ping:run'
          ],
      },
    install_requires=reqs,
	classifiers = [ 
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Build Tools',
		'License :: OSI Approved :: MIT License', 
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		],
	keywords = 'ping multi linguistic',
	packages = find_packages(exclude=['tests', 'data', 'asserts']),
)
